from schnell.app.fileutils import file_content
from schnell.app.treeutils import get_tables
from schnell.app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	tab,
)
from .common import (
	filepath_input,
	filepath_output,
	# tpl_appgraphql,
	tpl_appcontroller,
	tpl_appindex,
	tpl_appmodel,
	tpl_appservice,
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
	from apps.product import routes as product_router
	__TEMPLATE_APP_ROUTE_IMPORTS

	api_router.include_router(product_router.router, prefix='/products', tags=['products'])
	__TEMPLATE_APP_ROUTE_LIST

	# from apps.book.models import Book
__TEMPLATE_ALEMBIC_FIRSTAPP_IMPORT
__TEMPLATE_ALEMBIC_FIRSTAPP_NAME
	"""
	from .common import schema_fields, schema_import

	__TEMPLATE_PER_APP_SCHEMA_IMPORTS__ = '\n'.join([file_content(schema_import).replace('__TEMPLATE_TABLENAME_LOWER__', meja.model.lower()).replace('__TEMPLATE_TABLENAME_CASE__', meja.model) for meja in tables])
	__TEMPLATE_PER_APP_QUERY_PARAMS__ = ', '.join([f"Hello{meja.model}, List{meja.model}, Detail{meja.model}" for meja in tables])
	__TEMPLATE_PER_APP_MUTATION_FIELDS__ = '\n'.join([file_content(schema_fields).replace('__TEMPLATE_TABLENAME_LOWER__', meja.model.lower()).replace('__TEMPLATE_TABLENAME_CASE__', meja.model) for meja in tables])

	appimports = [f"from apps.{table.model.lower()} import routes as {table.model.lower()}_router" for table in tables]
	__TEMPLATE_APP_ROUTE_IMPORTS = '\n'.join(appimports)
	apptypedefs = [f"api_router.include_router({table.model.lower()}_router.router, prefix='/{table.model.lower()}s', tags=['{table.model.lower()}s'])" for table in tables]
	__TEMPLATE_APP_ROUTE_LIST = ', '.join(apptypedefs)
	first_table = tables[0].model
	__TEMPLATE_ALEMBIC_FIRSTAPP_NAME = first_table
	__TEMPLATE_ALEMBIC_FIRSTAPP_IMPORT = f"from apps.{first_table.lower()}.models import {first_table}"

	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_ROUTE_IMPORTS', __TEMPLATE_APP_ROUTE_IMPORTS)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_ROUTE_LIST', __TEMPLATE_APP_ROUTE_LIST)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ALEMBIC_FIRSTAPP_NAME', __TEMPLATE_ALEMBIC_FIRSTAPP_NAME)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ALEMBIC_FIRSTAPP_IMPORT', __TEMPLATE_ALEMBIC_FIRSTAPP_IMPORT)

	mkfile_template = mkfile_template.replace('__TEMPLATE_PER_APP_SCHEMA_IMPORTS__', __TEMPLATE_PER_APP_SCHEMA_IMPORTS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_PER_APP_QUERY_PARAMS__', __TEMPLATE_PER_APP_QUERY_PARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_PER_APP_MUTATION_FIELDS__', __TEMPLATE_PER_APP_MUTATION_FIELDS__)
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

