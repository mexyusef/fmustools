sqlalchemy_column_mapper = {
    'auto':			'Integer',
    'integer':      'Integer',
    'bigint':       'Integer',
    'float':        'Float',
    # 'double':     'DOUBLE',
    # 'enum':       'ENUM',
    # 'number':     'NUMBER',
    # 'decimal':	'models.DecimalField',

    'boolean':      'Boolean()',
    'date':         'DateTime',
    'timestamp':    'TIMESTAMP',

    # 'image':		'models.ImageField',

    'string':       'String',
    'text':         'Text',
    'varchar':      'String',
    # # apa beda auto_now=True dan auto_now_add=True?

    # # django specific
    # 'django_foreign_key':			'models.ForeignKey',
    # 'django_one_to_one':			'models.OneToOneField',
    # 'django_one_to_many':			'models.OneToManyField',
    # 'django_many_to_many':		'models.ManyToManyField',

    # 'email':        'models.EmailField',
    # 'slug':         'models.SlugField',
}

pydantic_basemodel_mapper = {
    'auto':			'int',
    'integer':      'int',
    'bigint':       'int',
    'float':        'float',
    # 'double':     'DOUBLE',
    # 'enum':       'ENUM',
    # 'number':     'NUMBER',
    # 'decimal':	'models.DecimalField',

    'boolean':      'bool',
    'date':         'datetime.date',
    'timestamp':    'datetime.datetime',

    # 'image':		'models.ImageField',

    'string':       'str',
    'text':         'str',
    'varchar':      'str',
    # # apa beda auto_now=True dan auto_now_add=True?

    # # django specific
    # 'django_foreign_key':			'models.ForeignKey',
    # 'django_one_to_one':			'models.OneToOneField',
    # 'django_one_to_many':			'models.OneToManyField',
    # 'django_many_to_many':		'models.ManyToManyField',

    # 'email':      'models.EmailField',
    # 'slug':       'models.SlugField',
}

pydantic_basemodel_mapper_optional = {
    'auto':			'Optional[int]',
    'integer':      'Optional[int]',
    'bigint':       'Optional[int]',
    'float':        'Optional[float]',
    # 'double':     'DOUBLE',
    # 'enum':       'ENUM',
    # 'number':     'NUMBER',
    # 'decimal':	'models.DecimalField',

    'boolean':      'Optional[bool]',
    'date':         'Optional[datetime.date]',
    'timestamp':    'Optional[datetime.datetime]',

    # 'image':		'models.ImageField',

    'string':       'Optional[str]',
    'text':         'Optional[str]',
    'varchar':      'Optional[str]',
    # # apa beda auto_now=True dan auto_now_add=True?

    # # django specific
    # 'django_foreign_key':			'models.ForeignKey',
    # 'django_one_to_one':			'models.OneToOneField',
    # 'django_one_to_many':			'models.OneToManyField',
    # 'django_many_to_many':		'models.ManyToManyField',

    # 'email':        'models.EmailField',
    # 'slug':         'models.SlugField',
}

graphene_mapper = {
    'auto':			'graphene.ID()',
    'integer':      'graphene.Int()',
    'bigint':       'graphene.Int()',
    'float':        'graphene.Float()',
    # 'double':       'DOUBLE',
    # 'enum':         'ENUM',
    # 'number':       'NUMBER',
    # 'decimal':			'models.DecimalField',

    'boolean':      'graphene.Boolean()',
    'date':         'graphene.types.datetime.DateTime()',
    'timestamp':    'graphene.types.datetime.DateTime()',

    # 'image':		'models.ImageField',

    'string':       'graphene.String()',
    'text':         'graphene.String()',
    'varchar':      'graphene.String()',
    # # apa beda auto_now=True dan auto_now_add=True?

    # # django specific
    # 'django_foreign_key':			'models.ForeignKey',
    # 'django_one_to_one':			'models.OneToOneField',
    # 'django_one_to_many':			'models.OneToManyField',
    # 'django_many_to_many':		'models.ManyToManyField',

    # 'email':        'models.EmailField',
    # 'slug':         'models.SlugField',
}
