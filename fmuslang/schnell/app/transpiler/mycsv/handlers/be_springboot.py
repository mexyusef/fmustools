from schnell.app.stringutils import tabify_content_tab, tabify_contentlist_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name
from schnell.app.libpohon.columnify import columnify, transform_table
from schnell.app.dirutils import joiner, joinhere
from schnell.app.fileutils import file_content, append_entry_tostring, get_definition_by_key_permissive_start
from schnell.app.libpohon.app_init import app_init
from schnell.app.libpohon.app_content import app_content
# C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\springboot\helper
from schnell.app.transpiler.frontend.fslang.springboot.helper import generate_app_xml_mapper

# C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\springboot\index-input.mk
# C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\springboot\templates\springboot_app_content_v1.tpl

# app
# 	transpiler
# 		frontend
# 			fslang
# 				springboot
# 					templates
# 		mycsv
# 			handlers

springboot_dir = joinhere(__file__, '../../../transpiler/frontend/fslang/springboot')
index_input_file = joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/index-input.mk')
index_input = file_content(index_input_file)
node_app_content = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_content_v1.tpl'))
tpl_appcontroller = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_controller_v1.tpl'))
tpl_appmodel = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_model_v1.tpl'))
tpl_appservice = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_service_v1.tpl'))
tpl_apprepository = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_repository_v1.tpl'))
tpl_appcreateinput = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_createinput_v1.tpl'))
tpl_appupdateinput = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_updateinput_v1.tpl'))
tpl_appquery = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_query_v1.tpl'))
tpl_appmutation = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_mutation_v1.tpl'))
tpl_appmapper_java = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_mapper_java_v1.tpl'))
tpl_appmapper_xml = file_content(joinhere(__file__, '../../../transpiler/frontend/fslang/springboot/templates/springboot_app_rest_mapper_xml_v1.tpl'))

mybatis_config = get_definition_by_key_permissive_start(index_input_file, '/springbooter/src/main/resources/mybatis-config.xml')
schema_gql = get_definition_by_key_permissive_start(index_input_file, '/springbooter/src/main/resources/graphql/schema.gql')
fulgent_app = get_definition_by_key_permissive_start(index_input_file, '/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/FulgentApplication.java')

def generate_app_repository(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_apprepository
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeRepository.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Repository.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'
		
	return kembali


def generate_app_service(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		per_table = tpl_appservice
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeService.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Service.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'
		
	return kembali


def generate_app_controller(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_appcontroller
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeController.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Controller.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'
		
	return kembali


def generate_app_model(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_appmodel
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeModel.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'
		
	return kembali


def generate_app_input(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table_create = tpl_appcreateinput
		per_table_create = per_table_create.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table_create = per_table_create.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table_update = tpl_appupdateinput
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
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header_create, per_table_create)
		kembali += per_table_create + '\n\n'

		header_update = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}UpdateInput.java'
		# entrify = append_entry(filepath_output,	header_update, per_table_update)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header_update, per_table_update)
		kembali += per_table_update + '\n\n'
		
	return kembali


def generate_app_query(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_appquery
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeQuery.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Query.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'
		
	return kembali


def generate_app_mutation(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_appmutation
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMutation.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Mutation.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'
		
	return kembali


def generate_app_mapper_java(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_appmapper_java
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMapper.java
		header = f'/springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/{tablename_lower}/{tablename_case}Mapper.java'
		# entrify = append_entry(filepath_output,	header, per_table)
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'

	return kembali


def generate_app_mapper_xml(tables):
	kembali = ''
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = tpl_appmapper_xml
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# /springbooter/src/main/java/__PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMapper.java
		# AttendeeMapper.xml,f(e=utama=/springbooter/src/main/resources/mapper/AttendeeMapper.xml)
		# /springbooter/src/main/resources/mapper/AttendeeMapper.xml
		header = f'/springbooter/src/main/resources/mapper/{tablename_case}Mapper.xml'
		# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
		kembali += per_table + '\n\n'

	return kembali


# C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\springboot\helper\__init__.py
from schnell.app.usutils import tab
from schnell.app.transpiler.frontend.fslang.springboot.helper.create_typedefs import create_typedefs
from schnell.app.transpiler.frontend.fslang.springboot.helper.create_inputs import create_inputs
from schnell.app.transpiler.frontend.fslang.springboot.helper.create_querytypes import create_querytypes
from schnell.app.transpiler.frontend.fslang.springboot.helper.create_mutationtypes import create_mutationtypes
from schnell.app.transpiler.frontend.fslang.springboot.helper.create_rootapp_autowired import create_rootapp_autowired

template_rootapp_import_perapp = """
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseService;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseRepository;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseQuery;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseMutation;
"""

def be_springboot(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	provider ='be_springboot'

	kembali += generate_app_repository(tables)
	kembali += '\n'
	kembali += generate_app_service(tables)
	kembali += '\n'
	kembali += generate_app_controller(tables)
	kembali += '\n'
	kembali += generate_app_model(tables)
	kembali += '\n'
	kembali += generate_app_input(tables)
	kembali += '\n'
	kembali += generate_app_query(tables)
	kembali += '\n'
	kembali += generate_app_mutation(tables)
	kembali += '\n'
	kembali += generate_app_mapper_java(tables)
	kembali += '\n'
	kembali += generate_app_mapper_xml(tables)
	kembali += '\n'


	__TEMPLATE_APP_XML_TYPEALIASES_LIST__ = [f'__TAB(2)<typeAlias alias="{table.model.lower()}" type="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.{table.model.lower()}.{table.model}" />' for table in tables]
	__TEMPLATE_APP_XML_TYPEALIASES_LIST__ = [item.replace('__TAB(2)', tab(2)) for item in __TEMPLATE_APP_XML_TYPEALIASES_LIST__]
	__TEMPLATE_APP_XML_TYPEALIASES__ = '\n'.join(__TEMPLATE_APP_XML_TYPEALIASES_LIST__)

	__TEMPLATE_APP_XMLMAPPERS_LIST_ = [f'__TAB(2)<mapper resource="mapper/{table.model}Mapper.xml"/>' for table in tables]
	__TEMPLATE_APP_XMLMAPPERS_LIST_ = [item.replace('__TAB(2)', tab(2)) for item in __TEMPLATE_APP_XMLMAPPERS_LIST_]
	__TEMPLATE_APP_XML_MAPPERS__ = '\n'.join(__TEMPLATE_APP_XMLMAPPERS_LIST_)

	kembali += '*'*20 + '[resources/mybatis-config.xml]' + '\n'
	kembali += (mybatis_config.replace('__TEMPLATE_APP_XML_TYPEALIASES__', __TEMPLATE_APP_XML_TYPEALIASES__)
		.replace('__TEMPLATE_APP_XML_MAPPERS__', __TEMPLATE_APP_XML_MAPPERS__))
	kembali += '\n'

	__TEMPLATE_APP_TYPEDEFS__ = create_typedefs(tables)
	__TEMPLATE_APP_INPUTTYPES__ = create_inputs(tables)
	__TEMPLATE_APP_QUERYTYPES__ = create_querytypes(tables)
	__TEMPLATE_APP_MUTATIONTYPES__ = create_mutationtypes(tables)

	kembali += '*'*20 + '[resources/schema.gql]' + '\n'
	kembali += (schema_gql.replace('__TEMPLATE_APP_TYPEDEFS__', __TEMPLATE_APP_TYPEDEFS__)
		.replace('__TEMPLATE_APP_INPUTTYPES__', __TEMPLATE_APP_INPUTTYPES__)
		.replace('__TEMPLATE_APP_QUERYTYPES__', __TEMPLATE_APP_QUERYTYPES__)
		.replace('__TEMPLATE_APP_MUTATIONTYPES__', __TEMPLATE_APP_MUTATIONTYPES__))
	kembali += '\n'

	__TEMPLATE_ROOTAPP_IMPORTS_LIST__ = [template_rootapp_import_perapp.replace('__tablename_lower', table.model.lower()).replace('__tablename_case', table.model) for table in tables]
	__TEMPLATE_ROOTAPP_IMPORTS__ = '\n'.join(__TEMPLATE_ROOTAPP_IMPORTS_LIST__)
	__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_ = [f'{table.model.lower()}Service' for table in tables]
	__TEMPLATE_ROOTAPP_SERVICEPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_)
	__TEMPLATE_ROOTAPP_AUTOWIRED__ = create_rootapp_autowired(tables)
	__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS_LIST_ = [f'{table.model}Service {table.model.lower()}Service' for table in tables]
	__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS_LIST_)
	__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_ = [f'new {table.model}Query({table.model.lower()}Service), new {table.model}Mutation({table.model.lower()}Service)' for table in tables]
	# query_mutation_service = ', '.join(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_)
	query_mutation_service = tabify_contentlist_tab(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_, 3, delim=',\n')
	__TEMPLATE_ROOTAPP_RESOLVERPARAMS__ = ',\n' + query_mutation_service

	kembali += '*'*20 + '[Application.java]' + '\n'
	kembali += (fulgent_app.replace('__TEMPLATE_ROOTAPP_IMPORTS__', __TEMPLATE_ROOTAPP_IMPORTS__)
		.replace('__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__', __TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__)
		.replace('__TEMPLATE_ROOTAPP_AUTOWIRED__', __TEMPLATE_ROOTAPP_AUTOWIRED__)
		.replace('__TEMPLATE_ROOTAPP_SERVICEPARAMS__', __TEMPLATE_ROOTAPP_SERVICEPARAMS__)
		.replace('__TEMPLATE_ROOTAPP_RESOLVERPARAMS__', __TEMPLATE_ROOTAPP_RESOLVERPARAMS__))
	kembali += '\n'

	return kembali
