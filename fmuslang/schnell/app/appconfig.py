# from schnell.app.appconfig import appconfig as AP
appconfig = {
  'last_expand_linktag': None,

  # khusus koneksi redis
  'redisconn': None,

  # holder utk anything...
  'any': None,
}

# global data utk bantuan
bantuan_data = {
  'bantuan_basedir': '/tmp',
}

# utk hold soup object, lxml doc object, requests.content dll
requests_data = {}

# utk taro berbagai variables dlm polyglot programming
programming_data = {}

# terutama utk
# res = column_attrs(column, provider)
# di dalam app.libpohon.columnify
libpohon_data = {
  'import_part': [
    'from django.db import models',
  ],
  'import_part_by_table': {},
  'django_auto_request': False,
}

declarative_language_data = {
  'creator.declarative.handler': {}
}

command_prompt_data = {}
command_prompt_data_extension = {}
