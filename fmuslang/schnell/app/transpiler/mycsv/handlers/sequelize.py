import json
from schnell.app.stringutils import tabify_content, default_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name

QuoteChar = '$$$'
ReplaceQuoteChar = '"'
EmptyReplaceQuoteChar = ''

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
	'django_foreign_key'    : '{ type: STRING, allowNull: false, references: "ModelRujukan", }',
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

def sequelize(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	columns = []
	for tblidx, tbl in enumerate(tables,1):
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		model = {}
		for colidx, column in enumerate(tbl.children):
			tipe_kolom_original = column.type
			nama_kolom = column.label
			tipe_kolom = type_mapper.get(tipe_kolom_original, tipe_kolom_original)
			constraints = []
			# ini duluan utk kasih key=col name ke dict model
			if hasattr(column, 'hasConstraint') and column.hasConstraint == True:
				model[column.label] = { 'type': tipe_kolom }
			else:
				model[column.label] = tipe_kolom
			if hasattr(column, 'relTo'):
				relation_model = column.relTo
				tipe_kolom = tipe_kolom.replace('ModelRujukan', relation_model)
			if hasattr(column, 'allowNull'):
				model[column.label] .update({ 'allowNull': column.allowNull })
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
				replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
				model[column.label] .update({ 'default': replacement })
				# pass
			if hasattr(column, 'defaultValue'):
				replacement = column.defaultValue.replace(QuoteChar, ReplaceQuoteChar)
				if replacement in ['False', 'True']:
					'''
					konversi ke js
					'''
					replacement = 'false' if replacement == 'False' else 'true'
				# else:
				# 	replacement = f'"{replacement}"'
				model[column.label] .update({ 'defaultValue': replacement })
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
				model[column.label] .update({ 'primaryKey': column.primaryKey })
			if hasattr(column, 'references'):				
				replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
				model[column.label] .update({ 'references': replacement })
				# pass
			if hasattr(column, 'referencesKey'):				
				replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
				model[column.label] .update({ 'referencesKey': replacement })
				# pass
			if hasattr(column, 'unique'):
				model[column.label] .update({ 'unique': column.unique })
			if hasattr(column, 'values'):
				'''
				values dan default menandakan enumvalues dan stringenumvalues
				item di dalamnya diapit QuoteChar $$$
				django perlu ganti $$$ ke empty
				node sequelize perlu ganti $$$ ke "
				'''
				replacement = [item.replace(QuoteChar, ReplaceQuoteChar) for item in column.values]
				model[column.label] .update({ 'values': replacement })
			if hasattr(column, 'subtype'):
				tipe_kolom = tipe_kolom.replace('__SUBTYPE__', type_mapper.get(column.subtype, column.subtype))
			if column.type == 'varchar' and hasattr(column, 'typenum'):
				tipe_kolom += f'({column.typenum})'

			item = f'{nama_kolom}: {tipe_kolom}'
			columns.append(item)

	hasil = json.dumps(model, indent=default_tab)
	kembali += "import Sequelize from 'sequelize';\n"
	kembali += "import { ARRAY, BIGINT, BOOLEAN, DATE, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, STRING, TEXT, UUID, UUIDV1, UUIDV4, } from 'sequelize';\n"
	kembali += f'const Todo = Sequelize.define(\n'
	tengah = f'"{tablename_lower}s",\n'
	# tengah += hasil.replace(ReplaceQuoteChar, '').replace('__DQ', '"') + '\n'
	tengah += hasil + '\n'
	tengah += f'{{ freezeTableName: true, schema: process.env.DB_SCHEMA, timestamps: false, }}'
	kembali +=  tabify_content(tengah)
	kembali += f'\n);'
	# fields = ', '.join(columns)
	# kembali += f'sequelize => {tablename_case}={tablename_lower} => {fields}'
	return kembali

