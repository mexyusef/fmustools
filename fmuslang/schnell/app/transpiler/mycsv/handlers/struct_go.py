from schnell.app.stringutils import tabify_content_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name
from schnell.app.libpohon.columnify import columnify, transform_table

from schnell.app.typemapper import type_mapper_by_provider

form_constructor = """func new__CAPIFNAME(__PARAMLIST) *__IFNAME {
	o := __IFNAME{__PARAMASSIGN}
	return &o
}"""

form_type = """type __IFNAME struct {
__FIELDS
}

__CONSTRUCTOR


__INSTANCE"""

from schnell.app.fakerutils import get_by_datatypes
# get_by_datatypes(tipedata, callnum=1, funcargs=None, as_string=False, as_list=False, as_is=False, quote_string=False)
form_instances = """// obj formal
// o := person{name: "Sean", age: 50}
o := __IFNAME{__OBJ_FORMAL_PARAM}

// obj simple
// o := person{"Sean", 50}
o := __IFNAME{__OBJ_SIMPLE_PARAM}

// pointer raw
// p := &person{"Sean", 50}
p := &__IFNAME{__OBJ_FORMAL_PARAM}

// pointer by ctor
// p := newPerson{"Sean", 50}
p := __IFNAME{__OBJ_SIMPLE_PARAM}"""

provider ='struct_go'

def bentuk_instance(tablename_case, hasil_columnify):
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']
	kembali = form_instances.replace('__IFNAME', tablename_case)
	obj_formal_param = [f'{names[index]}: {get_by_datatypes(item,as_is=True,quote_string=True)}' for index, item in enumerate(jenis)]
	obj_formal_param = ', '.join(obj_formal_param)

	obj_simple_param = [f'{get_by_datatypes(item,as_is=True,quote_string=True)}' for index, item in enumerate(jenis)]
	obj_simple_param = ', '.join(obj_simple_param)

	kembali = kembali.replace('__OBJ_FORMAL_PARAM', obj_formal_param)
	kembali = kembali.replace('__OBJ_SIMPLE_PARAM', obj_simple_param)
	return kembali


def bentuk_interface(tablename_case, hasil):
	hasil = tabify_content_tab(hasil, num_tab=1)
	# first = form_interface.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil)
	second = form_type.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil)
	# return first + '\n\n' + second
	return second


def bentuk_constructor(tablename_case, hasil_columnify):
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']
	aslinya = dapatkan['columns_types_original']

	paramlist = [f'{names[index]} {type_mapper_by_provider[provider][item]}' for index, item in enumerate(aslinya)]
	# paramlist = sorted(paramlist)
	paramlist = f', '.join(paramlist)

	paramassign = [f'{names[index]}: {names[index]}' for index, item in enumerate(aslinya)]
	# paramassign = sorted(paramassign)
	paramassign = f', '.join(paramassign)

	first = form_constructor \
		.replace('__IFNAME', tablename_case) \
		.replace('__CAPIFNAME', tablename_case.capitalize()) \
		.replace('__PARAMLIST', paramlist) \
		.replace('__PARAMASSIGN', paramassign)
	# first = tabify_content_tab(first) # whole ctor
	return first


def struct_go(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''	

	for _, tbl in enumerate(tables,1):
		if not hasattr(tbl, 'model'):
			print(f'table: tidak berisi model, please specify {{@NamaTabel}}. menggunakan default tablename = "{default_table_name}"')
			setattr(tbl, 'model', default_table_name)
		# tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		hasil_columnify = columnify(tables, provider, skip_columns={})
		hasil = transform_table(tablename_case, hasil_columnify, provider)
		# kembali += f'struct_ts => {tablename_case}={tablename_lower} => {fields}'
		kembali += bentuk_interface(tablename_case, hasil)
		kembali = kembali.replace('__CONSTRUCTOR', bentuk_constructor(tablename_case, hasil_columnify))
		kembali = kembali.replace('__INSTANCE', bentuk_instance(tablename_case, hasil_columnify))

	return kembali
