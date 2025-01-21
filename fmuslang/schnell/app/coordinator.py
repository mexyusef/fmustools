# yg dinanti2
# base utk coordinator..

from schnell.app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)
from schnell.app.stringutils import (
	tabify_content,
	tabify_content_space,
	tabify_content_tab,
	tabify_contentlist,
	tabify_contentlist_tab,
	tabify_contentlist_space,
	tab_tab, tab_space2, tab_space4
)
from schnell.app.treeutils import tables_from_rootnode, ispohon, istoken, anak, data
from schnell.app.usutils import tab
from schnell.app.fileutils import (
	file_content,
	append_entry_tostring,
	# append_entry_tofile,
	file_write,
)
from schnell.app.dirutils import (
	dirname,
	joiner,
	here,
	isabsolute,
	files_filter, # files_filter(dirpath, extension=[])
)
from schnell.app.fileutils import get_definition_by_key_permissive_start
from schnell.app.printutils import indah4
from schnell.app.utils import env_int


class BaseCoordinator:

	def __init__(self,
		RootNode,
		project_dir='__INPUT__',
		provider='django',
		filename_input='index-input.mk',
		filename_output='output.fmus',
		disini=here(__file__),
		disini_output=here(__file__),
		baris_output_index='index/fmus',
		app_content_templatefile='',
		tab_mode='space4'):
		self.root = RootNode
		# RootNode bisa lark.tree.Tree (punya attr data), lark.lexer.Token, atau AnyNode
		if ispohon(RootNode) and data(RootNode) == 'quick_statement':
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				print('[app.coordinator] rootnode adlh token (skipping):', RootNode, type(RootNode))
			self.tables = None
		else:
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				print('[app.coordinator] rootnode adlh pohon:', RootNode, type(RootNode))
			self.tables = tables_from_rootnode(self.root)

		self.tab_mode = tab_mode # tab, space2, space4
		
		self.tab = tab_tab
		if self.tab_mode == 'space2':
			self.tab = tab_space2
		elif self.tab_mode == 'space4':
			self.tab = tab_space4

		self.project_dir = project_dir
		self.requested_filename = filename_input
		self.mkfile_input = joiner(disini, self.requested_filename)

		# lokasi_untuk_output = disini
		# if dirname(self.mkfile_input) != disini:
		# 	lokasi_untuk_output = dirname(self.mkfile_input)
		self.mkfile_output = joiner(disini_output, filename_output)

		# self.mkfile_output = filename_output
		# if not isabsolute(filename_output):
		# 	self.mkfile_output = joiner(disini, self.mkfile_output)

		self.mkfile_input_content = file_content(self.mkfile_input)
		# kita bolehkan input content berisi TAB(1) utk atasi permasalah tab/space yg ribet
		# cek jk pengisian mkfile_input_content dioverride di children!
		self.mkfile_input_content = self.mkfile_input_content \
			.replace('__TAB(9)', self.tab*9) \
			.replace('__TAB(8)', self.tab*8) \
			.replace('__TAB(7)', self.tab*7) \
			.replace('__TAB(6)', self.tab*6) \
			.replace('__TAB(5)', self.tab*5) \
			.replace('__TAB(4)', self.tab*4) \
			.replace('__TAB(3)', self.tab*3) \
			.replace('__TAB(2)', self.tab*2) \
			.replace('__TAB(1)', self.tab*1)

		# default '' utk app content template, berisi __TABLENAME__, __TABLENAME_UPPER__, __TABLENAME_CASE__, dst
		self.app_content_templatefile = app_content_templatefile # file_content(joiner(disini, 'appcontent.tpl'))
		if app_content_templatefile:
			if not isabsolute(app_content_templatefile):
				app_content_templatefile = joiner(disini, app_content_templatefile)
			self.app_content_templatefile = file_content(app_content_templatefile)
		self.provider = provider
		self.baris_output_index = baris_output_index

	def baris_output(self):
		return self.baris_output_index

	def output(self):
		return self.mkfile_output

	def change_projectdir(self):
		self.mkfile_input_content = self.mkfile_input_content.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', self.project_dir)

	def db_init(self):
		if not self.tables:
			return
		from schnell.app.libpohon.db_init import db_init
		template_db_init = db_init(self.root, self.tab_mode)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_DB_INIT', template_db_init)

	def app_init(self):
		if not self.tables:
			return
		from schnell.app.libpohon.app_init import app_init
		template_app_init = app_init(self.tables)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)
		if hasattr(self.root, 'serverport'):
			self.mkfile_input_content = self.mkfile_input_content.replace('__NILAI_SERVER_PORT__', self.root.serverport)
		if hasattr(self.root, 'clientport'):
			self.mkfile_input_content = self.mkfile_input_content.replace('__NILAI_CLIENT_PORT__', self.root.clientport)

	def app_content(self, app_content_code='__TEMPLATE_SERVER_APP_CONTENT', tab_indent=0):
		"""
		ada __TEMPLATE_SERVER_APP_CONTENT
		dan dulunya __TEMPLATE_APP_CONTENT
		shg kita parameterized ke app_content_code

		tab_indent utk meminta indent tab sesuai tab_mode, krn app content sudah pasti akan butuh di-indent
		"""
		if not self.tables:
			return
		from schnell.app.libpohon.app_content import app_content
		# def app_content(tables, app_content_argument, tab=tab_space, provider='django'):

		template_app_content_templatefile = app_content(self.tables, self.app_content_templatefile, tab=self.tab)
		if tab_indent:
			if self.tab_mode == 'tab':
				template_app_content_templatefile = tabify_content_tab(template_app_content_templatefile, num_tab=tab_indent)
			elif self.tab_mode == 'space2':
				# input(f'app_content, tabmode space2 adlh {self.tab_mode}, tab_indent={tab_indent}...input adlh [{template_app_content_templatefile}] ')
				template_app_content_templatefile = tabify_content_space(template_app_content_templatefile, num_tab=tab_indent, space_size=2)
				# input(f'app_content, tabmode space2 adlh {self.tab_mode}, tab_indent={tab_indent}...hasil adlh [{template_app_content_templatefile}] ')
			elif self.tab_mode == 'space4':
				template_app_content_templatefile = tabify_content_space(template_app_content_templatefile, num_tab=tab_indent, space_size=4)
		self.mkfile_input_content = self.mkfile_input_content.replace(app_content_code, template_app_content_templatefile)

	def default_dbvalues(self):
		self.dbuser = 'usef'
		self.dbpass = 'rahasia'
		self.dbname = 'hapus'
		self.dbhost = 'localhost'
		self.dbport = 5432
		self.dbdialect = 'postgresql' # hrs valid utl alamat flyway
		if hasattr(self.root, 'dbname'):
			self.dbname = self.root.dbname
		if hasattr(self.root, 'username'):
			self.dbuser = self.root.username
		if hasattr(self.root, 'password'):
			self.dbpass = self.root.password
		if hasattr(self.root, 'host'):
			self.dbhost = self.root.host
		if hasattr(self.root, 'port'):
			self.dbport = self.root.port

	def mkfile(self):
		self.change_projectdir()
		self.default_dbvalues()
		self.db_init()
		self.app_init()
		self.app_content()
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('[app.coordinator] hasil mkfile:', self.mkfile_output)

	def model(self):
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('[app.coordinator] hasil model:', self.mkfile_output)

		# __REPLACE_WITH_PERTABLE_CRUD__ perlu diganti, dari baris-entry "per_table" dlm file yg sama, self.requested_filename
		if '__REPLACE_WITH_PERTABLE_CRUD__' in self.mkfile_input_content:
			content = get_definition_by_key_permissive_start(self.mkfile_input, 'per_table')
			if content:
				from schnell.app.libpohon.app_content import app_content_tab
				# sementara paksa utk fastapi dulu...harus ada pemetaan file fmus dan provider
				alltables_content = app_content_tab(self.tables, content, provider=self.provider)
				self.mkfile_input_content = self.mkfile_input_content.replace('__REPLACE_WITH_PERTABLE_CRUD__', alltables_content)

		# __TEMPLATE_ALL_POSTS
		# pagesdir = joiner(ayah(__file__,1), 'pages')
		# mdfiles = files_filter(pagesdir, ['.md'], only_filename=True)
		# mkentries_indexfmus = []
		# for file in mdfiles:
		# 	# index.md,f(e=utama=C:/work/tmp/tmp/nextjs-portfolio-starter/pages/posts/index.md)
		# 	indexentry = f"{file},f(e=__FILE__=/pages/{file})"
		# 	mkentries_indexfmus.append(indexentry)
		# 	header = f'/pages/{file}'
		# 	body = file_content(joiner(pagesdir, file))
		# 	self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, body)
		# mkentries = tabify_contentlist_space(mkentries_indexfmus, num_tab=3)
		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_ALL_POSTS', mkentries)


	def save_file(self):
		file_write(self.mkfile_output, self.mkfile_input_content)
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('[app.coordinator] hasil save file:', self.mkfile_output)

	def before_mkfile(self):
		pass
	def between_mkfile_model(self):
		pass
	def after_model(self):
		pass

	def generate(self):
		self.before_mkfile()
		self.mkfile()
		self.between_mkfile_model()
		self.model()
		self.after_model()
		self.save_file()
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('[app.coordinator] selesai generate!')
