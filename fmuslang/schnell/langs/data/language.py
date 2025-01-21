

from anytree import (
	AnyNode,
	AsciiStyle,
	PreOrderIter,
	RenderTree,
)
import lark
from lark import (
	Lark, 
	InlineTransformer, 
	Transformer,

	inline_args,
	v_args
)

from grammar import data_grammar
from processor import (
	tree_to_anytree,
	TheProcessor,
)


def process_language(stringified):
	parser = Lark(data_grammar, start='keseluruhan').parse
	parsed_tree = parser(stringified)
	transformer = TheProcessor()  
	transformed_tree = transformer.transform(parsed_tree)
	print('\nprocess_language pretty AST =', transformed_tree.pretty())

	config = {}
	pohon = AnyNode(name='root', type='root', value='generate')

	for ayah in transformed_tree.children:

		for anak in ayah.children:
			cmdargs = {
				'parent'			: pohon,
			}

			if anak.data == 'datanumber':
				jumlah = str(anak.children[0])
				config['generate:number'] = int(jumlah)

			elif anak.data == 'tablename':
				tablename = str(anak.children[0])
				config['generate:table'] = tablename
				config['columns'] = {}
				cabang = AnyNode(name='table', type='table', value=tablename, parent=pohon)

			elif anak.data == 'column':
				'''
				coltype ada 4 variasi
					columntype
						varchar 100
					columntype
						string

					columntype
						string
						email
					columntype
						varchar 100
						email

				contoh anak coltype:

				username:s(100)
				1 anak Tree dg 1 cucu = Token
				[Tree('varchar', [Token('BILBUL', '100')])]

				name:s
				1 anak Tree tanpa cucu
				[Tree('string', [])]
				
				email:s(100):e
				punya 2 anak Tree
				[
					Tree('varchar', [Token('BILBUL', '100')]), 
					Tree('email', [])
				]

				password:s
				punya 2 anak Tree
				[
					Tree('string', []), 
					Tree('password', [])
				]

				'''
				colname = anak.children[0]
				colnameval = str(colname.children[0])
				coltype = anak.children[1]
				coltype_childnum = len(coltype.children)
				cmdargs.update({ 'type' : 'column', })				
				# print('type:', coltype.data, coltype, '\nname:', colname.data, colname, '\n\n')
				# name: columnname Tree('columnname', [Token('HURUF', 'password')])
				colname_token = colname.children[0]
				nama_kolom = str(colname_token)
				coltype_data = coltype.children[0]
				jenis_kolom = str(coltype_data.data)
				print(f'\nk=v => {nama_kolom}={jenis_kolom}')
				cmdargs.update({ 'name' : nama_kolom, 'value': jenis_kolom })
				config['columns'][nama_kolom] = jenis_kolom

				# kolom:tipe
				# ini adlh pemrosesan spt name:string yg gak pake subtipe
				# coltype kita sebut juga tipe... atau field kedua pada kolom:tipe:subtipe
				if coltype_childnum == 1:
					'''
					bentuk kolom:tipe ada 2 jenis:
					kolom:tipe
					kolom:tipe(modifier)
					di sini kita gunakan istilah is_token utk tentukan jk tipe punya modifier
					'''
					anaktunggal = coltype.children[0]
					# anaktunggal bisa punya anak lagi: [] atau Token
					# jadi is_token bisa ditentukan dari panjang anak
					is_token = len(anaktunggal.children)
					if is_token:
						sang_token = anaktunggal.children[0]
						sang_token = str(sang_token)
						# print('Token (kolom:<tipe>):', sang_token)
						print(f'kolom:tipe(modifier) = {nama_kolom}:{jenis_kolom}({sang_token})')
						# kita gunakan istilah 'number' utk s(100) = varchar(100)
						# 100 adlh number
						cmdargs.update({ 'number': int(sang_token) })
						# cabang = AnyNode(name=nama_kolom, type='column', value=jenis_kolom, number=int(sang_token), parent=pohon)
					else:
						print(f'kolom:tipe = {nama_kolom}:{jenis_kolom}')

					print('***', cmdargs, '\n\n')
					cabang = AnyNode(**cmdargs)
				
				# kolom:tipe:subtipe
				elif coltype_childnum == 2:
					'''
					karena utk satu tipe itu bisa: tipe dan tipe(modifier)
					maka ada 4 kombinasi dg subtipe:
					1. tipe, subtipe
					2. tipe, subtipe(modifier)
						ini kita sebut anak2 bercucu2
					3. tipe(modifier), subtipe
						ini kita sebut anak1 bercucu1
					4. tipe(modifier), subtipe(modifier)
						ini kita sebut anak1 bercucu1 dan anak2 bercucu2
					
					jadi kita gunakan istilah: anak1=tipe, anak2=subtipe
					cucu1=modifier utk anak1, cucu2=modifier utk anak2

					contoh:
					email:s(100):e
					id sini anak1(s) punya modifier(100), sdangkan anak2 tdk bercucu
					maka ini adlh bentuk no 3.

					contoh:
					mypass:b:<rahasia>
					di sini <rahasia> adlh literal sedangkan jenis/datanya adlh bcrypt_value
					di sini kita sebut anak1+anak2/cucu2, atau bentuk no 2.

					contoh:
					nilai:i:ri(1,100)
					ini lebih kompleks dari bentuk no 2, krn bentuk modifier utk subtipe lebih ribet.

					tipe 		(modifier) 	: 	subtipe 	(modifier)
					^anak1	^cucu1					^anak2		^cucu2
					'''
					# tipe
					anak1 = coltype.children[0]
					# subtipe
					anak2 = coltype.children[1]

					modifier_kolom = ''
					bercucu1 = len(anak1.children)
					bercucu2 = len(anak2.children)
					if bercucu1:
						token1 = str(anak1.children[0])
						print('Token #1 (kolom:<tipe>:subtipe):', token1)
						modifier_kolom = f'({token1})'

					if bercucu2:
						'''
						modifier utk anak2 ini ada 2 jenis
						- direct spt bcrypt
						- complex spt random_int yg punya min dan max
						'''
						# cucu2 adlh min_max = modifier utk anak2/subtipe
						cucu2 = anak2.children[0]
						modifier_subtipe = str(cucu2)		

						if isinstance(cucu2, lark.tree.Tree):
							'''
							ini adlh bentuk 'complex' cucu2/subtipe
							kita identifikasi dg jenis cucu2 adlh Tree, bukan Token
							
							kolom:tipe=anak1=number:subtipe=anak2=random_int
							dg modifier = min_max

							random_int (anak2), subtipe nya adlh minmax...
							Tree(
								'min_max', 
								[
									Tree('min', [Token('BILBUL_BERTANDA', '1')]), 
									Tree('max', [Token('BILBUL_BERTANDA', '100')])
								]
							)
							'''
							# subtipe adlh anak2=random_int, modifiernya adlh cucu2=min_max
							cmdargs.update({ 'subclasstype': anak2.data })

							min_token = cucu2.children[0]
							min = str(min_token.children[0])
							subclasstype = '(' + min							
							cmdargs.update({ 'random_int_min': min })
							config['random_int_min'] = min

							has_max = len(cucu2.children) > 1
							if has_max:
								max_token = cucu2.children[1]
								max = str(max_token.children[0])
								subclasstype += ',' + max
								cmdargs.update({ 'random_int_max': max })
								config['random_int_max'] = max

							subclasstype += ')'
							
						else:
							'''
							ini adlh bentuk direct subtype/cucu2
							subtipe adlh token/literal -> contohnya bcrypt yg punya 'password' = literal
							'''
							# di sini subtipe bcrypt punya modifier/literal = bcrypt_value
							print('Token #2 (kolom:tipe:<subtipe>):', modifier_subtipe)
							if anak1.data == 'bcrypt':
								'''berarti sedang oprek bcrypt'''
								config['bcrypt_plaintext'] = modifier_subtipe

							subclasstype = modifier_subtipe
							# ini misalnya string:b:<token nilai bcrypt>
							cmdargs.update({ 'subclasstype': subclasstype })

					else:
						subclasstype = anak2.data
						cmdargs.update({ 'subclasstype': subclasstype })

					print(f'kolom:tipe:subtipe = {nama_kolom}:{jenis_kolom}{modifier_kolom}:{subclasstype}')
					print('***', cmdargs, '\n\n')

					cabang = AnyNode(**cmdargs)

				else:
					print('beda sendiri ini jenis kolom:', jenis_kolom)

	dahan = AnyNode(name='config', type='config', value=config, parent=pohon)

	# generated_tree = tree_to_anytree(transformed_tree)
	generated_tree = pohon
	print (RenderTree(generated_tree, style=AsciiStyle()))
	# generated_tree = pohon
	return generated_tree
