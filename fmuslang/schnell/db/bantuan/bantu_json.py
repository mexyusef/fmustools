import traceback
from jinja2 import Template


myjson_template = """[
		{% for record in records %}
__RECORD_TEMPLATE
		{% endfor %}
]
"""

record_template = f"""{{
__ENTRY_TEMPLATE__}},"""


def entry_template(records, appname, modelname):
	first_row = records[0]
	daftar_keys = list(first_row.__dict__.keys())

	# https://stackoverflow.com/questions/9005823/jinja-template-renders-double-quotes-or-single-quotes-as-39-34/9006024
	pairs = [f'"{col}": {{{{record.{col} | tojson}}}}' for col in daftar_keys]
	print('$pairs:', pairs, appname, modelname)
	
	per_entry_template = f""""model": "{appname}.{modelname}",
"pk": {{{{loop.index}}}},
"fields": {{
{',__NEWLINE'.join(pairs)}
}}\n""".replace('__NEWLINE', '\n')

	print('$pet:', per_entry_template)
	
	return record_template.replace('__ENTRY_TEMPLATE__', per_entry_template)


def get_stringtemplate(tablename, records):
	appname = tablename.lower()
	modelname = tablename
	print(f'\n\n*** appname = {appname}, modelname = {modelname}\n\n')
	stringtemplate = myjson_template \
		.replace('__TABLENAMES', tablename.title()+'s') \
		.replace('__RECORD_TEMPLATE', entry_template(records, appname, modelname))
	
	return stringtemplate


# def append_fixture_entry(tablename, body):
# 	"""
# 	buat entry fixture di django.mk
# 	"""
# 	start='--%'
# 	end='--#'
# 	header = f'/apps/{tablename}/__TEMPLATE_modelname.json'
# 	entry_fixture = f'\n{start} {header}\n' + body + f'\n{end}\n'
# 	append_file(filepath_output, entry_fixture)
# 	return entry_fixture


def gen_djangojsondata(tablename, records):
	"""
	bikin fixture entry %-- --# dan masukkan ke django.mk
	"""
	
	stringtemplate = get_stringtemplate(tablename, records)	
	template = Template(stringtemplate)

	try:
		hasil = template.render(records=records)
		koma = hasil.rfind(',')
		hasil = hasil[:koma] + hasil[koma+1:]
		print('='*40, 'generate JSON:')
		print(hasil)
		return hasil

	except Exception as err:
		print(f"Exception: {err} waktu process records: [{records[:5]}]")
		print(f"stringtemplate bermasalah adlh [{stringtemplate}]")
		print(traceback.format_exc())
		return None
