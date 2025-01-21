
type_mapper = {
	'empty_array': {
		'mongoose'				: '[]',
		'sequelize'				: 'ARRAY',
	},
	'array_of':	{
		'mongoose'				: 'Array',
		'sequelize'				: 'ARRAY(__SUBTYPE__)',
	},
	'auto': {
		'django'				: 'models.AutoField',
		'flask'					: 'sqlalchemy.Integer',
		'graphene'				: 'graphene.ID',
		'pydantic'				: 'int',
		'sequelize'				: '{ type: Number, required: true, }',
		'sqlalchemy'			: 'Integer',
	},
	'bigint': {
		'django'				: 'BIGINT',
		'flask'					: 'sqlalchemy.Integer',
		'graphene'				: 'graphene.Int',
		'pydantic'				: 'int',
		'sequelize'				: 'BIGINT',
		'sqlalchemy'			: 'Integer',
	},
	'blob': {},
	'boolean': {
		'django'				: 'models.BooleanField',
		'flask'					: 'sqlalchemy.Boolean',
		'graphene'				: 'graphene.Boolean',
		'mongoose'				: 'Boolean',
		'pydantic'				: 'bool',
		'sboot'					: 'Boolean',
		'sequelize'				: 'BOOLEAN',
		'sqlalchemy'			: 'Boolean',
	},
	'date': {
		'django'				: 'models.DateField',
		'flask'					: 'sqlalchemy.DateTime',
		'graphene'				: 'graphene.types.datetime.DateTime',
		'mongoose'				: 'Date',
		'pydantic'				: 'datetime.date',
		'sequelize'				: 'DATE',
		'sqlalchemy'			: 'DateTime',
	},
	'decimal': {
		'django'				: 'models.DecimalField',
		'sequelize'				: 'DECIMAL',
	},
	'double': {
		'django'				: 'DOUBLE',
		'sequelize'				: 'DOUBLE',
	},
	'email': {
		'django'				: 'models.EmailField',
	},
	'enum': {
		'django'				: 'ENUM',
		'sequelize'				: 'ENUM',
	},
	'float': {
		'django'				: 'FLOAT',
		'flask'					: 'sqlalchemy.Float',
		'graphene'				: 'graphene.Float',
		'nest'					: 'number',
		'pydantic'				: 'float',
		'sboot'					: 'Float',
		'sequelize'				: 'FLOAT',
		'sqlalchemy'			: 'Float',
	},
	'id':	{
		'graphene'				: 'graphene.ID',
	},
	'image':	{
		'django'				: 'models.ImageField',
		'sequelize'				: 'STRING',
	},
	'integer': {
		'django'				: 'models.IntegerField',
		'flask'					: 'sqlalchemy.Integer',
		'graphene'				: 'graphene.Int',
		'pydantic'				: 'int',
		'sboot'					: 'Int',
		'sequelize'				: 'INTEGER',
		'sqlalchemy'			: 'Integer',
	},
	'number': {
		'django'				: 'NUMBER',
		'mongoose'				: 'Number',
		'sequelize'				: 'DECIMAL',
	},
	'serial': {
		'flask'					: 'sqlalchemy.Integer',
	},
	'slug': {
		'django'				: 'models.SlugField',
		'sequelize'				: 'STRING',
	},
	'string': {
		'django'				: 'models.CharField',
		'djongo'				: 'models.CharField',
		'flask'					: 'sqlalchemy.String',
		'graphene'				: 'graphene.String',
		'mongoose'				: 'String',
		'nest'					: 'string',
		'pydantic'				: 'str',
		'sboot'					: 'String',
		'sequelize'				: 'STRING',
		'sqlalchemy'			: 'String',
	},
	'text': {
		'django'				: 'models.TextField',
		'djongo'				: 'models.CharField',
		'flask'					: 'sqlalchemy.Text',
		'graphene'				: 'graphene.String',
		'pydantic'				: 'str',
		'sequelize'				: 'TEXT',
		'sqlalchemy'			: 'Text',
	},
	'timestamp': {
		# apa beda auto_now=True dan auto_now_add=True?
		'django'				: 'models.DateTimeField',
		'djongo'				: 'models.DateTimeField',
		'flask'					: 'sqlalchemy.TimeStamp',
		'graphene'				: 'graphene.types.datetime.DateTime',
		'pydantic'				: 'datetime.datetime',
		'sequelize'				: 'TEXT',
		'sequelize'				: '__DQTIMESTAMP__DQ',
		'sqlalchemy'			: 'TimeStamp',
	},
	'url': {
		'djongo'				: 'models.URLField',
	},
	'uuid': {
		'sequelize'				: 'UUID',
	},
	'uuid1': {
		'sequelize'				: 'UUIDV1',
	},
	'uuid4': {
		'sequelize'				: 'UUIDV4',
	},
	'varchar': {
		'django'				: 'models.CharField',
		'flask'					: 'sqlalchemy.String',
		'graphene'				: 'graphene.String',
		'pydantic'				: 'str',
		'sequelize'				: 'STRING',
		'sqlalchemy'			: 'String',
	},

	# django specific
	'django_foreign_key': {
		'django'				: 'models.ForeignKey',
		'djongo'				: 'models.ForeignKey',
		'flask'					: 'sqlalchemy.ForeignKey',
		'mongoose'				: 'Schema.ObjectId',
		'sequelize'				: '{ type: STRING, allowNull: false, references: __DQModelRujukan__DQ, }',
	},
	'django_one_to_one': {
		'django'				: 'models.OneToOneField',
		'sequelize'				: '[{ type: String }]',
	},
	'django_one_to_many': {
		'django'				: 'models.OneToManyField',
	},
	'django_many_to_many': {
		'django'				: 'models.ManyToManyField',
		'sequelize'				: '[{ type: String }]',
	},
}
