from prompt_toolkit.application import run_in_terminal
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

# 1 line terminal repl
class Commander:
	def __init__(self, judul):
		self.body = TextArea(
			prompt=">>> ",
			style="class:input-field",
			height=1,
			focusable=True,
			accept_handler=self.input_dari_user,
			multiline=False,
			wrap_lines=False,
		)

		self.frame = Frame(
			title=judul,
			body=self.body			
		)

	def frame(self):
		return self.frame

	@property
	def textarea(self):
		return self.body

	def log(self, content):
		run_in_terminal(lambda: print(content))

	def lihat(self, event=None):
		run_in_terminal(input)

	def clear(self):
		self.textarea.text = ''

	def input_dari_user(self, buffer):
		self.log(buffer)
		self.lihat()
		self.clear()

