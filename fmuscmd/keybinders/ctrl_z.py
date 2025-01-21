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
	# run_fmus_for_content,
	# run_fmus_for_content_in_thread,
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
from schnell.app.printutils import indah4, print_list_warna, print_source_code_file
from schnell.app.stringutils import inputify, inputify_running, clean_string
from schnell.app.dictutils import contains_search_nested_dict, pattern_search_nested_dict
from configuration_values import search_result_to_commands, original_dict_to_json, config_app


def bind_key_z(bindings, repl):

    @bindings.add("c-z", 'a')  # search dict, setara dg %
    def _(event):

        global search_result_to_commands

        query = event.app.current_buffer.text.strip()
        if query:
            search_result_to_commands = pattern_search_nested_dict(original_dict_to_json, query, delimiter=' ')
            if search_result_to_commands:
                print()
                print_list_warna(search_result_to_commands, start=1)
                indah4(f"\nType '1' to '{len(search_result_to_commands)}' to execute selected command from above", warna='cyan')
                # jk gak temukan, biar user modify searchnya
                repl.add_to_history('%' + query)
                event.app.current_buffer.text = ""
            else:
                indah4("\nNo result.", warna='cyan')
        terima_prompt(event)

    @bindings.add("c-z", 'z')  # tree, list dir, print file atau print list of files sesuai query
    def _(event):
        # # event.app.current_buffer.insert_text('rem semoga ini masuk ya, tapi diproses gak oleh c-a, a?', fire_event=True)
        # event.app.current_buffer.insert_text('rem semoga ini masuk ya, tapi diproses gak oleh c-a, a?')
        # event.app.current_buffer.validate_and_handle()
        # jalankan_prompt(event, "rem senang sekali bisa tekan c-a, a")
        # # ini gak bisa karena manggil repl.temporary_prompt itu async loop sendiri
        # loop_temporary_repl_prompt(files(os.getcwd()), ca_a_handler)
        # kita coba fuzzy file press saja...
        query = event.app.current_buffer.text
        daftar_file = files(os.getcwd())
        found = [filename for filename in daftar_file if filename.strip() and (query.lower() in filename.lower())]
        if not query:
            os.system('wsl tree -C -L 1 -h .')  # tambah -h utk lihat ukuran file (512 utk folder)
        elif found:  # ada file dg pattern yg diminta
            if len(found)>1:  # ketemu bbrp
                indah4(f"\nFound {len(found)} = {found}.", warna='green')
                print_list_warna(found) # print list warna kadang cuma print 1 walau ada 2
                # print(f"\nFound {len(found)} => {found}.")
            else:  # tampilkan content jk ketemu filenya, jk dir ls
                filename = found[0]
                if isfile(filename):
                    pesan = f"Found: {filename}"
                    indah4(f"\n{pesan}\n{'*'*len(pesan)}", warna='green')
                    print_source_code_file(filename)
                elif isdir(filename):
                    os.system(f'ls -a --color=always --format=across -c -l {filename}')
        else:
            indah4(f"{query} not found.", warna='red')
        terima_prompt(event)
