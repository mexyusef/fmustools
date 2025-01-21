from asyncio import Future, ensure_future
import os, subprocess
from prompt_toolkit import prompt
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import confirm
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

from schnell.app.dirutils import joinhere, joiner, isfile
from schnell.app.printutils import (
    indah4,
    print_source_code_copy,
    is_source_code,
    print_source_code,
    print_source_code_file,
    print_highlight_query,
    print_highlight_query_file,
    print_source_code_file_with_markdown,
)
from schnell.gui.system.searcher.widgets.actorhandler import actor_handler
from schnell.db.writer_service import process_writer
from schnell.app.fileutils import file_write_timestamped, file_content
from schnell.app.formatutils.markdownutils import (
    print_markdown_content,
    print_markdown_file,
)
from schnell.app.fileutils import file_write, file_prepend, file_append, file_content
from schnell.app.fmus.fileops import insert_at_lines
from configuration_values import help_file, config_app
from ui.doubleeditor import show_double_editor, Application, append_output
from ui.pager import show_pager
from fpgemini import send_chat_stream, gemini_header
from fpprogress import progress_rainbow
from fmuslib import (
    temp_file_write,
    trypaste,
    run_fmus_for_content,
    run_fmus_for_content_in_thread,
    run_fmus_for_file_in_thread,
    run_fmus_for_file,
)



class EditorDialog:
    def __init__(self, title, text, is_read_only=False, show_ok_button=True):
        self.future = Future()
        # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\widgets\base.py
        self.editor = TextArea(
            text,
            scrollbar=True,
            line_numbers=True,
            height=D(preferred=10),
            read_only=is_read_only,
            # style='ansiblue bold',
            style="bg:ansiblack ansiblue",
        )

        def accept():
            self.future.set_result(self.editor.text)

        # def set_done():
        # 	# self.future.set_result(None)
        # 	# print_source_code_copy(self.editor.text)
        # 	self.future.set_result(self.editor.text)
        if show_ok_button:
            ok_button = Button(text="OK", handler=accept)

        # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\widgets\dialogs.py
        # kb = KeyBindings()
        # kb.add("tab", filter=~has_completions)(focus_next)
        # kb.add("s-tab", filter=~has_completions)(focus_previous)
        self.dialog = Dialog(
            title=title,
            body=HSplit(
                [
                    # Label(text=text)
                    self.editor,
                ]
            ),
            buttons=[ok_button],
            width=D(preferred=100),
            # with_background=True,
            # height=D(preferred=20),
            modal=True,
            z_index=10**10 + 1,
        )

    def __pt_container__(self):
        return self.dialog
