from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)
from app.libpohon.app_content_model import app_content as app_content_model
from app.libpohon.app_content import app_content
from app.stringutils import tabify_content, tabify_contentlist
from app.treeutils import tables_from_rootnode
from app.usutils import tab, tab_tab, tab_space
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
from app.stringutils import (
	escape_quotes,
	merge_lines,
)
from app.fileutils import get_definition_by_key_permissive_start
from app.fmus import Fmus
from anytree import RenderTree
from db.bantuan.generate_faker import generate_faker

entity_field_map = {
	'boolean':      'BOOL',
	'enum':         'GANTI',

	'double':       'FLOAT',
	'float':        'FLOAT', # float(n), n = 0-24 utk float
	'number':       'NUMERIC', # numeric(left,right)
	'decimal':		'NUMERIC', # numeric(left,right)
	
	# 'image':		'GANTI',

	'auto':			'SERIAL',
	'bigint':       'INT',
	'integer':      'INT',	

	# 'string':       'CHAR', # char(n), char itu fixed size
	'string':       'VARCHAR', # char(n), char itu fixed size
	'text':         'TEXT',
	'varchar':      'VARCHAR', # varchar(n)

	'date':         'DATE',
	'time':         'TIME',
	'timestamp':    'TIMESTAMP',
	# 'timestamp':    'TIMESTAMPTZ',

	'django_foreign_key':		'INT FOREIGN KEY REFERENCES',
	'django_one_to_one':		'GANTI',
	'django_one_to_many':		'GANTI',
	'django_many_to_many':		'GANTI',

	# 'email':        'GANTI',
	# 'slug':         'GANTI',
}

insert_statement = """
INSERT INTO __TABLE__ (__COLUMNS__)
VALUES (__VALUES__);
"""

grpc_field_map = {
  'string'            : 'string',
  'float'             : 'float',
  # int32, bytes
}


disini = here(__file__)


class Coordinator:


	def __init__(self, RootNode, project_dir='__INPUT__'):
		self.root = RootNode
		self.dbuser = 'usef'
		self.dbpass = 'rahasia'
		self.dbname = 'hapus'
		self.dbhost = 'localhost'
		self.dbport = 5432
		self.dbdialect = 'postgresql' # hrs valid utl alamat flyway
		if hasattr(RootNode, 'dbname'):
			self.dbname = RootNode.dbname
		if hasattr(RootNode, 'username'):
			self.dbuser = RootNode.username
		if hasattr(RootNode, 'password'):
			self.dbpass = RootNode.password
		if hasattr(RootNode, 'host'):
			self.dbhost = RootNode.host
		if hasattr(RootNode, 'port'):
			self.dbport = RootNode.port
		self.tables = tables_from_rootnode(self.root)
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


	def generate_config(self):
		self.file_path_config = joiner(disini, 'templates/app_path_config.tpl')
		self.file_path_config_content = file_content(self.file_path_config)

		self.file_config = joiner(disini, 'templates/app_config.js.tpl')
		file_config_content = file_content(self.file_config)

		all_table_content = []
		for index, tbl in enumerate(self.tables,1):
			tablename = tbl.model
			# tablename_lower = tbl.model.lower()

			per_table = app_content_model(tablename, self.file_path_config_content)
			all_table_content.append(per_table + '\n\n')

		all_table_contents = '\n'.join(all_table_content)
		file_config_content = file_config_content.replace('__TEMPLATE_APP_CONFIG', all_table_contents)

		file_config_header = '/tmp/rework/store/config.js'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, file_config_header, file_config_content)


	def generate_store(self):
		self.file_store_import = joiner(disini, 'templates/app_store_import.tpl')
		self.file_store_import_content = file_content(self.file_store_import)

		self.file_store_reducer = joiner(disini, 'templates/app_store_reducer.tpl')
		self.file_store_reducer_content = file_content(self.file_store_reducer)

		self.file_storejs = joiner(disini, 'templates/app_store.js.tpl')
		self.file_storejs_content = file_content(self.file_storejs)

		store_imports = app_content(self.tables, self.file_store_import_content)
		store_reducers = app_content(self.tables, self.file_store_reducer_content)

		self.file_storejs_content = self.file_storejs_content.replace('__TEMPLATE_APP_STORE_IMPORTS', store_imports)
		self.file_storejs_content = self.file_storejs_content.replace('__TEMPLATE_APP_STORE_REDUCERS', store_reducers)
		file_store_header = '/tmp/rework/store/index.js'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, file_store_header, self.file_storejs_content)


	def generate_appcontent(self):
		self.file_appcontent = joiner(disini, 'templates/app_content_template.tpl')
		self.file_appcontent_content = file_content(self.file_appcontent)
		self.file_actions = joiner(disini, 'templates/app_actions.tpl')
		self.file_actions_content = file_content(self.file_actions)
		self.file_constants = joiner(disini, 'templates/app_constants.tpl')
		self.file_constants_content = file_content(self.file_constants)
		self.file_reducers = joiner(disini, 'templates/app_reducers.tpl')
		self.file_reducers_content = file_content(self.file_reducers)

		appcontentlines = app_content(self.tables, self.file_appcontent_content)
		self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_CONTENT', appcontentlines)

		# /tmp/rework/store/__TABLENAME_LOWER__/__TABLENAME_LOWER__Actions.js
		# /tmp/rework/store/__TABLENAME_LOWER__/__TABLENAME_LOWER__Constants.js
		# /tmp/rework/store/__TABLENAME_LOWER__/__TABLENAME_LOWER__Reducers.js
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


	def mkfile(self):
		self.change_projectdir()
		self.db_init()
		self.app_init()
		# redux
		self.generate_appcontent()
		self.generate_config()
		self.generate_store()
		# sql
		self.entity_body = []
		self.insert_body = []
		self.generate_sql_insert()
		self.docker_command_list = []
		self.docker_command_list_body = ''
		self.generate_sql_body()

		first = '\n'.join(self.entity_body)
		second = '\n'.join(self.insert_body)
		sql_content = first + '\n-- ' + '*'*40 + '\n' + second
		# self.generate_sql_file(content)
		# kita masukkan ke migrations agar bisa bikin flyway command
		# self.basedir = joiner(project_dir, 'mymigrations/migrations')
		# if not isdir(self.basedir):
		# 	create_dir_with_parent(self.basedir)
		# filepath = joiner(self.basedir, 'sql_pg_dialect.sql')
		# self.output_mkfilename = filepath
		# file_write(self.output_mkfilename, content)
		sql_header = '/sql_pg_dialect.sql'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, sql_header, sql_content)
		self.generate_command_docker_bylist()
		self.generate_command_flyway()
		self.generate_json_csv()

		# grpc
		self.generate_gprc()

		# ts-related
		from db.bantuan.fullstack.bantu_ts import bantu_ts
		tsheader = '/typescript-related.js'
		tsbody = bantu_ts(self.root)
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, tsheader, tsbody)

		from db.bantuan.bantu_sbgql import bantu_sbgql
		sbgqlheader = '/springboot.gql'
		sbgqlbody = bantu_sbgql(self.root)
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, sbgqlheader, sbgqlbody)

		from db.bantuan.bantu_nest import bantu_nest as bantu_nest_v1
		nestheader = '/nest-v1.js'
		nestbody = bantu_nest_v1(self.root)
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, nestheader, nestbody)

		# hasilkan mkfile:
		# output: /mnt/c/tmp/working/output/nest_rest_gql-output.mk
		# from db.bantuan.backend.bantu_nest.bantu_nest import bantu_nest as bantu_nest_v2
		# nestheader = '/nest-v2.js'
		# nestbody = bantu_nest_v2(self.root)
		# self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, nestheader, nestbody)

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


	def generate_sql_insert(self):
		"""
		di sini ada contoh pake faker
		dimana kita peroleh { colname: data, colname2: data2 } utk masing2 record.
		"""
		from db.bantuan.common import django_relationship_fields
		for _, tbl in enumerate(self.root.children, 1):
			table_fields = []
			table_plural = tbl.model.lower() + 's'
			if hasattr(tbl, 'faker'):
				records = []
				for angka in range(tbl.faker):
					print('pre generate_faker: oprekking sql:', RenderTree(tbl))
					kwargs = generate_faker(table=tbl, init_counter=0 if angka==0 else None)
					bentuk_values = []
					for _, col in enumerate(tbl.children):
						is_string = col.type == 'string' or col.type == 'varchar' or col.type == 'text' or col.type == 'date' or col.type == 'timestamp'
						if col.type in django_relationship_fields: # django fk, 11, 1m, m1, mm
							continue
						item = kwargs[col.label]
						
						# enum diberi $$$ oleh ucsv/processor:358
						if is_string:
							if isinstance(item, str) and '$$$' in item:
								# item = item.replace('$$$', '"')
								item = item.replace('$$$', "'")
							else:
								'''
								postgres minta ' utk string
								'''
								# item = f'"{item}"'
								item = f"'{item}'"

						bentuk_values.append(f'{item}')

					stmt = insert_statement.replace('__TABLE__', table_plural) \
						.replace('__COLUMNS__', ', '.join([item for item in kwargs.keys()])) \
						.replace('__VALUES__', ', '.join(bentuk_values))

						# .replace('__VALUES__', ', '.join([item for item in kwargs.values()]))
					self.insert_body.append(stmt)


	def generate_sql_body(self):

		for table_no, table in enumerate(self.root.children, 1):
			table_fields = []
			primary_key = None
			for column_no, field in enumerate(table.children, 1):

				fieldspec = '@Column (__COLUMN_CONSTRAINT)'
				fieldspec_constraint_object = []
				# fieldspec_constraint_nonobject = ''

				# utk array, sql-nya apa? relation?
				# if hasattr(field, 'subtype'):
				# 	column = column.replace('__SUBTYPE__', entity_field_map.get(field.subtype, field.subtype))
				# 	if field.type == 'array_of':
				# 		fieldspec_constraint_nonobject = "'simple-array'"

				if hasattr(field, 'primaryKey'):
					'''
					primary key kita tambahkan di akhir para kolom gaya sql
					'''
					# fieldspec_constraint_object .append ('PRIMARY KEY')
					primary_key = f"PRIMARY KEY ({self.namify(field.label)})"

				jenis_data = entity_field_map.get(field.type, field.type)

				if field.type == 'django_foreign_key' and hasattr(field, 'relTo'):
					relation = field.relTo
					if '.' in relation and relation.count('.') == 1:
						relation = relation.strip('"') # hilangkan semua dq dulu
						foreign_table, foreign_column = relation.split('.')
						# city_id INT FOREIGN KEY REFERENCES city(id)
						jenis_data += ' ' + f'{foreign_table}({foreign_column})'
					else:
						jenis_data += ' ' + relation

				if hasattr(field, 'max_length') or hasattr(field, 'typenum'):
					if field.type == 'string' or field.type == 'varchar':
						
						if hasattr(field, 'max_length'):
							maxlen = field.max_length
						elif hasattr(field, 'typenum'):
							maxlen = field.typenum
						jenis_data = f'{jenis_data}({maxlen})'

				column = f"{self.namify(field.label)} {jenis_data}__CONSTRAINTS_HOLDER__"

				if hasattr(field, 'allowNull'):
					fieldspec_constraint_object.append('NULL' if field.allowNull else 'NOT NULL')

				if hasattr(field, 'defaultValue'):
					'''
					konversi False ke false
					juga utk time
					timestamp,dt,dbi,df=datetime.utcnow
					perlu konversi ke sql...nonpython...
					'''
					nilai_default = field.defaultValue
					if nilai_default == 'empty':
						nilai_default = "''"
					if field.type == 'boolean' and nilai_default.lower() in ['false', 'true']:
						nilai_default = nilai_default.lower()
					if (field.type == 'string' or field.type.startswith('varchar')) and nilai_default.count('"') == 0 and nilai_default.count("'") == 0:
						nilai_default = '"' + nilai_default + '"'
					fieldspec_constraint_object .append ('DEFAULT ' + nilai_default)

				stringified_fieldspec_constraint_object = ''
				if fieldspec_constraint_object:
					# kasih space stlh jenis kolom
					stringified_fieldspec_constraint_object = ' ' + ' '.join(fieldspec_constraint_object)

				# stringified_nonobject = ', '.join([fieldspec_constraint_nonobject])
				# print('stringified_nonobject:', stringified_nonobject)
				# fieldspec_constraint = stringified_nonobject + stringified_fieldspec_constraint_object
				fieldspec = column.replace('__CONSTRAINTS_HOLDER__', stringified_fieldspec_constraint_object)
				table_fields.append(fieldspec)

			if primary_key is not None:
				table_fields.append(primary_key)
			stringified_fields = ',\n'.join([tab(1)+item for item in table_fields])
			# nama_table = table.model.lower()
			# nama_entity = f"{table.model}Entity"
			sql_statement_terminator = ';'
			table_plural = table.model.lower() + 's'
			temp = f"\nCREATE TABLE IF NOT EXISTS {self.namify(table_plural)} (\n"
			temp += stringified_fields
			temp += f'\n){sql_statement_terminator}'
			self.entity_body.append(temp)

			# docker_cmd = '\n' + '-'*20 + '\n'
			# prefix_cmd = 'docker exec -it pg psql -U usef hapuslah -c'
			# create_table_oneline = escape_quotes(merge_lines(temp))
			# docker_cmd += f'{prefix_cmd} "{create_table_oneline}"'
			# self.entity_body.append(docker_cmd)
			# self.generate_command_docker(temp)
			self.docker_command_list.append(temp)


	def generate_command_docker_bylist(self):
		for temp in self.docker_command_list:
			docker_cmd = '\n\n'
			postgres_user = self.dbuser
			postgres_dbname = self.dbname
			prefix_cmd = f'docker exec -it pg psql -U {postgres_user} {postgres_dbname} -c'
			create_table_oneline = escape_quotes(merge_lines(temp))
			# self.docker_command_list
			docker_cmd += f'{prefix_cmd} "{create_table_oneline}"'
			# self.docker_command_list_body.append(docker_cmd)
			self.docker_command_list_body += docker_cmd


	def generate_command_docker(self, temp):
		docker_cmd = '\n' + '-'*20 + '\n'
		postgres_user = self.dbuser
		postgres_dbname = self.dbname
		prefix_cmd = f'docker exec -it pg psql -U {postgres_user} {postgres_dbname} -c'
		create_table_oneline = escape_quotes(merge_lines(temp))
		docker_cmd += f'{prefix_cmd} "{create_table_oneline}"'
		self.entity_body.append(docker_cmd)


	def generate_command_flyway(self):
		postgres_user = self.dbuser
		postgres_pass = self.dbpass
		postgres_dbname = self.dbname
		postgres_host = self.dbhost
		postgres_port = self.dbport
		postgres_dialect = self.dbdialect
		sqlfiles_location = './migrations'
		flyway_cmd = '/home/usef/flyway-7.11.3/flyway'
		prefix_cmd = f'{flyway_cmd} -X -url=jdbc:{postgres_dialect}://{postgres_host}:{postgres_port}/{postgres_dbname} -user={postgres_user} -password={postgres_pass} -locations=filesystem:{sqlfiles_location} -validateOnMigrate=false migrate'
		docker_cmd = '\n\n'
		docker_cmd += prefix_cmd
		# self.entity_body.append(docker_cmd)
		sql_header = '/flyway-cmd.sh'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, sql_header, docker_cmd)
		sql_header = '/docker-cmd.sh'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, sql_header, self.docker_command_list_body)


	def namify(self, name, quoting=True, quote='"'):
		if quoting:
			return f'{quote}{name}{quote}'
		return name


	def generate_json_csv(self):
		from db.bantuan.bantu_faker import bantu_faker
		# 'fake'        : lambda RootNode: bantu_faker(RootNode, 'json'),
		# 'fakejson'    : lambda RootNode: bantu_faker(RootNode, 'json_simple'),
		# 'fakecsv'     : lambda RootNode: bantu_faker(RootNode, 'json_csv'),
		json1header = '/jsondata-result.json'
		json1data = bantu_faker(self.root, 'json')
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, json1header, json1data)

		json2header = '/jsondata.json'
		json2data = bantu_faker(self.root, 'json_simple')
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, json2header, json2data)

		csvheader = '/csvdata.csv'
		csvdata = bantu_faker(self.root, 'csv')
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, csvheader, csvdata)


	def generate_gprc(self):
		self.grpc_tables = []
		self.grpc_service = []
		self.grpc_tablenames = []
		self.do_grpc_tables()
		self.do_grpc_service()
		
		header = '\n'.join(self.grpc_service)
		footer = '\n'.join(self.grpc_tables)
		grpc_body = header + '\n' + footer
		grpc_header = '/grpc.service'
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, grpc_header, grpc_body)


	def do_grpc_tables(self):
		for index, table in enumerate(self.root.children, 1):
			table_fields = []
			self.grpc_tablenames.append(table.model)
			for field_no, field in enumerate(table.children, 1):
				column = f"{grpc_field_map.get(field.type, field.type)} {field.label} = {field_no};"
				table_fields.append(column)
			
			stringified_fields = '\n'.join([tab_space(1)+item for item in table_fields])
			table = f"\nmessage {table.model} {{\n{stringified_fields}\n}}"
			self.grpc_tables.append(table)


	def do_grpc_service(self):
		self.grpc_service.append('\nsyntax = "proto3";')
		self.grpc_service.append(f'\nservice {self.root.dbname} {{')
		# rpc send_humidity(HumidityRequest) returns (HumidityResponse) {}
		# rpc send_humidity(HumidityRequest) {}
		# services = []
		for table in self.grpc_tablenames:
			svc = tab(1)+f"rpc send_{table.lower()}({table}) {{}}"
			self.grpc_service.append(svc)

		self.grpc_service.append('}')
