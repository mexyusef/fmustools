from app.dirutils import (
  ayah, joiner, here,
)
from app.fileutils import (
  file_content,
)

field_map = {
	'string'						: 'string',
	'float'							: 'number',
}

disini = joiner(here(__file__), 'templates')
dir_bantu_nest = ayah(__file__, 1)
dir_bantuan = ayah(dir_bantu_nest, 1)
dir_template = joiner(dir_bantuan, 'templates')


template_appmodule_file = joiner(disini, 'nestjs_appmodule_v1.tpl')
template_appmodule = file_content(template_appmodule_file)

template_module_file = joiner(disini, 'nestjs_module_v1.tpl')
template_module = file_content(template_module_file)

template_service_file = joiner(disini, 'nestjs_service_rest_v1.tpl')
template_service = file_content(template_service_file)

template_rest_file = joiner(disini, 'nestjs_rest_support_v1.tpl')
template_rest = file_content(template_rest_file)

template_controller_file = joiner(disini, 'nestjs_controller_v1.tpl')
template_controller = file_content(template_controller_file)

template_resolver_file = joiner(disini, 'nestjs_resolver_v1.tpl')
template_resolver = file_content(template_resolver_file)

template_gql_file = joiner(disini, 'nestjs_gql_support_v1.tpl')
template_gql = file_content(template_gql_file)