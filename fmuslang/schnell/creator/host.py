import sys
# ptterm hanya bisa utk prompt-toolkit 2.0.10
# https://codeload.github.com/prompt-toolkit/python-prompt-toolkit/tar.gz/refs/tags/2.0.10
# tdk bisa utk 3.0.0 dan di atasnya
# https://codeload.github.com/prompt-toolkit/python-prompt-toolkit/tar.gz/refs/tags/3.0.0
try:
	from ptterm import Terminal
except ImportError as err:
	class Terminal:
		pass
	# print('[creator.host]', err)

from prompt_toolkit.application import Application
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.layout.processors import TabsProcessor
from prompt_toolkit.lexers import DynamicLexer, PygmentsLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.layout.containers import (
	ConditionalContainer,
	Float,
	HSplit,
	VSplit,
	Window,
	WindowAlign,
)
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


class HostTerminal(Terminal):
	def __init__(self):
		self.kwargs = {
			# 'command'       : ['python', '-mapp.guest'],
			'command'       : ['bash'],
			'width'         : D(),
			# 'done_callback' : self.terminal_exit
		}
		super(HostTerminal, self).__init__(**self.kwargs)


TAB_LEN = 2
class HostEditor(TextArea):
	def __init__(self):
		self.kwargs = {
			'input_processors'  : [TabsProcessor(TAB_LEN)],
			'lexer'           : DynamicLexer(lambda: PygmentsLexer.from_filename(".txt", sync_from_start=False)),      

			'focus_on_click'  : True,
			'line_numbers'    : True,
			'scrollbar'       : True,
			
		}
		super(HostEditor, self).__init__(**self.kwargs)

style = Style([
	('terminal focused',    'bg:#aaaaaa'),
	('title',               'bg:#000044 #ffffff underline'),
	("status", "reverse"),
	("shadow", "bg:#440044"),
	
	# user dialog 1 line text area
	("input-field", "bg:#000000 #ffffff"),
])

bindings = KeyBindings()
@bindings.add('c-x', eager=True)
def _(event):
	event.app.exit()
	# try:
	# 	sys.exit(0)
	# except Exception:
	# 	sys.exit(0)

bindings.add("c-right")(focus_next)
bindings.add("c-left")(focus_previous)

class HostContainer:
	def __init__(self):
		self.show_editor = True
		self.show_terminal = True

		self.editor = HostEditor()

		self.editor_wrapper = ConditionalContainer(
			content=self.editor,
			filter=Condition(lambda: self.show_editor),
		)

		self.terminal = HostTerminal()

		# agar bisa ctrl+g utk toggle terminal utama = guest cli
		self.terminal_wrapper = ConditionalContainer(
			content=self.terminal,
			filter=Condition(lambda: self.show_terminal),
		)

		our_layout = Layout(
			container=HSplit([
				# Window(
				# 	height=1,
				# 	style='class:title',
				# 	content=FormattedTextControl(APPLICATION_TITLE)),
				VSplit([
					
					# self.terminal,
					self.terminal_wrapper,
					# HSplit([
					# 	self.terminal_wrapper,
					# 	self.output,
					# ]),

					Window(style='bg:#aaaaff', width=1),
					self.editor_wrapper,
				]),

				# ConditionalContainer(
				# 	content=self.commander,
				# 	filter=Condition(lambda: self.show_commander),
				# ),

				# statusbar
				# ConditionalContainer(
				# 	content=VSplit(
				# 		[
				# 			Window(
				# 				FormattedTextControl(self.statusbar_text), style="class:status"
				# 			),
				# 			Window(
				# 				FormattedTextControl(self.get_statusbar_right_text),
				# 				style="class:status.right",
				# 				width=9,
				# 				align=WindowAlign.RIGHT,
				# 			),
				# 		],
				# 		height=1,
				# 	),
				# 	filter=Condition(lambda: self.show_status_bar),
				# ),
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

	def run(self):
		self.application.run()
