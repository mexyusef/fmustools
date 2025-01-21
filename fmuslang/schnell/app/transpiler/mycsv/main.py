import datetime, os, sys, traceback

# schnelldir = '/home/usef/work/ulibs/schnell'
# app.transpiler.mycsv.main = os.pardir * 3
disini = os.path.normpath(os.path.abspath(os.path.dirname(__file__))) # mycsv
path_transpiler = os.path.join(disini, os.pardir)
path_app = os.path.join(path_transpiler, os.pardir)
path_schnell = os.path.join(path_app, os.pardir)
schnelldir = path_schnell
sidoarjodir = os.path.join(schnelldir, os.pardir)

sys.path.extend([sidoarjodir, schnelldir, '..'])

from schnell.app.utils import env_reload
# env_reload() # butuh utk bantu_faker

# from schnell.app.dirutils import (ayah, joiner, here)
from schnell.app.printutils import print_json, indah3, print_copy
from schnell.app.utils import trycopy, env_exist
from schnell.app.treeutils import (
	jumlahanak, beranak, chtoken, chdata, child, 
	child1,
	anak,
	data,
	token,	
)
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
from schnell.app.transpiler.mycsv.csv_operation import bahasa
from schnell.app.transpiler.mycsv.handlers import handler


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines


def process_language(code, returning=False):
	print(f'[app.transpiler.mycsv.main][process_language], code: [{code}] bahasa: [{bahasa[:10]}]......')
	kembali = ''
	try:
		pre_parser = Lark(bahasa, start='program')
		# print('#1b process language, type pre_parser:', type(pre_parser))
		parser = pre_parser.parse
		# print('#1c process language: stlh parse')
		print('='*20, code, '\n')
		parsed_tree = parser(code)
		# print('#2 process language: stlh Lark().parse(code)')
		instructions = TheProcessor().transform(parsed_tree)
		providers = []
		for insn in instructions:
			# print(data(insn))
			for item in anak(insn):
				print(item.pretty())
				for thing in anak(item):
					if data(thing) == 'csv_config':
						csv_items = child1(thing)
						for token_provider in anak(csv_items):
							prov = data(token_provider)
							providers.append(prov)
					if data(thing) == 'csv_code':
						kode = token(thing)
						kembali = handler(kode, providers, returning=returning)
		if returning:
			if isinstance(kembali, list):
				return '\n'.join(kembali)
			return kembali
	except Exception as err:
		print(err)
		trace = traceback.format_exc()
		print(trace)


def myrepl():
	code = 1

	# jk ada args, maka proses args sbg satu baris
	if len(sys.argv) > 1:
		print('terima args:', sys.argv[1:])
		code = ' '.join(sys.argv[1:])
		process_language(code)
		return

	while code != 'x':
		try:
			# prompt = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			prompt = datetime.datetime.utcnow().isoformat()
			code = input(f'CVSLANG {prompt} >> ')
			code = code.strip()			
			if code == 'bahasa':
				indah3(bahasa, warna='green')
			elif code != '' and code != 'x':
				# print(f'code adlh: [{code}]')
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
