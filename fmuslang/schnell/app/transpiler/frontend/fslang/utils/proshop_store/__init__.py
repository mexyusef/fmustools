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
		self.tables = tables_from_rootnode(self.root)
		self.project_dir = project_dir
		self.mkfile_input = joiner(disini, 'index-input.mk')
		self.mkfile_output = joiner(get_cwd(), 'proshop_store.mk')
		self.mkfile_input_content = file_content(self.mkfile_input)
		self.node_app_content = file_content(joiner(disini, 'templates/app_content_template.tpl'))

	def output(self):
		return self.mkfile_output

	def change_projectdir(self):
		self.mkfile_input_content = self.mkfile_input_content.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', self.project_dir)

	def db_init(self):
		from app.libpohon.db_init import db_init
		template_db_init = db_init(self.root)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_DB_INIT', template_db_init)

	def app_init(self):
		from app.libpohon.app_init import app_init
		template_app_init = app_init(self.tables)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)
		self.mkfile_input_content = self.mkfile_input_content.replace('__NILAI_SERVER_PORT__', self.root.serverport)

	def app_content(self):
		from app.libpohon.app_content import app_content_tab
		from app.libpohon.app_content_model import app_content_model_tab as app_content_model
		# mk structure in index/fmus
		appcontentlines = app_content_tab(self.tables, self.node_app_content)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_CONTENT', appcontentlines)

		# actions.js, constants.js, reducers.js
		self.file_actions_content = file_content(joiner(disini, 'templates/app_actions.tpl'))
		self.file_constants_content = file_content(joiner(disini, 'templates/app_constants.tpl'))
		self.file_reducers_content = file_content(joiner(disini, 'templates/app_reducers.tpl'))
		for index, tbl in enumerate(self.tables,1):
			tablename = tbl.model
			tablename_lower = tbl.model.lower()
			actions_content = app_content_model(tablename, self.file_actions_content)
			actions_header = f'/tmp/rework/store/{tablename_lower}/{tablename_lower}Actions.js'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, actions_header, actions_content)

			constants_content = app_content_model(tablename, self.file_constants_content)
			constants_header = f'/tmp/rework/store/{tablename_lower}/{tablename_lower}Constants.js'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, constants_header, constants_content)

			reducers_content = app_content_model(tablename, self.file_reducers_content)
			reducers_header = f'/tmp/rework/store/{tablename_lower}/{tablename_lower}Reducers.js'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, reducers_header, reducers_content)

		# config.js
		file_path_config_content = file_content(joiner(disini, 'templates/app_path_config.tpl'))
		file_config_content = file_content(joiner(disini, 'templates/app_config.js.tpl'))
		all_table_content = []
		for index, tbl in enumerate(self.tables,1):
			tablename = tbl.model
			# tablename_lower = tbl.model.lower()
			per_table = app_content_model(tablename, file_path_config_content)
			all_table_content.append(per_table + '\n\n')
		all_table_contents = '\n'.join(all_table_content)
		file_config_content = file_config_content.replace('__TEMPLATE_APP_CONFIG', all_table_contents)
		file_config_header = '/tmp/rework/store/config.js'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, file_config_header, file_config_content)
		# store/index.js
		file_store_import_content = file_content(joiner(disini, 'templates/app_store_import.tpl'))
		file_store_reducer_content = file_content(joiner(disini, 'templates/app_store_reducer.tpl'))
		file_storejs_content = file_content(joiner(disini, 'templates/app_store.js.tpl'))
		store_imports = app_content_tab(self.tables, file_store_import_content)
		store_reducers = app_content_tab(self.tables, file_store_reducer_content)
		file_storejs_content = file_storejs_content.replace('__TEMPLATE_APP_STORE_IMPORTS', store_imports)
		file_storejs_content = file_storejs_content.replace('__TEMPLATE_APP_STORE_REDUCERS', store_reducers)
		file_store_header = '/tmp/rework/store/index.js'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, file_store_header, file_storejs_content)

	def mkfile(self):
		self.change_projectdir()
		self.db_init()
		self.app_init()
		self.app_content()
		print('hasil mkfile:', self.mkfile_output)

	def model(self):
		print('hasil model:', self.mkfile_output)

	def save_file(self):
		file_write(self.mkfile_output, self.mkfile_input_content)
		print('hasil save file:', self.mkfile_output)

	def generate(self):
		self.mkfile()
		self.model()
		self.save_file()
		print('selesai generate springboot')
