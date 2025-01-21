import datetime, os, sys, traceback

# schnelldir = '/home/usef/work/ulibs/schnell'
# app.transpiler.frontend.main = os.pardir * 3
disini = os.path.normpath(os.path.abspath(os.path.dirname(__file__))) # frontend
path_transpiler = os.path.join(disini, os.pardir)
path_app = os.path.join(path_transpiler, os.pardir)
path_schnell = os.path.join(path_app, os.pardir)
schnelldir = path_schnell
sys.path.extend([schnelldir, '..'])

# from schnell.app.dirutils import (ayah, joiner, here)
from schnell.app.printutils import print_json, indah3, indah4, print_copy
from schnell.app.utils import trycopy, env_exist, env_reload
from schnell.app.treeutils import (
	child, child1,
	anak, jumlahanak, beranak,
	data,
	token, chtoken, chdata,
)
import schnell.vendor.lark as lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)

from schnell.vendor.lark.indenter import Indenter
# from schnell.app.transpiler.frontend.bahasa_html import bahasa
from schnell.app.transpiler.frontend.bahasa import bahasa as bahasa_declang
from schnell.app.transpiler.frontend.handler import handler


class TheProcessor(InlineTransformer):
	def declarative_program(self, *item_lines):
		return item_lines

from schnell.app.llmutils.langchainutils.llm_config import all_accounts
pre_parser = Lark(bahasa_declang, start='declarative_program')
parser = pre_parser.parse

def process_language(code, returning=True, debug=False, current_handler=handler): # , language_grammar=bahasa):
	if debug:
		indah4(f"""[schnell.app.transpiler.frontend.main.process language]
code: [{code}] 
grammar: [{bahasa_declang[:50]}]...
""", warna='magenta')
	try:
		indah4('='*20 + ' ' + code + '\n', warna='red')
		parsed_tree = parser(code)
		instructions = TheProcessor().transform(parsed_tree)
		results = []
		for insn in instructions:
			# print('loop outer:', data(insn))
			if all_accounts['declang_verbose']:
				print(insn.pretty())
			hasil = current_handler(insn)
			# indah4(hasil, warna='yellow')
			if hasil is not None:
				# kadang handler gak return value, kita gak perlu print output
				results.append(hasil)

		hasil = ''
		if results:
			if debug:
				print('[schnell.app.transpiler.frontend.main] results:', results)
			hasil = '\n'.join(results)
		if hasil:
			indah4(hasil, warna='yellow')
		if returning:
			# return ''.join(results)
			return hasil
		return results

	except Exception as err:
		indah4(f"""[ERROR] schnell.app.transpiler.frontend.main.process_language""", warna='red')
		print(err)
		trace = traceback.format_exc()
		print(trace)


def myrepl(debug=True):
	code = 1
	while code != 'x':
		try:
			# prompt = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			prompt = datetime.datetime.utcnow().isoformat()
			code = input(f'FE {prompt} >> ')
			code = code.strip()
			if code == 'bahasa':
				indah4(bahasa_declang, warna='green')
			elif code != '' and code != 'x':
				# print(f'code adlh: [{code}]')
				process_language(code, debug=debug)
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
			code = input(f'DECL {prompt} >> ')
			code = code.strip()
			if code == 'bahasa':
				indah3(bahasa_declang, warna='green')
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
