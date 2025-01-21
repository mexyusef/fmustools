from app.dirutils import joiner
from app.fileutils import (
  file_content,
  replace_string_in_file,
)
from app.utils import env_get

# app_schema_template_filename = 'db/bantuan/templates/django-graphql-app-schema-v1.tpl'
# app_schema_template_filepath = joiner(env_get('ULIBPY_BASEDIR'), app_schema_template_filename)


template_appjson_filename = 'db/bantuan/templates/nodereact-appjson-template-v1.tpl'
template_appjson_filepath = joiner(env_get('ULIBPY_BASEDIR'), template_appjson_filename)

template_node_appcontent_filename = 'db/bantuan/templates/nodereact-node-appcontent-template-v1.tpl'
template_node_appcontent_filepath = joiner(env_get('ULIBPY_BASEDIR'), template_node_appcontent_filename)

template_react_appcontent_filename = 'db/bantuan/templates/nodereact-react-appcontent-template-v1.tpl'
template_react_appcontent_file = joiner(env_get('ULIBPY_BASEDIR'), template_react_appcontent_filename)
