from app.fileutils import file_content
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	tab,
)
# from db.bantuan.common import tab
from .common import (
	filepath_input,
	filepath_output,
	# tpl_appgraphql,
	# tpl_appcontroller,
	tpl_appindex,
	tpl_appmodel,
	tpl_appforms,
	# tpl_apputil,
	tpl_appresource,
	tpl_appcontent,
)


def generate_server_app_content(tables, print_info=False):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model

		content = file_content(tpl_appcontent)
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


def assign_remaining_variables(tables, mkfile_template):
	"""
	utk remaining variables di mkfile yg perlu diassign.
	
	__TEMPLATE2_BLUEPRINTS_IMPORTS
	from project.apps import user
	__TEMPLATE2_BLUEPRINTS_REGISTER
	self.register_blueprint(user.blueprint)
	"""

	appimports = [tab(2) + f"from project.apps import {table.model.lower()}" for table in tables]
	__TEMPLATE2_BLUEPRINTS_IMPORTS = '\n'.join(appimports)
	apptypedefs = [tab(2) + f"self.register_blueprint({table.model.lower()}.blueprint)" for table in tables]
	__TEMPLATE2_BLUEPRINTS_REGISTER = '\n'.join(apptypedefs)
	# appresolvers = [f"{table.model.lower()}Resolver" for table in tables]
	# __TEMPLATE_APPS_RESOLVERS_LIST__ = ', '.join(appresolvers)

	mkfile_template = mkfile_template.replace('__TEMPLATE2_BLUEPRINTS_IMPORTS', __TEMPLATE2_BLUEPRINTS_IMPORTS)
	mkfile_template = mkfile_template.replace('__TEMPLATE2_BLUEPRINTS_REGISTER', __TEMPLATE2_BLUEPRINTS_REGISTER)
	# mkfile_template = mkfile_template.replace('__TEMPLATE_APPS_RESOLVERS_LIST__', __TEMPLATE_APPS_RESOLVERS_LIST__)
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

