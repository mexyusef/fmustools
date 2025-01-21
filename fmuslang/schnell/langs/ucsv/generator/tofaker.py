from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

sequelize_type_mapper = {
	'string':       'STRING',
	'integer':      'INTEGER',
	'number':       'NUMBER',
	'bigint':       'BIGINT',
	'boolean':      'BOOLEAN',
	'date':         'DATE',
	'float':        'FLOAT',
	'double':       'DOUBLE',
	'timestamp':    '$$$TIMESTAMP$$$',
	'enum':         'ENUM',
}

model = {}

def tosequelize(RootNode):
    for column in PreOrderIter(RootNode):
        # print('preoderiter:', column)
        if column.label != 'root':
            # print('preoderiter:', column.label)
            if hasattr(column, 'hasConstraint') and column.hasConstraint == True: # complex type {}
                model[column.label] = {
                    'type': sequelize_type_mapper[column.type]
                }
                if hasattr(column, 'unique'):
                    model[column.label] .update({ 'unique': column.unique })
                if hasattr(column, 'allowNull'):
                    model[column.label] .update({ 'allowNull': column.allowNull })
                if hasattr(column, 'default'):
                    model[column.label] .update({ 'defaultValue': column.default })
            else: # simple type
                model[column.label] = sequelize_type_mapper[column.type]

    return model


