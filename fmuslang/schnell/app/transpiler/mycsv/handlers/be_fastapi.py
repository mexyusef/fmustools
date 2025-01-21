from schnell.app.stringutils import tabify_content, tabify_content_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name
from schnell.app.libpohon.columnify import columnify, transform_columns
from schnell.app.libpohon.handlers import get_tipe_kolom
from schnell.app.dirutils import joiner
from schnell.app.fileutils import file_content
from schnell.app.printutils import print_json
from schnell.app.libpohon.helper import detect_replace_assignment
from schnell.app.treeutils import (
    assignment_paramlist_type,
    ASSIGNMENT_PARAMLIST_PREFIX,
    ASSIGNMENT_PARAMLIST_COMMA,
    ASSIGNMENT_PARAMLIST_NEWLINE0,
    ASSIGNMENT_PARAMLIST_NEWLINE1,

    assignment_firstcolumn,
    assignment_paramlist,
    assignment_paramlist_value,
    assignment_pydict_all,
    assignment_pydict_first,
    assignment_pydict_rest,
    ASSIGNMENT_FIRSTCOLUMN,
    ASSIGNMENT_PARAMLIST_SIMPLE,
    ASSIGNMENT_PARAMLIST_VALUE,
    ASSIGNMENT_PYDICT_ALL,
    ASSIGNMENT_PYDICT_FIRST,
    ASSIGNMENT_PYDICT_REST,
)
from schnell.app.appconfig import libpohon_data
from .common import disini, pemisah

modelfile = joiner(disini, 'templates/django_orm_mongo_model.tpl')

def create_model(tables, tablename_lower, tablename_case, provider):
	"""
	__IMPORTS__
	__FIELDS__
	__COLNAME__
	"""
	modelcontent = file_content(modelfile)
	modelcontent = modelcontent.replace('__TEMPLATE_MODELNAME_CASE__', tablename_case)
	modelcontent = modelcontent.replace('__TEMPLATE_MODELNAME_LOWER__', tablename_lower)

	# provider = 'django' # lihat type_mapper_by_provider utk daftar
	hasil_columnify = columnify(tables, provider)
	print_json(hasil_columnify)
	hasil_transform = transform_columns(tablename_case, tables_with_columns=hasil_columnify, provider=provider)
	bagian_django_model = tabify_content_tab(hasil_transform)
	# print('bagian_django_model:', bagian_django_model)

	modelcontent = modelcontent.replace('__TEMPLATE_MODEL_FIELDS__', bagian_django_model)
	import_part = '\n'.join(libpohon_data['import_part'])
	modelcontent = modelcontent.replace('__IMPORTS__', import_part)
	
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	first_column = names[0]
	# jenis = dapatkan['columns_types']
	# attrs = dapatkan['columns_attributes']
	modelcontent = modelcontent.replace('__COLNAME__', first_column)
	# utk paramlist etc dari app.treeutils
	# for TableNode in tables:
	# 	modelcontent = detect_replace_assignment(modelcontent, TableNode, pemetaan=provider)
	return modelcontent


def be_fastapi(tables, provider='fastapi'):
	"""
	ini ternyata baru handle 1 model
	"""
	kembali = ''
	tablename_lower, tablename_case = '',''
	original_columns = []
	columns = []
	colnotypes = []
	for tblidx, tbl in enumerate(tables,1):
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		for colidx, column in enumerate(tbl.children):
			# tipe_kolom = type_mapperper.get(column.type, column.type)
			tipe_kolom = get_tipe_kolom(column, 'django_orm')
			nama_kolom = column.label
			item = f'{nama_kolom}: {tipe_kolom}'
			columns.append(item)
			colnotypes.append(nama_kolom)
			original_columns.append(column)

	fields = ', '.join(columns)
	kembali += f'{provider} => {tablename_case}={tablename_lower} => {fields}'

	kembali += pemisah.replace('__TITLE__', 'model:')
	kembali += create_model(tables, tablename_lower, tablename_case, provider=provider)


	return kembali
