import json
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

QuoteChar = '$$$'
ReplaceQuoteChar = '"'

postgres_type_mapper = {
	'string':       'STRING',    
	'varchar':      'VARCHAR',
	'text':       	'TEXT',
	'integer':      'INTEGER',
	'number':       'DECIMAL',
	'bigint':       'BIGINT',
	'float':        'FLOAT',
	'double':       'DOUBLE',
	'uuid':       	'UUID',
	'uuid1':       	'UUIDV1',
	'uuid4':       	'UUIDV4',
	'boolean':      'BOOLEAN',
	'date':         'DATE',	
	'timestamp':    'TIMESTAMP',
	'enum':         'ENUM',
	'serial':       'SERIAL',
}



sequelize_instance_path = "../helpers/sequelize"
exportname = 'ContohExport'
tablename = 'ContohTable'
schemaname = 'ContohSchema'

def to_sql(RootNode):
	print(f"---------------------------------{__file__}-------------------------------")
	all_fields = []
	model = ''
	model_extra = ''
	for column in PreOrderIter(RootNode):
		# print('preoderiter:', column)
		field = ''
		if column.label != 'root':
			# print('preoderiter:', column.label)
			default_get_type = postgres_type_mapper[column.type]
			if column.type == 'varchar' and hasattr(column, 'typenum'):
				default_get_type += f'({column.typenum})'
			field += column.label + ' ' + default_get_type

			if hasattr(column, 'unique'):
				field += ' UNIQUE'

			if hasattr(column, 'allowNull'):
				if column.allowNull == False:
					field += ' NOT NULL'

			if hasattr(column, 'references'):
				replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
				newfield = f'FOREIGN KEY ({column.label}) REFERENCES ({replacement})'
				all_fields.append(newfield)

			if hasattr(column, 'primaryKey'):
				if hasattr(column, 'hasMultiplePrimaryKey'):
					newfield = f'__FIND_THIS_FOR_PK_COLUMN__ PRIMARY KEY ({column.label} __FIND_THIS_FOR_NEXT_PK__)'
					all_fields.append(newfield)
				else:
					field += ' PRIMARY KEY'
			if hasattr(column, 'values'):
				replacement = [item.replace(QuoteChar, ReplaceQuoteChar) for item in column.values]
				flatten = '_'.join(replacement).replace(' ', '_').replace('"', '').replace("'", '')
				stringified = ', '.join(replacement)

				model_extra += f'CREATE TYPE {flatten} AS ENUM ({stringified})'
				field += f' {flatten}'

			if hasattr(column, 'default'):
				replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
				field += f' DEFAULT {replacement}'

			if hasattr(column, 'defaultValue'):
				replacement = column.defaultValue.replace(QuoteChar, ReplaceQuoteChar)
				field += f' DEFAULT {replacement}'

			all_fields.append(field)

		else:
			model += f'CREATE TABLE IF NOT EXISTS {tablename} (__ALLFIELDS__)'

	# print('pre replace', model, all_fields)
	model = model.replace(
		'__ALLFIELDS__', 
		'\n\t' + ',\n\t'.join(all_fields) + '\n'
		)
	# print('post replace', model)
	return '\n' + model + '\n'


