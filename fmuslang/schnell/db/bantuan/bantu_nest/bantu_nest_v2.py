
from app.printutils import (
	indah3
)

from ..common import (
	TAB,
	tab,
	# nestjs_graphql_imports,
)

from .config import (
	template_appmodule,
	template_module,
	field_map,
	template_service,
	template_controller,
	template_rest,
	template_resolver,
	template_gql,
)


class KategoriOutput:

	def __init__(self, RootNode):
		self.root = RootNode

		self.result_appmodule = ''
		self.result_module = []
		self.result_service = []
		self.result_controller = []
		self.result_rest_support = []
		self.result_resolver = []
		self.result_gql_support = []
		
		self.pre_generate()

	def pre_generate(self):
		self.generate_appmodule()
		self.generate_module()
		self.generate_service()
		self.generate_controller()
		self.generate_rest_support()
		self.generate_resolver()
		self.generate_gql_support()

	def generate(self):
		separator = '\n\n// ' + '*' * 40 + '\n'
		service_separator = '// ' + '-'*40

		appmodule_info 			= '// ' + '-'*40 + f" nestjs app module"
		module_info 			= '// ' + '-'*40 + f" nestjs module"
		service_info 			= '// ' + '-'*40 + f" nestjs services"
		controller_info 	= '// ' + '-'*40 + f" nestjs controller"
		rest_support_info = '// ' + '-'*40 + f" nestjs REST support"
		resolver_info 	= '// ' + '-'*40 + f" nestjs resolver"
		gql_support_info = '// ' + '-'*40 + f" nestjs GQL support"
		

		total = '// *** NEST JS *** ' + '\n'
		total += appmodule_info + '\n'
		total += self.result_appmodule + '\n'

		total += module_info + '\n'
		total += service_separator.join(self.result_module)
		total += service_info + '\n'
		total += service_separator.join(self.result_service)
		total += controller_info + '\n'
		total += service_separator.join(self.result_controller)
		total += rest_support_info + '\n'
		total += service_separator.join(self.result_rest_support)

		total += resolver_info + '\n'
		total += service_separator.join(self.result_resolver)
		total += gql_support_info + '\n'
		total += service_separator.join(self.result_gql_support)

		return total


	def generate_appmodule(self):

		combined_result = ''
		import_modules = []
		import_entities = []
		use_modules = []
		use_entities = []

		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			import_modules.append(f"import {{ {model_case}Module }} from './{model_lower}/{model_lower}.module';")
			import_entities.append(f"import {{ {model_case}Entity }} from './{model_lower}/{model_lower}.entity';")
			use_modules.append(f"{model_case}Module")
			use_entities.append(f"{model_case}Entity")


		__TEMPLATE_IMPORT_MODULE_ALL_TABLES__ = '\n'.join(import_modules)
		__TEMPLATE_IMPORT_ENTITY_ALL_TABLES__ = '\n'.join(import_entities)
		# indent seperlunya
		__TEMPLATE_ALL_ENTITIES__ = tab(4) + ', '.join(use_entities)
		__TEMPLATE_ALL_MODULES__ = tab(2) + ', '.join(use_modules)
		self.result_appmodule = template_appmodule \
			.replace('__TEMPLATE_IMPORT_MODULE_ALL_TABLES__', __TEMPLATE_IMPORT_MODULE_ALL_TABLES__) \
			.replace('__TEMPLATE_IMPORT_ENTITY_ALL_TABLES__', __TEMPLATE_IMPORT_ENTITY_ALL_TABLES__) \
			.replace('__TEMPLATE_ALL_ENTITIES__', __TEMPLATE_ALL_ENTITIES__) \
			.replace('__TEMPLATE_ALL_MODULES__', __TEMPLATE_ALL_MODULES__)

	def generate_module(self):
		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			result_per_table = template_module \
				.replace('__TEMPLATE_MODELNAME_CASE__', model_case) \
				.replace('__TEMPLATE_MODELNAME_LOWER__', model_lower)

			self.result_module.append(result_per_table)

	def generate_service(self):

		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			result_per_table = template_service \
				.replace('__TEMPLATE_MODELNAME_CASE__', model_case) \
				.replace('__TEMPLATE_MODELNAME_LOWER__', model_lower)

			self.result_service.append(result_per_table)

	def generate_controller(self):

		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			result_per_table = template_controller \
				.replace('__TEMPLATE_MODELNAME_CASE__', model_case) \
				.replace('__TEMPLATE_MODELNAME_LOWER__', model_lower)

			self.result_controller.append(result_per_table)

	def generate_rest_support(self):

		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			result_per_table = template_rest \
				.replace('__TEMPLATE_MODELNAME_CASE__', model_case) \
				.replace('__TEMPLATE_MODELNAME_LOWER__', model_lower)

			self.result_rest_support.append(result_per_table)

	def generate_resolver(self):

		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			result_per_table = template_resolver \
				.replace('__TEMPLATE_MODELNAME_CASE__', model_case) \
				.replace('__TEMPLATE_MODELNAME_LOWER__', model_lower)

			self.result_resolver.append(result_per_table)

	def generate_gql_support(self):

		for index, table in enumerate(self.root.children, 1):
			
			model_case = table.model
			model_lower = table.model.lower()
			result_per_table = template_gql \
				.replace('__TEMPLATE_MODELNAME_CASE__', model_case) \
				.replace('__TEMPLATE_MODELNAME_LOWER__', model_lower)

			self.result_gql_support.append(result_per_table)


def bantu_nest(RootNode):
	indah3('bantu_nest', warna='white')
	generator = KategoriOutput(RootNode)
	return generator.generate()

