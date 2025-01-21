from anytree import (
	AnyNode,
	AsciiStyle,
	PreOrderIter,
	RenderTree,
)
from record import Record

# generated_columns sblm dibersihkan: ['email:varchar#email', 'password:string#password', 'mypass:bcrypt#rahasia', 'nilai:number#random_int']
# columnnames ['email', 'password', 'mypass', 'nilai']
# columntypes ['varchar#email', 'string#password', 'bcrypt#rahasia', 'number#random_int']
# tablename User
# tablenconfigurationame {'generate:number': 1, 'generate:table': 'User', 'columns': {'username': 'varchar', 'name': 'string', 'email': 'varchar', 'password': 'string', 'mypass': 'bcrypt', 'nilai': 'number'}}
def generate(generated_tree):
	tablename = None
	generated_columns = []
	configuration = None

	for item in PreOrderIter(generated_tree):

		if item.type == 'table':
			tablename = item.value

		elif item.type == 'config':
			configuration = item.value

		elif item.type == 'column':
			# ini spt, username:string
			# dari cmdargs.update({ 'name' : nama_kolom, 'value': jenis_kolom })
			item_value = f'{item.name}:{item.value}'

			# jk ada value, number, dan subclass maka bentuknya jadi: value#subclass,number
			# tujuannya, string punya subclass: telepon #, email, username, password, dst.
			# number di sini adlh modifier utk name,s(100) <- 100=number
			# contoh:
			# email:s(100):e	-> name:value(number):subclasstype
			#					menjadi -> name:value#subclasstype,number
			#         atau    -> email:varchar#email,100			
			# email:s:e 			-> katakunci:varchar#password
			if hasattr(item, 'subclasstype'):
				item_value = f'{item.name}:{item.value}#{item.subclasstype},{item.number}' \
					if hasattr(item, 'number') \
					else f'{item.name}:{item.value}#{item.subclasstype}'

			# jk ada value, number maka bentuknya jadi: value,number
			if hasattr(item, 'number'):
				item_value = f'{item.name}:{item.value}#{item.subclasstype},{item.number}' \
					if hasattr(item, 'subclasstype') \
					else f'{item.name}:{item.value},{item.number}'

			generated_columns.append(item_value)

	print(f'generated_columns sblm dibersihkan: {generated_columns}')
	columnnames = list( map(lambda item: item.split(':')[0], generated_columns) )
	columntypes = list( map(lambda item: item.split(':')[1], generated_columns) )
	print('columnnames', columnnames)
	print('columntypes', columntypes)
	print('tablename', tablename)
	print('tablenconfigurationame', configuration)
	print('='*80)
	return configuration, tablename, columntypes, columnnames
