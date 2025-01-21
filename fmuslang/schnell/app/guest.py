import datetime, threading

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import ANSI, HTML
# from prompt_toolkit.shortcuts import CompleteStyle, prompt
from prompt_toolkit.shortcuts import CompleteStyle
# from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.application.current import get_app
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.validation import Validator
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
from prompt_toolkit.completion import WordCompleter, FuzzyWordCompleter
# https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/examples/prompts/custom-key-binding.py
from prompt_toolkit.application import run_in_terminal
from .fileutils import (
	get_daftar,
	get_extension,
	get_definition,
	get_definition_permissive_start,
	get_definition_by_key_permissive_start,
)
from .utils import *
from .suggestion import UlibSuggestion
from .completer import complete, fake_completer
from .codehandler import FILENAMES
from .communication import start_client
from multiprocessing.connection import Listener

GUEST_CLI_HOST = 'localhost'
GUEST_CLI_PORT = 17101
GUEST_CLI_PASS = b'rahasia'

keluar = [
	'x', 'q', 'exit', 'quit', 'bye'
]

style = Style.from_dict(
	{
		"completion-menu.completion": "bg:#008888 #ffffff",
		"completion-menu.completion.current": "bg:#00aaaa #000000",
		"scrollbar.background": "bg:#88aaaa",
		"scrollbar.button": "bg:#222222",

		"username": "#884444 italic",
		"at": "#00aa00",
		"colon": "#00aa00",
		"pound": "#00aa00",
		"host": "#000088 bg:#aaaaff",
		"path": "#884444 underline",
		# Make a selection reverse/underlined.
		# (Use Control-Space to select.)
		"selected-text": "reverse underline",
	}
)

bindings = KeyBindings()

@bindings.add("f3")
def _(event):
	"""
	event adlh KeyPressEvent
	yg di dalamnya punya:
	self._app = get_app()
	get_app
	from prompt_toolkit.application.current import get_app
	berarti punya current_buffer
	get_app diperoleh dari:
	session = _current_app_session.get()		
	return session.app
	session dari: session = AppSession(input=input, output=output)

	./prompt_toolkit/application/application.py:    
	def current_buffer(self) -> Buffer:
		yg adlh:
	return self.layout.current_buffer or Buffer(
		name="dummy-buffer"
	)
	./prompt_toolkit/layout/layout.py:    
	def current_buffer(self) -> Optional[Buffer]:
	dan ternyata: misal jk text_area punya focus...maka dia adlh current_buffer
	makanya punya/bisa insert_text spt ini.
	jadi pada dasarnya bisa
	app.focus(text-area-element) abis itu bisa akses dia setara dg:
	app.current_buffer
	"""
	event.app.current_buffer.insert_text("launch f3")

# @bindings.add("f4")
# def _(event):
# 	event.app.current_buffer.insert_text("launch f4")

# @bindings.add("'", "f")
# def _(event):
# 	event.app.current_buffer.insert_text("for di semua bahasa")


# @bindings.add("'", "l")
# def _(event):
# 	event.app.current_buffer.insert_text("loop di semua bahasa")


class Repl:
	def __init__(self):
		# print('repl obj created...')
		self.done = False
		if env_exist('ULIBPY_HISTORY_FILE'):
			self.our_history = FileHistory(env_get('ULIBPY_HISTORY_FILE'))
		else:
			self.our_history = FileHistory('delete_me')
		
		self.internal_commands = [
			'cls', 'clear',
			'out', 'output',
			'msg', 'message',
		]
		self.previous_words = self.internal_commands
		self.session = self.create_prompt_session(complete(self.previous_words), self.previous_words)
		self.current_completer_source = None
		self.current_toc = None
		self.start_rpc_server()
		# bindings.add('f4')(self.choose_language)
		

	def xcursing(self, filepath):
		if get_extension(filepath) == 'mk':
			daftar = get_daftar(filepath)
			self.current_toc = daftar

			# ini suka gak berjalan di invoke pertama
			# mungkin perlu kirim \n dulu ke self.session
			self.change_completer(daftar)

			self.current_completer_source = filepath
			self.client.comm_handler(daftar)

	def choose_language(self, event=None):
		style = Style.from_dict(
			{
				"bottom-toolbar": "#aaaa00 bg:#ff0000",
				"bottom-toolbar.text": "#aaaa44 bg:#aa4444",
			}
		)
		self.session.prompt(
			HTML("<b>Pilih <u>bahasa</u>: </b>"), 
			accept_default=True, 
			default="python",
			style=style,
			bottom_toolbar=HTML(
				'(html) <b>Masukkan bahasa untuk kompilasi</b><style bg="ansired"> and shit</style>'
			)
		)

	def process_wmc_message(self, msg):
		if isinstance(msg, str):
			print('Guest CLI menerima str:', msg)
		elif isinstance(msg, list):
			print('Guest CLI menerima list:', msg)
		elif isinstance(msg, dict):
			# print('Guest CLI menerima dict:', msg)
			if 'type' in msg:
				if msg['type'] == 'xcurse':
					filepath = msg['filepath']
					# print('xcursing:', filepath)
					self.xcursing(filepath)
				elif msg['type'] == 'prompt':
					message = msg['message']
					choices = msg['choices']
					print(f'Guest CLI: prompt to user: {message} with {choices}')

	def start_rpc_server_internal(self):		
		address = (GUEST_CLI_HOST, GUEST_CLI_PORT)
		listener = Listener(address, authkey=GUEST_CLI_PASS)
		# print ('Guest CLI RPC Server listen at:', address)
		conn = listener.accept()
		# print ('Guest CLI RPC Server menerima:', listener.last_accepted)
		while True:
			msg = conn.recv()
			self.process_wmc_message(msg)
			if msg == 'close':
				conn.close()
				break
		listener.close()

	def start_rpc_server(self):
		threading.Thread(target=self.start_rpc_server_internal).start()

	# def wmc_to_guest(self, filepath):
	# 	print('guest cli menerima filepath to oprek dari wmc:', filepath)

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
		# coba
		# self.session.default_buffer.insert_text('new completer\n')
		# self.session.default_buffer.insert_text('new completer\n')
		# self.session.default_buffer.text = "ready"

	def temporary_prompt(self, prompt_message=HTML("<b>Pilih <u>salah</u> <i>satu</i>: </b>"), choices=FILENAMES):
		if not FILENAMES:
			from .codehandler import assign_filenames
			FILENAMES = assign_filenames(env_get('ULIBPY_BASEDIR'))
		valid_langs = choices
		def isvalid(text):
			return text.lower() in valid_langs
		validator = Validator.from_callable(
			isvalid,
			move_cursor_to_end=True,
			error_message="Pilih salah satu "+str(valid_langs)
		)
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
			f"""<host>{"%02d %02d:%02d:%02d" % (now.day, now.hour, now.minute, now.second)}</host>"""
			"<colon>:</colon>"
			" "
		)

	def run(self):
		self.client = start_client()
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
				print('guest.py err:', err)

	def process(self, text, strip=True):
		if strip:
			text = text.strip()

		if text == 'complete1':
			self.change_completer(fake_completer)
		elif text == 'complete2':
			self.change_completer(sql_keywords)
		elif text == 'toc':
			if self.current_toc:
				res = self.client.comm_handler(self.current_toc)
		elif text .startswith ('chooselang'):
			text = text.replace('chooselang', '', 1).strip()
			jawab = ''
			if text == '':
				jawab = self.temporary_prompt()
			else:
				'kita ambil choices saja, prompt/message blm diproses'
				import re
				m = re.match(r'(\[.*\])', text)
				if m:
					pilihan = eval(m.group(1))
					if pilihan:
						jawab = self.temporary_prompt(choices=pilihan)
						
			
			self.client.comm_handler({
				'type': 'language_choice',
				'choice': jawab
			})

		elif text .startswith ('chooseentry'):
			text = text.replace('chooseentry', '', 1).strip()
			jawab = ''
			if text == '':
				jawab = self.temporary_prompt()
			else:
				'kita ambil choices saja, prompt/message blm diproses'
				import re
				m = re.match(r'(\[.*\])', text)
				if m:
					pilihan = eval(m.group(1))
					if pilihan:
						jawab = self.temporary_prompt(choices=pilihan)
						self.client.comm_handler({
							'type': 'entry_choice',
							'choice': jawab
						})
			
			# print(f'Aku terima {jawab} dari Anda.')

		elif text in self.internal_commands+['c']:
			'''as is'''
			if text == 'c':
				text = 'cls'
			res = self.client.comm_handler(text)
		elif text in self.session.completer.words:
		# elif text in self.current_toc+self.internal_commands:
			'''
			https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/prompt_toolkit/shortcuts/prompt.py
			dari promptsession kita ambil wordcompleter dg .completer
			https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/prompt_toolkit/completion/word_completer.py
			dari wordcompleter kita ambil list dg .words
			'''
			# print('debug in completer.words #1')
			if self.current_completer_source:
				# print('debug in completer.words #2')
				# ada escape char di text kita escape dulu
				escape_me = ['+', '-', '*', '$', '^', '[', ']', '(', ')']
				if any([item for item in escape_me if item in text]):
					for item in escape_me:
						text = text.replace(item, '\\'+item)

				text = get_definition_by_key_permissive_start(self.current_completer_source, text)

			# print('debug in completer.words #3')
			if text:
				# print('debug in completer.words #4')
				res = self.client.comm_handler(text)

			# print('debug in completer.words #5')

if __name__ == '__main__':
	repl = Repl()
	try:
		repl.run()
	except Exception as err:
		print('guest.py err', err)

