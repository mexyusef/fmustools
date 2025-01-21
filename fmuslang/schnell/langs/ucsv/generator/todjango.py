import json
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

sequelize_type_mapper = {
	'string':       'models.CharField',
	'varchar':      'models.CharField',
	'text':         'models.TextField',
	'integer':      'models.IntegerField',
	'number':       'NUMBER',
	'bigint':       'BIGINT',
	'boolean':      'BOOLEAN',
	'date':         'models.DateField',
	'float':        'FLOAT',
	'double':       'DOUBLE',
	'timestamp':    'models.DateTimeField', # apa beda auto_now=True dan auto_now_add=True?
	'enum':         'ENUM',
	# django specific
	'email':        'models.EmailField',
	'slug':         'models.SlugField',
}

django_indent = 4*' '
django_template = f"""
from django.db import models

class __TABLENAME__(models.Model):
__FIELDS__
"""

model = {}

# dari nama table:
# from django.db import models
# class Ingredient(models.Model):

# apakah setiap model perlu ini? atau field yg diinginkan
#     def __str__(self):
#         return self.name

# lalu tiap model stlh python manage.py makemigrations+migrate
# from django.contrib import admin
# admin.site.register(masing2 model) pada project/app/admin.py atau modules/namamodule/admin.py

# name,v(100) harus hasilkan:
# name = models.CharField(max_length=100)

# bgm hasilkan:
# category = models.ForeignKey(
# 	Category, related_name="ingredients", on_delete=models.CASCADE
# )

def to_django(RootNode):
	"""
	root: AnyNode(label='root', model='mytable', output='alchemy', outputs=[], type='root'), initial result: []
	"""
	print('todjango, root node:', RootNode)
	for column in PreOrderIter(RootNode):
		
		print('todjango, preoderiter:', column)
		col_attrs = []

		if column.label != 'root':
			
			# print('preoderiter:', column.label)
			if hasattr(column, 'hasConstraint') and column.hasConstraint == True: # complex type {}

				# default_get_type = sequelize_type_mapper[column.type]
				model[column.label] = sequelize_type_mapper[column.type]
				if column.type == 'varchar' and hasattr(column, 'typenum'):
					'''
					password,v(100)
					AnyNode(hasConstraint=False, label='password', type='varchar', typenum='100')
					'''
					# default_get_type += f'({column.typenum})'
					col_attrs.append(f'max_length={column.typenum}')

				# model[column.label] = {
				# 	# 'type': sequelize_type_mapper[column.type]
				# 	'type': default_get_type
				# }
				if hasattr(column, 'unique'):
					# model[column.label] .update({ 'unique': column.unique })
					col_attrs.append('unique=True')

				if hasattr(column, 'allowNull'):
					# model[column.label] .update({ 'allowNull': column.allowNull })
					col_attrs.append('null=True')

				if hasattr(column, 'defaultValue'):
					# model[column.label] .update({ 'defaultValue': column.default })
					col_attrs.append(f'default={column.defaultValue}')

			else: # simple type
				model[column.label] = sequelize_type_mapper[column.type]
				if column.type == 'varchar' and hasattr(column, 'typenum'):
					# model[column.label] += f"(max_length={column.typenum})"
					col_attrs.append(f'max_length={column.typenum}')

			model[column.label] += "(" + ', '.join(col_attrs) + ")"

	formatted = []
	for k,v in model.items():
		field = f"{k.ljust(10)} = {v}"
		formatted.append(field)

	# django_template
	hasil = '\n'.join([django_indent+item for item in formatted])
	hasil = django_template \
		.replace('__TABLENAME__', RootNode.model) \
		.replace('__FIELDS__', hasil)
	
	# return '\n' + str(model) + '\n'
	return '\n' + hasil + '\n'
