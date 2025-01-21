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



class MessageDialog:
	def __init__(self, title, text):
		self.future = Future()

		def set_done():
			self.future.set_result(None)

		ok_button = Button(text="OK", handler=(lambda: set_done()))

		self.dialog = Dialog(
			title=title,
			body=HSplit([Label(text=text)]),
			buttons=[ok_button],
			width=D(preferred=80),
			modal=True,
		)

	def __pt_container__(self):
		return self.dialog



async def show_dialog_as_float(dialog, root_container):
	"Coroutine."
	float_ = Float(content=dialog)
	root_container.floats.insert(0, float_)

	app = get_app()

	focused_before = app.layout.current_window
	app.layout.focus(dialog)
	result = await dialog.future
	app.layout.focus(focused_before)

	if float_ in root_container.floats:
		root_container.floats.remove(float_)

	return result



def show_message(title, text, repl):
	async def coroutine():
		dialog = MessageDialog(title, text)
		await show_dialog_as_float(dialog, repl)

	ensure_future(coroutine())
