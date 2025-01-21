langkah kerja

bantu ts
bantu flask
bantu django
bantu fastapi
bantu sequelize
bantu mongoose

bikin portfolio super cepat gunakan bantus
persiapkan bantu items = bantems utk test, dsb
lamar kerjaan
kerjakan sebanyak mungkin test, semua jadi bantems

template di sini...

from app.printutils import (
	indah3
)

from ..common import (
  TAB,
  nestjs_graphql_imports,
)

field_map = {
	'string'						: 'string',
	'float'							: 'number',
}

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







from app.printutils import (
	indah3
)

from ...common import (
  TAB,
  nestjs_graphql_imports,
)

field_map = {
	'string'						: 'string',
	'float'							: 'number',
}

class KategoriOutput:

	def __init__(self, RootNode):
		self.root = RootNode
		self.tablenames = []
    self.result_body = []
    self.result_header = []
    self.result_footer = []

	def generate(self):
		separator = '\n\n// ' + '*' * 40 + '\n'
		return 'OK'

	def generate_mkfile(self):
		for index, table in enumerate(self.root.children, 1):
      table_fields = []
			for field_no, field in enumerate(table.children, 1):
        pass
	def generate_models(self):
		for index, table in enumerate(self.root.children, 1):
      table_fields = []
			for field_no, field in enumerate(table.children, 1):
        pass

def bantu_nodereact(RootNode):
	indah3('bantu_nodereact', warna='white')
	generator = KategoriOutput(RootNode)
	return generator.generate()
