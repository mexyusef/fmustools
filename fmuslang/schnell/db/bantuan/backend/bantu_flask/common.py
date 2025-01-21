from app.dirutils import (
  here, joiner
)
from db.bantuan.common import (
  output_folder,
  TEMPLATESDIR,
)
disini = here(__file__)

filename_input = 'myflask2'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')

# tpl_appindex = joiner(TEMPLATESDIR, 'flask_app_rest_index_v1.tpl')
tpl_appindex = joiner(disini, 'templates/app_init_v1.py')

# tpl_appcontroller = joiner(TEMPLATESDIR, 'flask_app_rest_controller_v1.tpl')

# tpl_appmodel = joiner(TEMPLATESDIR, 'flask_app_rest_model_v1.tpl')
tpl_appmodel = joiner(disini, 'templates/app_models_v1.py')

# tpl_appservice = joiner(TEMPLATESDIR, 'flask_app_rest_routes_v1.tpl')
# tpl_appforms = joiner(TEMPLATESDIR, 'flask_app_rest_forms_v1.tpl')
tpl_appforms = joiner(disini, 'templates/app_forms_v1.py')

# tpl_appresource = joiner(TEMPLATESDIR, 'flask_app_rest_resource_v1.tpl')
tpl_appresource = joiner(disini, 'templates/app_resource_v1.py')

tpl_approutes = joiner(disini, 'templates', 'app_routes_v1.py')

# tpl_appcontent = joiner(TEMPLATESDIR, 'flask_app_content_v1.tpl')
tpl_appcontent = joiner(disini, 'templates', 'apps_mk_content_v1.py')
