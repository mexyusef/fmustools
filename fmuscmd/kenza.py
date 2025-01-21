import os
from fmuslib import *


config_file = joinhere(__file__, 'kenza.txt')

def get_config_file_lines():
    dirtxt = file_content(config_file)
    dirtxtlines = [item.strip() for item in dirtxt.splitlines() if not item.startswith('#')]
    return dirtxtlines
# [[], [], ...] utk masing2 baris di kenza.txt
# kenza_subfolders_mapping = [{basename(folder): [joiner(folder, item) for item in dirs(folder)]} for folder in dirtxtlines if os.path.isdir(folder)]
# kenza_subfolders_mapping = [{folder: [item for item in dirs(folder)]} for folder in dirtxtlines if os.path.isdir(folder)]

# list of {}-items dimana {}-item berisi line-entry-kenza.txt: {subfolders}
def get_folder_mapping():
    return [
        {    folder: dict(zip([item for item in dirs(folder)], [None]*len(dirs(folder))))    }
            for folder in get_config_file_lines()
                if os.path.isdir(folder)
    ]


kenza_subfolders_mapping = get_folder_mapping()
# [
#     {
#         "C:\\work\\kenza\\repo1": {
#             "actions-demo": null,
#             "youtube-clone": null,
#             "zonefunds": null
#         }
#     },
#     {
#         "C:\\work\\kenza\\repo2": {
#             "3D_portfolio": null,
#             "tutorial_react_hooks": null,
#             "unichat-course": null
#         }
#     }
# ]
# print_json(kenza_subfolders_mapping)
def remove_keys_starting_with_special_char_inplace(my_dict, special_char='$'):
    keys_to_remove = [key for key in my_dict.keys() if key.startswith(special_char)]
    for key in keys_to_remove:
        del my_dict[key]


def combine_last_two_parts(dirpath, delimiter='_'):
    # Normalize the path to handle different separators
    dirpath = os.path.normpath(dirpath)
    
    # Split the path into parts
    parts = dirpath.split(os.path.sep)
    
    # Take the last two parts, combine with delimiter, and convert to lowercase
    combined_parts = delimiter.join(parts[-2:]).lower()

    return combined_parts

def test_combine_last_two_parts():
    dirpath = r'C:\work\kenza\AntonioErdeljac\passport-tutorial'
    result = combine_last_two_parts(dirpath)
    print(result)

kenza_template_fmus = """.,d
    __NAMAPROYEK__,f(D=__DIRSUMBER__)
    __NAMAPROYEK__,d
        $* code .
        /ketik)dir
"""

# from prompt_toolkit import PromptSession, prompt
# from prompt_toolkit.application import run_in_terminal
# from prompt_toolkit.auto_suggest import AutoSuggest, AutoSuggestFromHistory, Suggestion
# from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
# from prompt_toolkit.completion import WordCompleter, FuzzyWordCompleter, NestedCompleter, FuzzyCompleter
# from prompt_toolkit.formatted_text import ANSI, HTML
# from prompt_toolkit.history import FileHistory
# from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import confirm # , CompleteStyle, set_title
# from prompt_toolkit.validation import Validator


def process_kenza(request):
    """
    $c:/work/kenza/appgen sample-django
    yg akan kita lakukan:
        - bikin template fmus
        - modify template fmus
        - run template fmus
    ada pilihan: template fmus itu satu entry/fmus atau satu file/us
        sebaiknya satu entry sehingga kita bisa simpan/tempatkan bbrp entry jk dibutuhkan
        err...tapi jika entry, maka butuh bikin file dulu, mending langsung content
    """
    request = request.replace(' ', os.path.sep)
    # kita tambah bisa buka cmd di lokasi tersebut (utk update dsb), jk request diakhiri dg *
    # jadi bisa alternative: mau update direktori tsb
    ask_open_cmdline = False
    if request.endswith('*'):
        request = request.removesuffix('*').strip()
        ask_open_cmdline = True
    if os.path.isdir(request):
        if ask_open_cmdline:
            content = '/ketik)cd '+request+'|dir'
        else:
            content = (kenza_template_fmus
                    # .replace('__NAMABARIS__', request)
                    .replace('__NAMAPROYEK__', combine_last_two_parts(request))
                    .replace('__DIRSUMBER__', request)
                    )
        print('process_kenza:', request, '=>', content)
        jawab = confirm(f"Exec fmus clipboard [{content}]?")
        if jawab:  # True or False
            run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
            # if using_thread:
            #     run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
            # else:
            #     run_fmus_for_content(content, dirpath=os.getcwd())
