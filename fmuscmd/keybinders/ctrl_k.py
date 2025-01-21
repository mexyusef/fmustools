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
from schnell.app.stringutils import inputify, inputify_running, clean_string


###################### ctrl+k
def bind_key_k(bindings):
    @bindings.add("c-k", '1')  # git diff head
    def _(event):
        jalankan_prompt(event, "git diff --name-only HEAD~1")
    @bindings.add("c-k", '9')  # git commit fmus perintah
    def _(event):
        # kita diff main.py dulu shg tau apa yg hrs ditulis di commit msg
        commitcmd = "(cd C:\\work\\ciledug\\ciledug\\fmusperintah && git diff main.py)" 
        os.system(commitcmd)
        commitcmd2 = "(cd C:\\work\\ciledug\\ciledug\\fmusperintah && git add . && git commit -am\"__INPUT__\")"
        os.system(inputify_running(commitcmd2,outside_of_loop=True))
        terima_prompt(event)
    @bindings.add("c-k", '0')  # git commit sidoarjo
    def _(event):
        commitcmd = "(cd C:\\Users\\usef\\work\\sidoarjo && git add . && git commit -am\"__INPUT__\")"
        os.system(commitcmd)
        terima_prompt(event)
    # @bindings.add("c-k", 'a')
    # def _(event):
    # 	event.app.current_buffer.text = "ctrl+k a"
    @bindings.add("c-k", 'l')  # l for log
    def _(event):
        jalankan_prompt(event, "git log --oneline --graph --color --all")
    @bindings.add("c-k", 'o')  # o for clone
    def _(event):
        jalankan_prompt(event, f"git clone {pyperclip.paste()}")
    @bindings.add("c-k", 's')  # s for git status
    def _(event):
        jalankan_prompt(event, "git status")
    @bindings.add("c-k", 'u')  # u for pull
    def _(event):
        jalankan_prompt(event, "git pull")
    # @bindings.add("c-k", 'c-j')
    # def _(event):
    # 	event.app.current_buffer.text = "ctrl+k ctrl-j"
    # @bindings.add("c-k", 'c-l')
    # def _(event):
    # 	event.app.current_buffer.text = "ctrl+k ctrl-l"
