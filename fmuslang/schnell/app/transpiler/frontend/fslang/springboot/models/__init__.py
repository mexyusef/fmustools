
from app.fileutils import (
	file_content,
	append_entry_tostring,
)
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
from app.dirutils import here, joiner

disini = here(__file__)

tpl_appcontroller = joiner(disini, '../templates/springboot_app_rest_controller_v1.tpl')
tpl_appmodel = joiner(disini, '../templates/springboot_app_rest_model_v1.tpl')
tpl_appservice = joiner(disini, '../templates/springboot_app_rest_service_v1.tpl')
tpl_apprepository = joiner(disini, '../templates/springboot_app_rest_repository_v1.tpl')
tpl_appcreateinput = joiner(disini, '../templates/springboot_app_rest_createinput_v1.tpl')
tpl_appupdateinput = joiner(disini, '../templates/springboot_app_rest_updateinput_v1.tpl')
tpl_appquery = joiner(disini, '../templates/springboot_app_rest_query_v1.tpl')
tpl_appmutation = joiner(disini, '../templates/springboot_app_rest_mutation_v1.tpl')
tpl_appmapper_java = joiner(disini, '../templates/springboot_app_rest_mapper_java_v1.tpl')
tpl_appmapper_xml = joiner(disini, '../templates/springboot_app_rest_mapper_xml_v1.tpl')


def generate_app_repository(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_apprepository)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeRepository.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Repository.java'
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

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeService.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Service.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		
	return mkfile_input_content


def generate_app_controller(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appcontroller)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeController.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Controller.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		
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
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeModel.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		
	return mkfile_input_content


def generate_app_input(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table_create = file_content(tpl_appcreateinput)
		per_table_create = per_table_create.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table_create = per_table_create.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table_update = file_content(tpl_appupdateinput)
		per_table_update = per_table_update.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table_update = per_table_update.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table_create)
		print('-'*20)
		print(per_table_update)
		print('~'*40)

		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeInput.java
		header_create = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}CreateInput.java'
		# entrify = append_entry(filepath_output,	header_create, per_table_create)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header_create, per_table_create)

		header_update = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}UpdateInput.java'
		# entrify = append_entry(filepath_output,	header_update, per_table_update)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header_update, per_table_update)
		
	return mkfile_input_content


def generate_app_query(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appquery)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeQuery.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Query.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		
	return mkfile_input_content


def generate_app_mutation(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appmutation)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMutation.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Mutation.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		
	return mkfile_input_content


def generate_app_mapper_java(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appmapper_java)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMapper.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Mapper.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)

	return mkfile_input_content


def generate_app_mapper_xml(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appmapper_xml)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMapper.java
		# AttendeeMapper.xml,f(e=utama=/springbooter/src/main/resources/mapper/AttendeeMapper.xml)
		# /springbooter/src/main/resources/mapper/AttendeeMapper.xml
		header = f'/springbooter/src/main/resources/mapper/{tablename_case}Mapper.xml'
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)

	return mkfile_input_content


def gen_models(tables, mkfile_input_content):
	mkfile_input_content = generate_app_repository(tables, mkfile_input_content)
	mkfile_input_content = generate_app_service(tables, mkfile_input_content)
	mkfile_input_content = generate_app_controller(tables, mkfile_input_content)
	mkfile_input_content = generate_app_model(tables, mkfile_input_content)
	mkfile_input_content = generate_app_input(tables, mkfile_input_content)
	mkfile_input_content = generate_app_query(tables, mkfile_input_content)
	mkfile_input_content = generate_app_mutation(tables, mkfile_input_content)
	mkfile_input_content = generate_app_mapper_java(tables, mkfile_input_content)
	mkfile_input_content = generate_app_mapper_xml(tables, mkfile_input_content)
	return mkfile_input_content

