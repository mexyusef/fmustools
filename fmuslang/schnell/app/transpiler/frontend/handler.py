import re
from schnell.app.stringutils import tabify_content, tabify_contentlist
from schnell.app.treeutils import (
	anak,
	data,
	token,
	child1,
	child2,
	child3,
	child4,
	child,
	chdata,
	chtoken,
	ispohon, istoken,
	beranak,
	sebanyak,
	jumlahanak,
)
import schnell.vendor.lark as lark

from context import global_context
# pinjam dari creator, walau 2 bahasa declang yg berbeda
from schnell.creator.declarative.mapper import (
	elem_mapper,
	attr_mapper,
	cdata_mapper,
	value_mapper,
)


indent = 0


def inc():
	global indent
	indent += 1


def dec():
	global indent
	indent -= 1


def tab():
	# C:\Users\usef\work\sidoarjo\context.py
	return global_context['current_tab']*indent


# element_name: HURUF_DIGIT
def element_name(tree):
	kembali = token(tree)
	if kembali in elem_mapper:
		kembali = elem_mapper[kembali]
	return kembali


# element_children: "(" declarative_program ")"
def element_children(tree):
	"""
	tree adlh tuple
	itemsnya adlh Tree
	"""
	# print('elem child terima data:', type(tree), data(tree))
	anaks = []
	for tuple_item in anak(tree): # tree
		# print(' >> elem child iterate:', type(tuple_item), tuple_item) # tuple
		for item in tuple_item:
			res = declarative_element(item)
			anaks.append(res)

	return '\n'.join(anaks)


def item_key_value_berslash(tree):
	kembali = ''
	k,v='',''
	for item in anak(tree):  
		jenis = data(item)    
		if jenis == 'item_key':
			k = token(item)
		elif jenis == 'item_value_berslash':
			v = token(item)
			# print('value beraslash:', v, 'dari:', jenis)
	kembali += f'{k}={v}'
	return kembali


# item_key "=" item_value -> item_key_value
def item_key_value(tree):
	kembali = ''
	# kvs = []
	k,v='',''
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'item_key':
			k = token(item)
			if k in attr_mapper:
				k = attr_mapper[k]
		elif jenis == 'item_value':
			v = token(item)
			if v in value_mapper:
				v = value_mapper[v]
			# isinstance(insn, lark.tree.Tree) and insn.data == 'cdata_text'
			# schnell.vendor.lark.tree.Tree
			if len(item.children)==2 and isinstance(item.children[1], lark.tree.Tree) and item.children[1].data == 'transformer':
				from schnell.creator.declarative.transformer import transformer_function
				from constants import punctuations
				item_transformer = item.children[1]
				print('item_transformer:', item_transformer, 'jenis:', type(item_transformer))
				transformer_children = item_transformer.children
				for txf_insn in transformer_children:
					txf = txf_insn.data
					v = transformer_function(txf, v)
				for k2,v2 in punctuations.items():
					v = v.replace(k2,v2)
		# kvs.append(f'{k} = {v}')
		# ikuti C:\Users\usef\work\sidoarjo\schnell\creator\declarative\handler.py
		# # cek transformer
		# if len(item.children[1].children) > 1:
		# 	transformer = item.children[1].children[1]
		# 	for txf_insn in transformer.children:
		# 		txf = txf_insn.data
		# 		nilai = transformer_function(txf, nilai)

		# Tree(																	item = item_key_value
		# 	'item_key_value', [													item.children
		# 		Tree('item_key', [
		# 			Token('HURUF_DIGIT', 'nilai')]
		# 		),
		# 		Tree('item_value', [											item = item_value, len(item.children)==2
		# 			Token('HURUF_NILAI', 'kuda'),								item.children[0]
		# 			Tree('transformer', [										item.children[1]
		# 				Tree('tx_single', [])									item.children[1].children[0]
		# 			])
		# 		])
		# 	]
		# )

	kembali += f'{k}={v}'
	return kembali

# jangan lupa item itu bisa Tree lark.tree.Tree atau Token lark.lexer.Token
# declarative_element
#   element_name  b
#   element_children
#   	(
# 		Tree('declarative_element', [Tree('element_name', [Token('HURUF_DIGIT', 'c')]), Tree('element_config', [Tree('item_key_value_boolean', [Token('HURUF_DIGIT', 'disabled')])])]),
# 		Tree('declarative_element', [Tree('element_name', [Token('HURUF_DIGIT', 'd')])]),
# 		Tree('declarative_element', [
# 			Tree('element_name', [Token('HURUF_DIGIT', 'e')]),
# 			Tree('element_config', [
# 				Tree(
# 					'item_key_value', [
# 						Tree('item_key', [
# 							Token('HURUF_DIGIT', 'nilai')]
# 						),
# 						Tree('item_value', [
# 							Token('HURUF_NILAI', 'kuda'),
# 							Tree('transformer', [
# 								Tree('tx_single', [])
# 							])
# 						])
# 					]
# 				)
# 				]
# 			),
# 			Tree('cdata_text', [Token('HURUF_CDATA', 'sampurasun')]),
# 			Tree(
# 				'element_children', [
# 					(
# 						Tree(
# 							'declarative_element', [
# 								Tree(
# 									'element_name',
# 									[Token('HURUF_DIGIT', 'f')]
# 								)
# 							]
# 						),
# 						Tree(
# 							'declarative_element', [
# 								Tree(
# 									'element_name',
# 									[Token('HURUF_DIGIT', 'g')]
# 								)
# 							]
# 						)
# 					)
# 				]
# 			)
# 		])
# 	)


# HURUF_DIGIT  -> item_key_value_boolean
def item_key_value_boolean(tree):
	"""
	daripada:
	disabled=true
	mending:
	disabled
	"""
	name = token(tree)
	# petakan jika ada di attr_mapper yg aktif
	if name in attr_mapper:
		name = attr_mapper[name]
	# kembali = f'{name}=true'
	kembali = f'{name}'
	return kembali


# element_config: "[" element_config_item (element_config_separator element_config_item)* "]"
def element_config(tree):
	kembali = ''
	kvs = []
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'item_key_value':  # item_key "=" item_value       -> item_key_value
			kv = item_key_value(item)
			kvs.append(kv)
		elif jenis == 'item_key_value_berslash':
			kv = item_key_value_berslash(item)
			kvs.append(kv)
		elif jenis == 'item_key_value_boolean':  # HURUF_DIGIT  -> item_key_value_boolean
			kv = item_key_value_boolean(item)
			kvs.append(kv)
	kembali += ' '.join(kvs)
	return kembali


# declarative_element: "<" element_name element_config? cdata_text? element_children?
def declarative_element(tree):
	kembali = ''
	name, attrs, children, text = '','','', ''
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'element_name':
			name = element_name(item)
		elif jenis == 'element_config':
			attrs = element_config(item)
		elif jenis == 'element_children':
			children = element_children(item)
		elif jenis == 'cdata_text':  # cdata_text: "|" HURUF_CDATA
			text = token(item)
			if text in cdata_mapper:
				text = cdata_mapper[text]
	kembali += f'<{name}'
	if attrs:
		kembali += ' ' + attrs
	kembali += '>\n'
	if text:
		inc()
		content = tabify_content(text, tab())
		kembali += content
		dec()
		kembali += '\n'
	if children:
		inc()
		content = tabify_content(children, tab())
		kembali += content
		dec()
		kembali += '\n'
	kembali += f'</{name}>'
	return kembali


# C:\Users\usef\work\sidoarjo\schnell\creator\declarative\mapper.py
# C:\Users\usef\work\sidoarjo\declang.json
# C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\bahasa.py
# declarative_program: declarative_element (declarative_element)*
def handler(tree):
	kembali = declarative_element(tree)
	return kembali
