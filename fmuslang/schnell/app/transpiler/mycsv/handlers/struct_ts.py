from schnell.app.stringutils import tabify_content_tab
from schnell.app.transpiler.mycsv.handlers.common import default_table_name
from schnell.app.libpohon.columnify import columnify, transform_table


form_interface = """interface __IFNAME {
__FIELDS
}"""

form_type = """type __IFNAME = {
__FIELDS
}"""

# type Person = {
# 	id: string,
# 	name: string,
# 	city: string
# };
# class Employee {
# 	public id: string;
# 	public name: string;
# 	private dept: string;
# 	public city: string;
# 	constructor(id: string, name: string, dept: string, city: string) {
# 		this.id = id;
# 		this.name = name;
# 		this.dept = dept;
# 		this.city = city;
# 	}
# 	writeDept() {
# 		console.log(`${this.name} works in ${this.dept}`);
# 	}
# }
# let salesEmployee = new Employee("fvega", "Fidel Vega", "Sales", "Paris");
# salesEmployee.writeDept();

def bentuk_interface(tablename_case, hasil):
	hasil = tabify_content_tab(hasil, num_tab=1)
	first = form_interface.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil)
	second = form_type.replace('__IFNAME', tablename_case).replace('__FIELDS', hasil)
	return first + '\n\n' + second

def struct_ts(tables):
	kembali = ''
	tablename_lower, tablename_case = '',''
	provider ='struct_ts'

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

	return kembali
