import os, subprocess, traceback
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


from ciledug.palsu.palsu import process_palsu_language, bahasa_palsu


def handle_palsu(self_temporary_prompt, self_refresh_completer):
    base_folder = os.getcwd()
    daftar_isi = [
        # # C:\work\ciledug\ciledug\cepat\providers.py
        # "go/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "rs/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "java/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "js/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "py/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "rb/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "scala/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "ts/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "cpp/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "cs/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "elixir/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",
        # "mobile/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N",

        'x', 'exit', 'c',
        '#main',
        # '#handler',
        '#grammar',
        # '#provider',
        'bahasa',
    ]
    meta_dict = {
        "i": None,
        "i/5": None,
        "i:": {
            "ph": None,

            "i": None,
            "u8": None,
            "u16": None,
            "d": None,
            "f": None,
            "f(4,2)": None,

            "rd": None,
            "ri": None,
            "ri(1,100)": None,
            "rn": None,
            "rn(5)": None
        },
        "n": None,
        "s": None,
        "s/5": None,
        "s:": {
            "n": None,
            "fn": None,
            "ln": None,
            "e": None,
            "F": None,
            "M": None
        },

        "t": None,
        "ts": None,
        "dt": None,
        "dt:": {
            "iso": None,
            "dt": None,
            "d": None,
            "t": None,
            "b": None
        },

        "[s]": None,
        "[s];i;n;s": None,
        "{username=s}": None,
        "{username=s,password=s,data={age=i,girlfriend=s}}": None,
        "{name=s,avatar=s,links=[{title=s,url=s,image=s}]}": None,

        "L": None,
        "f/cari": None,

        ":name": None,

        ":word": None,

        ":words": None,
        ":words#nb=50": None,

        ":random_int": None,
        ":random_int#l": None,
        ":random_int#min=10000,max=20000": None,

        ":random_number": None,
        ":random_number#l": None,
        ":random_number#digits=10": None,

        ":date_between": None,
        ":date_between#l": None,
        ":date_between#start_date=2017-01-01,end_date=2023-08-01": None
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
                os.system(r'vscode C:\work\ciledug\ciledug\palsu\palsu.py')
                print()
            elif jawab == '#grammar':
                os.system(r'vscode C:\work\ciledug\ciledug\palsu\palsu.py')
                print()
            # elif jawab == '#handler':
            #     os.system(r'vscode C:\work\ciledug\ciledug\palsu\palsu.py')
            #     print()
            # elif jawab == '#provider':
            #     os.system(r'vscode C:\work\ciledug\ciledug\palsu\palsu.py')
            #     print()
            elif jawab == 'bahasa':
                print_source_code_copy(bahasa_palsu)
                print()
            elif jawab not in ['x', 'exit']:
                try:
                    results = process_palsu_language(jawab, returning=True)
                    if isinstance(results, list):
                        results = '\n'.join(results)
                    if not isinstance(results, str):
                        results = str(results)
                    indah4(results, warna='green')
                except KeyboardInterrupt:
                    indah4('[handle_palsu] Press Ctrl+C')
                    break
                except Exception as exc:
                    traceback.print_exc()
                    indah4(f'[handle_palsu] Exception: {str(exc)}.')
    # stlh handle, balikkan
    self_refresh_completer()
