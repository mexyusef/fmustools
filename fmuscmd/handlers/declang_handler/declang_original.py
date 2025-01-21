import os, subprocess, traceback

from schnell.creator.declarative.handler import generate_program as process_declang
from schnell.app.transpiler.frontend.bahasa import bahasa as bahasa_declang
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


def handle_declang(self_temporary_prompt, self_refresh_completer):
    base_folder = os.getcwd()
    daftar_isi = ['x', 'exit', 'c',
        'bahasa',
        ]
    meta_dict = {
        "<a<b<c": None,
        "<a<b(<c[disabled]<d<e(<f<g))": None,
        "<a<b(<c[disabled]<d<e[nilai=kuda]|sampurasun(<f<g))": None,
        "[i/0/@@@|main.html] <a<b(<c[disabled]<d<e[nilai=kuda]|sampurasun(<f<g))": None,
    }
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
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\main.py')
                print()
                os.system(r'vscode C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\bahasa.py')
                print()
            elif jawab == 'bahasa':
                print_source_code_copy(bahasa_declang)
                print()
            elif jawab not in ['x', 'exit']:
                try:
                    process_declang(jawab, returning=False)
                except KeyboardInterrupt:
                    indah4('[handle_declang] Press Ctrl+C')
                    break
                except Exception as exc:
                    traceback.print_exc()
                    indah4(f'[handle_declang] Exception: {str(exc)}.')
    self_refresh_completer()
