--% index/fmus
fsdjangomongo,d(/mk)
  %utama=__FILE__
__TEMPLATE_DB_INIT
  %__TEMPLATE_REDIS_PORT=7502
  %__TEMPLATE_REDIS_DBNO=13
  %__TEMPLATE_SERVER=0.0.0.0
  %__TEMPLATE_PORT=8500
  # @jika belum ada database bernama "__TEMPLATE_DBNAME", silahkan buat dulu di sini
  # $(cd /home/usef/danger/ulib/schnell/schnell/samples/ugo && ./jalan)

  .env,f(e=utama=/.env)
  docker-compose.yml,f(e=utama=/docker-compose.yml)
  manage.py,f(e=utama=/manage.py)
  run.sh,f(e=utama=/run.sh)	
  README.md,f(e=utama=/README.md)

__TEMPLATE_APP_INIT

  apps,d(/mk)
    mockdata,d(/mk)
      __init__.py,f(e=utama=kosong)
      urls.py,f(e=utama=/apps/mockdata/urls.py)
      views.py,f(e=utama=/apps/mockdata/views.py)
    profile,d(/mk)
      __init__.py,f(e=utama=/django-starter1/apps/profile/__init__.py)
      renderers.py,f(e=utama=/django-starter1/apps/profile/renderers.py)
      views.py,f(e=utama=/django-starter1/apps/profile/views.py)
      urls.py,f(e=utama=/django-starter1/apps/profile/urls.py)
      exceptions.py,f(e=utama=/django-starter1/apps/profile/exceptions.py)
      serializers.py,f(e=utama=/django-starter1/apps/profile/serializers.py)
      models.py,f(e=utama=/django-starter1/apps/profile/models.py)
__TEMPLATE_CONDITIONAL_USER



__TEMPLATE_APP_CONTENT

  main,d(/mk)
    __init__.py,f(e=utama=kosong)
    asgi.py,f(e=utama=/main/asgi.py)
    wsgi.py,f(e=utama=/main/wsgi.py)
    config.py,f(e=utama=/main/config.py/header)
__TEMPLATE_CONDITIONAL_DATABASE
    config.py,f(@a,e=utama=/main/config.py/apps)
    config.py,f(@a,e=utama=/main/config.py/middleware)
    config.py,f(@a,e=utama=/main/config.py/templates)
    config.py,f(@a,e=utama=/main/config.py/asgi_wsgi)
    config.py,f(@a,e=utama=/main/config.py/graphene)
    #routes.py,f(e=utama=/main/wsroutes.py)
    schema.py,f(e=utama=/main/schema.py)
    urls.py,f(e=utama=/main/urls.py)
    views.py,f(e=utama=/main/views.py)
    helpers,d(/mk)
      __init__.py,f(e=utama=/django-starter1/main/helpers/__init__.py)
      renderers.py,f(e=utama=/django-starter1/main/helpers/renderers.py)
      exceptions.py,f(e=utama=/django-starter1/main/helpers/exceptions.py)
      models.py,f(e=utama=/django-starter1/main/helpers/models.py)
      utils.py,f(e=utama=/django-starter1/main/helpers/utils.py)

  # $*code .
  $*chmod a+x run.sh
  # $*x-terminal-emulator 2>/dev/null &
  # $*qterminal 2>/dev/null &

  # migration user hrs duluan krn dibutuhkan oleh apps  
  # $ python manage.py makemigrations user profile
__TEMPLATE_APP_MIGRATE_COMMAND  
  # run migration utk user dan apps
  # $ python manage.py migrate
  # $ python manage.py createsuperuser
  # $ python manage.py loaddata masing-masing apps
--#

--% kosong
--#

--% /.env
SETTINGS_FILE=main.config
SALT_ROUNDS=14

DB1_NAME=__TEMPLATE_DBNAME
DB1_USER=__TEMPLATE_DBUSER
DB1_PASS=__TEMPLATE_DBPASS
DB1_HOST=__TEMPLATE_DBHOST
DB1_PORT=__TEMPLATE_DBPORT

CACHE_DB=__TEMPLATE_REDIS_DBNO
CACHE_HOST=__TEMPLATE_DBHOST
CACHE_PORT=__TEMPLATE_REDIS_PORT
CACHE_KEY_PREFIX=iot_cache
--#

--% /docker-compose.yml
version: '3'
services:
  # db:
  #   image: postgres
  #   environment:
  #     - POSTGRES_DB=__TEMPLATE_DBNAME
  #     - POSTGRES_USER=__TEMPLATE_DBUSER
  #     - POSTGRES_PASSWORD=__TEMPLATE_DBPASS
  #   ports:
  #     - "__TEMPLATE_DBPORT:5432"

  database:
    image: 'mongo'
    # container_name: 'mymongocontainer'
    environment:
      - MONGO_INITDB_DATABASE=__TEMPLATE_DBNAME
      # - MONGO_INITDB_ROOT_USERNAME=__TEMPLATE_DBUSER
      # - MONGO_INITDB_ROOT_PASSWORD=__TEMPLATE_DBPASS
    ports:
      - '__TEMPLATE_DBPORT-27019:27017-27019'
--#

--% /README.md
TODO:
utk masing-masing app:
relations.py
renderers.py
serializers.py
signals.py

===
# migration user hrs duluan krn dibutuhkan oleh apps  
$ python manage.py makemigrations user profile
__TEMPLATE_APP_MIGRATE_COMMAND  
# run migration utk user dan apps
$ python manage.py migrate
$ python manage.py createsuperuser
# $ python manage.py loaddata masing-masing apps

===
python manage.py loaddata article/user

{
  articleList {
    id
    title
  }
}

mutation {
  articleCreate(title: "judul-judulan", content: "tebak-tebakan...oy") {
    article {
      id
      title
    }
  }
}

mutation {
  articleUpdate(
    id:"9668"
    title: "judul yg berbeda"
  ) {
    article {
      id
      title
    }
  }
}

$ curl -X POST -H "Accept: application/json" -d "{\"rows\": 50, \"fields\": ['name', 'country']}" localhost:9100/api/mock/

  {"status":"ok","type":"POST","rows":50,"fields":["name","country"],"result":["Gwendolyn Morrison","Ecuador"]}

$ curl -X POST -H "Accept: application/json" -d "{\"rows\": 50, \"fields\": ['name', 'iso8601', 'country', 'sentence']}" localhost:9100/api/mock/

  {"status":"ok","type":"POST","rows":50,"fields":["name","iso8601","country","sentence"],"result":["William Weber","1979-03-02T17:59:09","Mauritania","Happy position director ball."]}

$ curl -X POST -H "Accept: application/json" -d "{\"rows\": 50, \"fields\": ['name', 'iso8601', 'country', 'city', 'sentence', 'email']}" localhost:9100/api/mock/

  {"status":"ok","type":"POST","rows":50,"fields":["name","iso8601","country","city","sentence","email"],"result":["David Coleman","2007-02-25T22:42:38","Saint Lucia","New Josephberg","Prepare game soon buy never.","erik08@hotmail.com"]}

$ curl -X POST -H "Accept: application/json" -d "{\"rows\": 50, \"fields\": ['country','city','username']}" localhost:9100/api/mock/

$ curl -X POST -H "Accept: application/json" -d '{"rows": 50, "fields": ["country","city","username"]}' localhost:9100/api/mock/

pengennya ada request.data berisi
{
  rows: 50,
  fields: [field1, field2, field3, field4],
}
>>> a  = {'{"rows": 50, "fields": [1,2,3]}': ['']}
>>> a.keys()
dict_keys(['{"rows": 50, "fields": [1,2,3]}'])
>>> list (a.keys())
['{"rows": 50, "fields": [1,2,3]}']
>>> b = list (a.keys()) [0]
>>> type(b)
<class 'str'>
>>> c = eval(b)
>>> type(c)
<class 'dict'>
>>> c
{'rows': 50, 'fields': [1, 2, 3]}

# menerima request POST #1: <QueryDict: {'{"rows": 50, "fields": [1,2,3]}': ['']}>
# menerima request POST #2: <QueryDict: {'{"rows": 50, "fields": [1,2,3]}': ['']}>
# menerima request POST: <QueryDict: {'{"rows": 50, "fields": [1,2,3]}': ['']}>
# https://stackoverflow.com/questions/53206284/django-views-when-is-request-data-a-dict-vs-a-querydict
# https://stackoverflow.com/questions/13349573/how-to-change-a-django-querydict-to-python-dict
# querydict_data = request.data
# # data = dict(querydict_data)

# operasi berikut ini jadi kunci agar bisa data['rows'] dst

# if isinstance(request.data, dict):			
# 	# ini dari axios
# 	data = request.data
# 	print('terima data sbg dict, request.data:', request.data, 'menjadi:', data)
# 	print('type dict:', type(request.data), 'jenis utk data:', type(data))
# else:
# 	# ini dari curl
# 	data = request.POST.dict()
# 	print('data sblm ambil keylist:', data)
# 	data = list(data.keys()) [0]
# 	print('data stlh ambil keylist dg index 0:', data)
# 	data = eval(data)
# 	print('menjadi data:', data)

# menjadi data: {'{"rows": 50, "fields": [1,2,3]}': ['']}
# menjadi data: {'{"rows": 50, "fields": [1,2,3]}': ''}
# from django.utils import six 
# post_dict = dict(six.iterlists(request.POST))
# print('menerima request POST #3:', post_dict)
# menerima request POST #3: {'{"rows": 50, "fields": [1,2,3]}': ['']}
--#

--% /run.sh
clear && python manage.py runserver __TEMPLATE_SERVER:__TEMPLATE_PORT
--#

--% /manage.py
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

--% /main/asgi.py
import os
# from django.core.asgi import get_asgi_application
# from dotenv import load_dotenv

# load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
# SETTINGS_FILE = os.environ.get('SETTINGS_FILE')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_FILE)
# application = get_asgi_application()

# from channels.routing import get_default_application
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.config")
# django.setup()
# application = get_default_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import apps

application = ProtocolTypeRouter({
  'websocket': AuthMiddlewareStack(
    URLRouter(
__TEMPLATE_WSROUTES
    )
  ),
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

--% /main/wsroutes.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing
# import sensor.routing
application = ProtocolTypeRouter({
  'websocket': AuthMiddlewareStack(
    URLRouter(
      chat.routes.websocket_urlpatterns
      +
      sensor.routes.websocket_urlpatterns,
    )
  ),
})
--#

--% /main/schema.py
import graphene
__TEMPLATE_SCHEMA_APP_IMPORTS__

class Query(__TEMPLATE_SCHEMA_APP_QUERIES__, graphene.ObjectType):
  pass

class Mutation(__TEMPLATE_SCHEMA_APP_MUTATIONS__, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
--#

--% /main/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from .schema import schema
from .views import RootView

urlpatterns = [
  path('', RootView.as_view()),
  path('admin/', admin.site.urls),
  path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

__TEMPLATE_APP_ROUTE

  path('api/', include('apps.user.urls')),
  path('api/', include('apps.profile.urls')),
  path('api/', include('apps.mockdata.urls')),
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

--% /main/config.py/header
import os

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CONFIG_DIR)

# QCROT_DIR = os.path.join(BASE_DIR, 'qcrot')
AUTH_USER_MODEL = 'user.User'

ROOT_URLCONF = 'main.urls'
STATIC_URL = '/static/'
SECRET_KEY = '-+6=0k1%n%xew+sx_(3&a*yzr#s%38!j)8)l2l^ful=9it5e)a'
DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
--#

--% /main/config.py/databases/postgres

DATABASES = {
  # 'default': {
  #   "ENGINE":   "django.db.backends.postgresql_psycopg2",
  #   "NAME":     os.environ.get('DB1_NAME'),
  #   "USER":     os.environ.get('DB1_USER'),
  #   "PASSWORD": os.environ.get('DB1_PASS'),
  #   "HOST":     os.environ.get('DB1_HOST'),
  #   "PORT":     os.environ.get('DB1_PORT'),
  # }

  "default": {
    "ENGINE": "djongo",
    "NAME": os.environ.get('DB1_NAME'),
    'CLIENT': {
      'host':  os.environ.get('DB1_HOST'),
      'port': os.environ.get('DB1_PORT'),
      # 'username': os.environ.get('DB1_USER'),
      # 'password': os.environ.get('DB1_PASS'),
      # 'authSource': 'admin',
      # 'authMechanism': 'SCRAM-SHA-1'
    },
    'LOGGING': {
      'version': 1,
      'loggers': {
        'djongo': {
          'level': 'DEBUG',
          'propagate': False,
        }
      },
    },
  }
  # "default": {
  # 	"ENGINE": "django.db.backends.sqlite3",
  # 	"NAME": os.path.join(BASE_DIR, "__TEMPLATE_DBNAME.db"),
  # }
}
--#

--% /main/config.py/databases/sqlite3

DATABASES = {
  # 'default': {
  #   "ENGINE":   "django.db.backends.postgresql_psycopg2",
  #   "NAME":     os.environ.get('DB1_NAME'),
  #   "USER":     os.environ.get('DB1_USER'),
  #   "PASSWORD": os.environ.get('DB1_PASS'),
  #   "HOST":     os.environ.get('DB1_HOST'),
  #   "PORT":     os.environ.get('DB1_PORT'),
  # }
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "__TEMPLATE_DBNAME.db"),
  }
}
--#

--% /main/config.py/apps

INSTALLED_APPS = [
  'channels',
  
__TEMPLATE_APP_INSTALLED_APPS

  'apps.profile',
  'apps.user',
  
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  'graphene_django',

  'rest_framework',
  'rest_framework.authtoken',
  'corsheaders',
]
--#

--% /main/config.py/middleware

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
--#

--% /main/config.py/templates

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
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
--#

--% /main/config.py/asgi_wsgi

# ASGI_APPLICATION = 'main.wsroutes.application'
ASGI_APPLICATION = 'main.asgi.application'
WSGI_APPLICATION = 'main.wsgi.application'

# CHANNEL_LAYERS = {
#   'default': {
#     'BACKEND': 'channels_redis.core.RedisChannelLayer',
#     'CONFIG': {
#       "hosts": [('127.0.0.1', 6379)],
#     },
#   },
# }
--#

--% /main/config.py/graphene

GRAPHENE = {
  "SCHEMA": "main.schema.schema",
  "MIDDLEWARE": ["graphql_jwt.middleware.JSONWebTokenMiddleware"],
}
--#

--% /apps/user/admin.py
from django.contrib import admin

from .models import User
admin.site.register(User)
--#

--% /apps/user/apps.py
from django.apps import AppConfig

class UserConfig(AppConfig):
  name = 'user'
--#

--% /apps/user/models.py
# from django.db import models
from djongo import models
from django.utils.translation import ugettext_lazy as _
# import bcrypt, datetime
import uuid

class User(models.Model):
  id          = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
  username    = models.CharField(max_length=64, blank=True, null=True, verbose_name=_('nama pengguna'))
  email       = models.EmailField(max_length=200, unique=True, verbose_name=_('alamat email'))
  password    = models.CharField(max_length=256, blank=False, null=False, verbose_name=_('kata kunci'))
  created_at  = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('waktu buat'))
  updated_at  = models.DateTimeField(auto_now=True, blank=True, verbose_name=_('waktu update'))

  role        = models.CharField(max_length=100, choices=[
    ('pengguna',    'Pengguna'),
    ('admin',       'Admin'),
    ('tamu',        'Tamu'),
  ], default='pengguna')

  class Meta:
    app_label = 'user'
    db_table = 'users'
    ordering = ['-email']
    # default_permissions = ()
    # permissions = (
    #   ('lihat_user', 'Melihat User'),
    #   ('tambah_user', 'Menambah User'),
    #   ('ubah_user', 'Mengubah User'),
    #   ('hapus_user', 'Menghapus User'),
    #   ('ubah_profil', 'Mengubah Profil'),
    #   ('ubah_password', 'Mengubah Password'),
    # )
  
  @property
  def is_staff(self):
    return True

  def __str__(self):
    return f"{self.username}, {self.email}"
--#

--% /apps/user/urls.py
from django.urls import re_path
from .views import UserView

urlpatterns = [
  re_path(r'^$', 
    UserView.as_view({ 
      'post'			: 'create', 
      'get'				: 'daftar' 
    }),
    name='user-index'),

  # url(r'^active/$', UserView.as_view({ 'get': 'active' }), name='user-active'),

  # url(r'^byEmail/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', UserView.as_view({ 'get': 'by_email', 'put': 'by_email_update', 'patch': 'by_email_partial_update'}), name='user-by-email'),

  re_path(r'^(?P<pk>[0-9]+)/$', 
    UserView.as_view({ 
      'get'				: 'retrieve', 
      'put'				: 'full_update', 
      'patch'			: 'partial_update', 
      'delete'		: 'destroy' 
    }),
    name='user-detail'),
]
--#

--% /apps/user/views.py
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render

from rest_framework import (status, mixins, viewsets)
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import NotFound
from rest_framework import serializers

from .models import User

class UserView(mixins.CreateModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  viewsets.GenericViewSet):

  queryset = User.objects.none()
  renderer_classes = (JSONRenderer, )

  def daftar(self, request, format=None):
    self.queryset = User.objects.all()
    # self.serializer_class = UserListSerializer
    return super(UserView, self).list(request, format)

  def retrieve(self, request, pk=None, format=None):
    self.queryset = User.objects.filter(id=pk)
    return super(UserView, self).retrieve(request, pk, format)

  def full_update(self, request, pk=None, *args, **kwargs):
    self.queryset = User.objects.filter(id=pk)
    return super(UserView, self).update(request, *args, **kwargs)

  def partial_update(self, request, pk=None, *args, **kwargs):
    self.queryset = User.objects.filter(id=pk)
    return super(UserView, self).partial_update(request, *args, **kwargs)

  def destroy(self, request, pk=None, format=None):
    self.queryset = User.all()
    # self.serializer_class = UserSerializer
    return super(UserView, self).destroy(request, pk, format)
--#

--% /apps/app/models.py
# from django.db import models
from djongo import models

class __TEMPLATE_MODELNAME(models.Model):
  id            = models.AutoField(primary_key=True)
  name          = models.CharField(max_length=255)
  title         = models.CharField(max_length=255)
  description   = models.CharField(max_length=500, blank=True, null=True)
  notes         = models.CharField(max_length=1000, blank=True, null=True)

  class Meta:
    app_label = '__TEMPLATE_modelname'
    db_table = '__TEMPLATE_modelnames'

  def __str__(self):
    return "{}".format(self.name)
--#

--% /apps/app/serializers.py
from rest_framework import serializers
from .models import __TEMPLATE_MODELNAME

class __TEMPLATE_MODELNAMESerializer(serializers.ModelSerializer):
  class Meta:
    model = __TEMPLATE_MODELNAME
    fields = '__all__'
--#

--% /apps/app/admin.py
from django.contrib import admin
from .models import __TEMPLATE_MODELNAME

admin.site.register(__TEMPLATE_MODELNAME)
--#

--% /apps/app/apps.py
from django.apps import AppConfig

class __TEMPLATE_MODELNAMEConfig(AppConfig):
  name = 'apps.__TEMPLATE_modelname'
--#

--% /apps/app/urls.py/view_by_function
from django.urls import path, re_path
from . import views

urlpatterns = [
  re_path('^create/?$', views.create),
  re_path('^list/?$', views.read_list),
  re_path('^detail/<int:pk>/?$', views.read_detail),
  re_path('^update/<int:pk>/?$', views.update),
  re_path('^delete/<int:pk>/?$', views.delete),
]
--#

--% /apps/app/urls.py/apiview
from django.urls import path, re_path
from . import views

urlpatterns = [  
  path('__TEMPLATE_modelname', __TEMPLATE_MODELNAMEAPIView.as_view())
]
--#

--% /apps/app/urls.py/viewset
from django.urls import path, re_path
#from . import views
from .views import __TEMPLATE_MODELNAMEViewSet
from .websocket import __TEMPLATE_MODELNAMEConsumer

# __PEMISAH_IMPORTS

urlpatterns = [

  re_path(r'__TEMPLATE_modelnames/?', __TEMPLATE_MODELNAMEViewSet.as_view({
    'get': 'list',
    'post': 'create',
  })),

  re_path(r'__TEMPLATE_modelnames/<str:pk>/?', __TEMPLATE_MODELNAMEViewSet.as_view({
    'get': 'detail',
    'put': 'update',
    'delete': 'destroy',
  })),

  # path('__TEMPLATE_modelname', __TEMPLATE_MODELNAMEAPIView.as_view()),

# __TAMBAHAN_URLS

]
websocket_urlpatterns = [
  re_path(r'__TEMPLATE_modelname/(?P<room_name>[\w\-\d]+)/$', __TEMPLATE_MODELNAMEConsumer),
]
--#

--% /apps/app/views.py/apiview
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .models import __TEMPLATE_MODELNAME

class __TEMPLATE_MODELNAMEAPIView(APIView):
  def get(self, _):
    __TEMPLATE_modelnames = __TEMPLATE_MODELNAME.objects.all()
    __TEMPLATE_modelname = random.choice(__TEMPLATE_modelnames)
    return Response({
      'id': __TEMPLATE_modelname.id,
    })
--#

--% /apps/app/views.py/viewset
# detail = get = retrieve
# delete = destroy
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import __TEMPLATE_MODELNAME
from .serializers import __TEMPLATE_MODELNAMESerializer

class __TEMPLATE_MODELNAMEViewSet(viewsets.ViewSet):

  def create(self, request):
    serializer = __TEMPLATE_MODELNAMESerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def list(self, request):
    __TEMPLATE_modelnames = __TEMPLATE_MODELNAME.objects.all()
    serializer = __TEMPLATE_MODELNAMESerializer(__TEMPLATE_modelnames, many=True)
    return Response(serializer.data)

  def detail(self, request, pk=None):
    __TEMPLATE_modelname = __TEMPLATE_MODELNAME.objects.get(id=pk)
    serializer = __TEMPLATE_MODELNAMESerializer(__TEMPLATE_modelname)
    return Response(serializer.data)

  def update(self, request, pk=None):
    __TEMPLATE_modelname = __TEMPLATE_MODELNAME.objects.get(id=pk)
    serializer = __TEMPLATE_MODELNAMESerializer(instance=__TEMPLATE_modelname, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  def destroy(self, request, pk=None):
    __TEMPLATE_modelname = __TEMPLATE_MODELNAME.objects.get(id=pk)
    __TEMPLATE_modelname.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
--#

--% /apps/mockdata/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('mock/', views.mockdata),
]
urlpatterns = format_suffix_patterns(urlpatterns)
--#

--% /apps/mockdata/views.py
import django
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from faker import Faker
fake = Faker()

keywords = [
  'country', 'city',
  'word', 'sentence', 'paragraph', 'text',
  'user_name', 'password',
  'name', 'first_name', 'last_name', 'name_male', 'name_female',
  'date', 'time', 'year', 'month', 'month_name', 'day_of_week', 'day_of_month', 'timezone',
  'iso8601',
  'random_digit', 'random_int',
  'image_url',
  'email', 'company_email', 'free_email', 'safe_email', 'job', 'address', 'phone_number',
]

@api_view(['GET', 'POST'])
def mockdata(request):

  if request.method == 'GET':
    get_data = {
      'status'  : 'ok',
      'type'    : 'GET',
    }
    return Response(get_data)

  elif request.method == 'POST':

    print('menerima request POST #1:', request.data)
    print('menerima request POST #2:', request.POST)


    if isinstance(request.data, django.http.request.QueryDict):
      data = request.data.dict()
      data = list(data.keys()) [0]
      data = eval(data)
    else:
      data = request.data

    total = []
    jumlah = 1
    try:
      jumlah = int(data['rows'])
    except Exception as err:
      print('Gagal ambil data rows dari request.POST:', err)

    for baris in range(jumlah):
      hasil = []
      image_url = ['img100', 'img200', 'img300', 'img400', 'img500', 'img600']
      for field in data['fields']:
        if field in keywords + image_url:
          if field in image_url:
            size = int ( field.replace('img', '') )
            item = fake.image_url(size, size)
          else:
            item = getattr(fake, field) ()
          hasil .append(item)
      total .append(hasil)

    post_data = {
      'status'  : 'ok',
      'type'    : 'POST',
      'rows'    : data['rows'],
      'fields'  : data['fields'],
      'result'	: total,
    }
    return Response(post_data)
--#

--% /django-starter1/main/helpers/__init__.py
from .models import TimestampedModel
from .renderers import CustomJSONRenderer
from .utils import generate_random_string

--#

--% /django-starter1/main/helpers/renderers.py
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

--% /django-starter1/main/helpers/exceptions.py
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

--% /django-starter1/main/helpers/models.py
# from django.db import models
from djongo import models

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
    ordering = ['-created_at', '-updated_at']

--#

--% /django-starter1/main/helpers/utils.py
import random
import string

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits

def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
  return ''.join(random.choice(chars) for _ in range(size))

--#


--% /django-starter1/apps/user/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profile.models import Profile
from .models import User


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
  if instance and created:
    instance.profile = Profile.objects.create(user=instance)


--#

--% /django-starter1/apps/user/__init__.py

from django.apps import AppConfig

class UserAppConfig(AppConfig):
  name = 'apps.user'
  label = 'user'
  verbose_name = 'User'

  def ready(self):
    import apps.user.signals

default_app_config = 'apps.user.UserAppConfig'

--#

--% /django-starter1/apps/user/renderers.py
from main.helpers import CustomJSONRenderer

class UserJSONRenderer(CustomJSONRenderer):

  charset = 'utf-8'
  object_label = 'user'
  pagination_object_label = 'users'
  pagination_count_label = 'usersCount'

  def render(self, data, media_type=None, renderer_context=None):
    token = data.get('token', None)
    if token is not None and isinstance(token, bytes):
      data['token'] = token.decode('utf-8')

    return super(UserJSONRenderer, self).render(data)

--#

--% /django-starter1/apps/user/admin.py
from django.contrib import admin
from apps.profile.models import Profile
from .models import User

admin.site.register(User)
admin.site.register(Profile)

--#

--% /django-starter1/apps/user/views.py
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .renderers import UserJSONRenderer
from .serializers import (
  LoginSerializer, RegistrationSerializer, UserSerializer
)

class LoginAPIView(APIView):
  permission_classes = (AllowAny,)
  renderer_classes = (UserJSONRenderer,)
  serializer_class = LoginSerializer

  def post(self, request):
    user = request.data.get('user', {})
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationAPIView(APIView):
  permission_classes = (AllowAny,)
  renderer_classes = (UserJSONRenderer,)
  serializer_class = RegistrationSerializer

  def post(self, request):
    user = request.data.get('user', {})
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
  permission_classes = (IsAuthenticated,)
  renderer_classes = (UserJSONRenderer,)
  serializer_class = UserSerializer

  def retrieve(self, request, *args, **kwargs):
    serializer = self.serializer_class(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def update(self, request, *args, **kwargs):
    user_data = request.data.get('user', {})
    serializer_data = {
      'username': user_data.get('username', request.user.username),
      'email': user_data.get('email', request.user.email),
      'profile': {
        'bio': user_data.get('bio', request.user.profile.bio),
        'image': user_data.get('image', request.user.profile.image)
      }
    }

    serializer = self.serializer_class(
      request.user, data=serializer_data, partial=True
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

--#

--% /django-starter1/apps/user/urls.py
# from django.conf.urls import url
from django.urls import path, re_path
from .views import (
  LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)

urlpatterns = [
  re_path(r'^users/login/?$', LoginAPIView.as_view()),
  re_path(r'^users/?$', RegistrationAPIView.as_view()),
  re_path(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
]

--#

--% /django-starter1/apps/user/backends.py
import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User

class JWTAuthentication(authentication.BaseAuthentication):
  authentication_header_prefix = 'Token'
  def authenticate(self, request):
    request.user = None
    auth_header = authentication.get_authorization_header(request).split()
    auth_header_prefix = self.authentication_header_prefix.lower()

    if not auth_header:
      return None

    if len(auth_header) == 1:
      return None

    elif len(auth_header) > 2:
      return None

    prefix = auth_header[0].decode('utf-8')
    token = auth_header[1].decode('utf-8')

    if prefix.lower() != auth_header_prefix:
      return None

    return self._authenticate_credentials(request, token)

  def _authenticate_credentials(self, request, token):
    try:
      payload = jwt.decode(token, settings.SECRET_KEY)
    except:
      msg = 'Invalid authentication. Could not decode token.'
      raise exceptions.AuthenticationFailed(msg)

    try:
      user = User.objects.get(pk=payload['id'])
    except User.DoesNotExist:
      msg = 'No user matching this token was found.'
      raise exceptions.AuthenticationFailed(msg)

    if not user.is_active:
      msg = 'This user has been deactivated.'
      raise exceptions.AuthenticationFailed(msg)

    return (user, token)

--#

--% /django-starter1/apps/user/serializers.py
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from apps.profile.serializers import ProfileSerializer

class RegistrationSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
  )
  token = serializers.CharField(max_length=255, read_only=True)

  class Meta:
    model = User
    fields = ['email', 'username', 'password', 'token']

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)
  username = serializers.CharField(max_length=255, read_only=True)
  password = serializers.CharField(max_length=128, write_only=True)
  token = serializers.CharField(max_length=255, read_only=True)

  def validate(self, data):
    email = data.get('email', None)
    password = data.get('password', None)

    if email is None:
      raise serializers.ValidationError(
        'An email address is required to log in.'
      )

    if password is None:
      raise serializers.ValidationError(
        'A password is required to log in.'
      )

    user = authenticate(username=email, password=password)

    if user is None:
      raise serializers.ValidationError(
        'A user with this email and password was not found.'
      )

    if not user.is_active:
      raise serializers.ValidationError(
        'This user has been deactivated.'
      )

    return {
      'email': user.email,
      'username': user.username,
      'token': user.token
    }

class UserSerializer(serializers.ModelSerializer):
  """Handles serialization and deserialization of User objects."""
  password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
  )
  profile = ProfileSerializer(write_only=True)
  bio = serializers.CharField(source='profile.bio', read_only=True)
  image = serializers.CharField(source='profile.image', read_only=True)

  class Meta:
    model = User
    fields = (
      'email', 'username', 'password', 'token', 'profile', 'bio', 'image',
    )
    read_only_fields = ('token',)

  def update(self, instance, validated_data):
    password = validated_data.pop('password', None)
    profile_data = validated_data.pop('profile', {})
    for (key, value) in validated_data.items():
      setattr(instance, key, value)

    if password is not None:
      instance.set_password(password)

    instance.save()

    for (key, value) in profile_data.items():
      setattr(instance.profile, key, value)

    instance.profile.save()
    return instance

--#

--% /django-starter1/apps/user/models.py
import jwt
from datetime import datetime, timedelta
from django.conf import settings

# from django.db import models
from djongo import models

from django.contrib.auth.models import (
  AbstractBaseUser, 
  BaseUserManager, 
  PermissionsMixin,
)

from main.helpers import TimestampedModel

class UserManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    if username is None:
      raise TypeError('Users must have a username.')

    if email is None:
      raise TypeError('Users must have an email address.')

    user = self.model(username=username, email=self.normalize_email(email))
    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, username, email, password):
    if password is None:
      raise TypeError('Superusers must have a password.')

    user = self.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return user

class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
  username = models.CharField(db_index=True, max_length=255, unique=True)
  email = models.EmailField(db_index=True, unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  objects = UserManager()

  class Meta:
    db_table = 'users'
    ordering = ['-username']

  def __str__(self):
    return f"{self.username}, {self.email}"

  @property
  def token(self):
    return self._generate_jwt_token()

  def get_full_name(self):
    return self.username

  def get_short_name(self):
    return self.username

  def _generate_jwt_token(self):
    dt = datetime.now() + timedelta(days=60)
    token = jwt.encode({
      'id': self.pk,
      'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')


--#

--% /django-starter1/apps/profile/__init__.py
--#

--% /django-starter1/apps/profile/renderers.py
from main.helpers import CustomJSONRenderer

class ProfileJSONRenderer(CustomJSONRenderer):
  object_label = 'profile'
  pagination_object_label = 'profiles'
  pagination_count_label = 'profilesCount'

--#

--% /django-starter1/apps/profile/views.py
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer

class ProfileRetrieveAPIView(RetrieveAPIView):
  permission_classes = (AllowAny,)
  queryset = Profile.objects.select_related('user')
  renderer_classes = (ProfileJSONRenderer,)
  serializer_class = ProfileSerializer

  def retrieve(self, request, username, *args, **kwargs):
    try:
      profile = self.queryset.get(user__username=username)
    except Profile.DoesNotExist:
      raise NotFound('A profile with this username does not exist.')

    serializer = self.serializer_class(profile, context = {
      'request': request
    })

    return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileFollowAPIView(APIView):
  permission_classes = (IsAuthenticated,)
  renderer_classes = (ProfileJSONRenderer,)
  serializer_class = ProfileSerializer

  def delete(self, request, username=None):
    follower = self.request.user.profile
    try:
      followee = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
      raise NotFound('A profile with this username was not found.')

    follower.unfollow(followee)
    serializer = self.serializer_class(followee, context={
      'request': request
    })
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, username=None):
    follower = self.request.user.profile
    try:
      followee = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
      raise NotFound('A profile with this username was not found.')

    if follower.pk is followee.pk:
      raise serializers.ValidationError('You can not follow yourself.')

    follower.follow(followee)

    serializer = self.serializer_class(followee, context={
      'request': request
    })

    return Response(serializer.data, status=status.HTTP_201_CREATED)


--#

--% /django-starter1/apps/profile/urls.py
# from django.conf.urls import url
from django.urls import path, re_path
from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

urlpatterns = [
  re_path(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
  re_path(r'^profiles/(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
]

--#

--% /django-starter1/apps/profile/exceptions.py
from rest_framework.exceptions import APIException

class ProfileDoesNotExist(APIException):
  status_code = 400
  default_detail = 'The requested profile does not exist.'

--#

--% /django-starter1/apps/profile/serializers.py
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username')
  bio = serializers.CharField(allow_blank=True, required=False)
  image = serializers.SerializerMethodField()
  following = serializers.SerializerMethodField()

  class Meta:
    model = Profile
    fields = ('username', 'bio', 'image', 'following',)
    read_only_fields = ('username',)

  def get_image(self, obj):
    if obj.image:
      return obj.image

    return 'http://clipart-library.com/images/8TzngraXc.jpg'

  def get_following(self, instance):
    request = self.context.get('request', None)
    if request is None:
      return False

    if not request.user.is_authenticated():
      return False

    follower = request.user.profile
    followee = instance

    return follower.is_following(followee)
--#

--% /django-starter1/apps/profile/models.py
# from django.db import models
from djongo import models
from main.helpers import TimestampedModel

class Profile(TimestampedModel):
  user = models.OneToOneField(
    'user.User', on_delete=models.CASCADE
  )
  bio = models.TextField(blank=True)
  image = models.URLField(blank=True)
  follows = models.ManyToManyField(
    'self',
    related_name='followed_by',
    symmetrical=False
  )
  # favorites = models.ManyToManyField(
  #   'article.Article',
  #   related_name='favorited_by'
  # )
  def __str__(self):
    return self.user.username

  def follow(self, profile):
    self.follows.add(profile)

  def unfollow(self, profile):
    self.follows.remove(profile)

  def is_following(self, profile):
    return self.follows.filter(pk=profile.pk).exists()

  def is_followed_by(self, profile):
    return self.followed_by.filter(pk=profile.pk).exists()

  def favorite(self, article):
    self.favorites.add(article)

  # def unfavorite(self, article):
  #   self.favorites.remove(article)

  # def has_favorited(self, article):
  #   return self.favorites.filter(pk=article.pk).exists()

--#
