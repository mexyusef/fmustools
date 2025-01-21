#   // images: { type: Array, required: false, default: [] },
# __TEMPLATE_MONGOSE_FIELDS__
import json
from schnell.app.usutils import tab
from schnell.app.printutils import print_json, indah4
from schnell.app.stringutils import tabify_content, tabify_contentlist, tabify_contentlist_space, tabify_contentlist_tab
from schnell.app.libpohon.handlers import (
	# type_mapper,
	get_tipe_kolom,
	column_attrs,
)
from schnell.app.typemapper import type_mapper_by_provider
from schnell.app.appconfig import libpohon_data

PROVIDER_REMOVE_ID = [
	'proshop_mongo',
	'node_antd_mongo',
]

def columnify(tables, provider='django', skip_columns={}):
	"""
	UPDATE:
	bisa skip columns
	{
		tablename: [column,column]
	}
	{
		User: [username, name, email]
	}
	if (tablename in skip_columns) and (column.label in skip_columns[tablename]):
		continue

	pengganti generate model universal
	contoh pake:
	app.transpiler.csv.handlers.help_nest_mongo
	"""
	tables_with_columns = {}
	table_attributes = {}
	for tblidx, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		columns_with_types = []
		columns_names = []
		columns_types = []
		columns_types_original = []
		columns_attributes = []
		for colidx, column in enumerate(tbl.children):
			# mapper = type_mapper.get(provider, 'default')
			# tipe_kolom = mapper.get(column.type, column.type)
			if (tablename_case in skip_columns) and (column.label in skip_columns[tablename_case]):
				continue
			if column.label == '_id':
				if provider in PROVIDER_REMOVE_ID:
					continue
			columns_types_original.append(column.type)
			tipe_kolom = get_tipe_kolom(column, provider)
			nama_kolom = column.label
			coltype = f'{nama_kolom}: {tipe_kolom}'
			colname = nama_kolom

			res = column_attrs(column, provider, tablename_case)
			if provider in ['django', 'django_mongo']:
				# cek jk perlu gunakan AutoField untuk auto_increment
				if libpohon_data['django_auto_request']:
					libpohon_data['django_auto_request'] = False
					tipe_kolom = 'models.AutoField'
					coltype = f'{nama_kolom}: {tipe_kolom}'
				elif tipe_kolom == 'models.CharField':
					# kembali = f'max_length={column.max_length}'
					# res = colattrs.append(kembali)
					ada_maxlen = [item for item in res if item.startswith('max_length')]
					if not ada_maxlen:
						res .append('max_length=255')
				elif tipe_kolom == 'JSONField':
					# print('res yg hrs dioprek skrg adlh:', res)
					# input('..sila gagalkan ini')
					# columns_attributes.extend(['default=list', 'blank=True', 'null=True'])
					res.extend(['default=list', 'blank=True', 'null=True'])					
			elif provider in ['flask', 'flask_mongo']:
				if tipe_kolom == 'String':
					ada_maxlen = [item for item in res if item.startswith('max_length')]
					if not ada_maxlen:
						tipe_kolom = f'{tipe_kolom}(128)'

			# if res:
			# 	columns_attributes.append(res) # jadi list of list
			columns_attributes.append(res)
			columns_with_types.append(coltype)
			columns_names.append(colname)
			columns_types.append(tipe_kolom)

		tables_with_columns[tablename_case] = {
			'columns_attributes': columns_attributes, # list of list
			'columns_with_types': columns_with_types,
			'columns_names': columns_names,
			'columns_types': columns_types,
			'table_attributes': table_attributes,
			'columns_types_original': columns_types_original,
		}
	return tables_with_columns


def transform_columns(tablenamecase, tables_with_columns, provider):
	"""
	processor dari columnify's result

	tables_with_columns = dict jk diindex dg nama table maka peroleh hasil columnify

	dari hasil columnify
	menjadi bentuk:
	nama = Field(attr1=a,attr2=a)
	atau:
	nama1: jenis1;
	nama2: jenis2;
	sudah terdelimit dg \n atau ; atau ,
	tapi belum tabified
	"""
	kembali = ''
	dapatkan = tables_with_columns[tablenamecase]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']
	# user,fk/User/d=cascade;								relTo = User
	# track,fk/Track/d=cascade/rn=likes;		relTo = Track
	# [['User'], ['Track']]
	attrs = dapatkan['columns_attributes']

	if provider == 'default':
		kembali += ''
	elif provider in ['django', 'django_mongo']:
		TIMESTAMPED_BASE_MODEL = 'TimestampedModel'
		DEFAULT_BASE_MODEL = 'models.Model'
		attrs = [', '.join(item) for item in attrs]
		# delim = ','
		res = [f'{names[index].ljust(15)} = {jenis[index]}({item})' for index, item in enumerate(attrs)]
		res = sorted(res)
		kembali = f'\n'.join(res)
	elif provider in ['flask', 'flask_mongo']:
		formatted = []
		for index, nama in enumerate(names):
			terpetakan = 'db.' + jenis[index]
			if terpetakan .startswith('db.ForeignKey'):
				terpetakan = terpetakan.replace('db.ForeignKey', 'db.Integer, db.ForeignKey')
				# relation_to
				relation_to = attrs[index].pop()
				terpetakan += relation_to
			hasil = f"db.Column({terpetakan}__CONSTRAINTS_HOLDER__)"
			# attrs = [''.join(item) for item in attrs if item]
			try:
				string_attrs = ', '.join(attrs[index])
			except Exception as err:
				print(f"""
				masalah pada:
				attrs adlh: {attrs}
				index adlh: {index}
				nama adlh: {nama}
				names adlh: {names}
				hasil adlh: {hasil}
				""")
				raise Exception(err)
			if string_attrs:
				string_attrs = ', ' + string_attrs # agar constraint holder dipisah ,
			hasil = hasil.replace('__CONSTRAINTS_HOLDER__', string_attrs)
			field = f"{nama.ljust(15)} = {hasil}"			
			formatted.append(field)

		# informasi tambahan:
		# list of list = attrs yg kita punya:
		# {attrs}
		# """
		oprek = sorted(formatted) # list
		res = tabify_contentlist_space(oprek) # string
		# indah4(f'''
		# hasil tabify contentlist utk flask:
		# input = {oprek}
		# output = {res}
		# ''', warna='green')
		# input('... flask ...')
		kembali = res # kembalian 'generated_fields' harus string
	elif provider in ['nest', 'nest_mongo']:
		# required = 'false' if not required else 'true'
		jenis = [f'type: {item}' for item in jenis]		
		# flatten 1 dari list of list ke list of str
		flat_attrs = [', '.join(item) for item in attrs]
		delim = ','
		res = [f'{names[index]}: {{ {jenis[index]}, {item} }}' for index, item in enumerate(flat_attrs)]
		# res = [f'{names[index]}: {{ {item} }}' for index, item in enumerate(jenis_attrs)]
		# res = [f'{names[index]}: {{ {item} }}' for index, item in enumerate(gabung)]
		res = sorted(res)
		kembali = f'{delim}\n'.join(res) + delim
	elif provider in ['node_antd', 'node_antd_mongo', 'proshop_mongo']:
		# flat_attrs = [', '.join(item) for item in attrs]
		# model = dict(zip(names, flat_attrs))
		# kembali = json.dumps(model, indent=tab())
		cols = []
		attrs = [', '.join(item) for item in attrs]
		for idx, item in enumerate(attrs):
			nama = names[idx]
			jenisitem = jenis[idx]
			if item:
				col = f'{nama}: {{ type: {jenisitem}, {item} }}'
			else:
				col = f'{nama}: {jenisitem}'
			cols.append(col)
		res = sorted(cols)
		kembali = '{\n' + tabify_contentlist(res, num_tab=2, delim=',\n') + '\n\t}'
	elif provider == 'struct_ts':
		delim = ';'
		res = [f'{names[index]}: {item}' for index, item in enumerate(jenis)]
		res = sorted(res)
		kembali = f'{delim}\n'.join(res) + delim
	elif provider == 'struct_java':
		delim = ';'
		# res = [f'this.{names[index]} = {item}' for index, item in enumerate(jenis)]
		res = [f'private final {item} {names[index]}' for index, item in enumerate(jenis)]
		# res = sorted(res)
		kembali = f'{delim}\n'.join(res) + delim
	elif provider == 'struct_go':
		# delim = ';'
		# res = [f'this.{names[index]} = {item}' for index, item in enumerate(jenis)]
		res = [f'{names[index]:<15} {item:<10} `json:"{names[index].lower()}"`' for index, item in enumerate(jenis)]
		# res = sorted(res)
		kembali = f'\n'.join(res)
	elif provider in ['react_bootstrap_form1']:
		kembali = '\n\n'.join(jenis)
	return kembali


def columnify_and_transform(tables, provider, which_table):
	"""
	tables
	provider
	which_table
		maksudnya tablename atau tablenamecase

	columnify
		hasilkan metadata berisi nama kolom, atribut kolom, dst
	transform
		bentuk ke output yg bisa digunakan oleh provider
	
	template_node_app_content = app_content(tablename, file_content(joiner(disini, 'templates/django_model.tpl')))
	generated_fields = columnify_and_transform(self.tables, 'django', tablename)
	generated_fields = tabify_content(generated_fields)
	per_table = template_node_app_content.replace('__FIELDS__', generated_fields)

	jelasnya lihat contoh yg menggunakan:
	for meja in self.tables:
		tablename = meja.model
		generated_fields = columnify_and_transform(self.tables, 'django', tablename)

	./app/transpiler/frontend/fslang/django/__init__.py:                    generated_fields = columnify_and_transform(self.tables, 'django', tablename)
	./app/transpiler/frontend/fslang/django/__init__.py:                    generated_fields = columnify_and_transform(self.tables, 'django', tablename)
	./app/transpiler/frontend/fslang/django_mongo/__init__.py:				generated_fields = columnify_and_transform(self.tables, 'django', tablename)
	./app/transpiler/frontend/fslang/django_mongo/__init__.py:				generated_fields = columnify_and_transform(self.tables, 'django', tablename)

	./app/transpiler/frontend/fslang/fastapi/__init__.py:      				generated_fields = columnify_and_transform(self.tables, 'fastapi', tablename)
	./app/transpiler/frontend/fslang/flask/models/__init__.py:              generated_fields = columnify_and_transform(tables, 'flask', tablename)
	./app/transpiler/frontend/fslang/flask/__init__.py:      				generated_fields = columnify_and_transform(self.tables, 'flask', tablename)
	./app/transpiler/frontend/fslang/micronaut_mongo/__init__.py:      		generated_fields = columnify_and_transform(self.tables, 'nest', tablename)
	./app/transpiler/frontend/fslang/moleculer/__init__.py:      			generated_fields = columnify_and_transform(self.tables, 'moleculer', tablename)
	./app/transpiler/frontend/fslang/nest/__init__.py:      				generated_fields = columnify_and_transform(self.tables, 'nest', tablename)
	./app/transpiler/frontend/fslang/nest_mongo/__init__.py:      			generated_fields = columnify_and_transform(self.tables, 'nest', tablename)
	./app/transpiler/frontend/fslang/node_antd/__init__.py:                 generated_fields = columnify_and_transform(self.tables, 'node_antd', tablename)
	./app/transpiler/frontend/fslang/node_antd_mongo/__init__.py:      		generated_fields = columnify_and_transform(self.tables, 'node_antd_mongo', tablename)
	./app/transpiler/frontend/fslang/node_apollo/__init__.py:				generated_fields = columnify_and_transform(self.tables, 'node_apollo', tablename)
	./app/transpiler/frontend/fslang/springboot/__init__.py:				generated_fields = columnify_and_transform(self.tables, 'springboot', tablename)
	./app/transpiler/frontend/fslang/springboot_mongo/__init__.py:      	generated_fields = columnify_and_transform(self.tables, 'nest', tablename)
	./app/transpiler/frontend/fslang/utils/proshop_backend/__init__.py:		generated_fields = columnify_and_transform(self.tables, self.provider, tablename)
	./app/transpiler/frontend/fslang/utils/proshop_node/__init__.py:		generated_fields_trx = columnify_and_transform(self.tables, self.provider, tablename)
	./app/transpiler/frontend/fslang/utils/proshop_routes/__init__.py:    	generated_fields = columnify_and_transform(self.tables, self.provider, tablename)

	"""
	hasil_columnify = columnify(tables, provider)
	indah4(f'{provider}: hasil_columnify:', warna='white', layar='blue')
	print_json(hasil_columnify)

	hasil_transform = transform_columns(which_table, tables_with_columns=hasil_columnify, provider=provider)
	indah4(f'{provider}: hasil_transform:', warna='white', layar='blue')
	print_json(hasil_transform)

	# input(' ...')

	return hasil_transform


def transform_table(tablename_case, hasil_columnify, provider):
	return transform_columns(tablename_case, tables_with_columns=hasil_columnify, provider=provider)


def generate_form_fields_per_table(self_tables, per_table, tablename, provider='react_bootstrap_form1', field_keyword='__FIELDS__', jumlah_tab=2):
	"""
	from schnell.app.libpohon import acmfile
	for tbl in self.tables:
		tablename = ...
		per_table = acmfile(tablename, disini, 'templatecontent.tpl')
		per_table berisi __FIELDS__ dkk
		per_table = generate_form_fields_per_table(self.tables, per_table, tablename, 'react_antd_form1', '__TABLE_COLUMNS__', 4)
		self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
	"""
	from schnell.app.stringutils import tabify_content_tab
	generated_fields = columnify_and_transform(self_tables, provider, tablename)
	generated_fields = tabify_content_tab(generated_fields, num_tab=jumlah_tab)
	# input(f"\n\nHasil tabify utk form adlh: [{generated_fields}]")
	return per_table.replace(field_keyword, generated_fields)

