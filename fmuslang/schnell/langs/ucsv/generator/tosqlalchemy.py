import json
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

QuoteChar = '$$$'
ReplaceQuoteChar = '"'
exportname = 'ContohExport'
tablename = 'ContohTable'
schemaname = 'ContohSchema'

# import sqlalchemy.types.*
# https://docs.sqlalchemy.org/en/13/core/type_basics.html
sqlalchemy_type_mapper = {
	'string':       'String',    
	'varchar':      'Unicode',
	'text':       	'Text',
	'integer':      'Integer',
	'number':       'Numeric',
	'bigint':       'BigInteger',
	'smallint':     'SmallInteger',
	'float':        'Float',
	'double':       'DOUBLE',
	'uuid':       	'UUID',
	'uuid1':       	'UUIDV1',
	'uuid4':       	'UUIDV4',
	'boolean':      'Boolean',
	'date':         'Date',	
	'timestamp':    'DateTime',
	'enum':         'Enum',
	'serial':       f"Integer, Sequence('{tablename}_NAMAKOLOM_seq')",
}

def importify(model):
	prefix = 'from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey' + '\n'
	prefix += 'meta = MetaData()'
	prefix += '\n\n'
	suffix = ''
	return prefix + model + suffix

def to_alchemy(RootNode):
	print(f"---------------------------------{__file__}-------------------------------")
	all_fields = []
	model = ''
	model_extra = ''
	for column in PreOrderIter(RootNode):
		# print('preoderiter:', column)
		field = 'Column ('
		if column.label != 'root':
			# print('preoderiter:', column.label)
			default_get_type = sqlalchemy_type_mapper[column.type]
			if column.type == 'varchar' and hasattr(column, 'typenum'):
				default_get_type += f'({column.typenum})'
			field += f"'{column.label}', {default_get_type}" # column.label + ' ' + default_get_type

			if hasattr(column, 'unique'):
				field += ', unique=True'

			if hasattr(column, 'allowNull'):
				if column.allowNull == False:
					field += ', nullable=False'

			# if hasattr(column, 'references'):
			# 	replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
			# 	newfield = f'FOREIGN KEY ({column.label}) REFERENCES ({replacement})'
			# 	all_fields.append(newfield)

			if hasattr(column, 'primaryKey'):
				field += ", primary_key=True"
				# if hasattr(column, 'hasMultiplePrimaryKey'):
				# 	newfield = f'__FIND_THIS_FOR_PK_COLUMN__ PRIMARY KEY ({column.label} __FIND_THIS_FOR_NEXT_PK__)'
				# 	all_fields.append(newfield)
				# else:
				# 	field += ' PRIMARY KEY'
				
			# if hasattr(column, 'values'):
			# 	replacement = [item.replace(QuoteChar, ReplaceQuoteChar) for item in column.values]
			# 	flatten = '_'.join(replacement).replace(' ', '_').replace('"', '').replace("'", '')
			# 	stringified = ', '.join(replacement)

			# 	model_extra += f'CREATE TYPE {flatten} AS ENUM ({stringified})'
			# 	field += f' {flatten}'

			# if hasattr(column, 'default'):
			# 	replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
			# 	field += f' DEFAULT {replacement}'

			# if hasattr(column, 'defaultValue'):
			# 	replacement = column.defaultValue.replace(QuoteChar, ReplaceQuoteChar)
			# 	field += f' DEFAULT {replacement}'

			field += ')'
			# sanitasi
			field = field.replace('NAMAKOLOM', column.label)
			all_fields.append(field)

		else:
			# model += f'CREATE TABLE IF NOT EXISTS {tablename} ( __ALLFIELDS__ )'
			model += f'{tablename} = Table ("{tablename}", \n\tmeta, \n\t__ALLFIELDS__ \n)'

	# print('pre replace', model, all_fields)
	model = model.replace('__ALLFIELDS__', ',\n\t'.join(all_fields))
	# print('post replace', model)
	return '\n' + importify(model) + '\n'


