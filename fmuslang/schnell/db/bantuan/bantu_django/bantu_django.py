from anytree import RenderTree #, Node, AnyNode, AsciiStyle, PreOrderIter
from anytree.search import find, findall
# from schnell.app.dirutils import (
# 	joiner,
# 	within_same_folder,
# )
from schnell.app.fileutils import (
	file_content,
	# append_file,
	replace_string_in_file,
)
from schnell.app.printutils import indah4
from schnell.db.bantuan.common import tab, Record
# from ..config import (
# 	# input_django_mkfile_template,
# 	output_django_mkfile,
# )
from .config import output_django_mkfile, input_django_mkfile_template
from .common import app_content_template, default_user_mk_entry


class DjangoOutput:


	def __init__(self, RootNode, project_dir='input'):
		self.root = RootNode
		self.tablenames = []
		self.mkfile_input = file_content(input_django_mkfile_template) \
				.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', project_dir)
		self.mkfile_output = ''


	def generate_db_init(self):
		self.mkfile_output = self.mkfile_input
		dbvalues = {}
		dblines = []
		dbinfo = self.root		

		if hasattr(dbinfo, 'username'):
			dbvalues['username'] = dbinfo.username
			dblines.append(f"%__TEMPLATE_DBUSER={dbinfo.username}")

		if hasattr(dbinfo, 'password'):
			dbvalues['password'] = dbinfo.password
			dblines.append(f"%__TEMPLATE_DBPASS={dbinfo.password}")

		if hasattr(dbinfo, 'host'):
			dbvalues['host'] = dbinfo.host
			dblines.append(f"%__TEMPLATE_DBHOST={dbinfo.host}")
			
		if hasattr(dbinfo, 'port'):
			dbvalues['port'] = dbinfo.port
			dblines.append(f"%__TEMPLATE_DBPORT={dbinfo.port}")

		if hasattr(dbinfo, 'dbname'):
			dbvalues['dbname'] = dbinfo.dbname
			dblines.append(f"%__TEMPLATE_DBNAME={dbinfo.dbname}")

		self.db_backend = 'sqlite'
		if 'host' in dbvalues:
			self.db_backend = 'postgres'
		if 'port' in dbvalues:
			self.db_backend = 'postgres'

		template_db_init = '\n'.join([tab(1)+item for item in dblines])
		print('='*20, 'generate_db_app_init/dblines')
		print(template_db_init)
		self.mkfile_output = self.mkfile_output.replace('__TEMPLATE_DB_INIT', template_db_init)


	def generate_app_init(self, tables):
		applines = []
		for index, tbl in enumerate(tables,1):
			# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
			appidx = str(index).zfill(2)
			try:
				tablename = tbl.model
			except AttributeError as err:
				import traceback
				# AttributeError: 'AnyNode' object has no attribute 'model'
				print('Ketemu error:', err)
				print('Cek apakah semua kolom kecuali kolom akhir terpisah dg terminator ";".')
				print(traceback.format_exc())
			# perlu utk lower...ini akan jadi nama direktori utk masing2 app
			applines.append(f"%__TEMPLATE_APP{appidx}={tablename.lower()}")

		template_app_init = '\n'.join([tab(1)+item for item in applines])
		print('='*20, 'applines')
		print(template_app_init)
		self.mkfile_output = self.mkfile_output.replace('__TEMPLATE_APP_INIT', template_app_init)


	def use_postgres_or_sqlite(self):
		# use_postgres = False
		old_string = '__TEMPLATE_CONDITIONAL_DATABASE'
		pgstring = tab(2) + 'config.py,f(@a,e=utama=/main/config.py/databases/postgres)'
		sqlitestring = tab(2) + 'config.py,f(@a,e=utama=/main/config.py/databases/sqlite3)'
		
		new_string = sqlitestring # self.db_backend = 'sqlite'
		if self.db_backend == 'postgres':
			new_string = pgstring

		replace_string_in_file(output_django_mkfile, old_string, new_string, replace_count=1)


	def handle_user_app(self, tables):
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
		for index, tbl in enumerate(tables,1):
			if tbl.model.lower() == 'user' or tbl.model.lower() == 'users':
				user_is_provided = True
				break

		if user_is_provided:			
			replace_string_in_file(output_django_mkfile, old_string, '', replace_count=1)
		else:
			# from ..config.bantu_django import default_user_mk_entry
			replace_string_in_file(output_django_mkfile, old_string, default_user_mk_entry, replace_count=1)


	def generate_app_content(self, tables):
		contentlines = []
		for index, tbl in enumerate(tables,1):
			# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
			appidx = str(index).zfill(2)
			# tablename = tbl.tables['tablename']
			tablename = tbl.model
			content = app_content_template(appidx, tablename)
			contentlines.append(content)

		# template_app_content = '\n'.join([tab(2)+item for item in contentlines])
		template_app_content = '\n'.join(contentlines)
		print('='*20, 'contentlines')
		print(template_app_content)
		self.mkfile_output = self.mkfile_output.replace('__TEMPLATE_APP_CONTENT', template_app_content)


	def generate_app_migrate(self, tables):
		# $ python manage.py makemigrations __TEMPLATE_APP01 __TEMPLATE_APP02
		# migrationlines = []
		# for index, tbl in enumerate(tables,1):
		#   appidx = str(index).zfill(2)
		migrations = [f"__TEMPLATE_APP{str(angka+1).zfill(2)}" for angka in range(len(tables))]
		migrationlines = tab() + f"$ python manage.py makemigrations {' '.join(migrations)}"
		print(migrationlines)
		self.mkfile_output = self.mkfile_output.replace('__TEMPLATE_APP_MIGRATE_COMMAND', migrationlines)


	def generate_app_route_installed(self, tables):
		routelines = []
		installedlines = []
		for index, tbl in enumerate(tables,1):
			# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
			appidx = str(index).zfill(2)
			item = f"path('api/', include('apps.__TEMPLATE_APP{appidx}.urls')),"
			routelines.append(item)
			install = f"'apps.__TEMPLATE_APP{appidx}',"
			installedlines.append(install)

		template_routelines = '\n'.join([tab(1)+item for item in routelines])
		print('='*20, 'routelines')
		print(template_routelines)
		self.mkfile_output = self.mkfile_output.replace('__TEMPLATE_APP_ROUTE', template_routelines)

		template_installedapps = '\n'.join([tab(1)+item for item in installedlines])
		print('='*20, 'installedlines')
		print('INSTALLED_APPS = [')
		print(template_installedapps)
		print(']')
		self.mkfile_output = self.mkfile_output.replace('__TEMPLATE_APP_INSTALLED_APPS', template_installedapps)


	def generate_mkfile(self, output_django_mkfile):
		with open(output_django_mkfile, 'w') as fd:
			fd.write(self.mkfile_output)

		# configuration = {
		# 	'table_nodes': tables,
		# 	'root_node': RootNode,
		# }
		# return configuration


	def generate_model(self, tables):
		from .bantu_django_model import generate_model
		# tables = configuration['table_nodes']
		generate_model(tables)


	def generate_websocket(self, tables):
		"""
		utk entry mk-nya lihat common:APP_CONTENT_TEMPLATE
		"""
		from .config import tpl_appwebsocket
		from .common import append_entry
		for index, tbl in enumerate(tables,1):
			tablename_case = tbl.model
			tablename_lower = tbl.model.lower()
			tpl_appwebsocket_content = file_content(tpl_appwebsocket)
			content = tpl_appwebsocket_content \
				.replace('__TEMPLATE_TABLENAME_LOWER___', tablename_lower) \
				.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
			entrify = append_entry(tbl.model, content, entry_name='websocket')


	def generate_faker_migration_seed(self, tables):
		from .bantu_django_faker import generate_faker, gen_jsondata
		for index, tbl in enumerate(tables,1):

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
				gen_jsondata(tbl.model, records)

			# input(f'\n\nPress Enter utk lanjut ke generate faker tabel berikutnya stlh {tbl.model}... ')
			print('*'*80)


	def generate_graphql(self, tables):
		from .bantu_graphql import generate_graphql
		# self.mkfile_output
		generate_graphql(tables)


	def generate_coordinator(self):
		print(RenderTree(self.root))
		node_tables = lambda node: hasattr(node, 'name') and node.name == 'table' and node.type == 'table'
		tables = findall(self.root, node_tables)
		print(f"generate from:", input_django_mkfile_template)
		print(f"generate to:", output_django_mkfile)
		print(f"tables:", tables)

		status = 'GO\n'
		self.generate_db_init()
		status += '...db init\n'		
		self.generate_app_init(tables)
		status += '...app init\n'
		self.generate_app_content(tables)
		status += '...app content\n'
		self.generate_app_migrate(tables)
		status += '...app migrate\n'
		self.generate_app_route_installed(tables)
		status += '...app route/installed\n'		

		self.generate_mkfile(output_django_mkfile)
		status += '...gen mkfile\n'

		# utk replace/append mk file tunggu generate_mkfile
		# sblm itu gunakan self.mkfile_output
		self.generate_graphql(tables)
		status += '...graphql\n'

		self.generate_model(tables)
		self.generate_websocket(tables)
		self.use_postgres_or_sqlite()
		# jk gak ada table user, kita provide default
		# pastikan mk output file sudah digenerate
		self.handle_user_app(tables)
		status += '...gen model\n'
		self.generate_faker_migration_seed(tables)
		status += '...gen seed\n'
		return status


	def generate(self):
		# separator = '\n\n// ' + '*' * 40 + '\n'
		status = self.generate_coordinator()
		status += f'output: {output_django_mkfile}\n'		
		return status


	def generate_program_output(self):
		"""
		bukan utk output vscode
		tapi utk langsung fmus.process
		# jd kembalikan mk program
		kembalikan mkfilepath
		"""
		self.generate_coordinator()
		# return self.mkfile_output
		return output_django_mkfile


def bantu_django(RootNode, project_dir='input', need_program_output=False):
	indah4('bantu_django', warna='white')
	grpc = DjangoOutput(RootNode, project_dir=project_dir)
	if need_program_output:
		return grpc.generate_program_output()
	return grpc.generate()
