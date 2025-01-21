from schnell.app.stringutils import tabify_content
from schnell.app.transpiler.mycsv.handlers.common import default_table_name

type_mapper = {
	# 'array_of'            : 'ARRAY(__SUBTYPE__)',
	'array_of'				: '__SUBTYPE__[]',
	'empty_array'			: '[]',
	'auto'                  : '{ type: Number, required: true, }',
	'bigint'                : 'BIGINT',
	'blob'                  : 'STRING',
	'boolean'               : 'BOOLEAN',
	'date'                  : 'DATE',
	'decimal'               : 'DECIMAL',
	'django_many_to_many'   : '[{ type: STRING }]',	
	'django_one_to_many'    : 'STRING',
	'django_one_to_one'     : '[{ type: STRING }]',
	'django_foreign_key'    : '{ type: STRING, allowNull: false, references: __DQModelRujukan__DQ, }',
	'double'                : 'DOUBLE',
	'enum'                  : 'ENUM',
	'float'                 : 'FLOAT',
	'image'                 : 'STRING',
	'integer'               : 'INTEGER',
	'number'                : 'DECIMAL',
	'serial'                : 'STRING',
	'slug'                  : 'STRING',
	'string'                : 'STRING',
	'text'                  : 'TEXT',
	'timestamp'             : '"TIMESTAMP"',
	'uuid'                  : 'UUID',
	'uuidv1'                : 'UUIDV1',
	'uuidv4'                : 'UUIDV4',
	'varchar'               : 'STRING',
}

template_postman_definitions = """"definitions": {
	"__TABLENAME_CASE__": {
	}
	"__TABLENAME_CASE__Input": {
	}
}
"""

template_postman_paths = """{
	"name": "__PATH_CRUD__",
	"event": [
__PATH_EVENT_ITEMS__
	],
	"request": {
__PATH_REQUEST_ITEM__
	},
	"response": [
__PATH_RESPONSE_ITEM__
	]
}"""

template_postman = """
{
  "info": {
	"_postman_id": "__UUID__",
	"name": "__TITLE__",
	"description": "__DESCRIPTION__",
	"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
__CRUD_SPECS__
  ]
}

"""

def swagger_postman(tables):
	kembali = ''
	unprocessed = []
	tablename_lower, tablename_case, tablename_cap, tablename_plural_lower = '','', '', ''
	for tblidx, tbl in enumerate(tables,1):
		columns = []
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		tablename_lower = tbl.model.lower()
		tablename_plural_lower = tablename_lower + 's'
		tablename_case = tbl.model
		tablename_cap = tbl.model.capitalize()
		for colidx, column in enumerate(tbl.children):
			# tipe_kolom = type_mapperper.get(column.type, column.type)
			tipe_kolom = column.type
			nama_kolom = column.label
			if hasattr(column, 'relTo'):
				pass
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
				pass
			if hasattr(column, 'db_index'):
				pass
			if hasattr(column, 'foreignKeyOnDelete'):
				pass
			if hasattr(column, 'max_length'):
				pass
			if hasattr(column, 'max_digits'):
				pass
			if hasattr(column, 'decimal_places'):
				pass
			if hasattr(column, 'related_name'):
				pass
			if hasattr(column, 'verbose_name'):
				pass
			if hasattr(column, 'primaryKey'):
				pass
			if hasattr(column, 'references'):				
				# replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
				# model[column.label] .update({ 'references': replacement })
				pass
			if hasattr(column, 'referencesKey'):				
				# replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
				# model[column.label] .update({ 'referencesKey': replacement })
				pass
			if hasattr(column, 'unique'):
				pass
			if hasattr(column, 'values'):
				pass
			item = f'{nama_kolom}: {tipe_kolom}'
			columns.append(item)

		fields = ', '.join(columns)
		template_postman_paths_list = []
		for path in ['list', 'create']:
			item = template_postman_paths.replace('__PATH_CRUD__', f"This is the path for {path.capitalize()}")
			template_postman_paths_list.append(item)
		for path in ['detail', 'update', 'delete']:
			item = template_postman_paths.replace('__PATH_CRUD__', f"This is the path for {path.capitalize()}")
			template_postman_paths_list.append(item)
		gabung = ',\n'.join(template_postman_paths_list)
		records = (template_postman.replace('__CRUD_SPECS__', gabung))
		unprocessed.append(f"{records}")
	
	kembali += '\n\n\n'.join(unprocessed)

	return kembali
