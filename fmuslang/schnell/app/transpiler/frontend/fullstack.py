import datetime, os, sys, traceback

# schnelldir = '/home/usef/work/ulibs/schnell'
# app.transpiler.frontend.fullstack = os.pardir * 3
disini = os.path.normpath(os.path.abspath(os.path.dirname(__file__))) # frontend
path_transpiler = os.path.join(disini, os.pardir)
path_app = os.path.join(path_transpiler, os.pardir)
path_schnell = os.path.join(path_app, os.pardir)
schnelldir = path_schnell
sys.path.extend([schnelldir, '..'])

# from schnell.app.dirutils import (ayah, joiner, here)
from schnell.app.printutils import print_json, indah3, indah4, print_copy
from schnell.app.utils import trycopy, env_exist, env_reload, env_set
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
	| statement_config? csv_statement? backend_statement? frontend_statement?

// pengennya gimana: bisa generate berbagai versi next/react/mui/bs/dst.
// bisa generate fmus
// bisa generate + execute fmus
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "i" 		-> info // info atau help, mengentai kode yg dioprek
	| "dj" 		-> be_django
	| "djm" 	-> be_django_mongo
	| "sb" 		-> be_springboot
	| "sbm"		-> be_springboot_mongo
	| "fast" 	-> be_fastapi
	| "fastm" 	-> be_fastapi_mongo
	| "fl" 		-> be_flask
	| "flm" 	-> be_flask_mongo
	| "ns" 		-> be_nest
	| "nsm" 	-> be_nest_mongo
	| "dw" 		-> be_dropwizard
	| "dwm" 	-> be_dropwizard_mongo
	| "mn" 		-> be_micronaut
	| "mnm" 	-> be_micronaut_mongo
	| "q" 		-> be_quarkus
	| "qm" 		-> be_quarkus_mongo
	| "nda" 	-> be_node_antd
	| "ndam" 	-> be_node_antd_mongo
	| "ndp" 	-> be_node_apollo
	| "ml" 		-> be_moleculer
	| "mlm"		-> be_moleculer_mongo
	| "lt" 		-> fe_react_light
	| "ag" 		-> fe_react_argon
	| "af" 		-> fe_react_airframe
	| "vo" 		-> fe_react_volt
	| "nt" 		-> fe_react_notus
	| "now" 	-> fe_react_now
	| "ppr" 	-> fe_react_paper
	| "xt" 		-> fe_react_xtreme
	| "all" 	-> fullstack
	| "fs" 		-> fullstack
	| "mqr"				-> misc_quickrepl
	| "msp"				-> misc_simplepython
	| "msut"			-> misc_simpleunittest
	| "mlang"			-> misc_langtemplate
	| "mtray"			-> misc_pytrayicon
	| "mcrajs"			-> misc_crajs
	| "mcrats"			-> misc_crats
	| "mrcli"			-> misc_rustcli
	| "mccli"			-> misc_cppcli
	| "mgcli"			-> misc_gocli
	| "mid"				-> misc_indon
	| "msfx"			-> misc_sfxso
	| "mjfx"			-> misc_jfxso
	| "mjupy"			-> misc_jupy
	| "mjuser"			-> misc_jupyuser
	| "mel"				-> misc_electron
	| "mbedj"			-> misc_be_django_corona
	| "mbeno"			-> misc_be_node_corona
	| "mqt"				-> misc_qtcmake
	| "mqt2"			-> misc_qtcmake2
	| "msel1"			-> misc_tselflutter1
	| "mrn1"			-> misc_reactnative1
	| "msun"			-> misc_androidkotlinbasesunflower
	| "mrural"			-> misc_rustwarpsimplerest
	| "mgseed"			-> misc_mongoseeder
// insert new misc app
	| "urlr"			-> utils_relight_routes
	| "upsr"			-> utils_proshop_routes
	| "upss"			-> utils_proshop_store
	| "upsb"			-> utils_proshop_backend 	// wm -e'***upsb,*/B^..^'
	| "uecommdj"		-> utils_ecommdj					// wm -e'***uecommdj,*/B^..^'
	| "upnode"			-> utils_proshop_node
	| "mhcx"			-> misc_htmlcss
	| "uvsb"			-> utils_vertxspringboot		// lebih mirip misc: wm -e '***uvsb,*/B'
	| "upmern"			-> utils_proshop_mern

// insert new utils app
backend_statement		: "B^" program_backend "^"
	| "B" // wm -e "***mrcli,*/B"

csv_statement			: "C^" program_csv "^"
frontend_statement		: "F^" program_frontend "^"

program_backend: HURUF_PROGRAM_BACKEND
program_csv: HURUF_PROGRAM_CSV

program_frontend: declarative_element ("," declarative_element)*
declarative_element: element_name element_config? cdata_text? element_children?
element_name: HURUF_DIGIT
element_config_separator: ","
element_config: "/" element_config_item (element_config_separator element_config_item)* "/"
	| "$" element_config_item_berslash (element_config_separator element_config_item_berslash)* "$"
element_config_item: HURUF_DIGIT  -> item_key_value_boolean
	| item_key "=" item_value       -> item_key_value
element_config_item_berslash: HURUF_DIGIT  -> item_key_value_boolean
	| item_key "=" item_value       -> item_key_value
	| item_key "=" item_value_berslash       -> item_key_value_berslash
element_children: "(" program_frontend ")"
item_key: HURUF_DIGIT
// item value hrs bisa terima:
// ' " { } ( ) [ ] / @ : ;
// <Route path="/@:username/favorites" component={ProfileFavorites} />
item_value: HURUF_NILAI
	| "'" HURUF_NILAI_BERSPASI "'" -> diapit_sq
	| "\\"" HURUF_NILAI_BERSPASI "\\"" -> diapit_dq
item_value_berslash: HURUF_NILAI_BERSLASH
cdata_text: HURUF_CDATA

HURUF_CDATA: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|" "|";"|":"|"+"|"-")*
HURUF_NILAI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" ")*
HURUF_NILAI_BERSLASH: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*
HURUF_NILAI_BERSPASI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"`"|"{"|"}"|"("|")"|"="|" ")*
HURUF_NON_OPEN: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|","|" "|"+"|"="|"-"|"_"|"@"|"#"|"$"|"%"|"^"|"&"|"*")*
HURUF_KODE_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{"|"<") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*

HURUF_PROGRAM_BACKEND: 	("_"|LETTER|DIGIT|"\\""|"{"|"[") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/"|","|";"|":"|"@"|"["|"]"|"#"|"|")*
HURUF_PROGRAM_CSV: 			("_"|LETTER|DIGIT|"\\""|"{"|"[") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/"|","|";"|":"|"@"|"["|"]"|"#"|"|")*
HURUF_PROGRAM_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*
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

# from schnell.app.transpiler.frontend.bahasa_html import bahasa
# from schnell.app.transpiler.frontend.bahasa import bahasa
# from schnell.app.transpiler.frontend.react.handler import handler

from schnell.app.transpiler.frontend.fslang.statement_config import statement_config
from schnell.app.transpiler.frontend.fslang.backend_statement import backend_statement
from schnell.app.transpiler.frontend.fslang.frontend_statement import frontend_statement
from schnell.app.transpiler.frontend.fslang.csv_statement import csv_statement

from schnell.app.transpiler.frontend.fslang.common import program_config

def handler(tree):
	"""
	statement
		statement_config
			statement_config_list
				fe_react_light
		backend_statement
			program_backend     satu
		frontend_statement
			program_frontend    dua
	"""
	print('[s.a.t.fe.fs.handler]:', data(tree))
	# print(tree.pretty())

	kembali = ''
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'statement_config':
			res = statement_config(item)
			print(f"[s.a.t.fe.fs.handler] hasil statement_config: {res}")
			program_config.update(res)
		elif jenis == 'backend_statement':
			res = backend_statement(item)
			program_config.update(res)
		elif jenis == 'csv_statement':
			res = csv_statement(item)
			program_config.update(res)
		elif jenis == 'frontend_statement':
			'''
			F: frontend_config => program_config
			'''
			res = frontend_statement(item)
			program_config.update(res)
	# cek apa perlu jalankan fmus: {'config': {'fmus': 'execute'}}
	# print('cek apa perlu jalankan fmus:', program_config)
	return kembali


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines


def process_language(code, returning=False, debug=True):
	global program_config
	try:
		pre_parser = Lark(bahasa, start='program')
		parser = pre_parser.parse
		indah4('='*20 + ' ' + code + '\n', warna='red')
		parsed_tree = parser(code)
		instructions = TheProcessor().transform(parsed_tree)
		# results = []
		for insn in instructions:
			# print('loop outer:', data(insn))
			if debug:
				print(insn.pretty())
				
			hasil = handler(insn)
			print('[fullstack] hasil handler (jk ada):', hasil)
			# results.append(hasil)

			# utk fullstack gak perlu ini all,*
			# krn dalam fullstack/__init__ sudah run_fmus utk masing2 generator
			if 'config' in program_config:
				config = program_config['config']
				if 'fmus' in config:
					if config['fmus'] == 'execute':
						print('lets execute the prisoners now!', program_config)
						from schnell.app.fileutils import get_definition_by_key_permissive_start
						from schnell.app.fmus import Fmus
						filepath = program_config['filepath']
						baris_entry = program_config['baris_entry']
						program = get_definition_by_key_permissive_start(filepath, baris_entry)
						fmus = Fmus(False)
						fmus.set_file_dir_template(filepath)
						fmus.process(program)
						input('[fullstack] Press any key to continue... ')
						program_config = {
							'config': {
								'fe': 'react-light',
							}
						}

		# hasil = '\n'.join(results)
		if returning:
			filepath = program_config['filepath']
			baris_entry = program_config['baris_entry']
			return filepath, baris_entry
		# indah3(hasil, warna='yellow')

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
			code = input(f'FULLSTACK {prompt} >> ')
			code = code.strip()			
			if code == 'bahasa':
				indah4(bahasa, warna='green')
			elif code.startswith('csv='):
				'''
				csv=json2/{@User=#2}username,s
				'''
				from schnell.app.dirutils import joiner
				from schnell.app.utils import perintahsp_simple
				# ternyata perintah dan perintah_shell memakan ; pada "username,s ; password,s"
				csvdir = joiner(schnelldir, 'app/transpiler/csv')
				sys.path.append(csvdir)
				code = code.removeprefix('csv=')
				# print(f'FS mengirimkan [{code}]')
				perintahsp_simple(f'python ../csv/main.py {code}')
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
			code = input(f'FULLSTACK {prompt} >> ')
			code = code.strip()	
			if code == 'bahasa':
				indah3(bahasa, warna='green')
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
