from schnell.app.printutils import (
	indah3
)
from schnell.app.stringutils import (
	list_stringify
)

from .common import (
	TAB,
	JAVA_MODEL_TEMPLATE,
	SBGQL_TEMPLATE,
)
from .generate_faker import generate_faker
from .utils import (
	get_tables_from_rootnode,
	process_each_table_from_rootnode,
)

field_map_java = {
	'string'						: 'String',
	'float'							: 'number',
	'array_of'					: '__SUBTYPE__[]',
}

field_map_gql = {
	'string'						: 'String',
	'float'							: 'number',
	'array_of'					: '[__SUBTYPE__]',
}

class SpringBootGQLOutput:


	def __init__(self, RootNode):
		self.root = RootNode


	def generate(self):
		gql_parts = self.generate_gql()
		separator = '\n' + '-' * 40 + '\n'
		java_parts = self.generate_java_model()
		java_object_instantiations = self.generate_java_objects()
		return gql_parts + separator + java_parts + separator + java_object_instantiations

	
	def generate_gql(self):
		gql_output = []
		for index, table in enumerate(self.root.children, 1):
			print(table.model)
			gql_table = SBGQL_TEMPLATE.replace('__TABLENAME', table.model)
			read_list = TAB+f'{table.model.lower()}List: [{table.model}]'
			read_detail = TAB+f'{table.model.lower()}Detail(id: String): {table.model}'
			read_opers = read_list + '\n' + read_detail			
			gql_table = gql_table.replace('__TABLE_READ_OPERATIONS', read_opers)
			gqlfields = []
			for field_no, field in enumerate(table.children, 1):
				column = f"{field.label}: {field_map_gql.get(field.type, field.type)}"				
				if hasattr(field, 'subtype'):
					column = column.replace('__SUBTYPE__', field_map_gql.get(field.subtype, field.subtype))
				print(column)
				gqlfields.append(column)
				
			# __TABLE_FIELDS_GQL
			str_gqlfields = list_stringify(gqlfields, sort=False, prefixer=TAB)
			gql_table = gql_table.replace('__TABLE_FIELDS_GQL', str_gqlfields)
			gql_output.append(gql_table)

		return list_stringify(gql_output, sort=False)


	def generate_java_objects(self):
		# generate_faker()
		# for index, table in enumerate(self.root.children, 1):
		# 	# print(table.model)
		# 	# java_table = JAVA_MODEL_TEMPLATE.replace('__TABLENAME', table.model)
		# 	# javafields = []
		# 	generate_object_instance = {}
		# 	for field_no, field in enumerate(table.children, 1):
		# 		generate_object_instance.update({
		# 			field.label = field_no
		# 		})

		all_tables = []
		tables = get_tables_from_rootnode(self.root)		
		for index, tbl in enumerate(tables, 1):
			
			if hasattr(tbl, 'faker'):

				generate_object_instance = {}
				for field_no, field in enumerate(tbl.children, 1):

					transformer = lambda x: f'"{x}"' if field.type=='string' else x
					if field.type == 'array_of':
						transformer = lambda a: str(a).replace('[', 'open', 1).replace(']', 'close', 1).replace('open', 'new String[] {').replace('close', '}').replace("'", '"')
					generate_object_instance.update({
						field.label: {
							'no': field_no,
							'transformer': transformer,
						}
					})

				records = []
				for angka in range(tbl.faker):
					kwargs = generate_faker(table=tbl, generate_object_instance=generate_object_instance)
					records.append(f"new {tbl.model} ({kwargs})")

				if records:
					stringified_records = ',\n'.join(records)
					all_tables.append(stringified_records)

		return '\n\n'.join(all_tables)

	def generate_java_model(self):
		java_output = []
		for index, table in enumerate(self.root.children, 1):
			print(table.model)
			java_table = JAVA_MODEL_TEMPLATE.replace('__TABLENAME', table.model)
			javafields = []
			for field_no, field in enumerate(table.children, 1):
				column = f"private {field_map_java.get(field.type, field.type)} {field.label};"				
				if hasattr(field, 'subtype'):
					column = column.replace('__SUBTYPE__', field_map_java.get(field.subtype, field.subtype))
				print(column)
				if hasattr(field, 'primaryKey'):
					javafields.append('@Id')
				javafields.append(column)

			# __TABLE_FIELDS_JAVA
			str_javafields = list_stringify(javafields, sort=False, prefixer=TAB)
			java_table = java_table.replace('__TABLE_FIELDS_JAVA', str_javafields)
			java_output.append(java_table)

		return list_stringify(java_output, sort=False)


def bantu_sbgql(RootNode):
	indah3('bantu_sbgql', warna='white')
	grpc = SpringBootGQLOutput(RootNode)
	return grpc.generate()
