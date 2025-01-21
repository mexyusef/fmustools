--% index/fmus
propbackend,d(/mk)
	%__TEMPLATE_SERVER_PORT=__NILAI_SERVER_PORT__
	docker-compose.yml,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_backend/docker-compose.mk=docker-compose.yml)
	manage.py,f(e=__FILE__=manage.py)
	.env,f(e=__FILE__=.env)
	.,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_backend/sqlite.mk=index/fmus*)
	restore.sh,f(e=__FILE__=restore db)
	run.sh,f(n=clear && python manage.py runserver 0.0.0.0:__NILAI_SERVER_PORT__)
	tempdb.sql,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_backend/db.mk=index/fmus)
	$*chmod a+x *.sh
	static,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_backend/resources.mk=index/fmus*)
	main,d(/mk)
		config.py,f(e=__FILE__=/main/config.py)
		urls.py,f(e=__FILE__=/main/urls.py)
		views.py,f(e=__FILE__=/main/views.py)
		wsgi.py,f(e=__FILE__=/main/wsgi.py)
		helpers,d(/mk)
			__init__.py,f(e=__FILE__=/main/helpers/__init__.py)
			exceptions.py,f(e=__FILE__=/main/helpers/exceptions.py)
			models.py,f(e=__FILE__=/main/helpers/models.py)
			renderers.py,f(e=__FILE__=/main/helpers/renderers.py)
			utils.py,f(e=__FILE__=/main/helpers/utils.py)
	apps,d(/mk)
__TEMPLATE_APP_CONTENT
	apps,d(/mk)
		user,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_backend/user.mk=index/fmus*)
		profile,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_backend/profile.mk=index/fmus*)
	apps,d(/load=__CURDIR/extras.mk=index/fmus*)
--#

--% manage.py
import os
import sys
from dotenv import load_dotenv

def main():
  load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
  SETTINGS_FILE = os.environ.get('SETTINGS_FILE')
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_FILE)

  try:
    from django.core.management import execute_from_command_line
  except ImportError as exc:
    raise ImportError("gagal import django") from exc
  
  execute_from_command_line(sys.argv)

if __name__ == '__main__':
  main()
--#

--% .env
SETTINGS_FILE=main.config
SALT_ROUNDS=14

DB1_NAME=tempdb
DB1_USER=usef
DB1_PASS=rahasia
DB1_HOST=localhost
DB1_PORT=5432

CACHE_DB=13
CACHE_HOST=localhost
CACHE_PORT=7502
CACHE_KEY_PREFIX=iot_cache
--#

--% /main/config.py
import os
from datetime import timedelta
from pathlib import Path

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(CONFIG_DIR)
BASE_DIR = Path(__file__).resolve().parent.parent

# QCROT_DIR = os.path.join(BASE_DIR, 'qcrot')
AUTH_USER_MODEL = 'user.User'

ROOT_URLCONF = 'main.urls'
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
STATICFILES_DIRS = [
	# BASE_DIR / "static",
	os.path.join(BASE_DIR, 'static'),
	# '/var/www/static/',
	os.path.join(BASE_DIR, 'frontend/build/static')
]

SECRET_KEY = '-+6=0k1%n%xew+sx_(3&a*yzr#s%38!j)8)l2l^ful=9it5e)a'
DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {
	'default': {
		"ENGINE":   "django.db.backends.postgresql_psycopg2",
		"NAME":     os.environ.get('DB1_NAME'),
		"USER":     os.environ.get('DB1_USER'),
		"PASSWORD": os.environ.get('DB1_PASS'),
		"HOST":     os.environ.get('DB1_HOST'),
		"PORT":     os.environ.get('DB1_PORT'),
	},

	# 'default': {
	#   'ENGINE': 'django.db.backends.sqlite3',
	#   'NAME': BASE_DIR / 'db.sqlite3',
	# },

	# "default": {
	# 	"ENGINE": "django.db.backends.sqlite3",
	# 	"NAME": os.path.join(BASE_DIR, "tempdb.db"),
	# },
}

INSTALLED_APPS = [
	# 'channels',
	
__TEMPLATE_INSTALLED_APPS__

	'apps.user',

	'django_extensions', # python manage.py show_urls
	
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'graphene_django',
	'nested_admin',
	'rest_framework',
	'rest_framework.authtoken',
	'corsheaders',
]

MIDDLEWARE = [
	"corsheaders.middleware.CorsMiddleware",
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'frontend/build')
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

# ASGI_APPLICATION = 'main.asgi.application'
WSGI_APPLICATION = 'main.wsgi.application'

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}
SIMPLE_JWT = {
	'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
	'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
	'ROTATE_REFRESH_TOKENS': False,
	'BLACKLIST_AFTER_ROTATION': True,
	'UPDATE_LAST_LOGIN': False,

	'ALGORITHM': 'HS256',
	'VERIFYING_KEY': None,
	'AUDIENCE': None,
	'ISSUER': None,

	'AUTH_HEADER_TYPES': ('Bearer',),
	'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
	'USER_ID_FIELD': 'id',
	'USER_ID_CLAIM': 'user_id',

	'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
	'TOKEN_TYPE_CLAIM': 'token_type',

	'JTI_CLAIM': 'jti',

	'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
	'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
	'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# CHANNEL_LAYERS = {
#   'default': {
#     'BACKEND': 'channels_redis.core.RedisChannelLayer',
#     'CONFIG': {
#       "hosts": [('127.0.0.1', 6379)],
#     },
#   },
# }

# GRAPHENE = {
# 	"SCHEMA": "main.schema.schema",
# 	"MIDDLEWARE": ["graphql_jwt.middleware.JSONWebTokenMiddleware"],
# }
--#

--% restore db
docker exec -it django_pg_db_1 psql -h localhost -U usef -p 5432 tempdb < tempdb.sql

docker exec -it propbackend_phppgadmin_1 psql -h localhost -U usef -p 5432 tempdb < tempdb.sql

docker exec -it propbackend_phppgadmin_1 psql -h 172.30.175.35 -U usef -p 5432 tempdb < tempdb.sql

PROJECTNAME, ROOTFOLDER
PROJECTNAME_phppgadmin_1
paling gampang: dari phppgadmin, sql, browse file
--#

--% /main/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.views.generic import TemplateView
from .views import RootView

urlpatterns = [
  path('', RootView.as_view()),
  # path('', TemplateView.as_view(template_name='index.html')),
  re_path('admin/?', admin.site.urls),
  re_path(r'^nested_admin/?', include('nested_admin.urls')),

__TEMPLATE_APP_URLS__

  path('api/', include('apps.user.urls')),
]
--#

--% /main/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

class RootView(APIView):
  def get(self, _):
    return Response({
      'status': 'OK',
      'message': 'Alive',
      'time': datetime.datetime.now().isoformat(),
    })
--#

--% /main/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
SETTINGS_FILE = os.environ.get('SETTINGS_FILE')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_FILE)
application = get_wsgi_application()
--#

--% /main/helpers/__init__.py
from .models import TimestampedModel
from .renderers import CustomJSONRenderer
from .utils import generate_random_string
--#

--% /main/helpers/exceptions.py
from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
  response = exception_handler(exc, context)
  handlers = {
    'NotFound': _handle_not_found_error,
    'ValidationError': _handle_generic_error
  }

  exception_class = exc.__class__.__name__

  if exception_class in handlers:
    return handlers[exception_class](exc, context, response)

  return response

def _handle_generic_error(exc, context, response):
  response.data = {
    'errors': response.data
  }
  return response

def _handle_not_found_error(exc, context, response):
  view = context.get('view', None)
  if view and hasattr(view, 'queryset') and view.queryset is not None:
    error_key = view.queryset.model._meta.verbose_name
    response.data = {
      'errors': {
        error_key: response.data['detail']
      }
    }

  else:
    response = _handle_generic_error(exc, context, response)

  return response
--#

--% /main/helpers/models.py
from django.db import models

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
    ordering = ['-created_at', '-updated_at']
--#

--% /main/helpers/renderers.py
import json
from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
  charset = 'utf-8'
  object_label = 'object'
  pagination_object_label = 'objects'
  pagination_object_count = 'count'

  def render(self, data, media_type=None, renderer_context=None):
    if data.get('results', None) is not None:
      return json.dumps({
        self.pagination_object_label: data['results'],
        self.pagination_count_label: data['count']
      })

    elif data.get('errors', None) is not None:
      return super(CustomJSONRenderer, self).render(data)
    
    else:
      return json.dumps({
        self.object_label: data
      })
--#

--% /main/helpers/utils.py
import random
import string

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits

def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
  return ''.join(random.choice(chars) for _ in range(size))
--#
