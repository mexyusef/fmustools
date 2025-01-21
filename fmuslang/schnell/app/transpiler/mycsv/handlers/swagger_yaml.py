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

template_yaml_definitions = """components:
  schemas:
    __TABLENAME_CASE__:
    __TABLENAME_CASE__nput:
"""

template_yaml_paths = """paths:
  /__TABLENAME_PLURAL_LOWER__:
    get:
__CRUD_LIST__
    post:
__CRUD_CREATE__
  /__TABLENAME_PLURAL_LOWER__/{id}:
    get:
__CRUD_DETAIL__
    post:
__CRUD_UPDATE__
    delete:
__CRUD_DELETE__
"""

template_yaml = """
openapi: 3.0.0
info:
  title: Todo API
  description: A simple API for managing todos
  version: 1.0.0
servers:
  - url: http://localhost:8000
__PATHS__
__DEFINITIONS__

"""

def swagger_yaml(tables):
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
		# kembali += f'swagger_yaml => {tablename_case}={tablename_lower} => {fields}'
		records = (template_yaml
			.replace('__PATHS__', 
	    		template_yaml_paths.replace('__TABLENAME_PLURAL_LOWER__', tablename_plural_lower))
			.replace('__DEFINITIONS__', 
	    		template_yaml_definitions.replace('__TABLENAME_CASE__', tablename_case)
			)
		)
		unprocessed.append(f"{records}")
	
	kembali += '\n\n\n'.join(unprocessed)

	return kembali
