import os
# creatordir = os.path.dirname(__file__)
# schnelldir = os.path.dirname(creatordir)
# sidoarjodir = os.path.dirname(schnelldir)
# databasedir = os.path.join(sidoarjodir, 'database')
# bylangsdir = os.path.join(sidoarjodir, 'database/by-langs')
from pathlib import Path
curfile = Path(__file__).resolve()
schnelldir = curfile.parent.parent
sidoarjodir = schnelldir.parent
databasedir = sidoarjodir / 'database'
bylangsdir = databasedir / 'by-langs'

subdirs = [item for item in os.listdir(bylangsdir) if os.path.isdir(os.path.join(bylangsdir,item))]

# # proses
# # 1. tambah di sini
# # 2. tambah di lang.py
# subdirs = [
#   'akka',
#   'android',
#   'angular',
#   'algods',
#   'bahasa',
#   'buku',
#   'bun', # harusnya bisa deteksi konstruk=bun_package dan lang=py, if not is_konstruk_subdir, maka cek jk bun(_package) adlh subdir di by-langs
#   'crack',
#   'compete',
#   # duluan dari data
#   'database',
#   'data',
  
#   'devops',
#   'django',
#   # 'dotnet', # utk asp.net core, ganti ke aspnetcore di bawah

#   'fastapi',
#   'flask',
  
#   'flutter',
#   'gawe', 
#   'guilang',

#   'goweb','cppweb','rustweb', #'rust',

#   'html_css_js',
  
#   'aspnetcore',
#   'laravel',
#   'phoenix',
#   'rails',

#   'karya',
#   'mathematics',
#   'medium',
#   'ml',
#   'node', 'deno', 'nest',
#   'pattern',
#   'proto', # amqp mqtt grpc kafka rmq 0mq
  
#   # sementara reactnative hrs duluan dari react, klo gak dimakan oleh react
#   'reactnative',
#   'react', 'vue', 'next',
  
#   'spring', 'springboot',
#   'systems',
#   'mmm',
  
#   'parser',
#   'scraper',
#   'vscode',
#   'workup',
# ]
