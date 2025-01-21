from app.dirutils import (
  here, joiner
)
from db.bantuan.common import (
  output_folder,
  TEMPLATESDIR,
)
disini = here(__file__)
templates = joiner(disini, 'templates')
filename_input = 'nest_rest_gql'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')

tpl_appcontent = joiner(templates, 'nestjs_app_content_v1.tpl')

tpl_appmodule = joiner(templates, 'nestjs_app_rest_module_v1.tpl')
tpl_appmodel = joiner(templates, 'nestjs_app_rest_model_v1.tpl')
tpl_appresolver = joiner(templates, 'nestjs_app_rest_resolver_v1.tpl')
tpl_appresolver_spec = joiner(templates, 'nestjs_app_rest_resolverspec_v1.tpl')
tpl_appcontroller = joiner(templates, 'nestjs_app_rest_controller_v1.tpl')
tpl_appcontroller_spec = joiner(templates, 'nestjs_app_rest_controllerspec_v1.tpl')
tpl_appservice = joiner(templates, 'nestjs_app_rest_service_v1.tpl')
tpl_appservice_spec = joiner(templates, 'nestjs_app_rest_servicespec_v1.tpl')
