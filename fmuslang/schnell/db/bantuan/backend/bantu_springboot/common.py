from app.dirutils import (
  here, joiner
)
from db.bantuan.common import (
  output_folder,
  TEMPLATESDIR,
)
disini = here(__file__)

filename_input = 'springboot'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')

# tpl_appindex = joiner(TEMPLATESDIR, 'springboot_app_rest_index_v1.tpl')
tpl_appcontroller = joiner(TEMPLATESDIR, 'springboot_app_rest_controller_v1.tpl')
tpl_appmodel = joiner(TEMPLATESDIR, 'springboot_app_rest_model_v1.tpl')
tpl_appservice = joiner(TEMPLATESDIR, 'springboot_app_rest_service_v1.tpl')
tpl_apprepository = joiner(TEMPLATESDIR, 'springboot_app_rest_repository_v1.tpl')
tpl_appcreateinput = joiner(TEMPLATESDIR, 'springboot_app_rest_createinput_v1.tpl')
tpl_appupdateinput = joiner(TEMPLATESDIR, 'springboot_app_rest_updateinput_v1.tpl')
tpl_appquery = joiner(TEMPLATESDIR, 'springboot_app_rest_query_v1.tpl')
tpl_appmutation = joiner(TEMPLATESDIR, 'springboot_app_rest_mutation_v1.tpl')
tpl_appmapper_java = joiner(TEMPLATESDIR, 'springboot_app_rest_mapper_java_v1.tpl')
tpl_appmapper_xml = joiner(TEMPLATESDIR, 'springboot_app_rest_mapper_xml_v1.tpl')

tpl_appcontent = joiner(TEMPLATESDIR, 'springboot_app_content_v1.tpl')
