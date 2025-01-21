from schnell.app.stringutils import tabify_content
from schnell.app.transpiler.mycsv.handlers.common import default_table_name
from schnell.app.dirutils import joiner
from schnell.app.fileutils import file_content
from schnell.app.printutils import print_json
from schnell.app.libpohon.columnify import columnify, transform_columns
from schnell.app.libpohon.handlers import get_tipe_kolom
from .common import disini


controller = joiner(disini, 'templates/help_nest_mongo_controller.tpl')
service = joiner(disini, 'templates/help_nest_mongo_service.tpl')
modelfile = joiner(disini, 'templates/help_nest_mongo_model.tpl')
mainfile = joiner(disini, 'templates/help_nest_mongo_main.tpl')
appmodule = joiner(disini, 'templates/help_nest_mongo_appmodule.tpl')

if_updated_tpl = """if (__FIELD__) {
	updated__TEMPLATE_MODELNAME_CASE__.__FIELD__ = __FIELD__;
}
"""


def create_model(tables, tablename_lower, tablename_case):
	"""
	__TEMPLATE_MONGOSE_FIELDS__
	category: { type: String, required: false },
	checked: { type: Boolean, required: false, default: false },
	images: { type: Array, required: false, default: [] },
	inStock: { type: Number, required: true, default: 0 },
	"""
	modelcontent = file_content(modelfile)
	modelcontent = modelcontent.replace('__TEMPLATE_MODELNAME_CASE__', tablename_case)
	modelcontent = modelcontent.replace('__TEMPLATE_MODELNAME_LOWER__', tablename_lower)

	provider = 'nest_mongo' # lihat type_mapper_by_provider utk daftar
	hasil_columnify = columnify(tables, provider)
	print_json(hasil_columnify)
	hasil_transform = transform_columns(tablename_case, tables_with_columns=hasil_columnify, provider=provider)
	bagian_mongoose_schema = tabify_content(hasil_transform)

	provider = 'struct_ts'
	hasil_columnify = columnify(tables, provider)
	print_json(hasil_columnify)
	hasil_transform = transform_columns(tablename_case, tables_with_columns=hasil_columnify, provider=provider)
	bagian_mongoose_document = tabify_content(hasil_transform)

	modelcontent = modelcontent.replace('__TEMPLATE_MONGOSE_FIELDS__', bagian_mongoose_schema)
	modelcontent = modelcontent.replace('__TEMPLATE_TYPESCRIPT_FIELDS__', bagian_mongoose_document)
	return modelcontent


def create_controller(tablenamelower, tablenamecase, coltypes, colnotypes):
	controllercontent = file_content(controller)
	controllercontent = controllercontent.replace('__TEMPLATE_MODELNAME_CASE__', tablenamecase)
	controllercontent = controllercontent.replace('__TEMPLATE_MODELNAME_LOWER__', tablenamelower)

	bodified = [f"@Body('{colnotypes[idx]}') {namajenis}" for idx,namajenis in enumerate(coltypes)]
	bodified_separated = ',\n'.join(bodified)
	bodifiedtab2 = tabify_content(bodified_separated, num_tab=2)
	bodifiedtab3 = tabify_content(bodified_separated, num_tab=3)
	controllercontent = controllercontent.replace('__TAB2_TEMPLATE_BODIFIED__', bodifiedtab2)
	controllercontent = controllercontent.replace('__TAB3_TEMPLATE_BODIFIED__', bodifiedtab3)
	return controllercontent


def create_service(tablenamelower, tablenamecase, coltypes, colnotypes):
	"""
	__TAB2_TEMPLATE_UPDATED__
	__TAB2_TEMPLATE_PARAMS__
    category: string,
    checked: boolean,
    content: string,
    description: string,
    images: string[],
    inStock: number,
    price: number,
    sold: number,
    title: string
	__TAB2_TEMPLATE_ARGS__
		category,
		checked,
		content,
		description,
		images,
		inStock,
		price,
		sold,
		title
	perlu juga buat:
    @Body('category') category: string,
    @Body('checked') checked: boolean,
    @Body('content') content: string,
    @Body('description') description: string,
    @Body('images') images: [],
    @Body('inStock') inStock: number,
    @Body('price') price: number,
    @Body('sold') sold: number,
    @Body('title') title: string,
	"""
	servicecontent = file_content(service)
	servicecontent = servicecontent.replace('__TEMPLATE_MODELNAME_CASE__', tablenamecase)
	servicecontent = servicecontent.replace('__TEMPLATE_MODELNAME_LOWER__', tablenamelower)
	# _TAB3_COLUMNS
	field_and_types = ',\n'.join(coltypes)
	# tab1cols = tabify_content(field_and_types, num_tab=1)
	tab2cols = tabify_content(field_and_types, num_tab=2)
	tab3cols = tabify_content(field_and_types, num_tab=3)
	# servicecontent = servicecontent.replace('__TAB1_TEMPLATE_PARAMS__', tab1cols)
	servicecontent = servicecontent.replace('__TAB2_TEMPLATE_PARAMS__', tab2cols)
	servicecontent = servicecontent.replace('__TAB3_TEMPLATE_PARAMS__', tab3cols)

	bodified = [f"@Body('{colnotypes[idx]}') {namajenis}" for idx,namajenis in coltypes]
	bodified_separated = ',\n'.join(bodified)
	bodifiedtab2 = tabify_content(bodified_separated, num_tab=2)
	bodifiedtab3 = tabify_content(bodified_separated, num_tab=3)
	servicecontent = servicecontent.replace('__TAB2_TEMPLATE_BODIFIED__', bodifiedtab2)
	servicecontent = servicecontent.replace('__TAB3_TEMPLATE_BODIFIED__', bodifiedtab3)

	only_fields = ',\n'.join(colnotypes)
	# tab1cols = tabify_content(field_and_types, num_tab=1)
	tab2fields = tabify_content(only_fields, num_tab=2)
	tab3fields = tabify_content(only_fields, num_tab=3)
	servicecontent = servicecontent.replace('__TAB2_TEMPLATE_ARGS__', tab2fields)
	servicecontent = servicecontent.replace('__TAB3_TEMPLATE_ARGS__', tab3fields)

	# title: __TEMPLATE_MODELNAME_LOWER__.title,
	dict_style_attr = [f'{field}: {tablenamelower}.{field}' for field in colnotypes]
	dict_style_attr = ',\n'.join(dict_style_attr)
	# tab1dict = tabify_content(dict_style_attr, num_tab=1)
	tab2dict = tabify_content(dict_style_attr, num_tab=2)
	tab3dict = tabify_content(dict_style_attr, num_tab=3)
	servicecontent = servicecontent.replace('__TAB2_TEMPLATE_DICT__', tab2dict)
	servicecontent = servicecontent.replace('__TAB3_TEMPLATE_DICT__', tab3dict)

	if_updated = [if_updated_tpl.replace('__TEMPLATE_MODELNAME_CASE__',tablenamecase).replace('__FIELD__',field) for field in colnotypes]
	if_updated = '\n'.join(if_updated)
	# tab1updated = tabify_content(if_updated, num_tab=1)
	tab2updated = tabify_content(if_updated, num_tab=2)
	tab3updated = tabify_content(if_updated, num_tab=3)
	# servicecontent = servicecontent.replace('__TAB1_TEMPLATE_UPDATED__', tab1updated)
	servicecontent = servicecontent.replace('__TAB2_TEMPLATE_UPDATED__', tab2updated)
	servicecontent = servicecontent.replace('__TAB3_TEMPLATE_UPDATED__', tab3updated)
	return servicecontent

def help_nest_mongo(tables):
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
			# tipe_kolom = column.type
			tipe_kolom = get_tipe_kolom(column, 'struct_ts')
			nama_kolom = column.label
			item = f'{nama_kolom}: {tipe_kolom}'
			columns.append(item)
			colnotypes.append(nama_kolom)
			original_columns.append(column)

	fields = ', '.join(columns)
	# kembali += f'help_nest_mongo => {tablename_case}={tablename_lower} => {fields}'
	from .common import pemisah

	# kembali += pemisah.replace('__TITLE__', 'service:')
	# kembali += create_service(tablename_lower, tablename_case, columns, colnotypes)

	kembali += pemisah.replace('__TITLE__', 'controller:')
	kembali += create_controller(tablename_lower, tablename_case, columns, colnotypes)

	# kembali += pemisah.replace('__TITLE__', 'model:')
	# kembali += create_model(tables, tablename_lower, tablename_case)

	return kembali
