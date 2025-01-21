field_map = {		
	'auto':					'Integer', # SERIAL
	'serial':				'Integer', # SERIAL
  'integer':      'Integer',
	'bigint':       'Integer',
  'float':        'Float',
	# 'double':       'DOUBLE',
	# 'enum':         'ENUM',	
	# 'number':       'NUMBER',
  # 'decimal':			'models.DecimalField',

	'boolean':      'Boolean',
	'date':         'DateTime',
  'timestamp':    'DateTime',

	# 'image':				'models.ImageField',
	
	'string':       'String',
  'varchar':      'String',
	'text':         'Text',
  # # apa beda auto_now=True dan auto_now_add=True?		

	# # django specific
	'django_foreign_key':			'ForeignKey',
	# 'django_one_to_one':			'models.OneToOneField',
	# 'django_one_to_many':			'models.OneToManyField',
	# 'django_many_to_many':		'models.ManyToManyField',	

	# 'email':        'models.EmailField',
	# 'slug':         'models.SlugField',
}
