from schnell.app.stringutils import tabify_content
from schnell.app.transpiler.mycsv.handlers.common import default_table_name

type_mapper = {
	'array_of'              : 'ARRAY(__SUBTYPE__)',
	'empty_array'						: 'Array',
	'auto'                  : '{ type: Number, required: true, }',
	'bigint'                : 'BIGINT',
	'blob'                  : 'String',
	'boolean'               : 'BOOLEAN',
	'date'                  : 'DATE',
	'decimal'               : 'DECIMAL',
	'django_many_to_many'   : '[{ type: String }]',	
	'django_one_to_many'    : 'String',
	'django_one_to_one'     : '[{ type: String }]',
	'django_foreign_key'    : '{ type: STRING, allowNull: false, references: __DQModelRujukan__DQ, }',
	'double'                : 'DOUBLE',
	'enum'                  : 'ENUM',
	'float'                 : 'FLOAT',
	'image'                 : 'STRING',
	'integer'               : 'INTEGER',
	'number'                : 'DECIMAL',
	'serial'                : 'String',
	'slug'                  : 'STRING',
	'string'                : 'STRING',
	'text'                  : 'TEXT',
	'timestamp'             : '"TIMESTAMP"',
	'uuid'                  : 'UUID',
	'uuidv1'                : 'UUIDV1',
	'uuidv4'                : 'UUIDV4',
	'varchar'               : 'STRING',
}

def hibernate(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	columns = []
	for tblidx, tbl in enumerate(tables,1):
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
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
	kembali += f'hibernate => {tablename_case}={tablename_lower} => {fields}'
	return kembali
