
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
)
from .generate_table import generate_table


def generate_app_index(tables):
	for tableno, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		per_table = generate_table(tbl)
		print('*'*40)
		print(per_table)
		print('~'*40)
		# def append_entry(filepath_output, header, body):
		header = f'/{tablename_lower}.sql'
		entrify = append_entry(filepath_output,	header, per_table)


def gen_models(tables):
	generate_app_index(tables)
	# generate_app_routes(tables)
	# generate_app_model(tables)
	# generate_app_forms_resource(tables)
