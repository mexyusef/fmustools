from db.bantuan.bantu_django.bantu_django import bantu_django
from db.bantuan.backend.bantu_springboot.bantu_springboot import bantu_springboot
from db.bantuan.backend.bantu_nest.bantu_nest import bantu_nest
from db.bantuan.backend.bantu_flask.bantu_flask import bantu_flask
from db.bantuan.backend.bantu_fastapi.bantu_fastapi import bantu_fastapi
from db.bantuan.fullstack.nodeapollo.nodeapollo import bantu_nodeapollo
from db.bantuan.fullstack import bantu_nodereact
from db.bantuan.bantu_sql import bantu_sql
from db.bantuan.dahsyat.tools.bantu_sql.bantu_sql import bantu_sql as bantu_flyway

# kita bikin urutan ini adlh urutan yg digenerated
project_names = {
  'flyway'          : {
    'project_dir'   : 'migrations-flyway',
    'handler'       : bantu_flyway,
    'id'            : 0,
  },
  'django'          : {
    'project_dir'   : 'mydjango',
    'handler'       : bantu_django,
    'id'            : 1,
  },
  'nestjs'          : {
    'project_dir'   : 'mynest',
    'handler'       : bantu_nest,
    'id'            : 2,
  },
  'nodeapollo'          : {
    'project_dir'   : 'mynodeapollo',
    'handler'       : bantu_nodeapollo,
    'id'            : 3,
  },
  'nodereact'          : {
    'project_dir'   : 'mynodereact',
    'handler'       : bantu_nodereact,
    'id'            : 4,
  },
  'springboot'      : {
    'project_dir'   : 'myspringboot',
    'handler'       : bantu_springboot,
    'id'            : 5,
  },
  'flask'           : {
    'project_dir'   : 'myflask',
    'handler'       : bantu_flask,
    'id'            : 6,
  },
  'fastapi'         : {
    'project_dir'   : 'myfastapi',
    'handler'       : bantu_fastapi,
    'id'            : 7,
  },


  'sql'          : {
    'project_dir'   : 'migrations-sql',
    'handler'       : bantu_sql,
    'id'            : 99,
  },
}
