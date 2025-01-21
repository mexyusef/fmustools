from schnell.app.stringutils import tabify_content
from schnell.app.transpiler.mycsv.handlers.common import default_table_name

type_mapper = {
	'array_of'              : 'Array', 
	'empty_array'						: 'Array',
	'auto'                  : 'String',
	'bigint'                : 'String',
	'blob'                  : 'String',
	'boolean'               : 'Boolean',
	'date'                  : 'Date',
	'decimal'               : 'Schema.Types.Decimal128',
	'django_many_to_many'   : 'Schema.Types.ObjectId',
	'django_one_to_many'    : 'Schema.Types.ObjectId',
	'django_one_to_one'     : 'Schema.Types.ObjectId',
	'django_foreign_key'    : 'Schema.Types.ObjectId',
	'double'                : 'Number', 
	'enum'                  : 'String',
	'float'                 : 'Number',
	'image'                 : 'String',
	'integer'               : 'Number',
	'number'                : 'String',
	'serial'                : 'String',
	'slug'                  : 'String',
	'string'                : 'String',
	'text'                  : 'String',
	'timestamp'             : 'Date',
	'uuid'                  : 'Schema.Types.ObjectId',
	'uuidv1'                : 'Schema.Types.ObjectId',
	'uuidv4'                : 'Schema.Types.ObjectId',
	'varchar'               : 'String',   
}

def mongoose(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	columns = []
	for tblidx, tbl in enumerate(tables,1):
		# print('table anynode:', tbl)
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		for colidx, column in enumerate(tbl.children):
			# tipe_kolom = sequelize_type_mapper.get(column.type, column.type)
			tipe_kolom_original = column.type
			nama_kolom = column.label
			tipe_kolom = type_mapper.get(tipe_kolom_original, tipe_kolom_original)
			constraints = []
			if hasattr(column, 'relTo'):
				pass
			if hasattr(column, 'allowNull'):
				required = 'false' if column.allowNull else 'true'
				constraints.append(f'required: {required}')
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
				default = column.defaultValue
				if tipe_kolom_original == 'string':
					default = f'"{default}"'
				constraints.append(f'default: {default}')
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
			if constraints:
				constraint_list = ', '.join(constraints)
				tipe_kolom = f'{{ type: {tipe_kolom}, {constraint_list} }}'
			item = f'{nama_kolom}: {tipe_kolom}'
			columns.append(item)

	fields = ', '.join(columns)
	kembali += "import mongoose from 'mongoose';\n"
	kembali += "// const mongoose = require('mongoose');\n\n"
	kembali += f'const {tablename_lower}Schema = new mongoose.Schema({{\n'
	field_list = ',\n'.join(columns)
	kembali += tabify_content(field_list)
	kembali += '\n}, { timestamps: true });\n\n'
	# kembali += f'mongoose => {tablename_case}={tablename_lower} => {fields}'
	kembali += f'export default mongoose.model("{tablename_case}", {tablename_lower}Schema);\n'
	kembali += f'// module.exports = mongoose.model("{tablename_case}", {tablename_lower}Schema);'
	return kembali
