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
from schnell.app.imageutils4 import display_images_from_clipboard
from schnell.app.filemanager.tui_browser import file_browser_pick
from schnell.app.filemanager.survey_browser import file_browser, folder_browser
from schnell.app.inpututils.tkinput import input_text_ctk, input_integer_ctk, input_float_ctk, input_boolean_ctk
from schnell.app.inpututils.survey_input import input_survey_text, input_survey_boolean



from keybinders.common import show_current_project_file_in_editor


def bind_pagedown(bindings, repl):  # clipboard operations
    @bindings.add("pagedown", "pagedown")  # start clipboard to file, ask for working filename
    def _(event):
        # namafile = input('[proyek baru] Masukkan nama file operasi clipboard: ')
        # namafile = input_text('[proyek baru] Masukkan nama file operasi clipboard: ')
        # namafile = input_text_ctk('[proyek baru] Masukkan nama file operasi clipboard: ')
        namafile = input_survey_text('[proyek baru] Masukkan nama file operasi clipboard: ')
        if namafile and namafile.strip():
            config_app["quick-projects"]["status"] = 1
            config_app["quick-projects"]["current-filename"] = namafile.strip()
            indah4(f'Operasi clipboard akan masuk ke {config_app["quick-projects"]["current-filename"]}.')
            repl.refresh_completer()
            # terpaksa lakukan ini dan restart dropdown menu
            # karena ternyata text-area jd pake yg lama dan tidak update walau kita ganti2 highlight barisentry pada dropdown menu
            # ternyata penyebab masalah adlh pick library
            event.app.current_buffer.validate_and_handle()  # jk menu dropdown lagi aktif jadi hilang

    @bindings.add("pagedown", "pageup")  # start clipboard to file, ask for working filename
    def _(event):
        namafile = file_browser()
        # namafile = file_browser_pick()
        if namafile and namafile.strip():
            config_app["quick-projects"]["status"] = 1
            config_app["quick-projects"]["current-filename"] = namafile.strip()
            indah4(f'Operasi clipboard akan masuk ke {config_app["quick-projects"]["current-filename"]}.')
            repl.refresh_completer()
            # ternyata penyebab masalah adlh pick library
            event.app.current_buffer.validate_and_handle()  # jk menu dropdown lagi aktif jadi hilang

    @bindings.add("pagedown", "escape")  # end clipboard to file
    def _(event):
        config_app["quick-projects"]["status"] = 0
        config_app["quick-projects"]["current-filename"] = None
        repl.refresh_completer()

    @bindings.add("pagedown", "f")  # run fmus utk kode di clipboard
    def _(event):
        # harus ada variasi utk content data dari fmus, file absolute/relative, url, dsb
        content = trypaste()
        if content:
            # from schnell.app.promptutils import yesno
            # import rich.prompt
            print_source_code(content)
            # jalankan = rich.prompt.Confirm.ask(prompt=f"Jalankan kode di atas di {os.getcwd()}?", default=True)
            jalankan = input_survey_boolean(f"Jalankan kode di atas di {os.getcwd()}?")
            if jalankan:
                # execute content
                if config_app["thread"]:
                    run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
                else:
                    run_fmus_for_content(content, dirpath=os.getcwd())

    @bindings.add("pagedown", "h")  # execute os.system pada clipboard (biar cepat)
    def _(event):
        # harus ada variasi utk content data dari fmus, file absolute/relative, url, dsb
        content = trypaste()
        if content:
            # from schnell.app.promptutils import yesno
            import rich.prompt
            print_source_code(content)
            jalankan = rich.prompt.Confirm.ask(prompt=f"Jalankan os.system di atas di {os.getcwd()}?", default=True)
            if jalankan:
                # execute content
                os.system(content)
                print("🏁")

    @bindings.add("pagedown", "i")  # insert clipboard to file at line
    def _(event):
        # harus ada variasi utk content data dari fmus, file absolute/relative, url, dsb
        contentdata = trypaste()
        filename = config_app["quick-projects"]["current-filename"]
        if not filename:
            filename = file_browser()
            config_app["quick-projects"]["current-filename"] = filename
            config_app["quick-projects"]["status"] = 1
        if not isfile(filename):
            file_write(filename, contentdata)
        else:
            # linespec = input(f'[{filename}] Masukkan nomor baris: ')
            # linespec = input_integer_ctk(f'[{filename}] Masukkan nomor baris: ')
            # linespec = input_text_ctk(f'[{filename}] Masukkan nomor baris: ')
            linespec = input_survey_text(f'[{filename}] Masukkan nomor baris: ')
            if linespec.isdigit():  # filename:42
                line_numbers = [int(linespec)]
                insert_at_lines(
                    filename, contentdata, line_numbers, line_index_start=1
                )

    @bindings.add("pagedown", "a")  # append clipboard to file
    def _(event):
        contentdata = trypaste()
        filename = config_app["quick-projects"]["current-filename"]
        if not filename:
            filename = file_browser()
            config_app["quick-projects"]["current-filename"] = filename
            config_app["quick-projects"]["status"] = 1
        if not isfile(filename):  # isfile gak bisa handle None
            file_write(filename, contentdata)
        else:
            file_append(filename, contentdata)

    @bindings.add("pagedown", "e")  # prepend clipboard to file (insert at 0)
    def _(event):
        contentdata = trypaste()
        filename = config_app["quick-projects"]["current-filename"]
        if not filename:
            filename = file_browser()
            config_app["quick-projects"]["current-filename"] = filename
            config_app["quick-projects"]["status"] = 1
        if not isfile(filename):
            file_write(filename, contentdata)
        else:
            file_prepend(filename, contentdata)

    @bindings.add("pagedown", "g")  # show image jika ada di clipboard
    def _(event):
        # contentdata = trypaste()
        display_images_from_clipboard()

    @bindings.add("pagedown", "down")  # insert 1 newline
    def _(event):
        # contentdata = trypaste()
        contentdata = '\n'
        filename = config_app["quick-projects"]["current-filename"]
        if not filename:
            filename = file_browser()
            config_app["quick-projects"]["current-filename"] = filename
            config_app["quick-projects"]["status"] = 1
        if not filename:
            return
        elif not isfile(filename):
            file_write(filename, contentdata)
        else:
            file_append(filename, contentdata)

    @bindings.add("pagedown", "up")  # insert 1 newline at line no
    def _(event):
        # contentdata = trypaste()
        contentdata = '\n'
        filename = config_app["quick-projects"]["current-filename"]
        if not filename:
            filename = file_browser()
            config_app["quick-projects"]["current-filename"] = filename
            config_app["quick-projects"]["status"] = 1
        if not isfile(filename):
            file_write(filename, contentdata)
        else:
            linespec = input_text_ctk(f'[{filename}] No baris (42=1 newline di #42, 42/3=3 newlines): ')
            if '/' in linespec:
                linespec, jumlah = [e.strip() for e in linespec.rsplit('/', 1)]
                if jumlah.isdigit():
                    contentdata = '\n' * int(jumlah)
            if linespec.isdigit():  # filename:42
                line_numbers = [int(linespec)]
                insert_at_lines(
                    filename, contentdata, line_numbers, line_index_start=1
                )

    @bindings.add("pagedown", "1")  # show content of current project file in floating editor
    def _(event):
        show_current_project_file_in_editor(config_app["quick-projects"]["current-filename"], repl)

    @bindings.add("pagedown", "2")  # tree of curdir, max level 2
    def _(event):
        from schnell.app.printutils import print_directory_tree
        request_dir = '.'
        request = event.app.current_buffer.text.strip()
        if request:
            request_dir = request
        print()
        print_directory_tree(request_dir)

    @bindings.add("pagedown", "3")  # tree of curdir, max level 3
    def _(event):
        from schnell.app.printutils import print_directory_tree
        request_dir = '.'
        request = event.app.current_buffer.text.strip()
        if request:
            request_dir = request
        print()
        print_directory_tree(start_path=request_dir, max_level=3)

    @bindings.add("pagedown", "escape")  # ganti lokasi default capture_and_copy_screenshot
    def _(event):
        namadirektori = folder_browser()
        # harusnya hanya bisa pilih direktori
        if namadirektori and namadirektori.strip():
            config_app["capture_and_copy_screenshot_folder"] = namadirektori.strip()
            indah4(config_app["capture_and_copy_screenshot_folder"], layar='yellow', warna='blue')

    # pagedown + delete coba setra ctrl+l di screenshot fmus-server fs.bat
    @bindings.add("pagedown", "delete")  # capture image lalu taro di clipboard
    def _(event):
        from schnell.app.ocrutils_new import capture_and_copy_screenshot
        saved_file = capture_and_copy_screenshot(
            # output_file=...,
            datadir=config_app["capture_and_copy_screenshot_folder"],
            # delay=0.5
        )
        print(f"File sekarang ada di clipboard.\n{saved_file}")

        # from schnell.app.printutils import print_directory_tree
        # request_dir = '.'
        # request = event.app.current_buffer.text.strip()
        # if request:
        #     request_dir = request
        # print()
        # print_directory_tree(start_path=request_dir, max_level=3)

