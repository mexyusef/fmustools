from anytree import RenderTree
from schnell.app.dirutils import joiner, isdir, create_dir_with_parent
from schnell.app.fileutils import file_write
from schnell.app.printutils import indah3
from schnell.app.stringutils import (
	escape_quotes,
	merge_lines,
)
from schnell.db.bantuan.common import tab
from schnell.db.bantuan.generate_faker import generate_faker

entity_field_map = {
	'boolean':      'BOOL',
	'enum':         'GANTI',

	'double':       'FLOAT',
	'float':        'FLOAT', # float(n), n = 0-24 utk float
	'number':       'NUMERIC', # numeric(left,right)
	'decimal':			'NUMERIC', # numeric(left,right)
	
	# 'image':				'GANTI',

	'auto':					'SERIAL',
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

	'django_foreign_key':			'INT FOREIGN KEY REFERENCES',
	'django_one_to_one':			'GANTI',
	'django_one_to_many':			'GANTI',
	'django_many_to_many':		'GANTI',

	# 'email':        'GANTI',
	# 'slug':         'GANTI',
}

insert_statement = """
INSERT INTO __TABLE__ (__COLUMNS__)
VALUES (__VALUES__);
"""


class SQLOutput:


	def __init__(self, RootNode, project_dir='input'):
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
		self.tablenames = []
		self.entity_body = []
		self.insert_body = []
		# kita masukkan ke migrations agar bisa bikin flyway command
		self.basedir = joiner(project_dir, 'mymigrations/migrations')
		if not isdir(self.basedir):
			create_dir_with_parent(self.basedir)
		filepath = joiner(self.basedir, 'sql_pg_dialect.sql')
		self.output_mkfilename = filepath


	def generate(self):
		# separator = '\n\n// ' + '*' * 40 + '\n'
		return self.generate_sql()


	def generate_file(self, content):
		file_write(self.output_mkfilename, content)


	def generate_program_output(self):
		self.generate_sql_body()
		self.generate_sql_insert()
		first = '\n'.join(self.entity_body)
		second = '\n'.join(self.insert_body)
		content = first + '\n' 
		# comment out in sql
		content += '-- '
		content += '*'*40 + '\n'
		content += second
		self.generate_file(content) # jadi semacam index.mk utk di run-fmus
		return content


	def generate_sql(self):
		self.generate_sql_body()
		self.generate_sql_insert()
		first = '\n'.join(self.entity_body)
		second = '\n'.join(self.insert_body)
		content = first + '\n' 
		# comment out in sql
		content += '-- '
		content += '*'*40 + '\n'
		content += second
		return content


	def generate_sql_insert(self):
		"""
		di sini ada contoh pake faker
		dimana kita peroleh { colname: data, colname2: data2 } utk masing2 record.
		"""
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

	
	def namify(self, name, quoting=True, quote='"'):
		if quoting:
			return f'{quote}{name}{quote}'
		return name

	
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
			self.generate_command_docker(temp)
			self.generate_command_flyway()


	def generate_command_docker(self, temp):
		# docker_cmd = '\n' + '-'*20 + '\n'
		docker_cmd = '-- '
		docker_cmd += '*'*40 + '\n'

		postgres_user = self.dbuser
		postgres_dbname = self.dbname
		prefix_cmd = f'docker exec -it dbcontainer psql -U {postgres_user} {postgres_dbname} -c'
		create_table_oneline = escape_quotes(merge_lines(temp))
		# comment out in sql
		docker_cmd += '-- '
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
		prefix_cmd = f'/home/usef/flyway-7.11.3/flyway -X -url=jdbc:{postgres_dialect}://{postgres_host}:{postgres_port}/{postgres_dbname} -user={postgres_user} -password={postgres_pass} -locations=filesystem:{sqlfiles_location} -validateOnMigrate=false migrate'
		# docker_cmd = '\n' + '-'*20 + '\n'
		docker_cmd = '-'*20 + '\n'
		# comment out in sql
		docker_cmd += '-- '
		docker_cmd += prefix_cmd		
		self.entity_body.append(docker_cmd)


def bantu_sql(RootNode, project_dir='input', need_program_output=False):
	indah3('bantu_sql', warna='white')
	grpc = SQLOutput(RootNode, project_dir=project_dir)
	if need_program_output: # ada file_write
		return grpc.generate_program_output()
	return grpc.generate()
