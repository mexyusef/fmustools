import os, subprocess, traceback

from schnell.app.transpiler.nonredis import process_language as process_lalang, bahasa_lalang

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

def handle_lalang(self_temporary_prompt, self_refresh_completer, bahasa='py'):
    base_folder = os.getcwd()
    daftar_isi = ['x', 'exit', 'c',
        '#main',
        '#generator',
        '#statement_item',
        '#block_item',
        '#export_item',
        '#import_item',
        '#grammar',
        'bahasa',
        ]
    meta_dict = {
        "@@myint{mymethod(){}}": None,
        "@@myint{mymethod:f(){} | mysecondmethod:s(){}}": None,
        "@@myinter{}": None,
        "mydt?dn": None,
        "mydt?dn24-08-78,04:00:00": None,
        "?+hello": None,
        "?+'hello world'": None,
        "?+<hello /name/>": None,
        "for$${?+'hello'}": None,
        "w(i<10){?+'hello, world'}": None,
        "s(i)(1){?+'satu'}(2){?+'dua'}(){?+'bukan satu atau dua'}": None,
    }
    # lihat sample lain di:
    # C:\work\ciledug\ciledug\fmusperintah\configs\karya.json
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
            elif jawab == '#main':
                os.system(f'vscode {FILE_LALANG}')
                print()
            elif jawab == '#grammar':
                os.system(f'vscode {FILE_GRAMMAR}')
                print()
            elif jawab == '#generator':
                os.system(f'vscode {FILE_GENERATOR}')
                print()
            elif jawab == '#block_item':
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\handlers\block_item.py')
                print()
            elif jawab == '#statement_item':
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\handlers\statement_item.py')
                print()
            elif jawab == '#export_item':
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\handlers\export_item.py')
                print()
            elif jawab == '#import_item':
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\handlers\import_item.py')
                print()
            elif jawab == 'bahasa':
                print_source_code_copy(bahasa_lalang)
                print()
            elif jawab not in ['x', 'exit']:
                try:
                    process_lalang(bahasa + '/' + jawab, returning=False)
                except KeyboardInterrupt:
                    indah4('[handle_lalang] Press Ctrl+C')
                    break
                except Exception as exc:
                    traceback.print_exc()
                    indah4(f'[handle_lalang] Exception: {str(exc)}.')
    # stlh handle, balikkan
    self_refresh_completer()
