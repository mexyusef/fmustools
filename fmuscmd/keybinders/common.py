from asyncio import Future, ensure_future
import os, re, subprocess
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


async def show_dialog_as_float(dialog, repl):
    "Coroutine."
    float_ = Float(content=dialog)
    repl.session.root_container.floats.insert(0, float_)

    app = get_app()

    focused_before = app.layout.current_window
    app.layout.focus(dialog)
    result = await dialog.future
    app.layout.focus(focused_before)

    if float_ in repl.session.root_container.floats:
        repl.session.root_container.floats.remove(float_)

    return result


def show_current_project_file_in_editor(title, repl):
    from .hotkey_editor import EditorDialog
    # config_app["quick-projects"]["status"] = 1
    # config_app["quick-projects"]["current-filename"] = namafile.strip()
    if config_app["quick-projects"]["status"] and config_app["quick-projects"]["current-filename"]:
        text = file_content(config_app["quick-projects"]["current-filename"])
        async def coroutine():
            dialog = EditorDialog(title, text, is_read_only=True, show_ok_button=False)
            content = await show_dialog_as_float(dialog, repl)
            # if content:
            #     try:
            #         run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
            #     except Exception as e:
            #         show_message("Error", f"{e}", repl)
        ensure_future(coroutine())


def terima_prompt(event):
    event.app.current_buffer.text = ""
    event.app.current_buffer.validate_and_handle()  # jk empty bs terima input


def extract_digit_and_rest(string):
    match = re.match(r'^(\d+)/(.*)$', string)
    if match:
        digit = int(match.group(1))
        rest = match.group(2)
        return digit, rest
    else:
        return None, string
