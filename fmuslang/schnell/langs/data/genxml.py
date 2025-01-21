from jinja2 import Environment, FileSystemLoader, BaseLoader	

from helper import (
	myxml_template,
)

def generate_xml(tablename, records):
	first_row = records[0]
	# print(first_row.__dict__)
	# print(list(first_row.__dict__.keys()))
	# print(first_row.username)
	daftar_keys = list(first_row.__dict__.keys())
	entry_template = ''
	for key in daftar_keys:
		entry_template += f"<{key}>{{{{ user.{key} }}}}</{key}>\n"

	record_template = f"""<{tablename.title()} id="{{{{ loop.index }}}}">\n{entry_template}</{tablename.title()}>"""
	# print('\ntemplate step 1')
	# print(record_template)

	stringtemplate = myxml_template \
		.replace('__TABLENAMES', tablename.title()+'s') \
		.replace('__RECORD_TEMPLATE', record_template)

	template = Environment(loader=BaseLoader()).from_string(stringtemplate)
	hasil = template.render(users=records)
	print('*' * 80)
	# print(hasil)
	return hasil
