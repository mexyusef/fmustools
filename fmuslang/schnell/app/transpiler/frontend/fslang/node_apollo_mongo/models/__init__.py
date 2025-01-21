from app.fileutils import (
	file_content,
	append_entry_tostring,
)
from app.dirutils import here, joiner
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	append_entry,
)

disini = here(__file__)

tpl_appgraphql = joiner(disini, '../templates/nodeapollo_app_gql_template_v1.tpl')
tpl_appcontroller = joiner(disini, '../templates/nodeapollo_app_rest_controller_v1.tpl')
tpl_appindex = joiner(disini, '../templates/nodeapollo_app_rest_index_v1.tpl')
tpl_appmodel = joiner(disini, '../templates/nodeapollo_app_rest_model_v1.tpl')
tpl_appservice = joiner(disini, '../templates/nodeapollo_app_rest_service_v1.tpl')
tpl_appcontent = joiner(disini, '../templates/nodeapollo_app_content_v1.tpl')

# /node-apollo-template/apps/__TEMPLATE_modelname/index.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.service.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.model.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.controller.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.graphql.js


def generate_app_index(tables, mkfile_input_content):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appindex)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)    

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/node-apollo-template/apps/{tablename_lower}/index.js'
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
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.service.js'
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
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.controller.js'
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
		header = f'/node-apollo-template/apps/{tablename_lower}/{tablename_lower}.model.js'
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)

	# from app.libpohon.app_content import app_content
	# template_node_app_content = app_content(tables, tpl_appmodel)
	# mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content


def generate_app_graphql(tables, mkfile_input_content):
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
		# entrify = append_entry(filepath_output,	header, per_table)
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content


def gen_models(tables, mkfile_input_content):
	# generate_app_index(tables)
	# generate_app_service(tables)
	# generate_app_controller(tables)
	# generate_app_model(tables)
	# generate_app_graphql(tables)
	mkfile_input_content = generate_app_index(tables, mkfile_input_content)
	mkfile_input_content = generate_app_service(tables, mkfile_input_content)
	mkfile_input_content = generate_app_controller(tables, mkfile_input_content)
	mkfile_input_content = generate_app_model(tables, mkfile_input_content)
	mkfile_input_content = generate_app_graphql(tables, mkfile_input_content)

	return mkfile_input_content
