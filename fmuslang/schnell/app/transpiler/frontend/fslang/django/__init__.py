from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)
from app.envvalues import datadir
from app.libpohon.record import Record
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
# from .antd_helper import AntdModel
# from .node_helper import NodeModel

from app.appconfig import libpohon_data

disini = here(__file__)

default_user_mk_entry = """
    user,d(/mk)
      signals.py,f(e=utama=/django-starter1/apps/user/signals.py)
      __init__.py,f(e=utama=/django-starter1/apps/user/__init__.py)
      renderers.py,f(e=utama=/django-starter1/apps/user/renderers.py)
      admin.py,f(e=utama=/django-starter1/apps/user/admin.py)
      views.py,f(e=utama=/django-starter1/apps/user/views.py)
      urls.py,f(e=utama=/django-starter1/apps/user/urls.py)
      backends.py,f(e=utama=/django-starter1/apps/user/backends.py)
      serializers.py,f(e=utama=/django-starter1/apps/user/serializers.py)
      models.py,f(e=utama=/django-starter1/apps/user/models.py)
"""

class Coordinator:


	def __init__(self, RootNode, project_dir='__INPUT__'):
		self.root = RootNode
		self.tables = tables_from_rootnode(self.root)
		self.project_dir = project_dir
		self.mkfile_input = joiner(disini, 'index-input.mk')
		# self.mkfile_output = joiner(disini, 'index.mk')
		self.mkfile_output = joiner(get_cwd(), 'django_backend_output.mk')
		self.mkfile_input_content = file_content(self.mkfile_input)

		self.django_model = file_content(joiner(disini, 'templates/django_model.tpl'))
		self.django_websocket = file_content(joiner(disini, 'templates/app_websocket.tpl'))
		self.django_app_content = file_content(joiner(disini, 'templates/app_content.tpl'))

		# self.antd_asset_json = file_content(joiner(disini, 'antd/asset_json.tpl'))
		# self.antd_asset_json_content = file_content(joiner(disini, 'antd/asset_json_content.tpl'))
		# self.antd_app_content = file_content(joiner(disini, 'antd/app_content.tpl'))

		self.hasil_columnify = columnify(self.tables, 'django')
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

		# self.db_backend = 'sqlite'
		if hasattr(self.root, 'host'):
			self.db_backend = 'postgres'
		if hasattr(self.root, 'port'):
			self.db_backend = 'postgres'


	def app_init(self):
		from app.libpohon.app_init import app_init
		template_app_init = app_init(self.tables)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)


	def app_content(self):
		from app.libpohon.app_content import app_content
		template_node_app_content = app_content(self.tables, self.django_app_content)
		template_node_app_content = tabify_content(template_node_app_content, num_tab=2)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_CONTENT', template_node_app_content)

		# oprek isi /main/asgi.py
		# apps.track.urls.websocket_urlpatterns
		# +
		# apps.like.urls.websocket_urlpatterns
		# __TEMPLATE_WSROUTES
		wsroutes = [f'apps.{table.model.lower()}.urls.websocket_urlpatterns' for table in self.tables]
		wsroutes = tabify_contentlist(wsroutes, num_tab=3, aslist=True)
		tab3 = '\t\t\t'
		wsroutes = f'\n{tab3}+\n'.join(wsroutes)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_WSROUTES', wsroutes)


	def generate_app_migrate(self):
		# $ python manage.py makemigrations __TEMPLATE_APP01 __TEMPLATE_APP02
		# migrationlines = []
		# for index, tbl in enumerate(tables,1):
		#   appidx = str(index).zfill(2)
		# migrations = [f"__TEMPLATE_APP{str(angka+1).zfill(2)}" for angka in range(len(self.tables))]
		migrations = [tbl.model for tbl in self.tables]
		migrationlines = tab() + f"# $ python manage.py makemigrations {' '.join(migrations)}"
		print('migrationlines:', migrationlines)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_MIGRATE_COMMAND', migrationlines)


	def generate_app_route_installed(self):
		routelines = []
		installedlines = []
		for index, tbl in enumerate(self.tables,1):
			# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
			appidx = str(index).zfill(2)
			item = f"path('api/', include('apps.__TEMPLATE_APP{appidx}.urls')),"
			routelines.append(item)
			install = f"'apps.__TEMPLATE_APP{appidx}',"
			installedlines.append(install)

		template_routelines = '\n'.join([tab(1)+item for item in routelines])
		print('='*20, 'routelines')
		print('template_routelines:', template_routelines)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_ROUTE', template_routelines)

		template_installedapps = '\n'.join([tab(1)+item for item in installedlines])
		print('='*20, 'installedlines')
		print('INSTALLED_APPS = [')
		print('template_installedapps:', template_installedapps)
		print(']')
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INSTALLED_APPS', template_installedapps)


	def mkfile(self):
		self.change_projectdir()
		self.db_init()
		self.app_init()
		self.app_content()
		# app migrate
		self.generate_app_migrate()
		# app route + installed apps
		self.generate_app_route_installed()


	def app_model(self):
		"""
		backend: model/sequelize
		"""
		# from app.libpohon.app_content import app_content
		from app.libpohon.app_content_model import app_content
		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)

		for meja in self.tables:
			tablename = meja.model\
			
			# template_node_app_content = app_content(self.tables, self.django_model)
			template_node_app_content = app_content(tablename, self.django_model)
			generated_fields = columnify_and_transform(self.tables, 'django', tablename)
			generated_fields = tabify_content(generated_fields)
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
			# header = f'/np/node-postgres/src/apps/{tablename.lower()}/models/postgres.js'
			header = f'/apps/{tablename}/models.py'
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
			pengganti = tabify_contentlist(names, num_tab=2, aslist=True)
			pengganti = ',\n'.join(pengganti) + ',\n'
			per_table = self.antd_asset_json_content.replace('__TEMPLATE_APP_ASSET_JSON', pengganti)
			header = f'/np/react-antd/assets/{tablename.lower()}.json'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)


	def generate_graphql(self):
		from .bantu_graphql import generate_graphql
		self.mkfile_input_content = generate_graphql(self.tables, self.mkfile_input_content)
		print('django selesai generate graphql')


	def generate_model(self):
		# from .bantu_django_model import generate_model
		# generate_model(self.tables)
		from app.utils import salin_objek
		from app.libpohon.app_content_model import app_content
		from app.libpohon import get_import

		# self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_SERVER_APP_CONTENT', template_node_app_content)

		TIMESTAMPED_BASE_MODEL = 'TimestampedModel'
		DEFAULT_BASE_MODEL = 'models.Model'
		TIMESTAMP_IMPORT = 'from main.helpers import TimestampedModel'

		for meja in self.tables:
			tablename = meja.model
			first_column = meja.children[0].label

			basemodel = TIMESTAMPED_BASE_MODEL if hasattr(meja, 'timestamp') else DEFAULT_BASE_MODEL
			# import_part = libpohon_data['import_part']
			# import_part = salin_objek(libpohon_data['import_part'])
			import_part = get_import(tablename)
			# if tablename in libpohon_data['import_part_by_table']:
			# 	import_part = salin_objek(libpohon_data['import_part_by_table'][tablename])

			if hasattr(meja, 'timestamp'): # {@User=#5,ts}
				basemodel =  TIMESTAMPED_BASE_MODEL
				import_part.append(TIMESTAMP_IMPORT)
			else:
				basemodel =  DEFAULT_BASE_MODEL

			generated_fields = columnify_and_transform(self.tables, 'django', tablename)
			template_node_app_content = app_content(tablename, self.django_model)
			generated_fields = tabify_content(generated_fields)
			per_table = template_node_app_content.replace('__FIELDS__', generated_fields)
			per_table = per_table.replace('__TABLENAME__', tablename)
			per_table = per_table.replace('__COLNAME__', first_column)
			per_table = per_table.replace('__TABLE_BASEMODEL__', basemodel)
			per_table = per_table.replace('__IMPORTS__', '\n'.join(import_part))
			# stlh import_part dipake utk sebuah table, kita kembalikan dulu default value
			# di sini bukan lokasi yg benar utk kembalikan ke default
			# krn table2 lain masih butuh informasi "relTo"
			# libpohon_data['import_part'] = ['from django.db import models']

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
			# header = f'/np/node-postgres/src/apps/{tablename.lower()}/models/postgres.js'
			# header = f'/np/node-postgres/src/apps/{tablename.lower()}/models/postgres.js'
			# self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
			entry_name = 'models'
			header = f'/apps/{tablename}/{entry_name}.py'
			# entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
			# entrify = append_entry(tbl.model, per_table, entry_name='models')
			# append_file(output_django_mkfile, entry_model)
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)


	def generate_websocket(self):
		"""
		utk entry mk-nya lihat common:APP_CONTENT_TEMPLATE
		"""
		# from .config import tpl_appwebsocket
		# from .common import append_entry
		for index, tbl in enumerate(self.tables,1):
			tablename = tbl.model
			tablename_lower = tbl.model.lower()
			# tpl_appwebsocket_content = file_content(tpl_appwebsocket)
			content = self.django_websocket \
				.replace('__TEMPLATE_TABLENAME_LOWER___', tablename_lower) \
				.replace('__TEMPLATE_TABLENAME_CASE__', tablename)
			# entrify = append_entry(tbl.model, content, entry_name='websocket')
			entry_name = 'websocket'
			header = f'/apps/{tablename}/{entry_name}.py'
			self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, content)


	def use_postgres_or_sqlite(self):
		# use_postgres = False
		old_string = '__TEMPLATE_CONDITIONAL_DATABASE'
		pgstring = tab(2) + 'config.py,f(@a,e=utama=/main/config.py/databases/postgres)'
		sqlitestring = tab(2) + 'config.py,f(@a,e=utama=/main/config.py/databases/sqlite3)'
		
		new_string = sqlitestring # self.db_backend = 'sqlite'
		if hasattr(self, 'db_backend') and self.db_backend == 'postgres':
			new_string = pgstring

		# replace_string_in_file(output_django_mkfile, old_string, new_string, replace_count=1)
		self.mkfile_input_content = self.mkfile_input_content.replace(old_string, new_string, 1)

		# jk gak ada table user, kita provide default
		# pastikan mk output file sudah digenerate


	def handle_user_app(self):
		"""
		jk user provide User table maka kita gak gunakan default user:
		input_django_mkfile_template
		default_user_mk_entry

		replace_string_in_file
		replace_string_in_file(filepath, old_string, new_string, replace_count=1)

		config.py,f(@a,e=utama=/main/config.py/databases/postgres)
		config.py,f(@a,e=utama=/main/config.py/databases/sqlite3)
		__TEMPLATE_CONDITIONAL_DATABASE
		"""
		old_string = '__TEMPLATE_CONDITIONAL_USER'
		user_is_provided = False
		for index, tbl in enumerate(self.tables,1):
			if tbl.model.lower() == 'user' or tbl.model.lower() == 'users':
				user_is_provided = True
				break

		if user_is_provided:
			# replace_string_in_file(output_django_mkfile, old_string, '', replace_count=1)
			self.mkfile_input_content = self.mkfile_input_content.replace(old_string, '', 1)
		else:
			# from ..config.bantu_django import default_user_mk_entry
			# replace_string_in_file(output_django_mkfile, old_string, default_user_mk_entry, replace_count=1)
			self.mkfile_input_content = self.mkfile_input_content.replace(old_string, default_user_mk_entry, 1)


	def generate_faker_migration_seed(self):
		from .bantu_django_faker import generate_faker, gen_jsondata
		for index, tbl in enumerate(self.tables,1):

			if hasattr(tbl, 'faker'):
				'''
				attr faker diset di lang.csv.processor
				sesuai jumlah wkt {@namatable=#jumlah} spt {@Review=#10}
				'''
				records = []
				for _ in range(tbl.faker):
					kwargs = generate_faker(table=tbl)
					records.append(Record(**kwargs))

				# tulis ke output/django.mk => entry utk fixtures
				# python manage.py loaddata apps/article/fixtures/article.json
				# python manage.py loaddata apps/comment/fixtures/comment.json
				# python manage.py loaddata apps/tag/fixtures/tag.json
				# if env_int('generate_json'):
				self.mkfile_input_content = gen_jsondata(tbl.model, records, self.mkfile_input_content)

			# input(f'\n\nPress Enter utk lanjut ke generate faker tabel berikutnya stlh {tbl.model}... ')
			print('*'*80, 'django: generate_faker_migration_seed END')


	def model(self):
		# self.app_model()
		# self.app_json()
		self.generate_graphql()

		self.generate_model()
		self.generate_websocket()
		self.use_postgres_or_sqlite()
		# jk gak ada table user, kita provide default
		# pastikan mk output file sudah digenerate
		self.handle_user_app()
		self.generate_faker_migration_seed()

		# # gen_models_reactantd_antd
		# # generate_react_component
		# antd = AntdModel(self.configuration, self.mkfile_input_content)
		# antd.generate_react_component()
		# antd.generate_menu_json()
		# antd.generate_app_routes()
		# self.mkfile_input_content = antd.latest()
		# node = NodeModel(self.root, self.tables, self.mkfile_input_content)
		# node.gen_apps_index()
		# self.mkfile_input_content = node.latest()


	def save_file(self):
		file_write(self.mkfile_output, self.mkfile_input_content)
		print('hasil save file:', self.mkfile_output)


	def generate(self):
		self.mkfile()
		self.model()
		self.save_file()
		print('selesai generate django')


	def output(self):
		return self.mkfile_output
