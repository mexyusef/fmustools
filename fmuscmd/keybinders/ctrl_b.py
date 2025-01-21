import os, pyperclip
from fpcommon import *
from configuration_values import config_app, ls_wide, ls_high
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
from schnell.app.printutils import indah4, print_list_warna
from schnell.app.stringutils import inputify, inputify_running, clean_string



###################### ctrl+b
def bind_key_b(bindings, repl):

    @bindings.add("c-b", 'd')  # toggle cek all drive space
    def _(event):
        config_app['check_all_drives_space'] = not config_app['check_all_drives_space']
        indah4(f"config_app['check_all_drives_space']={config_app['check_all_drives_space']}", warna='yellow')

    @bindings.add("c-b", 'm')  # toggle config = multicolumn
    def _(event):
        config_app['multicolumn'] = not config_app['multicolumn']
        config_app['ls_style'] = ls_wide if config_app['multicolumn'] else ls_high
        repl.refresh_completer()
        indah4(f"config_app['multicolumn']={config_app['multicolumn']}", warna='yellow')	

    @bindings.add("c-b", 'r')  # toggle config = readme_after_cd
    def _(event):
        config_app['readme_after_cd'] = not config_app['readme_after_cd']
        indah4(f"config_app['readme_after_cd']={config_app['readme_after_cd']}", warna='yellow')
    # @bindings.add("c-b", 'c-j')
    # def _(event):
    # 	event.app.current_buffer.text = "ctrl+b ctrl+j"
