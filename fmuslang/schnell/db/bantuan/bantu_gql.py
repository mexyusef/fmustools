from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter
from anytree.search import find, findall

from schnell.app.dirutils import (
	joiner,
)
from schnell.app.fileutils import (
	file_content,
	append_file,
	copy_file,
)
from schnell.app.utils import (env_get)
from schnell.app.printutils import (print_copy)

from .common import (
	filepath_output, 
	node_pg_antd_template,
	node_sequelize_app_mk_template,
	react_antd_app_json_template,
	react_antd_app_mk_template,
)
from schnell.bantuan.common import tab

from schnell.creator.bindings import process_fmus, run_fmus
from .common import filepath_output
from .model import gen_models
from .mkfile import gen_mkfile


def gen_template_db_init(RootNode):
	# dbvalues = {}
	dblines = []
	dbinfo = RootNode
	if hasattr(dbinfo, 'username'):
		# dbvalues['username'] = dbinfo.username
		dblines.append(f"%__TEMPLATE_DBUSER={dbinfo.username}")

	if hasattr(dbinfo, 'password'):
		# dbvalues['password'] = dbinfo.password
		dblines.append(f"%__TEMPLATE_DBPASS={dbinfo.password}")

	if hasattr(dbinfo, 'host'):
		# dbvalues['host'] = dbinfo.host
		dblines.append(f"%__TEMPLATE_DBHOST={dbinfo.host}")
		
	if hasattr(dbinfo, 'port'):
		# dbvalues['port'] = dbinfo.port
		dblines.append(f"%__TEMPLATE_DBPORT={dbinfo.port}")

	if hasattr(dbinfo, 'dbname'):
		# dbvalues['dbname'] = dbinfo.dbname
		dblines.append(f"%__TEMPLATE_DBNAME={dbinfo.dbname}")

	# %__TEMPLATE_DBUSER=usef
	# %__TEMPLATE_DBPASS=rahasia
	# %__TEMPLATE_DBHOST=gisel.ddns.net
	# %__TEMPLATE_DBPORT=9022
	# %__TEMPLATE_DBNAME=ecomm
	template_db_init = '\n'.join([tab(1)+item for item in dblines])
	print('='*20, 'dblines')
	print(template_db_init)
	return template_db_init


def gen_template_app_init(tables):
	applines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model
		# perlu utk lower...ini akan jadi nama direktori utk masing2 app
		# %__TEMPLATE_APP01=task
		# %__TEMPLATE_APP02=user
		applines.append(f"%__TEMPLATE_APP{appidx}={tablename.lower()}")

	template_app_init = '\n'.join([tab(1)+item for item in applines])
	print('='*20, 'applines')
	print(template_app_init)
	return template_app_init


def generate_nodepg_app_content(tables):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model

		content = node_sequelize_app_mk_template
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
	print('='*20, 'contentlines')
	print(template_app_content)
	return template_app_content


def generate_reactantd_app_json(tables):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model

		content = react_antd_app_json_template
		content = content \
			.replace('__TAB(6)', tab(6)) \
			.replace('__TAB(5)', tab(5)) \
			.replace('__TAB(4)', tab(4)) \
			.replace('__TAB(3)', tab(3)) \
			.replace('__TAB(2)', tab(2)) \
			.replace('__TAB(1)', tab(1))
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
	print('='*20, 'contentlines')
	print(template_app_content)
	return template_app_content


def generate_reactantd_app_content(tables):
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model

		content = react_antd_app_mk_template
		content = content \
			.replace('__TAB(6)', tab(6)) \
			.replace('__TAB(5)', tab(5)) \
			.replace('__TAB(4)', tab(4)) \
			.replace('__TAB(3)', tab(3)) \
			.replace('__TAB(2)', tab(2)) \
			.replace('__TAB(1)', tab(1))
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
	print('='*20, 'contentlines')
	print(template_app_content)
	return template_app_content


def gen_mkfile(RootNode):
	print(RenderTree(RootNode))

	node_tables = lambda node: hasattr(node, 'name') and node.name == 'table' and node.type == 'table'
	tables = findall(RootNode, node_tables)

	print(f"generate from:", node_pg_antd_template)
	print(f"generate to:", filepath_output)
	print(f"tables:", [item.model for item in tables])

	replace_me = file_content(node_pg_antd_template)

	template_db_init = gen_template_db_init(RootNode)
	replace_me = replace_me.replace('__TEMPLATE_DB_INIT', template_db_init)

	template_app_init = gen_template_app_init(tables)
	replace_me = replace_me.replace('__TEMPLATE_APP_INIT', template_app_init)

	nodepg_app_content = generate_nodepg_app_content(tables)
	replace_me = replace_me.replace('__TEMPLATE_SERVER_APP_CONTENT', nodepg_app_content)

	reactantd_app_json = generate_reactantd_app_json(tables)
	replace_me = replace_me.replace('__TEMPLATE_CLIENT_JSON_MODEL', reactantd_app_json)

	reactantd_app_content = generate_reactantd_app_content(tables)
	replace_me = replace_me.replace('__TEMPLATE_CLIENT_APP_CONTENT', reactantd_app_content)

	with open(filepath_output, 'w') as fd:
		fd.write(replace_me)

	configuration = {
		'table_nodes': tables,
		'root_node': RootNode,
	}
	return configuration


def generate_pg_antd(RootNode):
	configuration = gen_mkfile(RootNode)
	gen_models(configuration)
	if env_int('exec_fmus'):
		yesno = input('Lanjut execute buat backend? ')
		if yesno == 'y':
			run_fmus(filepath_output, 'program/fm.us')
