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
	tpl_appgraphql,
	tpl_appcontroller,
	tpl_appindex,
	tpl_appmodel,
	tpl_appservice,
	tpl_appcontent,
)


# /node-apollo-template/apps/__TEMPLATE_modelname/index.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.service.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.model.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.controller.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.graphql.js

def generate_app_index(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appindex)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)    

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/node-apollo-template/apps/{tablename_lower}/index.js'
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
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.service.js'
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
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.controller.js'
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
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.model.js'
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_graphql(tables):
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
		entrify = append_entry(filepath_output,	header, per_table)

def gen_models(tables):
	generate_app_index(tables)
	generate_app_service(tables)
	generate_app_controller(tables)
	generate_app_model(tables)
	generate_app_graphql(tables)
