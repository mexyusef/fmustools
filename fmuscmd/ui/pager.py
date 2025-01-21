from asyncio import Future, ensure_future
from pygments.lexers.python import PythonLexer

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


from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.dimension import LayoutDimension as D
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import SearchToolbar, TextArea



search_field = SearchToolbar(
	text_if_not_searching=[("class:not-searching", "Press '/' to start searching.")]
)


# # Key bindings.
# bindings = KeyBindings()


# @bindings.add("c-c")
# @bindings.add("q")
# def _(event):
#     "Quit."
#     event.app.exit()


style = Style.from_dict(
	{
		"status": "reverse",
		"status.position": "#aaaa00",
		"status.key": "#ffaa00",
		"not-searching": "#888888",
	}
)


class SimplePager:


	def __init__(self, title, text, temporary_callback):

		self.future = Future()

		self.temporary_callback = temporary_callback

		text_area = TextArea(
			text=text,
			read_only=True,
			scrollbar=True,
			line_numbers=True,
			height=D(preferred=25),
			search_field=search_field,
			lexer=PygmentsLexer(PythonLexer),
		)

		def get_statusbar_text():
			return [
				("class:status", title + " - "),
				(
					"class:status.position",
					"{}:{}".format(
						text_area.document.cursor_position_row + 1,
						text_area.document.cursor_position_col + 1,
					),
				),
				("class:status", " - Press "),
				("class:status.key", "Ctrl-C"),
				("class:status", " to exit, "),
				("class:status.key", "/"),
				("class:status", " for searching."),
			]

		pager_root_container = HSplit(
			[
				# The top toolbar.
				Window(
					content=FormattedTextControl(get_statusbar_text),
					height=D.exact(1),
					style="class:status",
				),
				# The main content.
				text_area,
				search_field,
			]
		)

		def accept():
			self.future.set_result("OK")

		# gen_button = Button(text="Generate", handler=generate)
		ok_button = Button(text="OK", handler=accept)

		# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\widgets\dialogs.py
		# kb = KeyBindings()
		# kb.add("tab", filter=~has_completions)(focus_next)
		# kb.add("s-tab", filter=~has_completions)(focus_previous)

		self.dialog = Dialog(
			# key_bindings=bindings,
			title=title,
			body=pager_root_container,
			buttons=[
				ok_button,
			],
			width=D(preferred=150),
			modal=True,
			z_index=10**10+1,
		)

	def __pt_container__(self):
		return self.dialog



def show_pager(title, text, root_container, temporary_callback):
	"""
	temporary_callback
		menerima data dari text kiri, utk mulai proses generate AI
	final_callback
		menerima data dari text kanan, utk simpan hasil dari generate AI
	"""
	async def coroutine():
		dialog = SimplePager(title, text, temporary_callback)
		Application.dialog = dialog

		content = await show_dialog_as_float(dialog, root_container)

		if content:
			try:
				temporary_callback(content)
			except Exception as e:
				show_message("Error", f"{e}")

	ensure_future(coroutine())
