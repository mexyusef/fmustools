from anytree.search import find, findall
from anytree import RenderTree
from schnell.app.stringutils import tabify_content
from schnell.app.printutils import indah3

from .django_orm import django_orm
from .be_fastapi import be_fastapi
from .be_flask import be_flask
from .hibernate import hibernate
from .mongoose import mongoose
from .mybatis import mybatis
from .prisma import prisma
from .sequelize import sequelize
from .sql_mssql import sql_mssql
from .sql_mysql import sql_mysql
from .sql_postgres import sql_postgres
from .sql_sqlite import sql_sqlite
from .struct_go import struct_go
from .struct_kt import struct_kt
from .struct_rs import struct_rs
from .struct_ts import struct_ts
from .struct_java import struct_java
from .nest_typeorm import nest_typeorm
from .nest_mongoose import nest_mongoose
from .help_nest_mongo import help_nest_mongo
from .help_nest_postgres import help_nest_postgres
from schnell.db.bantuan.bantu_faker import bantu_faker
from .everything import everything
from .fmusdir import fmusdir


provider_map = {
  # keys harus sesuai dengan csv_operations
  'everything'      : everything,
  'fmusdir'         : fmusdir,

  'django_orm'      : django_orm,
  'be_flask'        : be_flask,
  'be_fastapi'      : be_fastapi,
  'mongoose'        : mongoose,
  'sequelize'       : sequelize,
  'sql_postgres'    : sql_postgres,
  'sql_mssql'       : sql_mssql,
  'sql_mysql'       : sql_mysql,
  'sql_sqlite'      : sql_sqlite,
  'nest_typeorm'    : nest_typeorm,
  'nest_mongoose'   : nest_mongoose,
  'prisma'          : prisma,
  'hibernate'       : hibernate,
  'mybatis'         : mybatis,
  'struct_go'       : struct_go,
  'struct_rs'       : struct_rs,
  'struct_kt'       : struct_kt,
  'struct_ts'       : struct_ts,
  'struct_java'     : struct_java,
  'help_nest_mongo'     : help_nest_mongo,
  'help_nest_postgres'  : help_nest_postgres,

  # 'fake'        : lambda RootNode: bantu_faker(RootNode, 'json'),
  # 'fakejson'    : lambda RootNode: bantu_faker(RootNode, 'json_simple'),
  # 'fakecsv'     : lambda RootNode: bantu_faker(RootNode, 'json_csv'),
}

from schnell.langs.ucsv import processor
# confirm('mycsv handler #20 LAST')


def handler(code, providers=[], returning=False, debug=True):
  RootNode = processor(code, print)
  # root: AnyNode(dbname='hapuslah', host='localhost', label='root', output='', outputs=[], password='rahasia', port=5432, type='root', username='usef')
  # .type=='root', .label=='root', .host, .port, .dbname, .username, .password
  # print('root:', RootNode)
  if debug:
    print(RenderTree(RootNode))
    if providers:
      print('\n\n[app.transpiler.mycsv.handlers], providers:', providers, '\n')
    else:
      print('\n\nproviders (mg, sqlz, pg, go, etc) empty, not giving results\n')
  node_tables = lambda node: hasattr(node, 'name') and node.name == 'table' and node.type == 'table'
  # print('type node_tables:', type(node_tables))
  tables = findall(RootNode, node_tables)
  results = []
  for prov in providers:
    if prov == 'json1':
      res = bantu_faker(RootNode, 'json')
    elif prov == 'json2':
      res = bantu_faker(RootNode, 'json_simple')
    elif prov == 'csv':
      res = bantu_faker(RootNode, 'csv')
    else:
      if prov in ['everything', 'fmusdir']:
        res = provider_map[prov](tables, RootNode)
      else:
        res = provider_map[prov](tables)
    results.append(res)

  if returning:
    return results

  if results:
    # pemisah = '//'
    # hasil = [f'{pemisah} {providers[idx]}\n'+item for idx,item in enumerate(results)]
    # hapus: // everything, // mg, dsb
    hasil = [item for idx,item in enumerate(results)]
    hasil = '\n\n'.join(hasil)
    indah3(hasil, warna='green')

  print('\n\n')
  return ''
