--% index/fmus
language-mania,d(/mk)
	main1.py,f(e=__FILE__=/main1.py)
	main2.py,f(e=__FILE__=/main2.py)
	main3.py,f(e=__FILE__=/main3.py)
	main4.py,f(e=__FILE__=/main4.py)
	main5.py,f(e=__FILE__=/main5.py)
	decl,d(/load=__CURDIR/decl.fmus=index/fmus)
	README.md,f(e=__FILE__=README.md)
	run.sh,f(n=python main1.py)
	$*chmod a+x run.sh
--#

--% README.md
bahasa apa yg mau kita kembangkan
bahasa test / tdd
	cypress, jasmine, karma, mocha, chai, jest, react-test-library,
	ngunit, junit,	
	unittest, pytest
	supertest, rainforest (baru denger)
bahasa image dan meme
	w tengah, tapi h bisa specify posisi dalam % dari 0 sampai 100%...
	juga ukuran font...
	bisa juga specify font: penuhi width
bahasa charts...pie, bar/column, line, area, ...
csvlang mau tambah: (csv=...kode...), (json=...kode...)
bahasa scraper/crawler
bahasa diagram
--#

--% /main1.py
import datetime, enum, json, os, pyperclip, subprocess, sys, tempfile, traceback
from dotenv import load_dotenv
import lark
from lark import (
	Lark,
	InlineTransformer,
)
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

# .
curdir = os.path.dirname(os.path.abspath(__file__))
# ..
pardir = os.path.abspath(os.pardir)
# ../..
grandpardir = os.path.dirname(pardir)
# ../../..
greatgrandpardir = os.path.dirname(grandpardir)

# if greatgrandpardir not in sys.path:
# 	sys.path.append(greatgrandpardir)

schnelldir = '/home/usef/danger/ulib/schnell'
sys.path.append(schnelldir)
from app.dirutils import (
	ayah, joiner
)
from app.utils import (
	env_exist, env_get, env_int,
)
load_dotenv(joiner(schnelldir, '.env'))

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
keseluruhan: insn+

insn: 

HURUF_DIGIT: 						("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 						("_"|LETTER) 		("_"|LETTER|DIGIT|" ")*
HURUF_COMMA: 						("_"|LETTER) 		("_"|LETTER|DIGIT|",")*

HURUF_SYSTEM: 					("_"|LETTER|DIGIT|"*"|"/"|"."|"\\"") 	(LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\"|"\"")*
HURUF_PASSWORD: 				("_"|LETTER) ("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"@"|"#"|"*")*
HURUF_HOST: 						("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@")*
{base_grammar}
"""

class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions

def process_language(code):
	running_configuration = {**default_configuration}

	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*80, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	for insn in instructions: # instructions adlh tuple
		for tree in insn.children: # insn adlh Tree
			print(tree.pretty())


# def myrepl():
# 	code = 1
# 	while code != 'x':
# 		try:
# 			code = input('myrepl>> ')
# 			code = code.strip()
# 			if code == 'bahasa':
# 				print(bahasa)
# 			elif code != '' and code != 'x':
# 				process_language(code)
# 		except EOFError as eof:
# 			print('Ctrl+D? Exiting...', eof)
# 			break
# 		except Exception as err:
# 			print(err)

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
  # 'current_chart'               : Chartlang.HIGHCHART.value,
  # 'current_gui'                 : Guilang.PYQT5.value,
  'current_language'            : Lang.PY.value,
  # mestinya jk invoke flutter program, nilai ini jg langsung berubah
  # 'current_mobile'              : Mobilelang.FLUTTER.value,
  # 'current_declarative'         : Declang.REACT.value,
  # 'print_after_process'         : True,
  # tujuannya utk generate file dll
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
		"host": "#000088 bg:#aaaaff",
		"path": "#6644ee underline bg:#aaeeaa",
		# Make a selection reverse/underlined.
		# (Use Control-Space to select.)
		"selected-text": "reverse underline",
	}
)
def complete(words, insensitive=True):
	return FuzzyWordCompleter(words)


default_configuration = {}
bindings = KeyBindings()

class Repl:
	def __init__(self):

		self.previous_words = ['gaia', 'wieke', 'katy']
		self.done = False
		if env_exist('ULIBPY_HISTORY_FILE'):			
			self.our_history = FileHistory(joiner(tempfile.gettempdir(), 'repl.hist'))
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


	def change_completer(self, words):
		self.previous_words = words		
		self.session = self.create_prompt_session(complete(words), words)


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

	def process(self, text):
		text = text.strip()
		print('process terima:', text)		
		
		if text == 'bahasa':
			print(bahasa)

		elif text .startswith ('chooselang'):
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

		elif text in self.session.completer.words:
			'''
			https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/prompt_toolkit/shortcuts/prompt.py
			dari promptsession kita ambil wordcompleter dg .completer
			https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/prompt_toolkit/completion/word_completer.py
			dari wordcompleter kita ambil list dg .words
			'''
			print('Within completer.words:', text)
			# process_language(text)


repl = Repl()

if __name__ == '__main__':
	# myrepl()
	try:
		repl.run()
	except Exception as err:
		print('terminal_repl.py:', err)
		print(traceback.format_exc())
--#

--% /main2.py
################## START: grammar.py
# from creator.grammar.base import base_grammar
# from lang.ucsv.grammar.base import base_grammar
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
keseluruhan: database
| redis_statement

database: dbconfig? redis_statement
dbconfig						: "[" userpass? hostport? dbspec "]"
userpass						: user ":" pass "@"
hostport						: host? ":" port
user								: HURUF
pass								: HURUF_PASSWORD
host								: HURUF_HOST
port								: BILBUL
dbspec							: "/" dbnumber
dbnumber						: BILBUL

redis_statement     : statement (insn_separator statement)*
insn_separator      : NEWLINE
	| ";"
statement           : operation ("," operation)*
operation           : operator opargs*
operator            : HURUF_DIGIT
opargs              : HURUF_DIGIT


HURUF_DIGIT: 						("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 			("_"|LETTER) 				("_"|LETTER|DIGIT|" "|".")*
HURUF_COMMA: 			("_"|LETTER) 				("_"|LETTER|DIGIT|",")*

HURUF_PASSWORD: 	("_"|LETTER) 				("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"#"|"*")*
HURUF_HOST: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
{base_grammar}
"""
################## END: grammar.py

# from .grammar import bahasa
from grammar import bahasa

import json, os, pyperclip, subprocess, sys
import lark
from lark import (
	Lark,
	InlineTransformer,
)


class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions


def process(code):
	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*80, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	for insn in instructions: # instructions adlh tuple
		for tree in insn.children: # insn adlh Tree
			print(tree.pretty())


from prompt_toolkit import prompt       
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from os.path import expanduser

myPromptSession = PromptSession(history = FileHistory(expanduser('/tmp/.langredishist')))

def main():
	code = 1
	while code != 'x':
		try:
			# code = input('myrepl>> ')
			code = myPromptSession.prompt('myrepl>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code != '' and code != 'x':
				process(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)

if __name__ == '__main__':
	main()
--#

--% /main3.py
import json, os, pyperclip, subprocess, sys
import lark
from lark import (
	Lark,
	InlineTransformer,
)
curdir = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.pardir)
grandpardir = os.path.dirname(pardir)
greatgrandpardir = os.path.dirname(grandpardir)
# print("$", curdir, pardir, grandpardir, greatgrandpardir)
# print(os.listdir(greatgrandpardir))
if greatgrandpardir not in sys.path:
	sys.path.append(greatgrandpardir)

default_configuration = {}
def dummy(*args, **kwargs):
	pass

# DEBUG=False
DEBUG=True
debug = print if DEBUG else dummy


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
keseluruhan: insn+

insn: 

HURUF_DIGIT: 						("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 						("_"|LETTER) 		("_"|LETTER|DIGIT|" ")*
HURUF_COMMA: 						("_"|LETTER) 		("_"|LETTER|DIGIT|",")*

HURUF_SYSTEM: 					("_"|LETTER|DIGIT|"*"|"/"|"."|"\\"") 	(LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\"|"\"")*
HURUF_PASSWORD: 				("_"|LETTER) ("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"@"|"#"|"*")*
HURUF_HOST: 						("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@")*
{base_grammar}
"""

class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions

def process_language(code):
	running_configuration = {**default_configuration}

	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*80, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	for insn in instructions: # instructions adlh tuple
		for tree in insn.children: # insn adlh Tree
			print(tree.pretty())


def YANGDINGINAQUAAQUA():
	print('***              YANGDINGINAQUAAQUA')
	code = 1
	while code != 'x':
		try:
			code = input('YANGDINGINAQUAAQUA>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	YANGDINGINAQUAAQUA()
--#

--% /main4.py
# from creator.grammar.base import base_grammar

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

redux_grammar = f"""
keseluruhan: statement (statement_separator statement)*
statement: store_statement
| reducer_statement
| action_statement

statement_separator: ";"

store_statement       : "dummy"
reducer_statement     : "dummy"
action_statement      : "@" action_types_statement

action_types_statement: action_type ("," action_type)*
action_type: action_type_compound_left
| action_type_compound_right
| action_type_simple

action_type_compound_left: "{{" part_items "}}" part_shared
action_type_compound_right: part_shared "{{" part_items "}}" 


action_type_simple: HURUF_DIGIT
part_shared: HURUF_DIGIT
part_items: part_item ("," part_item)*
part_item: HURUF_DIGIT

HURUF_DIGIT: 			      ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 		  ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
{base_grammar}
"""
import json, os, pyperclip, subprocess, sys
import lark
from lark import (
	Lark,
	InlineTransformer,
)

from redux_grammar import redux_grammar as bahasa

class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions


def process(code):
	parser = Lark(bahasa, start='keseluruhan').parse
	print('='*80, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	for insn in instructions: # instructions adlh tuple
		for tree in insn.children: # insn adlh Tree
			print(tree.pretty())


def main():
	code = 1
	while code != 'x':
		try:
			code = input('myrepl>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code != '' and code != 'x':
				process(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)

if __name__ == '__main__':
	main()
--#

--% /main5.py
import json, os, pyperclip, subprocess, sys
import lark
from lark import (
	Lark,
	InlineTransformer,
)
curdir = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.pardir)
grandpardir = os.path.dirname(pardir)
greatgrandpardir = os.path.dirname(grandpardir)
# print("$", curdir, pardir, grandpardir, greatgrandpardir)
# print(os.listdir(greatgrandpardir))
if greatgrandpardir not in sys.path:
	sys.path.append(greatgrandpardir)

default_configuration = {}
def dummy(*args, **kwargs):
	pass

# DEBUG=False
DEBUG=True
debug = print if DEBUG else dummy


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

bahasa = r"""
?keseluruhan: _NL* abaikan

abaikan: HURUF_FOLDER_SYSTEM _NL [_INDENT abaikan+ _DEDENT]
HURUF_FOLDER_SYSTEM: 		("_"|LETTER|DIGIT|"/"|"."|"@"|"$"|"%"|"#") (LETTER|DIGIT|"_"|"["|"]"|"*"|"."|":"|"/"|","|"("|")"|"+"|"-"|"_"|"="|" "|"%"|"$"|"@"|"\\"|"\"")*
%declare _INDENT _DEDENT
_NL: /(\r?\n[\t ]*)+/

HURUF_DIGIT: 						("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 						("_"|LETTER) 		("_"|LETTER|DIGIT|" ")*
HURUF_COMMA: 						("_"|LETTER) 		("_"|LETTER|DIGIT|",")*

HURUF_SYSTEM: 					("_"|LETTER|DIGIT|"*"|"/"|"."|"\\"") 	(LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\"|"\"")*
HURUF_PASSWORD: 				("_"|LETTER) ("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"@"|"#"|"*")*
HURUF_HOST: 						("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@")*
%s
""" % (base_grammar)

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


def treeify(tree, parent=None, level=0, workdir=''):
	current_node = parent
	for child in tree.children:
		print(TAB*level, 'oprek:', child)
		if isinstance(child, lark.lexer.Token):
			original = str(child)
			kembalian = process_folderline(original, level, workdir=workdir, ParentNode=current_node)
			if kembalian:
				current_node = kembalian
				workdir = current_node.workdir

		elif isinstance(child, lark.tree.Tree):
			debug(TAB*level, 'kondisi parent node skrg:', current_node)
			newlevel = level + 1
			treeify(child, parent=current_node, level=newlevel, workdir=workdir)

	return current_node


def process_language(code):
	parser = Lark(bahasa, start='keseluruhan', parser='lalr', postlex=TreeIndenter()).parse
	print('='*60, 'code:')
	print("[" + code + "]")
	tree = parser(code)
	print('-'*60, 'prettify for a white guy:\n')
	# print(tree.pretty())
	pohon = treeify(tree)
	
	if pohon:
		print('*'*80, 'Final:')
		# from krepl.filemanager.generator import generate
		# generate(run_configuration, pohon)
		# print(RenderTree(pohon))

sample_code = "i /i,p,n,a,dp,tp,s,rg,cg,l |d,phuruf,shuruf"

def YANGDINGINAQUAAQUA():
	print('***              YANGDINGINAQUAAQUA')
	print(f'=>				{sample_code}')
	code = 1
	while code != 'x':
		try:
			code = input('YANGDINGINAQUAAQUA>> ')
			code = code.strip()
			if code == 'bahasa':
				print(bahasa)
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	YANGDINGINAQUAAQUA()
--#
