from app.fileutils import file_content
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	append_entry,
)
from .common import (
	filepath_input,
	filepath_output,

	tpl_appcontent,

	tpl_appcontroller,
	tpl_appmodel,
	tpl_appservice,
	tpl_apprepository,
	tpl_appcreateinput,
	tpl_appupdateinput,
	tpl_appquery,
	tpl_appmutation,
	tpl_appmapper_java,
	tpl_appmapper_xml,
)

def generate_app_repository(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_service(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_controller(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_model(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_input(tables):
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
		entrify = append_entry(filepath_output,	header_create, per_table_create)
		header_update = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}UpdateInput.java'
		entrify = append_entry(filepath_output,	header_update, per_table_update)


def generate_app_query(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_mutation(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_mapper_java(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)


def generate_app_mapper_xml(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def gen_models(tables):
	# tpl_appcontroller,
	# tpl_appmodel,
	# tpl_appservice,
	# tpl_apprepository,
	# tpl_appinput,
	# tpl_appquery,
	# tpl_appmutation,
	# tpl_appmapper_java,
	# tpl_appmapper_xml,
	generate_app_repository(tables)
	generate_app_service(tables)
	generate_app_controller(tables)
	generate_app_model(tables)
	generate_app_input(tables)
	generate_app_query(tables)
	generate_app_mutation(tables)
	generate_app_mapper_java(tables)
	generate_app_mapper_xml(tables)
