from app.treeutils import (
	data,
	token,
	child1,
	child2,
	child3,
	child4,
	child,
	chdata,
	chtoken,
	anak,
	ispohon, istoken,
	beranak,
	sebanyak,
	jumlahanak,
)
from anytree.search import find, findall
from anytree import RenderTree
from app.fileutils import (
	file_content,
	file_write,
	file_copy,
	append_entry_tostring,
	replace_string_in_file,
)
from app.dirutils import (
	joiner, ayah
)
from langs.ucsv import processor
from app.transpiler.frontend.fslang.common import program_config
from app.printutils import print_json
from app.treeutils import tables_from_rootnode
from app.stringutils import tabify_content, tabify_contentlist
from app.usutils import (
	tab,
	jenis_kolom,
	type_mapper,
	append_entry,
)

frontend_config = {}

disini = joiner(ayah(__file__,1))

from .helper import fastapi_mongo_app_content, fastapi_mongo_app_fmus

app_content_by_backend = {
	'fastapi-mongo': {
		'fmus': fastapi_mongo_app_fmus,
		'content': fastapi_mongo_app_content,
	}
}


from .django import Coordinator as django_generator
from .django_mongo import Coordinator as django_mongo_generator
from .dropwizard import Coordinator as dropwizard_generator
from .dropwizard_mongo import Coordinator as dropwizard_mongo_generator
from .fastapi import Coordinator as fastapi_generator
from .fastapi_mongo import Coordinator as fastapi_mongo_generator
from .flask import Coordinator as flask_generator
from .flask_mongo import Coordinator as flask_mongo_generator
from .micronaut import Coordinator as micronaut_generator
from .micronaut_mongo import Coordinator as micronaut_mongo_generator
from .moleculer import Coordinator as moleculer_generator
from .moleculer_mongo import Coordinator as moleculer_mongo_generator
from .nest import Coordinator as nest_generator
from .nest_mongo import Coordinator as nest_mongo_generator
from .node_antd import Coordinator as node_antd_generator
from .node_antd_mongo import Coordinator as node_antd_mongo_generator
from .node_apollo import Coordinator as node_apollo_generator
from .node_apollo_mongo import Coordinator as node_apollo_mongo_generator
from .quarkus import Coordinator as quarkus_generator
from .quarkus_mongo import Coordinator as quarkus_mongo_generator
from .springboot import Coordinator as springboot_generator
from .springboot_mongo import Coordinator as springboot_mongo_generator
from .fullstack import Coordinator as fullstack_generator

generator_by_backend = {
	'django': django_generator,
	'django_mongo': django_mongo_generator,
	'dropwizard': dropwizard_generator,
	'dropwizard_mongo': dropwizard_mongo_generator,
	'fastapi': fastapi_generator,
	'fastapi_mongo': fastapi_mongo_generator,
	'flask': flask_generator,
	'flask_mongo': flask_mongo_generator,
	'micronaut': micronaut_generator,
	'micronaut_mongo': micronaut_mongo_generator,
	'moleculer': moleculer_generator,
	'moleculer_mongo': moleculer_mongo_generator,
	'nest': nest_generator,
	'nest_mongo': nest_mongo_generator,
	'node_antd': node_antd_generator,
	'node_antd_mongo': node_antd_mongo_generator,
	'node_apollo': node_apollo_generator,
	'node_apollo_mongo': node_apollo_mongo_generator,
	'quarkus': quarkus_generator,
	'quarkus_mongo': quarkus_mongo_generator,
	'springboot': springboot_generator,
	'springboot_mongo': springboot_mongo_generator,
	'fullstack': fullstack_generator,
}


class BackendCreator:


	def __init__(self, RootNode, backend='fastapi_mongo', project_dir='input'):
		self.root = RootNode
		self.backend = backend
		source = joiner(disini, self.backend + '/index-input.mk')
		target = joiner(disini, self.backend + '/index.mk')
		file_copy(source, target)
		self.mkfile_output_filepath = target
		self.mkfile_input_content = file_content(target)
		self.mkfile_output_content = self.mkfile_input_content
		self.tablenames = []
		self.tables = tables_from_rootnode(self.root)
		self.app_content_template = app_content_by_backend[self.backend]['fmus']


	def generate_db_init(self):
		"""
		*,fastm/C<<{@User=#5}username,s;title,s,BY;description,s>>
		"""
		# dbvalues = {}
		dblines = []
		dbinfo = self.root
		dbtype = (hasattr(dbinfo, 'dbtype') and dbinfo.dbtype) or 'mongodb'
		dbuser = (hasattr(dbinfo, 'username') and dbinfo.username) or 'usef'
		dbpass = (hasattr(dbinfo, 'password') and dbinfo.password) or 'rahasia'
		dbhost = (hasattr(dbinfo, 'host') and dbinfo.host) or 'localhost'
		dbport = (hasattr(dbinfo, 'port') and dbinfo.port) or '17027'
		dbname = (hasattr(dbinfo, 'dbname') and dbinfo.dbname) or 'tempdb'

		dblines.append(f"%__TEMPLATE_DBUSER={dbuser}")
		dblines.append(f"%__TEMPLATE_DBPASS={dbpass}")
		dblines.append(f"%__TEMPLATE_DBHOST={dbhost}")
		dblines.append(f"%__TEMPLATE_DBPORT={dbport}")
		dblines.append(f"%__TEMPLATE_DBNAME={dbname}")
		dblines.append(f"%__TEMPLATE_DBTYPE={dbtype}")

		template_db_init = '\n'.join([tab(1)+item for item in dblines])
		print('='*20, 'generate_db_app_init/dblines')
		print(template_db_init)
		self.mkfile_output_content = self.mkfile_output_content.replace('__TEMPLATE_DB_INIT', template_db_init)


	def generate_app_content(self):
		contentlines = []
		for index, tbl in enumerate(self.tables,1):
			tablename = tbl.model
			tablename_lower = tablename.lower()
			tablename_upper = tablename.upper()
			# __TABmongo.py,f(e=__FILE__=/__TABLENAME_LOWER/mongo.py)
			# baris_entry = /__TABLENAME_LOWER/mongo.py
			# gunakan \t bukan double space di file mk
			content = self.app_content_template.replace('__TABLENAME_LOWER',tablename_lower).replace('__TAB', tab(1, use_space=False))
			content = tabify_content(content, self_tab='\t', num_tab=2)
			contentlines.append(content)

		template_app_content = '\n'.join(contentlines)
		print('='*20, 'contentlines')
		print(template_app_content)
		self.mkfile_output_content = self.mkfile_output_content.replace('__TEMPLATE_APP_CONTENT', template_app_content)

		# generate app entry
		# header = '/__TABLENAME_LOWER/mongo.py'
		# append_entry_tostring(self.mkfile_output_content, )
		for index, tbl in enumerate(anak(self.root),1):
			tablename = tbl.model
			tablename_lower = tablename.lower()
			tablename_upper = tablename.upper()
			header = f'/{tablename_lower}/mongo.py'
			body = app_content_by_backend[self.backend]['content'].replace('__TABLENAME_LOWER',tablename_lower).replace('__TABLENAME_CASE', tablename)
			# isi columns pada body
			columns = []
			find_by, find_by_with_type = '', '' # title etc -> title,s,BY -> rest find record by title...
			for column in anak(tbl):
				nama = column.label
				jenis = column.type
				jenis = jenis_kolom(jenis, 'pydantic')
				# title: str
				stmt = f'{nama}: {jenis}'
				columns.append(stmt)
				if hasattr(column, 'allowNull'):
					pass
				if hasattr(column, 'auto_increment'):
					pass
				if hasattr(column, 'auto_now'):
					pass
				if hasattr(column, 'auto_now_add'):
					pass
				if hasattr(column, 'blank'):
					pass
				if hasattr(column, 'db_index'):
					pass
				if hasattr(column, 'decimal_places'):
					pass
				if hasattr(column, 'defaultValue'):
					pass
				if hasattr(column, 'editable'):
					pass
				if hasattr(column, 'find_by'):
					find_by = nama
					find_by_with_type = f'{nama}: {jenis}'
				if hasattr(column, 'foreignKeyOnDelete'):
					pass
				if hasattr(column, 'max_digits'):
					pass
				if hasattr(column, 'max_length'):
					pass
				if hasattr(column, 'primaryKey'):
					pass
				if hasattr(column, 'related_name'):
					pass
				if hasattr(column, 'relTo'):
					pass
				if hasattr(column, 'unique'):
					pass
				if hasattr(column, 'values'):
					pass
				if hasattr(column, 'verbose_name'):
					pass
			
			if not find_by:
				find_by = tbl.children[0].label
				find_by_with_type = find_by + ': ' + tbl.children[0].type
			semua_kolom = tabify_contentlist(columns)
			column_params = ', '.join(columns)
			column_args = ', '.join([col.label for col in tbl.children])
			# "title": title, "description": description
			dict_like = ', '.join([f'"{col.label}": {col.label}' for col in tbl.children])
			body = body.replace('__TEMPLATE_MODEL_KOLOM', semua_kolom)
			body = body.replace('__TEMPLATE_COLUMN_FINDBY', find_by)
			body = body.replace('__TEMPLATE_COLUMN_FINDBY_TYPE', find_by_with_type)
			body = body.replace('__TEMPLATE_COLUMN_ARGS', column_args)
			body = body.replace('__TEMPLATE_COLUMN_PARAMS', column_params)
			body = body.replace('__TEMPLATE_COLUMN_DICT_LIKE', dict_like)
			self.mkfile_output_content = append_entry_tostring(self.mkfile_output_content, header, body)


	def replace_variables(self):
			"""
			routes.py
			__TEMPLATE_ROUTE_IMPORTS
			from apps.__TABLENAME_LOWER import mongo as __TABLENAME_LOWER_router
			__TEMPLATE_ROUTE_PATHS
			api_router.include_router(__TABLENAME_LOWER_router.router, prefix='/__TABLENAME_LOWERs', tags=['__TABLENAME_LOWERs'])

			main.py
			__TEMPLATE_HOST
			__TEMPLATE_PORT
			"""
			# self.tables = tables_from_rootnode(self.root)
			route_imports = [f'from apps.{table.model.lower()} import mongo as {table.model.lower()}_router' for table in self.tables]
			route_imports = '\n'.join(route_imports)

			route_paths = [f"api_router.include_router({table.model.lower()}_router.router, prefix='/{table.model.lower()}s', tags=['{table.model.lower()}s'])" for table in self.tables]
			route_paths = '\n'.join(route_paths)

			self.mkfile_output_content = \
				self.mkfile_output_content \
					.replace('__TEMPLATE_ROUTE_IMPORTS', route_imports) \
					.replace('__TEMPLATE_ROUTE_PATHS', route_paths)


	def generate_mkfile(self):
		file_write(self.mkfile_output_filepath, self.mkfile_output_content)
		print('writing to (self.mkfile_output_filepath):', self.mkfile_output_filepath)


	def generate_model(self, tables):
		pass


	def generate_coordinator(self):
		self.generate_db_init()
		self.generate_app_content()
		self.replace_variables()
		self.generate_mkfile()


	def generate(self):
		self.generate_coordinator()


def get_konfigurasi_backend():
	hasil = None
	try:
		hasil = program_config['config']['be']
	except Exception as e:
		print('Gagal get_konfigurasi_backend() / Exception: '+str(e) + '\nprogram_config:')
		print_json(program_config)
		hasil = program_config["be"]
	return hasil


def csv_statement(tree):
	"""
	csv_statement
		program_csv username,s
	"""
	print('csv_statement:', data(tree))
	print('csv_statement => config sekarang:')  
	print_json(program_config)
	
	code = chtoken(tree)  
	RootNode = processor(code, print)
	print(RenderTree(RootNode))

	node_tables = lambda node: hasattr(node, 'name') and node.name == 'table' and node.type == 'table'
	tables = findall(RootNode, node_tables) # tuple of anynode table..
	# # tables: (AnyNode(faker=5, model='User', name='table', type='table'),)
	# print('tables:', tables)

	konfigurasi_backend = get_konfigurasi_backend()
	# bc = BackendCreator(RootNode, konfigurasi_backend)
	# bc.generate()
	generator = generator_by_backend[konfigurasi_backend] (RootNode)
	generator.generate()

	frontend_config.update({
		# 'filepath': bc.mkfile_output_filepath,
		'filepath': generator.output(),
		'baris_entry': 'index/fmus',
	})

	# print('frontend_statement => final result:')
	# print_json(frontend_config)
	return frontend_config
