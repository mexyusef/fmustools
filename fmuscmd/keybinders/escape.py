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
# from schnell.app.filemanager.tui_browser import file_browser, inquire_text, inquire_yn, file_browser_pick
from schnell.app.printutils import indah4, print_list_warna, indah3
from schnell.app.stringutils import inputify, inputify_running, clean_string
from schnell.app.imageutils4 import display_images_from_clipboard
from schnell.app.filemanager.tui_browser import file_browser_pick
from schnell.app.filemanager.survey_browser import file_browser
from schnell.app.inpututils.tkinput import input_text_ctk, input_integer_ctk, input_float_ctk, input_boolean_ctk
from schnell.app.inpututils.survey_input import input_survey_text, input_survey_boolean
from vendor.survey import survey

from keybinders.common import extract_digit_and_rest, terima_prompt


def bind_escape(bindings, repl):

    @bindings.add("escape", "escape")  # esc-esc refresh TUI
    def _(event):
        repl.refresh_completer()
        event.app.current_buffer.validate_and_handle()

    # @bindings.add("escape", "1")  # coba gunakan path completer
    # def _(event):
    # 	# repl.refresh_completer()
    # 	event.app.current_buffer.text = 'cd '
    # 	repl.path_completer()
    @bindings.add("escape", "1")
    def _(event):
        options = [
                'gemini',
                'openai',
                'groq',
                'together',
                'cohere',
            ]
        index = survey.routines.select('Select LLM: ',
            options=options,
            focus_mark='👉 ',
            # callback=lambda item:pilihan_sekarang(repl, item),
            evade_color=survey.colors.basic('yellow'))

        selection = options[index]
        if selection:
            config_app["llm:llm"] = selection

    # generate code for all llms
    @bindings.add("escape", "0")
    def _(event):
        generate_code_prompt = event.app.current_buffer.text.strip()
        if not generate_code_prompt:
            generate_code_prompt = trypaste()
        if generate_code_prompt:
            print('\ngenerate:', generate_code_prompt)
            # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_scrape.py
            from schnell.app.llmutils.langchainutils.agents.role_just_scrape import generate_code_for_all
            jumlah, masukan = extract_digit_and_rest(generate_code_prompt)
            if jumlah:
                res = generate_code_for_all(masukan, jumlah=jumlah)
            else:
                res = generate_code_for_all(masukan)
            terima_prompt(event)
            indah3(res, warna='yellow')

    # generate code for nvidia
    @bindings.add("escape", "n")
    def _(event):
        generate_code_prompt = event.app.current_buffer.text.strip()
        if not generate_code_prompt:
            generate_code_prompt = trypaste()
        if generate_code_prompt:
            print('\ngenerate:', generate_code_prompt)
            # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_scrape.py
            from schnell.app.llmutils.langchainutils.agents.role_just_scrape import generate_code
            jumlah, masukan = extract_digit_and_rest(generate_code_prompt)
            if jumlah:
                res = generate_code(masukan, llm_name='nvidia', jumlah=jumlah)
            else:
                res = generate_code(masukan, llm_name='nvidia')
            terima_prompt(event)
            indah3(res, warna='yellow')

    # generate code for groq
    @bindings.add("escape", "q")
    def _(event):
        generate_code_prompt = event.app.current_buffer.text.strip()
        if not generate_code_prompt:
            generate_code_prompt = trypaste()
        if generate_code_prompt:
            print('\ngenerate:', generate_code_prompt)
            # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_scrape.py
            from schnell.app.llmutils.langchainutils.agents.role_just_scrape import generate_code
            jumlah, masukan = extract_digit_and_rest(generate_code_prompt)
            if jumlah:
                res = generate_code(masukan, llm_name='groq', jumlah=jumlah)
            else:
                res = generate_code(masukan, llm_name='groq')
            terima_prompt(event)
            indah3(res, warna='yellow')
