from app.stringutils import (
	tabify_content_tab, 
	tabify_content_space,
	tabify_contentlist_space,
	tabify_contentlist_tab,
)
from app.usutils import tab

template_rootapp_import_perapp = """
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseService;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseRepository;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseQuery;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.__tablename_lower.__tablename_caseMutation;
"""

from .create_typedefs import create_typedefs
from .create_inputs import create_inputs
from .create_querytypes import create_querytypes
from .create_mutationtypes import create_mutationtypes
from .create_rootapp_autowired import create_rootapp_autowired

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
	# query_mutation_service = ', '.join(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_)
	query_mutation_service = tabify_contentlist_tab(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_, 3, delim=',\n')
	__TEMPLATE_ROOTAPP_RESOLVERPARAMS__ = ',\n' + query_mutation_service

	# mybatis-config.xml
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_XML_TYPEALIASES__', __TEMPLATE_APP_XML_TYPEALIASES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_XML_MAPPERS__', __TEMPLATE_APP_XML_MAPPERS__)
	# schema.gql
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_TYPEDEFS__', __TEMPLATE_APP_TYPEDEFS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_INPUTTYPES__', __TEMPLATE_APP_INPUTTYPES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_QUERYTYPES__', __TEMPLATE_APP_QUERYTYPES__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_MUTATIONTYPES__', __TEMPLATE_APP_MUTATIONTYPES__)
	# FulgentApplication.java
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_IMPORTS__', __TEMPLATE_ROOTAPP_IMPORTS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__', __TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_AUTOWIRED__', __TEMPLATE_ROOTAPP_AUTOWIRED__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_SERVICEPARAMS__', __TEMPLATE_ROOTAPP_SERVICEPARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_RESOLVERPARAMS__', __TEMPLATE_ROOTAPP_RESOLVERPARAMS__)
	return mkfile_template


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
