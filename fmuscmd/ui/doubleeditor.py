from asyncio import Future, ensure_future
import os
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.widgets import (
	Button,
	Dialog,
	Label,
	MenuContainer,
	MenuItem,
	SearchToolbar,
	TextArea,
)
from prompt_toolkit.layout.containers import (
	ConditionalContainer,
	Float,
	HSplit,
	VSplit,
	Window,
	WindowAlign,
)
from prompt_toolkit.layout.dimension import D

from schnell.app.printutils import (
	print_source_code_copy,
	is_source_code,
	print_source_code,
	print_source_code_file,
	print_highlight_query,
	print_highlight_query_file,
	print_source_code_file_with_markdown,
)
from fpprogress import progress_rainbow
from fmuslib import (
	# temp_file_write,
	# extract_file_paths,
	# ayah, bongkar, joiner, joinhere, basename,
	# creator_languages, creator_context,
	# is_git_repo, get_branch_and_remote,
	# get_latest_commit_info,
	# is_file_not_binary,
	# process_lalang,
	run_fmus_for_content,
	run_fmus_for_content_in_thread, 
	run_fmus_for_file_in_thread,
	run_fmus_for_file,
)
from .uicommon import show_dialog_as_float, show_message



class Application:
	dialog = None



class DoubleEditorDialog:
	def __init__(self, title, text, temporary_callback):

		self.future = Future()

		self.editor = TextArea(
			text,
			scrollbar=True,
			line_numbers=True,
			height=D(preferred=15),
			# style='ansiblue bold',
			style='bg:ansiblack ansibrightgreen',
		)
		self.output = TextArea(
			text='',
			read_only=True,
			scrollbar=True,
			line_numbers=True,
			height=D(preferred=15),
			# style='ansiblue bold',
			style='bg:ansiblack ansibrightyellow',
		)
		self.temporary_callback = temporary_callback

		def accept():
			self.future.set_result(self.output.text)

		def generate():
			# self.future.set_result(self.editor.text)
			self.temporary_callback(self.editor.text)

		gen_button = Button(text="Generate", handler=generate)
		ok_button = Button(text="OK", handler=accept)

		# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\widgets\dialogs.py
		# kb = KeyBindings()
		# kb.add("tab", filter=~has_completions)(focus_next)
		# kb.add("s-tab", filter=~has_completions)(focus_previous)
		self.dialog = Dialog(
			title=title,
			body=VSplit([
				# Label(text=text)
				self.editor,
				self.output,
			]),
			buttons=[
				gen_button,
				ok_button,
			],
			width=D(preferred=150),
			# with_background=True,
			# height=D(preferred=20),
			modal=True,
			z_index=10**10+1,
		)

	def __pt_container__(self):
		return self.dialog


def show_double_editor(title, text, root_container, temporary_callback, final_callback):
	"""
	temporary_callback
		menerima data dari text kiri, utk mulai proses generate AI
	final_callback
		menerima data dari text kanan, utk simpan hasil dari generate AI
	"""
	async def coroutine():
		dialog = DoubleEditorDialog(title, text, temporary_callback)
		Application.dialog = dialog

		content = await show_dialog_as_float(dialog, root_container)

		if content:
			try:
				# # with open(path, "rb") as f:
				# # 	text_field.text = f.read().decode("utf-8", errors="ignore")
				# # ApplicationState.current_content = content
				# # print_source_code_copy(content)
				# # repl.session.text_area.text = content
				# run_fmus_for_content_in_thread(content, dirpath=os.getcwd())				
				final_callback(content)
				# progress_rainbow(0.1, 10)
			except Exception as e:
				show_message("Error", f"{e}")

	ensure_future(coroutine())


def append_output(dialog, data):
	dialog.output.text += data


def set_output(dialog, data):
	dialog.output.text = data
