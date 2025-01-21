from app.fileutils import file_content
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	tab,
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


xml_mapper_entry = """
__TAB(5)$$GANTI_DENGAN_MODEL_TITLE$$Mapper.xml,f(e=utama=/springbooter/src/main/resources/mapper/$$GANTI_DENGAN_MODEL_TITLE$$Mapper.xml)
"""

def generate_app_xml_mapper(tables, print_info=False):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		tablename = tbl.model
		appidx = str(index).zfill(2)
		content = xml_mapper_entry
		content = content \
			.replace('__TAB(9)', tab(9)) \
			.replace('__TAB(8)', tab(8)) \
			.replace('__TAB(7)', tab(7)) \
			.replace('__TAB(6)', tab(6)) \
			.replace('__TAB(5)', tab(5)) \
			.replace('__TAB(4)', tab(4)) \
			.replace('__TAB(3)', tab(3)) \
			.replace('__TAB(2)', tab(2)) \
			.replace('__TAB(1)', tab(1))

		content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
		# content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
		# content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
		content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.upper())
		content = content.replace('$$GANTI_DENGAN_MODEL_TITLE$$', tablename)
		content = content.replace('$$GANTI_DENGAN_MODEL_LOWER$$', tablename.lower())
		content = content.replace('$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$', tablename + 's')
		content = content.replace('$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$', tablename.lower() + 's')

		contentlines.append(content)

	# template_app_content = '\n'.join([tab(2)+item for item in contentlines])
	template_app_content = '\n'.join([item for item in contentlines])
	if print_info:
		print('='*20, 'contentlines')
		print(template_app_content)

	return template_app_content

def generate_server_app_content(tables, print_info=False):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model
		tablename_lower = tbl.model.lower()

		content = file_content(tpl_appcontent)
		content = content \
			.replace('__TAB(9)', tab(9)) \
			.replace('__TAB(8)', tab(8)) \
			.replace('__TAB(7)', tab(7)) \
			.replace('__TAB(6)', tab(6)) \
			.replace('__TAB(5)', tab(5)) \
			.replace('__TAB(4)', tab(4)) \
			.replace('__TAB(3)', tab(3)) \
			.replace('__TAB(2)', tab(2)) \
			.replace('__TAB(1)', tab(1))
		content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
		# content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
		# content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
		content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.upper())
		content = content.replace('$$GANTI_DENGAN_MODEL_TITLE$$', tablename)
		content = content.replace('$$GANTI_DENGAN_MODEL_LOWER$$', tablename.lower())
		content = content.replace('$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$', tablename + 's')
		content = content.replace('$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$', tablename.lower() + 's')

		content = content.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		content = content.replace('__TEMPLATE_TABLENAME_CASE__', tablename)
		contentlines.append(content)

	# template_app_content = '\n'.join([tab(2)+item for item in contentlines])
	template_app_content = '\n'.join([item for item in contentlines])
	if print_info:
		print('='*20, 'contentlines')
		print(template_app_content)

	return template_app_content


template_rootapp_import_perapp = """
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseService;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseRepository;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseQuery;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseMutation;
"""


create_typedefs_fieldlist_default = """
	id: ID!
	name: String!
"""

create_typedefs_template = """
type __TEMPLATE_TABLENAME_CASE__ {
__TYPEDEFS_FIELDLIST__
}
"""

def create_typedefs(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()

		per_table = create_typedefs_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		# harusnya oprek tiap field...
		per_table = per_table.replace('__TYPEDEFS_FIELDLIST__', create_typedefs_fieldlist_default.strip())
		result.append(per_table)

	return '\n'.join(result)

# input AttendeeInput {


# }
create_inputs_fieldlist_default = """
	id: ID
	name: String
"""
create_inputs_template = """
input __TEMPLATE_TABLENAME_CASE__CreateInput {
__TYPEDEFS_CREATEFIELDLIST__
}
input __TEMPLATE_TABLENAME_CASE__UpdateInput {
__TYPEDEFS_UPDATEFIELDLIST__
}
"""
def create_inputs(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()

		per_table = create_inputs_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		# harusnya oprek tiap field...
		per_table = per_table.replace('__TYPEDEFS_CREATEFIELDLIST__', create_inputs_fieldlist_default.strip())
		per_table = per_table.replace('__TYPEDEFS_UPDATEFIELDLIST__', create_inputs_fieldlist_default.strip())
		result.append(per_table)

	return '\n'.join(result)


create_querytypes_template = """
all__TEMPLATE_TABLENAME_CASE__s: [__TEMPLATE_TABLENAME_CASE__]
find__TEMPLATE_TABLENAME_CASE__ById(id: ID): __TEMPLATE_TABLENAME_CASE__
"""

def create_querytypes(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()
		per_table = create_querytypes_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		result.append(per_table)

	return '\n'.join(result)


create_mutationtypes_template = """
create__TEMPLATE_TABLENAME_CASE__(__TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__CreateInput): __TEMPLATE_TABLENAME_CASE__
update__TEMPLATE_TABLENAME_CASE__(id: ID, __TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__UpdateInput): __TEMPLATE_TABLENAME_CASE__
delete__TEMPLATE_TABLENAME_CASE__(id: ID): String
"""

def create_mutationtypes(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()
		per_table = create_mutationtypes_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		result.append(per_table)

	return '\n'.join(result)

create_rootapp_autowired_template = """
  @Autowired
  private __TEMPLATE_TABLENAME_CASE__Service __TEMPLATE_TABLENAME_LOWER__Service;
"""

def create_rootapp_autowired(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()
		per_table = create_rootapp_autowired_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		result.append(per_table)

	return '\n'.join(result)

def assign_remaining_variables(tables, mkfile_template):
	"""
	"""
	__TEMPLATE_APP_XML_TYPEALIASES_LIST__ = [f'__TAB(2)<typeAlias alias="{table.model.lower()}" type="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.{table.model.lower()}.{table.model}" />' for table in tables]
	__TEMPLATE_APP_XML_TYPEALIASES_LIST__ = [item.replace('__TAB(2)', tab(2)) for item in __TEMPLATE_APP_XML_TYPEALIASES_LIST__]
	__TEMPLATE_APP_XML_TYPEALIASES__ = '\n'.join(__TEMPLATE_APP_XML_TYPEALIASES_LIST__)

	__TEMPLATE_APP_XMLMAPPERS_LIST_ = [f'__TAB(2)<mapper resource="mapper/{table.model}Mapper.xml"/>' for table in tables]
	__TEMPLATE_APP_XMLMAPPERS_LIST_ = [item.replace('__TAB(2)', tab(2)) for item in __TEMPLATE_APP_XMLMAPPERS_LIST_]
	__TEMPLATE_APP_XML_MAPPERS__ = '\n'.join(__TEMPLATE_APP_XMLMAPPERS_LIST_)

	__TEMPLATE_APP_TYPEDEFS__ = create_typedefs(tables)
	__TEMPLATE_APP_INPUTTYPES__ = create_inputs(tables)
	__TEMPLATE_APP_QUERYTYPES__ = create_querytypes(tables)
	__TEMPLATE_APP_MUTATIONTYPES__ = create_mutationtypes(tables)

	__TEMPLATE_ROOTAPP_IMPORTS_LIST__ = [template_rootapp_import_perapp.replace('__tablename_lower', table.model.lower()).replace('__tablename_case', table.model) for table in tables]
	__TEMPLATE_ROOTAPP_IMPORTS__ = '\n'.join(__TEMPLATE_ROOTAPP_IMPORTS_LIST__)

	__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_ = [f'{table.model.lower()}Service' for table in tables]
	__TEMPLATE_ROOTAPP_SERVICEPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_)

	__TEMPLATE_ROOTAPP_AUTOWIRED__ = create_rootapp_autowired(tables)

	__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS_LIST_ = [f'{table.model}Service {table.model.lower()}Service' for table in tables]
	__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS_LIST_)

	__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_ = [f'new {table.model}Query({table.model.lower()}Service), new {table.model}Mutation({table.model.lower()}Service)' for table in tables]
	__TEMPLATE_ROOTAPP_RESOLVERPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_)

	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_XML_TYPEALIASES__', __TEMPLATE_APP_XML_TYPEALIASES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_XML_MAPPERS__', __TEMPLATE_APP_XML_MAPPERS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_TYPEDEFS__', __TEMPLATE_APP_TYPEDEFS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_INPUTTYPES__', __TEMPLATE_APP_INPUTTYPES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_QUERYTYPES__', __TEMPLATE_APP_QUERYTYPES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_MUTATIONTYPES__', __TEMPLATE_APP_MUTATIONTYPES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_IMPORTS__', __TEMPLATE_ROOTAPP_IMPORTS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__', __TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_AUTOWIRED__', __TEMPLATE_ROOTAPP_AUTOWIRED__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_SERVICEPARAMS__', __TEMPLATE_ROOTAPP_SERVICEPARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_RESOLVERPARAMS__', __TEMPLATE_ROOTAPP_RESOLVERPARAMS__)
	return mkfile_template


def gen_mkfile(RootNode, project_dir='input'):
	tables = get_tables(RootNode)

	print(f"generate from:", filepath_input)
	print(f"generate to:", filepath_output)
	print(f"tables:", [item.model for item in tables])

	mkfile_template = file_content(filepath_input) \
		.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', project_dir)

	template_db_init = gen_template_db_init(RootNode)
	mkfile_template = mkfile_template.replace('__TEMPLATE_DB_INIT', template_db_init)

	template_app_init = gen_template_app_init(tables)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_INIT', template_app_init)

	server_app_content = generate_server_app_content(tables)
	mkfile_template = mkfile_template.replace('__TEMPLATE_SERVER_APP_CONTENT', server_app_content)

	xml_mapper_content = generate_app_xml_mapper(tables)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_XMLMAPPER_ENTRY', xml_mapper_content)

	mkfile_template = assign_remaining_variables(tables, mkfile_template)

	write_mkfile(mkfile_template, filepath_output)

	return tables
