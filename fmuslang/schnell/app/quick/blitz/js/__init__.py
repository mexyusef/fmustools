from app.utils import env_int
# from app.printutils import indah4
from app.treeutils import tables_from_rootnode, ispohon, istoken, anak, data
from app.usutils import tab
from app.fileutils import (
	file_content,
	append_entry_tostring,
	# append_entry_tofile,
	file_write,
)
from app.dirutils import (
	ayah, 
	joiner, 
	here,
	basename, dirname,
	files_filter, # files_filter(dirpath, extension=[])
)
from app.fileutils import get_definition_by_key_permissive_start
from app.fmus import Fmus


disini = here(__file__)


class Coordinator:

	def __init__(self, RootNode, filename, project_dir='__INPUT__'):
		self.root = RootNode
		# RootNode bisa lark.tree.Tree (punya attr data), lark.lexer.Token, atau AnyNode
		if ispohon(RootNode) and data(RootNode) == 'quick_statement':
			print('[coordinator] rootnode adlh token (skipping):', RootNode, type(RootNode))
			self.tables = None
		else:
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				print('[coordinator] rootnode adlh pohon:', RootNode, type(RootNode))
			self.tables = tables_from_rootnode(self.root)

		self.project_dir = project_dir
		self.mkfile_input = joiner(disini, filename)
		lokasi_untuk_output = disini
		if dirname(self.mkfile_input) != disini:
			lokasi_untuk_output = dirname(self.mkfile_input)
		self.mkfile_output = joiner(lokasi_untuk_output, 'output.fmus')

		self.mkfile_input_content = file_content(self.mkfile_input)
		self.node_app_content = '' # file_content(joiner(disini, 'appcontent.tpl'))

	def output(self):
		return self.mkfile_output

	def change_projectdir(self):
		self.mkfile_input_content = self.mkfile_input_content.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', self.project_dir)

	def db_init(self):
		if not self.tables:
			return
		from app.libpohon.db_init import db_init
		template_db_init = db_init(self.root)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_DB_INIT', template_db_init)

	def app_init(self):
		if not self.tables:
			return
		from app.libpohon.app_init import app_init
		template_app_init = app_init(self.tables)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)
		self.mkfile_input_content = self.mkfile_input_content.replace('__NILAI_SERVER_PORT__', self.root.serverport)
		self.mkfile_input_content = self.mkfile_input_content.replace('__NILAI_CLIENT_PORT__', self.root.clientport)

	def app_content(self):
		if not self.tables:
			return
		from app.libpohon.app_content import app_content
		template_node_app_content = app_content(self.tables, self.node_app_content)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)

	def mkfile(self):
		self.change_projectdir()
		self.db_init()
		self.app_init()
		self.app_content()
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('hasil mkfile:', self.mkfile_output)

	def model(self):
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('hasil model:', self.mkfile_output)

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
			print('hasil save file:', self.mkfile_output)

	def generate(self):
		self.mkfile()
		self.model()
		self.save_file()
		# print('selesai generate!')
