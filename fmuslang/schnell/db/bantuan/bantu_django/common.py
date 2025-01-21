from app.fileutils import (
	file_content,
	append_file,
)
# from ..config import output_django_mkfile
from .config import output_django_mkfile
from db.bantuan.common import tab

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
__TAB__TAB__TEMPLATE_modelname.json,f(e=utama=/apps/__TABLENAME__/__TEMPLATE_modelname.json)
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



def app_content_template(appidx, tablename):
	# capitalize, OrderItem jadi Orderitem...
	content = APP_CONTENT_TEMPLATE \
		.replace('__APPIDX__', appidx) \
		.replace('__TABLENAME_CAP__', tablename.capitalize()) \
		.replace('__TABLENAME_LOW__', tablename.lower()) \
		.replace('__TABLENAME__', tablename) \
		.replace('__TAB', tab(1))

	return '\n'.join([tab(2)+item for item in content.splitlines()])


def append_entry(tablename, body, entry_name='models', start='--%', end='--#'):
	"""
	/apps/{tablename}/models.py
	"""	
	header = f'/apps/{tablename}/{entry_name}.py'
	entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
	append_file(output_django_mkfile, entry_model)
	return entry_model
