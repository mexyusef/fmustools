from app.fileutils import file_content
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	tab as unused_tab,
	tab_real as tab, # gunakan \t di mkfile utk flyway
)
# from db.bantuan.common import tab
from .common import (
	filepath_input,
	filepath_output,
	# tpl_appindex,
	# tpl_appmodel,
	# tpl_appforms,
	# tpl_appresource,
	# tpl_appcontent,
)


def generate_server_app_content(tables, print_info=False):
	"""
	migrations,d(/mk)
		V1____TEMPLATE_TABLENAME.sql,f(e=__FILE__=__TEMPLATE_TABLENAME.sql)
	"""
	contentlines = []
	for tableno, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(tableno).zfill(2) # 01, 02, dst.
		tablename_lower = tbl.model.lower()                                                                   
		tablename_case = tbl.model
		# /todo.sql, /user.sql dll sbg baris entry di mk file stlh mk file digenerated
		baris = f'V{tableno}__{tablename_lower}.sql,f(e=__FILE__=/{tablename_lower}.sql)'
		contentlines.append(baris)

	template_app_content = '\n'.join([tab(2)+item for item in contentlines])
	if print_info:
		print('='*20, 'contentlines')
		print(template_app_content)

	return template_app_content


def gen_mkfile(RootNode, project_dir='input'):
	tables = get_tables(RootNode)

	print(f"generate from:", filepath_input)
	print(f"generate to:", filepath_output)
	print(f"tables:", [item.model for item in tables])

	mkfile_template = file_content(filepath_input) \
		.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', project_dir)

	template_db_init = gen_template_db_init(RootNode, use_real_tab=True)
	mkfile_template = mkfile_template.replace('__TEMPLATE_DB_INIT', template_db_init)

	template_app_init = gen_template_app_init(tables, use_real_tab=True)
	mkfile_template = mkfile_template.replace('__TEMPLATE_APP_INIT', template_app_init)

	server_app_content = generate_server_app_content(tables)
	mkfile_template = mkfile_template.replace('__TEMPLATE_SERVER_APP_CONTENT', server_app_content)

	write_mkfile(mkfile_template, filepath_output)
	return tables
