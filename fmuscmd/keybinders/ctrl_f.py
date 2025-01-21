import os, pyperclip, subprocess
from fpcommon import *
from configuration_values import (
    config_app,
    ls_wide,
    ls_high,
    notedown,
    plaintext,    
)
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
    trypaste, trycopy,
	# files_filter,
	# file_content, get_definition_fmusfile_barisentry, file_write, file_lines,
	# change_file_extension_in_path,
	# programming_languages, replify,
	# process_writer,
	execute_code,
)
from schnell.app.clipboardutils import trycopy, trypaste
from schnell.app.printutils import indah4, print_list_warna, indah3
from schnell.app.stringutils import inputify, inputify_running, clean_string

# # Test cases
# print(extract_digit_and_rest("5/example"))  # Output: (5, 'example')
# print(extract_digit_and_rest("example"))   # Output: (None, 'example')
# from keybinders import terima_prompt

from keybinders.common import extract_digit_and_rest, terima_prompt

###################### ctrl+b
def bind_key_f(bindings, repl):

    # @bindings.add("c-b", 'd')  # toggle cek all drive space
    # def _(event):
    #     config_app['check_all_drives_space'] = not config_app['check_all_drives_space']
    #     indah4(f"config_app['check_all_drives_space']={config_app['check_all_drives_space']}", warna='yellow')

    @bindings.add("c-f", "1")
    def _(event):
        subprocess.Popen(
            [
                r"C:\work\kenza\zpt\fmus-iterate\fctb-console\WinformsTemplateFCTBNetFramework48\bin\Debug\WinformsTemplateFCTBNetFramework48.exe"
            ]
        )


    @bindings.add("c-f", "a")
    def _(event):
        subprocess.Popen(
            [
                r"C:\work\kenza\zpt\fmus-iterate\python-cs\WinformsTemplateFCTBNetFramework48\bin\Debug\WinformsTemplateFCTBNetFramework48.exe"
            ]
        )


    @bindings.add("c-f", "b")
    def _(event):
        subprocess.Popen(
            [
                r"C:\work\kenza\zpt\fmus-iterate\fctb-web\WinformsTemplateFCTBNetFramework48\bin\Debug\WinformsTemplateFCTBNetFramework48.exe"
            ]
        )


    @bindings.add("c-f", "c")
    def _(event):
        subprocess.Popen([r"C:\work\kenza\zpt\fmuspad\Tester\bin\Release\Tester.exe"])


    @bindings.add("c-f", "d")  # myeditor versi release
    def _(event):
        # subprocess.Popen([devpad])
        subprocess.Popen(
            [
                "C:\\work\\kenza\\zpt\\fmus-iterate\\myeditor\\WinformsTemplateFCTBNetFramework48\\bin\\Release\\WinformsTemplateFCTBNetFramework48.exe"
            ]
        )


    @bindings.add("c-f", "e")  # myeditor versi debug
    def _(event):
        subprocess.Popen(
            [
                "C:\\work\\kenza\\zpt\\fmus-iterate\\myeditor\\WinformsTemplateFCTBNetFramework48\\bin\\Debug\\WinformsTemplateFCTBNetFramework48.exe"
            ]
        )


    @bindings.add("c-f", "f")
    def _(event):
        # subprocess.Popen([notedown])
        agi_chat = "C:\\hapus\\juni2024\\claude\\WinformsTemplateFCTBNetFramework48\\bin\\Release\\agichat.exe"
        subprocess.Popen([agi_chat])

    @bindings.add("c-f", "g")
    def _(event):
        poet_editor = 'C:/\"Program Files\"/WindowsApps/40705VladimirMakarevich.65177D571F179_2.0.0.0_x86__7pdq99dwsatg4/poet.exe'
        subprocess.Popen([poet_editor])

    @bindings.add("c-f", "m")  # notepad next (open source)
    def _(event):
        # subprocess.Popen([notepad])
        subprocess.run("C:\\work\\ciledug\\ciledug\\fmusperintah\\vendor\\editors\\new-notepad\\NotepadNext-v0.7-win64\\NotepadNext.exe".split(), shell=True)
    
    @bindings.add("c-f", "n")  # notepad
    def _(event):
        # subprocess.Popen([notepad])
        subprocess.run(r"C:\Windows\system32\notepad.exe".split(), shell=True)


    @bindings.add("c-f", "o")  # notepad++
    def _(event):
        # subprocess.run([r'C:\Program Files"\Notepad++\notepad++.exe'], shell=True)
        process = subprocess.Popen([r'C:\Program Files"\Notepad++\notepad++.exe'], shell=True)
        # Do other stuff in your CLI app while Notepad++ is open
        # ...
        # Wait for Notepad++ to finish
        # process.communicate()

    @bindings.add("c-f", "p")
    def _(event):
        subprocess.Popen([plaintext])

    # @bindings.add("c-f", 'w')
    # def _(event):
    # 	subprocess.Popen([codewriter])  # access denied
    # @bindings.add("c-f", "c-j")
    @bindings.add("c-f", "pageup")  # generate code
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
                res = generate_code(masukan, llm_name=config_app["llm:llm"], jumlah=jumlah)
            else:
                res = generate_code(masukan, llm_name=config_app["llm:llm"])
            terima_prompt(event)
            indah3(res, warna='yellow')

    # @bindings.add("c-f", "c-k")
    @bindings.add("c-f", "pagedown")  # understand code
    def _(event):
        understand_code_prompt = event.app.current_buffer.text.strip()
        if not understand_code_prompt:
            understand_code_prompt = trypaste()
        if understand_code_prompt:
            print('\nunderstand:', understand_code_prompt)
            # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_understand.py
            from schnell.app.llmutils.langchainutils.agents.role_just_understand import understand_code
            jumlah, masukan = extract_digit_and_rest(understand_code_prompt)
            if jumlah:
                res = understand_code(masukan, llm_name=config_app["llm:llm"], jumlah=jumlah)
            else:
                res = understand_code(masukan, llm_name=config_app["llm:llm"])
            terima_prompt(event)
            indah3(res, warna='green')
