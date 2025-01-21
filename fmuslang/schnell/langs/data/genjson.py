from jinja2 import Template

from helper import (
	get_stringtemplate,
)

def generate_json(tablename, records):

	stringtemplate = get_stringtemplate(tablename, records)
	
	template = Template(stringtemplate)
	hasil = template.render(users=records)
	# remove last comma
	lastcommaindex = hasil.rfind(',')
	clean_stringtemplate = hasil[:lastcommaindex] + hasil[lastcommaindex+1:]
	print('*' * 80)
	# print(clean_stringtemplate)
	return clean_stringtemplate
