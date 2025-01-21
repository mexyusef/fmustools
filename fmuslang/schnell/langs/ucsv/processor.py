import json, os, pyperclip, sys
# from lark.visitors import InlineTransformer
# from lark import (
# 	Lark,
# 	# InlineTransformer,
# )
# from lark.visitors import InlineTransformer
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

# appdir = '/home/usef/danger/ulib/schnell/'
# sys.path.append(appdir)
# app.transpiler.lalang.py = os.pardir * 2
# langs.ucsv.processor.py = os.pardir * 2
disini = os.path.normpath(os.path.abspath(os.path.dirname(__file__))) # ucsv
path_langs = os.path.join(disini, os.pardir)
path_schnell = os.path.join(path_langs, os.pardir)
schnelldir = path_schnell
sys.path.extend([schnelldir, '..'])

import schnell.vendor.lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)
from schnell.app.printutils import indah4
from schnell.app.utils import env_get, env_int
from schnell.app.treeutils import (
	data,
	token as get_token,
	child1,
	child2,
	child3,
	child4,
	child,
	chdata,
	chtoken,
	anak as anak_treeutils_func,
	ispohon, istoken,
	beranak,
	sebanyak,
	jumlahanak,
)
from schnell.langs.ucsv.grammar import bahasa


# QuoteChar = ''
# QuoteChar = '"'
QuoteChar = '$$$'

WebFramework = [
	'to_sequelize',
	'to_sql',

	'to_actix',
	'to_asp',
	'to_django',
	'to_flask',
	'to_gorm',
	'to_laravel',
	'to_play',
	'to_phoenix',
	'to_rails',
	'to_springboot',
]

left_key = {
	'belongsTo': 'foreignKey',
	'hasOne': 'sourceKey',
}

right_key = {
	'belongsTo': 'targetKey',
	'hasOne': 'foreignKey',
}


class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions


def process_table(RootNode, parent_tree, debug):

	TableNode = AnyNode(parent=RootNode, name='table', type='table')

	for tree in parent_tree.children:

		if tree.data == 'statement':

			StatementNode = AnyNode(parent=TableNode)
			StatementNode.hasConstraint = False

			for branch in tree.children:

				if branch.data == 'column_name':
					StatementNode.label = str(branch.children[0])

				elif branch.data == 'column_type_spec':
					'''
					s
					t
					D utk double
					f float
					'''
					datatype = branch.children[0]
					StatementNode.type = datatype.data

					if StatementNode.type == 'django_foreign_key':
						StatementNode.foreignKey = True
						for constr in datatype.children:
							if constr.data == 'rel_to_object':
								content = str(constr.children[0])
								StatementNode.relTo = content
							elif constr.data == 'rel_to_string':
								content = str(constr.children[0])
								StatementNode.relTo = f'"{content}"'

							elif constr.data == 'action_list':
								crud_tree = constr.children[0]
								crud = crud_tree.data
								if crud == 'delete_action':
									# bisa models.CASCADE atau models.SET_NULL
									# default cascade
									StatementNode.foreignKeyOnDelete = 'models.CASCADE'
									if len(crud_tree.children) > 0:
										deltype = crud_tree.children[0]
										if deltype.data == 'delete_setnull':
											StatementNode.foreignKeyOnDelete = 'models.SET_NULL'
										# cascade_or_setnull = deltype.children[0]
										# if cascade_or_setnull.data == 'delete_setnull':
										# 	StatementNode.foreignKeyOnDelete = 'models.SET_NULL'

							elif constr.data == 'related_name':
								content = str(constr.children[0])
								StatementNode.related_name = f'"{content}"'
							elif constr.data == 'verbose_name':
								content = str(constr.children[0])
								StatementNode.verbose_name = f'"{content}"'

					elif StatementNode.type == 'django_one_to_one':
						StatementNode.oneToOne = True
						for constr in datatype.children:
							if constr.data == 'rel_to_object':
								content = str(constr.children[0])
								StatementNode.relTo = content
							elif constr.data == 'rel_to_string':
								content = str(constr.children[0])
								StatementNode.relTo = f'"{content}"'
							elif constr.data == 'action_list':
								crud = constr.children[0].data
								if crud == 'delete_action':
									StatementNode.foreignKeyOnDelete = 'models.CASCADE'
							elif constr.data == 'related_name':
								content = str(constr.children[0])
								StatementNode.related_name = f'"{content}"'
							elif constr.data == 'verbose_name':
								content = str(constr.children[0])
								StatementNode.verbose_name = f'"{content}"'

					elif StatementNode.type == 'django_one_to_many':
						StatementNode.oneToMany = True
						for constr in datatype.children:
							if constr.data == 'rel_to_object':
								content = str(constr.children[0])
								StatementNode.relTo = content
							elif constr.data == 'rel_to_string':
								content = str(constr.children[0])
								StatementNode.relTo = f'"{content}"'
							elif constr.data == 'action_list':
								crud = constr.children[0].data
								if crud == 'delete_action':
									StatementNode.foreignKeyOnDelete = 'models.CASCADE'
							elif constr.data == 'related_name':
								content = str(constr.children[0])
								StatementNode.related_name = f'"{content}"'
							elif constr.data == 'verbose_name':
								content = str(constr.children[0])
								StatementNode.verbose_name = f'"{content}"'

					elif StatementNode.type == 'django_many_to_many':
						StatementNode.manyToMany = True
						for constr in datatype.children:
							if constr.data == 'rel_to_object':
								content = str(constr.children[0])
								StatementNode.relTo = content
							elif constr.data == 'rel_to_string':
								content = str(constr.children[0])
								StatementNode.relTo = f'"{content}"'
							elif constr.data == 'action_list':
								crud = constr.children[0].data
								if crud == 'delete_action':
									StatementNode.foreignKeyOnDelete = 'models.CASCADE'
							elif constr.data == 'related_name':
								content = str(constr.children[0])
								StatementNode.related_name = f'"{content}"'
							elif constr.data == 'verbose_name':
								content = str(constr.children[0])
								StatementNode.verbose_name = f'"{content}"'

					elif StatementNode.type == 'varchar':
						varchar = datatype
						varcharnum = str(varchar.children[0])
						StatementNode.typenum = varcharnum
						if len(varchar.children) > 1:
							subtype = varchar.children[1]
							StatementNode.subtype = subtype.data
							if subtype.data == 'bcrypt_value':
								StatementNode.bcrypt_plaintext = str(subtype.children[0])
								StatementNode.subtype = 'bcrypt'

					elif StatementNode.type == 'integer':
						if len(datatype.children) > 0:
							'''
							column_type_spec
								integer
									random_int
										min_max
											min       1
											max       100
							column_type_spec
								integer
									random_number
										numdigits   5
							'''
							anak = datatype.children[0]
							if anak.data == 'random_int':
								StatementNode.subtype = anak.data
								mm = anak.children[0]
								for cucu in mm.children:
									if cucu.data == 'min':
										StatementNode.min = str(cucu.children[0])
									elif cucu.data == 'max':
										StatementNode.max = str(cucu.children[0])
							elif anak.data == 'pyfloat':
								'''
								i:f(4)			#.####
								i:f(4,2)	 ##.####
								'''
								StatementNode.subtype = anak.data
								mm = anak.children[0]
								for cucu in mm.children:
									if cucu.data == 'digitright':
										StatementNode.right = int(cucu.children[0])
									elif cucu.data == 'digitleft':
										StatementNode.left = int(cucu.children[0])
							elif anak.data == 'random_number':
								StatementNode.subtype = anak.data
								nd = anak.children[0]
								StatementNode.digits = int(nd.children[0])


					elif len(datatype.children) > 0:
						'''
						column_type_spec
							string
								password
						column_type_spec
							varchar
								255
								bcrypt_value  rahasia
						'''
						subtype = datatype.children[0]
						StatementNode.subtype = subtype.data
						if subtype.data == 'bcrypt_value':
							StatementNode.bcrypt_plaintext = str(subtype.children[0])
							StatementNode.subtype = 'bcrypt'
						

				elif branch.data == 'column_constraint_spec':
					'''
					N 			not null
					u 			unique
					'''
					StatementNode.hasConstraint = True

					for constraint in branch.children:

						if constraint.data == 'not_null':
							StatementNode.allowNull = False

						elif constraint.data == 'yes_null':
							StatementNode.allowNull = True

						elif constraint.data == 'yes_blank':
							StatementNode.blank = True

						elif constraint.data == 'no_blank':
							StatementNode.blank = False

						elif constraint.data == 'editable':
							StatementNode.editable = True

						elif constraint.data == 'no_editable':
							StatementNode.editable = False

						elif constraint.data == 'find_by':
							StatementNode.find_by = True

						elif constraint.data == 'yes_trim':
							StatementNode.trim = True
						elif constraint.data == 'yes_uppercase':
							StatementNode.upper = True
						elif constraint.data == 'yes_lowercase':
							StatementNode.lower = True
						elif constraint.data == 'yes_required':
							StatementNode.allowNull = False
						elif constraint.data == 'not_required':
							StatementNode.allowNull = True
						elif constraint.data == 'required_with_validation':
							validation_message = str(constraint.children[0])
							StatementNode.requiredWithValidation = QuoteChar + validation_message + QuoteChar

						elif constraint.data == 'unique':
							StatementNode.unique = True

						elif constraint.data == 'no_unique':
							StatementNode.unique = False

						elif constraint.data == 'auto_increment':
							StatementNode.auto_increment = True

						elif constraint.data == 'auto_now':
							StatementNode.auto_now = True

						elif constraint.data == 'auto_now_add':
							StatementNode.auto_now_add = True

						elif constraint.data == 'db_index':
							StatementNode.db_index = True

						elif constraint.data == 'min_length':
							nilai = str(constraint.children[0])
							StatementNode.min_length = nilai
							print('\n\n***ketemu min_length:', nilai, 'utk statement:', StatementNode.label)

						elif constraint.data == 'max_length':
							nilai = str(constraint.children[0])
							StatementNode.max_length = nilai
							print('\n\n***ketemu max length:', nilai, 'utk statement:', StatementNode.label)

						elif constraint.data == 'max_digits':
							nilai = str(constraint.children[0])
							StatementNode.max_digits = nilai
							# print('\n\n***ketemu max length:', nilai, 'utk statement:', StatementNode.label)

						elif constraint.data == 'decimal_places':
							nilai = str(constraint.children[0])
							StatementNode.decimal_places = nilai
							# print('\n\n***ketemu max length:', nilai, 'utk statement:', StatementNode.label)

						elif constraint.data == 'primary_key':
							'''
							sementara utk django dulu
							| "pk" pk_column_list?
							pk_column_list: ":" column_list
							column_list: column_name ("," column_name)*
							'''
							StatementNode.primaryKey = True
							# col_list = constraint.children[0]
							# pk = []
							# for constraint_detail in col_list.children:
							# 	if constraint_detail.data == 'column_name':
							# 		nama_pk = str(constraint_detail.children[0])
							# 		pk.append(nama_pk)
							# StatementNode.pk = pk

						elif constraint.data == 'django_foreign_key':
							'''
							namakolom,fk,rel.to.huruf,=d,rn=related_name,vn=verbose_name
							'''
							StatementNode.foreignKey = 'django fk'

						elif constraint.data == 'one_to_one':
							StatementNode.oneToOne = 'django 121'

						elif constraint.data == 'one_to_many':
							StatementNode.oneToMany = 'django 12m'

						elif constraint.data == 'many_to_many':
							StatementNode.manyToMany = 'django m2m'

						elif constraint.data == 'foreign_key':
							StatementNode.foreignKey = True
							for constraint_detail in constraint.children:

								if constraint_detail.data == 'schema_table_column_name':
									for detail in constraint_detail.children:
										name = str(detail.children[0])
										if detail.data == 'schemaname':
											StatementNode.fk_schema = name
										elif detail.data == 'tablename':
											StatementNode.fk_table = name
										elif detail.data == 'column_name':
											StatementNode.fk_column = name

								elif constraint_detail.data == 'action_list':
									for detail in constraint_detail.children:
										if detail.data == 'action_name':
											action_type = detail.children[0].data
											action_name = str(detail.children[0].children[0])
											StatementNode.fk_action = {
												action_type: action_name
											}

						elif constraint.data == 'references':
							rujukan_table = str(constraint.children[0])
							StatementNode.references = QuoteChar + rujukan_table + QuoteChar

						elif constraint.data == 'references_key':
							rujukan_kolom = str(constraint.children[0])
							StatementNode.referencesKey = QuoteChar + rujukan_kolom + QuoteChar

						elif constraint.data == 'column_constraint':

							for colcon in constraint.children:

								if StatementNode.type == 'enum' or StatementNode.type == 'string':
									enumvalues = []

									if colcon.data == 'enumvalues':
										for enumvalue in colcon.children:

											if enumvalue.data == 'enumvalue':
												enumval = str(enumvalue.children[0])
												debug('nilai enum:', enumval)
												enumvalues.append(QuoteChar + enumval + QuoteChar)

										StatementNode.values = enumvalues
										StatementNode.subtype = 'enumvalues'

									elif colcon.data == 'enumname':
										enumnameval = str(colcon.children[0])
										StatementNode.enumname = enumnameval

									elif colcon.data == 'enumdefault':
										enumdefault = str(colcon.children[0])
										debug('default enum:', enumdefault)
										StatementNode.defaultValue = QuoteChar + enumdefault + QuoteChar

									elif colcon.data == 'stringenumvalues': # sementara sama kode dg enumvalues
										for enumvalue in colcon.children:

											if enumvalue.data == 'enumvalue':
												enumval = str(enumvalue.children[0])
												debug('nilai enum:', enumval)
												enumvalues.append(QuoteChar + enumval + QuoteChar)

										StatementNode.values = enumvalues
										StatementNode.subtype = 'stringenumvalues'

									elif colcon.data == 'stringenumdefault':
										enumdefault = str(colcon.children[0])
										debug('default enum:', enumdefault)
										# StatementNode.defaultValue = QuoteChar + enumdefault + QuoteChar
										StatementNode.default = QuoteChar + enumdefault + QuoteChar

									elif colcon.data == 'nilai_default': # username,s,df=guest
										StatementNode.defaultValue = str(colcon.children[0])

								elif colcon.data == 'nilai_default':
									StatementNode.defaultValue = str(colcon.children[0])

				elif branch.data == 'sistem':
					pass
				elif branch.data == 'lingkungan':
					pass

				elif branch.data == 'has_one':
					pass
				elif branch.data == 'has_many':
					pass
				elif branch.data == 'belongs_to':
					pass
				elif branch.data == 'belongs_to_many':
					pass
					
				elif branch.data == 'one_to_one':
					pass
				elif branch.data == 'one_to_many':
					pass
				elif branch.data == 'many_to_one':
					pass
				elif branch.data == 'many_to_many':
					pass

				elif branch.data == 'primary_key_column':
					pass
				elif branch.data == 'foreign_key_column':
					pass

				elif branch.data == 'index_column':
					StatementNode.type = 'index'
					for cabang in branch.children:

						if cabang.data == 'column_name':
							StatementNode.label = str(cabang.children[0])

						elif cabang.data == 'direction_spec':
							direction = cabang.children[0].data
							StatementNode.index_direction = direction

						elif cabang.data == 'unique':
							StatementNode.index_unique = True						

		elif tree.data == 'configuration':

			# ConfigNode = AnyNode(name='config', type='config', parent=TableNode)
			# ConfigNode.tables = {}

			for ayah_jenis in tree.children:
				# if env_int('ULIBPY_FMUS_DEBUG'):
				# 	print('cari config_spec:', ayah_jenis)
				# for jenis in branch.children:
				# 	print('cari config ***:', jenis)

				if ayah_jenis.data == 'config_spec':
					for jenis in ayah_jenis.children:

						if jenis.data == 'config_name_number':
							config_name_spec = jenis.children[0]
							config_number_spec = jenis.children[1]
							number_of_data = config_number_spec.children[0]
							number_of_data_token = number_of_data.children[0]

							schema_or_table = config_name_spec.children[0]
							ber_schema = len(schema_or_table.children) == 2
							if ber_schema:
								schemaname = str(schema_or_table.children[0].children[0])
								tablename = str(schema_or_table.children[1].children[0])
								# ConfigNode.tables['schemaname'] = schemaname
								TableNode.schemaname = schemaname
							else:
								tablename = str(schema_or_table.children[0].children[0])

							# ConfigNode.tables['tablename'] = tablename
							TableNode.model = tablename

							fakernum = str(number_of_data_token)
							fakernos = int(fakernum)
							# ConfigNode.tables['fakernum'] = fakernos
							TableNode.faker = fakernos

						elif jenis.data == 'config_name_spec':
							schema_table = jenis.children[0]

							# print('temukan schema_table', schema_table)
							# input(' ')

							for name in schema_table.children:

								if name.data == 'schemaname':
									schemaname = str(name.children[0])
									TableNode.schemaname = schemaname

								elif name.data == 'tablename':
									tablename = str(name.children[0])
									TableNode.model = tablename

						elif jenis.data in ['has_one_syntax', 'belongs_to_syntax']:
							'''
							config_spec
								has_one_syntax
									assoc_table           User
									foreign_column        id
									domestic_column       user_id
									as_column             user
							'''
							if jenis.data == 'has_one_syntax':
								TableNode.has_or_belongs = 'has_one'
							else:
								TableNode.has_or_belongs = 'belongs_to'
							for turunan in anak_treeutils_func(jenis):
								if data(turunan) == 'assoc_table':
									TableNode.assoc_table = get_token(turunan)
								if data(turunan) == 'foreign_column':
									TableNode.foreign_column = get_token(turunan)
								if data(turunan) == 'domestic_column':
									TableNode.domestic_column = get_token(turunan)
								if data(turunan) == 'as_column':
									TableNode.as_column = get_token(turunan)

				elif ayah_jenis.data == 'config_timestamp_spec':
					TableNode.timestamp = True

				elif ayah_jenis.data == 'config_remove_attribute_id':
					TableNode.remove_attribute_id = True

				elif ayah_jenis.data == 'config_name_number':
					'''
					bisa ayah_jenis dan bisa jenis
					'''
					config_name_spec = ayah_jenis.children[0]
					config_number_spec = ayah_jenis.children[1]
					number_of_data = config_number_spec.children[0]
					number_of_data_token = number_of_data.children[0]

					schema_or_table = config_name_spec.children[0]
					ber_schema = len(schema_or_table.children) == 2
					if ber_schema:
						schemaname = str(schema_or_table.children[0].children[0])
						tablename = str(schema_or_table.children[1].children[0])
						# ConfigNode.tables['schemaname'] = schemaname
						TableNode.schemaname = schemaname
					else:
						tablename = str(schema_or_table.children[0].children[0])

					# ConfigNode.tables['tablename'] = tablename
					TableNode.model = tablename

					fakernum = str(number_of_data_token)
					fakernos = int(fakernum)
					# ConfigNode.tables['fakernum'] = fakernos
					TableNode.faker = fakernos


default_server_ip = env_get('ULIBPY_SERVERIP') or 'localhost'
default_server_port = env_get('ULIBPY_SERVERPORT') or '8000'
default_client_ip = env_get('ULIBPY_CLIENTIP') or 'localhost'
default_client_port = env_get('ULIBPY_CLIENTPORT') or '3000'
default_dbname = env_get('ULIBPY_DEFAULT_DBNAME') or 'tempdb'  # bisa gak kasih [/dbname] biar csvcode makin singkat

def process_language(code, debug):
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		debug(f'[langs.ucsv.processor.process_language] process_language, terima: [{code}]')
	parser = Lark(bahasa, start='keseluruhan').parse
	transformer = TheProcessor()
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		debug('='*10, code, '\n')
	parsed_tree = parser(code)
	transformed_tree = transformer.transform(parsed_tree)

	RootNode = AnyNode(type='root', label='root', output='', outputs=[])
	# 25/8/2022, jd default semua punya
	RootNode.serverport = default_server_port
	RootNode.serverip = default_server_ip
	RootNode.clientport = default_client_port
	RootNode.clientip = default_client_ip
	RootNode.dbname = default_dbname

	for insn in transformed_tree:

		# insn adlh database
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			debug(insn.pretty())

		for table_or_config in insn.children:

			if table_or_config.data == 'dbconfig':

				# RootNode.serverport = env_get('ULIBPY_SERVERPORT')
				# RootNode.serverip = env_get('ULIBPY_SERVERIP')
				# RootNode.clientport = env_get('ULIBPY_CLIENTPORT')
				# RootNode.clientip = env_get('ULIBPY_CLIENTIP')

				for configitem in table_or_config.children:
					if configitem.data == 'dbspec':
						dbname_tree = configitem.children[0]
						dbname = str(dbname_tree.children[0])
						RootNode.dbname = dbname
					elif configitem.data == 'backendspec':
						spec = get_token(configitem)
						for item in spec.split(','):
							if item.startswith('p'):
								item = item.removeprefix('p')
								if item.isdigit():
									if len(item) == 1:
										serverport = item + '000'
									else:
										serverport = item
								RootNode.serverport = serverport
							elif item.startswith('h'):
								item = item.removeprefix('h')
								if item == '0':
									serverip = '0.0.0.0'
								else:
									serverip = item
								RootNode.serverip = serverip
					elif configitem.data == 'frontendspec':
						spec = get_token(configitem)
						for item in spec.split(','):
							if item.startswith('p'):
								item = item.removeprefix('p')
								if item.isdigit():
									if len(item) in [1,2,3]:
										clientport = item + '0'*(3 if len(item)==1 else 2)
									else:
										clientport = item
								RootNode.clientport = clientport
							elif item.startswith('h'):
								item = item.removeprefix('h')
								if item == 0:
									clientip = '0.0.0.0'
								else:
									clientip = item
								RootNode.clientip = clientip
					elif configitem.data == 'hostport':
						for anak in configitem.children:
							if anak.data == 'host':
								token = str(anak.children[0])
								RootNode.host = token
							elif anak.data == 'port':
								token = str(anak.children[0])
								RootNode.port = int(token)
					elif configitem.data == 'userpass':
						for anak in configitem.children:
							if anak.data == 'user':
								token = str(anak.children[0])
								RootNode.username = token
							elif anak.data == 'pass':
								token = str(anak.children[0])
								RootNode.password = token
					elif data(configitem) == 'dbtype':
						dbtype = chdata(configitem)
						RootNode.dbtype = dbtype

			if table_or_config.data == 'table':
				process_table(RootNode, table_or_config, debug)

	return RootNode
