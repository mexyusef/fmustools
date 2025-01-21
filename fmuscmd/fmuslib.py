import re
import common_import
from prompt_toolkit import prompt
from schnell.app.clipboardutils import trypaste, trycopy
from schnell.app.dirutils import joinhere, ayah, bongkar, files_filter, joiner, basename, dirs, isdir, isfile, files
from schnell.app.executils import execute_code
from schnell.app.fileutils import file_write, file_content, file_lines, get_definition_fmusfile_barisentry, is_file_not_binary, change_file_extension_in_path
from schnell.app.fmusutils import (
    # utk jalankan filepath=barisentry berisi fmuslang
    run_fmus_for_file_in_thread,
    run_fmus_for_file,
    # utk jalankan literal fmuslang
    run_fmus_for_content_in_thread,
    run_fmus_for_content,
)
from schnell.app.printutils import indah3, indah4, print_json, print_list_warna
from schnell.app.urlutils import run_url
from schnell.app.appconfig import appconfig as schnell_appconfig
from database.langnew import programming_languages
from startup import initialize_programming_data, programming_data
initialize_programming_data()
from schnell.db.myredis import redis_repl
from schnell.db.writer_service import process_writer
from schnell.creator.repl_language.replify import replify
from schnell.creator.context import context as creator_context, languages as creator_languages
from schnell.app.gitutils import is_git_repo, get_branch_and_remote, get_latest_commit_info
from schnell.app.transpiler.nonredis import process_language as process_lalang
from schnell.app.transpiler.frontend.main import process_language as process_declang2
from schnell.creator.declarative.handler import generate_program as process_declang1
from schnell.app.temputils import temp_file_write


def first_key(my_dict):
    key_list = list(my_dict.keys())
    return key_list[0]


play_folder_template = r"""BASE_FOLDER,d
    %__NAMA_FMUS__=__INPUT_NAMA_FMUS__.fmus
    %__DIR_OUTPUT__=__INPUT_NAMA_DIR_OUTPUT__
__IS_GITPULL__
    /reverse)BASE_FOLDER|__DIR_OUTPUT__\__NAMA_FMUS__
"""

# gen atau play fmus utk sebuah folder
def generate_fmus_for_folder(base_folder, git_pull=True, dir_output = r"c:\windows\temp"):
    namafile = prompt('[generate_fmus_for_folder] Masukkan nama file fmus utk hold isidir tanpa ekstensi: ')
    if namafile:
        content = (play_folder_template
                   .replace('BASE_FOLDER', base_folder)
                   .replace('__INPUT_NAMA_DIR_OUTPUT__', dir_output)
                   .replace('__IS_GITPULL__', '    $* git pull' if git_pull else '')
                   .replace('__INPUT_NAMA_FMUS__', namafile)
                   )
        if not content.endswith('\n'):
            content += '\n'
        # file_fmus = temp_file_write(content, '.fmus')
        run_fmus_for_content(content)
        kembalian = joiner(dir_output, f'{namafile}.fmus')
        return kembalian
    return None


def extract_file_paths(input_string):
    # Define a regular expression pattern for Windows file paths
    pattern = r'[a-zA-Z]:\\[^\n\)]+'  # kadang file diakhiri )

    # Use re.findall to find all matches in the input string
    file_paths = re.findall(pattern, input_string)
    # result = []
    # # C:\Users\usef\work\sidoarjo\database\by-langs\database\postgres.mk=postgres docker-compose.yml/code)
    # for path in file_paths:
    #     if '=' in path:
    #         result.append([item.strip() for item in path.split('=')][0])
    #     else:
    #         result.append(path)
    # return result
    return file_paths


def test_extract_file_paths():
    # input_string = "The file paths are C:\\example\\file.txt and D:\\documents\\file2.txt"
    input_string = "docker-compose.yml/fmus🧭🏃‍♂️docker-compose.yml,f(e=C:\\Users\\usef\\work\\sidoarjo\\database\\by-langs\\database\\postgres.mk=postgres docker-compose.yml/code)"
    paths = extract_file_paths(input_string)

    # Output the extracted file paths
    for path in paths:
        print("File Path:", path)

if __name__ == '__main__':
    test_extract_file_paths()
