import json, subprocess, sys, time
import asyncio, pdb
from enum import Enum
import os, shutil, threading

from pygments.lexers.html import HtmlLexer
from pygments.lexers.python import PythonLexer
from prompt_toolkit.lexers import DynamicLexer, PygmentsLexer
# lexer=PygmentsLexer(HtmlLexer)

from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.application import run_in_terminal
# from prompt_toolkit.layout import Layout, VSplit, HSplit, Window
# from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.processors import TabsProcessor
from prompt_toolkit.filters import Condition
from prompt_toolkit.layout.containers import (
	ConditionalContainer,
	Float,
	HSplit,
	VSplit,
	Window,
	WindowAlign,
)
from prompt_toolkit.layout.margins import NumberedMargin, ScrollbarMargin
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import (
	Box,
	Button,
	Checkbox,
	# CheckboxList,
	Dialog,
	Frame,
	HorizontalLine,
	Label,
	MenuContainer,
	MenuItem,
	ProgressBar,
	RadioList,
	ArgToolbar,CompletionsToolbar,FormattedTextToolbar,
	SearchToolbar,SystemToolbar,ValidationToolbar,
	Shadow,
	TextArea,
	VerticalLine,
)
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.application.current import get_app
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.document import Document
from prompt_toolkit.filters import (
		# Condition,
		# FilterOrBool,
		has_focus,
)
# from prompt_toolkit.clipboard import InMemoryClipboard
# from prompt_toolkit.history import InMemoryHistory
# from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from prompt_toolkit import prompt
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard

from schnell.vendor.ptterm import Terminal

from multiprocessing.connection import Client
# if platform() not in ['termux']:
# 	from multiprocessing.connection import Client

from .appconfig import programming_data
from .dirutils import ayah, isfile, joiner
from .fileutils import write_file, append_file, mk_file_to_dict
from .codehandler import CodeHandler
from .completer import create_meta_completer
from .suggestion import UlibSuggestion
# from .utils import platform
from .utils import (
	trycopy,
	env_get, env_exist, env_add,
	import_from_string,
	platform,
)
from .commander import Commander
from .peta import keys_mapping


GUEST_CLI_HOST = 'localhost'
GUEST_CLI_PORT = 17101
GUEST_CLI_PASS = b'rahasia'

style = Style([
	('terminal focused',    'bg:#aaaaaa'),
	('title',               'bg:#000044 #ffffff underline'),
	("status", "reverse"),
	("shadow", "bg:#440044"),
	
	# user dialog 1 line text area
	("input-field", "bg:#000000 #ffffff"),
])

APPLICATION_TITLE = ' [ WMP by Fulgent ]'
TAB_LEN = 2
bindings = KeyBindings()

@bindings.add('c-x', eager=True)
def _(event):
	event.app.exit()

bindings.add("c-right")(focus_next)
bindings.add("c-left")(focus_previous)

# https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html
# pilihan utk control: c-delete c-_ c-^ c-] c-@ (ini sama dg ctrl+space) c-m (enter) c-i (tab)
# c-left, c-right, c-up, c-down
# s-left, s-right, s-up, s-down
# s-delete, s-tab
# juga: left, right, up, down, escape, dan std: home, end, delete, pageup, pagedown, insert
@bindings.add("c-\\", "<any>")
def _(event):
	for item in event.key_sequence:
		print(item) # keypress(key='a') dst.
		if item.key == 'a':
			print('anda tekan ctrl backslash a')


from .lexerlist import lexer_list, language_from_lexer

class UserDialog(Enum):
	RADIO = 1
	INPUT = 2
	SINGLE_LINE = 3
	MULTI_LINE = 4
	TERMINAL = 5

class Repl:

	def terminal_exit(self):
		self.application.exit()

	def create_output_terminal(self):
		return Terminal(
			# command = ['/bin/bash'],
			command = ['python', '-mapp.wmc'],
			# height=D(preferred=5),
			# scrollbar=True,
			done_callback=self.close_output,
		)

	def __init__(self):
		self.done = False
		self.show_output_terminal = False
		self.show_guest_cli = True
		self.show_editor = True
		self.show_user_dialog = False
		self.active_dialog = UserDialog.RADIO
		self.show_status_bar = True
		self.show_commander = False

		self.current_file_saved = None

		ukuran = shutil.get_terminal_size()
		self.maxw = ukuran.columns
		self.maxh = ukuran.lines
		self.statusbar_text = ' Tekan Ctrl+X keluar'

		# https://github.com/prompt-toolkit/ptterm/blob/master/ptterm/terminal.py
		self.terminal = Terminal(
			# command=['python', '-mapp.repl_backend'],
			command = ['python', '-mapp.guest'],
			# command=['python','-c','"print(42);input(\"...\")"'],
			# command=['python', '-c', 'print("test")'],
			# command=['python'],
			# width=D(preferred=int(self.maxw * .25)),
			width=D(),
			# height=D(preferred=25),
			done_callback=self.terminal_exit
		)
		self.output_terminal = self.create_output_terminal()

		self.output = ConditionalContainer(
			content=Frame(self.output_terminal, title='WMC'),
			filter=Condition(lambda: self.show_output_terminal),
		)
		self.text_area = TextArea(
			lexer=DynamicLexer(
				lambda: PygmentsLexer.from_filename(
					# ApplicationState.current_path or 
					".txt", sync_from_start=False
				)
			),
			focus_on_click=True,
			input_processors=[TabsProcessor(TAB_LEN)],
			scrollbar=True,
			line_numbers=True,
		)

		self.radios = RadioList(values=lexer_list)
		self.settings = {
			'radios': None,
			'checkboxes': None,
			'input': None,
			'yes_no_maybe': None,
		}
		# self.user_input = input_dialog(title='Input', text='Enter yo!')
		def cbify(nomer):
			return Checkbox(text='Setting %d'%nomer)
		
		checkboxes = list(map(cbify, [1,2,3,4]))
		self.user_input = HSplit(checkboxes)

		# harus dimasukkan bersama single_line_input dg HSplit
		# search_field = SearchToolbar()

		# jk kita langsung TextArea selalu gagal
		self.single_line_input = Frame(
			title='Input filename then Enter',
			body=TextArea(
				prompt=">>> ",
				style="class:input-field",
				height=1,
				# focusable=True,
				# accept_handler=self.input_dari_user,
				multiline=False,
				wrap_lines=False,
			),
		)

		self.small_terminal = Terminal(
			# command = eval(env_get('ULIBPY_SMALL_TERM_CMD')),
			command = ['bash'],
			width=D(preferred=20),
			done_callback=self.recreate_small_terminal
		)

		# semua control utk user dialog masuk sini
		self.radio_input = HSplit([
			ConditionalContainer(
				content=self.radios,
				filter=Condition(lambda: self.active_dialog == UserDialog.RADIO)
			),
			ConditionalContainer(
				content=self.user_input,
				filter=Condition(lambda: self.active_dialog == UserDialog.INPUT)
			),
			# ConditionalContainer(
			# 	content=self.single_line_input,
			# 	filter=Condition(lambda: self.active_dialog == UserDialog.SINGLE_LINE)
			# ),
			ConditionalContainer(
				content=self.small_terminal,
				filter=Condition(lambda: self.active_dialog == UserDialog.TERMINAL)
			),
		])
		self.user_dialog = ConditionalContainer(
			content=Frame(body=self.radio_input),
			filter=Condition(lambda: self.show_user_dialog),
		)

		# kita pake wrapper krn kita butuh akses text-area langsung utk ubah text
		self.text_area_wrapper = ConditionalContainer(
			content=self.text_area,
			filter=Condition(lambda: self.show_editor),
		)
		self.text_area_and_dialog = HSplit([
			# Window(
			# 	content=self.user_dialog,
			# ),

			self.text_area_wrapper,
			self.user_dialog,
		])
		# agar bisa ctrl+g utk toggle terminal utama = guest cli
		self.terminal_wrapper = ConditionalContainer(
			content=self.terminal,
			filter=Condition(lambda: self.show_guest_cli),
		)
		# self.commander = Commander('Enter command:')
		self.commander = Frame(
			title='Enter command',
			body=TextArea(
				prompt=">>> ",
				style="class:input-field",
				height=1,
				focusable=True,
				accept_handler=self.input_dari_user,
				multiline=False,
				wrap_lines=False,
			),
		)

		our_layout = Layout(
			container=HSplit([
				Window(
					height=1,
					style='class:title',
					content=FormattedTextControl(APPLICATION_TITLE)),
				VSplit([

					# self.terminal,
					HSplit([
						self.terminal_wrapper,
						self.output,
					]),

					Window(style='bg:#aaaaff', width=1),
					self.text_area_and_dialog,
				]),
				ConditionalContainer(
					content=self.commander,
					filter=Condition(lambda: self.show_commander),
				),
				# statusbar
				ConditionalContainer(
					content=VSplit(
						[
							Window(
								FormattedTextControl(self.statusbar_text), style="class:status"
							),
							Window(
								FormattedTextControl(self.get_statusbar_right_text),
								style="class:status.right",
								width=9,
								align=WindowAlign.RIGHT,
							),
						],
						height=1,
					),
					filter=Condition(lambda: self.show_status_bar),
				),
			]),
			focused_element=self.terminal
		)

		self.application = Application(
			layout=our_layout,
			style=style,
			key_bindings=merge_key_bindings([
				# load_key_bindings(),
				bindings,
			]),
			full_screen=True,
			mouse_support=True,
		)

		self.codehandler = CodeHandler()
		self.init_key_bindings()
		self.init_rpc_server_thread()		
		self.setup_polyglot_handler()
		
	def get_statusbar_text(self):
		status = " Ctrl+X keluar"
		if self.settings['radios']:
			status += ' | Radio = ' + self.settings['radios']
		return status

	def get_statusbar_right_text(self):
		return " {}:{}  ".format(
			self.text_area.document.cursor_position_row + 1,
			self.text_area.document.cursor_position_col + 1,
		)

	def close_output(self):
		self.show_output_terminal = False
		# self.output_terminal = self.create_output_terminal()

	def recreate_small_terminal(self):
		command = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SMALL_TERM_CMD"] # eval(env_get('ULIBPY_SMALL_TERM_CMD'),)
		self.active_dialog = UserDialog.RADIO
		self.toggle_dialog()
		self.application.layout.focus(self.text_area)
		# ini malah ngehang...
		# self.small_terminal = Terminal(
		# 	# command = ['python', '-mapp.prompter', '2'],
		# 	command = command,
		# 	width=D(preferred=20),
		# 	done_callback=self.recreate_small_terminal
		# )


	def toggle_editor(self, event=None):
		self.show_editor = not self.show_editor
		if self.show_editor:
			self.application.layout.focus(self.text_area)

	def toggle_guest(self, event=None):
		self.show_guest_cli = not self.show_guest_cli
		if self.show_guest_cli:
			self.application.layout.focus(self.terminal)

	def toggle_output(self, event=None):
		self.show_output_terminal = not self.show_output_terminal
		if self.show_output_terminal:
			self.application.layout.focus(self.output_terminal)

	def toggle_commander(self, event=None):
		self.show_commander = not self.show_commander
		if self.show_commander:
			self.application.layout.focus(self.commander)

	def toggle_dialog(self, event=None):
		self.show_user_dialog = not self.show_user_dialog
		if self.show_user_dialog:
			self.settings['radios'] = self.radios.current_value
			if self.radios.current_value:
				raw_lexer = import_from_string(self.radios.current_value)
				self.text_area.lexer = PygmentsLexer(
					raw_lexer, 
					# sync_from_start=False,
				)
			self.application.layout.focus(self.radios)

	def log(self, content):
		if isinstance(content, list):
			run_in_terminal(lambda: print(*content))
		else:
			run_in_terminal(lambda: print(content))

	def lihat(self, event=None):
		run_in_terminal(input)

	def try_apply_completer(self, bahasa):
		workfolder = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SCHNELL_COMPLETERDIR"] # env_get('ULIBPY_SCHNELL_COMPLETERDIR')
		filepath = joiner(ayah(__file__, 2), workfolder, bahasa + '.mk')
		if isfile(filepath):
			'''
			bikin completer dg display dan display_meta
			'''
			completer_dict = mk_file_to_dict(filepath)
			MyCompleter = create_meta_completer(completer_dict)

			# self.log(json.dumps(completer_dict, indent=4))

			self.text_area.complete_while_typing = True
			self.text_area.complete_style = CompleteStyle.MULTI_COLUMN
			# isi completer dan suggestion
			self.text_area.completer = MyCompleter
			# ternyata jadi total mess utk multiline suggestion
			# self.text_area.auto_suggest = UlibSuggestion(list(completer_dict.keys()))

	def apply_lexer_completion(self, event=None):
		"""
		self.radios = RadioList = DialogList punya
		values = [ (1,2), (1,2), ... ]
		current_values
		current_value = values [index] [0]
		kita butuh values [index] [1] utk akses label dari radio terpilih
		"""
		lexer = self.radios.current_value
		
		if lexer:
			raw_lexer = import_from_string(lexer)
			self.text_area.lexer = PygmentsLexer(
				raw_lexer, 
				# sync_from_start=False,				
			)
			bahasa = self.radios.values[self.radios._selected_index][1]
			# self.log('Harusnya skrg setup auto fuzzy completion utk bahasa: '+bahasa)
			self.try_apply_completer(bahasa)

	def clear(self):
		self.text_area.text = ''

	def comm_handler(self, keyword):
		if isinstance(keyword, list):
			result = '\n'.join(keyword)
			result += '\n'
			self.text_area.buffer.insert_text(result)
			
		elif isinstance(keyword, str):
			if keyword == 'clear' or keyword == 'cls':
				self.clear()
			elif keyword == 'bash':
				os.system('/bin/bash')
			elif keyword == 'output' or keyword == 'out':
				self.toggle_output()
			elif keyword .startswith('msg'):
				text = keyword.replace('msg', '', 1).strip()
				# Event loop is already running
				# hrs cari tau gimana attach???
				message_dialog(
					title="From client/guest",
					text=text,
				).run()
			else:
				# result = "server berhasil memproses " + keyword
				# result += '\n'
				result = keyword + '\n'
				self.text_area.buffer.insert_text(result)
				trycopy(result)

		elif isinstance(keyword, dict):
			# self.log('terima dari term utk apply lexer..')
			if 'type' in keyword:
				if keyword['type'] == 'apply_lexer':
					'mulanya dari c-] mengirim chooselang ke output terminal/wmc'
					'siapa yg ngirim? dari wmc dg chooselang -> radio dialog'
					bahasa = keyword['language']
					lexer = keyword['lexer']
					if lexer:
						raw_lexer = import_from_string(lexer)
						self.text_area.lexer = PygmentsLexer(raw_lexer)
				elif keyword['type'] == 'save_filename':
					filename = keyword['filename']
					content = self.text_area.text
					self.save_file(filename, content)
					self.statusbar_text = f"| File {filename} saved"
				elif keyword['type'] == 'hapus_baris':
					start_end = keyword['args'] # [start] atau [start,end]
					self.delete_lines(start_end)
					self.statusbar_text = f"Baris {start_end} deleted"
				elif keyword['type'] == 'language_choice':
					'guest cli mengirim ini stlh user memilih entry bhs mana yg mau diaktifkan'
					'tdk ada informasi lexer di sini'
					bahasa = keyword['choice']
					# print('host/codehandler: harusnya set filename ke:', bahasa)
					self.codehandler.set_filename(bahasa)
					lexer = language_from_lexer(bahasa)
					if lexer:
						raw_lexer = import_from_string(lexer)
						self.text_area.lexer = PygmentsLexer(raw_lexer)
				elif keyword['type'] == 'entry_choice':
					'''stlh guestcli menerima pilihan entry mana utk ditampilkan di editor
					host menerima entry_choice
					manggil handler utk dapatkan entry for baris in current filename
					'''
					choice = keyword['choice']
					text = self.codehandler.entry_for_line(choice)
					if text:
						self.write_editor(text)
						# self.show_editor = True
						# self.text_area.buffer.insert_text(text)

	def init_rpc_server_thread(self):
		from .communication import create_rpc_handler, start_server
		handler = create_rpc_handler()
		handler.register_function(self.comm_handler)
		server = threading.Thread(target=start_server, args=(handler,))
		server.start()

	def init_key_bindings(self):
		"""
		https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html
		https://www.gitmemory.com/issue/prompt-toolkit/python-prompt-toolkit/675/488088463
		bisa pake:
		s-delete
		s-tab
		c-left					dan s- ekivalen
		c-right
		c-up
		c-down
		c-@ = c-space
		c-h = backspace
		c-i = tab
		c-m = enter
		
		
		
		tambah:
		s-tab
		home,end,pageup dan pagedown jg pake agar bs digunakan texteditor
		"""
		# ini perlu ? gak perlu lagi, gunakan ctrl left/right
		# bindings.add('c-w')(self.switch_focus_wrapper)
		
		bindings.add('c-e')(self.toggle_editor)
		bindings.add('c-f')(self.go_fullscreen)
		bindings.add('c-g')(self.toggle_guest)
		bindings.add('c-o')(self.toggle_output)
		bindings.add('c-s')(self.save_current_filename)
		bindings.add('c-s', 'a')(self.write_to_output_terminal)
		bindings.add('c-u')(self.toggle_dialog)
		bindings.add('c-v')(self.paste_to_text_area)
		bindings.add('c-y')(self.copy_editor)

		bindings.add('c-]')(self.write_to_output_terminal)		
		bindings.add('c-\\')(self.toggle_commander)
		# butuh tekan ctrl+shift
		bindings.add('c-_')(self.lihat)
		bindings.add('c-@')(self.write_to_guest_cli_terminal)
		bindings.add('c-^')(self.apply_lexer_completion)

		# harus bisa toggle bindings.add dan bindings.remove		
		# bindings.add('c-i')(self.handle_tab)
		# terpaksa insert jadi tab
		bindings.add('insert')(self.handle_tab)
		# tab dibutuhkan oleh guest.cli
		# bindings.add('tab')(self.handle_tab)

		# bisa dipetakan ke 2 keys berbeda, tapi handler bisa membedakan
		# chooselang (lexer) vs choosefile (save)			
		# bindings.add('c-s')(self.try_save_editor) # perlu juga copy ke clipboard		
		# lexer + completer/suggestion
		# bisa hapus 2 digit, koma, 2 digit = 5
		# bindings.add('s-delete', '<any>', '<any>', '<any>', '<any>', '<any>')(self.delete_lines)
		# bisa hapus sampai 2 digit
		# bindings.add('c-delete', '<any>', '<any>', '<any>')(self.delete_line)
		# agar bisa handle 1 digit atau 2 digit:
		bindings.add('c-delete', '<any>', '<any>')(self.delete_line)
		bindings.add('c-delete', '<any>')(self.delete_line)
		bindings.add('s-right')(self.open_content_in_editor)
		bindings.add('c-up')(self.cursor_up)
		bindings.add('c-down')(self.cursor_down)

		# escape, u setara dg alt+u
		bindings.add('escape', 'u', '<any>')(self.cycle_user_dialog)
		prefix = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SCHNELL_POLYGLOT_KEY"] # env_get('ULIBPY_SCHNELL_POLYGLOT_KEY')
		bindings.add(prefix, '<any>')(self.polyglot_handler)

	def setup_polyglot_handler(self):
		def internal(pesan):
			self.log(pesan)
			self.lihat()

		def handle_key(key='q', special_key=False):
			"""
			kita bikin special key ~ utk toc
			"""
			res = self.codehandler.handle(key)
			if special_key:
				self.write_editor('\n'.join(res))
			elif len(res) == 1:
				result = res[0]
				result = self.codehandler.entry_for_line(result)
				self.write_editor(result)
			elif len(res) > 1:
				# self.log(['Ada banyak hasil:', res, 'mesti minta prompt ke guest cli utk pilih'])
				choices = str(res)
				self.write_terminal_guest(f"chooseentry {choices}\n")

		keys_mapping['q'] = lambda: handle_key('q')
		keys_mapping['w'] = lambda: handle_key('w')
		keys_mapping['e'] = lambda: handle_key('e')
		keys_mapping['r'] = lambda: handle_key('r')

		keys_mapping['t'] = lambda: handle_key('t')
		keys_mapping['y'] = lambda: handle_key('y')
		keys_mapping['u'] = lambda: handle_key('u')
		keys_mapping['i'] = lambda: handle_key('i')
		keys_mapping['o'] = lambda: handle_key('o')
		keys_mapping['p'] = lambda: handle_key('p')
		
		keys_mapping['a'] = lambda: handle_key('a')
		keys_mapping['s'] = lambda: handle_key('s')
		keys_mapping['d'] = lambda: handle_key('d')
		keys_mapping['f'] = lambda: handle_key('f')
		keys_mapping['g'] = lambda: handle_key('g')
		keys_mapping['h'] = lambda: handle_key('h')
		keys_mapping['j'] = lambda: handle_key('j')
		keys_mapping['k'] = lambda: handle_key('k')
		keys_mapping['l'] = lambda: handle_key('l')
		keys_mapping['z'] = lambda: handle_key('z')
		keys_mapping['x'] = lambda: handle_key('x')
		keys_mapping['c'] = lambda: handle_key('c')
		keys_mapping['v'] = lambda: handle_key('v')
		keys_mapping['b'] = lambda: handle_key('b')
		keys_mapping['n'] = lambda: handle_key('n')
		keys_mapping['m'] = lambda: handle_key('m')
		keys_mapping['left'] = lambda: handle_key('left')
		keys_mapping['up'] = lambda: handle_key('up')
		keys_mapping['down'] = lambda: handle_key('down')
		keys_mapping['right'] = lambda: handle_key('right')
		keys_mapping['1'] = lambda: handle_key('1')
		keys_mapping['2'] = lambda: handle_key('2')
		keys_mapping['3'] = lambda: handle_key('3')
		keys_mapping['4'] = lambda: handle_key('4')
		keys_mapping['5'] = lambda: handle_key('5')
		keys_mapping['6'] = lambda: handle_key('6')
		keys_mapping['7'] = lambda: handle_key('7')
		keys_mapping['8'] = lambda: handle_key('8')
		keys_mapping['9'] = lambda: handle_key('9')
		# def insert():
		# 	get_app().current_buffer.insert_text("inserting 0")
		# keys_mapping['0'] = insert
		keys_mapping['0'] = lambda: handle_key('0')
		keys_mapping['-'] = lambda: handle_key('-')
		keys_mapping['='] = lambda: handle_key('=')
		keys_mapping['['] = lambda: handle_key('[')
		keys_mapping[']'] = lambda: handle_key(']')
		keys_mapping['\\'] = lambda: handle_key('\\')
		keys_mapping['|'] = lambda: handle_key('|')
		keys_mapping[';'] = lambda: handle_key(';')
		keys_mapping["'"] = lambda: handle_key("'")
		keys_mapping[','] = lambda: handle_key(',')
		keys_mapping['.'] = lambda: handle_key('.')
		keys_mapping['/'] = lambda: handle_key('/')
		keys_mapping['`'] = lambda: handle_key('`')

		keys_mapping['~'] = lambda: handle_key('~', special_key=True) # toc

	def go_fullscreen(self, event):
		"antara: text_area, terminal dan output_terminal"
		if has_focus(self.text_area)():
			self.show_guest_cli = False
			self.show_output_terminal = False
		elif has_focus(self.terminal)():
			self.show_editor = False
			self.show_output_terminal = False
		elif has_focus(self.output_terminal)():
			self.show_editor = False
			self.show_guest_cli = False
		else:
			# default utk editor
			self.show_editor = True

	def polyglot_handler(self, event):
		pilihan = event.key_sequence[1].key
		if pilihan in keys_mapping.keys():
			if keys_mapping[pilihan]:
				keys_mapping[pilihan]()

	def prompt_handler(self, event):
		pilihan = event.key_sequence[1].key
		if pilihan == '0':
			self.prompt_confirm()

	def prompt_confirm(self):
		"""
		ternyata gak bisa jalankan confirm krn event loop and shit
		"""
		from prompt_toolkit.shortcuts import confirm
		from prompt_toolkit import HTML, prompt
		result = None
		def internal():
			answer = confirm(HTML("<b>Should</b> we do that?"))
			result = answer
		run_in_terminal(internal)
		if result:
			self.log(f"Peroleh hasil:", result)

	def cursor_down(self, event):
		if self.show_editor:
			self.text_area.buffer.cursor_down()

	def cursor_up(self, event):
		if self.show_editor:
			self.text_area.buffer.cursor_up()

	def open_content_in_editor(self, event):
		if self.show_editor:
			# pastikan utk gunakan visual studio code
			editor = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SCHNELL_VISUAL"]
			# if not env_exist('VISUAL'):
			# 	editor = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SCHNELL_VISUAL"] # env_get('ULIBPY_SCHNELL_VISUAL')
			# 	env_add('VISUAL', editor)
			self.text_area.buffer.open_in_editor()

	def handle_tab(self, event):
		"""
		tricky

		kita ikutin ini saja.
		self.text_area.document.cursor_position_row + 1,
		self.text_area.document.cursor_position_col + 1,

		text_field.buffer.cursor_position = (
			text_field.buffer.document.translate_row_col_to_index(
				line_number - 1, 0
			)
		)
		akhirnya stlh baca source code dan search 'insert' ketemu cepat...
		"""		
		if self.show_editor and has_focus(self.text_area.buffer)():
			# mulai = self.text_area.buffer.cursor_position
			# self.text_area.buffer.text += '\t'
			# self.text_area.buffer.document.text += '\t'
			self.text_area.buffer.insert_text('\t')
			# self.text_area.buffer.cursor_position = mulai + TAB_LEN
			# self.text_area.document.cursor_position_col += TAB_LEN

	def get_single_line_input(self, consume=True, close_after=True):

		output = self.single_line_input.body.text
		if close_after:
			self.toggle_dialog()

		if consume:
			self.single_line_input.body.text = ''
		return output

	def input_dari_user(self, buff):
		"""
		pengennya kita gunakan utk control text-area, guest, output, dll
		utk oprek seting dsb
		"""
		# self.log(buff) # <Buffer(name='', text='') at 140349438396400>
		self.log(self.commander.body.text)
		self.lihat()
		self.commander.body.text = ''

	def input_dari_user_old(self, buff):
		"""
		self.body = body di dalam frame utk akses content
		"""
		output = self.single_line_input.body.text
		# coba ganti focus control dulu
		# self.application.layout.focus(self.text_area)
		self.toggle_dialog()
		def log():
			print('Input dari user adlh:', output)
		run_in_terminal(log)
		# biar bisa dipake oleh next
		self.single_line_input.body.text = ''

	def save_file(self, filename, content, append_mode=False):
		workfolder = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SCHNELL_WORKDIR"] # env_get('ULIBPY_SCHNELL_WORKDIR')
		filepath = joiner(ayah(__file__, 2), workfolder, filename)
		if append_mode:
			append_file(filepath, content)
		else:
			write_file(filepath, content)

		self.current_file_saved = filepath

	def copy_editor(self, event=None):
		content = self.text_area.text
		trycopy(content)

	def try_save_editor(self, event=None):
		"""
		semua ini bagusnya di taro di user dialog settings/checkbox
		utk editor perlu juga bisa kasih key utk set params
		agar bs jd full blown editor dan kita gak pusing gunakan external editor
		completer: :class:`~prompt_toolkit.completion.Completer` instance
				for auto completion.
		complete_while_typing: Boolean.
		history: :class:`~prompt_toolkit.history.History` instance.
		auto_suggest: :class:`~prompt_toolkit.auto_suggest.AutoSuggest`
				instance for input suggestions.
		lexer: :class:`~prompt_toolkit.lexers.Lexer` instance for syntax
				highlighting.
		wrap_lines: When `True`, don't scroll horizontally, but wrap lines.
		style: A style string.
		search_field: An optional `SearchToolbar` object.
		read_only: FilterOrBool = False,
		"""
		content = self.text_area.text
		if content:
			self.single_line_input.body.accept_handler = self.accept_filename_write
			self.active_dialog = UserDialog.SINGLE_LINE
			self.show_user_dialog = True
			self.application.layout.focus(self.single_line_input)

			# self.accept_filename_write()

	def accept_filename_write(self, unused_buffer=None):
		filename = self.single_line_input.body.text		
		if filename:
			content = self.text_area.text
			self.save_file(filename, content)
			self.toggle_dialog()
			self.single_line_input.body.text = ''

	def save_current_filename(self):
		# jk sdh save file sebelumnya save ke file yg sama
		# otherwise ask user utk masukkan
		if self.current_file_saved:
			self.save_file(self.current_file_saved, content)
		else:
			from collections import namedtuple as NT
			event = NT('event', 'key_sequence')
			kunci = NT('kunci', 'key')
			kirim = event(key_sequence=[kunci(key='c-s')])
			self.write_to_output_terminal(kirim)

	def write_to_output_terminal(self, event):
		"""
		kita pengen bisa nulis ke:
		guest cli
			utk bisa prompt dg validasi
			self.terminal.terminal_control.process.write_input(data)
		output terminal
			utk dialog
			self.output_terminal.terminal_control.process.write_input(data)
		"""
		# data = 'contoh nulis ke terminal dari main app/host\n'
		# self.log(event.key_sequence)
		key = event.key_sequence[0].key
		if key == 'c-]':
			data = 'chooselang\n'
		elif key == 'c-s':
			data = 'choosefile\n'

		self.application.layout.focus(self.output_terminal)
		self.output_terminal.terminal_control.process.write_input(data)

	def write_to_guest_cli_terminal(self, event):
		key = event.key_sequence[0].key
		if key == 'c-@':
			data = 'chooselang\n'
			self.write_terminal_guest(data)

	def write_terminal_guest(self, data):
		"""pastikan perintah diakhiri dg enter
		"""
		if not data.endswith('\n'):
			data += '\n'
		self.application.layout.focus(self.terminal)
		self.terminal.terminal_control.process.write_input(data)

	def write_terminal_output(self, data):
		if not data.endswith('\n'):
			data += '\n'
		self.application.layout.focus(self.output_terminal)
		self.output_terminal.terminal_control.process.write_input(data)

	def write_editor(self, data):
		self.application.layout.focus(self.text_area)
		self.text_area.buffer.insert_text(data)

	def ask_prompt_from_guest_cli(self, event=None):
		"""
		self.client = Client(address, authkey=GUEST_CLI_PASS)
		selalu ngehang
		"""
		# cari tempat yg pas biar bisa konek ke guest cli
		# client to guest cli
		print('can i connect to guest?')
		address = (GUEST_CLI_HOST, GUEST_CLI_PORT)
		self.client = Client(address, authkey=GUEST_CLI_PASS)
		print('yes you can...')
		import time
		time.sleep(.5)
		self.client.send({
			'type': 'prompt',
			'message': 'Masukkan bahasa untuk dieksekusi: ',
			'choices': ['Python', 'Go', 'C++'],
		})

	def cycle_user_dialog(self, event):
		# 0 = escape, 1 = u, 2 = 1/2/...
		pilih = event.key_sequence[2].key
		# krn kita tekan alt+u 1 maka memang pengen aktifkan radio, atau 2 utk aktifkan inputbox
		# print(event.key_sequence)
		if pilih == '1':
			self.active_dialog = UserDialog.RADIO
			self.show_user_dialog = True
			self.application.layout.focus(self.radios)
		elif pilih == '2':
			self.active_dialog = UserDialog.INPUT
			self.show_user_dialog = True
			self.application.layout.focus(self.user_input)
		# elif pilih == '3':
		# 	# print(event.key_sequence)
		# 	# def pesan():
		# 	# 	print('harusnya handle single line:', event.key_sequence)
		# 	# run_in_terminal(pesan)
		# 	self.active_dialog = UserDialog.SINGLE_LINE
		# 	self.show_user_dialog = True
		# 	self.application.layout.focus(self.single_line_input)
		elif pilih == '5':
			self.active_dialog = UserDialog.TERMINAL
			self.show_user_dialog = True
			self.application.layout.focus(self.small_terminal)

	# def increase(self, event):
	# 	last = self.text_area.window.preferred_width(self.maxw).preferred
	# 	w = self.text_area.window.preferred_width(self.maxw).weight
	# 	i = self.text_area.window.preferred_width(self.maxw).min
	# 	x = self.text_area.window.preferred_width(self.maxw).max
	# 	print('+ last:', last, 'berat:', w, 'min:', i, 'max:', x)
	# 	self.text_area.window.preferred_width(last + 1)
	# 	self.text_area.window.reset()

	# def decrease(self, event):
	# 	last = self.text_area.window.preferred_width(self.maxw).preferred
		
	# 	print('- last:', last)
	# 	self.text_area.window.preferred_width(last - 1)
	# 	self.text_area.window.reset()

	def exit(self, event):
		self.application.exit()

	def switch_focus_wrapper(self, event):
		self.switch_focus()

	def switch_focus(self):
		"Change focus when Control-W is pressed."
		if self.application.layout.has_focus(self.terminal):
			self.application.layout.focus(self.text_area)
		else:
			self.application.layout.focus(self.terminal)

	def paste_to_text_area(self, event=None):
		self.text_area.buffer.paste_clipboard_data(get_app().clipboard.get_data())

	def delete_lines(self, start_end):
		"""
		"""
		start = start_end[0] - 1
		end = -1
		if len(start_end) == 2:
			end = start_end[1] - 1

		if self.show_editor:
			content = self.text_area.text.splitlines()
			# result = content
			if content:
				if start < 0:
					start = 0
				if end == -1:
					end = len(content) - 1
				if (start <= end) and (0 <= start < len(content)) and (0 <= end < len(content)):
					newcontent = content[:start]+content[end+1:]
					result = '\n'.join(newcontent)
					# posisi kursor biar gampang ke akhir saja
					# cursorpos = len(result) - 1
					# ke awal saja
					cursorpos = 0
					self.text_area.buffer.document = Document(result, cursorpos)

	def delete_line(self, event):
		# skip ctrl-del
		# keys = [item.key for item in event.key_sequence][1:]
		# print('hapus:', keys)
		# start = ''.join(keys)
		start = event.key_sequence[1].key
		if len(event.key_sequence) == 3:
			start += event.key_sequence[2].key
		
		
		if self.show_editor and start.isdigit():
			content = self.text_area.text.splitlines()
			if content:
				start = int(start) - 1
				if 0 <= start <= len(content):
					newcontent = content[:start]+content[start+1:]
					result = '\n'.join(newcontent)
					# posisi kursor biar gampang ke akhir saja
					cursorpos = len(result) - 1
					self.text_area.buffer.document = Document(result, cursorpos)

	def run(self):
		self.application.run()

