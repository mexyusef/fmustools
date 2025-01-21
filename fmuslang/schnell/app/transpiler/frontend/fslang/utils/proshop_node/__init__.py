from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)
from app.stringutils import tabify_content, tabify_contentlist, tabify_content_tab
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
		self.mkfile_output = joiner(get_cwd(), 'index.mk')
		self.mkfile_input_content = file_content(self.mkfile_input)
		self.node_app_content = file_content(joiner(disini, 'app_content.tpl'))
		self.provider = 'proshop_mongo'

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
		from app.libpohon.app_content_model import app_content_model_tab
		template_node_app_content = app_content_tab(self.tables, self.node_app_content)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)

		for index, tbl in enumerate(self.tables,1):
			tablename = tbl.model
			tablename_lower = tablename.lower()
			first_column = tbl.children[0].label

			ordering_field = first_column
			labels = [col.label for col in tbl.children]
			if 'created_at' in labels:
				ordering_field = 'created_at'
			elif 'createdAt' in labels:
				ordering_field = 'createdAt'

			header = f'/np/node-mongodb/src/apps/{tablename_lower}/model.js'
			generated_fields_trx = columnify_and_transform(self.tables, self.provider, tablename)
			args_fields = generated_fields_trx # tabify_content_tab(generated_fields_trx, num_tab=1)
			# hasil_columnify = columnify(self.tables, self.provider)

			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_model.tpl')))
			per_table = per_table.replace('__TABLE_FIELDS__', args_fields)
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/np/node-mongodb/src/apps/{tablename_lower}/controller.js'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_controller.tpl')))
			# __TABLE_FIELDS__
			# __FIELDS_UPDATE_ASSIGNMENT__
			# "      orderItems,"
			# "    product.name = name"
			skips = ['id', '_id']
			assignment = '\n'.join([f"{tablename_lower}.{item.label} = {item.label}" for item in tbl.children if item.label not in skips])
			assignment = tabify_content_tab(assignment, num_tab=2)
			args_fields = ',\n'.join([f"{item.label}" for item in tbl.children if item.label not in skips])
			args_fields = tabify_content_tab(args_fields, num_tab=2)
			per_table = per_table.replace('__TABLE_FIELDS__', '{\n' + args_fields + '\n\t}')
			per_table = per_table.replace('__FIELDS_UPDATE_ASSIGNMENT__', assignment)
			
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/np/node-mongodb/src/apps/{tablename_lower}/route.js'
			# __CREATE_MIDDLEWARE_OR_NONE__
			# __LIST_MIDDLEWARE_OR_NONE__
			# __DETAIL_MIDDLEWARE_OR_NONE__
			# __UPDATE_MIDDLEWARE_OR_NONE__
			# __DELETE_MIDDLEWARE_OR_NONE__
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_route.tpl')))
			per_table = per_table.replace('__CREATE_MIDDLEWARE_OR_NONE__', '')
			per_table = per_table.replace('__LIST_MIDDLEWARE_OR_NONE__', '')
			per_table = per_table.replace('__DETAIL_MIDDLEWARE_OR_NONE__', '')
			per_table = per_table.replace('__UPDATE_MIDDLEWARE_OR_NONE__', '')
			per_table = per_table.replace('__DELETE_MIDDLEWARE_OR_NONE__', '')
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

		server_imports = [f"import {tbl.model.lower()}Routes from './apps/{tbl.model.lower()}/route.js'" for tbl in self.tables]
		server_imports = '\n'.join(server_imports)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_SERVER_IMPORTS', server_imports)
		server_uses = [f"app.use('/api/{tbl.model.lower()}s', {tbl.model.lower()}Routes)" for tbl in self.tables]
		server_uses = '\n'.join(server_uses)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_SERVER_USES', server_uses)
		seeder_imports = [f"import {tbl.model} from './apps/{tbl.model.lower()}/model.js'" for tbl in self.tables]
		seeder_imports = '\n'.join(seeder_imports)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SEEDER_IMPORTS', seeder_imports)
		# await Order.deleteMany()
		# __TEMPLATE_DELETE_NON_PRODUCT_USER
		skips = ['Product', 'User']
		seeder_deletelist = [f"await {tbl.model}.deleteMany()" for tbl in self.tables if tbl.model not in skips]
		seeder_deletelist = '\n'.join(seeder_deletelist)
		seeder_deletelist = tabify_content_tab(seeder_deletelist, num_tab=2)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_DELETE_NON_PRODUCT_USER', seeder_deletelist)

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
