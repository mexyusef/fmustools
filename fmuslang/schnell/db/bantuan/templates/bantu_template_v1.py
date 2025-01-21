from app.printutils import (
	indah3
)
from db.bantuan.common import (
  tab,
)

"""
**.,d
	mkfile.py,f(t=)
	model.py,f(t=)
	common.py,f(t=)
	field_map.py,f(t=)
"""
# mkfile.mk
##########
# model.mk
##########
# common.py
###########
from app.dirutils import (
  here, joiner
)
from db.bantuan.config import output_folder
disini = here(__file__)

filename_input = 'node-whatever'
filename_input_ext = f'{filename_input}.mk'
filepath_input = joiner(disini, filename_input_ext)

filepath_output = joiner(output_folder, f'{filename_input}-output.mk')
# field_map.py
##############
field_map = {
	'string'						: 'string',
	'float'							: 'number',
}
# local_templates.py
####################
from .common import filepath_output, filepath_input
from .field_map import field_map

class KategoriOutput:

	def __init__(self, RootNode):
		self.root = RootNode
		self.tablenames = []
    self.result_body = []
    self.result_header = []
    self.result_footer = []

	def generate(self):
		separator = '\n\n// ' + '*' * 40 + '\n'
		return self.generate_header() + \
    separator + \
    self.generate_body() + \
    separator + \
    self.generate_footer()

	def generate_body(self):

		for index, table in enumerate(self.root.children, 1):
			
      table_fields = []

			for field_no, field in enumerate(table.children, 1):
				
        column = f"{field.label}: {entity_field_map.get(field.type, field.type)};\n"

				if hasattr(field, 'subtype'):
          pass
				if hasattr(field, 'allowNull'):
					pass
        if hasattr(field, 'defaultValue'):
          pass
        if hasattr(field, 'primaryKey'):
          pass

        table_fields.append(column)

      stringified_fields = '\n'.join([TAB+item for item in table_fields])

      nama_table = table.model.lower()
			nama_entity = f"{table.model}Entity"
      result_per_table = f"\n@Entity('{nama_table}')\nexport class {nama_entity} {{\n\n"
			result_per_table += stringified_fields
			result_per_table += '\n}'

			self.result_body.append(result_per_table)


def bantu_kategori(RootNode):
	indah3('bantu_kategori', warna='white')
	generator = KategoriOutput(RootNode)
	return generator.generate()
