import os
import subprocess
from asyncio import Future, ensure_future
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
# print('hot2')
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
# print('hot3')
from configuration_values import help_file, config_app
from ui.doubleeditor import show_double_editor, Application, append_output
from ui.pager import show_pager
# print('hot4')
from fpgemini import send_chat_stream, gemini_header
# print('hot5')
from fpprogress import progress_rainbow
from fmuslib import (
    temp_file_write,
    trypaste,
    run_fmus_for_content,
    run_fmus_for_content_in_thread,
    run_fmus_for_file_in_thread,
    run_fmus_for_file,
)
# print('hot6')
# from schnell.app.temputils import file_write


class ApplicationState:
    """
    Application state.

    For the simplicity, we store this as a global, but better would be to
    instantiate this as an object and pass at around.
    """

    show_status_bar = True
    current_path = None
    current_content = None
    goto_line = -1
    input_number = None


class TextInputDialog:
    def __init__(self, title="", label_text="", completer=None):
        self.future = Future()

        def accept_text(buf):
            get_app().layout.focus(ok_button)
            buf.complete_state = None
            return True

        def accept():
            self.future.set_result(self.text_area.text)

        def cancel():
            self.future.set_result(None)

        self.text_area = TextArea(
            completer=completer,
            multiline=False,
            width=D(preferred=40),
            accept_handler=accept_text,
        )

        ok_button = Button(text="OK", handler=accept)
        cancel_button = Button(text="Cancel", handler=cancel)

        self.dialog = Dialog(
            title=title,
            body=HSplit([Label(text=label_text), self.text_area]),
            buttons=[ok_button, cancel_button],
            width=D(preferred=80),
            modal=True,
        )

    def __pt_container__(self):
        return self.dialog


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


# print('hot7')
from keybinders.hotkey_editor import EditorDialog


def get_line_number(repl, title="Get line number", body="Masukkan line number:"):
    async def coroutine():
        open_dialog = TextInputDialog(
            title=title,
            label_text=body,
            completer=PathCompleter(),
        )

        masukan_input = await show_dialog_as_float(open_dialog, repl)
        # try:
        #     masukan_input = int(masukan_input)
        # except ValueError as verr:
        #     show_message("Invalid line number", str(verr), repl)
        # else:
            # # ini cara go to line number
            # text_field.buffer.cursor_position = (
            #     text_field.buffer.document.translate_row_col_to_index(
            #         line_number - 1, 0
            #     )
            # )
        if masukan_input and masukan_input.strip():
            masukan_input = masukan_input.strip()
            ApplicationState.input_number = masukan_input  # mulai dari 1
            config_app["quick-projects"]["input-from-user"] = masukan_input
            print(f"""get_line_number: telah diterima masukan_input
            masukan_input = {masukan_input}
            config_app["quick-projects"]["input-from-user"] = {config_app["quick-projects"]["input-from-user"]}
            ApplicationState.input_number = {ApplicationState.input_number}
            """)

    ensure_future(coroutine())


def do_open_file(repl):
    async def coroutine():
        open_dialog = TextInputDialog(
            title="Open file",
            label_text="Enter the path of a file:",
            completer=PathCompleter(),
        )

        path = await show_dialog_as_float(open_dialog, repl)
        ApplicationState.current_path = path

        if path is not None:
            try:
                with open(path, "rb") as f:
                    content = f.read().decode("utf-8", errors="ignore")
                    # ApplicationState.current_content = f.read().decode("utf-8", errors="ignore")
                    print_source_code_copy(content)
            except OSError as e:
                show_message("Error", f"{e}", repl)

    ensure_future(coroutine())


def do_go_to(repl):
    async def coroutine():
        dialog = TextInputDialog(title="Go to line", label_text="Line number:")

        line_number = await show_dialog_as_float(dialog, repl)

        try:
            line_number = int(line_number)
        except ValueError as verr:
            show_message("Invalid line number", str(verr), repl)
        else:
            # # ini cara go to line number
            # text_field.buffer.cursor_position = (
            #     text_field.buffer.document.translate_row_col_to_index(
            #         line_number - 1, 0
            #     )
            # )
            ApplicationState.goto_line = line_number  # mulai dari 1

    ensure_future(coroutine())


def do_about(repl):
    show_message("Fmushell", "Fmushell\nThe greatest shell of all time.", repl)


def show_message(title, text, repl):
    async def coroutine():
        dialog = MessageDialog(title, text)
        await show_dialog_as_float(dialog, repl)

    ensure_future(coroutine())


# print('hot8')
from keybinders.common import show_current_project_file_in_editor, show_dialog_as_float


def show_editor(title, text, repl):
    async def coroutine():
        dialog = EditorDialog(title, text)
        content = await show_dialog_as_float(dialog, repl)
        if content.strip():
            content = content.strip()
            try:
                # with open(path, "rb") as f:
                # 	text_field.text = f.read().decode("utf-8", errors="ignore")
                # ApplicationState.current_content = content
                # print_source_code_copy(content)
                # repl.session.text_area.text = content
                if config_app["thread"]:
                    run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
                else:
                    run_fmus_for_content(content, dirpath=os.getcwd())
                # progress_rainbow(0.1, 10)
            except Exception as e:
                show_message("Error", f"{e}", repl)

    ensure_future(coroutine())


# def show_current_project_file_in_editor(title, repl):
#     # config_app["quick-projects"]["status"] = 1
#     # config_app["quick-projects"]["current-filename"] = namafile.strip()
#     if config_app["quick-projects"]["status"] and config_app["quick-projects"]["current-filename"]:
#         text = file_content(config_app["quick-projects"]["current-filename"])
#         async def coroutine():
#             dialog = EditorDialog(title, text, is_read_only=True, show_ok_button=False)
#             content = await show_dialog_as_float(dialog, repl)
#             # if content:
#             #     try:
#             #         run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
#             #     except Exception as e:
#             #         show_message("Error", f"{e}", repl)
#         ensure_future(coroutine())



def terima_prompt(event):
    event.app.current_buffer.text = ""
    event.app.current_buffer.validate_and_handle()  # jk empty bs terima input


# print('hot9')
from keybinders.hotkey_help import buat_kalimat_aktor, screenshot


def create_gemini_prompt(request):
    if not request:
        bariskalimat = ""
        actor_no = "empty"
    else:
        actor_no = request
        nama_aktor = actor_handler(":" + request, debug=False)
        kata_kata = process_writer(request, print_result=False, as_list=True)
        kata_kata = "- " + "\n- ".join(kata_kata)
        bariskalimat = buat_kalimat_aktor(kata_kata, nama_aktor)

    filepath = joinhere(
        __file__, "../data/gemini", f"chat-hotkey-{actor_no}-stream.txt"
    )
    # filepath_all = joinhere(__file__, '../data/gemini', f'chat-hotkey-{actor_no}-all.txt')
    return bariskalimat, filepath


# print('hot10')
# from schnell.app.filemanager.tui_browser import file_browser, inquire_text, inquire_yn, file_browser_pick
from schnell.app.imageutils4 import display_images_from_clipboard
from schnell.app.filemanager.tui_browser import file_browser_pick
from schnell.app.filemanager.survey_browser import file_browser
from schnell.app.inpututils.tkinput import input_text_ctk, input_integer_ctk, input_float_ctk, input_boolean_ctk
from schnell.app.inpututils.survey_input import input_survey_text, input_survey_boolean
from vendor.survey import survey
# print('hot11')
from keybinders.pagedown import bind_pagedown
# print('hot12')
from keybinders.pageup import bind_pageup
# print('hot13')
from keybinders.escape import bind_escape
# print('hot14')

def bind_home(bindings, repl):
    @bindings.add("home")
    def _(event):
        pass


def bind_end(bindings, repl):
    @bindings.add("end")
    def _(event):
        pass


# c-left, c-right, c-up, c-down
# c-@, c-\, c-], c-^, c-_, c-delete
# s-left, s-right, s-up, s-down
# c-s-left, c-s-right, c-s-up, c-s-down

def run_fmus(text):
    indah4("🚀", warna="yellow")
    if config_app["thread"]:
        run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
    else:
        run_fmus_for_content(text, dirpath=os.getcwd())


def bind_ctrl_del(bindings, repl):
    # ###################### ctrl+del
    @bindings.add("c-delete", "1")  # jalankan fmus dari content text_area_editor di kanan
    def _(event):
        # asyncio.run(coba_progressbar())  # gak bisa async krn sudah loop
        # global text_area_editor_focused
        # thread_task_2 = threading.Thread(target=task_2)
        # thread_task_2.start()
        if config_app["text_area_editor_focused"]:
            content = repl.session.text_area_editor.text.strip()
            if content:
                run_fmus(content)
        else:
            indah4("text_area_editor_focused not True", warna="blue")
        # # try:
        # # 	jalankan_fmus_dengan_progressbar()
        # # except Exception as e:
        # # 	indah4(str(e), warna='yellow')
        # # Wait for thread_task_2 to finish before proceeding with the main thread
        # thread_task_2.join()

    # if not config_app["enable_page_navigation_bindings"]
    # kita pengen tau apa enable_page_navigation_bindings=False bikin setiap kali kita ngetik di text_area_editor
    # maka terketik pula di text_area
    @bindings.add("c-delete", "0")  # toggle enable_page_navigation_bindings
    def _(event):
        # asyncio.run(coba_progressbar())  # gak bisa async krn sudah loop
        # global text_area_editor_focused
        # thread_task_2 = threading.Thread(target=task_2)
        # thread_task_2.start()
        config_app["enable_page_navigation_bindings"] = not config_app["enable_page_navigation_bindings"]
        indah4(f"""config_app["enable_page_navigation_bindings"]={config_app["enable_page_navigation_bindings"]}
        nilai False berarti ngetik di text_area_editor akan muncul juga di text_area
        """, warna="blue")

    # coba survey versi kita
    @bindings.add("c-delete", "escape")  # toggle enable_page_navigation_bindings
    def _(event):
        from fpsurvey import file_browser
        file_browser(repl)


def bind_key_hotkey(bindings, repl):
    bind_pageup(bindings, repl)
    bind_pagedown(bindings, repl)
    bind_ctrl_del(bindings, repl)
    bind_escape(bindings, repl)

    # ###################### ctrl+] gak jalan, coba ctrl+_
    @bindings.add("c-_")  # toggle tampilkan text_area (termasuk editor dan progressbar)
    def _(event):
        # repl.session.show_textarea = not repl.session.show_textarea
        config_app["show_textarea"] = not config_app["show_textarea"]
        repl.refresh_completer()
        terima_prompt(event)

    @bindings.add("s-tab")  # take screenshot dg schnell.app.ocrutils.take_screenshot
    def _(event):
        request = event.app.current_buffer.text.strip()
        screenshot(request)

    @bindings.add("s-delete")  # about fmush
    def _(event):
        do_about(repl)
        # repl.refresh_completer()

    @bindings.add("c-\\", "1")  # editor utk fmus code
    def _(event):
        show_editor("Create fmus code here", "", repl)
        # repl.refresh_completer()  # jadi ngehang
        # terima_prompt(event)
        # if ApplicationState.current_content:
        # 	print_source_code_copy(ApplicationState.current_content)
        # 	run_fmus_for_content_in_thread(ApplicationState.current_content, dirpath=os.getcwd())
        # event.app.current_buffer.validate_and_handle()
        # repl.session.text_area.text = ApplicationState.current_content

    @bindings.add("c-\\", "2")  # do_open_file
    def _(event):
        do_open_file(repl)

    @bindings.add("c-\\", "3")  # do_go_to
    def _(event):
        do_go_to(repl)

    @bindings.add("c-\\", "b")  # munculkan prompt di window berdasarkan "aktor"
    def _(event):
        request = event.app.current_buffer.text.strip()
        bariskalimat, filepath = create_gemini_prompt(request)
        show_editor(filepath, bariskalimat, repl)

    @bindings.add("c-\\", "c")  # spt del-d tapi gak pake GUI
    def _(event):
        request = event.app.current_buffer.text.strip()
        bariskalimat, filepath = create_gemini_prompt(request)

        def print_chat_stream(data):
            file_write_timestamped(
                filepath, data, write_mode="a", formatter="%Y%m%d-%H"
            )
            indah4(data, warna="green", layar="yellow")

        send_chat_stream(bariskalimat, print_chat_stream)

    @bindings.add("c-\\", "d")
    def _(event):
        """
        from fpgemini import send_chat_stream, gemini_header
        def send_chat_stream(prompt, callback):  # c-o, m
        """
        request = event.app.current_buffer.text.strip()
        if not request:
            bariskalimat = ""
            actor_no = "empty"
        else:
            actor_no = request
            nama_aktor = actor_handler(":" + request, debug=False)
            kata_kata = process_writer(request, print_result=False, as_list=True)
            kata_kata = "- " + "\n- ".join(kata_kata)
            bariskalimat = buat_kalimat_aktor(kata_kata, nama_aktor)

        filepath = joinhere(
            __file__, "../data/gemini", f"chat-hotkey-{actor_no}-stream.txt"
        )
        filepath_all = joinhere(
            __file__, "../data/gemini", f"chat-hotkey-{actor_no}-all.txt"
        )

        def print_chat_stream(data):  # co, m (chat)
            file_write_timestamped(
                filepath, data, write_mode="a", formatter="%Y%m%d-%H"
            )
            # indah4(msg, warna='green', layar='yellow')
            append_output(Application.dialog, data)

        # dipanggil dengan penekanan tombol <Generate>
        barisprompt = ""

        def temporary_callback(
            data_prompt,
        ):  # menerima prompt = data utk dikirim ke gemini AI dari left text area
            nonlocal barisprompt
            barisprompt = data_prompt
            file_write_timestamped(
                filepath,
                gemini_header(data_prompt),
                write_mode="a",
                formatter="%Y%m%d-%H",
            )
            send_chat_stream(bariskalimat, print_chat_stream)

        # dipanggil dg penekanan tombol <OK>
        def final_callback(data):  # menerima output dari gemini AI (right text area)
            # filename = temp_file_write(data, '.txt')
            # run_fmus_for_content_in_thread(f"**showfile={filename}", dirpath=os.getcwd())
            # simpan isi dari textarea output
            file_write_timestamped(
                filepath_all,
                gemini_header(barisprompt) + "\n" + data,
                write_mode="a",
                formatter="%Y%m%d-%H",
            )
            # send_chat_stream(bariskalimat, print_chat_stream)

        show_double_editor(
            "DE",
            bariskalimat,
            repl.session.root_container,
            temporary_callback,
            final_callback,
        )

    @bindings.add("c-\\", "delete")  # \ jadi \\ utk masukkan ke json
    def _(event):
        repl.process("#run#/clip)s12$$$")

    @bindings.add("c-\\", "f")  # coba pager dg dialog
    def _(event):
        bariskalimat = event.app.current_buffer.text.strip()
        if bariskalimat:
            filepath = joiner(os.getcwd(), bariskalimat)
            if isfile(bariskalimat):
                isifile = file_content(bariskalimat)
                repl.session.app.enable_page_navigation_bindings = True
                repl.session.app.mouse_support = True
                show_pager(
                    filepath,
                    isifile,
                    repl.session.root_container,
                    lambda data: print(data),
                )
                repl.session.app.enable_page_navigation_bindings = False

    @bindings.add("c-\\", "g")  # coba pager dg application
    def _(event):
        bariskalimat = event.app.current_buffer.text.strip()
        if bariskalimat:
            filepath = joiner(os.getcwd(), bariskalimat)
            if isfile(filepath):
                subprocess.Popen(
                    rf"python C:\work\ciledug\ciledug\fmusperintah\fppager.py {filepath}".split()
                )

    ###################### ctrl+\
    # @bindings.add("c-\\")  # show help, lebih baik pake "pager"
    # def _(event):
    #     # print_markdown_file(r'C:\work\ciledug\ciledug\fmusperintah\HELP.md')
    #     print_markdown_file(help_file)
    #     terima_prompt(event)
