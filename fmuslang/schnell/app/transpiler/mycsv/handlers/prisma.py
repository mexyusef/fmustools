from schnell.app.stringutils import tabify_content_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name

# tambah @updatedAt

type_mapper = {
	'array_of'              : '[]', 
	'empty_array'			: 'Array',
	'auto'                  : 'String',
	'bigint'                : 'String',
	'blob'                  : 'String',
	'boolean'               : 'Boolean',
	'date'                  : 'Date',
	'decimal'               : 'String',
	'django_many_to_many'   : 'String',
	'django_one_to_many'    : 'String',
	'django_one_to_one'     : 'String',
	'django_foreign_key'    : 'String',
	'double'                : 'Number', 
	'enum'                  : 'String',
	'float'                 : 'Number',
	'image'                 : 'String',
	'integer'               : 'Int',
	'json'               	: 'Json',
	'number'                : 'String',
	'serial'                : 'String',
	'slug'                  : 'String',
	'string'                : 'String',
	'text'                  : 'String',
	'timestamp'             : 'DateTime',
	'uuid'                  : 'String',
	'uuidv1'                : 'String',
	'uuidv4'                : 'String',
	'varchar'               : 'String',   
}

info_database = """generator client {
	provider = "prisma-client-js"
}

datasource db {
	provider = "postgresql"
	// provider = "mysql"
	// provider = "mongodb"
	// url      = env("DATABASE_URL")
	// DATABASE_URL="postgresql://localhost:5432/tempdb?schema=public"
	// DATABASE_URL="mongodb+srv://acluster0.sxmukp6.mongodb.net/test"
	url      = "postgresql://localhost:5432/tempdb?schema=public"
}


// npx prisma migrate dev --name init

"""

def prisma(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	columns = []
	# database = tables.parent # tuple has no parent
	# print('rootnode:', database)
	for tblidx, tbl in enumerate(tables,1):
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		has_enums = []
		for colidx, column in enumerate(tbl.children):
			# tipe_kolom = sequelize_type_mapper.get(column.type, column.type)
			tipe_kolom_original = column.type
			nama_kolom = column.label
			tipe_kolom = type_mapper.get(tipe_kolom_original, tipe_kolom_original)
			constraints = []
			if hasattr(column, 'relTo'):
				# AnyNode(foreignKey=True, foreignKeyOnDelete='models.CASCADE', hasConstraint=False, label='user_id', relTo='User', type='django_foreign_key')
				if column.type == 'django_foreign_key':
					# user User @relation(fields: [user_id], reference: [id])
					# user_id Int
					# user_id adlh kolom here (us) di table apapun nama table kita, dan id adlh kolom there (foreign) di table User

					# kita bikin fk/User.id/d=cascade utk hasilkan table sana = User, dg kol nya: id
					# padanan di sini adlh user_id
					table_disana = column.relTo
					id_disana = 'id'
					if '.' in column.relTo:
						table_disana, id_disana = column.relTo.split('.')
					kolom_disini = f'{table_disana.lower()}_{id_disana}'
					tipe_kolom = table_disana # User
					# @relation(fields: [user_id], reference: [id])
					attr = f'@relation(fields: [{kolom_disini}], references: [{id_disana}])'
					constraints.append(attr)
					# tambah kolom baru, kolom_disini
					columns.append(f'{kolom_disini:<15} Int')
			if hasattr(column, 'allowNull'):
				if column.allowNull:
					tipe_kolom += '?' # https://youtu.be/mU8-nKwfw4Y?t=1746
			if hasattr(column, 'auto_increment'):
				item = '@default(autoincrement())'
				constraints.append(item)
			if hasattr(column, 'auto_now'):
				item = '@default(now())'
				constraints.append(item)
			if hasattr(column, 'auto_now_add'):
				item = '@default(now())'
				constraints.append(item)
			if hasattr(column, 'blank'):
				pass
			if hasattr(column, 'editable'):
				pass
			if hasattr(column, 'default'):
				'''
				values dan default menandakan enumvalues dan stringenumvalues
				item di dalamnya diapit QuoteChar $$$
				django perlu ganti $$$ ke empty
				node sequelize perlu ganti $$$ ke "
				'''
				# replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
				# model[column.label] .update({ 'default': replacement })
				pass
			if hasattr(column, 'defaultValue'):
				# nilai = 'true' if column.defaultValue else 'false'
				nilai = column.defaultValue
				item = f'@default("{nilai}")'
				constraints.append(item)
			if hasattr(column, 'db_index'):
				pass
			if hasattr(column, 'foreignKeyOnDelete'):
				pass
			if hasattr(column, 'max_length'):
				nilai = column.max_length
				item = f'@db.VarChar({nilai})'
				constraints.append(item)
			if hasattr(column, 'max_digits'):
				pass
			if hasattr(column, 'decimal_places'):
				pass
			if hasattr(column, 'related_name'):
				pass
			if hasattr(column, 'verbose_name'):
				pass
			if hasattr(column, 'primaryKey'):
				item = '@id'
				constraints.append(item)
			if hasattr(column, 'references'):
				pass
				# replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
				# model[column.label] .update({ 'references': replacement })
			if hasattr(column, 'referencesKey'):
				pass
				# replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
				# model[column.label] .update({ 'referencesKey': replacement })
			if hasattr(column, 'unique'):
				item = '@unique'
				constraints.append(item)
			if hasattr(column, 'values'):
				'''
				{@Book}title,s;year,dt;author,s;category,s,(good,bad,excellent,horrible>good)
				AnyNode(label='root', output='', outputs=[], type='root')
				└── AnyNode(model='Book', name='table', type='table')
						├── AnyNode(hasConstraint=False, label='title', type='string')
						├── AnyNode(hasConstraint=False, label='year', type='date')
						├── AnyNode(hasConstraint=False, label='author', type='string')
						└── AnyNode(default='$$$good$$$', hasConstraint=True, 
							label='category', subtype='stringenumvalues', type='string', 
							values=['$$$good$$$', '$$$bad$$$', '$$$excellent$$$', '$$$horrible$$$'])
				'''
				from schnell.app.stringutils import tabify_contentlist_tab
				new_enum = '''enum __ENUM_NAME {\n__ENUMCONTENT\n}'''
				nama_enum = column.label.capitalize()
				tanda_tanya = '?' if (not hasattr(column, 'allowNull') or column.allowNull==True) else ''
				tipe_kolom = nama_enum + tanda_tanya
				new_enum = new_enum.replace('__ENUM_NAME', nama_enum)
				content = [item.replace('$$$','') for item in column.values]
				content = tabify_contentlist_tab(content)
				new_enum = new_enum.replace('__ENUMCONTENT', content)
				has_enums.append(new_enum)				
			# handle array
			if column.type == 'array_of' and hasattr(column, 'subtype'):
				subtype = type_mapper[column.subtype]
				tipe_kolom = f'{subtype}[]'
			if constraints:
				constraint_list = ' '.join(constraints)
				tipe_kolom = f'{tipe_kolom:<10} {constraint_list}'
			item = f'{nama_kolom:<15} {tipe_kolom}'
			columns.append(item)

	kembali += info_database
	if has_enums:
		kembali += '\n'.join(has_enums) + '\n\n'
	kembali += f'model {tablename_case} {{\n'
	field_list = '\n'.join(columns)
	kembali += tabify_content_tab(field_list)
	kembali += '\n}'
	# kembali += '\n'
	# fields = ', '.join(columns)
	# kembali += f'prisma => {tablename_case}={tablename_lower} => {fields}'
	return kembali

