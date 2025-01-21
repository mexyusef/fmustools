from app.fileutils import (
	file_content,
	append_file,
)
# from ..config import output_django_mkfile
# from .config import output_django_mkfile
# from db.bantuan.common import tab
from app.usutils import tab

default_user_mk_entry = """
    user,d(/mk)
      signals.py,f(e=utama=/django-starter1/apps/user/signals.py)
      __init__.py,f(e=utama=/django-starter1/apps/user/__init__.py)
      renderers.py,f(e=utama=/django-starter1/apps/user/renderers.py)
      admin.py,f(e=utama=/django-starter1/apps/user/admin.py)
      views.py,f(e=utama=/django-starter1/apps/user/views.py)
      urls.py,f(e=utama=/django-starter1/apps/user/urls.py)
      backends.py,f(e=utama=/django-starter1/apps/user/backends.py)
      serializers.py,f(e=utama=/django-starter1/apps/user/serializers.py)
      models.py,f(e=utama=/django-starter1/apps/user/models.py)
"""

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
__TABwebsocket.py,f(e=utama=/apps/__TABLENAME__/websocket.py)
__TABurls.py,f(e=utama=/apps/app/urls.py/viewset)
__TABviews.py,f(e=utama=/apps/app/views.py/viewset)
__TABserializers.py,f(e=utama=/apps/app/serializers.py)
__TABfixtures,d(/mk)
__TAB__TAB__TABLENAME_LOW__.json,f(e=utama=/apps/__TABLENAME__/__TABLENAME_LOW__.json)
"""


django_model_template = """
__IMPORTS__

class __TABLENAME__(__TABLE_BASEMODEL__):
__FIELDS__

__TABclass Meta:
__TAB__TABapp_label = '__TEMPLATE_modelname'
__TAB__TABdb_table = '__TEMPLATE_modelnames'

__TABdef __str__(self):
__TAB__TABreturn "{}".format(self.__COLNAME__)
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


def app_content_template(appidx, tablename):
	# capitalize, OrderItem jadi Orderitem...
	content = APP_CONTENT_TEMPLATE \
		.replace('__APPIDX__', appidx) \
		.replace('__TABLENAME_CAP__', tablename.capitalize()) \
		.replace('__TABLENAME_LOW__', tablename.lower()) \
		.replace('__TABLENAME__', tablename) \
		.replace('__TAB', tab(1))

	return '\n'.join([tab(2)+item for item in content.splitlines()])


# def append_entry(tablename, body, entry_name='models', start='--%', end='--#'):
# 	"""
# 	/apps/{tablename}/models.py
# 	"""	
# 	header = f'/apps/{tablename}/{entry_name}.py'
# 	entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
# 	append_file(output_django_mkfile, entry_model)
# 	return entry_model


myjson_template = """[
		{% for record in records %}
__RECORD_TEMPLATE
		{% endfor %}
]
"""

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



def get_stringtemplate(tablename, records):
	appname = tablename.lower()
	modelname = tablename
	print(f'\n\n*** appname = {appname}, modelname = {modelname}\n\n')
	stringtemplate = myjson_template \
		.replace('__TABLENAMES', tablename.title()+'s') \
		.replace('__RECORD_TEMPLATE', entry_template(records, appname, modelname))
	
	return stringtemplate

# def append_fixture_entry(filepath_output, tablename, body):
# 	"""
# 	buat entry fixture di django.mk
# 	"""
# 	start='--%'
# 	end='--#'
# 	header = f'/apps/{tablename}/__TEMPLATE_modelname.json'
# 	entry_fixture = f'\n{start} {header}\n' + body + f'\n{end}\n'
# 	append_file(filepath_output, entry_fixture)
# 	return entry_fixture

