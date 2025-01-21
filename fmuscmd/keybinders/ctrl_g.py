import os
from prompt_toolkit import prompt
from schnell.app.printutils import (
    indah4,
	print_source_code_copy, is_source_code, print_source_code, print_source_code_file,
	print_highlight_query,
	print_highlight_query_file,
	print_source_code_file_with_markdown,
)
from fpcommon import *


def bind_key_g(bindings):
    @bindings.add("c-g", 'f')
    def _(event):
        cmd = "grep -n -I -C0 \"__INPUT__\" C:\\work\\ciledug\\ciledug\\fmusperintah\\configs\\*.json C:\\work\\ciledug\\ciledug\\fmusperintah\\*.json"
        query = event.app.current_buffer.text.strip()
        if query:
            query = query.strip()
            os.system(cmd.replace('__INPUT__', query))
            terima_prompt(event)

    @bindings.add("c-g", 'g')
    def _(event):
        cmd = "grep -n -I -C0 \"__INPUT__\" C:\\work\\ciledug\\ciledug\\fmusperintah\\configs\\*.json C:\\work\\ciledug\\ciledug\\fmusperintah\\*.json"
        query = input(f"Enter query to grep: ")
        if query:
            query = query.strip()
            os.system(cmd.replace('__INPUT__', query))
            terima_prompt(event)

    @bindings.add("c-g", 'm')  # run main.go
    def _(event):
        os.system('go run main.go')
        terima_prompt(event)

    @bindings.add("c-g", 'r')  # baca readme.md
    def _(event):
        filename = 'README.md'
        # indah4(f'reading {filename} => {os.path.isfile(filename)}', warna='blue')
        print_source_code_file_with_markdown(filename)
        terima_prompt(event)

    # @bindings.add("c-g", 'c-j')
    # def _(event):
    #     event.app.current_buffer.text = "ctrl+g ctrl+j"
