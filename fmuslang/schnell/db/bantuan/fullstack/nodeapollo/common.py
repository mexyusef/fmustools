from app.dirutils import (
  here, joiner
)
from db.bantuan.common import (
  output_folder,
  # TEMPLATESDIR,
)
disini = here(__file__)

filename_input = 'node-rest-graphql-2'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')

TEMPLATESDIR = joiner(disini, 'templates')
tpl_appgraphql = joiner(TEMPLATESDIR, 'nodeapollo_app_gql_template_v1.tpl')
tpl_appcontroller = joiner(TEMPLATESDIR, 'nodeapollo_app_rest_controller_v1.tpl')
tpl_appindex = joiner(TEMPLATESDIR, 'nodeapollo_app_rest_index_v1.tpl')
tpl_appmodel = joiner(TEMPLATESDIR, 'nodeapollo_app_rest_model_v1.tpl')
tpl_appservice = joiner(TEMPLATESDIR, 'nodeapollo_app_rest_service_v1.tpl')
tpl_appcontent = joiner(TEMPLATESDIR, 'nodeapollo_app_content_v1.tpl')
