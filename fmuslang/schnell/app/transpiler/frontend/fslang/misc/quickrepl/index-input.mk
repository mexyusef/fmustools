--% index/fmus
qrepl,d(/mk)
	main.py,f(e=__FILE__=/main.py)
	main2.py,f(e=__FILE__=/main2.py)
--#

--% /main2.py
import enum
import datetime, enum, json, os, pyperclip, subprocess, sys, tempfile, traceback
from dotenv import load_dotenv
import lark
from lark import (
	Lark,
	InlineTransformer,
)
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter
from prompt_toolkit import PromptSession
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.completion import WordCompleter, FuzzyWordCompleter
from prompt_toolkit.auto_suggest import (
	AutoSuggest, 
	AutoSuggestFromHistory, 
	Suggestion, 
	ThreadedAutoSuggest
)
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.formatted_text import ANSI, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import Validator
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard


schnelldir = '/home/usef/danger/ulib/schnell'
sys.path.extend([schnelldir, '..'])
from app.utils import (
	env_exist, env_get, env_int,
)
from app.dirutils import (
	ayah, joiner, here
)
from app.utils import (
	env_exist, env_get, env_int,
)

#################################################################
############# grammar
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
bahasa = f"""
keseluruhan: program
program: insn+
insn: "a" 	-> insn_a
| "b"				-> insn_b
| "c"				-> insn_c
HURUF_DIGIT: 			("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 		("_"|LETTER|DIGIT) 		("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 			("_"|LETTER) 				("_"|LETTER|DIGIT|" "|".")*
HURUF_COMMA: 			("_"|LETTER) 				("_"|LETTER|DIGIT|",")*

HURUF_PASSWORD: 	("_"|LETTER) 				("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"#"|"*")*
HURUF_HOST: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
{base_grammar}
"""
############# processor
class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions

def processor(code, debug):
	debug(f'* PROCESSOR: [{code}]')
	parser = Lark(bahasa, start='keseluruhan').parse
	transformer = TheProcessor()
	debug('='*80, code, '\n')
	parsed_tree = parser(code)
	transformed_tree = transformer.transform(parsed_tree)
	RootNode = AnyNode(type='root', label='root', output='', outputs=[])
	for insn in transformed_tree:
		debug(insn.pretty())
		for anak in insn.children:
			# debug(anak.data)
			nama = anak.data
			AnyNode(parent=RootNode, name=anak.data, type=anak.data, label=anak.data)

	return RootNode
#################################################################
############# generator
def generator(RootNode):
	print('* GENERATOR')
	print(RenderTree(RootNode))
#################################################################

class Lang(enum.Enum):
  CPP       = 'cpp'
  CS        = 'cs'
  CLJ       = 'clj'
  DART      = 'dart'
  ELIXIR    = 'elixir'
  ELM       = 'elm'
  ERLANG    = 'erlang'
  GO        = 'go'
  GROOVY    = 'groovy'
  HS        = 'hs'
  JAVA      = 'java'
  JS        = 'js'
  KT        = 'kt'
  PHP       = 'php'
  PL        = 'pl'
  PY        = 'py'
  R         = 'r'
  RB        = 'rb'
  RS        = 'rs'
  SCALA     = 'scala'
  SWIFT     = 'swift'
  TS        = 'ts'

  AWK       = 'awk'
  BASH      = 'bash'
  BATCH     = 'batch'
  CSS       = 'css'
  LESS      = 'less'
  SASS      = 'sass'
  SED       = 'sed'
languages = [item.value for item in Lang]
context = {
  'current_language'            : Lang.PY.value,
  'working_folder'              : None,
}
keluar = [
	'x', 'q', 'exit', 'quit', 'bye'
]
style = Style.from_dict(
	{
		"completion-menu.completion": "bg:#008888 #ffffff",
		"completion-menu.completion.current": "bg:#00aaaa #000000",
		"scrollbar.background": "bg:#88aaaa",
		"scrollbar.button": "bg:#222222",

		"username": "#884444 italic bg:#aaeeaa",
		"at": "#00aa00",
		"colon": "#00aa00 bold",
		"pound": "#00aa00",
		"host": "#000088 bg:#aaffaa",
		"path": "#6644ee underline bg:#aaeeaa",
		# Make a selection reverse/underlined.
		# (Use Control-Space to select.)
		"selected-text": "reverse underline",
	}
)
def complete(words, insensitive=True):
	return FuzzyWordCompleter(words)

class UlibSuggestion(AutoSuggest):
	def __init__(self, entries):
		self.entries = entries

	def get_suggestion(self, buff, document):
		# Consider only the last line for the suggestion.
		text = document.text.rsplit("\n", 1)[-1]
		if text.strip():
			for word_lines in self.entries:
				for word in word_lines.splitlines():
					if word.startswith(text):
						return Suggestion(word[len(text) :])

		return None

bindings = KeyBindings()
lokasi_history = '/home/usef/dahsyat/sejarah'

class Repl:
	
	def __init__(self):
		if env_exist('ULIBPY_HISTORY_FILE'):
			self.our_history = FileHistory(joiner(lokasi_history, 'template.hist'))
		
		self.previous_words = [
			'[usef:rahasia@gisel.ddns.net:9022/monyong]',
			'[usef:rahasia@gisel.ddns.net:9022/monyong]{@Delete=#100,ts}',
			'[usef:rahasia@gisel.ddns.net:9022/monyong]{@Delete=#100,ts}title,s,len=20',
		]
		self.done = False
		self.session = self.create_prompt_session(complete(self.previous_words), self.previous_words)

	def create_prompt_session(self, completer, suggest_words=None):
		if suggest_words:
			return PromptSession(
				auto_suggest=UlibSuggestion(suggest_words),
				history=self.our_history,
				key_bindings=bindings,
				completer=completer, 
				complete_while_typing=True,
				complete_style=CompleteStyle.MULTI_COLUMN,
				style=style
			)
		return PromptSession(
			history=self.our_history,
			key_bindings=bindings,
			completer=completer, 
			complete_while_typing=True,
			complete_style=CompleteStyle.MULTI_COLUMN,
			style=style
		)
	def temporary_prompt(self, 
		prompt_message=HTML("<b>Pilih <u>salah</u> <i>satu</i>: </b>"), 
		choices=languages):

		valid_langs = choices
		def isvalid(text):
			return text.lower() in [item.lower() for item in valid_langs]

		validator = Validator.from_callable(
			isvalid,
			move_cursor_to_end=True,
			error_message="Pilih salah satu "+str(valid_langs)
		)

		# ini tambah di config
		choices = sorted(choices)

		jawab = self.session.prompt(
			prompt_message,
			completer=FuzzyWordCompleter(choices),
			validator=validator, 
			validate_while_typing=True,
			clipboard=PyperclipClipboard(),
			style=style,
		)
		# print('Anda memilih:', jawab)
		self.change_completer(self.previous_words)
		return jawab
	@property
	def prompt(self):
		now = datetime.datetime.now()
		return HTML(
			# "<username>usef</username><at>@</at>"
			# f"""<host>{"%02d/%02d %02d:%02d:%02d" % (now.day, now.month, now.hour, now.minute, now.second)}</host>"""
			f"""<host>{"%s %02d/%s %02d:%02d:%02d" % (now.strftime('%a'), now.day, datetime.datetime.now().strftime('%j'), now.hour, now.minute, now.second)}</host>"""
			f" <path>[{env_get('ULIBPY_MKFILE_KEY')[:3]}]</path>"
			f"<username>{context['current_language']}</username>"
			"<colon>:</colon>"
			" "
		)
	def run(self):
		while not self.done:
			try:
				text = self.session.prompt(self.prompt, auto_suggest=AutoSuggestFromHistory())				
				if text in keluar:
					break				
				elif text:
					self.process(text)
			except KeyboardInterrupt:
				continue
			except EOFError:
				break
			except Exception as err:
				print('repl run() err:', err)
				print(traceback.format_exc())

	def process(self, text, strip=True):
		
		if strip:
			text = text.strip()

		print(f"process terima", text)
		
		if text .startswith ('chooselang'):
			text = text.replace('chooselang', '', 1).strip()
			jawab = ''
			if text == '':
				jawab = self.temporary_prompt()
			else:
				'''
				ambil pilihan berupa list dari args, lalu eval
				kita ambil choices saja, prompt/message blm diproses
				'''
				m = re.match(r'(\[.*\])', text)
				if m:
					pilihan = eval(m.group(1))
					if pilihan:
						jawab = self.temporary_prompt(choices=pilihan)
			print('Terima:', jawab)
		else:
			'''
			{@MyTable}username,s,Y;password,s,N,df=monyet,u,ai
			'''
			print('Ready to generate...')
			RootNode = processor(text, print)
			generator(RootNode)


repl = Repl()

@bindings.add("f12")
def _(event):
	event.app.current_buffer.insert_text("f12 ditekan...")

if __name__ == '__main__':
	try:
		repl.run()
	except Exception as err:
		print('terminal_repl.py:', err)
		print(traceback.format_exc())
--#

--% /main.py
import datetime, os, sys, traceback

# pyinstaller -F wmcer.py
# c:\work\ulibs\schnell\dist>wmcer.exe
#   'ULIBPY_BASEDIR' not in os.environ
#   perlu utk akses library fmus.

disini = os.path.dirname(__file__)
envfile = os.path.join(disini, '.env')

# perlu cek jk envfile not isfile
if not os.path.isfile(envfile):
  print(f'{envfile} not found')
  if sys.platform == 'win32':
    envfile = 'C:/work/ulibs/schnell/.env'
  else:
    envfile = '/home/usef/work/ulibs/schnell/.env'
  print(f'using {envfile}')

from dotenv import load_dotenv
load_dotenv(envfile)

# ./.env
# load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
# ../.env
# load_dotenv(os.path.join(os.path.dirname(__file__), os.pardir, '.env'))
# ULIBPY_BASEDIR=/home/usef/work/ulibs/schnell
if 'ULIBPY_BASEDIR' not in os.environ:
  print("""
  'ULIBPY_BASEDIR' not in os.environ
  perlu utk akses library fmus.
  """)
  sys.exit(0)

schnelldir = os.environ['ULIBPY_BASEDIR']
sys.path.extend([schnelldir, '..'])

from app.dirutils import (
	ayah, joiner, here
)
from app.printutils import print_json, indah3, indah4, print_copy
from app.utils import (
	faker, print_faker, printcopy_faker
)
from app.utils import trycopy, env_exist, env_reload, env_set
from app.treeutils import (
	child, child1, 
	anak, jumlahanak, beranak,
	data,
	token, chtoken, chdata,
)
from lark import (
	Lark,
	InlineTransformer,
)
from langs import base_grammar

main_language = """
program: statement+
statement: 
	| statement_config? csv_statement? backend_statement? frontend_statement?
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "i" 		-> info // info atau help, mengentai kode yg dioprek
	| "dj" 		-> be_django
	| "djm" 	-> be_django_mongo
	| "sb" 		-> be_springboot

backend_statement		: "B^" program_backend "^"
csv_statement				: "C^" program_csv "^"
frontend_statement	: "F^" program_frontend "^"

program_backend: HURUF_PROGRAM_BACKEND
program_csv: HURUF_PROGRAM_CSV

HURUF_CDATA: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|" "|";"|":"|"+"|"-")*
HURUF_NILAI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" ")*
HURUF_NILAI_BERSLASH: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*
HURUF_NILAI_BERSPASI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"`"|"{"|"}"|"("|")"|"="|" ")*
HURUF_NON_OPEN: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|","|" "|"+"|"="|"-"|"_"|"@"|"#"|"$"|"%"|"^"|"&"|"*")*
HURUF_KODE_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{"|"<") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*

HURUF_PROGRAM_BACKEND: ("_"|LETTER|DIGIT|"\\""|"{"|"[") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/"|","|";"|":"|"@"|"]"|"#")*
HURUF_PROGRAM_CSV: ("_"|LETTER|DIGIT|"\\""|"{"|"[") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/"|","|";"|":"|"@"|"["|"]"|"#"|"|")*
HURUF_PROGRAM_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*
"""

huruf = """
HURUF_DIGIT: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
"""

bahasa = f"""
{main_language}

{huruf}

{base_grammar}
"""

class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines

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
	print('handler:', data(tree))
	# print(tree.pretty())

	kembali = ''	
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'statement_config':
			res = statement_config(item)
			program_config.update(res)
		elif jenis == 'backend_statement':
			backend_statement(item)
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

def process_language(code):
	global program_config
	try:
		pre_parser = Lark(bahasa, start='program')
		parser = pre_parser.parse
		indah4('='*20 + ' ' + code + '\n', warna='red')
		parsed_tree = parser(code)
		instructions = TheProcessor().transform(parsed_tree)
		results = []

		for insn in instructions:

			if debug:
				print(insn.pretty())

			hasil = handler(insn)
			print('fullstack, hasil handler (jk ada):', hasil)
	except Exception as err:
		print(err)
		trace = traceback.format_exc()
		print(trace)

def main_repl(debug=True):
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
				from app.dirutils import joiner
				from app.utils import perintahsp_simple
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

def main_test():
	print_faker('paragraph', 100)

if __name__ == '__main__':
	main()
--#
