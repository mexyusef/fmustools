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


from .common import run_command_in_folder, count_suffix


FILE_FMUS = joinhere(__file__, 'handle_ciledug.fmus')


def run_command_in_folder2(command, folder_path):
    current_directory = os.getcwd()
    try:
        os.chdir(folder_path)
        subprocess.run(command, shell=True)
    finally:
        os.chdir(current_directory)


def handle_ciledug(base_folder, self_temporary_prompt, self_refresh_completer):
    """
    <emoji> folder-item <perintah>
    folder-item <perintah>
    """
    daftar_file = files(base_folder)
    daftar_folder = dirs(base_folder)
    formatted_folders = [f"[{item}]" for item in daftar_folder]
    daftar_isi = (get_daftar_isi(FILE_FMUS)
        + daftar_file
        )
    meta_dict = {k:None for k in daftar_isi}
    meta_dict.update({
        item: None
        for item in formatted_folders
    })
    jawab = None
    try:
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
                    os.system(f'vscode {FILE_FMUS}')
                    print()
                    os.system(f'vscode {base_folder}')
                    print()
                    ciledugfile = r'C:\work\ciledug\ciledug\fmusperintah\ciledug.txt'
                    os.system(f'vscode {ciledugfile}')
                    print()
                elif jawab == 'explorer':
                    os.system(f'explorer {base_folder}')
                    print()
                elif jawab in daftar_file:
                    filepath = joiner(base_folder, jawab)
                    print_source_code_file_with_markdown(filepath)
                elif jawab in formatted_folders:
                    jawab = jawab.removeprefix('[').removesuffix(']')
                    run_command_in_folder(base_folder, f'dir {jawab}')
                else:
                    content_cmd = define_filepath_barisentry(FILE_FMUS, jawab)
                    run_command_in_folder(base_folder, content_cmd)
                    dir_diminta = [item for item in daftar_folder if jawab.startswith(item)] [0]
                    jumlah = count_suffix(dir_diminta, jawab)
                    dir_diminta = jawab.removesuffix('/'*jumlah)
                    tree_cmd = f"wsl tree -C -L {jumlah} {dir_diminta}"
                    run_command_in_folder(base_folder, tree_cmd)
                    mintadir = joiner(base_folder, dir_diminta)
                    tree_cmd = f"wsl tree -C -L 1 {mintadir}"
                    run_command_in_folder(base_folder, tree_cmd)
            else:
                indah4(f"not 'foldering' {dir_diminta} of {jawab}", warna='yellow')

    except KeyboardInterrupt:
        indah4('[handle_ciledug] Press Ctrl+C')
    except Exception as exc:
        traceback.print_exc()
        indah4(f'[handle_ciledug] Exception: {str(exc)}.')
    self_refresh_completer()
