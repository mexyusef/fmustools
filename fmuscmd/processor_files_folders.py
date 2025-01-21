import os
from schnell.app.dirutils import (
    isfile,
    dirname,
    isdir,
    get_all_folders,
    files,
    dirs,
    copy_directory,
)
from schnell.app.fileutils import (
    is_file_binary,
    is_file_not_binary,
    get_daftar_isi,
    fmusfile_entry,
    define_filepath_barisentry,
    define_filepath_barisentry_with_lineno,
    define_filepath_equal,
    define_filepath_equal_with_lineno,
)
from schnell.app.fileutils import file_write, file_prepend, file_append, file_content
from schnell.app.printutils import (
    print_source_code_copy,
    is_source_code,
    print_source_code,
    print_source_code_file,
    print_highlight_query,
    print_highlight_query_file,
    print_source_code_file_with_markdown,
)

from fmuslib import (
    temp_file_write,
    extract_file_paths,
    ayah,
    bongkar,
    joiner,
    joinhere,
    basename,
    creator_languages,
    creator_context,
    is_git_repo,
    get_branch_and_remote,
    get_latest_commit_info,
    is_file_not_binary,
    process_lalang,
    process_declang1,  # mapper
    process_declang2,  # no mapper
    run_fmus_for_content,
    run_fmus_for_content_in_thread,
    run_fmus_for_file_in_thread,
    run_fmus_for_file,
    schnell_appconfig,
    redis_repl,
    files_filter,
    file_content,
    get_definition_fmusfile_barisentry,
    file_write,
    file_lines,
    change_file_extension_in_path,
    programming_languages,
    replify,
    process_writer,
    execute_code,
    indah3,
    indah4,
    print_list_warna,
    print_json,
    trypaste,
    trycopy,
    run_url,
)
from configuration_values import *
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit import prompt


def processor_files(temporary_prompt):
    extra_choices = ["D", "c", "v", "x", "exit"]
    daftar_isi = files(os.getcwd())
    if not daftar_isi:
        indah4("No files.", warna="red")
        return
    daftar_isi += extra_choices
    jawab = None
    while jawab not in ["x", "exit"]:
        # jawab = temporary_prompt("🗒️📄💫➢ ", choices=daftar_isi)
        jawab = temporary_prompt(
            "➢ ", choices=daftar_isi, meta_dict={k: None for k in daftar_isi}
        )
        if jawab and jawab in daftar_isi:
            if jawab == "c":
                os.system("cls")
                print()
            elif jawab == "v":
                os.system(vim)
                # print()
            elif jawab == "D":
                processor_folders(temporary_prompt)
            else:
                print_source_code_file_with_markdown(jawab)
                # print_source_code_file(jawab)
                # try:
                # 	print_source_code_file(jawab)
                # except Exception as err:
                # 	indah4(f"gagal baca {jawab}: {err}.", warna='red')


def processor_folders(temporary_prompt):
    extra_choices = ["..", "...", "F", "c", "v", "x", "exit"]
    daftar_isi = dirs(os.getcwd())
    if not daftar_isi:
        indah4("No folders.", warna="red")
        return
    daftar_isi += extra_choices
    jawab = None
    while jawab not in ["x", "exit"]:
        # jawab = temporary_prompt(f"🗂️{os.getcwd()}💫➤ ", choices=daftar_isi)
        jawab = temporary_prompt(
            f"{os.getcwd()}➤ ",
            choices=daftar_isi,
            meta_dict={k: None for k in daftar_isi},
        )
        if jawab and jawab in daftar_isi:
            if jawab == "...":
                lokasi = ayah(os.getcwd(), 2)
                os.chdir(lokasi)
            elif jawab == "c":
                os.system("cls")
                print()
            elif jawab == "v":
                os.system(vim)
                # print()
            elif jawab == "F":
                processor_files(temporary_prompt)
            else:
                os.chdir(jawab)
            daftar_isi = dirs(os.getcwd()) + extra_choices
            os.system("wsl tree -C -L 1 .")


def processor_folders_with_args(temporary_prompt, basefolder):
    """dir cloner"""
    extra_choices = ["..", "...", "F", "c", "v", "x", "exit"]
    daftar_isi = dirs(basefolder)
    if not daftar_isi:
        indah4("No folders.", warna="red")
        return
    daftar_isi += extra_choices
    jawab = None
    while jawab not in ["x", "exit"]:
        jawab = temporary_prompt(
            f"{basefolder}➤ ",
            choices=daftar_isi,
            meta_dict={k: None for k in daftar_isi},
        )
        if jawab and jawab in daftar_isi:
            fulldir = joiner(basefolder, jawab)
            if isdir(fulldir):
                isyes = confirm(f"Clone {jawab} ke {os.getcwd()}?")
                if isyes:
                    targetdir = joiner(os.getcwd(), jawab)
                    copy_directory(fulldir, targetdir)
