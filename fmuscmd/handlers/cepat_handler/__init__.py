import os, subprocess, traceback

from ciledug.cepat.cepat import processor_mycsv
from ciledug.cepat.grammar_mycsv import bahasa_mycsv
from ciledug.cepat.grammar_ucsv import bahasa_ucsv

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


def handle_cepat_mycsv(self_temporary_prompt, self_refresh_completer):
    base_folder = os.getcwd()
    daftar_isi = [
        "go/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "rs/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "java/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "js/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "py/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "rb/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "scala/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "ts/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "cpp/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "cs/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "elixir/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        "mobile/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",

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
                os.system(r'vscode C:\work\ciledug\ciledug\cepat\cepat.py')
                print()
                os.system(r'vscode C:\work\ciledug\ciledug\cepat\grammar_mycsv.py')
                print()
                os.system(r'vscode C:\work\ciledug\ciledug\cepat\cepat.py')
                print()
                os.system(r'vscode C:\work\ciledug\ciledug\cepat\providers.py')
                print()
            elif jawab == 'bahasa':
                print_source_code_copy(bahasa_mycsv)
                print()
            elif jawab not in ['x', 'exit']:
                try:
                    results = processor_mycsv(jawab, returning=True)
                    results = '\n'.join(results)
                    indah4(results, warna='green')
                except KeyboardInterrupt:
                    indah4('[handle_cepat_mycsv] Press Ctrl+C')
                    break
                except Exception as exc:
                    traceback.print_exc()
                    indah4(f'[handle_cepat_mycsv] Exception: {str(exc)}.')
    self_refresh_completer()
