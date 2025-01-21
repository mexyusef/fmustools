from app.dirutils import (
  here, joiner
)
from app.fileutils import file_content

disini = here(__file__)
schema_import = joiner(disini, '../templates/replace_schema_import.tpl')
schema_fields = joiner(disini, '../templates/replace_schema_fields.tpl')


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
	# from .common import schema_fields, schema_import

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
