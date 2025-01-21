from app.fileutils import (
	file_content,
	append_entry_tostring,
)
from app.dirutils import here, joiner
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	append_entry,
)
from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)

disini = here(__file__)

# tpl_appcontroller = joiner(disini, 'templates/springboot_app_rest_controller_v1.tpl')
# tpl_appmodel = joiner(disini, 'templates/springboot_app_rest_model_v1.tpl')
# tpl_appservice = joiner(disini, 'templates/springboot_app_rest_service_v1.tpl')
# tpl_apprepository = joiner(disini, 'templates/springboot_app_rest_repository_v1.tpl')
# tpl_appcreateinput = joiner(disini, 'templates/springboot_app_rest_createinput_v1.tpl')
# tpl_appupdateinput = joiner(disini, 'templates/springboot_app_rest_updateinput_v1.tpl')
# tpl_appquery = joiner(disini, 'templates/springboot_app_rest_query_v1.tpl')
# tpl_appmutation = joiner(disini, 'templates/springboot_app_rest_mutation_v1.tpl')
# tpl_appmapper_java = joiner(disini, 'templates/springboot_app_rest_mapper_java_v1.tpl')
# tpl_appmapper_xml = joiner(disini, 'templates/springboot_app_rest_mapper_xml_v1.tpl')

tpl_appmodule = joiner(disini, '../templates/nestjs_app_rest_module_v1.tpl')
tpl_appmodel = joiner(disini, '../templates/nestjs_app_rest_model_v1.tpl')
tpl_appresolver = joiner(disini, '../templates/nestjs_app_rest_resolver_v1.tpl')
tpl_appresolver_spec = joiner(disini, '../templates/nestjs_app_rest_resolverspec_v1.tpl')
tpl_appcontroller = joiner(disini, '../templates/nestjs_app_rest_controller_v1.tpl')
tpl_appcontroller_spec = joiner(disini, '../templates/nestjs_app_rest_controllerspec_v1.tpl')
tpl_appservice = joiner(disini, '../templates/nestjs_app_rest_service_v1.tpl')
tpl_appservice_spec = joiner(disini, '../templates/nestjs_app_rest_servicespec_v1.tpl')
tpl_appcontent = joiner(disini, '../templates/nestjs_app_content_v1.tpl')

# def generate_app_repository(tables, mkfile_input_content):
# 	for index, tbl in enumerate(tables,1):
# 		tablename_lower = tbl.model.lower()
# 		tablename_case = tbl.model

# 		per_table = file_content(tpl_apprepository)
# 		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
# 		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

# 		print('*'*40)
# 		print(per_table)
# 		print('~'*40)
# 		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeRepository.java
# 		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Repository.java'
# 		# entrify = append_entry(filepath_output,	header, per_table)
#     mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)    
#   return mkfile_input_content


def generate_app_module(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appmodule)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# attendee.module.ts,f(e=utama=/nestjs/src/attendee/attendee.module.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.module.ts'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content


def generate_app_service(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appservice)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table2 = file_content(tpl_appservice_spec)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('-'*20)
		print(per_table2)
		print('~'*40)
		# attendee.service.ts,f(e=utama=/nestjs/src/attendee/attendee.service.ts)
		# attendee.service.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.service.spec.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.service.ts'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		header2 = f'/nestjs/src/{tablename_lower}/{tablename_lower}.service.spec.ts'
		# entrify = append_entry(filepath_output,	header2, per_table2)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table2)
	return mkfile_input_content


def generate_app_controller(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appcontroller)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table2 = file_content(tpl_appcontroller_spec)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('-'*20)
		print(per_table2)
		print('~'*40)
		# attendee.controller.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.ts)
		# attendee.controller.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.spec.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.controller.ts'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		header2 = f'/nestjs/src/{tablename_lower}/{tablename_lower}.controller.spec.ts'
		# entrify = append_entry(filepath_output,	header2, per_table2)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table2)
	return mkfile_input_content


def generate_app_resolver(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appresolver)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		
		per_table2 = file_content(tpl_appresolver_spec)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('-'*20)
		print(per_table2)
		print('~'*40)
		# attendee.resolver.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.ts)
		# attendee.resolver.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.spec.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.resolver.ts'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		header2 = f'/nestjs/src/{tablename_lower}/{tablename_lower}.resolver.spec.ts'
		# entrify = append_entry(filepath_output,	header2, per_table2)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table2)
	return mkfile_input_content


def generate_app_model(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appmodel)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# attendee.model.ts,f(e=utama=/nestjs/src/attendee/attendee.model.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.model.ts'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content


def generate_app_graphql(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appgraphql)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.graphql.js'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content


def gen_models(tables, mkfile_input_content):
	mkfile_input_content = generate_app_module(tables, mkfile_input_content)
	mkfile_input_content = generate_app_model(tables, mkfile_input_content)
	mkfile_input_content = generate_app_service(tables, mkfile_input_content)
	mkfile_input_content = generate_app_controller(tables, mkfile_input_content)
	mkfile_input_content = generate_app_resolver(tables, mkfile_input_content)

	return mkfile_input_content

