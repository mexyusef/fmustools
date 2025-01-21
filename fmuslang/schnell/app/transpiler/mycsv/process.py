import datetime, sys, traceback

from schnell.app.autoutils import confirm
# from schnell.app.dirutils import (ayah, joiner, here)
from schnell.app.printutils import print_json, indah3, print_copy
from schnell.app.utils import trycopy, env_exist
from schnell.app.treeutils import (
	child,
	child1,
	anak,
	jumlahanak, beranak,
	data,
	token,
	chtoken, chdata,
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
from schnell.app.transpiler.mycsv.csv_operation import bahasa as bahasa_mycsv
from schnell.app.transpiler.mycsv.handlers import handler


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines

parser = Lark(bahasa_mycsv, start='program').parse
def process_language(code, returning=False, debug=False):
	results = []
	try:
		print('='*20, code, '\n')
		parsed_tree = parser(code)
		# print('#2 process language: stlh Lark().parse(code)')
		instructions = TheProcessor().transform(parsed_tree)
		providers = []
		for insn in instructions:
			# print(data(insn))
			for item in anak(insn):
				if debug:
					print(item.pretty())
				for thing in anak(item):
					if data(thing) == 'csv_config':
						csv_items = child1(thing)
						for token_provider in anak(csv_items):
							prov = data(token_provider)
							providers.append(prov)
					if data(thing) == 'csv_code':
						kode = token(thing)
						results = handler(kode, providers, returning=returning, debug=debug)
		if returning:
			return results
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
				indah3(bahasa_mycsv, warna='green')
			elif code != '' and code != 'x':
				# print(f'code adlh: [{code}]')
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


def quick_repl():
	code = 1
	while code != 'x':
		try:
			# prompt = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			prompt = datetime.datetime.utcnow().isoformat()
			code = input(f'CVSLANG {prompt} >> ')
			code = code.strip()			
			if code == 'bahasa':
				indah3(bahasa_mycsv, warna='green')
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
