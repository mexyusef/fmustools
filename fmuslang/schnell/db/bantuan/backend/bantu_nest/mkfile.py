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
	
	tpl_appmodule,
	tpl_appmodel,
	tpl_appresolver,
	tpl_appresolver_spec,
	tpl_appcontroller,
	tpl_appcontroller_spec,
	tpl_appservice,
	tpl_appservice_spec,
	
	tpl_appcontent,
)


def generate_server_app_content(tables, print_info=False):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model
		tablename_lower = tbl.model.lower()

		content = file_content(tpl_appcontent)
		content = content.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		content = content.replace('__TEMPLATE_TABLENAME_CASE__', tablename)
		content = content \
			.replace('__TAB(6)', tab(6)) \
			.replace('__TAB(5)', tab(5)) \
			.replace('__TAB(4)', tab(4)) \
			.replace('__TAB(3)', tab(3)) \
			.replace('__TAB(2)', tab(2)) \
			.replace('__TAB(1)', tab(1))
		content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
		content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
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


template_rootapp_import_perapp = """
import { __tablename_caseModule } from './__tablename_lower/__tablename_lower.module';
import { __tablename_caseEntity } from './__tablename_lower/__tablename_lower.model';
"""

def assign_remaining_variables(tables, mkfile_template):
	"""
	import { AttendeeModule } from './attendee/attendee.module';
	import { AttendeeEntity } from './attendee/attendee.model';
	AttendeeEntity,
	AttendeeModule
	"""

	__TEMPLATE_ROOTAPP_IMPORTS_LIST__ = [template_rootapp_import_perapp.replace('__tablename_lower', table.model.lower()).replace('__tablename_case', table.model) for table in tables]
	__TEMPLATE_ROOTAPP_IMPORTS__ = '\n'.join(__TEMPLATE_ROOTAPP_IMPORTS_LIST__)

	__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_ = [f'{table.model}Entity' for table in tables]
	__TEMPLATE_ROOTAPP_SERVICEPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_)

	__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_ = [f'{table.model}Module' for table in tables]
	__TEMPLATE_ROOTAPP_RESOLVERPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_)

	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_IMPORTS__', __TEMPLATE_ROOTAPP_IMPORTS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_ENTITYPARAMS__', __TEMPLATE_ROOTAPP_SERVICEPARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_MODULEPARAMS__', __TEMPLATE_ROOTAPP_RESOLVERPARAMS__)
	return mkfile_template


def gen_mkfile(RootNode, project_dir='input'):
	tables = get_tables(RootNode)

	print(f"generate from:", filepath_input)
	print(f"generate to:", filepath_output)
	print(f"tables:", [item.model for item in tables])

	# mkfile_template = file_content(filepath_input)
	mkfile_template = file_content(filepath_input) \
		.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', project_dir)

	template_db_init = gen_template_db_init(RootNode)
	mkfile_template = mkfile_template.replace('__TEMPLATE_DB_INIT', template_db_init)

	template_app_init = gen_template_app_init(tables)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_INIT', template_app_init)

	server_app_content = generate_server_app_content(tables)
	mkfile_template = mkfile_template.replace('__TEMPLATE_SERVER_APP_CONTENT', server_app_content)

	mkfile_template = assign_remaining_variables(tables, mkfile_template)

	write_mkfile(mkfile_template, filepath_output)

	return tables

