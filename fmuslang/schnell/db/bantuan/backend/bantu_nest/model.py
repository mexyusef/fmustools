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

def generate_app_module(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appmodule)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		# attendee.module.ts,f(e=utama=/nestjs/src/attendee/attendee.module.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.module.ts'
		entrify = append_entry(filepath_output,	header, per_table)

def generate_app_service(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appservice)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table2 = file_content(tpl_appservice_spec)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('-'*20)
		print(per_table2)
		print('~'*40)
		# attendee.service.ts,f(e=utama=/nestjs/src/attendee/attendee.service.ts)
		# attendee.service.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.service.spec.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.service.ts'
		entrify = append_entry(filepath_output,	header, per_table)
		header2 = f'/nestjs/src/{tablename_lower}/{tablename_lower}.service.spec.ts'
		entrify = append_entry(filepath_output,	header2, per_table2)

def generate_app_controller(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appcontroller)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table2 = file_content(tpl_appcontroller_spec)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('-'*20)
		print(per_table2)
		print('~'*40)
		# attendee.controller.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.ts)
		# attendee.controller.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.spec.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.controller.ts'
		entrify = append_entry(filepath_output,	header, per_table)
		header2 = f'/nestjs/src/{tablename_lower}/{tablename_lower}.controller.spec.ts'
		entrify = append_entry(filepath_output,	header2, per_table2)

def generate_app_resolver(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appresolver)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		
		per_table2 = file_content(tpl_appresolver_spec)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table2 = per_table2.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('-'*20)
		print(per_table2)
		print('~'*40)
		# attendee.resolver.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.ts)
		# attendee.resolver.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.spec.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.resolver.ts'
		entrify = append_entry(filepath_output,	header, per_table)
		header2 = f'/nestjs/src/{tablename_lower}/{tablename_lower}.resolver.spec.ts'
		entrify = append_entry(filepath_output,	header2, per_table2)

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
		# attendee.model.ts,f(e=utama=/nestjs/src/attendee/attendee.model.ts)
		header = f'/nestjs/src/{tablename_lower}/{tablename_lower}.model.ts'
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
	generate_app_module(tables)
	generate_app_model(tables)
	generate_app_service(tables)
	generate_app_controller(tables)
	generate_app_resolver(tables)
	# generate_app_graphql(tables)
