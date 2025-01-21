from app.dirutils import joiner
from app.fileutils import (
  file_content,
  replace_string_in_file,
)
from app.utils import env_get

from ..common import tab
from ..config import output_django_mkfile
from .helper import append_entry

"""
__TEMPLATE_TABLENAME_CASE__
__TEMPLATE_TABLENAME_LOWER__

__TEMPLATE_TABLENAME_GRAPHQLFIELDS__
title = graphene.String()
content = graphene.String()

# title, content
__TEMPLATE_TABLENAME_SIMPLEPARAMFIELDS__

# title=None, content=None
__TEMPLATE_TABLENAME_ASNONEPARAMFIELDS__

__TEMPLATE_TABLENAME_ASSIGNPARAMFIELDS__
article = Article.objects.create(
  title = title, content = content
)

__TEMPLATE_TABLENAME_VALUEASSIGNMENTS__
if title:
  article.title = title
if content:
  article.content = content
"""


graphql_types_mapper = {
	# 'bigint':       'BIGINT',
	# 'double':       'DOUBLE',
	# 'enum':         'ENUM',

	'float':        'graphene.Float()',
	'id':           'graphene.ID()',

	'boolean':      'graphene.Boolean()',
	'date':         'graphene.types.datetime.DateTime()',
	'timestamp':    'graphene.types.datetime.DateTime()',
  
  'string':       'graphene.String()',
	'text':         'graphene.String()',
  'varchar':      'graphene.String()',

	'integer':      'graphene.Int()',
	'auto':					'graphene.ID()',
}

app_schema_template_filename = 'db/bantuan/templates/django-graphql-app-schema-v1.tpl'
app_schema_template_filepath = joiner(env_get('ULIBPY_BASEDIR'), app_schema_template_filename)


def value_assignment(tablename, item):
  return f"if {item}:\n{tab(1)}{tablename}.{item} = {item}"


def handle_app_schema(tables):

  # app_templates_result = []
 
  for tblindex, tbl in enumerate(tables,1):
    __TEMPLATE_TABLENAME_CASE__ = tbl.model
    __TEMPLATE_TABLENAME_LOWER__ = tbl.model.lower()
    app_template = file_content(app_schema_template_filepath)
    app_template = app_template.replace('__TEMPLATE_TABLENAME_CASE__', __TEMPLATE_TABLENAME_CASE__)
    app_template = app_template.replace('__TEMPLATE_TABLENAME_LOWER__', __TEMPLATE_TABLENAME_LOWER__)

    # for colindex, node in enumerate(tbl.children):
    #   '''
    #   skip utk id
    #   node
    #     type
    #     label
    #   '''
    #   if node.label == 'id':
    #     continue

    columns = [node.label for node in tbl.children if node.label != 'id']
    # coltypes = [node.type for node in tbl.children if node.label != 'id']
    name_types = [(node.label, node.type) for node in tbl.children if node.label != 'id']
    if columns:
      gql_fields = [f"{nama} = {graphql_types_mapper.get(jenis, jenis)}" for (nama,jenis) in name_types]
      __TEMPLATE_TABLENAME_GRAPHQLFIELDS__ = '\n'.join([tab(2)+item for item in gql_fields]) # tab
      __TEMPLATE_TABLENAME_SIMPLEPARAMFIELDS__ = ', '.join([item for item in columns])
      __TEMPLATE_TABLENAME_ASNONEPARAMFIELDS__ = ', '.join([f"{item} = None" for item in columns])
      __TEMPLATE_TABLENAME_ASSIGNPARAMFIELDS__ = ', '.join([f"{item} = {item}" for item in columns])
      value_assign = '\n'.join([value_assignment(__TEMPLATE_TABLENAME_LOWER__, item) for item in columns])
      # print(f'value_assign, sblmn split: [{value_assign}]')
      value_assign_linify = value_assign.splitlines()
      # print(f'value_assign, stlh split: [{value_assign}]')
      value_assign_indent = [tab(3) + item for item in value_assign_linify]
      # print(f'value_assign, stlh indent: [{value_assign}]')
      __TEMPLATE_TABLENAME_VALUEASSIGNMENTS__ = '\n'.join(value_assign_indent)
      # print(f'value_assign, akhir: [{__TEMPLATE_TABLENAME_VALUEASSIGNMENTS__}]')

      app_template = app_template.replace('__TEMPLATE_TABLENAME_GRAPHQLFIELDS__', __TEMPLATE_TABLENAME_GRAPHQLFIELDS__)
      app_template = app_template.replace('__TEMPLATE_TABLENAME_SIMPLEPARAMFIELDS__', __TEMPLATE_TABLENAME_SIMPLEPARAMFIELDS__)
      app_template = app_template.replace('__TEMPLATE_TABLENAME_ASNONEPARAMFIELDS__', __TEMPLATE_TABLENAME_ASNONEPARAMFIELDS__)
      app_template = app_template.replace('__TEMPLATE_TABLENAME_ASSIGNPARAMFIELDS__', __TEMPLATE_TABLENAME_ASSIGNPARAMFIELDS__)
      app_template = app_template.replace('__TEMPLATE_TABLENAME_VALUEASSIGNMENTS__', __TEMPLATE_TABLENAME_VALUEASSIGNMENTS__)

    # app_templates_result.append(app_template)
    append_entry(__TEMPLATE_TABLENAME_CASE__, app_template, 'schema.py')

"""
kita mengisi:
from apps.article.schema import schema as article_schema
__TEMPLATE_SCHEMA_APP_IMPORTS__
article_schema.Query
__TEMPLATE_SCHEMA_APP_QUERIES__
article_schema.Mutation
__TEMPLATE_SCHEMA_APP_MUTATIONS__

utk:
import graphene
# from apps.article.schema import schema as article_schema
__TEMPLATE_SCHEMA_APP_IMPORTS__

class Query(__TEMPLATE_SCHEMA_APP_QUERIES__, graphene.ObjectType):
  pass

class Mutation(__TEMPLATE_SCHEMA_APP_MUTATIONS__.Mutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
"""
def handle_main_schema(tables):
  import_separator = '\n'
  query_mutation_separator = ', '
  __TEMPLATE_SCHEMA_APP_IMPORTS__ = []
  __TEMPLATE_SCHEMA_APP_QUERIES__ = []
  __TEMPLATE_SCHEMA_APP_MUTATIONS__ = []
  for index, tbl in enumerate(tables,1):
    appname = tbl.model
    appnamelower = appname.lower()
    app_query = f"{appnamelower}_schema.Query"
    app_mutation = f"{appnamelower}_schema.Mutation"
    entry_import = f"from apps.{appnamelower}.schema import schema as {appnamelower}_schema"
    __TEMPLATE_SCHEMA_APP_IMPORTS__.append(entry_import)
    __TEMPLATE_SCHEMA_APP_QUERIES__.append(app_query)
    __TEMPLATE_SCHEMA_APP_MUTATIONS__.append(app_mutation)

  importsval = import_separator.join(__TEMPLATE_SCHEMA_APP_IMPORTS__)
  queriesval = query_mutation_separator.join(__TEMPLATE_SCHEMA_APP_QUERIES__)
  mutationsval = query_mutation_separator.join(__TEMPLATE_SCHEMA_APP_MUTATIONS__)
  # return importsval, queriesval, mutationsval
  replace_string_in_file(output_django_mkfile, '__TEMPLATE_SCHEMA_APP_IMPORTS__', importsval)
  replace_string_in_file(output_django_mkfile, '__TEMPLATE_SCHEMA_APP_QUERIES__', queriesval)
  replace_string_in_file(output_django_mkfile, '__TEMPLATE_SCHEMA_APP_MUTATIONS__', mutationsval)


def generate_graphql(tables):
  handle_main_schema(tables)
  handle_app_schema(tables)
