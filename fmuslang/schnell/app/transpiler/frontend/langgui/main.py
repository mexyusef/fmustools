
import datetime, sys, traceback

schnelldir = '/home/usef/work/ulibs/schnell'
sys.path.extend([schnelldir, '..'])

# from app.dirutils import (ayah, joiner, here)
from app.printutils import print_json, indah3, print_copy
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

env_set('ULIBPY_FMUS_DEBUG', 1)

react_language = """
program: statement+
statement: 
	| statement_config? statement_choice

// pengennya gimana: bisa generate berbagai versi next/react/mui/bs/dst.
// bisa generate fmus
// bisa generate + execute fmus
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "@" -> run_on_wsl
	| "0" -> run_on_windows

// index=list -> product item(s) -> product detail
statement_choice: "a1" -> create_product_model
	| "a2" -> create_product_api // utk dikonversi ke list of product items
	| "a3" -> create_product_item_component // product item, list itu di pages/index
	| "a4" -> create_product_style // display: grid, grid-template-columns: list + detail
	| "a5" -> create_product_detail_page // pages/product/[id]
	| "a6" -> create_add_to_cart_action // product-item tambah button yg panggil action ini
	// button add to cart/buy juga muncul pd product detail page
	// disable button jk in-stock=0
	| "a7" -> add_cart_to_navbar
	| "a8" -> create_cart_page // list cart items + shipping form
	| "a9" -> create_cart_item_component
	| "a10" -> redux_add_to_cart
	| "a11" -> redux_cart_increase_decreate
	| "1" -> accelerator
	| "accel" -> accelerator
	| "acc" -> accelerator
	| "2" -> alert
	| "3" -> appbar
	| "4" -> autocomplete
	| "5" -> button
	| "btn" -> button
	| "b" -> button
	| "6" -> canvas
	| "7" -> card
	| "8" -> carousel
	| "9" -> cascader
	| "10" -> chart_bar
	| "11" -> chart_donut
	| "12" -> chart_line
	| "13" -> chart_pie
	| "14" -> chart_radar
	| "15" -> chart_scatter
	| "16" -> checkbox
	| "17" -> collapse
	| "18" -> column
	| "19" -> combobox
	| "20" -> context
	| "21" -> datepicker
	| "22" -> dialog_opendir
	| "23" -> dialog_openfile
	| "24" -> dialog_savefile
	| "25" -> drag
	| "26" -> drawer
	| "27" -> dropdown
	| "28" -> event
	| "29" -> form
	| "form" -> form
	| "30" -> form_item
	| "fi" -> form_item
	| "31" -> frame
	| "frame" -> frame
	| "frm" -> frame
	| "32" -> graph_dot
	| "33" -> gridview
	| "34" -> group
	| "35" -> icon
	| "36" -> image
	| "37" -> import
	| "38" -> label
	| "39" -> layout
	| "40" -> link
	| "41" -> listview
	| "42" -> main
	| "43" -> menu
	| "44" -> messagebox
	| "45" -> modal
	| "46" -> navigation
	| "47" -> navigation_bottom
	| "48" -> notification
	| "49" -> pagination
	| "50" -> popconfirm
	| "51" -> popover
	| "52" -> progressbar
	| "53" -> radio
	| "54" -> reference
	| "55" -> richtext
	| "56" -> row
	| "57" -> screen
	| "58" -> snackbar
	| "59" -> spinbox
	| "60" -> splash
	| "61" -> splitter
	| "62" -> statusbar
	| "63" -> step
	| "64" -> switch
	| "65" -> tab
	| "66" -> table
	| "67" -> textarea
	| "68" -> textfield
	| "69" -> toast
	| "70" -> toolbar
	| "71" -> tooltip
	| "72" -> teeview
	| "73" -> window
	| "74" -> xml

"""

huruf = """
HURUF_DIGIT: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
"""

from langs import base_grammar

bahasa = f"""
{react_language}

{huruf}

{base_grammar}
"""

# from app.transpiler.frontend.bahasa_html import bahasa
# from app.transpiler.frontend.bahasa import bahasa
# from app.transpiler.frontend.react.handler import handler


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines


def process_language(code, returning=False, debug=True):
	# print('#1 process language, code:', code, 'grammar:', bahasa[:50] + '...')
	try:
		pre_parser = Lark(bahasa, start='program')
		parser = pre_parser.parse
		indah3('='*20 + ' ' + code + '\n', warna='red')
		parsed_tree = parser(code)
		instructions = TheProcessor().transform(parsed_tree)
		results = []
		for insn in instructions:
			# print('loop outer:', data(insn))
			if debug:
				print(insn.pretty())
				
			# hasil = handler(insn)
			# results.append(hasil)

		hasil = '\n'.join(results)
		if returning:
			return hasil
		indah3(hasil, warna='yellow')

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
			code = input(f'GUI {prompt} >> ')
			code = code.strip()			
			if code == 'bahasa':
				indah3(bahasa, warna='green')
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
