# handle .env
import os
from prompt_toolkit.shortcuts import CompleteStyle, confirm
from schnell.app.dirutils import does_exist
from schnell.app.fileutils import file_append_ensure_newline, file_content
from schnell.app.printutils import (
    indah4,
	print_source_code_copy, is_source_code, print_source_code, print_source_code_file,
	print_highlight_query,
	print_highlight_query_file,
	print_source_code_file_with_markdown,
)


def handle_env(text):
    text = text.strip()
    print(f"handle_env: {text}")
    if text and (not does_exist('.env')):
        indah4('No .env file. Created?', warna='yellow', newline=False)
        buat = confirm(' ')
        if buat:
            # touch_file('.env')
            os.system('vscode .env')

    if does_exist('.env'):
        if not text:
            print_source_code_file('.env')
        else:
            file_append_ensure_newline('.env', text)
            indah4(file_content('.env'), warna='green')
    else:
        indah4('No .env file.', warna='red')
