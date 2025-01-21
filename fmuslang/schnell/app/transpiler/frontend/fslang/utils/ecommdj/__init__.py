from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)
from app.stringutils import tabify_content, tabify_contentlist
from app.treeutils import tables_from_rootnode
from app.usutils import tab
from app.fileutils import (
	file_content,
	append_entry_tostring,
	# append_entry_tofile,
	file_write,
)
from app.dirutils import (
	get_cwd, 
	joiner, 
	here,
)
from app.fileutils import get_definition_by_key_permissive_start
from app.fmus import Fmus


disini = here(__file__)


class Coordinator:

	def __init__(self, RootNode, project_dir='__INPUT__'):
		self.root = RootNode
		# self.tables = tables_from_rootnode(self.root)
		self.project_dir = project_dir
		self.mkfile_input = joiner(disini, 'index-input.mk')
		self.mkfile_output = joiner(get_cwd(), 'index.mk')
		self.mkfile_input_content = file_content(self.mkfile_input)
		self.node_app_content = '' # file_content(joiner(disini, 'appcontent.tpl'))

	def output(self):
		return self.mkfile_output

	def change_projectdir(self):
		self.mkfile_input_content = self.mkfile_input_content.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', self.project_dir)

	def db_init(self):
		from app.libpohon.db_init import db_init
		# template_db_init = db_init(self.root)
		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_DB_INIT', template_db_init)

	def app_init(self):
		from app.libpohon.app_init import app_init
		# template_app_init = app_init(self.tables)
		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)

	def app_content(self):
		from app.libpohon.app_content import app_content
		# template_node_app_content = app_content(self.tables, self.node_app_content)
		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)

	def mkfile(self):
		self.change_projectdir()
		self.db_init()
		self.app_init()
		self.app_content()
		print('hasil mkfile:', self.mkfile_output)

	def model(self):
		from app.fileutils import get_definition_by_key_permissive_start
		from app.fmus import Fmus

		fmus = Fmus(False)
		baris_entry = 'index/fmus'

		# bukannya gak perlu process fmus  di sini?
		# krn sudah otomatis dilakukan dari index-input.mk nya ecommdj
		# yg penting index.mk sudah tercipta di backend, routes, store
		from ..proshop_backend import Coordinator as backend
		BE = backend(self.root)
		BE.generate()
		# filepath = BE.output()
		# program = get_definition_by_key_permissive_start(filepath, baris_entry)		
		# fmus.set_file_dir_template(filepath)
		# fmus.process(program)

		from ..proshop_routes import Coordinator as FE_routes
		FE = FE_routes(self.root)
		FE.generate()
		# filepath = FE.output()
		# program = get_definition_by_key_permissive_start(filepath, baris_entry)		
		# fmus.set_file_dir_template(filepath)
		# fmus.process(program)

		from ..proshop_store import Coordinator as FE_store
		FE = FE_store(self.root)
		FE.generate()
		# filepath = FE.output()
		# program = get_definition_by_key_permissive_start(filepath, baris_entry)
		# fmus.set_file_dir_template(filepath)
		# fmus.process(program)

		print('hasil model:', self.mkfile_output)

	def save_file(self):
		file_write(self.mkfile_output, self.mkfile_input_content)
		print('hasil save file:', self.mkfile_output)

	def generate(self):
		self.mkfile()
		self.model()
		self.save_file()
		print('selesai generate springboot')
