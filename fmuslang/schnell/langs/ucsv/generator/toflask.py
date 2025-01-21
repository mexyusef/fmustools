from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

sequelize_type_mapper = {
	'string':       'db.String',
    'varchar':      'db.String',
    'text':         'db.Text',
	'integer':      'db.Integer',
	'number':       'db.Numeric',
	'bigint':       'BIGINT',
	'boolean':      'db.Boolean',
	'date':         'db.Date',
	'float':        'db.Float',
	'double':       'DOUBLE',
	'timestamp':    'db.DateTime',
	'enum':         'ENUM',
}

model = ''
model_template = "__COLUMN_NAME__ = db.Column(__COLUMNS__)"
def to_flask(RootNode):
    for column in PreOrderIter(RootNode):
        # print('preoderiter:', column)
        if column.label != 'root':
            model_template.replace('__COLUMN_NAME__', column.label)
            columns = []
            if hasattr(column, 'hasConstraint') and column.hasConstraint == True: # complex type {}
                model[column.label] = {
                    'type': sequelize_type_mapper[column.type]
                }
                if hasattr(column, 'unique'):
                    columns .append('unique=True')
                if hasattr(column, 'allowNull'):
                    columns .append('nullable=True')
                if hasattr(column, 'primary_key'):
                    columns .append('primary_key=True')
                if hasattr(column, 'foreign_key'):
                    columns .append("db.ForeignKey('__FK_TABLE__.__FK_COLUMN__')")
            else: # simple type
                model[column.label] = sequelize_type_mapper[column.type]

    return model


