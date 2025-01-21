from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
# from anytree.importer import JsonImporter, DictImporter
from anytree.search import find, findall

from constants import punctuations
from context import global_context
from startup import programming_data, initialize_programming_data
if not programming_data:
	initialize_programming_data()

import schnell.vendor.lark as lark
from schnell.vendor.lark import Lark, InlineTransformer
from schnell.app.dirutils import ayah, joiner, bongkar, isfile
from schnell.app.fileutils import file_lines, get_definition_by_key_permissive_start, file_content
from schnell.app.printutils import indah0, indah3, indah4
from schnell.app.utils import env_get, trypaste
from schnell.app.utils import trypaste
from schnell.app.appconfig import declarative_language_data
from ..context import (
	current_decl_filename,
)
from .mapper import (
	elem_mapper,
	attr_mapper,
	cdata_mapper,
	value_mapper,
)

# from schnell.creator.declarative.transformer import transformer_function
from .transformer import transformer_function


# TAB = ' '*2
DELIMITER_SAMADENGAN = '='
DELIMITER_KOLON = ': '

# puncs utk:
# cdata (yaml: value utk tag)
# value utk key-val/attrs
# x18x22sleepx22x28 x223600x22x19] -> ["sleep", "3600"], x30etcx30config -> /etc/config, myx13pod -> my-pod

def decl_filename_to_dict(filepath):
	pasangan = file_lines(filepath)
	pisah = [[el.strip() for el in item.split('=', 1)] for item in pasangan]
	return dict(pisah)


def assign_level(pohon):
	for node in PreOrderIter(pohon):
		# print(node, node.depth)
		node.level = node.depth


def create_closing_tags(pohon):
	"""
	ribet
	"""
	for element in findall(pohon, lambda node: node.name == 'element'):
		first_children = element.children[0]
		closing = AnyNode(parent=element, level=first_children.level, name=first_children.name, type='closing_tag_element')


def reindex(pohon):
	for index, node in enumerate(PreOrderIter(pohon), 1):
		node.counter = index
		node.id = index


def remove_mapper_keys(toremovelist, which=0):
	"""
	which
	0 = elem/tag mapper
	1 = attr mapper
	2 = value mapper
	"""
	kembali = elem_mapper
	for item in toremovelist:
		if which == 0:
			elem_mapper.pop(item)
		elif which == 1:
			kembali = attr_mapper
			attr_mapper.pop(item)
		elif which == 2:
			kembali = cdata_mapper
			cdata_mapper.pop(item)
		elif which == 3:
			kembali = value_mapper
			value_mapper.pop(item)
	return kembali


def add_mapper_keys(toadddict, which=0):
	"""
	#+e{a:1,b:2}

	0 = element/tag
	1 = attribute
	2 = cdata/text
	3 = value dari attribute
	"""
	# global elem_mapper, attr_mapper, cdata_mapper, value_mapper
	kembali = None
	indah4(f'add_mapper_keys, which: {which}, toadddict={toadddict}', warna='magenta')
	if which == 0:
		elem_mapper.update(toadddict)
		kembali = elem_mapper
		indah4('elem add mapper now', warna='yellow')
	elif which == 1:
		indah4('1', warna='cyan')
		attr_mapper.update(toadddict)
		kembali = attr_mapper
		indah4('attr add mapper now', warna='yellow')
	elif which == 2:
		indah4('2', warna='cyan')
		cdata_mapper.update(toadddict)
		kembali = cdata_mapper
		indah4('cdata add mapper now', warna='yellow')
	elif which == 3:
		indah4('3', warna='cyan')
		value_mapper.update(toadddict)
		kembali = value_mapper
		indah4('value add mapper now', warna='yellow')
	return kembali


def values_from_clipboard(which=0):
	"""
	which
		elem		0
		attr		1
		cdata		2
		value		3
	a=b
	c=d
	e=f
	"""
	print('[creator.declarative.handler] values_from_clipboard')	
	content = trypaste()
	print('[creator.declarative.handler] content:', content)
	baris = [line for line in content.splitlines() if line.count('=')==1]
	if baris:
		dictify = {}
		print('[creator.declarative.handler] baris:', baris)
		for b in baris:
			k,v = b.split('=')
			dictify[k]=v

		print('[creator.declarative.handler] dict:', dict)
		return reset_mapper_keys(dictify, which=which)

	return None


def reset_mapper_keys(newvalue=None, which=0):
	"""
	reset ke value baru
	"""
	# from .mapper import elem_mapper, attr_mapper, cdata_mapper, value_mapper
	global elem_mapper, attr_mapper, cdata_mapper, value_mapper
	if which == 0:
		elem_mapper=newvalue
		kembali = elem_mapper
	elif which == 1:
		attr_mapper=newvalue
		kembali = attr_mapper
	elif which == 2:
		cdata_mapper=newvalue
		kembali = cdata_mapper
	elif which == 3:
		value_mapper=newvalue
		kembali = value_mapper
	return kembali


def load_from_ini(content, which=0):
	print('[creator.declarative.handler] load_from_ini, which:', which)
	# content = trypaste()
	print('[creator.declarative.handler] content:', content)
	baris = [line for line in content.splitlines() if line.count('=')==1]
	if baris:
		dictify = {}
		print('[creator.declarative.handler] baris:', baris)
		for b in baris:
			k,v = b.split('=',1)
			dictify[k]=v

		print('[creator.declarative.handler] dict:', dictify)
		# return reset_mapper_keys(dictify, which=which)
		return add_mapper_keys(dictify, which=which)

	return None


def load_kubernetes():
	from .mapper import cdata_kubernetes_ini, elem_kubernetes_ini
	load_from_ini(elem_kubernetes_ini, 0)
	load_from_ini(cdata_kubernetes_ini, 2)


def load_from_ini_file(filepath, which=0):
	filepath = bongkar(filepath)
	if isfile(filepath):
		load_from_ini(file_content(filepath), which=which)
		indah4(f'{filepath} INI-reloaded...', warna='green')
	else:
		indah4(f'{filepath} not found', warna='red')


def process_declarative_program(program, ayah, delimiter=DELIMITER_SAMADENGAN, first_time=False):
	"""
	belum bener nih, masih muter2 stlh selesai..
	"""
	for insn in program:

		# print('process insn:', insn)

		if isinstance(insn, lark.tree.Tree) and insn.data == 'element_config':
			'''
			jk element_config kita proses anak2nya dan kita attach ke parent=element
			element_config
				element_config_item   config1
				element_config_item   config2
			element_config
				element_config_item     disabled
				item_key_value
					item_key      type
					item_value    base
			'''
			# print('		process config')
			for item in insn.children:

				if item.data == 'element_config_item':
					nilai = str(insn.children[0].children[0])

					# attr: disabled
					if nilai in attr_mapper:
						nilai = attr_mapper[nilai]

					if hasattr(ayah, 'config'):
						ayah.config.append(nilai)
					else:
						ayah.config = [nilai]

				elif item.data == 'item_key_value':
					'''
					element_config_item: HURUF_DIGIT
						| item_key "=" item_value       -> item_key_value
					item_key: HURUF_DIGIT
					item_value: HURUF_DIGIT_SPASI transformer?
					transform_value: "'" -> tx_single
						| "'d" -> tx_double
					'''
					kunci = str(item.children[0].children[0])
					nilai = str(item.children[1].children[0])

					# attr: className=...
					if kunci in attr_mapper:
						kunci = attr_mapper[kunci]
					if nilai in value_mapper:
						nilai = value_mapper[nilai]

					# cek transformer
					if len(item.children[1].children) > 1:
						transformer = item.children[1].children[1]
						for txf_insn in transformer.children:
							txf = txf_insn.data
							nilai = transformer_function(txf, nilai)
							# if txf == 'tx_single':
							# 	nilai = f"'{nilai}'"
							# elif txf == 'tx_double':
							# 	nilai = f'"{nilai}"'
							# elif txf == 'tx_braces':
							# 	nilai = f'{{ {nilai} }}'
							# elif txf == 'tx_brackets':
							# 	nilai = f'[ {nilai} ]'
							# elif txf == 'tx_parentheses':
							# 	nilai = f'( {nilai} )'

					# replace puncs di nilai
					for k,v in punctuations.items():
						nilai = nilai.replace(k,v)
					if hasattr(ayah, 'config'):
						ayah.config.append(f"{kunci}{delimiter}{nilai}")
					else:
						ayah.config = [f"{kunci}{delimiter}{nilai}"]

			continue # pastikan tidak proses token ke bawah

		elif isinstance(insn, lark.tree.Tree) and insn.data == 'cdata_text':
			# previous insn adlh element name...
			# from schnell.app.treeutils import get_previous_sibling

			# elem = get_previous_sibling(insn)
			# index_aku = ayah.index(insn)
			# if index_aku and index_aku > 0:

			print('[creator.declarative.handler] ayah:', ayah, 'children:', ayah.children)
			# ayah: AnyNode(name='element', type='dahan') 
			# children: (AnyNode(name='c', original='element_name', type='tag_element'),)
			prev = ayah.children[0]
			if prev:
				print('[creator.declarative.handler] process insn:', insn, 'sibling?', prev)
				if prev:
					cdata = str(insn.children[0])
					print('[creator.declarative.handler] cdata:', cdata)
					if cdata in cdata_mapper:
						cdata = cdata_mapper[cdata]
					prev.cdata = cdata
			continue

		elif isinstance(insn, lark.lexer.Token):
			# print('DECL TOKEN', str(insn))
			nama_elemen = str(insn)
			# print('item:', insn, 'parent:', ayah)
			# if hasattr(ayah, 'txf'):
			# 	'''
			# 	jk minta transformasi text element name, maka dulukan dibanding mapper
			# 	'''
			# 	if nama_elemen in ayah.txf:
			# 		print(f'transform elem name dari {nama_elemen} ke {ayah.txf[nama_elemen]}')
			# 		nama_elemen = ayah.txf[nama_elemen]
			if nama_elemen in declarative_language_data['creator.declarative.handler']:
				# print(f"transform elem name dari {nama_elemen} ke {declarative_language_data['creator.declarative.handler'][nama_elemen]}")
				nama_elemen = declarative_language_data['creator.declarative.handler'].pop(nama_elemen) # [nama_elemen]
				# hapus stlh pake
				# del declarative_language_data['creator.declarative.handler'][nama_elemen]

			if nama_elemen in elem_mapper:
				nama_elemen = elem_mapper[nama_elemen]

			ayah.original = ayah.name
			ayah.name = nama_elemen
			ayah.type = 'tag_element'
			# krn sebab ini dan itu, original='element_config_item' hrs parent ke sibling pertama
			if ayah.original=='element_config_item':
				first_sibling = ayah.parent.children[0]
				ayah.parent = first_sibling
			continue

		# elif insn.data == 'element' or insn.data == 'element_children':
		# 	# teknik skip
		# 	anak = ayah

		else: # element_name, element_config, element_config_item, element_children
			# print('DECL', insn.pretty())
			# element_name: HURUF_DIGIT transformer?
			name = insn.data
			# if name == 'element_name':
			# 	print('found elem:', name)
			if name == 'element_name' and len(insn.children)>1:
				'''
				element
					element_name
						a             insn.children[0]
						transformer   insn.children[1]
							tx_capitalize
				'''
				transformer = insn.children[1]
				to_transform = str(insn.children[0])
				for txf_insn in transformer.children:
					# print(f'trying transforming {to_transform}')
					result_transform = transformer_function(txf_insn.data, to_transform)
					# print(f'result of transforming {to_transform} = {result_transform}')
					if to_transform != result_transform:
						# ternyata gak bisa kasih txf ke tree...now what?
						declarative_language_data['creator.declarative.handler'][to_transform] = result_transform
					# print(f'insn now:', insn)
			anak = AnyNode(name=name, parent=ayah, type='dahan')

		if hasattr(insn, 'children'):
			process_declarative_program(insn.children, anak, delimiter=delimiter)
			# create closing tag utk anak
			# closing = AnyNode(name=anak.name, parent=anak, type='closing_tag')


def generate_declarative_program(pohon, yaml_mode=False, json_mode=False):
	"""
	dipanggil: $ decl
	"""
	generated_code = ''
	current_config = None
	createdir = programming_data['j']['schnell']['app']['configuration']['ULIBPY_CREATORDBDIR'] # env_get('ULIBPY_CREATORDBDIR')
	# createdir = joiner(self.config.run_configuration['cwd'], 'createdb')
	decl_filename = joiner(createdir, current_decl_filename())
	reserved_tagnames = decl_filename_to_dict(decl_filename)

	for node in PreOrderIter(pohon):
		
		indent = (global_context['current_tab']*( (node.depth//3) - 1 ))
		tagname = node.name

		# replacer
		if tagname in reserved_tagnames:
			tagname = reserved_tagnames[tagname]

		if node.name == 'element':
			if hasattr(node, 'config'):
				current_config = node.config

		elif node.type == 'tag_element' and node.original == 'element_name':
			if not yaml_mode and not json_mode:
				generated_code += indent + "<" + tagname # node.name.upper()
			elif yaml_mode:
				generated_code += indent + tagname + ':'
			elif json_mode:
				generated_code += f'{indent}"{tagname}": '
				if not hasattr(node, 'cdata'):
					generated_code += '{\n'

			if current_config:
				# current_config adlh attrs utk sebuah tag
				if json_mode:
					pisah_koma = ', '.join(current_config)
					generated_code += indent + global_context['current_tab'] + f'[{pisah_koma}]\n'
				else:
					for conf in current_config:
						'''
						append attrs utk masing-masing tag
						'''
						# print('config:', conf)
						if not yaml_mode and not json_mode:
							generated_code += f" {conf}"
						elif yaml_mode:
							generated_code += f"\n{indent + global_context['current_tab']}{conf}"
				current_config = None

			# open tag on its own line
			if not yaml_mode and not json_mode:
				generated_code += ">" + "\n"
			# else:
			# 	generated_code += "\n"

			if hasattr(node, 'cdata'):
				# cdata adlh text utk sebuah tag
				# atau value utk "section" di yaml
				if not yaml_mode and not json_mode:
					generated_code += indent + node.cdata + "\n"
				elif yaml_mode:
					generated_code += " " + node.cdata + "\n"
				elif json_mode:
					generated_code += f'"{node.cdata}"\n'
				# print('yes cdata:', node, '=>', node.cdata)
			elif yaml_mode:
				generated_code += "\n"

		elif node.type == 'tag_element' and node.original == 'frontend_usage':
			pass

		elif node.type == 'closing_tag_element':
			# generated_code += indent + "</" + node.name.upper() + ">" + "\n\n"
			if not yaml_mode and not json_mode:
				generated_code += indent + "</" + tagname + ">" + "\n"
			elif json_mode:
				if not hasattr(node, 'cdata'):
					generated_code += indent + '}\n'


	# print_copy(generated_code)
	# trycopy(generated_code)
	indah3(generated_code, warna='yellow')
	return generated_code


def generate_program(insn, as_service=False, yaml_mode=False, json_mode=False):
	pohon = AnyNode(name='root', type='root', value='declarative')
	"""
	repl.py#1674
	if insn.data == 'declarative_program':
		from schnell.creator.declarative import root_declarative/generate_program
		self.pohon = root_declarative(insn)

	DF...code...
	DF[yaml]...code...
	insn: insn
		declarative_program
			fileconfig  yaml
			declaratives___
				element
					element_name    apiVersion
					cdata_text      v1
	"""
	check_yaml = insn.children[0]
	delimiter = DELIMITER_SAMADENGAN
	if check_yaml.data == 'fileconfig':
		check_yaml_value = str(check_yaml.children[0])
		if check_yaml_value == 'yaml':
			delimiter = DELIMITER_KOLON
			yaml_mode=True
		elif check_yaml_value == 'json':
			delimiter = DELIMITER_KOLON
			json_mode=True

	process_declarative_program(insn.children, pohon, delimiter=delimiter, first_time=True)

	# print(findall(self.pohon, lambda node: hasattr(node, 'original')))
	assign_level(pohon)
	create_closing_tags(pohon)
	reindex(pohon)

	# if self.config.run_configuration['print_after_process']:
	generated_code = generate_declarative_program(pohon, yaml_mode=yaml_mode, json_mode=json_mode)

	if as_service:
		return pohon, generated_code
	return pohon
