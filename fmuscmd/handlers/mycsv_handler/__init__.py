import os, subprocess, traceback

from schnell.app.transpiler.mycsv.process import process_language as process_mycsv, bahasa_mycsv

from schnell.app.dirutils import (
    files, dirs,
    isfile, isdir,
    joiner,
    joinhere,
)
from schnell.app.fileutils import (
    define_filepath_barisentry,
    define_filepath_equal,
    get_daftar_isi,
)
from schnell.app.printutils import (
    indah4,
    print_source_code_copy,
    print_source_code_file,
    print_source_code_file_with_markdown,
)


FILE_LALANG = r'C:\Users\usef\work\sidoarjo\schnell\app\transpiler\nonredis.py'
FILE_GRAMMAR = r'C:\Users\usef\work\sidoarjo\schnell\app\transpiler\grammar.py'
FILE_GENERATOR = r'C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\generator.py'

def handle_mycsv(self_temporary_prompt, self_refresh_completer):
    base_folder = os.getcwd()
    daftar_isi = [
        "mg/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "sqlz/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "pg/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "ms/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "my/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "sqlt/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "torm/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "mg2/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "pris/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "hbr/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "bts/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "go/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "rs/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "kt/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "ts/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "java/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "dj/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "fl/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "fa/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "nsm/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "nsp/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "json1/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "json2/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "csv/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "all/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "fmus/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",

        'x', 'exit', 'c',
        'bahasa',
    ]
    meta_dict = {}
    meta_dict.update({k:None for k in daftar_isi})
    jawab = None
    while jawab not in ['x', 'exit']:
        jawab = self_temporary_prompt(f"[{base_folder}]👉 ",
            meta_dict=meta_dict,
            choices=daftar_isi,
            do_validation=False,
        )
        if jawab:
            if jawab == 'c':
                os.system('cls')
                print()
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\mycsv\process.py')
                print()
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\mycsv\csv_operation.py')
                print()
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\mycsv\handlers\__init__.py')
                print()
            elif jawab == 'bahasa':
                print_source_code_copy(bahasa_mycsv)
                print()
            elif jawab not in ['x', 'exit']:
                try:
                    process_mycsv(jawab, returning=False)
                except KeyboardInterrupt:
                    indah4('[handle_mycsv] Press Ctrl+C')
                    break
                except Exception as exc:
                    traceback.print_exc()
                    indah4(f'[handle_mycsv] Exception: {str(exc)}.')
    self_refresh_completer()
