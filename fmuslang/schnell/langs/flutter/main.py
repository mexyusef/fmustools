import json, os, pyperclip, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
# schnell = os.path.join(os.pardir, os.pardir, 'app')
sidoarjodir = os.path.join(os.pardir, os.pardir, os.pardir)
sys.path += [here, sidoarjodir]

try:
	import pyperclip
except ImportError as err:
	pass

def trycopy(content):
	try:
		pyperclip.copy(content)
	except Exception as err:
		pass


import schnell.vendor.lark as lark
from schnell.vendor.lark import (
	Lark,
	# InlineTransformer,
)
from schnell.vendor.lark.visitors import InlineTransformer

from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter

curdir = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.pardir)
grandpardir = os.path.dirname(pardir)
greatgrandpardir = os.path.dirname(grandpardir)
# print("$", curdir, pardir, grandpardir, greatgrandpardir)
# print(os.listdir(greatgrandpardir))
if greatgrandpardir not in sys.path:
	sys.path.append(greatgrandpardir)

default_configuration = {}

SPACE = '  '

base_grammar = """
%import common.CNAME                -> HURUF
%import common.ESCAPED_STRING       -> KALIMAT
%import common.WORD
%import common.DIGIT
%import common.HEXDIGIT
%import common.LETTER
%import common.INT                  -> BILBUL
%import common.SIGNED_INT           -> BILBUL_BERTANDA
%import common.SIGNED_NUMBER        -> BIL_BERTANDA
%import common.FLOAT                -> PECAHAN
%import common.NEWLINE
%import common.WS
%ignore WS
"""

from map_widgets import map_widgets
from map_attrs import map_attrs
from map_class import (
	map_stateful,
	map_stateless
)
from map_constants import map_constants

bahasa = f"""
keseluruhan: insn+

// w1(k1=c1)
// w1(k1=c1,k2=w2,k3=w3)
// w1(k1=c1,k2=w2,k3=w3,k4=[w4(k1=c3),w5(k3=c3)])

// krn gak class_stateful+ maka less full less -> yg less ke3 jadi kemakan widgets
// krn widget bs dimulai dg widget_name yg bisa makan "less" dan "full"
insn: class_stateful
| class_stateless
| widgets
| "/" singkat

class_stateless		: "less" class_config? class_members?
class_stateful		: "full" class_config? class_members?
class_config			: "[" class_name "]"
class_members: "(" class_member ("," class_member)* ")"
class_member			: "mi" -> member_int
| "mb" -> member_bool
| "md" -> member_double
| "mf" -> member_float
| "ml" -> member_list
| "ms" -> member_string

class_name: HURUF_DIGIT_SPASI

widgets: widget
| widget_list
widget_list: "[" widget ("," widget)* "]"
widget: (widget_type|widget_name) widget_content?
widget_type: "w1" -> widget_1
|"w2" -> widget_2
|"w3" -> widget_3
|"w4" -> widget_4
|"w5" -> widget_5

widget_name: HURUF_DIGIT

widget_content: "(" attr_widgets  ")"

attr_widgets: attr_widget ("," attr_widget)*

// attr_widget: (attr_type|attr_name) "=" widget_or_constant
// biar natural spt flutter gunakan : alih2 =
attr_widget: (attr_type|attr_name) ":" widget_or_constant
| "\\"" HURUF_DIGIT_SPASI "\\"" -> text_content
| HURUF_DIGIT_SPASI -> content
// contoh: Text("hello")
// contoh: Icon(Icons.dashboard) -> ambil dari map_const
// di sini kita gak perlu awali ic(/icmenu), cukup ic(icmenu)

attr_type: "k1" -> attr_1
|"k2" -> attr_2
|"k3" -> attr_3
|"k4" -> attr_4
|"k5" -> attr_5
// contoh: children, padding, onTap dst
attr_name: HURUF_DIGIT
widget_or_constant: value_constant
| "/" const_name
| widgets
// const_name mendahului widgets -> mendahului widget_name
// nope kita bedakan saja const dan widget name via '/' utk const
value_constant: "c1" -> constant_1
|"c2" -> constant_2
|"c3" -> constant_3
|"c4" -> constant_4
|"c5" -> constant_5
const_name: HURUF_SYSTEM

singkat: widget_or_constant

HURUF_DIGIT: 						("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 						("_"|LETTER) 		("_"|LETTER|DIGIT|" ")*
HURUF_COMMA: 						("_"|LETTER) 		("_"|LETTER|DIGIT|",")*

HURUF_SYSTEM: 					("_"|LETTER|DIGIT|"*"|"/"|"."|"\\"") 	(LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\"")*
HURUF_PASSWORD: 				("_"|LETTER) ("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"@"|"#"|"*")*
HURUF_HOST: 						("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@")*
{base_grammar}
"""

def generator():
	pass

def process_widget(ast_tree, any_tree, level, attr_to_hold_on):
	widget_name = ast_tree.children[0]
	widget_name_str = str(widget_name.children[0])
	# jk tidak ada widget_content maka return dg hanya name (berarti content default atau kosong)

	if attr_to_hold_on:
		'''sbg parent, siapkan anchors utk diproses children
		'''
		template_cantol = '__TEMPLATE__' + attr_to_hold_on
		# setattr(any_tree, attr_to_hold_on, '__TEMPLATE__')
		if hasattr(any_tree, 'anchors'):
			any_tree.anchors.update({attr_to_hold_on:template_cantol})
		else:
			any_tree.anchors = {attr_to_hold_on:template_cantol}

	if len(ast_tree.children) == 1:
		widget = AnyNode(type='widget', name=widget_name_str, parent=any_tree, level=level+1, cantol=attr_to_hold_on)
		return

	widget_content = ast_tree.children[1]
	widget = AnyNode(type='widget', name=widget_name_str, parent=any_tree, level=level+1, cantol=attr_to_hold_on)
	attr_widgets = widget_content.children[0]
	print('-- widget, anytree parent now:', widget)
	for attr in attr_widgets.children:
		# attr_widgets bisa berisi attr_widget atau text_content sbg attr di sini
		# jk attr_widget maka punya children[0] = attr_name
		if attr.data == 'text_content':
			content = str(attr.children[0])
			widget.text_content = content
			continue
		elif attr.data == 'content':
			content = str(attr.children[0])
			widget.content = content
			continue

		attr_name = attr.children[0]

		attr_name_str = str(attr_name.children[0])
		# print('     ..iterating', attr_name_str)
		attr_woc = attr.children[1]
		# print('woc:', attr_woc)
		for woc in attr_woc.children:
			if woc.data == 'const_name':
				# utk constant berarti gak ada pembuatan node baru
				# cantolkan ke node yg sdh ada
				const_value = str(woc.children[0])
				if hasattr(widget, 'attributes'):
					widget.attributes.update({
						attr_name_str: const_value
					})
				else:
					widget.attributes = {
						attr_name_str: const_value
					}
			elif woc.data == 'widgets':
				# print('\n\ncalling process_widgets from attr...', attr)
				# process_widgets(attr, any_tree=widget, level=level+1, attr_to_hold_on=attr_name_str)
				# print('\n\ncalling process_widgets from attr...', woc)
				process_widgets(woc, any_tree=widget, level=level+1, attr_to_hold_on=attr_name_str)
			elif woc.data == 'value_constant':
				pass

def process_widgets(ast_tree, any_tree, level=0, attr_to_hold_on=None):
	# print('== widgets')
	for cabang in ast_tree.children:
		# print('*', cabang.data)
		if cabang.data == 'widget':
			process_widget(cabang, any_tree, level, attr_to_hold_on)
		elif cabang.data == 'widget_list':
			any_tree.has_widget_list = 1
			for wid in cabang.children:
				process_widget(wid, any_tree, level, attr_to_hold_on)

# def processor(ast_tree, any_tree, level=0):
# 	# print('processor', pohon)
# 	for cabang in ast_tree:
# 		print('*', cabang.data)
# 		if cabang.data == 'widget':
# 			process_widget(cabang, any_tree, level)

class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions

def process_language(code):
	running_configuration = {**default_configuration}

	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*20, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	counter = 1

	level=0
	# root_anytree = AnyNode(type='root', name=root_asttree.data, level=level)
	root_anytree = AnyNode(type='root', name='root_widget_dummy', level=level)

	singkat_to_print = []
	
	for insn in instructions: # instructions adlh tuple dari insn+ -> (insn, insn, ...)
		for tree in insn.children: # insn adlh Tree
			root_asttree = tree
			print(root_asttree.pretty())
			if root_asttree.data == 'widgets':
				process_widgets(root_asttree, root_anytree, level)
			elif root_asttree.data == 'class_stateful':
				print('==> full')
				classwidget = AnyNode(type='class', name='full', parent=root_anytree, level=level+1)
				for anak in root_asttree.children:
					if anak.data == 'class_config':
						class_name = anak.children[0]
						class_name_str = str(class_name.children[0])
						classwidget.classname = class_name_str
			elif root_asttree.data == 'class_stateless':
				print('==> less')
				classwidget = AnyNode(type='class', name='less', parent=root_anytree, level=level+1)
				for anak in root_asttree.children:
					if anak.data == 'class_config':
						class_name = anak.children[0]
						class_name_str = str(class_name.children[0])
						classwidget.classname = class_name_str
			elif root_asttree.data == 'singkat':
				for woc in root_asttree.children:
					constname = woc.children[0]
					constname_str = str(constname.children[0])
					cetak = constname_str
					if constname_str in map_constants:
						cetak = cetak.replace(constname_str, map_constants[constname_str])
					# print(cetak)
					# trycopy(cetak)
					singkat_to_print .append(cetak)
			counter += 1

	# utk satu saja
	# insn = instructions[0]
	# root_asttree = insn.children[0] # widgets
	# print(root_asttree.pretty())
	# process_widgets(root_asttree, root_anytree, level)
	if singkat_to_print:
		cetak = '\n'.join(singkat_to_print)
		print(cetak)
		trycopy(cetak)
		input('...copied. Use the clipboard now before being overwritten. ')

	print('='*80)
	cetak = RenderTree(root_anytree)
	print(cetak)


	generated = ''
	cek_widget_list = [] # helper bantu bentuk children=[Widget(),Widget(),...]
	last_node = None

	for counter, node in enumerate(PreOrderIter(root_anytree)):
		if node.type == 'root':
			continue
		elif node.type == 'class':
			template_classname = '__TEMPLATE_CLASSNAME'
			if node.name == 'full':
				dummy = map_stateful
				if hasattr(node, 'classname'):
					# dummy += f'({node.classname})'
					dummy = dummy.replace(template_classname, node.classname)
				generated += dummy + '\n'
			else:
				dummy = map_stateless
				if hasattr(node, 'classname'):
					# dummy += f'({node.classname})'
					dummy = dummy.replace(template_classname, node.classname)
				generated += dummy + '\n'
		elif node.type == 'widget':			

			node_name = node.name
			if node.name in map_widgets:
				node_name = map_widgets[node.name]

			generated_widget = ''
			# generated_widget = SPACE*(int(node.level)-1)
			generated_widget += f"{node_name}("

			if hasattr(node, 'text_content'):
				# ini jadi kurang , jk disanding dg attrs lain
				generated_widget += f'"{node.text_content}"'
			elif hasattr(node, 'content'):
				# ini jadi kurang , jk disanding dg attrs lain
				replaceme = node.content
				if replaceme in map_constants:
					replaceme = map_constants[replaceme]
				generated_widget += f'{replaceme}'

			attrs_anchors = []
			if hasattr(node, 'attributes'):
				attributes = []
				for k,v in node.attributes.items():
					# perlu map v ke map_constants
					# attributes.append(f"{k}: {v}")
					# cek jk k ada di map_attrs
					key = k
					val = v
					if k in map_attrs:
						key = map_attrs[k]
						# utk val berguna utk
						# 'sy': '__TEMPLATE__sy'
						# tapi bahaya utk
						# 'fw': 'fwb'
						# maka hanya replace jk ada __TEMPLATE__ yg emang utk direplace
						if '__TEMPLATE__' in v and k in v:
							val = v.replace(k, map_attrs[k])
					
					# coba replace constant di value, blm test
					if v in map_constants:
						val = val.replace(v, map_constants[v])
					attributes.append(f"{key}: {val}")
				
				if attributes and hasattr(node, 'content'):
					# jk ada "" dan diikuti attrs, maka kasih , dulu
					generated_widget += ', '

				attrs_anchors += attributes

			if hasattr(node, 'anchors'):
				anchors = []
				for k,v in node.anchors.items():
					# cek jk k ada di map_attrs
					key = k
					val = v
					if k in map_attrs:
						key = map_attrs[k]
						# val = v.replace(k, map_attrs[k])
						if '__TEMPLATE__' in v and k in v:
							val = v.replace(k, map_attrs[k])
					if v in map_constants:
						val = val.replace(v, map_constants[v])
					anchors.append(f"{key}: {val}")
				
				attrs_anchors += anchors

			generated_widget += ', '.join(attrs_anchors)
			# if attrs_anchors:
			# 	generated_widget += '\n'
			# 	generated_widget += ',\n'.join(attrs_anchors)
			# 	generated_widget += ")" + '\n'
			# else:
			# 	generated_widget += ")"

			generated_widget += ")" # ini sudah tutup Widget(...)

			if hasattr(node, 'cantol') and node.cantol:
				cantol_name = node.cantol				
				if hasattr(node.parent, 'anchors') and cantol_name in node.parent.anchors:
					if cantol_name in map_attrs:
						cantol_name = map_attrs[cantol_name]
					template_name = '__TEMPLATE__' + cantol_name
					# chs=__TEMPLATE_chs bisa jadi: chs=[Widget(),Widget()] atau chs=Widget()
					# cek jk kita node pertama
					children_pemilik_cantol = [node for node in node.parent.children if hasattr(node, 'cantol')]
					if hasattr(node.parent, 'has_widget_list'):
						print('harus proses widget_list utk', generated_widget, 'sebanyak:', len(children_pemilik_cantol))
						if not cek_widget_list:
							# cek jk ada sibling						
							if len(children_pemilik_cantol) > 1: # jk widget_list instead of widget
								# cek_widget_list.append('[') # [ utk [Widget(),Widget()]
								cek_widget_list.append(generated_widget) # Widget()
							else: # hanya satu cantol utk parent's anchors's template
								generated = generated.replace(template_name, generated_widget)
						else: # [Widget(), ...kita di sini..., Widget()] atau [Widget(), ..., terakhir di sini]
							# cek jk node terakhir
							if len(children_pemilik_cantol) == len(cek_widget_list)+1:
								cek_widget_list.append(generated_widget)
								# cek_widget_list.append(']')
								generated_widget = '[' + ', '.join(cek_widget_list) + ']'
								generated = generated.replace(template_name, generated_widget)
								cek_widget_list = []
							else: # jk di tengah, jangan dulu assign generated = ...
								cek_widget_list.append(generated_widget)
					else:
						generated = generated.replace(template_name, generated_widget)


					# generated_widget = '\n' + (SPACE*int(node.level)) + generated_widget
					# ini memasukkan node ke lokasi parent yg saat ini berisi
					# chs=__TEMPLATE_chs
					# permasalahannya jk ada bbrp node yg memiliki cantol chs (widget_list)
					# generated = generated.replace(template_name, generated_widget)
				else:
					print(f'parent punya anchors tapi gak ada tuh {cantol_name}')
					# generated += '\n' + (SPACE*int(node.level)) + generated_widget
					# generated += '\n' + generated_widget
					generated += generated_widget
			else:
				# generated += '\n' + (SPACE*int(node.level)) + generated_widget
				# generated += '\n' + generated_widget
				generated += generated_widget


		last_node = node

	print('*'*40)
	print(generated)
	trycopy(generated)

default_program = """
ma(tit:txt("monyet",slv:/icsearch),dbg:scaf(body:row(ch:dtab),fab:csv(txt:txt("hello boyz"))),thm:thmd(pmc:/tsfz,ab:sbui),hm:/mqw)
"""

def process_program(code=None):
	if not code:
		code = default_program

	# select dari berbagai ...
	process_language(default_program)


def show_attrs(code=None):
	kamus = {v:k for k,v in map_attrs.items()}
	urut = sorted(kamus.items(), key=lambda x:x[0].lower())
	urut = {k:v for k,v in urut}
	cetak = json.dumps(urut, indent=4)
	if code:
		cetak = filter_lines(cetak, code)
	print(cetak)
	trycopy(cetak)

def show_const(code=None):
	kamus = {v:k for k,v in map_constants.items()}
	urut = sorted(kamus.items(), key=lambda x:x[0].lower())
	urut = {k:v for k,v in urut}
	cetak = json.dumps(urut, indent=4)
	if code:
		cetak = filter_lines(cetak, code)
	print(cetak)
	trycopy(cetak)

def show_widgets(code=None):
	kamus = {v:k for k,v in map_widgets.items()}
	urut = sorted(kamus.items(), key=lambda x:x[0].lower())
	urut = {k:v for k,v in urut}
	cetak = json.dumps(urut, indent=4)
	if code:
		cetak = filter_lines(cetak, code)
	print(cetak)
	trycopy(cetak)

def show_all(code=None):
	kamus = {v:k for k,v in map_widgets.items()}
	kamus.update({v:k for k,v in map_attrs.items()})
	kamus.update({v:k for k,v in map_constants.items()})
	urut = sorted(kamus.items(), key=lambda x:x[0].lower())
	urut = {k:v for k,v in urut}
	cetak = json.dumps(urut, indent=4)
	if code:
		cetak = filter_lines(cetak, code)
	print(cetak)
	trycopy(cetak)

def filter_lines(content, cari):
	baris = content.splitlines()
	saring = [item for item in baris if cari.lower() in item.lower()]
	return '\n'.join(saring)

def myrepl():
	print('***              myrepl')
	code = 1
	while code != 'x':
		try:
			code = input('myrepl>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code .startswith('attrs'):
				kamus = {v:k for k,v in map_attrs.items()}
				urut = sorted(kamus.items(), key=lambda x:x[0].lower())
				urut = {k:v for k,v in urut}
				cetak = json.dumps(urut, indent=4)
				print(cetak)
			elif code .startswith('const'):
				kamus = {v:k for k,v in map_constants.items()}
				urut = sorted(kamus.items(), key=lambda x:x[0].lower())
				urut = {k:v for k,v in urut}
				cetak = json.dumps(urut, indent=4)
				print(cetak)
			elif code .startswith('widgets'):
				kamus = {v:k for k,v in map_widgets.items()}
				urut = sorted(kamus.items(), key=lambda x:x[0].lower())
				urut = {k:v for k,v in urut}
				cetak = json.dumps(urut, indent=4)
				# cetak = json.dumps(urut, indent=4)
				# cetak = json.dumps(dict(zip(urut.keys(), urut.values())), indent=4)				
				print(cetak)
			elif code .startswith('all'):
				# kamus1 = {v:k for k,v in map_attrs.items()}
				# kamus2 = {v:k for k,v in map_constants.items()}
				# kamus3 = {v:k for k,v in map_widgets.items()}
				# keys = list(kamus1.keys()) + list(kamus2.keys()) + list(kamus3.keys())
				# vals = list(kamus1.values()) + list(kamus2.values()) + list(kamus3.values())
				# cetak = json.dumps(dict(zip(keys, vals)), indent=4)
				# cetak = json.dumps(zip(vals, keys), indent=4)

				kamus = {v:k for k,v in map_widgets.items()}
				kamus.update({v:k for k,v in map_attrs.items()})
				kamus.update({v:k for k,v in map_constants.items()})
				urut = sorted(kamus.items(), key=lambda x:x[0].lower())
				urut = {k:v for k,v in urut}
				cetak = json.dumps(urut, indent=4)

				print(cetak)
			elif code .startswith('#'):
				code = code.replace('#','',1).strip
				process_program(code)
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
