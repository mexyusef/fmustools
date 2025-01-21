import os, pyperclip
from fpcommon import *
from fmuslib import (
	# temp_file_write,
	# extract_file_paths,
	# ayah, bongkar, joiner, joinhere, basename,
	# creator_languages, creator_context,
	# is_git_repo, get_branch_and_remote,
	# get_latest_commit_info,
	is_file_not_binary, isfile, isdir,
	# process_lalang,
	run_fmus_for_content,
	run_fmus_for_content_in_thread,
	# run_fmus_for_file_in_thread,
	# run_fmus_for_file,
	# schnell_appconfig,
	# redis_repl,
	files_filter, files,
	# file_content, get_definition_fmusfile_barisentry, file_write, file_lines,
	# change_file_extension_in_path,
	# programming_languages, replify,
	# process_writer,
	execute_code,
)
from schnell.app.clipboardutils import trycopy, trypaste
from schnell.app.dictutils import contains_search_nested_dict, pattern_search_nested_dict
from schnell.app.fileutils import file_write, file_prepend, file_append, file_content
from schnell.app.fmus.fileops import insert_at_lines
from schnell.app.printutils import indah4, print_list_warna, print_source_code_file
from schnell.app.stringutils import inputify, inputify_running, clean_string, sanitize


from prompt_toolkit.shortcuts import confirm, prompt

from configuration_values import search_result_to_commands, original_dict_to_json, config_app, potongify

###################### ctrl+n
# kita pengen file,f(t=,@line>(something)|i+|data)
# @bindings.add("c-n")
# def _(event):
# 	# event.app.current_buffer.insert_text("insert control-n: masukkan cwd ke stack jk belum ada\nlalu print daftarnya")
# 	append_to_dirstack()
# 	print()
# 	print_list_warna(dir_stack, start=1)
def bind_key_n(bindings):

    @bindings.add("c-n", '1')
    def _(event):
        event.app.current_buffer.text = "ctrl+n 1"

    @bindings.add("c-n", 'a')  # prompt-line=filename, input dari clipboard
    def _(event):
        """
        filename
            write
        filename:@
            write
        filename:0@
            prepend, insert at the head
        filename:~@
            append, insert at the tail/end

        filename:3@
            append, new line 3 dg content clipboard
        filename:++3@
            append, pada line 3 yang ada, append dg content clipboard
        coba lihat
        from schnell.app.fmus.fileops import insert_at_lines, insert_after_query
        insert_at_lines(filepath, string_to_insert, lines_to_insert_at, encoding='utf-8')
        insert_at_lines(item.workdir, string_to_insert, lines_to_insert_at)

        filename:@<line-expression>
        """
        # C:\Users\usef\work\sidoarjo\schnell\app\fmus\fileops\__init__.py
        # insert_at_lines(filepath, string_to_insert, lines_to_insert_at, encoding='utf-8', line_index_start=0):
        filename = event.app.current_buffer.text.strip()
        if filename:
            filename = potongify(filename)  # agar bisa pasang emoji dll
        if filename:
            content = trypaste()
            if ':' in filename:
                filename, operasi_clipboard = [e.strip() for e in filename.split(':',1)]
                if operasi_clipboard in ['@']:
                    file_write(filename, content)
                elif operasi_clipboard in ['0@']:
                    file_prepend(filename, content)
                elif operasi_clipboard in ['~@']:
                    file_append(filename, content)
                elif operasi_clipboard.endswith('@'):  # berarti gak ada operasi clipboard, hanya operasi file
                    operasi_file, _ = [e.strip() for e in operasi_clipboard.split('@',1)]
                    # sementara kita letakkan clipboard di new line dulu, belum proses utk append pd line yg ada
                    if operasi_file:
                        if operasi_file.isdigit():  # 24@
                            # line index mulai dari 1
                            line_numbers = [int(operasi_file)]
                            insert_at_lines(filename, content, line_numbers, line_index_start=1)
                        elif ',' in operasi_file:  # 24,42,69@
                            line_numbers = [int(e.strip()) for e in operasi_file.split(',')]
                            insert_at_lines(filename, content, line_numbers, line_index_start=1)
            else:
                # jk gak ada : berarti langsung tulis ke file
                jawab = confirm(f"""Tulis isi di bawah ke {filename}\n{'-'*10}\n{content}\n{'-'*10}\n? """)
                if jawab:
                    file_write(filename, content)
        indah4(content, warna='cyan')
        terima_prompt(event)


    @bindings.add("c-n", 'b')  # prompt-line=file-content, siap utk tulis ke file, minta input=filename+linespec
    def _(event):
        # event.app.current_buffer.text = "file,f(c=)"
        filecontent = event.app.current_buffer.text.strip()
        if filecontent:
            indah4('\nMasukkan nama file untuk menulis content: ', warna='magenta')
            filename = input('')
            if filename:
                if ':' in filename:
                    filename, linespec = [e.strip() for e in filename.split(':',1)]
                    # jika filename sudah ada
                    if isfile(filename):
                        trycopy(file_content(filename))  # biar bisa dimonitor
                        if linespec == '0':  # filename:0
                            file_prepend(filename, filecontent)
                        elif linespec == '~':  # filename:~
                            file_append(filename, filecontent)
                        elif linespec.isdigit():  # filename:42
                            line_numbers = [int(linespec)]
                            insert_at_lines(filename, filecontent, line_numbers, line_index_start=1)
                    else:
                        file_write(filename, filecontent)
                else:  # filename
                    file_write(filename, filecontent)
                indah4(filename, warna='cyan')
                terima_prompt(event)


    @bindings.add("c-n", 'c')  # input=filename, ready to fmusrun clipboard=>file
    def _(event):
        # event.app.current_buffer.text = "file,f(c=)"
        filename = event.app.current_buffer.text.strip()
        if filename:
            # terima_prompt(event)
            indah4(trypaste(), warna='cyan')
            indah4('------------', warna='green')
            event.app.current_buffer.text = f'🏃‍♂️ {filename},f(C=)'
            # terima_prompt(event)
            # os.system('dir /w')
        else:
            indah4('Tulis nama file sebelum ctrl+n, c', warna='red')

    @bindings.add("c-n", 'f')  # preset fmuscode utk dijalankan (bisa dg c-n, n)
    def _(event):
        # curtext = event.app.current_buffer.text
        # cursor = len(event.app.current_buffer.document.text_before_cursor)
        letakkan = config_app['fmuscode'][config_app['fmuscode_index']]
        config_app['fmuscode_index'] = (config_app['fmuscode_index']+1) % (len(config_app['fmuscode']))
        event.app.current_buffer.text = letakkan

    # @bindings.add("c-n", 'm')
    # def _(event):
    #     event.app.current_buffer.text = "__INPUT__,f(t=,@line>(lit)|i+|data)"

    @bindings.add("c-n", 'n')
    def _(event):
        # event.app.current_buffer.text = "__INPUT__,f(t=,@line~(rgx)|i+|data)"
        fmuscontent = event.app.current_buffer.text.strip()
        if fmuscontent:
            # \\n dan \\t
            fmuscontent = fmuscontent.replace('\\n', '\n').replace('\\t', '\t')
            fmuscontent = sanitize(fmuscontent)
            if config_app['thread']:
                run_fmus_for_content_in_thread(fmuscontent, dirpath=os.getcwd())
            else:
                run_fmus_for_content(fmuscontent, dirpath=os.getcwd())

    # @bindings.add("c-n", 'o')
    # def _(event):
    #     event.app.current_buffer.text = "__INPUT__,f(t=,@btw>(sta)(end)|i+|data)"

    # @bindings.add("c-n", 'p')
    # def _(event):
    #     event.app.current_buffer.text = "__INPUT__,f(t=,@btw~(sta)(end)|i+|data)"

    # @bindings.add("c-n", 'z')
    # def _(event):
    #     curtext = event.app.current_buffer.text
    #     cursor = len(event.app.current_buffer.document.text_before_cursor)
    #     letakkan = config_app['emojis'][config_app['emoji_index']]
    #     config_app['emoji_index'] = (config_app['emoji_index']+1)%(len(config_app['emojis']))
    #     event.app.current_buffer.text = curtext[:cursor] + letakkan + curtext[cursor:]
