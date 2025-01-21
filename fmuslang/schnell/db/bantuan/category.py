"""
target:
django
flask
fastapi
node+mg
node+pg
springboot: rest+gql
react+antd
react+bs
react+mui
  berbagai charts:
  bizcharts
  chartjs
  echarts
  recharts
  berbagai map:
  leaflet
  esri

nextjs+mui
nestjs: rest+gql

low priority:
sensor+edge
flutter-base
reactnative-base
androidkotlin-base

generate:
node+react -> ecommerce
node+react -> sop
node+react -> diagram
node+react -> spor/sucor/backoffice
django+react -> ecommerce
django+react -> sosmed/mumble

low priority:
flask -> arsip, scraping
fastapi -> machine learning
"""

from .bantu_django import bantu_django
from .bantu_faker import bantu_faker
from .bantu_grpc import bantu_grpc
from .bantu_nest import bantu_nest as bantu_nest_old
from .bantu_sbgql import bantu_sbgql
from .bantu_sql import bantu_sql

from .frontend.redux import process_redux
from .fullstack import bantu_nodereact
from .fullstack.bantu_ts import bantu_ts
from .fullstack.nodeapollo.nodeapollo import bantu_nodeapollo
from .backend.bantu_fastapi.bantu_fastapi import bantu_fastapi
from .backend.bantu_flask.bantu_flask import bantu_flask
from .backend.bantu_springboot.bantu_springboot import bantu_springboot
from .backend.bantu_nest.bantu_nest import bantu_nest
from schnell.db.bantuan.dahsyat.tools.bantu_sql.bantu_sql import bantu_sql as bantu_flyway

category_map = {
  'django'      : bantu_django,
  'fake'        : lambda RootNode: bantu_faker(RootNode, 'json'),
  'fakejson'    : lambda RootNode: bantu_faker(RootNode, 'json_simple'),
  'fakecsv'     : lambda RootNode: bantu_faker(RootNode, 'csv'),
  'fastapi'     : bantu_fastapi,
  'flask'       : bantu_flask,
  'grpc'        : bantu_grpc,
  'nest2'       : bantu_nest_old,
  'nest'        : bantu_nest,
  'nodeapo'     : bantu_nodeapollo,
  'nodereact'   : bantu_nodereact,
  'sql'         : bantu_sql,
  'flyway'      : bantu_flyway,
  'sbgql'       : bantu_sbgql,
  'sboot'       : bantu_springboot,
  'ts'          : bantu_ts,
}

frontend_map = {
  'redux'       : process_redux,
}
