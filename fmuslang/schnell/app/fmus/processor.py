# import ast, copy, json, os, re, shutil, sys
import json, uuid
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
# from anytree.importer import JsonImporter, DictImporter
# from anytree.search import find, findall
# prohibited_chars = {
# 	'__DQ': '"',
# 	'__SQ': "'",
# 	'__BT': '`',
# }
import schnell.vendor.lark as lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)
# from lark.visitors import InlineTransformer
# from lark import (
# 	Lark,
# 	# InlineTransformer,
# )
# from lark.visitors import InlineTransformer
from schnell.vendor.lark.indenter import Indenter

# from schnell.app.fmusutils import replace_from_configuration
from schnell.app.appconfig import programming_data
from schnell.app.stringutils import chars_to_sanitize_in_file_operation
from schnell.app.fileutils import get_definition_by_key_permissive_start
# prohibited_chars = chars_to_sanitize_in_file_operation
# original local imports
from schnell.app.grammar import (
	base_grammar,
	bahasa,
	filedir_bahasa,
)
# local imports
# from schnell.app.definitor import BaseDefinitor
from schnell.app.dirutils import (
	# abs_dir,
	# ayah,
	# create_dir,
	# find_patterns,
	# here,
	# isdir,
	is_windows_drive,
	isfile,
	joiner,
	normy,
	# doesexist,
	# tempdir,
	# file_under_tempdir,
	# exists_in_dir,
	files_filter,
)
from schnell.app.printutils import (
	Debug,
	# dir_w,
	# filter_print_latest_files,
	indah, indah0, indah4,
	# print_copy,
	# print_copy_enumerate,
	# print_copy_enumerate_list,
	# print_copy_file,
	# print_list_warna,
)
from schnell.app.utils import (
	# trycopy,
	# trypaste,
	# yesno,
	env_get,
	env_int,
	is_windows,
	linuxify,
	platform,
	windowsify,
)
from schnell.app.treeutils import (
	chtoken, chdata,
	data, token, beranak,
	child1, child2, child3, child4, child5,
)

from .common import Common, LISTDIR, LISTSTR, LISTCMA
from .helper import decode_filename


is_debugging = env_int('ULIBPY_FMUS_DEBUG') > 1
# is_debugging = 2

class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions


class TreeIndenter(Indenter):
	NL_type             = '_NL'
	OPEN_PAREN_types    = []
	CLOSE_PAREN_types   = []
	INDENT_type         = '_INDENT'
	DEDENT_type         = '_DEDENT'
	tab_len             = 4


class Processor:


	def __init__(self, run_configuration):
		self.run_configuration = run_configuration
		self.debug = Debug(env_int('ULIBPY_FMUS_DEBUG')>0)
		# input('create processor/print debug '+run_configuration['debug'])
		self.parser = Lark(bahasa, start='keseluruhan', parser='lalr', postlex=TreeIndenter()).parse
		self.parser_filedir = Lark(filedir_bahasa, start='keseluruhan').parse


	def process_language(self, code):

		# is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
		# # is_debugging = 2

		if is_debugging:
			indah(f'''***** PROCESSOR *****
			self.run_configuration all = {self.run_configuration}
			self.run_configuration replacer = {self.run_configuration['replacer']}
			''', warna='magenta', layar='black', newline=True, bold=True, blink=True)

		if is_debugging:
			indah4(f"[processor:process_language] #1 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		if '__FILE__' in self.run_configuration['replacer']:
			if is_debugging:
				self.debug(f"{'='*10} [processor:process_language] #1b mk file = {self.run_configuration['replacer']['__FILE__']}\n")
		else:
			if is_debugging:
				self.debug(f"[processor:process_language] #1c __FILE__ not in replacer (from clipboard or wmcer)\n")

		if is_debugging:
			indah4(f"[processor:process_language] #2 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		# di sini ubah projectdir ke __CURDIR jk berbeda
		# harusnya hanya jika parent bukan di /<abs path>
		# err...tapi di awal projectdir adlh /tmp/sample sesuai config.json
		# hrs deteksi jk load child program kita jangan lakukan pengubahan... => seconded at 3/8/2023

		# self.run_configuration replacer
		# '__FILE__': 'C:\\Users\\usef\\work\\sidoarjo\\perintah\\fmusfiles\\files.mk',
		# '__IF_ETH0': 'localhost',
		# '__SYS_TEMP2': 'C:\\Users\\usef\\AppData\\Local\\Temp\\',
		# '__SYS_TEMP': 'C:\\Users\\usef\\AppData\\Local\\Temp',
		# '__PWD__': 'C:\\portfolio\\react\\pwa-vite-react-boilerplate-rework',
		# '__CURDIR__': 'C:\\Users\\usef\\work\\sidoarjo\\perintah\\fmusfiles',
		# 'ULIBPY__PWD__': 'C:\\portfolio\\react\\pwa-vite-react-boilerplate-rework',
		# '__CHILDFILE__': 'C:\\Users\\usef\\work\\sidoarjo\\perintah\\fmusfiles\\files.mk',
		# '__CHILDCURDIR__': 'C:\\Users\\usef\\work\\sidoarjo\\perintah\\fmusfiles',
		is_loading_child_program = ('__CHILDFILE__' in self.run_configuration['replacer']
			      and '__CHILDCURDIR__' in self.run_configuration['replacer']
				  and self.run_configuration['replacer']['__PWD__']!=self.run_configuration['replacer']['__CHILDCURDIR__'])
		if '__CURDIR__' in self.run_configuration['replacer'] and not is_loading_child_program:
			curdir_selected = self.run_configuration['replacer']['__CURDIR__']
			if (self.run_configuration['projectdir'] != curdir_selected
				and self.run_configuration['projectdir'] == self.run_configuration['original_projectdir']):
				if is_debugging:
					indah4(f"[processor:process_language] #2b ubah projectdir dari {self.run_configuration['projectdir']} ke {curdir_selected}", warna='magenta')
				# input('...press any key')
				self.run_configuration['projectdir'] = curdir_selected

		if is_debugging:
			indah4(f"[processor:process_language] #3 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		if is_debugging:
			self.debug("[processor:process_language] #3b code = [" + code + "]" + '\n')
			self.debug('-'*10, f"[processor:process_language] #3c start projectdir [{self.run_configuration['projectdir']}]\n")

		if is_debugging:
			indah4(f"[processor:process_language] #4 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		root_tree = self.parser(code)

		if is_debugging:
			indah4(f'''[processor:process_language] #5
			hasil root_tree = self.parser(code):
			{root_tree}
			''')
		# indah4(f"[processor] #5 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		self.run_configuration['counter'] = -1

		if is_debugging:
			self.debug(f"\n[processor:process_language] #6 PRE treeify - configuration projectdir = {self.run_configuration['projectdir']}\n")
		if self.run_configuration['projectdir']:
			# workdir pertama mengikuti 'projectdir'
			pohon = self.treeify(root_tree, workdir=self.run_configuration['projectdir'])
		else:
			pohon = self.treeify(root_tree)

		# indah4(f'''
		# root_tree stlh treeify:
		# {root_tree}
		# dan pohon:
		# {RenderTree(pohon)}
		# ''')
		# indah4(f"[processor] #6 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		if is_debugging:
			indah4(f"""[processor:process_language] #7 root_tree PRE cantol source code = [{pohon}]""", warna='green')

		jumlah_cantol_max = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SOURCECODE_CANTOL_MAX"] # env_int('ULIBPY_SOURCECODE_CANTOL_MAX')
		if len(code) > jumlah_cantol_max:
			pohon.source_code = code[:jumlah_cantol_max]
		else:
			pohon.source_code = code

		if is_debugging:
			indah4(f'''[processor:process_language] #8
			root_tree POST cantol source code = [{pohon}]
			''', warna='yellow')

		# ini utk lihat tree sblm masuk generator
		# cocok utk debug
		# self.debug(RenderTree(pohon))
		self.run_configuration['total'] = self.run_configuration['counter']

		if is_debugging:
			indah4('[processor:process_language]. END.\n\n', warna='red')

		return pohon


	def treeify(self, tree, parent=None, level=0, workdir=''):

		# is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1

		current_node = parent

		for child in tree.children:
			if is_debugging:
				self.debug(f"""\n\n{Common.TAB * level}[processor:treeify] #1 treeify
				level: {level} 
				initial assignment for workdir: [{workdir}]
				parent/current_node = {current_node}
				child yg akan jadi original: {child}
				berjenis {type(child)}
				""")

			if isinstance(child, lark.lexer.Token):
				original = str(child)
				kembalian = self.process_folderline(original, level, workdir=workdir, ParentNode=current_node)
				if kembalian:
					current_node = kembalian
					workdir = current_node.workdir
					if is_debugging:
						self.debug(f"[processor:treeify] #1b (+) current_node OK dari self.process_folderline utk code [{original}]\n")
				else:
					if is_debugging:
						self.debug(f"[processor:treeify] #1c (x) No kembalian dari self.process_folderline utk code [{original}]\n")

			elif isinstance(child, lark.tree.Tree):
				sekarang = str(child)
				if is_debugging:
					self.debug(Common.TAB * level, f'[processor:treeify] #2 parent node utk code [{sekarang}] skrg:', current_node)
				newlevel = level + 1
				self.treeify(child, parent=current_node, level=newlevel, workdir=workdir)

		return current_node


	def replace_me(self, line):
		for k, v in self.run_configuration['replacer'].items():
			try:
				line = line.replace(k, v)
			except Exception as err:
				indah4(f'''[processor]
				{err}
				k {k}, v {v}
				''', warna='red')
		return line


	def sanitize_prohibited_chars(self, content):
		"""
		kita bisa tulis DQ sbg pengganti double quote
		@re,baris_cari_dalam_mk_file,"something DQemphasizedDQ and other"
		lihat di h feature
		pubspec.yaml,f(f=pubspec.yaml,@ra=flutter_sdk_no="sdk: DQ>=2.")
		sebetulnya lebih baik jk kita gunakan
		__DQ daripada DQ doang...
		"""
		for k,v in chars_to_sanitize_in_file_operation.items():
			content = content.replace(k, v)

		return content


	def process_folderline(self, code, parentLevel=0, workdir='', ParentNode=None):

		# is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
		# # is_debugging = 2

		if is_debugging:
			self.debug(f'[s.a.f.processor:process_folderline] #1 code: [{code}]. level = {parentLevel}, parent = {ParentNode}\n')

		hasil_parse = self.parser_filedir(code)
		transformed = TheProcessor().transform(hasil_parse) [0] # insn+ adlh tuple, jd ambil elem 0

		if is_debugging:
			indah4(f"[processor:process_folderline] #2 initial workdir={workdir}, code={code}, Common.dict={list(Common.temporary_dict.keys())}", warna='yellow')

		if is_debugging:
			self.debug(f'''[processor:process_folderline] #3
			tree prettified: {transformed.pretty()}
			jenis: {type(transformed)}
			jika "lark.tree.Tree", data adalah:
			{data(transformed)}
			''')
		NewNode = None # AnyNode(name='/', type='dir')
		self.run_configuration['counter'] += 1

		if not beranak(transformed):
			'''
			item.command digunakan utk process_language(command)
			code = original = / <command>
			jadi:
			item.command = code.removeprefix('/')
			'''
			NewNode = AnyNode(name='empty_quick_command',
				type='empty_quick_command',
				forced_entry=False,
				counter=self.run_configuration['counter'],
				content='empty_quick_command',
				command=code.removeprefix('/'),
				original=code,
				workdir=normy(workdir),
				level=parentLevel)
			if env_int('ULIBPY_FMUS_DEBUG')>=1:
				print('[processor::process_folderline][empty_quick_command] #4 buat empty quick:', NewNode)

		for tree in transformed.children:

			if tree.data == 'comment':
				comment = str(tree.children[0])
				indah4('# ' + comment, warna='magenta')
				return None # gak perlu bikin newnode utk diproses generator

			elif tree.data == 'pesan_instruksi':
				comment = str(tree.children[0])

				# replacer utk %variables
				# Common.replace_me
				if is_debugging:
					indah4(f'[processor:process_folderline|pesan_instruksi] #5 Common.replace_me dipanggil untuk [{comment}]', warna='yellow', layar='blue')
				comment_new = Common.replace_me(comment)
				if '__INPUT__' in comment_new and not '__INPUT__' in comment:
					# jk malah dapat __INPUT__ dari sebelumnya, skip, biar yg update nanti oleh generator
					# why? krn misal item sblm ini (item-1) adlh %savetemp yg dia sendiri gak menerima nilai dari user sampai fase generator
					# jk jk di sini item+0 peroleh __INPUT__ maka hilang asosiasinya dg item-1
					# from rich.pretty import pprint
					# pprint(Common.temporary_dict)
					pass
				else:
					comment = comment_new

				# if not '__PWD' in Common.temporary_dict:
				# 	# kasih replacer utk keyword:
				# 	# UPDATE:
				# 	# ini tidak benar
				# 	# PWD harus selalu senilai dg asal mulanya
				# 	comment = comment.replace('__PWD__', workdir)
				# 	comment = comment.replace('__PWD', workdir)

				# kita tambah fitur utk tidak input() jk pesan diakhiri dg *
				forced_entry = False
				if comment.endswith('*'):
					comment = comment[:-1]
					forced_entry = True
				if not ParentNode:
					NewNode = AnyNode(name='info',
						type='pesan_instruksi',
						forced_entry=forced_entry,
						counter=self.run_configuration['counter'],
						content=comment,
						original=code,
						workdir=normy(workdir),
						level=parentLevel)
				else:
					NewNode = AnyNode(name='info',
						type='pesan_instruksi',
						forced_entry=forced_entry,
						counter=self.run_configuration['counter'],
						content=comment,
						original=code,
						workdir=normy(workdir),
						level=parentLevel,
						parent=ParentNode)

			elif tree.data == 'save_variables':
				'''
				tadinya processor dan generator dipisah filenya.
				jadi utk variables di processor agar bisa diakses di generator via tree.variables
				yg digunakan wkt process f(e=), f(b64=) dst.
				skrg semua bisa akses dari Common.temporary_dict.
				'''
				from schnell.app.fmusutils import replace_from_configuration # supaya tdk circular import
				singkat = str(tree.children[0].children[0])
				panjang = str(tree.children[1].children[0])
				has_text_oper = len(tree.children) == 3

				# gunakan library biar tertib
				# for k,v in self.run_configuration['replacer'].items():
				# 	if env_int('ULIBPY_FMUS_DEBUG') > 1:
				# 		self.debug(f'[processor] * replacing {k} dengan {v}', warna='white', newline=True)
				# 	# if k in panjang:
				# 	# 	indah4(f'		*save_variables* replacing {k} dengan {v}', warna='white')
				# 	panjang = panjang.replace(k, v)
				# # panjang di sini juga bisa berisi "input" yg hrs diupdate
				old_panjang_sebelum_replace_from_configuration = panjang
				# __TEMPLATE_DJANGOAPP => __INPUT__
				singkat_panjang = {singkat:old_panjang_sebelum_replace_from_configuration}
				panjang = replace_from_configuration(panjang, self.run_configuration)

				if env_int('ULIBPY_FMUS_DEBUG') > 1:
					indah4(f"""\n[processor|save_variables] #1\n\tlen(tree.children) = {len(tree.children)}\n\tcek [{panjang}] dalam COMMONDICT [{Common.temporary_dict}]""",
					warna='yellow')
					# indah4(str(RenderTree(tree)), warna='cyan', layar='yellow')
					indah4(tree.pretty(), warna='yellow', layar='cyan')

				# if panjang in Common.temporary_dict:
				# 28/12/22, jk ada current temp vars, new temp var bs gunakan valuenya
				if Common.temporary_dict:
					if env_int('ULIBPY_FMUS_DEBUG') > 1:
						indah4(f"""[processor|save_variables] #2 replacing "{panjang}" dalam {Common.temporary_dict}""", warna='yellow')
					panjang = Common.replace_me(panjang)

				# jika punya text_operations maka harus skip, karena nilai/panjang belum benar
				# harus tunggu generator utk benerin
				# save_variables
				# singkat       NAMAFOLDER
				# panjang       NAMAPACKAGE
				# text_operations
				# 	dot_to_slash
				if not panjang.endswith('|basename') and not panjang in ['__OPENFILE__', '__OPENDIR__', '__SAVEFILE__'] and not has_text_oper:
					if env_int('ULIBPY_FMUS_DEBUG') > 1:
						indah4(f"""[processor|save_variables] #3 updating Common.temporary_dict\nfrom singkat: {singkat} to panjang: {panjang}\nitem =\n{tree.pretty()}""", warna='magenta')
					Common.temporary_dict.update({ singkat: panjang, })

				if env_int('ULIBPY_FMUS_DEBUG') > 1:
					indah4(f'[processor|save_variables] #4 updating COMMONDICT jadi: [{Common.temporary_dict}]', warna='yellow')

				# utk save variables kita tidak masukkan ke counter...
				# atau counter kita bikin sama
				self.run_configuration['counter'] -= 1 # agar counter tidak increment

				common_args = {
					'name'				:'simpan_temp_vars',
					'singkat_panjang'	: singkat_panjang,
					'singkat'			: singkat,
					'panjang'			: panjang,
					'old_panjang_sebelum_replace_from_configuration': old_panjang_sebelum_replace_from_configuration,
					'variables'			: {singkat:panjang},
					'counter'			: -1, #run_configuration['counter'],
					'type'				:'simpan_temp_vars', 
					'original'			: code,
					'workdir'			: workdir, 
					'level'				: parentLevel
				}

				if has_text_oper:
					textopers = tree.children[2]
					operations = [textoper.data for textoper in textopers.children]
					common_args.update({
						'text_operations' : operations
					})
					# agar __TABLENAME_LOWER__ bisa dipake utk namafile
					if len(operations)==1 and operations[0] == 'modelify':
						base = singkat.removesuffix('__')
						newdict_for_modelify = {}
						newdict_for_modelify[base + '_LOWER__'] = panjang.lower()
						newdict_for_modelify[base + '_UPPER__'] = panjang.upper()
						newdict_for_modelify[base + '_PLURAL__'] = panjang + 's'
						newdict_for_modelify[base + '_PLURAL_LOWER__'] = panjang.lower() + 's'
						newdict_for_modelify[base + '_PLURAL_UPPER__'] = panjang.upper() + 's'
						newdict_for_modelify[base + '_PLURAL_CAP__'] = panjang.capitalize() + 's'
						newdict_for_modelify[base + '_CASE__'] = panjang.capitalize()
						newdict_for_modelify[base + '_CAP_PLURAL__'] = panjang.capitalize() + 's'
						common_args['variables'].update(newdict_for_modelify)
						Common.temporary_dict.update(newdict_for_modelify)
				if is_debugging:
					indah4(f"[processor|save_variables] #5 selesai handle % (save_variables) common_args={json.dumps(common_args, indent=4)}", warna='green')
				if ParentNode:
					common_args.update({
						'parent' : ParentNode
					})

				NewNode = AnyNode(**common_args)

			elif tree.data == 'system_operation_type':
				nama_operasi = str(tree.children[0])
				# nama operasi: $something bla bla __TEMPLATE juga hrs dihandle
				nama_operasi = Common.replace_me(nama_operasi)
				# utk rujuk $notepad __TEMPLATES__/whatever.txt
				# nama_operasi.replace('__TEMPLATES__', run_configuration['templatesdir'])
				# kita rujuk ke filemanager.py: run_configuration['replacer']
				if is_debugging:
					indah0(f"[processor] system_operation_type ($) nama operasi pre = {nama_operasi}", warna='white', bold=True, newline=True)

				for k,v in self.run_configuration['replacer'].items():
					if not isinstance(v, str):
						'''
						__PROCESS_FILES
						__PROCESS_STRINGS
						__PROCESS_COMMAS
						'''
						v = str(v)
					nama_operasi = nama_operasi.replace(k, v)

				# biar spt @ bisa gunakan __PWD
				nama_operasi = nama_operasi.replace('__PWD__', workdir)
				nama_operasi = nama_operasi.replace('__PWD', workdir)

				if is_debugging:
					indah0(f"[processor] system_operation_type ($) nama operasi post = {nama_operasi}", warna='white', bold=True, newline=True)

				if not ParentNode:
					NewNode = AnyNode(name='sysop',
						type='sysop_command',
						counter=self.run_configuration['counter'],
						command=nama_operasi, 
						original=code,
						workdir=normy(workdir),
						level=parentLevel)
				else:
					NewNode = AnyNode(name='sysop',
						type='sysop_command',
						counter=self.run_configuration['counter'],
						command=nama_operasi,
						original=code,
						workdir=normy(workdir),
						level=parentLevel, 
						parent=ParentNode)

			elif tree.data == 'special_command':
				"""
				&nama_operasi ?
				"""
				nama_operasi = str(tree.children[0])

				# self.debug('a) special_command, nama_operasi = command = ', nama_operasi)
				nama_operasi = Common.replace_me(nama_operasi)
				# self.debug('b) special_command, nama_operasi = command = ', nama_operasi)
				for k,v in self.run_configuration['replacer'].items():
					if is_debugging:
						self.debug(f'[processor] * replacing {k} dengan {v}', warna='white', newline=True)
					nama_operasi = nama_operasi.replace(k, v)
				# self.debug('c) special_command, nama_operasi = command = ', nama_operasi)

				cmd_params = {
					'name'			: 'special_command',
					'type'			: 'special_command',
					'counter' 		: self.run_configuration['counter'],
					'replacer'		: self.run_configuration['replacer'],
					'command'		: nama_operasi,
					'original'		: code,
					'workdir'		: workdir,
					'level'			: parentLevel
				}
				if ParentNode:
					cmd_params.update({
						'parent'	: ParentNode
					})

				NewNode = AnyNode(**cmd_params)

			elif tree.data == 'quick_command':
				"""
				/perintah
				"""
				nama_operasi = str(tree.children[0])
				if is_debugging:
					print(f'''[processor][quick_command] #1 nama_operasi = [{nama_operasi}]''')
				nama_operasi = Common.replace_me(nama_operasi)
				if is_debugging:
					print(f'''[processor][quick_command] #2 nama_operasi = [{nama_operasi}]''')
				for k,v in self.run_configuration['replacer'].items():
					if is_debugging:
						self.debug(f'[processor] * replacing {k} dengan {v}', warna='white', newline=True)
					try:
						if not isinstance(v, str):
							v = str(v)
						nama_operasi = nama_operasi.replace(k, v)
					except Exception as err:
						print(f'''[processor][quick_command]
						err {err}
						k {k}
						v {v}
						''')
				# print(f'''[processor][quick_command] #3 nama_operasi = [{nama_operasi}]''')
				cmd_params = {
					'name'			: 'quick_command',
					'type'			: 'quick_command',
					'counter' 		: self.run_configuration['counter'],
					'replacer'		: self.run_configuration['replacer'],
					'command'		: nama_operasi,
					'original'		: code,
					'workdir'		: workdir,
					'level'			: parentLevel
				}
				if ParentNode:
					cmd_params.update({
						'parent'	: ParentNode
					})
				NewNode = AnyNode(**cmd_params)

			elif tree.data == 'request_operation_from_user':
				if not ParentNode:
					NewNode = AnyNode(name='sysop',
						type='user_command',
						counter=self.run_configuration['counter'],
						original=code,
						workdir=normy(workdir),
						level=parentLevel)
				else:
					NewNode = AnyNode(name='sysop',
						type='user_command',
						counter=self.run_configuration['counter'],
						original=code,
						workdir=normy(workdir),
						level=parentLevel, 
						parent=ParentNode)

			elif tree.data == 'filename':
				namafile = str(tree.children[0])
				# UPDATE
				# kita kasih __AT__ utk @ krn bentrok dg pesan-instruksi
				# namafile = namafile.replace('__AT__', '@').replace('__AT', '@')
				namafile = decode_filename(namafile)
				# step 1: cek nama ada di %variables
				if is_debugging:
					self.debug('[processor] cek %variables ==> namafile sblm replace:', namafile, '\n')
				#utk simpan nama lama jk nama file direplace dari %variables
				old_name=namafile
				namafile = Common.replace_me(namafile)

				if is_debugging:
					self.debug('[processor] cek %variables ==> namafile stlh replace:', namafile)
					self.debug(f'\n-------------- [processor] filename pre: {namafile} -------------->>\n')

				# step 2: cek nama ada di replacer (boleh dong __CURDIR__,d dst)
				replacer_output = self.run_configuration['replacer']
				if env_int('ULIBPY_FMUS_DEBUG') < 2:
					replacer_output = str(replacer_output)[:500] + '...(snip)'
				if is_debugging:
					self.debug('[processor] config replacer =', replacer_output)
					self.debug('[processor] cek config replacer ==> namafile sblm replace:', namafile, '\n')

				namafile = self.replace_me(namafile)
				# di sini kita normy kan dulu, krn terkadang hasilkan c:\work\oprek/nxblog
				# dan nxblog malah menjadi file..
				namafile = normy(namafile)

				if is_debugging:
					self.debug('[processor] cek config replacer ==> namafile stlh replace:', namafile)
					self.debug(f'\n-------------- [processor] filename post: {namafile} -------------->>\n\n')

				# cek ada __INPUT__
				# jk ya, minta di sini
				# hindari circular import
				# DONT
				# krn jadi "static", jk dalam while, sudah gak pernah dipanggil lagi
				# from schnell.app.fmusutils import get_input_generic
				# namafile = get_input_generic(namafile)

				workdir = workdir + ('/' if workdir else '') + namafile

				if namafile == '/':
					'''
					/,d akan setara .,d ?
					krn workdir dimulai dg projectdir
					projectdir sendiri akan diisi dari config.json
					atau dari __CURDIR__ set dir/file template wkt instantiate Fmus
					'''
					workdir = self.run_configuration['projectdir']
					NewNode = AnyNode(name=namafile,
						old_name=old_name,
						type='dir',
						original=code,
						counter=self.run_configuration['counter'],
						workdir=normy(workdir),
						level=parentLevel)

				elif namafile == '.':
					workdir = self.run_configuration['projectdir']
					if ParentNode:
						NewNode = AnyNode(name=namafile,
							old_name=old_name,
							type='dir',
							original=code,
							parent=ParentNode,
							counter=self.run_configuration['counter'],
							# jk punya parent maka workdir sama dg parent
							workdir=normy(workdir),
							level=parentLevel)
					else:
						NewNode = AnyNode(name=namafile,
							old_name=old_name,
							type='dir',
							original=code,
							counter=self.run_configuration['counter'],
							workdir=normy(workdir),
							level=parentLevel)

						if env_int('ULIBPY_FMUS_DEBUG')>1:
							self.debug('[s.a.f.processor] NewNode created utk dot fmus entry:', NewNode)

				elif namafile .startswith('/') or (is_windows() and is_windows_drive(namafile)):
					'''
					jk user specify lokasi absolute: /home/usef/projects/kerja
					+update: utk windows, jk namafile: c:... blm handle utk d:... dst.
					+TODO: handle char utk drive: d..z.
					di sini, workdir sudah diset ke namafile
					kita set projectdir agar di akhir, command tree projectdir juga ngarah ke lokasi abs yg diset
					'''
					# old_projectdir = self.run_configuration['projectdir']
					workdir = namafile
					if is_windows():
						if platform() == 'wsl':
							workdir = linuxify(namafile)
						elif platform() == 'termux':
							workdir = normy(namafile)
						else:
							workdir = windowsify(namafile)

					if is_debugging:
						indah4(f"[processor:process_folderline|filename] {namafile} dimulai dg / atau c:\\, workdir = {workdir} ", warna='yellow')
					# input('...press any key')

					self.run_configuration['projectdir'] = workdir
					# indah4(f"[processor/process_folderline] #2 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='yellow')

					# indah4(f"setting new projectdir ke {self.run_configuration['projectdir']} dari {old_projectdir}", warna='magenta')					

					NewNode = AnyNode(name=workdir,
						old_name=old_name,
						type='dir',
						counter=self.run_configuration['counter'],
						original=code,
						workdir=normy(workdir),
						level=parentLevel,
						# update: kita paksa /tmp/something bisa berada di bawah /home/something
						parent=ParentNode,
						)
				else:
					NewNode = AnyNode(name=namafile,
						old_name=old_name,
						parent=ParentNode,
						counter=self.run_configuration['counter'],
						original=code,
						workdir=normy(workdir),
						level=parentLevel)

			elif tree.data == 'filetype':
				tipefile = tree.children[0].data # file atau dir
				NewNode.type = tipefile

			elif tree.data == 'komentar_dari_template':
				'''
				insn
					komentar_dari_template
						komentar_kunci        file_komentar
						komentar_baris        contoh/komentar
				'''
				anak1 = tree.children[0]
				anak2 = tree.children[1]
				nilai_singkat = str(anak1.children[0]) # kunci ke root_tree.variables atau temporary_dict
				# nilai_baris = anak2.data # 'Token' object has no attribute 'data'
				nilai_baris = str(anak2.children[0])
				if nilai_singkat in Common.temporary_dict:				
					template_file = Common.temporary_dict[nilai_singkat]
					# entries = BaseDefinitor.manual_list_grep(nilai_baris, template_file, kunci='--')
					entries = Common.list_grep(nilai_baris, template_file)
					if entries:
						if len(entries) == 1:
							hasil = entries[0]
							# comment = BaseDefinitor.manual_definisi(hasil, template_file, kunci='--')
							comment = Common.definisi(hasil, template_file)
							if not ParentNode:
								NewNode = AnyNode(name='info',
									source=template_file,
									counter=self.run_configuration['counter'],
									baris=nilai_baris, 
									type='komentar_untuk_instruksi_selanjutnya',
									content=comment, 
									original=code,
									workdir=normy(workdir),
									level=parentLevel)
							else:
								NewNode = AnyNode(name='info',
									source=template_file,
									counter=self.run_configuration['counter'],
									baris=nilai_baris,
									type='komentar_untuk_instruksi_selanjutnya',
									content=comment, 
									original=code,
									workdir=normy(workdir),
									level=parentLevel, 
									parent=ParentNode)

			elif tree.data == 'pesan_instruksi_dari_template':
				'''
				ikuti komentar_dari_template
				@(filename=baris_cari)
				@(utama_is_template_file_in_temporary_dict=baris_cari)
				'''
				from schnell.app.fmusutils import replace_from_configuration # supaya tdk circular import
				anak1 = tree.children[0]
				anak2 = tree.children[1]
				template_file = str(anak1.children[0])
				cari_baris = str(anak2.children[0])
				# harus ijinkan juga dari absolute path
				# skrg ini filetemplate hrs dari save_variable

				# self.debug('pesan_instruksi_dari_template, template_file #1', template_file)
				if template_file in Common.temporary_dict:
					template_file = Common.temporary_dict[template_file]
				# self.debug('pesan_instruksi_dari_template, template_file #2', template_file)

				# biar tertib gunakan fmusutils
				# for k,v in self.run_configuration['replacer'].items():
				# 	# self.debug('try replacing:', k)
				# 	template_file = template_file.replace(k, v)
				template_file = replace_from_configuration(template_file, self.run_configuration)
					
				forced_entry = False
				if isfile(template_file):
					# di sini kita tambah cari_baris bisa diakhiri * utk forced_entry
					if cari_baris.endswith('*'):
						cari_baris = cari_baris[:-1]
						forced_entry = True
					entries = Common.list_grep(cari_baris, template_file)
					if entries:
						# harus ijinkan juga peroleh multiple entries ambil yg min key=len
						if len(entries) == 1:
							hasil = entries[0]
							comment = Common.definisi(hasil, template_file)
							params = {
								'name':			'pesan',
								'type':			'pesan_instruksi_selanjutnya',
								'source':		template_file,
								'counter':		self.run_configuration['counter'],
								'baris':		cari_baris,
								'forced_entry': forced_entry,
								'content':		comment, 
								'original':		code,
								'workdir':		workdir, 
								'level':		parentLevel
							}
							if ParentNode:
								params.update({
									'parent': 	ParentNode
								})
							NewNode = AnyNode(**params)

			elif tree.data == 'fileoperation':  # fileoperation: "(" file_dir_operation_type ("," file_dir_operation_type)* ")"
				'''
				ada top level insn:
				filename "," filetype fileoperation?
				"$" system_operation_type
				..
				fileoperation punya anak file_dir_operation_type:
				fileoperation: "(" file_dir_operation_type ("," file_dir_operation_type)* ")"
				fileoperation										tree
					file_dir_operation_type					operasi
						file_operation_type							operasi.children[0]
						dir_operation_type							operasi.children[1]
						operation_attributes						operasi.children[2]
				'''
				operations = []

				for operasi in tree.children:  # file_dir_operation_type

					operasi_type_tree = operasi.children[0]
					operasi_type = operasi_type_tree.data # dirop: copy_dir_from, fileop: input_from_user_with_prompt
					
					if operasi_type == 'operation_attributes':  # file operation

						operation_attributes = operasi_type_tree

						for attr in operation_attributes.children:
							'''
							operation_attributes: operation_attr // ("," operation_attr)*
							'''

							if attr.data == 'binary_file_operation':  # @b
								NewNode.binary_mode = True

							elif attr.data == 'appending_mode':  # @a
								NewNode.appending_mode = True

							elif attr.data == 'tab_to_space':  # @ts
								NewNode.tab_to_space = True

							elif attr.data == 'insert_before':  # @ib...
								# ambil line indicator
								# | "ib" "=" singkat "=" HURUF_FOLDER_LAMA -> insert_before
								# children0.children0 = singkat
								# children1 = HURUF_FOLDER_LAMA -> line_indicator
								# berarti attr = insert_before dan HURUF_FOLDER_LAMA = children[0] adlh lark.lexer.Token
								if hasattr(attr, 'children') and len(attr.children) == 2:
									line_content = str(attr.children[0].children[0])
									line_indicator = self.sanitize_prohibited_chars(str(attr.children[1]))
									NewNode.insert_replace = 1 # 1 = ib, 2 = ia, 3 = ra, 4 = rf
									NewNode.line_indicator = line_indicator
									NewNode.line_content = line_content

							elif attr.data == 'insert_after':  # @ia...
								if hasattr(attr, 'children') and len(attr.children) == 2:
									line_content = str(attr.children[0].children[0])
									line_indicator = self.sanitize_prohibited_chars(str(attr.children[1]))
									NewNode.insert_replace = 2 # 1 = ib, 2 = ia, 3 = ra, 4 = rf
									NewNode.line_indicator = line_indicator
									NewNode.line_content = line_content

							elif attr.data == 'replace_at':  # @ra...
								if hasattr(attr, 'children') and len(attr.children) == 2:
									line_content = str(attr.children[0].children[0])									
									line_indicator = self.sanitize_prohibited_chars(str(attr.children[1]))
									# self.debug(f"line content utk replace at [{line_indicator}]...\n")
									# input('.........................')
									NewNode.insert_replace = 3 # 1 = ib, 2 = ia, 3 = ra, 4 = rf
									NewNode.line_indicator = line_indicator
									NewNode.line_content = line_content

							elif attr.data == 'replace_from':  # @rf
								if hasattr(attr, 'children') and len(attr.children) == 2:
									line_content = str(attr.children[0].children[0])
									line_indicator = self.sanitize_prohibited_chars(str(attr.children[1]))
									NewNode.insert_replace = 4 # 1 = ib, 2 = ia, 3 = ra, 4 = rf
									NewNode.line_indicator = line_indicator
									NewNode.line_content = line_content

							elif attr.data == 'remove_lines':  # @rm
								if hasattr(attr, 'children') and len(attr.children) == 2:
									jumlah_hapus = str(attr.children[0].children[0]) # jumlah hapus
									line_indicator = str(attr.children[1])
									NewNode.insert_replace = 5 # 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
									NewNode.line_indicator = line_indicator
									NewNode.line_content = jumlah_hapus
									NewNode.jumlah_hapus = jumlah_hapus

							elif attr.data == 'replace_entry':  # @re
								'''
								| "re" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_entry
								singkat adlh baris_cari utk pengganti/replacer = children[0]
								kita sebut line_content

								MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE adlh string replacee = children[1]
								kita sebut line_indicator

								baiknya kita sebut 
								newline/target/destination dan oldline/source
								atau
								newstr dan oldstr
								'''
								if hasattr(attr, 'children') and len(attr.children) == 2:
									line_content = str(attr.children[0].children[0])
									line_indicator = self.sanitize_prohibited_chars(str(attr.children[1]))
									# 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
									# 6 = replace_entry, 7 = replace_between
									NewNode.insert_replace = 6
									NewNode.line_indicator = line_indicator # pattern to search in orig file
									NewNode.line_content = line_content # singkat, baris_entry

							elif attr.data == 'replace_between':  # @rb
								if hasattr(attr, 'children') and len(attr.children) == 3:
									line_content = str(attr.children[0].children[0])
									line_indicator = self.sanitize_prohibited_chars(str(attr.children[1]))
									line_indicator_end = str(attr.children[2])
									# 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
									# 6 = replace_entry, 7 = replace_between
									NewNode.insert_replace = 7
									NewNode.line_indicator = line_indicator
									NewNode.line_indicator_end = line_indicator_end
									NewNode.line_content = line_content

							elif attr.data == 'replace_string':  # @rs
								string_new = self.sanitize_prohibited_chars(str(attr.children[0]))
								string_old = self.sanitize_prohibited_chars(str(attr.children[1]))
								# 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
								# 6 = replace_entry, 7 = replace_between
								# 8 = replace_string dlm file = myfile.txt,f(f,@rs="baru"="lama")
								NewNode.insert_replace = 8
								NewNode.string_new = string_new
								NewNode.string_old = string_old
								# ini sekedar agar di proses generator dan seragam
								# sewaktu dir/file operation: load_from_file
								NewNode.line_content = string_new
								NewNode.line_indicator = string_old

							elif attr.data == 'replace_content':  # @rc
								'''
								| "rc" "=" singkat -> replace_content // whole file replace
								'''
								if hasattr(attr, 'children') and len(attr.children) == 1:
									line_content = str(attr.children[0].children[0])
									# line_indicator = '' # self.sanitize_prohibited_chars(str(attr.children[1]))
									NewNode.insert_replace = 9 # InsertReplace.ReplaceContent
									NewNode.line_indicator = ''
									NewNode.line_content = line_content

							elif attr.data == 'commenting_file':  # @cf
								# | "cf"
								# "=" 
								# "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" 
								# "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> commenting_file
								# indah4('[processor] commenting file', warna='yellow')
								if hasattr(attr, 'children') and len(attr.children) == 2:
									simbol_komentar = token(attr)
									baris_untuk_dikomentari = self.sanitize_prohibited_chars(token(attr, 1))
									# baris_cari_komentar = str(attr.children[2])
									# 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
									# 6 = replace_entry, 7 = replace_between
									NewNode.insert_replace = 10
									NewNode.line_indicator = baris_untuk_dikomentari
									NewNode.line_content = simbol_komentar

							elif attr.data == 'insert_at':  # @iA
								'''
								| "iA" "=" singkat "=" BILBUL_BERTANDA -> insert_at // f=capcay.txt,iA=barisentry=-1
								'''
								if hasattr(attr, 'children') and len(attr.children) == 2:
									baris_entry = str(attr.children[0].children[0]) # jumlah hapus
									linenumber_lokasi_insert = str(attr.children[1])
									NewNode.insert_replace = 11 # 1 = ib, 2 = ia, 3 = ra, 4 = rf, 5 = remove lines
									NewNode.line_indicator = baris_entry
									NewNode.line_content = linenumber_lokasi_insert

							elif attr.data == 'excluding_in_copy': # (@x[tmp*,lock*,*error*,__pycache__])
								patterns = []
								for pat in attr.children:
									if pat.data == 'pattern':
										pola = str(pat.children[0])
										patterns .append(pola)
								NewNode.patterns = patterns # patterns=['*.txt', '*.tmp']

							elif attr.data == 'fileops_line_expression':
								'''
								for operasi in tree.children:  # file_dir_operation_type
									operasi_type_tree = operasi.children[0]
									operasi_type = operasi_type_tree.data # dirop: copy_dir_from, fileop: input_from_user_with_prompt				
									if operasi_type == 'operation_attributes':  # file operation
										operation_attributes = operasi_type_tree
										for attr in operation_attributes.children:
								tree
									operasi
										operasi_type_tree
											attr
								@line=1,2,3|i+|(aku cuma)
								insn
									filename      contoh.txt
									filetype
										file
									fileoperation
										file_dir_operation_type
											touch_file
										file_dir_operation_type
											operation_attributes
												fileops_line_expression					<- attr
													line_expression
														line_item
															line_number       1
														line_item
															line_number       2
														line_item
															line_number       3
													line_insert_after
													line_data_literal     aku cuma
								@line>(find me goose)|i+|(aku cuma)
								'''
								print(attr.pretty())
								NewNode.fileops_operation = attr.data
								line_expression, line_operation, line_data = attr.children
								# line_expression punya anak...
								indah4(str(line_expression), layar='yellow')
								line_expr_children = []
								if len(line_expression.children):
									for line_expr_child in line_expression.children:
										indah4(line_expr_child.data, layar='green')
										if line_expr_child.data == 'line_item':											
											line_item_child = str(line_expr_child.children[0].children[0])
											# indah4(f"line_item_child={line_item_child}", layar='blue')
											line_expr_children.append(line_item_child)
								jenis_data = 'line_data_literal'  # default
								data_untuk_digunakan = token(line_data)
								if line_data.data == 'line_data_filepath':
									jenis_data = 'line_data_filepath'
								elif line_data.data == 'line_data_fmus':
									jenis_data = 'line_data_fmus'
									data_untuk_digunakan += '=' + str(line_data.children[1])
								elif line_data.data == 'line_data_input':
									jenis_data = 'line_data_input'
								elif line_data.data == 'line_data_url':
									jenis_data = 'line_data_url'
								NewNode.fileops_attributes = {
									'line_operation': line_operation.data,
									'line_data': data_untuk_digunakan,
									'data_type': jenis_data,
									'line_query': line_expr_children, # token(line_expression),
								}
								# _ = input('fileops_line_expression: ')

							elif attr.data == 'fileops_line_contains':
								NewNode.fileops_operation = attr.data
								NewNode.fileops_attributes = {}
								line_query, line_operation, line_data = attr.children
	# 							indah4(f"""fileops_line_contains
	# line_query		= {line_query}
	# line_operation	= {line_operation}
	# line_data		= {line_data}
	# attr.children	= {attr.children}
	# """, warna='blue')
								jenis_data = 'line_data_literal'  # default
								data_untuk_digunakan = token(line_data)
								if line_data.data == 'line_data_filepath':
									jenis_data = 'line_data_filepath'
								elif line_data.data == 'line_data_fmus':
									jenis_data = 'line_data_fmus'
									# di generator, line_data diharapkan berisi file=entry
									# processing_data = item.fileops_attributes['line_data']
									# processing_data = get_definition_fmusfile_barisentry(processing_data)
									data_untuk_digunakan += '=' + str(line_data.children[1])
								elif line_data.data == 'line_data_input':
									jenis_data = 'line_data_input'
								elif line_data.data == 'line_data_url':
									jenis_data = 'line_data_url'
								NewNode.fileops_attributes = {
									'line_operation': line_operation.data,
									'line_data': data_untuk_digunakan,
									'data_type': jenis_data,
									'line_query': token(line_query),
								}

							elif attr.data == 'fileops_line_matches':
								NewNode.fileops_operation = attr.data
								# NewNode.fileops_attributes = {}
								line_query, line_operation, line_data = attr.children
								jenis_data = 'line_data_literal'
								data_untuk_digunakan = token(line_data)
								if line_data.data == 'line_data_filepath':
									jenis_data = 'line_data_filepath'
								elif line_data.data == 'line_data_fmus':
									jenis_data = 'line_data_fmus'
									data_untuk_digunakan += '=' + str(line_data.children[1])
								elif line_data.data == 'line_data_input':
									jenis_data = 'line_data_input'
								elif line_data.data == 'line_data_url':
									jenis_data = 'line_data_url'
								NewNode.fileops_attributes = {
									'line_operation': line_operation.data,
									'line_data': data_untuk_digunakan,
									'data_type': jenis_data,
									'line_query': token(line_query),
								}

							elif attr.data == 'fileops_line_between_contains':
								NewNode.fileops_operation = attr.data
								NewNode.fileops_attributes = {}
								marker_start, marker_end, line_operation, line_data = attr.children
								jenis_data = 'line_data_literal'
								data_untuk_digunakan = token(line_data)
								if line_data.data == 'line_data_filepath':
									jenis_data = 'line_data_filepath'
								elif line_data.data == 'line_data_fmus':
									jenis_data = 'line_data_fmus'
									data_untuk_digunakan += '=' + str(line_data.children[1])
								elif line_data.data == 'line_data_input':
									jenis_data = 'line_data_input'
								elif line_data.data == 'line_data_url':
									jenis_data = 'line_data_url'
								NewNode.fileops_attributes = {
									'line_operation': line_operation.data,
									'line_data': data_untuk_digunakan,
									'data_type': jenis_data,
									'line_query_start': token(marker_start),
									'line_query_end': token(marker_end),
								}

							elif attr.data == 'fileops_line_between_matches':
								'''
								insn
								filename      contoh5.txt
								filetype
									file
								fileoperation
									file_dir_operation_type
									operation_attributes
										fileops_line_between_matches
											line_regex    start regex
											line_regex    end regex
											line_insert_after
											line_data_literal     aku cuma
								'''								
								NewNode.fileops_operation = attr.data
								marker_start, marker_end, line_operation, line_data = attr.children
								jenis_data = 'line_data_literal'
								data_untuk_digunakan = token(line_data)
								if line_data.data == 'line_data_filepath':
									jenis_data = 'line_data_filepath'
								elif line_data.data == 'line_data_fmus':
									jenis_data = 'line_data_fmus'
									data_untuk_digunakan += '=' + str(line_data.children[1])
								elif line_data.data == 'line_data_input':
									jenis_data = 'line_data_input'
								elif line_data.data == 'line_data_url':
									jenis_data = 'line_data_url'
								NewNode.fileops_attributes = {
									'line_operation': line_operation.data,
									'line_data': data_untuk_digunakan,
									'data_type': jenis_data,
									'line_query_start': token(marker_start),
									'line_query_end': token(marker_end),
								}

							elif attr.data == 'fileops_string_at':
								'''
								fileops_string_at
									string_matches        GANTI AKU DONG
									string_replace_at
									string_data_literal   aku ganti dirimu yang jelek itu
								'''
								NewNode.fileops_operation = attr.data
								NewNode.fileops_attributes = {}
								string_matches, string_operation, string_data = attr.children
								jenis_data = 'string_data_literal'
								data_untuk_digunakan = token(string_data)
								if string_data.data == 'string_data_filepath':
									jenis_data = 'string_data_filepath'
								elif string_data.data == 'string_data_fmus':
									jenis_data = 'string_data_fmus'
									data_untuk_digunakan += '=' + str(string_data.children[1])
								elif string_data.data == 'string_data_input':
									jenis_data = 'string_data_input'
								elif string_data.data == 'string_data_url':
									jenis_data = 'string_data_url'
								NewNode.fileops_attributes = {
									'string_query': token(string_matches),
									'string_operation': string_operation.data,
									# 'string_data': token(string_data),
									'string_data': data_untuk_digunakan,
									'data_type': jenis_data,
								}

							elif attr.data == 'fileops_string_after':
								NewNode.fileops_operation = attr.data
								NewNode.fileops_attributes = {}
								string_matches, string_operation, string_data = attr.children
								jenis_data = 'string_data_literal'
								data_untuk_digunakan = token(string_data)
								if string_data.data == 'string_data_filepath':
									jenis_data = 'string_data_filepath'
								elif string_data.data == 'string_data_fmus':
									jenis_data = 'string_data_fmus'
									data_untuk_digunakan += '=' + str(string_data.children[1])
								elif string_data.data == 'string_data_input':
									jenis_data = 'string_data_input'
								elif string_data.data == 'string_data_url':
									jenis_data = 'string_data_url'
								NewNode.fileops_attributes = {
									'string_query': token(string_matches),
									'string_operation': string_operation.data,
									# 'string_data': token(string_data),
									'string_data': data_untuk_digunakan,
									'data_type': jenis_data,
								}

							elif attr.data == 'fileops_string_before':
								NewNode.fileops_operation = attr.data
								NewNode.fileops_attributes = {}
								string_matches, string_operation, string_data = attr.children
								jenis_data = 'string_data_literal'
								data_untuk_digunakan = token(string_data)
								if string_data.data == 'string_data_filepath':
									jenis_data = 'string_data_filepath'
								elif string_data.data == 'string_data_fmus':
									jenis_data = 'string_data_fmus'
									data_untuk_digunakan += '=' + str(string_data.children[1])
								elif string_data.data == 'string_data_input':
									jenis_data = 'string_data_input'
								elif string_data.data == 'string_data_url':
									jenis_data = 'string_data_url'
								NewNode.fileops_attributes = {
									'string_query': token(string_matches),
									'string_operation': string_operation.data,
									# 'string_data': token(string_data),
									'string_data': data_untuk_digunakan,
									'data_type': jenis_data,
								}

					elif operasi_type == 'load_program_from':
						file_value = str(operasi_type_tree.children[0])
						line_value = str(operasi_type_tree.children[1])
						# dahului = agar: load_program_from=filevalue=linevalue
						# operasi_value = f"={file_value}={line_value}"
						if is_debugging:
							self.debug(f"[processor] load_program_from={file_value}={line_value}\n")
							self.debug(f"[processor] load_program_from NewNode sekarang adlh: [{NewNode}]\noriginal [{code}].\n")
							self.debug(f"[processor] load_program_from ParentNode adlh: [{ParentNode}]\n")
						operations.append(f"load_program_from={file_value}={line_value}")

					elif operasi_type == 'grep_within_directory':
						print(operasi.pretty())
						print(operasi_type_tree.pretty())
						grep_query = token(operasi_type_tree)
						operations.append(f"grep={grep_query}")
						# input('[processor] Press any key to process grep_within_directory')

					elif operasi_type == 'find_within_directory':
						print(operasi.pretty())
						print(operasi_type_tree.pretty())
						grep_query = token(operasi_type_tree)
						operations.append(f"find={grep_query}")

					elif operasi_type == 'remove_within_directory':
						print(operasi.pretty())
						print(operasi_type_tree.pretty())
						grep_query = token(operasi_type_tree)
						operations.append(f"rm={grep_query}")

					else:
						'''
						kita tambah baru
						insn
							filename      aku_bukan_pengemis_cinta.js
							filetype
								file
							fileoperation
								file_dir_operation_type
									ambil_entry_dari_file_template
										singkat template
										cari1024
						insn
							filename      Palsu.js
							filetype
								file
							fileoperation
								file_dir_operation_type
									load_from_file_absolute   /tmp/kepalsuan
						insn
							filename      StripeCheckout.js
							filetype
								file
							fileoperation
								file_dir_operation_type							-> operasi_type
									paste_from_clipboard_with_pause
						oper: ambil_entry_dari_file_template=Tree('singkat', [Token('HURUF', 'template')])
							operasi_value
							=Tree('singkat', [Token('HURUF', 'template')])
							if isinstance(child, lark.tree.Tree):
						oper: paste_from_clipboard_with_pause
						'''
						operasi_value = None

						if len(operasi.children[0].children) > 0:

							maybe_operasi_value = operasi.children[0].children[0]  # a\n\tb\n\n<maybe_operasi_value>

							if is_debugging:
								self.debug('\n[processor] fileoperation/file_dir_operation_type/utama/child0:', maybe_operasi_value, '\n')

							# if isinstance(maybe_operasi_value, lark.tree.Tree) and len(operasi.children[0].children)>1:
							if operasi.children[0].data == 'ambil_entry_dari_file_template':
								'''
								bentuk:
								e=file_template=cari_baris
								'''
								mk_filepath = maybe_operasi_value.children[0]
								file_template = str(mk_filepath)
								cari_baris = str(operasi.children[0].children[1])
								# dict ini jadi str krn akan di-ast.literal_eval di ambil_entry*.py
								operasi_value = str({file_template:cari_baris})

							elif operasi.children[0].data == 'ambil_entry_codegen':
								'''
								bentuk:
								"cg" langchoice? "=" singkat_folder "=" HURUF_FOLDER_NEXTJS

								cg=file_template=cari_baris
								   ^anak0			   ^anak1		tree ambil_entry_codegen punya 2 anak
								cg[java]=file_template=cari_baris
								  ^anak0 ^anak1			   ^anak2	tree ambil_entry_codegen punya 3 anak
								cg[scala]=file_template=cari_baris
								'''
								baris_cg = operasi.children[0]
								if len(baris_cg.children) == 2:
									'''
									cg=file_template=cari_baris
									'''
									langchoice = 'py' # hardcoded for now
									singkat_folder_wrap = baris_cg.children[0]
									cari_baris_unwrap = baris_cg.children[1]
								else:
									'''
									cg[java]=file_template=cari_baris
									'''
									# jangan lupa str() kan krn ini adlh Token object
									langchoice = str(baris_cg.children[0].children[0])
									singkat_folder_wrap = baris_cg.children[1]
									cari_baris_unwrap = baris_cg.children[2]

								singkat_folder_unwrap = singkat_folder_wrap.children[0]
								# mk_filepath = maybe_operasi_value.children[0]
								# mk_filepath = singkat_folder_unwrap
								file_template = str(singkat_folder_unwrap)
								cari_baris = str(cari_baris_unwrap)
								operasi_value = str({file_template:cari_baris})
								operasi_value = str({file_template:cari_baris, 'langchoice':langchoice})
								NewNode.operations_langchoice = langchoice

							elif operasi.children[0].data == 'ambil_replify_here':
								'''
								| "code" langchoice "=" ISI_FILE_TERMASUK_KOMA_TAMBAH_PERSEN -> ambil_replify_here
								'''
								pohon = operasi.children[0]
								langchoice = str(pohon.children[0].children[0])
								codecontent = str(pohon.children[1])
								NewNode.operations_codecontent = codecontent
								NewNode.operations_langchoice = langchoice

							elif operasi.children[0].data == 'ambil_terdekod_dari_file_template':
								'''
								ambil_terdekod_dari_file_template
								b64=file_template=cari_baris_berisi_data_terencode_base64
								sementara ini sama dg ambil_entry_dari_file_template
								'''
								singkat = maybe_operasi_value.children[0]
								file_template = str(singkat)
								cari_baris = str(operasi.children[0].children[1])
								operasi_value = str({file_template:cari_baris})

							elif operasi.children[0].data in ['query_specific_llm', 'query_specific_llm_for_code', 'query_active_llm_from_fmus']:
								'''
								| "q" ":" HURUF "="	ISI_CONTENT_FILE_BISA_URL 		-> query_specific_llm
								| "qc" ":" HURUF "="	ISI_CONTENT_FILE_BISA_URL	-> query_specific_llm_for_code
								| "Q" "=" singkat_folder "=" HURUF_FOLDER_NEXTJS	-> query_active_llm_from_fmus
								'''
								llm_provider = str(operasi.children[0].children[0])
								query_content = str(operasi.children[0].children[1])

								# operasi_value = str({fmus_file:baris_entry}) # utk query_active_llm_from_fmus
								if operasi.children[0].data == 'query_active_llm_from_fmus':
									# llm_provider = Tree('singkat_folder', [Token('HURUF_FOLDER_LAMA', 'coba.fmus')])
									llm_provider = operasi.children[0].children[0]
									llm_provider = str(llm_provider.children[0])

								operasi_value = str({llm_provider:query_content})

							elif operasi.children[0].data in ['query_specific_llm_from_fmus']: # ada 3 anak
								'''
								| "Q" ":" HURUF "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 		-> query_specific_llm_from_fmus
								'''
								# oper = query_active_llm_from_fmus={"Tree('singkat_folder', [Token('HURUF_FOLDER_LAMA', 'coba.fmus')])": 'tugas-1'}
								llm_provider = str(operasi.children[0].children[0])
								fmus_file = operasi.children[0].children[1] # ini masih tree
								fmus_file = str(fmus_file.children[0]) # semoga ini sudah file

								baris_entry = str(operasi.children[0].children[2])
								fmus_file_baris_entry = fmus_file + '=' + baris_entry
								operasi_value = str({llm_provider:fmus_file_baris_entry})

							else:
								operasi_value = str(maybe_operasi_value) # /path/to/source
						
						# e.g. append => "ambil_terdekod_dari_file_template=filepath:barisentry"
						operasi_value = '' if not operasi_value else '='+operasi_value
						operations.append(operasi_type + operasi_value)
				
				if operations != []:
					if is_debugging:
						self.debug(f"[processor] Adding operations [{operations}] ke node [{NewNode}]\n")
					NewNode.operations = operations

			elif tree.data == 'branch_instruksi':
				'''
				| "~" branch_instruksi
				branch_instruksi
					: if_branch			"if" "[" binary_condition (binary_condition)* "]"?
					| else_branch		"else" "[" binary_condition "]"?
					| while_loop		"while" "[" value_condition ("," value_condition)* "]"?
					| unless_loop		"unless" "[" value_condition ("," value_condition)* "]"?
				if dan else menjadi node dg name+type=branching
				selain ngoprek diri sendiri (kasih id, counter, condition, type=if/else)
				juga memodifikasi 'parent' node dg attr: branch_info
				berisi: id, counter, dan conditions (utk anak2 dari branch ini)
				'''
				branch_child = tree.children[0]
				peta_nilai = {
					'binary_no': 0,
					'binary_yes': 1,
					'binary_input': 2,
					'exist_filedir': 3,
					'dont_exist_filedir': 4,
				}
				
				conditions = []
				branch_instruksi = 'branching'
				branch_extra_info = {}
				# files_filter(dirpath, extension=[], only_filename=False, sort=False)
				# from schnell.app.dirutils import files_filter

				if branch_child.data == 'if_branch':
					branch_type = 'if'
					if is_debugging:
						self.debug('[processor] oprek if:', branch_child)
					# buat info branch (id, conds)
					branch_id = str(uuid.uuid4())
					branch_counter = 1 # if_branch selalu 1
					branch_info = {
						'id': branch_id,
						'counter': branch_counter, 
					}
					if hasattr(branch_child, 'children') and len(branch_child.children)>0:
						if_condition = branch_child.children[0]
						# self.debug('[processor] oprek if/if condition:', if_condition)
						if hasattr(if_condition, 'children'):						
							for kondisi in if_condition.children:
								''' if: "if" if_condition <- condition.children '''
								# self.debug('[processor] oprek if/if condition/kondisi:', kondisi)
								# self.debug('		data kondisi:', kondisi.data)
								# self.debug('		anak kondisi:', kondisi.children)
								nilai = str(kondisi.data)
								if data(kondisi) in ['exist_filedir', 'dont_exist_filedir']:
									nilai += '=' + token(kondisi)									
									# indah4(f"""[processor] if/fileexist condition: {nilai}""", warna='green')
									# input(' ... ')
									conditions.append(nilai)
								else:
									conditions.append(peta_nilai[nilai])
								if is_debugging:
									indah4(f"""[processor] if condition/kondisi: {kondisi}\n\tdata kondisi: {kondisi.data}\n\tanak kondisi: {kondisi.children}\n\tloop_condition: {nilai}""", warna='green')

								branch_info.update({
									'conditions': conditions
								})
					if ParentNode:
						if hasattr(ParentNode, 'branch_info'):
							ParentNode.branch_info.append(branch_info)
						else:
							ParentNode.branch_info = [branch_info]

				elif branch_child.data == 'else_branch':
					branch_type = 'else'
					# self.debug('[processor] oprek branch else:', branch_child)
					# get branch id
					if ParentNode and hasattr(ParentNode, 'branch_info'):
						branch_id = ParentNode.branch_info[-1]['id']
						branch_counter = ParentNode.branch_info[-1]['counter'] + 1
						ParentNode.branch_info[-1]['counter'] = branch_counter

					if hasattr(branch_child, 'children') and len(branch_child.children)>0:
						else_condition = branch_child.children[0]
						# self.debug('[processor] oprek else/else condition', else_condition)
						if hasattr(else_condition, 'children'):
							kondisi = else_condition.children[0]
							nilai = str(kondisi.data)
							if data(kondisi) in ['exist_filedir', 'dont_exist_filedir']:
								nilai += '=' + token(kondisi)
								# indah4(f"""[processor] else/fileexist condition: {nilai}""", warna='green')
								conditions.append(nilai)
							else:
								conditions.append(peta_nilai[nilai])
							if is_debugging:
								self.debug(f'[processor] else_condition => {nilai}.')

				elif branch_child.data == 'while_loop' or branch_child.data == 'unless_loop':
					'''
					perkenalkan: selama ada file dg ekstensi xxx dalam item.workdir
					~while[__LS=txt]
					~while[__LS=*]
					while_condition: "[" value_condition ("," value_condition)* "]"
					for kondisi in loop_condition.children:
					memproses kondisi/value_condition yg terpisah oleh koma
					'''
					from schnell.app.fmusutils import replace_from_configuration # supaya tdk circular import
					branch_instruksi = 'looping'
					loop_type = 'while' if branch_child.data == 'while_loop' else 'unless'
					branch_id = str(uuid.uuid4())
					branch_counter = 1 # if_branch selalu 1
					branch_info = {
						'id': branch_id,
						'counter': branch_counter, 
					}
					# jk specify while condition -> ~while[yes] = selama input=yes
					# jk specify unless condition -> ~unless[yes] = selama bukan input=yes
					if hasattr(branch_child, 'children') and len(branch_child.children)>0:
						loop_condition = branch_child.children[0]
						if is_debugging:
							self.debug('[processor] loop (while/unless) condition:', loop_condition)
						if hasattr(loop_condition, 'children'):
							for kondisi in loop_condition.children:
								# self.debug('[processor] oprek loop condition/kondisi:', kondisi)
								# self.debug('		data kondisi:', kondisi.data)
								# self.debug('		anak kondisi:', kondisi.children)
								value_condition = str(kondisi.children[0])
								conditions.append(value_condition)
								if is_debugging:
									indah4(f"""[processor] loop condition/kondisi: {kondisi}\n\tdata kondisi: {kondisi.data}\n\tanak kondisi: {kondisi.children}\n\tloop_condition: {value_condition}""", warna='green')
								branch_info.update({
									'conditions': conditions
								})

								if value_condition.startswith(LISTDIR) and '=' in value_condition:
									# step 1 utk oprek files dlm curdir
									_, file_extension = value_condition.split('=')
									if file_extension:
										branch_extra_info['__PROCESS_DIR'] = workdir
										if file_extension == '*':
											branch_extra_info['__PROCESS_FILES'] = [joiner(workdir, item) for item in files_filter(normy(workdir))]
										else:
											branch_extra_info['__PROCESS_FILES'] = [joiner(workdir, item) for item in files_filter(normy(workdir), [file_extension])]
										self.run_configuration['replacer']['__PROCESS_FILES'] = branch_extra_info['__PROCESS_FILES']
								elif value_condition.startswith(LISTSTR):
									'''
									~while[__STR=filepath=barisentry]
									~while[__STR=satu dua tiga empat]
									'''
									if '=' in value_condition:
										if value_condition.count('=') == 2:
											fpath, bentry = value_condition.removeprefix(LISTSTR+'=').split('=')
											fpath = replace_from_configuration(fpath, self.run_configuration)
											if not isfile(fpath):
												test_filepath_from_curdir = joiner(workdir, fpath)
												if isfile(test_filepath_from_curdir):
													fpath = test_filepath_from_curdir
											if isfile(fpath):
												peroleh = get_definition_by_key_permissive_start(fpath, bentry)
												if peroleh:
													branch_extra_info['__PROCESS_STRINGS'] = peroleh.split()
										elif value_condition.count('=') == 1:
											'''
											~while[__STR=satu dua tiga empat]
											'''
											strdata = value_condition.removeprefix(LISTSTR+'=')
											branch_extra_info['__PROCESS_STRINGS'] = strdata.split()

										if '__PROCESS_STRINGS' in branch_extra_info:
											self.run_configuration['replacer']['__PROCESS_STRINGS'] = branch_extra_info['__PROCESS_STRINGS']

								elif value_condition.startswith(LISTCMA):
									'''
									~while[__CMA=filepath=barisentry]
									~while[__CMA=satu,dua,tiga,empat] # nope, gak bisa ini, krn , adlh pemisah value_condition
									'''
									if '=' in value_condition:
										if value_condition.count('=') == 2:
											fpath, bentry = value_condition.removeprefix(LISTCMA+'=').split('=')
											fpath = replace_from_configuration(fpath, self.run_configuration)
											if not isfile(fpath):
												test_filepath_from_curdir = joiner(workdir, fpath)
												if isfile(test_filepath_from_curdir):
													fpath = test_filepath_from_curdir
											if isfile(fpath):
												# from schnell.app.fileutils import get_definition_by_key_permissive_start
												peroleh = get_definition_by_key_permissive_start(fpath, bentry)
												if peroleh:
													branch_extra_info['__PROCESS_COMMAS'] = [item.strip() for item in peroleh.split(',')]
											if '__PROCESS_COMMAS' in branch_extra_info:
												self.run_configuration['replacer']['__PROCESS_COMMAS'] = branch_extra_info['__PROCESS_COMMAS']

					if ParentNode:
						if hasattr(ParentNode, 'branch_info'):
							ParentNode.branch_info.append(branch_info)
						else:
							ParentNode.branch_info = [branch_info]

				cmd_params = {
					'name'				: branch_instruksi,
					'type'				: branch_instruksi,
					'counter' 			: self.run_configuration['counter'],
					'replacer'			: self.run_configuration['replacer'],
					'original'			: code,
					# 'branch_type'		: branch_type,
					'branch_id'			: branch_id,
					'branch_condition'	: conditions,
					'branch_counter'	: branch_counter,					
					'workdir'			: workdir, 
					'level'				: parentLevel,
					'branch_extra_info'	: branch_extra_info,
				}
				if branch_instruksi == 'branching':
					cmd_params.update({
						'branch_type'			: branch_type,
						'skip'					: True, # default di awal sblm generator
					})
				else:
					cmd_params.update({
						'loop_type'				: loop_type,
						'execute'				: True, # default di awal sblm generator
					})
				if ParentNode:
					cmd_params.update({
						'parent'				: ParentNode
					})				
				NewNode = AnyNode(**cmd_params)
				if is_debugging:									
					self.debug(f'\n\t[processor] {branch_instruksi} node: [{NewNode}]\n')

			elif tree.data == 'pickone_instruksi':
				'''
				punya len children > 0 berarti children bukan []
				dan berisi tree utk choose_condition
				'''
				# peta_nilai_pickone_instruksi = {
				# 	# 'binary_no': 0,
				# 	'pilihan_angka': 1,
				# 	'pilihan_input': 999,
				# }
				pilihan_input = 999
				conditions = []
				if hasattr(tree, 'children') and len(tree.children)>0:
					# jk ?pick[#,i]
					for choosenums in tree.children:
						# "sekarang choosenum adlh choose_condition tree"
						if hasattr(choosenums, 'children') and len(choosenums.children)>0:
							for choosenum in choosenums.children:
								if hasattr(choosenum, 'children') and len(choosenum.children)==1:
									# print('[processor:1212] obox:', choosenum)
									bilangan = str(choosenum.children[0])
									if choosenum.data == 'pilihan_angka':
										conditions.append(int(bilangan))
									elif choosenum.data == 'pilihan_input':
										"jk minta input maka masukkan 999, sementara ini gak dipake"
										conditions.append(pilihan_input)
									
									# conditions.append(peta_nilai_pickone_instruksi[bilangan])
									cmd_params = {
										'name'					: 'pickone_ormore',
										'type'					: 'pickone_ormore',
										'counter' 				: self.run_configuration['counter'],
										'replacer'				: self.run_configuration['replacer'],
										'pickone_condition'		: conditions,
										'original'				: code,
										'workdir'				: workdir, 
										'level'					: parentLevel
									}
									if ParentNode:
										cmd_params.update({
											'parent'	: ParentNode
										})
									NewNode = AnyNode(**cmd_params)
									if is_debugging:
										self.debug('\n[processor] pickone node:', NewNode, '\n')
				else:
					# utk ?pick saja...
					cmd_params = {
						'name'						: 'pickone_ormore',
						'type'						: 'pickone_ormore',
						'counter' 					: self.run_configuration['counter'],
						'replacer'					: self.run_configuration['replacer'],
						'original'					: code,
						'workdir'					: workdir, 
						'level'						: parentLevel
					}
					if ParentNode:
						cmd_params.update({
							'parent'	: ParentNode
						})
					NewNode = AnyNode(**cmd_params)
					if is_debugging:
						self.debug('\n[processor] pickone node:', NewNode, '\n')

		return NewNode

