
from anytree import (
	AnyNode,
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

class TheProcessor(InlineTransformer):
	def __init__(self):
		self.config = {}

	def keseluruhan(self, *instructions):
		print ('\nTheProcessor/keseluruhan ->', instructions)
		return instructions[0] # adlh tuple berisi 1 item: insn

def tree_to_anytree(root_tree):
	pohon = AnyNode(name='root', type='root')
	config = {}

	print('sumber =', RenderTree(root_tree))

	for child in root_tree.children:

		if child.data == 'data_insn':

			print('taksuka cucu?', RenderTree(child))

			for grandchild in child.children:

				print('bermasalahkah?', RenderTree(grandchild))

				if grandchild.data == 'datanumber':
					
					jumlah = str(grandchild.children[0]) # ini adlh Token(TYPE, NILAI)
					config['generate:number'] = int(jumlah)

				elif grandchild.data == 'tablename':
					tablename = str(grandchild.children[0])
					config['generate:table'] = tablename
					config['columns'] = {}
					cabang = AnyNode(name='table', type='table', value=tablename, parent=pohon)

				elif grandchild.data == 'column':
					anak1 = grandchild.children[0] # dapatkan nama kolom
					anak2 = grandchild.children[1] # dapatkan tipe kolom
					columnname = str(anak1.children[0]) # Token
					columntype_tree = anak2.children[0] # Tree(varchar, [Token(BILBUL, '100')
					columntype = columntype_tree.data # Tree -> varchar
					config['columns'][columnname] = columntype

					# utk tipe kolom: kolom:tipe:subtipe
					# subtipe sendiri bisa punya anak => number punya subtipe random_int dg anak min dan max
					if len(anak2.children) == 2: 
						# field:s:e, type anak 0 dan 1 == Tree
						subclasstree = anak2.children[1]
						subclasstype = anak2.children[1].data # sibling dari columntype yg adlh anak2.children[0].data
						if subclasstype == 'bcrypt_value':
							katakunci = str(anak2.children[1].children[0])
							config['bcrypt_plaintext'] = katakunci
						elif subclasstype == 'random_int':
							# bisa punya min dan max
							# get min dan max
							if len(subclasstree.children) > 0:
								minmax = subclasstree.children[0]
								if minmax.data == 'min_max':
									for min_or_max in minmax.children:
										if min_or_max.data == 'min':
											config['random_int_min'] = str(min_or_max.children[0])
										elif min_or_max.data == 'max':
											config['random_int_max'] = str(min_or_max.children[0])

						cabang = AnyNode(name=columnname, type='column', value=columntype, subclass=subclasstype, parent=pohon)

					elif len(columntype_tree.children) == 1: # field:s(100)
						columnnumber = str(columntype_tree.children[0])
						cabang = AnyNode(name=columnname, type='column', value=columntype, number=int(columnnumber), parent=pohon)

					else: # field:s
						cabang = AnyNode(name=columnname, type='column', value=columntype, parent=pohon)

	dahan = AnyNode(name='config', type='config', value=config, parent=pohon)
	return pohon
