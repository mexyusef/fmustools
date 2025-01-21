import datetime, pathlib, os, sys

sidoarjodir = r'c:\users\usef\work\sidoarjo'
sys.path.insert(0, sidoarjodir)
# sidoarjodir = pathlib.Path(__file__).resolve().parent.parent.parent.parent
# sys.path.append(str(sidoarjodir))

from schnell.app.appconfig import programming_data
from schnell.app.dirutils import ayah
from schnell.app.printutils import print_json, indah3, indah4
from schnell.app.transpiler.grammar import bahasa as bahasa_lalang
from schnell.app.transpiler.config import program_context, daftar_languages, languages
from schnell.app.transpiler.zgenerate.helper.redis_helper import getstr, ada_inlist
from schnell.app.transpiler.zgenerate.refactor.generator import generate
from schnell.app.utils import trycopy, env_exist, env_reload

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

# if not env_exist('ULIBPY_REDIS_HOST'):
# 	# jk gak ada konfi utk redis maka perlu loading manual
# 	env_reload()


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines


def process_program_configuration_items(childrens):
	global program_context
	program_context['language_context'] = []
	for item in childrens:
		if item.data == 'program_configuration_item':
			lang_lib_frame_tool_ctx = item.children[0]
			lang_config = lang_lib_frame_tool_ctx.data
			# if lang_config in daftar_languages:
			if lang_config in languages:
				if lang_config not in program_context['language_context']:
					program_context['language_context'].append(lang_config)
			elif lang_config == 'library_context':
				'''
				library_context
					library_items
						library_item    mylib
				'''
				items = lang_lib_frame_tool_ctx.children[0]
				for item in items.children:
					itemname = str(item.children[0])
					if itemname not in program_context['library_context']:
						program_context['library_context'].append(itemname)
			elif lang_config == 'framework_context':
				'''
				framework_context
					framework_items
						framework_item  myframework
				'''
				items = lang_lib_frame_tool_ctx.children[0]
				for item in items.children:
					itemname = str(item.children[0])
					if itemname not in program_context['framework_context']:
						program_context['framework_context'].append(itemname)
			elif lang_config == 'tools_context':
				'''
				tools_context
					tools_items
						tools_item      mytools
				'''
				items = lang_lib_frame_tool_ctx.children[0]
				for item in items.children:
					itemname = str(item.children[0])
					if itemname not in program_context['tools_context']:
						program_context['tools_context'].append(itemname)


global_parser = Lark(bahasa_lalang, start='program').parse

def process_language(code, returning=True, verbose=True):
	global program_context

	print('='*20, code, '\n')

	instructions = TheProcessor().transform(global_parser(code))

	hasil_dalam_list = []
	bahasa_terpilih = []
	
	for insn in instructions: # instructions adlh tuple
		# insn = program_language, item_line
		for tree in insn.children: # insn adlh Tree
			if verbose:
				# print(f'{insn.data}: {type(insn)}', f'{tree.data}: {type(tree)}')
				print(tree.pretty())

			if tree.data == 'program_configuration_items':
				'''
				setiap /py,ts/ dll akan dimasukkan program_context yg sebetulnya dilempar ke generator
				tapi blm digunakan utk saat ini
				'''
				process_program_configuration_items(tree.children)
				if program_context and 'language_context' in program_context and program_context['language_context']:
					daftar = program_context['language_context']
					if verbose:
						print('daftar from specified command =', daftar)

			elif tree.data in ['item', 'item_separator']:
				for lang in daftar:
					# panggil generate dari gen_*.py
					# hasil = daftar_languages[lang](tree, program_context)
					hasil = generate(tree, program_context, lang)
					if hasil:
						hasil_dalam_list.append(hasil)
						bahasa_terpilih.append(lang)
					# else:
					# 	# hasil item_separator diskip
					# 	# tapi nantinya dipake, utk bisa programmatically create newline etc
					# 	print(f'[app.transpiler.refactor.process_language] no result [{hasil}] for language "{lang}" in daftar {daftar}')

	if returning:
		if verbose:
			print('[app.transpiler.refactor.process_language] returning utk jenis', type(hasil_dalam_list))
		if isinstance(hasil_dalam_list, list):
			return '\n'.join(hasil_dalam_list)
		elif isinstance(hasil_dalam_list, str):
			return hasil_dalam_list
	else:
		print_json(program_context)
		# dipisah = ('\n'+'='*20+'\n').join(hasil_dalam_list)
		dipisah = [('='*10 + f' {bahasa_terpilih[idx]}\n')+item for (idx, item) in enumerate(hasil_dalam_list)]
		dipisah = '\n'.join(dipisah)
		indah3(dipisah, warna='green')
	# kosongkan setiap kali invoke, biar gak numpuk
	program_context = {
		'language_context': [],
		'library_context': [],
		'framework_context': [],
		'tools_context': [],
	}


shortcuts = {
	's:int': '/py/?K__ARG/pyint', # list of 5 ints
	's:i': '/py/?K__ARG/pyint', # list of 5 ints
	's:rl': '/py/?r=*', # redis list
	's:list': '/py/?r=*', # redis list
	's:1': '/py/?rs=ulangsingle',
	's:2': '/py/?rs+ulangsingle=', # dikahiri dg = berarti minta arg
}

def myrepl():
	code = 1
	while code != 'x':
		try:
			code = input(f'LALANG-REFAC {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} >> ')
			code = code.strip()
			# print(f'code adlh: [{code}]')
			if code == 'bahasa':
				# print(f'code #1 adlh: [{code}]')
				# trycopy(bahasa)
				indah4(bahasa_lalang, warna='green')
			elif code == 'editfile':
				os.system(f"code {__file__}")
			elif code == 'editfo,der':
				os.system(f"code {ayah(__file__,1)}")
			elif code and [item for item in shortcuts.keys() if item.startswith(code)]:
				# print(f'code #2 adlh: [{code}]')
				# sementara blm pake args
				program = shortcuts[code]
				if program.endswith('=') or '__ARG' in program:
					arg = input(f'Masukkan argumen untuk {program}: ')
					arg = arg.strip()
					if arg:
						if program.endswith('='):
							program += arg
						else:
							program = program.replace('__ARG', arg, 1)
							while program.count('__ARG'):
								arg = input(f'Masukkan argumen berikutnya untuk {program}: ')
								if arg:
									program = program.replace('__ARG', arg, 1)
						print(f'convert code from {code} to {program}')
						process_language(program)
				else:
					print(f'convert code from {code} to {program}')
					process_language(program)
			elif code.startswith('__'):
				# print(f'code #3 adlh: [{code}]')
				# utk snippet
				program = code.removeprefix('__').strip()
				from snippets import cari_asstring
				hasil = cari_asstring(program)
				indah3(hasil, warna='white')
			elif code != '' and code != 'x':
				# print(f'code #4 adlh: [{code}]')
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
