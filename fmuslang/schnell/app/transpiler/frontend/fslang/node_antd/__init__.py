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
from app.envvalues import datadir
from .antd_helper import AntdModel
from .node_helper import NodeModel


disini = here(__file__)

class Coordinator:


	def __init__(self, RootNode, project_dir='__INPUT__'):
		self.root = RootNode
		self.tables = tables_from_rootnode(self.root)
		self.project_dir = project_dir
		self.mkfile_input = joiner(disini, 'index-input.mk')
		# self.mkfile_output = joiner(disini, 'index.mk')
		self.mkfile_output = joiner(get_cwd(), 'node_antd_backend_output.mk')
		self.mkfile_input_content = file_content(self.mkfile_input)
		self.node_app_content = file_content(joiner(disini, 'node/app_content.tpl'))
		self.antd_asset_json = file_content(joiner(disini, 'antd/asset_json.tpl'))
		self.antd_asset_json_content = file_content(joiner(disini, 'antd/asset_json_content.tpl'))
		self.antd_app_content = file_content(joiner(disini, 'antd/app_content.tpl'))    
		self.node_model = file_content(joiner(disini, 'node/sequelize_model.tpl'))
		self.hasil_columnify = columnify(self.tables, 'node_antd')
		# self.configuration_style = {
		#   'models': {}
		# }
		
		self.configuration = {
			'table_nodes': self.tables,
			'root_node': self.root,
			'models': {},
		}
		self.set_configuration_models()


	def set_configuration_models(self):
		for table in self.tables:
			tablename = table.model
			dapatkan = self.hasil_columnify[tablename]
			names = dapatkan['columns_names']
			jenis = dapatkan['columns_types_original']
			self.configuration['models'][tablename] = [{'name':nama, 'type':jenis[idx]} for idx,nama in enumerate(names)]


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


	def app_content(self):
		from app.libpohon.app_content import app_content
		template_node_app_content = app_content(self.tables, self.node_app_content)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)
		template_asset_json = app_content(self.tables, self.antd_asset_json)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_CLIENT_JSON_MODEL', template_asset_json)
		template_antd_app_content = app_content(self.tables, self.antd_app_content)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_CLIENT_APP_CONTENT', template_antd_app_content)


	def mkfile(self):
		self.change_projectdir()
		self.db_init()
		self.app_init()
		self.app_content()


	def app_model(self):
		"""
		backend: model/sequelize
		"""
		from app.libpohon.app_content_model import app_content
		
		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)

		for meja in self.tables:
			tablename = meja.model
			template_node_app_content = app_content(tablename, self.node_model)
			generated_fields = columnify_and_transform(self.tables, 'node_antd', tablename)
			per_table = template_node_app_content.replace('__FIELDS__', generated_fields)
			per_table = per_table.replace('__TABLENAME__', tablename)
			per_table = per_table.replace('__TABLENAME_LOWER__', tablename.lower())
			per_table = per_table.replace('__TABLENAME_UPPER__', tablename.upper())
			per_table = per_table.replace('__TABLENAME_LOWER_PLURAL__', tablename.lower() + 's')
			per_table = per_table.replace('__TABLENAME_UPPER_PLURAL__', tablename.upper() + 's')
			per_table = per_table.replace('__TABLENAME_CAP_PLURAL__', tablename.capitalize() + 's')
			per_table = per_table.replace('__TAB(1)', tab(1))
			per_table = per_table.replace('__TAB(2)', tab(2))
			per_table = per_table.replace('__TAB(3)', tab(3))
			per_table = per_table.replace('__TAB(4)', tab(4))
			per_table = per_table.replace('__TAB(5)', tab(5))
			per_table = per_table.replace('__TAB(6)', tab(6))
			per_table = per_table.replace('__TAB(7)', tab(7))
			per_table = per_table.replace('__TAB(8)', tab(8))
			per_table = per_table.replace('__TAB(9)', tab(9))
			per_table = per_table.replace('__TAB', tab(1))
			header = f'/np/node-postgres/src/apps/{tablename.lower()}/models/postgres.js'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)


	def app_json(self):
		"""
		frontend: isi json utk kolom table
		"""  
		for meja in self.tables:
			tablename = meja.model
			dapatkan = self.hasil_columnify[tablename]
			names = dapatkan['columns_names']
			jenis = dapatkan['columns_types']
			attrs = dapatkan['columns_attributes']
			# utk jadi json hrs apit "" dan skip utk id
			names = [f'"{item}"' for item in names if item != 'id']
			pengganti = tabify_contentlist(names, num_tab=2, aslist=True)
			pengganti = ',\n'.join(pengganti) + ',\n'
			per_table = self.antd_asset_json_content.replace('__TEMPLATE_APP_ASSET_JSON', pengganti)
			header = f'/np/react-antd/assets/{tablename.lower()}.json'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)


	def model(self):
		self.app_model()
		self.app_json()
		# gen_models_reactantd_antd
		# generate_react_component
		antd = AntdModel(self.configuration, self.mkfile_input_content)
		antd.generate_react_component()
		antd.generate_menu_json()
		antd.generate_app_routes()
		self.mkfile_input_content = antd.latest()

		node = NodeModel(self.root, self.tables, self.mkfile_input_content)
		node.gen_apps_index()
		self.mkfile_input_content = node.latest()


	def save_file(self):
		file_write(self.mkfile_output, self.mkfile_input_content)
		print('hasil save file:', self.mkfile_output)


	def generate(self):
		self.mkfile()
		self.model()
		self.save_file()
		print('selesai generate node_antd')


	def output(self):
		return self.mkfile_output
