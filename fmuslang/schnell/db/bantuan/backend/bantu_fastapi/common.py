from app.dirutils import (
  here, joiner
)
from db.bantuan.common import (
  output_folder,
  TEMPLATESDIR,
)
disini = here(__file__)

filename_input = 'myfastapi2'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')

tpl_appindex = joiner(disini, 'templates', 'fastapi_app_rest_index_v1.tpl')
tpl_appcontroller = joiner(disini, 'templates', 'fastapi_app_rest_crud_v1.tpl')
tpl_appmodel = joiner(disini, 'templates', 'fastapi_app_rest_models_v1.tpl')
tpl_appservice = joiner(disini, 'templates', 'fastapi_app_rest_routes_v1.tpl')
tpl_appcontent = joiner(disini, 'templates', 'fastapi_app_content_v1.tpl')

tpl_appgraphql = joiner(disini, 'templates', 'fastapi_app_schema_v1.tpl')
schema_import = joiner(disini, 'templates', 'replace_schema_import.tpl')
schema_fields = joiner(disini, 'templates', 'replace_schema_fields.tpl')