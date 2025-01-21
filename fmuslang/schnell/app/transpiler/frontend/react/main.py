
import datetime, sys, traceback

schnelldir = '/home/usef/work/ulibs/schnell'
sys.path.extend([schnelldir, '..'])

# from app.dirutils import (ayah, joiner, here)
from app.printutils import print_json, indah4, print_copy
from app.utils import trycopy, env_exist, env_reload, env_set
from app.treeutils import (
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
# from lark.visitors import InlineTransformer
# from lark import (
# 	Lark,
# 	# InlineTransformer,
# )
# from lark.visitors import InlineTransformer
from schnell.vendor.lark.indenter import Indenter

from .bahasa import bahasa

env_set('ULIBPY_FMUS_DEBUG', 1)


# from app.transpiler.frontend.bahasa_html import bahasa
# from app.transpiler.frontend.bahasa import bahasa
from app.transpiler.frontend.react.handlers.ecomm import handler


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines


def process_language(code, returning=False, debug=True):
	# print('#1 process language, code:', code, 'grammar:', bahasa[:50] + '...')
	try:
		pre_parser = Lark(bahasa, start='program')
		parser = pre_parser.parse
		indah4('='*20 + ' ' + code + '\n', warna='red')
		parsed_tree = parser(code)
		instructions = TheProcessor().transform(parsed_tree)
		results = []
		for insn in instructions:
			# print('loop outer:', data(insn))
			if debug:
				print(insn.pretty())
				
			hasil = handler(insn)
			results.append(hasil)

		hasil = '\n'.join(results)
		if returning:
			return hasil
		indah4(hasil, warna='yellow')

	except Exception as err:
		print(err)
		trace = traceback.format_exc()
		print(trace)


def myrepl(debug=True):
	code = 1
	while code != 'x':
		try:
			# prompt = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			prompt = datetime.datetime.utcnow().isoformat()
			code = input(f'REACT {prompt} >> ')
			code = code.strip()			
			if code == 'bahasa':
				indah4(bahasa, warna='green')
			elif code != '' and code != 'x':
				# print(f'code adlh: [{code}]')
				process_language(code, debug=debug)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
