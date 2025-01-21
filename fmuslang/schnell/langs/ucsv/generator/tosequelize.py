import json
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

QuoteChar = '$$$'
ReplaceQuoteChar = '"'

sequelize_type_mapper = {
	'string':       'STRING',
	'varchar':      'STRING',
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
	'timestamp':    ReplaceQuoteChar + 'TIMESTAMP' + ReplaceQuoteChar,
	'enum':         'ENUM',
}

model = {}

sequelize_instance_path = "../helpers/sequelize"
exportname = 'ContohExport'
tablename = 'ContohTable'
schemaname = 'ContohSchema'

def importify(model):
	prefix1 = f'const sequelize = require("{sequelize_instance_path}")\n'
	prefix2 = 'const { BIGINT, BOOLEAN, DATE, DOUBLE, ENUM, FLOAT, INTEGER, STRING, TEXT, UUID, UUIDV1, UUIDV4 } = require("sequelize")\n\n'
	prefix3 = f'''const {exportname} = sequelize.define(\n"{tablename}",\n'''
	prefix = prefix1 + prefix2 + prefix3
	suffix1 = f"""{{
	freezeTableName: true,
	schema: "{schemaname}",
	timestamps: false,
}}
)\n"""
	suffix2 = f'module.exports = {exportname}'

#     if 'content' in run_configuration:
# 		mid_suffix = f"""
# {exportname}.{run_configuration['content']}
# """
# 		suffix2 = mid_suffix + suffix2

	suffix = suffix1 + suffix2
	return prefix + model + ",\n" + suffix

def tosequelize(RootNode):
	print(f"---------------------------------{__file__}-------------------------------")
	for column in PreOrderIter(RootNode):
		# print('preoderiter:', column)
		if column.label != 'root':
			# print('preoderiter:', column.label)
			if hasattr(column, 'hasConstraint') and column.hasConstraint == True: # complex type {}
				default_get_type = sequelize_type_mapper[column.type]
				if column.type == 'varchar' and hasattr(column, 'typenum'):
					default_get_type += f'({column.typenum})'
				model[column.label] = {
					'type': default_get_type
				}
				if hasattr(column, 'unique'):
					model[column.label] .update({ 'unique': column.unique })
				if hasattr(column, 'allowNull'):
					model[column.label] .update({ 'allowNull': column.allowNull })
				if hasattr(column, 'references'):
					replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
					model[column.label] .update({ 'references': replacement })
				if hasattr(column, 'referencesKey'):
					replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
					model[column.label] .update({ 'referencesKey': replacement })
				if hasattr(column, 'primaryKey'):
					model[column.label] .update({ 'primaryKey': column.primaryKey })
				if hasattr(column, 'values'):
					replacement = [item.replace(QuoteChar, ReplaceQuoteChar) for item in column.values]
					model[column.label] .update({ 'values': replacement })
				if hasattr(column, 'default'):
					replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
					model[column.label] .update({ 'default': replacement })
				if hasattr(column, 'defaultValue'):
					replacement = column.defaultValue.replace(QuoteChar, ReplaceQuoteChar)
					model[column.label] .update({ 'defaultValue': replacement })
				
			else: # simple type				
				default_get_type = sequelize_type_mapper[column.type]
				if column.type == 'varchar' and hasattr(column, 'typenum'):
					default_get_type += f'({column.typenum})'
				model[column.label] = default_get_type

	# return importify(model)
	return '\n' + importify(json.dumps(model, indent=4)) + '\n'
