from anytree import RenderTree, AsciiStyle
from processor import process_language as processor_process_language
from generator.tosql import to_sql
from generator.tosqlalchemy import to_alchemy
from generator.tosequelize import tosequelize
from generator.tolaravel import to_laravel
from generator.todjango import to_django

def generate(RootNode, running_configuration):

	model = ''

	if not hasattr(RootNode, 'model'):
		RootNode.model = running_configuration['default_tablename']

	# default output = all
	if not RootNode.outputs:
		
		# print('masukkan sequelize')
		model += f"{'_'*40} sequelize"
		model += tosequelize(RootNode)
		
		# print('masukkan sql')
		model += f"{'_'*40} sql"
		model += to_sql(RootNode)

		# print('masukkan sqlalchemy')
		model += f"{'_'*40} sqlalchemy"
		model += to_alchemy(RootNode)

		# print('masukkan laravel')
		# model += f"{'_'*40} laravel"
		# model += to_laravel(RootNode)

		# print('masukkan django')
		model += f"{'_'*40} django"
		model += to_django(RootNode)
		# print('berhasil masukkan django')

	else:
		# if RootNode.output == 'sequelize':
		if 'sequelize' in RootNode.outputs:
			RootNode.output = 'sequelize'
			model += tosequelize(RootNode)
		# if RootNode.output == 'sql':
		if 'sql' in RootNode.outputs:
			RootNode.output = 'sql'
			model += to_sql(RootNode)
		# if RootNode.output == 'alchemy':
		if 'alchemy' in RootNode.outputs:
			RootNode.output = 'alchemy'
			model += to_alchemy(RootNode)
		# if RootNode.output == 'laravel':
		if 'laravel' in RootNode.outputs:
			RootNode.output = 'laravel'
			model += to_laravel(RootNode)
		# if RootNode.output == 'django':
		if 'django' in RootNode.outputs:
			RootNode.output = 'django'
			model += to_django(RootNode)

	print('*'*80)
	print(model) # utk hasil selalu tampil...


def process_language(running_configuration, debug, code):
  RootNode = processor_process_language(code, debug)

  debug(RenderTree(RootNode))

  generate(RootNode, running_configuration)
