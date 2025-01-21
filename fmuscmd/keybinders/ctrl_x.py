import os, pyperclip
from fpcommon import *
from fmuslib import (
	# temp_file_write,
	# extract_file_paths,
	# ayah, bongkar, joiner, joinhere, basename,
	# creator_languages, creator_context,
	# is_git_repo, get_branch_and_remote,
	# get_latest_commit_info,
	# is_file_not_binary,
	# process_lalang,
	# run_fmus_for_content,
	# run_fmus_for_content_in_thread,
	# run_fmus_for_file_in_thread,
	# run_fmus_for_file,
	# schnell_appconfig,
	# redis_repl,
	# files_filter,
	# file_content, get_definition_fmusfile_barisentry, file_write, file_lines,
	# change_file_extension_in_path,
	# programming_languages, replify,
	# process_writer,
	execute_code,
)
from schnell.app.clipboardutils import trycopy, trypaste
from schnell.app.printutils import indah4
from configuration_values import config_app

###################### ctrl+x
def bind_key_x(bindings):

    # @bindings.add("c-x", '1')
    # def _(event):
    #     event.app.current_buffer.text = "ctrl+x 1"

    # @bindings.add("c-x", 'a')
    # def _(event):
    #     event.app.current_buffer.text = "ctrl+x a"
    # ------------------------------------------------------ executor
    @bindings.add("c-x", 'c')
    def _(event):
        execute_code('cpp')

    @bindings.add("c-x", 'g')
    def _(event):
        execute_code('go')

    @bindings.add("c-x", 'c-g')
    def _(event):
        indah4('ctrl-x, ctrl-g: exec main.go', warna='blue')
        os.system('go run main.go')
        terima_prompt(event)

    @bindings.add("c-x", 'j')
    def _(event):
        execute_code('java')

    @bindings.add("c-x", 'p')
    def _(event):
        execute_code('py')

    @bindings.add("c-x", 'c-p')
    def _(event):
        python_filepath = pyperclip.paste()
        indah4(python_filepath, warna='cyan')
        jalankan_prompt(event, f"python {python_filepath}")

    @bindings.add("c-x", 'u')
    def _(event):
        execute_code('rs')

    @bindings.add("c-x", 'x')  # show emojis
    def _(event):
        curtext = event.app.current_buffer.text
        cursor = len(event.app.current_buffer.document.text_before_cursor)
        letakkan = config_app['emojis'][config_app['emoji_index']]
        trycopy(letakkan)  # tujuan kita memang mau copy
        config_app['emoji_index'] = (config_app['emoji_index']+1)%(len(config_app['emojis']))
        event.app.current_buffer.text = curtext[:cursor] + letakkan + curtext[cursor:]
