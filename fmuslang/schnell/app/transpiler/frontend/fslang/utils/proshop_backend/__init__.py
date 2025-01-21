from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
	transform_table,
)
from app.stringutils import tabify_content, tabify_contentlist, tabify_contentlist_tab
from app.treeutils import tables_from_rootnode
from app.usutils import tab, tab_tab
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
from app.appconfig import libpohon_data
from app.libpohon import get_import
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
		self.provider = 'django'
		self.hasil_columnify = columnify(self.tables, self.provider)
		# hasil_transform = transform_columns(tablename, tables_with_columns=hasil_columnify, provider=provider)

	def transform_table(self, tablename_case):
		return transform_columns(tablename_case, tables_with_columns=self.hasil_columnify, provider=self.provider)

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
		# from app.utils import salin_objek
		TIMESTAMPED_BASE_MODEL = 'TimestampedModel'
		DEFAULT_BASE_MODEL = 'models.Model'
		TIMESTAMP_IMPORT = 'from main.helpers import TimestampedModel'

		template_node_app_content = app_content_tab(self.tables, self.node_app_content)
		template_node_app_content = tabify_content(template_node_app_content, self_tab=tab_tab(), num_tab=2)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_CONTENT', template_node_app_content)

		# import json
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

			header = f'/apps/{tablename}/urls.py'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_urls.tpl')))
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/apps/{tablename}/views.py'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_views.tpl')))
			# __TEMPLATE_FIELD_ASSIGNMENT_FOR_UPDATE
			# product.field4 = data['field4']
			assignments = [f"{tablename_lower}.{col.label} = data['{col.label}']" for col in tbl.children if (col.label != 'id' and col.label != '_id')]
			assignments = tabify_contentlist(assignments)
			per_table = per_table.replace('__TEMPLATE_FIELD_ASSIGNMENT_FOR_UPDATE', assignments)
			# __TEMPLATE_ORDERING_FIELD
			per_table = per_table.replace('__TEMPLATE_ORDERING_FIELD', ordering_field)
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/apps/{tablename}/admin.py'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_admin.tpl')))
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/apps/{tablename}/apps.py'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_apps.tpl')))
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/apps/{tablename}/serializers.py'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_serializers.tpl')))
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

			header = f'/apps/{tablename}/models.py'
			per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_models.tpl')))
			generated_fields = columnify_and_transform(self.tables, self.provider, tablename)
			generated_fields = tabify_content(generated_fields, self_tab=tab_tab(), num_tab=1)

			# libpohon_data harus setelah "columnify", krn dia yg ngisi data libpohon_data
			basemodel = TIMESTAMPED_BASE_MODEL if hasattr(tbl, 'timestamp') else DEFAULT_BASE_MODEL
			# print(f"""
			# 	{json.dumps(libpohon_data['import_part_by_table'], indent=2)}
			# """)
			# import_part = salin_objek(libpohon_data['import_part_by_table'][tablename])
			import_part = get_import(tablename)
			if hasattr(tbl, 'timestamp'): # {@User=#5,ts}
				basemodel =  TIMESTAMPED_BASE_MODEL
				import_part.append(TIMESTAMP_IMPORT)
			else:
				basemodel =  DEFAULT_BASE_MODEL

			per_table = per_table.replace('__TABLE_FIELDS__', generated_fields)
			per_table = per_table.replace('__FIRST_FIELD__', first_column)
			per_table = per_table.replace('__TABLE_BASEMODEL__', basemodel)
			per_table = per_table.replace('__MODEL_IMPORTS__', '\n'.join(import_part))

			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)

		# __TEMPLATE_INSTALLED_APPS__
		# skip user krn sudah kita masukkan secara default
		installed_apps = [f"'apps.{item.model.lower()}'" for item in self.tables if item.model.lower()!='user']
		installed_apps = tabify_contentlist(installed_apps, self_tab=tab_tab(), delim=',\n') + ','
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_INSTALLED_APPS__', installed_apps)

		# __TEMPLATE_APP_URLS__
		apps_urls = [f"path('api/', include('apps.{item.model.lower()}.urls'))" for item in self.tables]
		apps_urls = tabify_contentlist(apps_urls, self_tab=tab_tab(), delim=',\n') + ','
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_URLS__', apps_urls)


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

	def handle_user_model(self):
		"""
		columnify(tables, provider='django', skip_columns=[])
		transform_table(tablename_case, hasil_columnify, provider)
		"""

		additional_user_columns = ''
		usermk_output = joiner(get_cwd(), 'user.mk')
		usermk_input = joiner(disini, 'user-input.mk')
		usermk_input_content = file_content(usermk_input)

		table_user = 'User'
		skip_user_columns = {
			table_user: [
				'username',
				'name',
				'first_name',
				'last_name',
				'email',
				'phone',
				'is_active',
				'is_staff',
				'roles',
			]
		}

		columnify_all = columnify(self.tables, self.provider, skip_user_columns)
		if table_user in columnify_all:

			names = columnify_all[table_user]['columns_names']
			jenis = columnify_all[table_user]['columns_types']
			attrs = columnify_all[table_user]['columns_attributes']

			TIMESTAMPED_BASE_MODEL = 'TimestampedModel'
			DEFAULT_BASE_MODEL = 'models.Model'
			attrs = [', '.join(item) for item in attrs]
			# delim = ','
			res = [f'{names[index].ljust(15)} = {jenis[index]}({item})' for index, item in enumerate(attrs)]
			cols = sorted(res)
			additional_user_columns = tabify_contentlist_tab(cols, num_tab=1, delim='\n')

		usermk_input_content = usermk_input_content.replace('__TEMPLATE_ADDITIONAL_USER_COLUMNS_', additional_user_columns)
		file_write(usermk_output, usermk_input_content)

	def generate(self):
		self.mkfile()
		self.model()
		self.handle_user_model()
		self.save_file()
		print('selesai generate backend')
