from schnell.app.stringutils import tabify_content_tab, tabify_contentlist_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name
from schnell.app.libpohon.columnify import columnify, transform_table

form_interface = """public class __IFNAME {
__FIELDS

__CONSTRUCTOR

__GETTER

__SETTER
}

__INSTANCE"""

form_constructor = """public __IFNAME(__PARAMLIST) = {
__FIELDS
}"""

form_getter = """public __JENIS getCAPNAMA() {
	return ORIGNAMA;
}"""

form_setter = """public void setCAPNAMA(ORIGNAMA) {
	return this.ORIGNAMA = ORIGNAMA;
}"""

from schnell.app.fakerutils import get_by_datatypes, get_by_type_or_name
# get_by_datatypes(tipedata, callnum=1, funcargs=None, as_string=False, as_list=False, as_is=False, quote_string=False)
form_instances = """
__IFNAME __LOWER_IFNAME_inst = new __IFNAME(__OBJ_SIMPLE_PARAM);
"""

def bentuk_instance(tablename_case, hasil_columnify):
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']
	aslinya = dapatkan['columns_types_original']
	kembali = form_instances.replace('__IFNAME', tablename_case).replace('__LOWER_IFNAME', tablename_case.lower())
	# obj_formal_param = [f'{names[index]}: {get_by_datatypes(item,as_is=True,quote_string=True)}' for index, item in enumerate(jenis)]
	# obj_formal_param = ', '.join(obj_formal_param)

	# obj_simple_param = [f'{get_by_datatypes(item,as_is=True,quote_string=True)}' for index, item in enumerate(aslinya)]
	obj_simple_param = [f'{get_by_type_or_name(item,names[index],as_is=True,quote_string=True)}' for index, item in enumerate(aslinya)]
	obj_simple_param = ', '.join(obj_simple_param)

	# kembali = kembali.replace('__OBJ_FORMAL_PARAM', obj_formal_param)
	kembali = kembali.replace('__OBJ_SIMPLE_PARAM', obj_simple_param)
	return kembali

def bentuk_interface(tablename_case, hasil):
	hasil = tabify_content_tab(hasil, num_tab=1)
	first = form_interface.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil)
	# second = form_type.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil)
	# return first + '\n\n' + second
	return first

def bentuk_constructor(tablename_case, hasil_columnify):
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']

	delim = ';'
	res = [f'this.{names[index]} = {item}' for index, item in enumerate(jenis)]
	# res = [f'private final {item} {names[index]}' for index, item in enumerate(jenis)]	
	# res = sorted(res)

	hasil = f'{delim}\n'.join(res) + delim
	hasil = tabify_content_tab(hasil) # isi ctor
	
	paramlist = [f'{item} {names[index]}' for index, item in enumerate(jenis)]
	# paramlist = sorted(paramlist) # jangan disort dulu krn bikin gagal wkt bikin instance
	paramlist = f', '.join(paramlist)

	first = form_constructor.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil).replace('__PARAMLIST', paramlist)
	first = tabify_content_tab(first) # whole ctor
	return first

def bentuk_getter(tablename_case, hasil_columnify):
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']

	res = [form_getter.replace('__JENIS', item).replace('ORIGNAMA', names[index]).replace('CAPNAMA', names[index].capitalize()) for index, item in enumerate(jenis)]
	# res = sorted(res)
	hasil = f'\n'.join(res)
	hasil = tabify_content_tab(hasil)
	return hasil

def bentuk_setter(tablename_case, hasil_columnify):
	dapatkan = hasil_columnify[tablename_case]
	names = dapatkan['columns_names']
	jenis = dapatkan['columns_types']

	res = [form_setter.replace('__JENIS', item).replace('ORIGNAMA', names[index]).replace('CAPNAMA', names[index].capitalize()) for index, item in enumerate(jenis)]
	# res = sorted(res)
	hasil = f'\n'.join(res)
	hasil = tabify_content_tab(hasil)
	return hasil

def struct_java(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	provider ='struct_java'

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

		kembali = kembali.replace('__GETTER', bentuk_getter(tablename_case, hasil_columnify))
		kembali = kembali.replace('__SETTER', bentuk_setter(tablename_case, hasil_columnify))
		kembali = kembali.replace('__INSTANCE', bentuk_instance(tablename_case, hasil_columnify))

	return kembali
