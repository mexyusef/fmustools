TAB = ' ' * 4
TABS = TAB * 3

config_json_template = """
{
  "development": {
	"username": "usef",
	"password": "rahasia",
	"database": "sementara",
	"host": "localhost",
	"dialect": "postgres",
	"port": 9999
  }
}
"""

seeder_filename_template = """
module.exports = {
  up: (queryInterface, Sequelize) => {
	return queryInterface.bulkInsert('_TABLENAMES', 
__RECORDS
	);
  },
  down: (queryInterface, Sequelize) => {
	return queryInterface.bulkDelete('_TABLENAMES', null, {});
  }
};
"""

myjson_template = """{
	"__TABLENAMES": {
		{% for user in users %}
__RECORD_TEMPLATE
		{% endfor %}
	}
}
"""

myxml_template = """<?xml version="1.0" encoding="UTF-8"?>
<__TABLENAMES>
    {% for user in users %}

__RECORD_TEMPLATE

    {% endfor %}
</__TABLENAMES>
"""

record_template = f"""{TABS}"{{{{ loop.index }}}}": {{
__ENTRY_TEMPLATE__
{TABS}}},"""

def entry_template(records):
  first_row = records[0]
  daftar_keys = list(first_row.__dict__.keys())

  entry_template = ",\n".join(
    [f'''{TABS}"{key}": "{{{{ user.{key} }}}}"''' \
      for key in daftar_keys]
  )
  # return entry_template
  return record_template.replace('__ENTRY_TEMPLATE__', entry_template)

# def get_record_template_value(records):
#   return record_template.replace('__ENTRY_TEMPLATE__', entry_template(records))

def get_stringtemplate(tablename, records):
  record_template = entry_template(records)

  stringtemplate = myjson_template \
    .replace('__TABLENAMES', tablename.title()+'s') \
    .replace('__RECORD_TEMPLATE', record_template)

  return stringtemplate
