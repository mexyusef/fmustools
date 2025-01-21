import datetime, decimal, json
from schnell.app.dirutils import joiner
from schnell.app.fileutils import (
	file_content,
	append_file,
)
from schnell.app.utils import env_exist, env_get

TAB_SPACE_MULT = 2
TAB = ' ' * TAB_SPACE_MULT
JSON_INDENT = TAB_SPACE_MULT
TABS = TAB * 2
if not env_exist('ULIBPY_BASEDIR'):
	SCHNELL_BASEDIR = '/home/usef/work/ulibs/schnell'
else:
	SCHNELL_BASEDIR = env_get('ULIBPY_BASEDIR')

TEMPLATESDIR = joiner(SCHNELL_BASEDIR, 'db/bantuan/templates')
# output_folder = '/home/usef/common/working/redahsyat/output/'
# output_folder = '/home/usef/tmp/working/output/'
if not env_exist('ULIBPY_BANTUAN_OUTPUT'):
	output_folder = '/mnt/c/tmp/working/output/'
else:
	output_folder = env_get('ULIBPY_BANTUAN_OUTPUT')

JAVA_MODEL_TEMPLATE = """
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Table
@Entity
public class __TABLENAME {
__TABLE_FIELDS_JAVA
}
"""


SBGQL_TEMPLATE = """
schema {
	query: Query
}

type Query {
__TABLE_READ_OPERATIONS
}

type __TABLENAME {
__TABLE_FIELDS_GQL
}
"""


myjson_template = """[
		{% for record in records %}
__RECORD_TEMPLATE
		{% endfor %}
]
"""


# jk node.label (bukan node.type) bernilai spt ini
# sudah sama dg faker
langsung_panggil_method = [			
	'address',
	'city',
	'company',
	'country',
	'email',
	'first_name',
	'job',	
	'last_name',
	'name',	
	'phone_number',
	'postcode',
	'text',
	'uuid4',
]


ubah_method_dan_panggil = {
	# 'id'					: 'uuid4', # gak semua id itu uuid
	'isbn'				: 'isbn13',
	'phone'				: 'phone_number',
	'publisher'		: 'company',
	'postalcode'	: 'postcode',
	'zipcode'			: 'postcode',
	'zip'					: 'postcode',
	'firstname' 	: 'first_name',
	'lastname' 		: 'last_name',
	'created_at'	: 'iso8601',
	'createdAt'		: 'iso8601',
	'updated_at'	: 'iso8601',
	'updatedAt'		: 'iso8601',
}

# SKIPPING >>>2/ bentuk [nama=order,type=django_one_to_one] 
# AnyNode(allowNull=True, blank=True, foreignKeyOnDelete='models.CASCADE', hasConstraint=True, label='order', oneToOne=True, relTo='Order', type='django_one_to_one')
django_relationship_fields = [
	# 'django_foreign_key',
	'django_one_to_one', 
	'django_one_to_many', 
	'django_many_to_many'
]


nestjs_graphql_imports = """import {
	Field,
	ID,
	InputType,
	Int,
	ObjectType,
} from '@nestjs/graphql';
"""


sequelize_type_mapper = {
	
	'bigint':       'BIGINT',
	'double':       'DOUBLE',
	'enum':         'ENUM',
	'float':        'FLOAT',
	'number':       'NUMBER',

	'boolean':      'models.BooleanField',
	'date':         'models.DateField',
	'decimal':			'models.DecimalField',
	'image':				'models.ImageField',
	'integer':      'models.IntegerField',
	'auto':					'models.AutoField',
	'string':       'models.CharField',
	'text':         'models.TextField',
	'timestamp':    'models.DateTimeField', # apa beda auto_now=True dan auto_now_add=True?
	'varchar':      'models.CharField',	

	# django specific
	'django_foreign_key':			'models.ForeignKey',
	'django_one_to_one':			'models.OneToOneField',
	'django_one_to_many':			'models.OneToManyField',
	'django_many_to_many':		'models.ManyToManyField',	

	'email':        'models.EmailField',
	'slug':         'models.SlugField',
}


record_template = f"""{{
__ENTRY_TEMPLATE__}},"""


def entry_template(records, appname, modelname):
	first_row = records[0]
	daftar_keys = list(first_row.__dict__.keys())

	# https://stackoverflow.com/questions/9005823/jinja-template-renders-double-quotes-or-single-quotes-as-39-34/9006024
	# https://www.programcreek.com/python/example/107584/jinja2.runtime.Undefined
	# pairs = [f'"{col}": {{{{record.{col} | tojson | string | default("")}}}}' for col in daftar_keys]
	pairs = [f'"{col}": {{{{record.{col} | string | tojson }}}}' for col in daftar_keys]
	print('$pairs:', pairs, appname, modelname)
	
	per_entry_template = f""""model": "{appname}.{modelname}",
"pk": {{{{loop.index}}}},
"fields": {{
{',__NEWLINE'.join(pairs)}
}}\n""".replace('__NEWLINE', '\n')
	print('$pet:', per_entry_template)
	

	return record_template.replace('__ENTRY_TEMPLATE__', per_entry_template)


class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			# return (str(o) for o in [o])
			# return float(o)
			return str(o)
		elif isinstance(o, (datetime.date, datetime.datetime)):
			return o.isoformat()
		return super(DecimalEncoder, self).default(o)


class RecordEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return str(o)
		elif isinstance(o, Record):
			return {k:v for (k,v) in o.__dict__.items() if not k.startswith('__')}
		elif isinstance(o, (datetime.date, datetime.datetime)):
			return o.isoformat()
		return super(RecordEncoder, self).default(o)


class Record:
	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		# for k,v in self.__dict__.items():
		# 	if v is None:
		# 		self.__dict__[k] = ''

	def __str__(self):
		return json.dumps(self.__dict__, indent=TAB_SPACE_MULT, cls=DecimalEncoder)

	def __repr__(self):
		return json.dumps(self.__dict__, indent=TAB_SPACE_MULT, cls=DecimalEncoder)

	def keys_vals(self):
		return self.__dict__.keys(), self.__dict__.values()

	def values(self):
		return self.__dict__.values()

	def csv(self):
		"""
		pastikan semua values berbentuk str
		"""
		stringified = [str(item) for item in self.__dict__.values()]
		return ', '.join(stringified)


def records_csv(list_of_items):
	return '\n'.join([item.csv() for item in list_of_items])


def records_jsonify(list_of_items, header='data', count='length'):
	return json.dumps({
		header: list_of_items,
		count: len(list_of_items),
	}, indent=TAB_SPACE_MULT, cls=RecordEncoder)


def records_jsonify_simple(list_of_items):
	return json.dumps(list_of_items, indent=TAB_SPACE_MULT, cls=RecordEncoder)


def tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True):
	if use_space:
		return num*space
	else:
		return num*tab


def append_fixture_entry(filepath_output, tablename, body):
	"""
	buat entry fixture di django.mk
	"""
	start='--%'
	end='--#'
	header = f'/apps/{tablename}/__TEMPLATE_modelname.json'
	entry_fixture = f'\n{start} {header}\n' + body + f'\n{end}\n'
	append_file(filepath_output, entry_fixture)
	return entry_fixture


def append_entry(filepath_output, header, body):
	"""
	contoh:
	header = f'/apps/{tablename}/models.py'
	"""
	start='--%'
	end='--#'
	entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
	append_file(filepath_output, entry_model)
	return entry_model


def get_stringtemplate(tablename, records):
	appname = tablename.lower()
	modelname = tablename
	print(f'\n\n*** appname = {appname}, modelname = {modelname}\n\n')
	stringtemplate = myjson_template \
		.replace('__TABLENAMES', tablename.title()+'s') \
		.replace('__RECORD_TEMPLATE', entry_template(records, appname, modelname))
	
	return stringtemplate


APP_CONTENT_TEMPLATE = """__TEMPLATE_APP__APPIDX__,d(/mk)
__TAB%__TEMPLATE_MODELNAME_CAP=__TABLENAME_CAP__
__TAB%__TEMPLATE_MODELNAME=__TABLENAME__
__TAB%__TEMPLATE_modelname=__TABLENAME_LOW__
__TAB%__TEMPLATE_modelnames=__TABLENAME__s
__TAB__init__.py,f(e=utama=kosong)
__TABapps.py,f(e=utama=/apps/app/apps.py)
__TABadmin.py,f(e=utama=/apps/app/admin.py)
__TABmodels.py,f(e=utama=/apps/__TABLENAME__/models.py)
__TABschema.py,f(e=utama=/apps/__TABLENAME__/schema.py)
__TABurls.py,f(e=utama=/apps/app/urls.py/viewset)
__TABviews.py,f(e=utama=/apps/app/views.py/viewset)
__TABserializers.py,f(e=utama=/apps/app/serializers.py)
__TABfixtures,d(/mk)
__TAB__TAB__TEMPLATE_modelname.json,f(e=utama=/apps/__TABLENAME__/__TEMPLATE_modelname.json)
	"""


def app_content_template(appidx, tablename):
	# capitalize, OrderItem jadi Orderitem...
	content = APP_CONTENT_TEMPLATE \
		.replace('__APPIDX__', appidx) \
		.replace('__TABLENAME_CAP__', tablename.capitalize()) \
		.replace('__TABLENAME_LOW__', tablename.lower()) \
		.replace('__TABLENAME__', tablename) \
		.replace('__TAB', tab(1))

	return '\n'.join([tab(2)+item for item in content.splitlines()])
