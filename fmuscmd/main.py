import argparse, datetime, html, json, os, pathlib, pyautogui, subprocess, sys, threading, time, traceback
from configuration_values import *
from common_import import (
    global_context,
    command_prompt_data,
    command_prompt_data_extension,
    PERINTAH_JSON,
)
from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.application.current import get_app
from prompt_toolkit.auto_suggest import AutoSuggest, AutoSuggestFromHistory, Suggestion
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
from prompt_toolkit.completion import (
    WordCompleter,
    FuzzyWordCompleter,
    NestedCompleter,
    FuzzyCompleter,
)
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.formatted_text import ANSI, HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import CompleteStyle, confirm, set_title, PromptSession2
from prompt_toolkit.validation import Validator
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
from fmuslib import first_key
from fputils import (
    is_only_dots,
    navigate_back,
    navigate_back_multiple,
    percent_day,
    percent_hour,
)
from schnell.app.quick import process_language as process_quick
from schnell.app.keyboardutils import wait_for_shortcut, wait_for_shortcut_pynput
from schnell.app.dirutils import isfile, dirname, isdir, get_all_folders, files, dirs
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
from schnell.app.fmus.fileops import insert_at_lines
from schnell.app.stringutils import (
    inputify,
    inputify_running,
    inputify_varify_running,
    clean_string,
    sanitize
)
from schnell.app.googleutils import cari_google
from schnell.app.googleutils import cari_youtube
from schnell.app.devoputils.diskutils import (
    get_available_disk_space,
    get_free_memory_size,
    get_cpu_usage_percent,
    get_disk_drives,
)
from schnell.app.devoputils.networkutils import list_listening_ports
from schnell.app.devoputils.memoryutils import (
    list_processes_by_memory,
    list_processes_with_path,
)
from schnell.app.devoputils.cpuutils import get_cpu_usage_percent
from schnell.app.dictutils import (
    contains_search_nested_dict,
    pattern_search_nested_dict,
)
from schnell.app.formatutils.markdownutils import (
    print_markdown_content,
    print_markdown_file,
)
from schnell.app.printutils import (
    print_source_code_copy,
    is_source_code,
    print_source_code,
    print_source_code_file,
    print_highlight_query,
    print_highlight_query_file,
    print_source_code_file_with_markdown,
)
from schnell.app.vscodeutils import vscode_edit_file
from schnell.creator.grammar import bahasa as bahasa_repl
from schnell.db.replservice import repl_service  # penyimpan last_file dan last_lineno
from handlers.declang_handler import (
    handle_declang,
    reset_mapper,
    load_from_clipboard,
    elem_mapper,
    attr_mapper,
    cdata_mapper,
    value_mapper,
)
# from handlers.declang_handler import handle_declang
from perintah import perintah as process_perintah
from fpcommon import *

from processor_files_folders import (
    processor_folders_with_args,
    processor_files,
    processor_folders,
)
from kenza import (
    process_kenza,
    remove_keys_starting_with_special_char_inplace,
    kenza_subfolders_mapping,
    get_folder_mapping,
)
# print("4")

def change_dir(folder):
    try:
        os.chdir(folder)
        file_write(file_location_last_file, os.path.abspath(os.getcwd()))
    except Exception as err:
        indah4(err, warna="red")


def ulib_history():
    # import sys, tempfile
    # print('ulib_history', file_location)
    # if env_exist('ULIBPY_HISTORY_FILE'):
    # 	file_location = env_get('ULIBPY_HISTORY_FILE')
    # 	if sys.platform == 'win32' and env_exist('ULIBPY_HISTORY_FILE_WIN32'):
    # 		file_location = os.path.join(tempfile.gettempdir(), env_get('ULIBPY_HISTORY_FILE_WIN32'))
    return file_location_history


def create_if_empty_file(filepath):
    if not os.path.exists(filepath):
        pathlib.Path(filepath).touch()


def append_to_dirstack():
    current_location = os.getcwd()
    current_location = os.path.abspath(current_location)
    if not current_location in dir_stack:
        dir_stack.append(current_location)


bindings = KeyBindings()
last_file_not_passed_arguments = True


class UlibSuggestion(AutoSuggest):
    def __init__(self, entries):
        self.entries = entries

    def get_suggestion(self, buff, document):
        # Consider only the last line for the suggestion.
        text = document.text.rsplit("\n", 1)[-1]
        if text.strip():
            for word_lines in self.entries:
                for word in word_lines.splitlines():
                    if word.startswith(text):
                        return Suggestion(word[len(text) :])

        return None


# perintah\fmusfiles\snippets
def process_snippets():
    daftar_mk_files = files_filter(snippets_dir, [".mk"])
    daftar_mk_files = [joiner(snippets_dir, filename) for filename in daftar_mk_files]
    hasil = {f"{item}": None for item in daftar_mk_files}
    return hasil


def update_original_dict_to_json():
    from configuration_values import original_dict_to_json
    original_dict_to_json.update(
        {
            "edit-snip<|vscode": process_snippets(),
            "run-snip#run#/$snippets=": process_snippets(),
        }
    )
    original_dict_to_json["#"] = {
        item: None
        for item in daftar_config_files_content  # if item.strip() and not item.strip().startswith('#')
    }
    original_dict_to_json["ciledug"] = {
        item: None
        for item in ciledug_files_content  # if item.strip() and not item.strip().startswith('#')
    }
    original_dict_to_json["cirebon"] = {
        item: None for item in cirebon_files_content_cleanup
    }

update_original_dict_to_json()

############ START: proses config/*.json
# agar bisa dipake utk satu file json, misal data.json, dll
def update_file_json(file_json):
    isi_json = read_json(file_json)
    if isi_json:
        original_dict_to_json.update(isi_json)
        original_dict_keys.update({key: file_json for key in isi_json.keys()})


# baca dari configs, ambil semua json, dan update
def baca_configs():
    for file_json in daftar_json_configs_files:
        # indah4(f'original_dict_to_json => {file_json}', warna='white')
        file_json = os.path.join(json_configs_dir, file_json)
        # isi_json = read_json(file_json)
        # if isi_json:
        # 	original_dict_to_json.update(isi_json)
        update_file_json(file_json)


baca_configs()
############ END: proses config/*.json


# coba update dengan pertama cari dulu filenamenya jk ada
# bisa: data.json, ai.json, dst
# ~reload=data.json
def update_file_json_by_filename(filename):
    if filename in [
        "data.json"
    ]:  # beda lokasi utk data.json dibanding yg lain yg ada di configs/
        harus_ada = joiner(fmusperintah_dir, filename)
        update_file_json(harus_ada)
        indah4(f"reloading {harus_ada}", warna="white")
    else:
        cek_ada = joiner(json_configs_dir, filename)
        if isfile(cek_ada):
            update_file_json(cek_ada)
            indah4(f"reloading {cek_ada}", warna="white")


def kbrepl():
    repl_config = joinhere(__file__, "kbrepl.json")
    isi_json = read_json(repl_config)
    original_dict_to_json["."] = WordCompleter(
        isi_json.keys(),
        meta_dict={k: v for k, v in isi_json.items()},
        sentence=True,
        match_middle=True,
        ignore_case=True,
    )


kbrepl()

# handler utk "gen ..."
def handle_generator_process(filepath, barisentry):
    global repl
    # content = fmusfile_entry(filepath, barisentry)
    content, lineno = define_filepath_barisentry_with_lineno(filepath, barisentry)
    repl_service.last_file = filepath
    repl_service.last_lineno = lineno
    if barisentry.endswith("/md"):
        # from schnell.app.temputils import temp_file_write # file_write(data, suffix=".gif", delete=False)
        # tempfilepath = temp_file_write(content, '.md')
        # os.system(f'm {tempfilepath}')
        print_markdown_content(content)
    elif barisentry.endswith("!"):  # bisa exec command
        content = inputify(content)
        for baris in content.splitlines():
            os.system(baris)
    elif barisentry.endswith(".ipynb"):  # jalankan jupyter notebook di vscode
        # buat file di temp utk dibuka di vscode
        file_notebook = temp_file_write(content, ".ipynb")
        # pemanggilan = f"ipython notebook --NotebookApp.default_url={file_notebook}"
        pemanggilan = f"vscode {file_notebook}"
        # indah4(f"file_notebook={file_notebook}, pemanggilan={pemanggilan}", warna='black', layar='yellow')
        # indah4(f"file_notebook={file_notebook}", warna='white', layar='yellow')
        os.system(pemanggilan)
        # C:\Users\usef\work\sidoarjo\schnell\vendor\ptpython\ipython.py
        # from schnell.vendor.ptpython.ipython import embed
        # # embed({'notebook-file': file_notebook})
        # embed()
    elif barisentry.endswith("/fmus"):  # do-something/fmus
        # indah3(content, warna='yellow')
        print_source_code_copy(content)
        jalankan = confirm(f"Jalankan kode di atas di {os.getcwd()}?")
        if jalankan:
            # execute content
            if config_app["thread"]:
                run_fmus_for_content_in_thread(
                    content, dirpath=os.getcwd(), filepath=filepath
                )
            else:
                run_fmus_for_content(content, dirpath=os.getcwd(), filepath=filepath)
    # elif [item for item in ['.jpg', '.jpeg', '.webp', '.png', '.ico', '.gif'] if barisentry.endswith(item)]:
    # 	# decode to temp
    # 	# show
    # 	os.system()
    # harus bs jalankan fmus mk/reader utk 1 file fmus/mk
    # elif barisentry == 'fmusmk':
    # 	pass  # jalankan fmusmk
    # elif barisentry == 'fmusreader':
    # 	pass  # jalankan fmusreader
    else:
        # coba print source code
        print_source_code_copy(content)  # sudah bisa detek
        # if is_source_code(barisentry):
        # 	print_source_code_copy(content)
        # else:
        # 	indah3(content, warna='yellow')


def handle_generator(request, temporary_prompt=None):
    found_from_generatorjson = False

    # # matikan 30-12-23
    # # handle entries dari generator.json
    # # gen email/typescript fmusfile
    # for prefix, filepath in generator_paths.items():
    # 	if request.startswith(prefix):
    # 		found_from_generatorjson = True
    # 		if len(filepath)==1:  # jk ada list of files pada entry prefix di generator.json...perlu cara utk tentukan yg mana utk masing2 barisentry
    # 			filepath = filepath[0]
    # 		else:
    # 			filepath = filepath[0]  # sementara jk list, ambil saja yg entry pertama, abaikan yg lain
    # 		barisentry = request.removeprefix(prefix).strip()
    # 		# print(f"handle_generator, request [{request}], prefix [{prefix}], file [{filepath}] entry [{barisentry}].")
    # 		handle_generator_process(filepath, barisentry)

    # handle entries dari data.json dan configs/*.json
    # gen fmusfile
    if (
        not found_from_generatorjson
    ):  # jk dynamic "gen ..." dari file selain generator.json
        if request.startswith("gen "):
            code = request.removeprefix("gen ").strip()  # code adlh fmusfile
            if code:
                # coba pake temporary prompt bisa gak
                if isfile(code):
                    if code.endswith(".fmus") or code.endswith(".mk"):
                        daftar_isi = get_daftar_isi(code) + ["c", "#", "x", "exit"]
                        config_app["temporary_prompt_current_fmusfile"] = code
                        jawab = None
                        try:
                            while jawab not in ["x", "exit"]:
                                # jawab = temporary_prompt("💬💖👉 ", choices=daftar_isi)
                                jawab = temporary_prompt(
                                    "👉 ",
                                    meta_dict={k: None for k in daftar_isi},
                                    choices=daftar_isi,
                                )
                                if jawab and jawab in daftar_isi:
                                    if jawab == "c":
                                        os.system("cls")
                                        print()
                                    elif jawab == "#":
                                        os.system(f"vscode {code}")
                                        print()
                                    else:
                                        handle_generator_process(code, jawab)
                        except KeyboardInterrupt:
                            indah4("Press Ctrl+C")
                            pass
                # ini aneh juga, dlm barisentry sebuah fmusfile, bisa berisi anotherfmus=barisentry
                elif (
                    ".fmus=" in code or ".mk=" in code
                ):  # jk file=entry langsung proses, either print saja atau print+jalankan
                    filepath, barisentry = [item.strip() for item in code.split("=", 1)]
                    handle_generator_process(filepath, barisentry)
                else:
                    # jawab = temporary_prompt("ini berasal dari handle_generator => ")
                    jawab = f"{code} not found in {os.getcwd()}."
                    indah4(jawab, layar="yellow", warna="blue")

# update dg devops.json dsb.
def update_original_dict_to_json_with_json_files(
    LOKASI_JSON=r"C:\work\kenza\fmus",
    # PERINTAH_JSON=r"C:\Users\usef\work\sidoarjo\config_perintah.json",
):
    """
    masukkan json config files dari kenza/fmus sehingga bisa devops.json ... dari cli
    """
    # handle *.json files di kenza/fmus
    daftar_json = files_filter(LOKASI_JSON, extension=[".json"])
    for file_json in daftar_json:
        file_json = os.path.join(LOKASI_JSON, file_json)
        hasil = read_json(file_json)
        if "perintah" in hasil and len(hasil):
            # print('reading:', file_json, 'len:', len(hasil))
            ada = hasil.get("perintah")
            if len(ada):
                completer_list = []
                completer_meta = {}
                # e.g., [devops.json]={}
                fmus_file = change_file_extension_in_path(file_json, ".json", ".fmus")
                file_json_key = basename(file_json)
                # original_dict_to_json[file_json_key] = { f"###code {fmus_file}": None }
                first_item = f"🔴vscode {fmus_file}"
                completer_list.append(first_item)
                completer_meta[first_item] = f"Edit fmus file {fmus_file}"
                for kunci_entry, nilai_entry in ada.items():
                    # if 'file' in nilai_entry and 'entry' in nilai_entry:
                    nilai_file = nilai_entry["file"]
                    nilai_entry = nilai_entry["entry"]
                    bentuk = f"{nilai_file}={nilai_entry}"
                    # original_dict_to_json[file_json_key].update({ f"{kunci_entry}{bentuk}": None })
                    completer_list.append(bentuk)
                    completer_meta[bentuk] = (
                        f"Eksekusi fmus code di {nilai_file}={nilai_entry}"
                    )
                original_dict_to_json[file_json_key + "#file-entry#"] = WordCompleter(
                    completer_list, meta_dict=completer_meta, ignore_case=True
                )

    # handle config_perintah.json
    config_perintah_json = read_json(PERINTAH_JSON)
    if "perintah" in config_perintah_json and len(config_perintah_json):
        # print('reading:', PERINTAH_JSON, 'len:', len(config_perintah_json))
        ada = config_perintah_json.get("perintah")
        if len(ada):  # pastikan bukan {'perintah':{}} karena gak boleh none
            # original_dict_to_json[basename(PERINTAH_JSON)] = ada
            completer_list = []
            completer_meta = {}
            file_json_key = basename(PERINTAH_JSON) + "#file-entry#"
            # original_dict_to_json[file_json_key] = {}
            for kunci_entry, nilai_entry in ada.items():
                # config_perintah_json kadang gak lengkap
                if "file" in nilai_entry and "entry" in nilai_entry:
                    nilai_file = nilai_entry["file"]
                    nilai_entry = nilai_entry["entry"]
                    bentuk = f"{nilai_file}={nilai_entry}"
                    # original_dict_to_json[basename(file_json)] = bentuk
                    # original_dict_to_json[file_json_key].update({ kunci_entry: { bentuk: None } })
                    completer_list.append(bentuk)
                    completer_meta[bentuk] = (
                        f"Eksekusi fmus code di {nilai_file}={nilai_entry}"
                    )
                    # original_dict_to_json[file_json_key].update({ f"{kunci_entry}{bentuk}": None  })
            original_dict_to_json[file_json_key] = WordCompleter(
                completer_list, meta_dict=completer_meta, ignore_case=True
            )


update_original_dict_to_json_with_json_files()

# handle || di key
temporary_dict = {}


def update_nested_dict(d, parent_dict=None, parent_key=""):
    """
    ini masih buggy utk yg nested
    tapi berhasil utk yg top level
    - 1 jan 2024
            kita pengen bisa 'expand' misal fmus file atau dir menjadi berbagai isi
            kita gunakan emoji spesifik utk penandanya
    """
    updated_dict = {}
    completer_list = []
    completer_meta = {}
    for key, value in d.items():
        if isinstance(
            value, dict
        ):  # value kita batasi either dict (termasuk empty {}) atau null
            updated_value = update_nested_dict(value, parent_dict=d, parent_key=key)
        else:  # null value
            updated_value = value

        # || entry mengisi completer_list/meta
        if delimiter_for_metadict in key:  # jika key ada || maka value pasti None
            left_part, right_part = [
                item.strip() for item in key.split(delimiter_for_metadict, 1)
            ]
            if not updated_value:
                # if left_part not in updated_dict:
                if left_part not in completer_meta:
                    # gak bisa langsung update updated_dict karena next key,value harus dari bagian WordCompleter yg sama
                    completer_list.append(left_part)
                    completer_meta.update({left_part: right_part})
            else:  # gak jelas efek blok ini apa, selain melihat left||right: {not-empty}
                # jadi ini jika key||meta=value tapi value tdk None
                # maka abaikan meta
                # ini adlh kasus dimana "ada completer_list tapi updated_dict tdk kosong"
                updated_dict[left_part] = updated_value
        # non || entry mengisi updated_dict
        else:  # tidak ada ||, berarti value bisa None atau dict, jk dict, updated_value adlh WordCompleter
            # wait
            # 	updated_value = update_nested_dict(value, parent_dict=d, parent_key=key)
            # 		maka updated_value bisa dict atau WordCompleter (jk update_nested_dict(..) kembalikan WordCompleter)
            # 	updated_value = value
            # 		maka updated_value adlh None
            updated_dict[key] = updated_value
            if temporary_dict:
                updated_dict.update(temporary_dict)
                temporary_dict.clear()
            # cek ada urai-berai dir🦢
            if "🦢" in key:
                dirpath = extract_file_paths(key.replace("🦢", ""))[0]
                if isdir(dirpath):
                    daftar_mk_files = files_filter(
                        dirpath, [".fmus", ".mk"], abs_path=True
                    )
                    if daftar_mk_files:
                        # ternyata extract_file_paths masih gagal memisah bentuk
                        # Exception [Errno 22] Invalid argument: 'C:\\work\\ciledug\\ciledug\\fmusperintah\\helpers\\python 🧭🔴gen C:\\work\\ciledug\\ciledug\\fmusperintah\\helpers\\python\\bubbletea-examples.fmus'
                        kunci = "👶" + dirpath.replace(":", "").replace("\\", "_")
                        updated_dict.update(
                            {
                                kunci: {
                                    f"🧭🔴gen {item}": None for item in daftar_mk_files
                                }
                            }
                        )
            # cek ada urai-berai fmus🐦
            if "🐦" in key:
                fmusfilepath = extract_file_paths(key.replace("🐦", ""))[0]
                if fmusfilepath.endswith(".fmus") or fmusfilepath.endswith(".mk"):
                    daftar_barisentry = get_daftar_isi(fmusfilepath)
                    kunci = "👶" + fmusfilepath.replace(":", "").replace("\\", "_")
                    updated_dict.update(
                        {
                            kunci: {
                                f"🧭{fmusfilepath}={item}": None
                                for item in daftar_barisentry
                            }
                        }
                    )

    if completer_list and completer_meta:
        # ini akan dikembalikan dan dihandle oleh baris:
        # updated_value = update_nested_dict(value, key, delimiter_for_metadict)
        # TODO:
        # ini akan "makan" entry utk yg berkey dg delimiter_for_metadict
        # entries lain yg sibling akan diabaikan/dihapus di updated_dict[key] = updated_value
        # TODO:
        # cek jk updated_dict itu sudah ada content, maka don't hancurkan dg assignment =WordCompleter scr langsung dan total
        # 26/11
        if updated_dict:  # "ada completer_list tapi updated_dict tdk kosong"
            # wait up some of keys bisa WordCompleter, bisa juga string:null...
            # bgm cara gabung dg WordCompleter??? ambil saja list dan metanya => words dan meta_dict
            # 		gak usah khawatir, pada baris sini, semua 'kandidat' WordCompleter masuk completer_list/meta
            #  __init__(self, words, ignore_case=False, meta_dict=None, WORD=False, sentence=False, match_middle=False, pattern=None)
            # self.words = words, self.meta_dict = meta_dict or {}
            # di sini kita jadi tau sentence dan match_middle utk completion
            # lihat C:\Users\usef\work\sidoarjo\schnell\vendor\prompt_toolkit\prompt_toolkit\completion\word_completer.py

            # found problem: 26/11/23
            # jk salah satu item dari updated_dict adlh key dg value dict juga (yg bisa nested)
            # maka dia hidupnya hancur karena menjadi key=None, valuenya hilang
            # seharusnya dia diselamatkan di tempat yg berbeda bersama value nya
            # kita sebut saja item ini adlh item-sial dg key-sial=value-sial
            # maka harusnya parent[key]=WordCompleter hrs dibarengi dg
            # parent[key+' '+key-sial]=value-sial

            # daftar_kunci_non_completer = list(updated_dict.keys())
            daftar_kunci_non_completer = []
            for kunci_anak, nilai_anak in updated_dict.items():
                if nilai_anak:
                    # terpaksa kita gunakan +
                    # jk gunakan spasi entah kenapa nilai_anak gak muncul di sugesti completion
                    # new_key = parent_key+'+'+kunci_anak
                    # 27/12/23 coba ganti dg fake space
                    new_key = parent_key + "🔹" + kunci_anak
                    temporary_dict[new_key] = nilai_anak
                    # print(f"set temp dict, key {new_key}, val {nilai_anak}")
                else:  # jk kunci_anak=None berarti masukkan ke WordCompleter
                    daftar_kunci_non_completer.append(kunci_anak)

            completer_list += daftar_kunci_non_completer
            completer_meta.update(
                dict(zip(daftar_kunci_non_completer, daftar_kunci_non_completer))
            )
        updated_dict = WordCompleter(
            completer_list, meta_dict=completer_meta, ignore_case=True
        )

    return updated_dict


original_dict_to_json = update_nested_dict(original_dict_to_json)
original_cd_dict = {i: item for (i, item) in enumerate(original_cd_list, start=1)}


# stlh cd, mkdir, dsb, refresh completer yg jg memnaggil ini
def update_subfolders():
    # global original_dict_to_json
    daftar_folder = [
        folder for folder in os.listdir(os.getcwd()) if os.path.isdir(folder)
    ]
    daftar_file = [
        folder for folder in os.listdir(os.getcwd()) if os.path.isfile(folder)
    ]
    daftar_file_in_cwd_untuk_dihandle = {item: None for item in daftar_file}
    # hapus daftar file sebelumnya
    remove_current_files_from_dict(original_dict_to_json)
    # tambah daftar file baru ke completion
    # add_current_files_to_dict(original_dict_to_json, daftar_file)
    original_dict_to_json.update(daftar_file_in_cwd_untuk_dihandle)

    # teknik kita utk update folder
    new_cd_folder = {item: None for item in daftar_folder}
    original_folders = {v: None for v in original_cd_dict.values()}
    # original_dict_to_json['cd'] = { '..': None }
    # original_dict_to_json['cd'].update(new_cd_folder)
    original_dict_to_json["cd"] = new_cd_folder
    original_dict_to_json["cd"].update({"..": None})
    original_dict_to_json["cd"].update(original_folders)
    # siapa saja yg butuh completion ut kcd
    original_dict_to_json["~"] = new_cd_folder
    original_dict_to_json["ls"] = new_cd_folder
    original_dict_to_json["dir"] = new_cd_folder
    # agar bisa proses file dg berbagai teknik
    original_dict_to_json["`"] = daftar_file_in_cwd_untuk_dihandle
    original_dict_to_json["v"] = daftar_file_in_cwd_untuk_dihandle  # vim
    # kita assing p ke python di dlm fmusperintah
    original_dict_to_json["p"] = {
        item: None for item in daftar_file if item.endswith(".py")
    }
    original_dict_to_json["cat"] = daftar_file_in_cwd_untuk_dihandle

    original_dict_to_json["rat"] = daftar_file_in_cwd_untuk_dihandle  # search highlight
    original_dict_to_json["pad"] = daftar_file_in_cwd_untuk_dihandle  # fmuspad
    original_dict_to_json["pg"] = daftar_file_in_cwd_untuk_dihandle  # pager


def create_meta_completer(completer_dict, insensitive=True):
    words = list(completer_dict.keys())
    return FuzzyWordCompleter(
        words,
        meta_dict=completer_dict,
    )


def show_time():
    # return datetime.datetime.now().isoformat()
    return datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")


class Repl:
    def __init__(self):
        self.done = False

        histfile = ulib_history()
        create_if_empty_file(histfile)
        self.our_history = FileHistory(histfile)

        self.previous_words = internal_commands
        self.git_info = None
        self.show_bottom_toolbar = False

        self.last_file = None
        self.last_lineno = None

        # ini juga pastikan sblm refresh completer
        # # lebih baik jadikan lambda biar bisa diubah2
        # def get_bottom_toolbar(self):
        #     # now = datetime.datetime.now()
        #     return HTML(
        #         f' 🎉 <style bg="ansibrightred">{html.escape(self.git_info)}</style>'
        #     )
        self.get_bottom_toolbar = lambda: HTML(f' 🎉 <style bg="ansibrightred">{html.escape(self.git_info)}</style>')
        # self.get_bottom_toolbar = lambda: HTML(f' 🎉 <style bg="ansibrightred">{html.escape(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}</style>')

        # ini bikin cmd lost focus
        set_title("fmusperintah")
        self.refresh_completer()

    def before_run(self):
        # print('nilai last_file_not_passed_arguments:', last_file_not_passed_arguments)
        if last_file_not_passed_arguments and os.path.isfile(file_location_last_file):
            new_cwd = file_content(file_location_last_file)
            change_dir(new_cwd)
            # add to dirstack
            append_to_dirstack()
            # pastikan sblm refresh completer
            self.refresh_completer()

    def get_last_entry(self, index=-1):
        # Get all entries in history
        history_entries = self.our_history.get_strings()

        # Check if there are any entries
        if history_entries:
            # Get the last entry using negative indexing
            last_entry = history_entries[index]
            return last_entry
        else:
            return None

    def add_to_history(self, entry):
        self.our_history.append_string(entry)

    def update_git_info(self, current_location, max_git_message_len=100):
        if is_git_repo(current_location):
            branch_name, remote_url = get_branch_and_remote(current_location)
            (
                commit_datetime,
                commit_author,
                commit_message,
                commit_info,
                num_file_changes,
            ) = ("", "", "", "", "")
            try:
                (
                    commit_datetime,
                    commit_author,
                    commit_message,
                    num_file_changes,
                ) = get_latest_commit_info(current_location)
            except:
                pass
            pesan_git = clean_string(commit_message.strip()[:max_git_message_len])
            # pesan_git = pesan_git.replace('\n', '_')  # jangan sampai newline di bottombar
            # hilangkan \n di git_info biar bottom-toolbar gak makan space
            pesan_git = pesan_git.replace("\n", "✦").replace("\r", "☽")
            # ─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───
            # ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
            commit_info = (
                f"[{commit_datetime} {commit_author} +{num_file_changes}|{pesan_git}]"
            )

            if branch_name and remote_url:
                self.git_info = f"[{remote_url}|{branch_name}]{commit_info}"
                self.show_bottom_toolbar = True
            elif branch_name:
                self.git_info = f"[{branch_name}]{commit_info}"
                self.show_bottom_toolbar = True
            else:
                self.git_info = os.getcwd()
                self.show_bottom_toolbar = False

        else:
            # print(f"refresh_completer, current_location={current_location}: not a git repo")
            self.git_info = None
            self.show_bottom_toolbar = False

    def refresh_completer(self):
        update_subfolders()
        mycompleter = FuzzyCompleter(
            NestedCompleter.from_nested_dict(original_dict_to_json),
            # C:\Users\usef\work\sidoarjo\schnell\vendor\prompt_toolkit\prompt_toolkit\completion\fuzzy_completer.py
            # pattern='^[a-zA-Z0-9_\s]*'  # bisa space utk completion
        )
        current_location = os.getcwd()
        self.update_git_info(current_location)
        self.session = self.create_prompt_session(mycompleter, self.previous_words)

    def change_dir_and_refresh_completer(self, open_folder):
        try:
            change_dir(open_folder)
            self.refresh_completer()
            open_folder = os.path.realpath(open_folder)
            if not open_folder in dir_stack:
                dir_stack.append(open_folder)
            if config_app["readme_after_cd"] and any(
                [isfile("README.md"), isfile("README.rst"), isfile("readme.md")]
            ):
                if isfile("README.md"):
                    print_source_code_file_with_markdown("README.md")
                elif isfile("README.rst"):
                    print_source_code_file_with_markdown("README.rst")
                elif isfile("readme.md"):
                    print_source_code_file_with_markdown("readme.md")

        except Exception as err:
            print("[change_dir_and_refresh_completer] exception:", err)

    # # lebih baik jadikan lambda biar bisa diubah2
    # def get_bottom_toolbar(self):
    #     # now = datetime.datetime.now()
    #     return HTML(
    #         f' 🎉 <style bg="ansibrightred">{html.escape(self.git_info)}</style>'
    #     )

    def create_prompt_session(self, completer, suggest_words=None, validator=None):
        suggestion_list = AutoSuggestFromHistory()
        if suggest_words:
            suggestion_list = UlibSuggestion(suggest_words)
        # print(f"create_prompt_session, pwd={os.getcwd()}, config_app["show_bottom_toolbar"]={config_app["show_bottom_toolbar"]}")
        # print('create_prompt_session =>', config_app["show_textarea"])
        return PromptSession2(
            # https://python-prompt-toolkit.readthedocs.io/en/master/pages/reference.html
            # bottom_toolbar=get_toolbar_tokens if config_app["show_bottom_toolbar"] else None,
            bottom_toolbar=(
                self.get_bottom_toolbar() if (self.show_bottom_toolbar and config_app["show_bottom_toolbar"]) else None
            ),
            # refresh_interval=0.5,
            # swap_light_and_dark_colors=True,
            clipboard=PyperclipClipboard(),  # ctrl+w cut, ctrl+y paste, ctrl+space, ctrl+@ selection
            validator=validator if validator else None,
            # editing_mode=editing_mode,
            enable_open_in_editor=True,
            enable_system_prompt=True,
            enable_suspend=True,
            # enable_history_search=True,
            # include_default_pygments_style=False,
            # input_processors=[
            # 	ConditionalProcessor(
            # 		processor=HighlightMatchingBracketProcessor(chars="[](){}"),
            # 		filter=HasFocus(DEFAULT_BUFFER) & ~IsDone(),
            # 	)
            # ],
            # lexer=PygmentsLexer(LiteCliLexer),
            # message=get_message,
            # multiline=cli_is_multiline(self),
            # prompt_continuation=get_continuation,
            # reserve_space_for_menu=self.get_reserved_space(),
            # tempfile_suffix=".sql",
            # auto_suggest=AutoSuggestFromHistory(),
            auto_suggest=suggestion_list,
            completer=completer,
            complete_while_typing=True,
            complete_style=(
                CompleteStyle.MULTI_COLUMN
                if config_app["multicolumn"]
                else CompleteStyle.COLUMN
            ),
            history=self.our_history,
            key_bindings=bindings,
            mouse_support=True,
            search_ignore_case=True,
            style=prompt_style,
            text_area_height=config_app["text_area_height"],
            text_area_style=config_app["text_area_style"],
            text_area_lexer=config_app["text_area_lexer"],
            text_area_editor_style=config_app["text_area_editor_style"],
            text_area_editor_lexer=config_app["text_area_editor_lexer"],
            show_textarea=config_app["show_textarea"],
            show_textarea_editor=config_app["show_textarea_editor"],
            show_editor_toolbar=config_app["show_editor_toolbar"],
            progress_day=percent_day(),
            progress_hour=percent_hour(),
            # enable_page_navigation_bindings=config_app['enable_page_navigation_bindings'],
        )

    @property
    def prompt(self):
        cwd = os.getcwd()
        now = datetime.datetime.now()
        active_project_file = ''
        if config_app["quick-projects"]["status"]:
            active_project_file = "|" + config_app["quick-projects"]["current-filename"]
        try:
            if not config_app["check_all_drives_space"]:
                free_space = get_available_disk_space()
            else:
                drive_spaces = [
                    drive + get_available_disk_space(drive)
                    for drive in get_disk_drives()
                ]
                free_space = (
                    ",".join(drive_spaces)
                    + "|"
                )
                if len(drive_spaces) > 1:
                    config_app["max_panjang_path"] = 30  # space utk path jadi sedikit
        except Exception as err:
            free_space = str(err)[:40] + ".."
        free_mem = get_free_memory_size()
        # cpu_activity = get_cpu_usage_percent()
        # https://python-prompt-toolkit.readthedocs.io/en/master/pages/asking_for_input.html
        lang = creator_context["current_language"]
        day_date_month = f"{now.strftime('%a')} {now.day}/{now.month}"
        doy = datetime.datetime.now().strftime("%j")
        waktu = f"{now.hour}:{now.minute}:{now.second}"
        # format1 = f"""<host>[P|{lang}] {day_date_month} 👷{doy} {waktu} [📁{free_space}🧠{free_mem}🔄{cpu_activity}%] {os.getcwd()}</host>"""
        # cpu activity terlalu lambat
        max_panjang_path = config_app["max_panjang_path"]
        max_panjang_line = config_app["max_panjang_line"]

        terminal_lines = os.get_terminal_size().lines
        terminal_cols = os.get_terminal_size().columns
        if len(cwd) > max_panjang_path:  # terlalu panjang utk di baris #1
            if len(cwd) < max_panjang_line:  # cukup 1 line->di new line saja
                cwd = "\n" + cwd
            else:
                cwd = cwd[:max_panjang_path] + "\n" + cwd[max_panjang_path:]
        format1 = f"""<host>[{terminal_lines}x{terminal_cols}|{lang}{active_project_file}|GHOQTUcnrs] {day_date_month} 👷{doy} {waktu} [📁{free_space}🧠{free_mem}] {cwd}</host>"""
        format2 = "<colon>▶ </colon>"
        # return HTML(format1 + ('\n'+self.git_info if self.git_info else '') + "\n" + format2)
        return HTML(format1 + "\n" + format2)

    def create_validator_from_choices(self, choices, pesan_error=None):
        def isvalid(text):
            return text.lower() in [item.lower() for item in choices]

        validator = Validator.from_callable(
            isvalid,
            move_cursor_to_end=True,
            error_message=(
                pesan_error if pesan_error else "Pilih salah satu " + str(choices)
            ),
        )
        return validator

    def temporary_prompt(
        self,
        prompt_message=HTML("<b>Pilih <u>salah</u> <i>satu</i>: </b>"),
        choices=["satu", "dua", "tiga"],
        meta_dict=None,
        do_validation=True,
        completer=None,
    ):
        """
        https://pygments.org/docs/styles/
        ansiblack
        ansired
        ansigreen
        ansiyellow
        ansiblue
        ansimagenta
        ansicyan
        ansigray
        ansibrightblack
        ansibrightred
        ansibrightgreen
        ansibrightyellow
        ansibrightblue
        ansibrightmagenta
        ansibrightcyan
        ansiwhite
        """

        if not meta_dict:
            meta_dict = dict(
                zip(choices, choices)
            )  # perlu agar selain handle-cirebon yg masih kasih completer via choices, bukan meta_dict
            if do_validation:
                validator = self.create_validator_from_choices(choices)
        else:
            if do_validation:
                validator = self.create_validator_from_choices(meta_dict.keys())

        jawab = self.session.prompt(
            HTML(
                f"<style fg=\"ansiyellow\" bg=\"ansibrightblue\">(Press tab➡️, 'x' or 'exit' to quit)\n{html.escape(prompt_message)}</style>"
            ),
            # completer=FuzzyWordCompleter(choices),
            # completer=create_meta_completer(meta_dict),
            # shg bs ikutin gaya dict yg diberikan utk completer
            completer=(
                FuzzyCompleter(
                    NestedCompleter.from_nested_dict(update_nested_dict(meta_dict))
                )
                if not completer
                else completer
            ),
            # completer=FuzzyCompleter(NestedCompleter.from_nested_dict(meta_dict)),
            complete_while_typing=True,
            complete_style=(
                CompleteStyle.MULTI_COLUMN
                if config_app["multicolumn"]
                else CompleteStyle.COLUMN
            ),
            # rprompt=show_time,
            rprompt=self.mengisi_textarea_dengan_waktu,  # mengisi_textarea_dengan_waktu, config_app['temporary_prompt_current_fmusfile']
            refresh_interval=1,
            mouse_support=True,
            # history=self.our_history,
            validator=validator if do_validation else None,
            validate_while_typing=True if do_validation else False,
            clipboard=PyperclipClipboard(),
            style=prompt_style_temporary,
            # perlu own keybinding utk keluar...
        )
        # print('Anda memilih:', jawab)
        # self.change_completer(self.previous_words)
        self.refresh_completer()
        # self.previous_words = self.previous_words
        # self.session = self.create_prompt_session(FuzzyWordCompleter(self.previous_words), self.previous_words)
        return jawab

    def temporary_prompt_for_bahasa(self, completer, prompt_message="⏩", kanan=None):
        jawab = self.session.prompt(
            HTML(
                f"<style fg=\"ansiyellow\" bg=\"ansibrightblue\">(Press tab➡️ to choose, #entry to edit, 'x' or 'exit' to quit)\n{html.escape(prompt_message)}</style>"
            ),
            completer=completer,
            complete_while_typing=True,
            complete_style=(
                CompleteStyle.MULTI_COLUMN
                if config_app["multicolumn"]
                else CompleteStyle.COLUMN
            ),
            # rprompt=kanan if kanan else show_time,
            rprompt=lambda: self.mengisi_textarea_dengan_logged_dict(
                kanan
            ),  # config_app['temporary_prompt_logged_dict']
            refresh_interval=1,
            mouse_support=True,
            clipboard=PyperclipClipboard(),
            # history
            # keybinding
        )
        return jawab

    def loop_temporary_prompt_for_bahasa(self, completer, callback, kanan=None):
        jawab = None
        while jawab not in ["x", "exit"]:
            jawab = self.temporary_prompt_for_bahasa(completer, kanan=kanan)
            if jawab:
                if jawab == "c":
                    os.system("cls")
                    print()
                else:
                    # jawab adlh wrapper utk file+barisentry, decode dan ambil contentnya
                    callback(jawab)

    def text_area_set(self, data):
        self.session.text_area.text = data

    def text_area_append(self, data, add_newline=False):
        self.session.text_area.text += ("\n" if add_newline else "") + data

    def mengisi_textarea(self):
        content = get_app().current_buffer.document.text
        # next kita proses hanya jika content berisi fmus...
        result = content
        if "🧭" in content:
            if not config_app["show_textarea"]:
                last_prompt = content.split()[0]  # ambil yg terpisah space pertama, krn ini cara trigger menu dropdown
                config_app["show_textarea"] = True
                config_app["text_area_height"] = 10  # tentu pengen yg bisa lihat dg enak
                self.refresh_completer()
                # get_app().current_buffer.document.text = last_prompt  # Exception property 'text' of 'Document' object has no setter
                # print('last_prompt:', last_prompt, 'jenis:', type(last_prompt))
                get_app().current_buffer.validate_and_handle()
                # ini duluan/terlalu cepat
                # get_app().current_buffer.text = last_prompt  # ini belum accept/validate
            paths = extract_file_paths(content)
            if not paths and ('FP_CONFIG_DIR' in content or 'FP_ROOT_DIR' in content):
                # replace keyword-dir
                path = content.replace('FP_CONFIG_DIR', r"C:\work\ciledug\ciledug\fmusperintah\configs").replace('FP_ROOT_DIR', r"C:\work\ciledug\ciledug\fmusperintah")
                # try again
                paths = extract_file_paths(path)

            # print('mengisi_textarea:', paths)
            for path in paths:  # padahal kita bikin hanya ada satu path dlm content
                if not isfile(path) and not '.fmus=' in path and not '.mk=' in path:  # utk hindari exception
                    continue

                result = ""
                if ".fmus" in path or ".mk" in path:
                    if "=" in path:  # jika fmusfilepath=barisentry
                        # filepath, barisentry
                        # result = define_filepath_equal(path)
                        result, lineno = define_filepath_equal_with_lineno(path)
                        repl_service.last_file = path.split("=")[0].strip()
                        repl_service.last_lineno = lineno
                    else:  # jika fmusfilepath
                        result = get_daftar_isi(path)
                        if (
                            len(result) == 1
                        ):  # jk cuma 1 barisentry spt default, baca saja isinya
                            result, lineno = define_filepath_barisentry_with_lineno(
                                path, result[0]
                            )
                            repl_service.last_file = path
                            repl_service.last_lineno = lineno
                        else:
                            result = "\n".join(result)
                elif isfile(path):  # hati2, bisa salah kena dir
                    result = file_content(path)
                if result:
                    trycopy(result)
        elif "🌄" in content:  # coba tambah ini
            paths = extract_file_paths(content)
            for path in paths:
                if is_image_file(path):
                    mulai(os.system, args=(path,))
                    # os.system(path)  # tampilkan gambar
        # set text area hanya jk focus bukan pada text area, shg kita bs work pd text area tsb
        # apa ini penyebab jika ngetik di text_area_editor maka tampil juga di text_area?
        if not config_app["enable_page_navigation_bindings"]:
            self.text_area_set(result)
        return ""  # rprompt kita kosongkan

    def mengisi_textarea_dengan_waktu(self):  # utk temporary prompt
        barisentry = get_app().current_buffer.document.text
        # next kita proses hanya jika content berisi fmus...
        result = barisentry
        if (
            result != config_app["temporary_prompt_last_barisentry"]
        ):  # kita proses hanya jika user select barisentry baru
            config_app["temporary_prompt_last_barisentry"] = result
            if config_app["temporary_prompt_current_fmusfile"]:
                result, lineno = define_filepath_barisentry_with_lineno(
                    config_app["temporary_prompt_current_fmusfile"], barisentry
                )
                if result:
                    trycopy(result)
                    self.text_area_set(result)
                    repl_service.last_file = config_app[
                        "temporary_prompt_current_fmusfile"
                    ]
                    repl_service.last_lineno = lineno
        return datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")

    def mengisi_textarea_dengan_logged_dict(
        self, tulisan_kanan=None
    ):  # utk temporary prompt bahasa yg pake logged-dict
        # config_app['temporary_prompt_logged_dict']
        wrapper_barisentry = get_app().current_buffer.document.text
        # next kita proses hanya jika content berisi fmus...
        result = wrapper_barisentry
        if (
            result != config_app["temporary_prompt_last_barisentry"]
        ):  # proses jk hanya barisentry baru
            config_app["temporary_prompt_last_barisentry"] = result
            if config_app["temporary_prompt_logged_dict"]:
                result = logged_dict_to_content(
                    config_app["temporary_prompt_logged_dict"], wrapper_barisentry
                )
                if result:
                    trycopy(result)
                    self.text_area_set(result)
        return (
            tulisan_kanan
            if tulisan_kanan
            else datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
        )

    def path_completer(self):
        daftar_isi = ["..", "x", "exit"]
        jawab = None
        while jawab not in ["x", "exit"]:
            jawab = self.temporary_prompt(
                prompt_message=os.getcwd() + "> ",
                choices=daftar_isi,
                do_validation=False,
                completer=PathCompleter(),
            )
            if jawab:
                if isdir(jawab):
                    lokasi = jawab
                    if is_only_dots(lokasi):  # cd ., cd .., cd ..., cd ....
                        lokasi = navigate_back_multiple(os.getcwd(), jawab)
                        # print('navigate_back_multiple', lokasi)
                    elif jawab.startswith(".."):  # cd ..repository, cd...main
                        lokasi = navigate_back(os.getcwd(), jawab)
                        # print('navigate_back', lokasi)
                    os.chdir(lokasi)
                elif isfile(jawab):
                    if is_file_not_binary(jawab):
                        print_source_code_file_with_markdown(jawab)
                    else:
                        indah4(f"{jawab} is binary.", warna="yellow")
        self.refresh_completer()

    def run(self):
        self.before_run()
        while not self.done:
            try:
                text = self.session.prompt(
                    self.prompt,
                    auto_suggest=AutoSuggestFromHistory(),
                    # rprompt=show_time,  # nanti ganti bisa handle current buffer
                    # rprompt=lambda: f"#{len(self.prompt.value)}"
                    # rprompt=lambda: f"#{len(self.prompt.value)}"
                    # rprompt=lambda: get_app().current_buffer.document.text
                    rprompt=lambda: self.mengisi_textarea(),
                )
                if text in keluar:
                    break
                elif text:
                    self.process(text)
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
            except Exception as exc:
                pass
                # print('repl run() err:', exc)
                # print(traceback.format_exc())

    def process(self, text, strip=True):
        # global using_thread, search_result_to_commands
        global search_result_to_commands

        if strip:
            text = text.strip()

        # perkenalkan alias dg rekursif
        if statement_delimiter in text:  # handle penggunaan ;;;
            for statement in text.split(statement_delimiter):
                self.process(statement)
            return

        # # perkenalkan potong kiri <| dan potong kanan |>, tentu karakter ini jarang dipake spt halnya statement_delimiter
        # # ternyata hrs duluan dari ;u dsb karena suka begini ... <| ;u alamat ;;; other-statement
        # if potong_kiri in text or potong_kanan in text:
        # 	# jangan lupa utk strip, karena "gen" dan " gen" jadi berbeda, " gen" malah panggilan wmcgen
        # 	if potong_kiri in text:
        # 		_, text = [item.strip() for item in text.split(potong_kiri, 1)]
        # 	if potong_kanan in text:
        # 		text, _ = [item.strip() for item in text.split(potong_kanan, 1)]
        # 	# kita biarkan text turun ke bawah
        text = potongify(text)

        if text.startswith(";"):  # handle ;k utk #ketik#, ;r utk #run#, ;u utk #url#
            """
            ;k sesuatu utk diketik
            ;r sesuatu utk run fmus
            ;u sesuatu utk buka url
            ;c sesuatu utk run cmd in shell => eh ini gak perlu lah...langsung saja
            ADD:
            bisa bbrp perintah sekaligus? too risky? misal ;k | ;k | ;k utk bikin 3 #ketik#
            """
            if text.startswith(";k"):
                code = text.replace(";k", "#ketik#", 1)
                self.process(code)
            elif text.startswith(";r"):
                code = text.replace(";r", "#run#", 1)
                self.process(code)
            elif text.startswith(";u"):
                code = text.replace(";u", "#url#", 1)
                self.process(code)
            # elif text.startswith(';c'):
            # 	code = text.replace(';c', '###', 1)
            # 	self.process(code)
            return

        # text = inputify(text)  # jangan lupa sblm dimakan ###, dsb
        # text = inputify_running(text)  # jangan lupa sblm dimakan ###, dsb
        text = inputify_varify_running(text)  # dukung __VAR1__ dsb

        if "###" in text:  # misal ###code
            # abaikan ### perintah dengan os.system
            # ini adlh perintah yg perlu dijalankan
            _, text = text.split("###", 1)
            # text = bongkar(text)  # /etc/mysql/sakila menjadi \etc\mysql\sakila, sialan
            # indah4(f'fmusperintah:cmd ==> {text}', warna='yellow')
            indah4("▶️", warna="yellow")
            os.system(text)
            return

        if "#ketik#" in text or "✍️" in text:
            if "#ketik#" in text:
                # whatever: #ketik#python someplace.py
                _, text = [item.strip() for item in text.split("#ketik#", 1)]
            else:
                _, text = [item.strip() for item in text.split("✍️", 1)]
            # text = bongkar(text)  # gawat g //S dikonversi ke g\S krn normy
            text = "/ketik)" + text  # tambahkan fmus code /ketik)
            # indah4(f'fmusperintah:ketik ==> {text}', warna='yellow')
            indah4("⌨️👩‍💻", warna="yellow")
            if config_app["thread"]:
                thread = run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
                print(thread)
            else:
                run_fmus_for_content(text, dirpath=os.getcwd())
            return

        if (
            "#run#" in text or "⚡" in text
        ):  # run literal fmus content, bisa ⚡ utk ganti #run#
            # TODO: bisa search image dan save...harus cari yg punya api...
            # whatever: #ketik#python someplace.py
            if "#run#" in text:
                _, text = [item.strip() for item in text.split("#run#", 1)]
            else:
                _, text = [item.strip() for item in text.split("⚡", 1)]
            if text in [
                "clipboard",
                "clipboard*",
            ]:  # #run#clipboard untuk kode fmus yg berada di clipboard
                content = trypaste()
                if content:
                    if not content.endswith("\n"):
                        content += "\n"

                    do_execute = False
                    if text == "clipboard*":  # force
                        do_execute = True
                    else:
                        jawab = confirm(f"Exec fmus clipboard [{content}]?")
                        if jawab:  # True or False
                            do_execute = True
                    if do_execute:
                        if config_app["thread"]:
                            run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
                        else:
                            run_fmus_for_content(content, dirpath=os.getcwd())
            else:
                # harus bisa gunakan \n dan \t utk fmuslang
                text = text.replace('\\n', '\n').replace('\\t', '\t')
                text = inputify(text)
                if not text.endswith("\n"):
                    text += "\n"
                # indah4(f'fmusperintah:run ==> {text}', warna='yellow')
                indah4("🚀", warna="yellow")
                # text = '/ketik)' + text  # tambahkan fmus code /ketik)
                # print('fmusperintah:ketik ==>', text)
                if config_app["thread"]:
                    run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
                else:
                    run_fmus_for_content(text, dirpath=os.getcwd())
            return

        if "#url#" in text or "🌐" in text:
            # if text.startswith('#url#'):
            # 	# jika #url#alamat
            # 	text = text.removeprefix('#url#').strip()
            # else:
            if "#url#" in text:
                # jika whatever#url#alamat
                _, text = [item.strip() for item in text.split("#url#", 1)]
            else:
                _, text = [item.strip() for item in text.split("🌐", 1)]

            text = inputify(text)
            if not text.startswith("http") and not text in ["|"] and not "|" in text:
                text = "http://" + text
            # indah4(f'fmusperintah:url ==> {text}', warna='yellow')
            indah4(f"🌐{text}", warna="yellow")
            run_url(text)
            return

        if "#reflect#" in text or "🪞" in text:
            if text.startswith("#reflect#"):
                # jika #reflect#package
                query = text.removeprefix("#reflect#").strip()
            elif text.startswith("🪞"):
                query = text.removeprefix("🪞").strip()
            else:
                # jika whatever#reflect#package
                if "#reflect#" in text:
                    _, query = [item.strip() for item in text.split("#reflect#", 1)]
                else:
                    _, query = [item.strip() for item in text.split("🪞", 1)]
            # if query.startswith("schnell"):  # hanya proses schnell package
            #     process_quick("ref)" + query)
            process_quick("ref)" + query)
            return

        if "#file#" in text or "🚀" in text:  # run fmus utk argumen filepath
            if "#file#" in text:
                _, filepath = [item.strip() for item in text.split("#file#", 1)]
            else:
                _, filepath = [item.strip() for item in text.split("🚀", 1)]
            content = file_content(filepath)
            if config_app["thread"]:
                run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
            else:
                run_fmus_for_content(content, dirpath=os.getcwd())
            return

        if "#copy#" in text or "#@#" in text or "📋" in text:  # copy text di kanan ke clipboard
            if "#copy#" in text:
                _, contentkanan = [item.strip() for item in text.split("#copy#", 1)]
            elif "#@#" in text:
                _, contentkanan = [item.strip() for item in text.split("#@#", 1)]
            else:
                _, contentkanan = [item.strip() for item in text.split("📋", 1)]
            if contentkanan:
                trycopy(contentkanan)
            return

        if "#x#" in text:  # explorer filepath di kanan
            _, contentkanan = [item.strip() for item in text.split("#x#", 1)]
            if contentkanan:
                os.system(f"explorer {contentkanan}")
            return

        if "#image#" in text:  # view image setara dg 🌄 (tapi tanpa recurring karena diexec stlh tekan enter)
            paths = extract_file_paths(text)
            for path in paths:
                if is_image_file(path):
                    mulai(os.system, args=(path,))
            return

        if (
            "#file-entry#" in text or "✂️" in text
        ):  # run fmus utk argument filepath=barisentry
            # whatever #file-entry# filepath
            if "#file-entry#" in text:
                _, string_fmusfile_barisentry = [
                    item.strip() for item in text.split("#file-entry#", 1)
                ]
            else:
                _, string_fmusfile_barisentry = [
                    item.strip() for item in text.split("✂️", 1)
                ]
            if not "=" in string_fmusfile_barisentry:
                indah4(
                    f"tidak ada '=' pada [{string_fmusfile_barisentry}] untuk request [{text}]",
                    warna="red",
                )
                return
            filepath, barisentry = string_fmusfile_barisentry.split("=", 1)
            # content = get_definition_fmusfile_barisentry(fmusfile_barisentry)
            if config_app["thread"]:
                # run_fmus_for_content_in_thread(content, dirpath=os.getcwd())
                run_fmus_for_file_in_thread(
                    filepath, barisentry, new_working_folder=os.getcwd()
                )
            else:
                # run_fmus_for_content(content, dirpath=os.getcwd())
                run_fmus_for_file(filepath, barisentry, new_working_folder=os.getcwd())
            return

        elif text.startswith("/"):  # search
            # indah4(f'fmusperintah:search ==> {text}', warna='yellow')
            indah4(f"🔍", warna="yellow")
            # text = '/' + text  # //query
            # if config_app['thread']:
            # 	# thread = run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
            # 	# print(thread)
            # 	# os.system(text)
            # 	run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
            # else:
            # 	run_fmus_for_content(text, dirpath=os.getcwd())

            # lebih baik direct, lebih cepat...
            text = text.removeprefix("/").strip()
            # special utk /`...setara dg ` di kbrepl
            if text.startswith("`"):
                baris = [
                    item
                    for item in bahasa_repl.splitlines()
                    if item
                    and ":" in item
                    and "HURUF" not in item
                    and item.endswith('"')
                ]
                code = text.removeprefix("`").strip()
                if code:
                    baris = [item for item in baris if code in item]
                else:
                    pass
                print("\n".join(baris))
            else:
                # kirim "self" sbg repl service
                # redis_repl(text, self)
                redis_repl(
                    text, repl_service
                )  # utk f12 bisa akses last_file dan last_lineno
            return

        elif text.startswith(":"):  # execute code
            text = text.removeprefix(":").strip()
            if text:
                execute_code(text)
            return

        elif (text.startswith("@") and not "=>" in text):  # old replify, skip jk "ada => di input" yang khusus utk file manip
            text = text.removeprefix("@").strip()
            lang = creator_context["current_language"]
            # jk /R)py/ tapi bukan /R)/... yg minta cari
            if "/" in text and not text.startswith("/"):  # @scala/fM
                _lang, _request = text.split(
                    "/", 1
                )  # bisa /R)f//sass?e, jadi gak selalu /R)scala/ff
                if _lang in programming_languages:
                    lang = _lang
                    text = _request
            hasil = replify(text, os.getcwd(), lang)
            indah3(hasil, warna="blue")
            return

        elif text.startswith("%"):  # dict play/search, %% utk cari nama file.json yg berisi query
            query = text.removeprefix("%").strip()
            if query:
                if query in ["print", "pp", "p"]:
                    from rich.pretty import pprint

                    pprint(original_dict_to_json)
                elif query.startswith("%"):
                    edit_mode = False
                    query = query.removeprefix("%").strip()
                    if query.endswith("*"):  # bisa edit
                        edit_mode = True
                        query = query.removesuffix("*").strip()
                    found = {k: v for k, v in original_dict_keys.items() if query in k}
                    exact_found = {k: v for k, v in found.items() if v.endswith(query+'.json')}
                    if exact_found:
                        if edit_mode:
                            try:
                                json_file = list(exact_found.values())[0]
                                os.system(f"vscode {json_file}")
                            except Exception as e:
                                indah4(str(e), warna="red")
                    elif found:
                        # print_json(found)
                        for index, (key, value) in enumerate(found.items(), start=1):
                            indah4(f"{index}. {key}\n\t✨ {value}", warna='green')
                        pilihan = 0
                        if len(found) > 1:
                            pilihan = prompt(
                                f"Masukkan pilihan (1 sampai {len(found)}) untuk edit: "
                            )
                            if pilihan and 1 <= int(pilihan) <= len(found):
                                pilihan = int(pilihan) - 1
                        if edit_mode:
                            try:
                                json_file = list(found.values())[pilihan]
                                # print('edit:', json_file)
                                # json_file = found[first_key]
                                os.system(f"vscode {json_file}")
                            except Exception as e:
                                indah4(str(e), warna="red")
                    # 	else:
                    # 		print('not editing')
                    # else:
                    # 	print('not found')
                else:
                    # search_result_to_commands = contains_search_nested_dict(original_dict_to_json, query, delimiter=' ')
                    search_result_to_commands = pattern_search_nested_dict(
                        original_dict_to_json, query, delimiter=" "
                    )
                    if search_result_to_commands:
                        print_list_warna(search_result_to_commands, start=1)
                        indah4(
                            f"\nType '1' to '{len(search_result_to_commands)}' to execute selected command from above.",
                            warna="cyan",
                        )
                    else:
                        print_json(original_dict_to_json)
                        indah4("\nNo result.", warna="cyan")
            return

        # elif text.startswith('$'):  # reload kenza.txt
        # 	query = text.removeprefix('$').strip()
        # 	if query in ['reload']:
        # 		remove_keys_starting_with_special_char_inplace(original_dict_to_json)
        # 		update_with_kenza_folders(reload=True)
        # 		self.refresh_completer()
        # 		indah4('original_dict_to_json reloaded...', warna='white')
        # 	else:
        # 		process_kenza(query)
        # 	return

        elif text.startswith(
            "."
        ):  # replify, belum handle multiple statements dari repl-lang => err sudah, tinggal . Mdet dst
            # intercept .env
            if text.startswith(".env"):
                text = text.removeprefix(".env").strip()
                from handlers import handle_env

                handle_env(text)
                return

            text = text.removeprefix(".").strip()

            # handle replify
            if not text:
                return

            if text.startswith("\\"):
                # ganti language
                lang = text.removeprefix("\\").strip()
                if lang in creator_languages:
                    creator_context["current_language"] = lang
                    print_json(creator_context)
                return

            if not text in ["f12", "`"]:
                text = "f" + text

            lang = creator_context["current_language"]
            # jk /R)py/ tapi bukan /R)/... yg minta cari
            if "/" in text and not text.startswith("/"):
                _lang, _request = text.split(
                    "/", 1
                )  # bisa /R)f//sass?e, jadi gak selalu /R)scala/ff
                if _lang in programming_languages:
                    lang = _lang
                    text = _request

            hasil = replify(text, os.getcwd(), lang)
            indah3(hasil, warna="blue")
            return

        elif text.startswith("ciledug "):
            text = text.removeprefix("ciledug ").strip()
            from handlers import handle_ciledug

            handle_ciledug(text, self.temporary_prompt, self.refresh_completer)
            return

        elif text.startswith("cirebon "):
            text = text.removeprefix("cirebon ").strip()
            # indah4(f"main/handle_cirebon => {text}.", warna='green')
            from handlers.handle_cirebon import handle_cirebon

            # indah4(f"main/handle_cirebon lanjut => {text}.", warna='green')
            handle_cirebon(text, self.temporary_prompt, self.refresh_completer)
            return

        elif text.startswith("-"):
            text = text.removeprefix("-").strip()
            # indah4(f"main/handle_cirebon => {text}.", warna='green')
            from handlers.handle_minus import handle_minus

            # indah4(f"main/handle_cirebon lanjut => {text}.", warna='green')
            handle_minus(text, self.session, self.refresh_completer)
            return

        # oprek english
        elif text.startswith("E ") or text.startswith("eng "):  # english bisa E atau eng
            if text.startswith("E "):
                text = text.removeprefix("E ").strip()
            else:
                text = text.removeprefix("eng ").strip()
            process_writer(text, print_result=True)
            return

        elif text.isdigit():
            last_entry = self.get_last_entry(
                -2
            )  # index -2, krn index -1 itu text digit
            if search_result_to_commands and last_entry.startswith("%"):
                key = int(text) - 1
                if 0 <= key <= len(search_result_to_commands):
                    panggil = search_result_to_commands[key]
                    # # # ini gak jalan:
                    # # get_app().current_buffer.text = search_result_to_commands[key]
                    # panggil = potongify(panggil)
                    # print('stlh terpotong:', panggil)
                    panggil_proses = html.escape(panggil)
                    lanjut = confirm(HTML(f"Yakin jalankan {panggil_proses}? "))
                    if lanjut:
                        self.process(panggil)
                        self.add_to_history(
                            panggil
                        )  # krn cuma digit yg masuk ke history
            else:
                indah4(
                    f"no search_result_to_commands [{len(search_result_to_commands)}] AND last_entry [{last_entry}] dont start with %.",
                    warna="red",
                )
            return

        elif text.startswith("lalang"):
            text = text.removeprefix("lalang").strip()
            if text.startswith("/"):  # lalang/ts, lalang/go, lalang/=lalang/py
                bahasa = text.removeprefix("/").strip()
                if not bahasa:
                    bahasa = "py"
                from handlers.lalang_handler import handle_lalang

                handle_lalang(self.temporary_prompt, self.refresh_completer, bahasa)
            else:
                process_lalang(text, returning=False)
            return

        elif text.startswith("declang") and not text.startswith("declang2"):
            text = text.removeprefix("declang").strip()
            if not text:
                handle_declang(self.temporary_prompt, self.refresh_completer)
            elif text.startswith("load:"):
                text = text.removeprefix("load:").strip()
                if text.startswith("elem="):
                    text = text.removeprefix("elem=").strip()
                    if text in ["@"]:
                        load_from_clipboard("elem")
                elif text.startswith("attr="):
                    text = text.removeprefix("attr=").strip()
                    if text in ["@"]:
                        load_from_clipboard("attr")
                elif text.startswith("value="):
                    text = text.removeprefix("value=").strip()
                    if text in ["@"]:
                        load_from_clipboard("value")
                elif text.startswith("cdata="):
                    text = text.removeprefix("cdata=").strip()
                    if text in ["@"]:
                        load_from_clipboard("cdata")
            elif text.startswith("print:"):
                text = text.removeprefix("print:").strip()
                if not text:
                    print_json(elem_mapper)
                    print_json(attr_mapper)
                    print_json(value_mapper)
                    print_json(cdata_mapper)
            else:
                process_declang2(text, returning=False)
            return

        elif text.startswith("declang2"):
            text = text.removeprefix("declang2").strip()
            if not text:
                handle_declang(self.temporary_prompt, self.refresh_completer)
            else:
                process_declang1(text, as_service=False)
            return

        elif text.startswith("mycsv"):
            text = text.removeprefix("mycsv").strip()
            from handlers.mycsv_handler import handle_mycsv

            handle_mycsv(self.temporary_prompt, self.refresh_completer)
            return

        elif text.startswith("cepat"):
            text = text.removeprefix("cepat").strip()
            from handlers.cepat_handler import handle_cepat_mycsv

            handle_cepat_mycsv(self.temporary_prompt, self.refresh_completer)
            return

        elif text.startswith("palsu"):
            query = text.removeprefix("palsu").strip()
            if not query:
                from handlers.palsu_handler import handle_palsu

                handle_palsu(self.temporary_prompt, self.refresh_completer)
            else:
                process_quick("palsu)" + query)
            return

        elif text.startswith("history"):
            code = text.removeprefix("history").strip()
            sejarah = list(self.our_history.load_history_strings())
            balik = sejarah[::-1]
            if code:
                if code.isdigit():  # jika pengen last n history
                    balik = balik[-1 * int(code) :]  # history 5 => -5:
                else:
                    balik = [item for item in balik if code in item]
            print_list_warna(balik, start=1)
            return

        elif text.startswith("watch:"):
            query = text.removeprefix("watch:").strip()
            if query == "ts":
                from handlers import typescript_watcher

                typescript_watcher()
            elif query == "py":
                from handlers import python_watcher

                python_watcher()
            elif query == "elixir":
                from handlers import elixir_watcher

                elixir_watcher()
            else:
                print(query, "not implemented.")
            return

        elif text == "F":  # processor_files
            try:
                processor_files(self.temporary_prompt)
            except:
                self.refresh_completer()
            return

        elif text == "D" or text.startswith("D "):  # processor_folders
            try:
                if text.startswith("D"):
                    basefolder = text.removeprefix("D").strip()
                    if isdir(basefolder):
                        processor_folders_with_args(self.temporary_prompt, basefolder)
                    else:
                        indah4(f"{basefolder} is not a directory.", warna="red")
                else:
                    processor_folders(self.temporary_prompt)
            except:
                self.refresh_completer()
            return

        elif text in ["cls", "clear", "c"]:
            os.system("cls")
            # print()
            self.refresh_completer()

        # elif text.startswith("thr="):
        #     # thr=0, thr=1
        #     text = text.removeprefix("thr=").strip()
        #     if not text:
        #         print("using_thread:", config_app["thread"])
        #     elif text.isdigit():
        #         nilai = int(text)
        #         config_app["thread"] = bool(nilai)

        elif text.startswith("config:"):  # config:thr=1, config:thr=0
            text = text.removeprefix("config:").strip()

            if not text:
                print_json(config_app)
                # print_json(original_dict_keys)

            elif text.startswith("thread="):  # config:thread=
                nilai = text.removeprefix("thread=").strip()
                if nilai and nilai.isdigit():
                    config_app["thread"] = bool(int(nilai))

            elif text.startswith("openai_key="):  # config:openai_key=
                nilai = text.removeprefix("openai_key=").strip()
                if nilai:
                    config_app["openai_key"] = nilai
                    print_json(config_app)

            elif text.startswith("openai_model="):  # config:openai_model=
                nilai = text.removeprefix("openai_model=").strip()
                if nilai:
                    config_app["openai_model"] = nilai

            elif text.startswith("openai_temperature="):  # config:openai_temperature=
                nilai = text.removeprefix("openai_temperature=").strip()
                if nilai and nilai.isdigit():
                    config_app["openai_temperature"] = int(nilai)

            elif text.startswith("server:fastapi:port"):  # configserver:fastapi:port=
                nilai = text.removeprefix("server:fastapi:port").strip()
                if nilai and nilai.isidit():
                    config_app["server:fastapi"]["port"] = int(nilai)
                    print_json(config_app["server:fastapi"])

            elif text.startswith("text_area_height="):
                nilai = text.removeprefix("text_area_height=").strip()
                if nilai and nilai.isdigit():
                    config_app["text_area_height"] = int(nilai)
                    self.refresh_completer()

            elif text.startswith("text_area_style="):  # config:text_area_style=
                nilai = text.removeprefix("text_area_style=").strip()
                if nilai:
                    config_app["text_area_style"] = nilai
                    self.refresh_completer()

            elif text.startswith("text_area_lexer="):  # config:text_area_lexer=
                nilai = text.removeprefix("text_area_lexer=").strip()
                if nilai:
                    config_app["text_area_lexer"] = nilai
                    self.refresh_completer()

            elif text.startswith("show_textarea_editor="):  # config:text_area_lexer=
                nilai = text.removeprefix("show_textarea_editor=").strip()
                if nilai and nilai.isdigit():
                    config_app["show_textarea_editor"] = bool(int(nilai))
                    self.refresh_completer()

            elif text.startswith("show_bottom_toolbar="):  # config:text_area_lexer=
                nilai = text.removeprefix("show_bottom_toolbar=").strip()
                if nilai and nilai.isdigit():
                    config_app["show_bottom_toolbar"] = bool(int(nilai))
                    self.refresh_completer()

            elif text == "vscode":
                from schnell.app.inpututils.survey_input import input_survey_select
                pilih = input_survey_select("Masukkan versi vscode: ", vscode_exec)
                print("pilih:", pilih, "OK?", pilih in vscode_exec)
                if pilih in vscode_exec:
                    config_app["vscode"] = pilih

            elif text.startswith("models:cohere"):
                from schnell.app.llmutils.langchainutils.llm_config import cohere_models, cohere_models_get_default
                if len(cohere_models)==1:
                    indah4("Cuma ada 1 model di cohere_models", warna="yellow")
                    indah4(json.dumps(cohere_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(cohere_models.keys())
                    current_model = cohere_models_get_default()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in cohere_models:
                        cohere_models_get_default(nilai)
                        print(cohere_models_get_default())
                        self.refresh_completer()

            elif text.startswith("models:groq"):
                from schnell.app.llmutils.langchainutils.llm_config import groq_models, groq_models_get_default
                if len(groq_models)==1:
                    indah4("Cuma ada 1 model di groq_models", warna="yellow")
                    indah4(json.dumps(groq_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(groq_models.keys())
                    current_model = groq_models_get_default()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in groq_models:
                        groq_models_get_default(nilai)
                        print(groq_models_get_default())
                        self.refresh_completer()
            elif text.startswith("models:gemini"):
                from schnell.app.llmutils.langchainutils.llm_config import gemini_models, gemini_models_get_default
                if len(gemini_models)==1:
                    indah4("Cuma ada 1 model di gemini_models", warna="yellow")
                    indah4(json.dumps(gemini_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(gemini_models.keys())
                    current_model = gemini_models_get_default()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in gemini_models:
                        gemini_models_get_default(nilai)
                        print(gemini_models_get_default())
                        self.refresh_completer()
            elif text.startswith("models:gemini:vision"):
                from schnell.app.llmutils.langchainutils.llm_config import gemini_models, google_models_get_default_for_vision
                if len(gemini_models)==1:
                    indah4("Cuma ada 1 model di gemini_models", warna="yellow")
                    indah4(json.dumps(gemini_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(gemini_models.keys())
                    current_model = google_models_get_default_for_vision()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in gemini_models:
                        google_models_get_default_for_vision(nilai)
                        print(google_models_get_default_for_vision())
                        self.refresh_completer()
            elif text.startswith("models:huggingface"):
                from schnell.app.llmutils.langchainutils.llm_config import huggingface_models, huggingface_models_get_default
                if len(huggingface_models)==1:
                    indah4("Cuma ada 1 model di huggingface_models", warna="yellow")
                    indah4(json.dumps(huggingface_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(huggingface_models.keys())
                    current_model = huggingface_models_get_default()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in huggingface_models:
                        huggingface_models_get_default(nilai)
                        print(huggingface_models_get_default())
                        self.refresh_completer()
            elif text.startswith("models:openai"):
                from schnell.app.llmutils.langchainutils.llm_config import openai_models, openai_models_get_default
                if len(openai_models)==1:
                    indah4("Cuma ada 1 model di openai_models", warna="yellow")
                    indah4(json.dumps(openai_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(openai_models.keys())
                    current_model = openai_models_get_default()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in openai_models:
                        openai_models_get_default(nilai)
                        print(openai_models_get_default())
                        self.refresh_completer()
            elif text.startswith("models:openai:vision"):
                from schnell.app.llmutils.langchainutils.llm_config import openai_models, openai_models_get_default_for_vision
                if len(openai_models)==1:
                    indah4("Cuma ada 1 model di openai_models", warna="yellow")
                    indah4(json.dumps(openai_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(openai_models.keys())
                    current_model = openai_models_get_default_for_vision()
                    nilai = radio("judul", "isi", semua_keys, current_model)
                    if nilai and nilai in openai_models:
                        openai_models_get_default_for_vision(nilai)
                        print(openai_models_get_default_for_vision())
                        self.refresh_completer()
            elif text.startswith("models:together"):
                from schnell.app.llmutils.langchainutils.llm_config import together_models, together_models_get_default
                if len(together_models)==1:
                    indah4("Cuma ada 1 model di together_models", warna="yellow")
                    indah4(json.dumps(together_models,indent=2))
                else:
                    from schnell.app.promptutils import radio, check
                    semua_keys = list(together_models.keys())
                    current_model = together_models_get_default()
                    nilai = radio("models:together", "Pilih model untuk models:together", semua_keys, current_model)
                    if nilai and nilai in together_models:
                        together_models_get_default(nilai)
                        print(together_models_get_default())
                        self.refresh_completer()
            elif text.startswith("models:active="):
                from schnell.app.llmutils.langchainutils.llm_config import invoke_all, all_accounts, change_active_model
                nilai = text.removeprefix("models:active=").strip()
                if nilai and nilai in invoke_all.keys():
                    change_active_model(nilai)
                    print_json(all_accounts)
            elif text.startswith("models"):  # config:models
                from schnell.app.llmutils.langchainutils.llm_config import invoke_all, all_accounts, llm_models
                # information = f"*** llm_models:\n{llm_models}\n\n*** invoke_all:\n{invoke_all}\n\n*** all_accounts:\n{all_accounts}"
                indah4('*** llm_models', warna='yellow')
                print_json(llm_models)
                indah4('*** invoke_all', warna='green')
                print_json(invoke_all)
                indah4('*** all_accounts', warna='blue')
                print_json(all_accounts)
            elif text.startswith("invoke_all="):  # config:invoke_all=gemini,cohere, config:invoke_all=
                # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\llm_config.py
                # C:\Users\usef\work\sidoarjo\schnell\app\promptutils.py
                from schnell.app.llmutils.langchainutils.llm_config import invoke_all
                nilai = text.removeprefix("invoke_all=").strip()
                if nilai and nilai in invoke_all.keys():
                    selected = [e.strip() for e in nilai.split(',')]
                    if selected:
                        for key in invoke_all:
                            if key in selected:
                                invoke_all[key] = 1
                            else:
                                invoke_all[key] = 0
                        self.refresh_completer()
                else:
                    if not nilai:  # user kasih kosong
                        from schnell.app.promptutils import radio, check  # radio(judul, isi, pilihan=['a','b','c'])
                        semua_keys = list(invoke_all.keys())
                        semua_keys_selected = [item for item in invoke_all.keys() if invoke_all[item]==1]
                        # print('semua_keys:', semua_keys, 'semua_keys_selected:', semua_keys_selected)
                        nilai = check("judul", "isi", semua_keys, semua_keys_selected)
                        # set nilai 1/0 utk invoke_all
                        print_json(nilai)

                        for key in invoke_all:
                            if key in nilai:
                                invoke_all[key] = 1
                            else:
                                invoke_all[key] = 0

                        self.refresh_completer()

        elif text.startswith("context:"):
            # global_context
            text = text.removeprefix("context:").strip()
            print("context:", text)

            if not text:
                print_json(global_context)

            elif text.startswith("current_tab="):  # context:current_tab=
                # kita gunakan ss utk space 2, ssss utk space 4, t utk tab
                nilai = text.removeprefix("current_tab=").strip()
                if nilai:
                    global_context["current_tab"] = nilai.replace("s", " ").replace(
                        "t", "\t"
                    )
                    print_json(global_context)

            elif text == "print=cmd":
                indah4(str(command_prompt_data), warna="blue")
            elif text == "print=cmdext":
                indah4(str(command_prompt_data_extension), warna="magenta")
            elif text == "print=cmdall":
                indah4(str(command_prompt_data), warna="blue")
                indah4(str(command_prompt_data_extension), warna="magenta")

            elif "=" in text:
                kunci, nilai = [text.split("=")]
                if kunci in global_context:
                    if nilai in ["True", "False"]:
                        nilai = True if nilai == "True" else False
                    elif nilai in ["None"]:
                        nilai = None
                    elif nilai.isdigit():
                        nilai = int(nilai)
                    global_context[kunci] = nilai
                    print_json(global_context)

        elif text.startswith("test_warna="):
            args = text.removeprefix("test_warna=").strip()
            if "," in args:
                args = [item.strip() for item in args.split(",")]
            else:
                args = [args]
            test_warna(*args)

        elif text.startswith("!"):  # exec shell command, ! harus di awal kata, berbeda dg ### yang bisa ditengah
            text = text.removeprefix("!").strip()
            os.system(text)

        elif text.startswith("fmus:"):
            if text.startswith("fmus:content"):
                text = text.removeprefix("fmus:content").strip()
                args = ""
                if text:
                    args = " " + text
                os.system(rf"python C:\work\ciledug\ciledug\fmuscontent\main.py{args}")
            elif text.startswith("fmus:dirs"):
                text = text.removeprefix("fmus:dirs").strip()
                args = ""
                if text:
                    args = " " + text
                os.system(rf"python C:\work\ciledug\ciledug\fmusdirs\main.py{args}")
            elif text.startswith("fmus:file"):
                text = text.removeprefix("fmus:file").strip()
                args = ""
                if text:
                    args = " " + text
                os.system(rf"python C:\work\ciledug\ciledug\fmusfile\main.py{args}")
            elif text.startswith("fmus:installer"):
                text = text.removeprefix("fmus:installer").strip()
                args = ""
                if text:
                    args = " " + text
                os.system(
                    rf"python C:\work\ciledug\ciledug\fmusinstaller\main.py{args}"
                )
            elif text.startswith("fmus:ketik"):
                text = text.removeprefix("fmus:ketik").strip()
                args = ""
                if text:
                    args = " " + text
                os.system(rf"python C:\work\ciledug\ciledug\fmusketik\main.py{args}")
            elif text.startswith("fmus:url"):
                text = text.removeprefix("fmus:url").strip()
                args = ""
                if text:
                    args = " " + text
                os.system(rf"python C:\work\ciledug\ciledug\fmusurl\main.py{args}")
            elif text.startswith("fmus:redis"):
                text = text.removeprefix("fmus:redis").strip()
                os.system(r"python C:\work\ciledug\ciledug\redis\main.py")
            elif text.startswith("fmus:fastapi:"):
                text = text.removeprefix("fmus:fastapi:").strip()
                from server.server_fastapi import control_fastapi, list_connected_clients, send_message_to_client
                if text == "status":
                    control_fastapi("status")
                elif text == "stop":
                    control_fastapi("stop")
                # elif text == "stop_win":
                #     control_fastapi("stop_win")
                # elif text == "stop_force":
                #     control_fastapi("stop_force")
                # elif text == "stop_kill":
                #     control_fastapi("stop_kill")
                elif text == "start":
                    control_fastapi("start")
                elif text == "reload":
                    control_fastapi("reload")
                elif text == "clients":
                    clients = list_connected_clients()
                    print_json(clients)
            elif text.startswith("fmus:flask:"):
                text = text.removeprefix("fmus:flask:").strip()
                from server.server_flask import control_server
                res = control_server(text)
                print(res)
                # if text == "status":
                #     res = control_server("status")
                #     print(res)
                # elif text == "stop":
                #     res = control_server("stop")
                #     print(res)
                # elif text == "start":
                #     print("Starting Flask server...")
                #     res = control_server("start")
                #     print(res)
                # elif text == "reload":
                #     res = control_server("reload")
                #     print(res)
                # elif text == "stop_win":
                #     control_fastapi("stop_win")
                # elif text == "stop_force":
                #     control_fastapi("stop_force")
                # elif text == "stop_kill":
                #     control_fastapi("stop_kill")
                # elif text == "clients":
                #     clients = list_connected_clients
                #     print_json(clients)

        elif text == "editfile":
            run_vscode(__file__)

        elif text == "editfolder":
            run_vscode(ayah(__file__, 1))

        elif text == "editconfig":
            run_vscode(config_file)

        elif text == "edithelp":
            run_vscode(help_file)

        elif text in ["pt", "ip"]:
            if text == "pt":
                from schnell.vendor.ptpython.repl import embed

                embed(globals(), locals())
            else:
                from schnell.vendor.ptpython.ipython import embed

                embed()

        elif text == "R" or text.startswith("R:"):  # skrg mending ctrl+k
            # list_listening_ports
            # R:reload=...
            # R:ports
            # update_subfolders()
            # mycompleter = FuzzyCompleter(NestedCompleter.from_nested_dict(original_dict_to_json))
            # self.session = self.create_prompt_session(mycompleter, self.previous_words)
            if text == "R":
                self.refresh_completer()
            elif text == "R:ports":
                list_listening_ports()
            elif text == "R:cpu":
                cpu_percent = get_cpu_usage_percent()
                indah4(f"{cpu_percent}%", warna="blue")
            elif text.startswith("R:dirs="):
                query = text.removeprefix("R:dirs=").strip()
                if isdir(query):
                    subfolders = get_all_folders(query)
                    print_list_warna(subfolders, start=1)
            elif text.startswith("R:mem"):
                # R:mem, R:mem=, R:mem=10
                query = text.removeprefix("R:mem").strip()
                if not query:
                    list_processes_by_memory()
                elif query == "=":
                    list_processes_with_path(0)
                elif query.removeprefix("=").strip().isdigit():
                    jumlah = int(query.removeprefix("=").strip())
                    list_processes_with_path(jumlah)

        elif text.startswith("g/"):
            bariskalimat = text.removeprefix("g/").strip()
            cari_google(bariskalimat)

        elif text.startswith("y/"):
            bariskalimat = text.removeprefix("y/").strip()
            cari_youtube(bariskalimat)

        elif text == "cap":  # capcay/scratchpad
            from schnell.app.richtextual.scratchpad import main

            main()

        elif text == "bahasa" or text.startswith("bahasa="):
            from fpbahasa import create_selection_of_bahasa

            request_bahasa = text.removeprefix("bahasa")
            completer = None
            if not request_bahasa:
                completer, logged_dict, bahasa = create_selection_of_bahasa()
            elif request_bahasa.startswith("="):
                request_bahasa = request_bahasa.removeprefix("=").strip()
                if request_bahasa in programming_languages:
                    completer, logged_dict, bahasa = create_selection_of_bahasa(
                        request_bahasa
                    )
            # di sini, kunci utk dapatkan filepath dan barisentry ada di logged_dict
            config_app["temporary_prompt_logged_dict"] = logged_dict
            if completer:

                def handler(kunci):  # jika user choose (select+enter) kunci
                    # loggeddict => [key-wrapper] = { filepath: ..., barisentry: ... }
                    nilai = logged_dict.get(kunci, None)
                    if nilai:
                        filepath = nilai.get("filepath")
                        barisentry = nilai.get("barisentry")
                        # print(f"kita oprek: {filepath}={barisentry}")
                        # content = fmusfile_entry(filepath, barisentry)
                        content, lineno = define_filepath_barisentry_with_lineno(
                            filepath, barisentry
                        )
                        repl_service.last_file = filepath
                        repl_service.last_lineno = lineno
                        print_source_code_copy(content)
                        # mungkin perlu extra: publish redis

                self.loop_temporary_prompt_for_bahasa(
                    FuzzyCompleter(completer), handler, kanan=bahasa
                )
                self.refresh_completer()

        elif text.startswith("playfmus ") or text.startswith(
            "playfmus="
        ):  # playfmus folder|filter atau playfmus=folder|filter
            # playfmus folder|filter
            # playfmus folder|filter*
            # filter => find_files_with_extensions
            from fpplayfmus import play_fmus_files

            if text.startswith("playfmus="):
                basefolder = text.removeprefix("playfmus=").strip()
            else:
                basefolder = text.removeprefix("playfmus ").strip()
            if not basefolder:
                completer, logged_dict, filepilihan = play_fmus_files()
            else:
                select_all = False
                if basefolder.endswith("*"):  # select all fmus/mk files
                    basefolder = basefolder.removesuffix("*").strip()
                    select_all = True
                filter_name = None
                if "|" in basefolder:
                    basefolder, filter_name = [
                        item.strip() for item in basefolder.split("|")
                    ]
                # print(f'basefolder={basefolder}, filter_name={filter_name}')
                completer, logged_dict, filepilihan = play_fmus_files(
                    basefolder, filter_name, select_all=select_all
                )

            # agar bisa rprompt, text_area, dst.
            config_app["temporary_prompt_logged_dict"] = logged_dict

            if completer:

                def playfmus_handler(kunci):
                    # bisa diawali # utk edit
                    to_edit = False
                    if kunci.startswith('#'):
                        to_edit = True
                        kunci = kunci.removeprefix('#').strip()
                    nilai = logged_dict.get(kunci, None)
                    if nilai:
                        filepath = nilai.get("filepath")
                        barisentry = nilai.get("barisentry")

                        if to_edit:
                            vscode_edit_file(filepath)
                            return

                        # content = fmusfile_entry(filepath, barisentry)
                        content, lineno = define_filepath_barisentry_with_lineno(
                            filepath, barisentry
                        )
                        repl_service.last_file = filepath
                        repl_service.last_lineno = lineno
                        if barisentry.endswith(
                            "!"
                        ):  # bisa exec command jk barisentry nya berakhir !
                            content = inputify(content)
                            for baris in content.splitlines():
                                os.system(baris)
                        elif barisentry.endswith("/fmus"):
                            # indah3(content, warna='yellow')
                            print_source_code_copy(content)
                            jalankan = confirm(
                                f"Jalankan kode di atas di {os.getcwd()}?"
                            )
                            if jalankan:
                                # execute content
                                if config_app["thread"]:
                                    run_fmus_for_content_in_thread(
                                        content, dirpath=os.getcwd(), filepath=filepath
                                    )
                                else:
                                    run_fmus_for_content(
                                        content, dirpath=os.getcwd(), filepath=filepath
                                    )
                        else:
                            print_source_code_copy(content)
                        # mungkin perlu extra: publish redis

                self.loop_temporary_prompt_for_bahasa(
                    FuzzyCompleter(completer),
                    playfmus_handler,
                    kanan=(
                        f"Play {len(filepilihan)} fmus"
                        if len(filepilihan) > 1
                        else filepilihan[0]
                    ),
                )
                self.refresh_completer()
            else:
                indah4(
                    f'No files in {basefolder}{f" for query={filter_name}" if filter_name else ""}.',
                    warna="red",
                )

        elif text.startswith("gen ") or text.startswith("gen="):
            try:
                if text.startswith("gen="):
                    fmusfilepath = text.removeprefix("gen=").strip()
                else:
                    fmusfilepath = text.removeprefix("gen ").strip()
                config_app["temporary_prompt_current_fmusfile"] = fmusfilepath
                # pastikan textarea keliatan jk blm aktif
                if not config_app["show_textarea"]:
                    config_app["show_textarea"] = True
                    config_app["text_area_height"] = 10  # tentu pengen yg bisa lihat dg enak
                    self.refresh_completer()
                handle_generator(
                    text, self.temporary_prompt
                )  # tambah bisa ganti prompt
                self.refresh_completer()
                # jk control c suka gak balik prompt-nya
            except Exception as gagal:
                print(traceback.format_exc())
                indah4(
                    f"""exception waktu handle generator "gen " atau "gen="\n[{gagal}]\nbalikkan tmp-prompt""",
                    warna="red",
                )
                self.refresh_completer()
            return

        elif text.startswith("genfolder ") or text.startswith(
            "genfolder="
        ):  # coba play folder terutama git repo
            from fmuslib import generate_fmus_for_folder

            if text.startswith("genfolder="):
                query = text.removeprefix("genfolder=").strip()
            else:
                query = text.removeprefix("genfolder ").strip()
            # original_cwd = os.getcwd()  # krn exec fmus jd ganti lokasi
            git_pull = False
            if query.startswith("*"):
                query = query.removeprefix("*").strip()
                git_pull = True
            fmusfile = None
            if (
                not query
            ):  # default gen-folder (mungkin folder di bawah sudah tidak ada)
                default_repo = r"C:\work\ciledug\openai-cookbook"
                fmusfile = generate_fmus_for_folder(default_repo, git_pull=git_pull)
            else:
                query = os.path.abspath(
                    query
                )  # paksakan absolute, krn kita sudah ganti folder
                if isdir(query):
                    fmusfile = generate_fmus_for_folder(query, git_pull=git_pull)
            indah4(f"{text} => fmusfile={fmusfile}.", warna="blue")
            if fmusfile:
                config_app["temporary_prompt_current_fmusfile"] = fmusfile
                handle_generator("gen " + fmusfile, self.temporary_prompt)
            self.refresh_completer()

        elif text.startswith("cd "):
            lokasi = text.removeprefix("cd ").strip()
            # change_dir(lokasi)
            # self.refresh_completer()
            if is_only_dots(lokasi):  # cd ., cd .., cd ..., cd ....
                lokasi = navigate_back_multiple(os.getcwd(), text)
                print("navigate_back_multiple", lokasi)
            elif text.startswith("cd .."):  # cd ..repository, cd...main
                lokasi = navigate_back(os.getcwd(), text)
                print("navigate_back", lokasi)
            self.change_dir_and_refresh_completer(lokasi)
            os.system(config_app["ls_style"])

        elif text == "cd":
            self.path_completer()

        elif text.startswith("~"):  # change dir atau cari file/dir di curdir
            query = text.removeprefix("~").strip()
            if not query:  # sama dg #, print list of preset  dirs
                indah4(
                    """
                ~           = #
                ~9          = cd to ...
                ~dir        = cd <dir>
                ~@<digit>   = copy digit to clipboard
                ~reload=data.json
                ~other      = fzf <other>
                """,
                    warna="green",
                )
                print_list_warna(original_cd_list, start=1)  # setara dg f8
            elif query.isdigit():  # change ke preset dir
                lokasi = original_cd_dict[int(query)]
                indah4(f"{query} => {lokasi}", warna="magenta")
                self.change_dir_and_refresh_completer(lokasi)
                os.system(config_app["ls_style"])
            elif query.startswith("@"):  # ~@, ~@4, copy curdir atau preset dir
                query = query.removeprefix("@").strip()
                if not query:  # ~@ adlh copy curdir
                    lokasi = os.getcwd()
                    indah4(f"{lokasi} copied...", warna="magenta")
                    trycopy(lokasi)
                elif query.isdigit():
                    lokasi = original_cd_dict[int(query)]
                    indah4(f"{lokasi} copied...", warna="magenta")
                    trycopy(lokasi)
            elif os.path.isdir(query):  # change to requested dir
                # change_dir(lokasi)
                # self.refresh_completer()
                self.change_dir_and_refresh_completer(query)
                # os.system('dir')
                os.system(config_app["ls_style"])
            elif query.startswith("reload="):  # ~reload=data.json, ~reload=ai.json
                filename = query.removeprefix("reload=").strip()
                if filename:
                    update_file_json_by_filename(filename)
                    self.refresh_completer()
            else:
                # os.system(f'dir *{query}*')
                os.system(f"{fzf} {query}")

        elif text.startswith("#"):  # editor code
            text = text.removeprefix("#").strip()
            # open_folder = '.'
            if not text:
                print_list_warna(original_cd_list, start=1)  # setara dg f8
            elif text in ["l", "list", "ls", "dir"]:
                print_list_warna(original_cd_list, start=1)  # setara dg f8
            elif text.isdigit():
                open_folder = original_cd_dict[int(text)]
                run_vscode(open_folder)
            elif text.startswith(
                ":"
            ):  # tambah func: #:data.json, #:z.json, #:csharp-asp.json
                filename = text.removeprefix(":").strip()
                if filename in ["data.json"]:
                    file_json = joiner(fmusperintah_dir, filename)
                    run_vscode(file_json)
                else:
                    file_json = joiner(json_configs_dir, filename)
                    if isfile(file_json):
                        run_vscode(file_json)
            elif os.path.isdir(text):
                run_vscode(text)
            elif '.fmus=' in text or '.mk=' in text:
                # kedepan hrs bisa edit pada entry yg diminta
                filepath = [e.strip() for e in text.split('=')][0]
                run_vscode(filepath)
            else:  # file sudah atau atau belum, bisa dibuka oleh code
                run_vscode(text)

        elif text.startswith("cat "):
            request = text.removeprefix("cat ").strip()
            if request:
                if isdir(request):  # bisa lihat direktori
                    os.system(f"ls -a --color=always --format=across -c -l {request}")
                else:
                    print_source_code_file_with_markdown(request)

        elif text.startswith(">"):  # actor handler
            request = text.removeprefix(">").strip()
            from schnell.gui.system.searcher.widgets.actorhandler import actor_handler

            content = actor_handler(request, debug=True)
            indah3(content, warna="cyan")

        elif text.startswith("rat "):  # rat file, rat file/query => print highlight word in file
            request = text.removeprefix("rat ").strip()
            # indah4(f"start ratting [{request}].", warna='green')
            if request:
                if "/" in request:  # rat filename/kata_utk_dihighlight
                    filepath, query = request.rsplit("/", 1)
                    # indah4(f"/ in ratting [{request}] => {filepath}, {query}.", warna='yellow')
                    if filepath and query:
                        print_highlight_query_file(filepath, query)
                    else:
                        indah4(f"gagal ratting {request}.", warna="red")
                else:
                    print_source_code_file_with_markdown(request)

        elif text.startswith("pad"):
            request = text.removeprefix("pad").strip()
            if request:
                if request == ".":
                    request = os.getcwd()
                pemanggilan = fmuspad + " --root " + request
            else:
                pemanggilan = fmuspad + " --root " + os.getcwd()
            # subprocess.Popen([pemanggilan])
            os.system(pemanggilan)

        elif text.startswith("pg"):  # pager
            request = text.removeprefix("pg").strip()
            pemanggilan = f"{pager} {request}"
            # indah4(pemanggilan, warna='blue')
            os.system(pemanggilan)

        elif text.startswith("p "):
            request = text.removeprefix("p ").strip()
            if request:
                os.system(f"python {request}")

        elif text.startswith("mn"):
            command_to_invoke = inputify(text.replace("mn", micronaut, 1))
            os.system(command_to_invoke)

        elif text.startswith("fmusread"):
            command_to_invoke = inputify(text.replace("fmusread", fmusreader, 1))
            os.system(command_to_invoke)

        elif text.startswith("fmusmk"):
            command_to_invoke = inputify(text.replace("fmusmk", fmusmk, 1))
            os.system(command_to_invoke)

        elif "sort -" in text:
            command_to_invoke = inputify(text.replace("sort -", f"{unixsort} -r", 1))
            os.system(command_to_invoke)

        elif text.startswith("bunx"):
            command_to_invoke = inputify(text.replace("bunx", bunx, 1))
            os.system(command_to_invoke)

        elif text.startswith("b ") or text in ["b", "b@"] or text.startswith("b@"):
            # bisa juga b@x utk tsx atau jsx
            text = inputify(text)
            if text == "b":
                os.system(bunny)
            elif text == "b@":
                # ambil dari clipboard
                filename = copy_clipboard_to_file()
                os.system(bunny + f" {filename}")
            elif text.startswith("b@"):
                # kita tambah kemampuan specifying filename
                # misalnya b@Component.tsx
                suffix = text.removeprefix("b@").strip()
                if "." in suffix:  # specify namafile
                    filename = copy_clipboard_to_file(force_filename=suffix)
                else:
                    filename = copy_clipboard_to_file(suffix)
                print(f"filename={filename}, suffix={suffix}")
                os.system(bunny + f" {filename}")
            else:
                file_or_folder = text.removeprefix("b ").strip()
                if file_or_folder == "@":  # b @ sama dengan b@
                    file_or_folder = copy_clipboard_to_file()
                command_to_invoke = f"{bunny} {file_or_folder}"
                # indah4(f"exec: {command_to_invoke}", warna='cyan')
                os.system(command_to_invoke)

        elif text.startswith("v ") or text == "v":  # vim
            if text == "v":
                os.system(vim)
            else:
                file_or_folder = text.removeprefix("v ").strip()
                command_to_invoke = f"{vim} {file_or_folder}"
                # indah4(f"exec: {command_to_invoke}", warna='cyan')
                os.system(command_to_invoke)

        elif text.startswith("elia"):  # elia
            # python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\tests\elia.py
            # from schnell.app.llmutils.elia_chat.__main__ import cli
            # cli()
            process = subprocess.Popen(r"python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\tests\elia.py".split())
            process.wait()

        elif text.startswith("render"):
            command_to_invoke = text.replace("render", render)
            os.system(command_to_invoke)

        elif text.startswith("|"):
            process_perintah(text, DictToObject({"workdir": os.getcwd()}))  # /$|

        elif text.startswith("="):  # size of folders
            process_perintah(
                "sz" + text, DictToObject({"workdir": os.getcwd()})
            )  # /$sz=

        elif text.startswith("mkdir ") or text.startswith("rm"):
            # baca direktori yang terbaru (jika terbuat/terhapus), rmdir, rm -rf, mkdir
            os.system(text)
            self.refresh_completer()

        elif text.startswith("`"):  # handle files
            namafile = text.removeprefix("`").strip()
            is_colon = is_star = False
            if namafile.endswith(":"):
                namafile = namafile.removesuffix(":").strip()
                is_colon = True
            elif namafile.endswith("*"):
                namafile = namafile.removesuffix("*").strip()
                is_star = True
            file_lengkap = joiner(os.getcwd(), namafile)
            # jk python: execute
            if any(
                [
                    item
                    for item in [
                        ".md",
                        ".txt",
                        ".sql",
                        ".java",
                        ".cs",
                        ".cpp",
                        ".js",
                        ".ts",
                    ]
                    if namafile.endswith(item)
                ]
            ):
                if is_star:
                    run_vscode(namafile)  # edit
                else:
                    # os.system(f'mark {namafile}')
                    # print('printing:', namafile)
                    print_source_code_file(namafile)
            # jika py
            # `:namafile.py => exec, `namafile.py => read
            elif namafile.endswith(".py"):
                if is_colon:  # file.py: 	exec
                    os.system(f"python {namafile}")
                elif is_star:  # file.py* 	edit
                    run_vscode(namafile)
                else:
                    # os.system(f'cat {namafile}')  # cari commands yg dukung lexer python
                    print_source_code_file(namafile)
            elif namafile.endswith(".json"):
                os.system(f'jq --color-output "." {namafile}')
            # jika image
            elif any(
                [
                    item
                    for item in [
                        ".jpg",
                        ".png",
                        ".gif",
                        ".bmp",
                        ".jpeg",
                        ".mp4",
                        ".wmv",
                        ".pdf",
                    ]
                    if namafile.endswith(item)
                ]
            ):
                os.system(namafile)
            elif is_file_not_binary(file_lengkap):
                # os.system(f'bat {namafile}')  # bat = rust version of cat with colors
                print_source_code_file(file_lengkap)
            else:
                # indah4(f'not processing {namafile}', warna='yellow')
                print_source_code_file(file_lengkap)

        elif ".fmus=" in text or ".mk=" in text:  # bisa print barisentry langsung
            filepath, barisentry = [item.strip() for item in text.split("=", 1)]
            content = fmusfile_entry(filepath, barisentry)
            # content = define_filepath_equal(text)
            # print_source_code_copy(content)  # matikan sementara krn layar jadi kacau sejak pick/survey/pytermtk
            print(content)
            # jk myfile.fmus=runme/fmus maka tanya jk mau jalankan
            if barisentry.endswith('/fmus'):
                jalankan = confirm(f"Jalankan kode di atas di {os.getcwd()}?")
                if jalankan:
                    if config_app["thread"]:
                        run_fmus_for_content_in_thread(
                            content, dirpath=os.getcwd(), filepath=filepath
                        )
                    else:
                        run_fmus_for_content(content, dirpath=os.getcwd(), filepath=filepath)

        elif "=>" in text:
            contentdata, filename = [e.strip() for e in text.split("=>")]
            # print(contentdata, '===', filename)
            if contentdata == "@" or not contentdata:
                contentdata = trypaste()
            # cek juga jk isfile, jk fmus=barisentry, dst
            elif ".fmus=" in contentdata or ".mk=" in contentdata:
                contentdata = define_filepath_equal(contentdata)
            elif isfile(contentdata):
                contentdata = file_content(contentdata)
            contentdata = (
                sanitize(contentdata)
                .replace("\\n", "\n")
                .replace("\\t", "\t")
                .replace("\r", "")
            )
            # print('ready contentdata:', contentdata)
            ###############################################################
            if ":" in filename:  # @=>capcay.txt:0, @=>capcay.txt:~, @=>capcay.txt:42
                filename, linespec = [e.strip() for e in filename.split(":", 1)]
                # jika filename sudah ada
                if isfile(filename):
                    trycopy(file_content(filename))  # biar bisa dimonitor
                    if linespec == "0":  # filename:0
                        file_prepend(filename, contentdata)
                    elif linespec == "~":  # filename:~
                        file_append(filename, contentdata)
                    elif linespec.isdigit():  # filename:42
                        line_numbers = [int(linespec)]
                        insert_at_lines(
                            filename, contentdata, line_numbers, line_index_start=1
                        )
                else:
                    file_write(filename, contentdata)
            else:  # filename
                file_write(filename, contentdata)

        else:
            if text.startswith('ojol/'):
                from frutils import fr_process_file_key_value
                fr_process_file_key_value(text.removeprefix('ojol/').strip())
                return
            if text:
                text = inputify(text)
                # indah4(f'fmusperintah ==> {text}', warna='yellow')
                # run_fmus_for_content_in_thread(content, dirpath=tempdir(), filepath=None)
                if config_app["thread"]:
                    # thread = run_fmus_for_content_in_thread(text, dirpath=os.getcwd())
                    # print(thread)
                    os.system(text)
                else:
                    # run_fmus_for_content(text, dirpath=os.getcwd())
                    os.system(text)


# # 15-des-23 matikan .env krn jarang pake ULIBPY_*
# # load .env dulu utk hasilkan ULIBPY_ROOTDIR agar bisa bongkar
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)

repl = Repl()


def loop_temporary_repl_prompt(daftar_isi, callback):
    daftar_isi += ["x", "exit"]
    jawab = None
    while jawab not in ["x", "exit"]:
        jawab = repl.temporary_prompt(
            "✈️ ", choices=daftar_isi, meta_dict={k: None for k in daftar_isi}
        )
        if jawab and jawab in daftar_isi:
            callback(jawab)


def edit_entry(filepath, lineno):
    if not lineno or lineno < 0:
        lineno = 0
    cmd = f'vscode --goto "{filepath}:{lineno}:1"{background}'
    os.system(cmd)


# dir_stack_completer = FuzzyCompleter(dir_stack)
def dir_stack_validator(text):
    return text in dir_stack


from schnell.app.fileutils import file_write_timestamped
# print('10')
# file_write_timestamped(filepath, text, write_mode='w', formatter='%Y%m%d_%H%M%S')
from fpopenai import (
    get_response as oai_response,
    get_stream as oai_stream,
    create_client,
)
# print('11')
from fpgemini import get_response, get_stream
# print('12')
from fpgemini import (
    start_chat,
    start_chat_stream,
    send_chat,
    send_chat_stream,
    gemini_header,
)
# print('13')
from fpcohere import generate_cohere_response
# print('14')
from fpgroq import generate_groq_response
# print('15')


def print_stream(msg):  # co, k (gen text)
    config_app["last_gemini_file"] = joinhere(__file__, "data/gemini", "stream.txt")
    file_write_timestamped(
        config_app["last_gemini_file"], msg, write_mode="a", formatter="%Y%m%d-%H"
    )
    indah4(msg, warna="green", layar="yellow")


def print_chat_stream(msg):  # co, m (chat)
    config_app["last_gemini_file"] = joinhere(
        __file__, "data/gemini", "chat-stream.txt"
    )
    file_write_timestamped(
        config_app["last_gemini_file"], msg, write_mode="a", formatter="%Y%m%d-%H"
    )
    indah4(msg, warna="green", layar="yellow")


# event.app.current_buffer.text='📢'
# pyautogui.hotkey('win', 'h')


def print_openai_stream(msg):  # co, b
    config_app["last_openai_file"] = joinhere(
        __file__, "data/openai", "chat-stream.txt"
    )
    file_write_timestamped(
        config_app["last_openai_file"], msg, write_mode="a", formatter="%Y%m%d-%H"
    )
    indah4(msg, warna="green", layar="yellow")


# https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html
# jangan pake c@ utk c-space, cm, ch, ci
# print('20')
# ###################### shift-del
from keybinders.hotkey import bind_key_hotkey
# print('21')
bind_key_hotkey(bindings, repl)
######################


# ###################### ctrl+a, dont use, digunakan utk ke start of line
# print('22')
###################### ctrl+b
from keybinders.ctrl_b import bind_key_b
bind_key_b(bindings, repl)
# ###################### ctrl+e, dont use, utk go to end of line
# print('23')
###################### ctrl+f
from keybinders.ctrl_f import bind_key_f
bind_key_f(bindings, repl)
# print('24')
###################### ctrl+g
from keybinders.ctrl_g import bind_key_g
bind_key_g(bindings)
# ###################### ctrl+h (dont use, ini adlh backspace)
# ###################### ctrl+i (sebelumnya setara dg tab, dont use, emang ini adlh tab...)
# print('25')
from keybinders.ctrl_k import bind_key_k
bind_key_k(bindings)
# ###################### ctrl+m (ini bikin enter jadi 2x, dont use, ini adlh enter)
###################### ctrl+n
# print('26')
from keybinders.ctrl_n import bind_key_n
bind_key_n(bindings)
# print('27')

###################### ctrl+o
@bindings.add("c-o", "1")  # buat client dengan openai key dari config
def _(event):
    create_client(config_app["openai_key"])
    indah4("OpenAI set with new key")
    # terima_prompt(event)


@bindings.add("c-o", "a")  # openai completion
def _(event):
    pertanyaan = event.app.current_buffer.text.strip()
    if pertanyaan:
        jawaban = oai_response(
            pertanyaan,
            model=config_app["openai_model"],
            temperature=config_app["openai_temperature"],
        )
        print("\n" * 3)
        print_source_code_copy(jawaban)
        terima_prompt(event)


@bindings.add("c-o", "b")  # openai completion stream
def _(event):
    pertanyaan = event.app.current_buffer.text.strip()
    if pertanyaan:
        config_app["last_openai_file"] = joinhere(
            __file__, "data/openai", "chat-stream.txt"
        )
        file_write_timestamped(
            config_app["last_openai_file"],
            gemini_header(pertanyaan),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        jawaban = oai_stream(
            pertanyaan,
            callback=print_openai_stream,
            model=config_app["openai_model"],
            temperature=config_app["openai_temperature"],
        )
        # print_source_code_copy(jawaban)
        terima_prompt(event)


# jadi kita ngomong dulu, dan tulisan masuk buffer
# abis itu co-j utk proses gemini
@bindings.add("c-o", "j")  # gemini
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        marktext = get_response(bariskalimat)
        config_app["last_gemini_file"] = joinhere(__file__, "data/gemini", "prompt.txt")
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(marktext),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        print_source_code_copy(marktext)
        terima_prompt(event)


@bindings.add("c-o", "k")  # gemini stream
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        config_app["last_gemini_file"] = joinhere(__file__, "data/gemini", "stream.txt")
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(bariskalimat),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        get_stream(bariskalimat, print_stream)
        # print_source_code_copy(marktext)
        terima_prompt(event)


@bindings.add("c-o", "c-l")  # start chat non-stream, utk mulai chat baru, co-cl
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        config_app["last_gemini_file"] = joinhere(
            __file__, "data/gemini", "chat-prompt.txt"
        )
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(bariskalimat),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        marktext = start_chat(bariskalimat)
        file_write_timestamped(
            config_app["last_gemini_file"],
            marktext,
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        print_source_code_copy(marktext)
        terima_prompt(event)


@bindings.add("c-o", "l")  # send chat non-stream, co-l
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        config_app["last_gemini_file"] = joinhere(
            __file__, "data/gemini", "chat-prompt.txt"
        )
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(bariskalimat),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        marktext = send_chat(bariskalimat)
        file_write_timestamped(
            config_app["last_gemini_file"],
            marktext,
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        print_source_code_copy(marktext)
        terima_prompt(event)


###################################### coba ctrl+o, shift+l
# ffmpeg -i myvideo.mp4 --cut-from-seconds 100 --cut-until-seconds 200 -o outputvideo_seconds100-200.mp4
# ffmpeg -i myvideo.mp4 -ss 100 -t 100 -c copy outputvideo_seconds100-200.mp4
template_prompt = """Convert the pseudo code for command line command that I give below into its real, correct version.
Respond only with the correct command which I can run directly verbatim, without any explanation.

__BARISKALIMAT__
"""


######################################
@bindings.add("c-o", "L")  # coba dulu ctrl+o, shift+l
def _(event):
    # indah4('control o shift l')
    # coba ffmpeg
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        bariskalimat = template_prompt.replace("__BARISKALIMAT__", bariskalimat)
        config_app["last_gemini_file"] = joinhere(
            __file__, "data/gemini", "chat-prompt-template.txt"
        )
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(bariskalimat),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        marktext = send_chat(bariskalimat)
        file_write_timestamped(
            config_app["last_gemini_file"],
            marktext,
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        indah3(marktext, warna="blue", layar="yellow")
        terima_prompt(event)


###################################### coba ctrl+o, shift+l
@bindings.add("c-o", "c-m")  # start chat stream, utk mulai chat stream baru, co-cm
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        config_app["last_gemini_file"] = joinhere(
            __file__, "data/gemini", "chat-stream.txt"
        )
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(bariskalimat),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        start_chat_stream(bariskalimat, print_chat_stream)
        terima_prompt(event)


######################################
@bindings.add("c-o", "m")  # send chat stream, co-m
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        config_app["last_gemini_file"] = joinhere(
            __file__, "data/gemini", "chat-stream.txt"
        )
        file_write_timestamped(
            config_app["last_gemini_file"],
            gemini_header(bariskalimat),
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        send_chat_stream(bariskalimat, print_chat_stream)
        terima_prompt(event)



###################################### groq
@bindings.add("c-o", "q")  # send text generation
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        if bariskalimat == "@":
            print("Masukkan prompt untuk query groq ke clipboard", end='')
            input(" ")
            bariskalimat = trypaste().strip()
            if not bariskalimat:
                print("No data")
                return
        prompt_response = generate_groq_response(prompt=bariskalimat)
        config_app["last_groq_file"] = joinhere(__file__, "data/groq", "prompt.txt")
        file_write_timestamped(
            config_app["last_groq_file"],
            gemini_header(bariskalimat) + prompt_response,
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        print("\n" * 3)
        print_source_code_copy(prompt_response)
        terima_prompt(event)


###################################### cohere
@bindings.add("c-o", "r")  # send text generation
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    if bariskalimat:
        if bariskalimat == "@":
            print("Masukkan prompt untuk query cohere ke clipboard", end='')
            input(" ")
            bariskalimat = trypaste().strip()
            if not bariskalimat:
                print("No data")
                return
        prompt_response = generate_cohere_response(prompt=bariskalimat)
        config_app["last_cohere_file"] = joinhere(__file__, "data/cohere", "prompt.txt")
        file_write_timestamped(
            config_app["last_cohere_file"],
            gemini_header(bariskalimat) + prompt_response,
            write_mode="a",
            formatter="%Y%m%d-%H",
        )
        # file_write_timestamped(joinhere(__file__, 'data/cohere', 'generate.txt'),
        # 	gemini_header(prompt_response),
        # 	write_mode='a',
        # 	formatter='%Y%m%d-%H')
        # file_write_timestamped(joinhere(__file__, 'data/gemini', 'prompt.txt'), gemini_header(marktext), write_mode='a', formatter='%Y%m%d-%H')
        print("\n" * 3)
        print_source_code_copy(prompt_response)
        terima_prompt(event)

###################################### search
@bindings.add("c-o", "o")  # google search
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    cari_google(bariskalimat)
    terima_prompt(event)


@bindings.add("c-o", "y")  # youtube search
def _(event):
    bariskalimat = event.app.current_buffer.text.strip()
    cari_youtube(bariskalimat)
    terima_prompt(event)


# print('28')
###################### ctrl+q
from keybinders.ctrl_q import bind_key_q
bind_key_q(bindings)
###################### ctrl+r utk reverse search history
###################### ctrl+s utk search history
###################### ctrl+x
# print('29')
from keybinders.ctrl_x import bind_key_x
bind_key_x(bindings)
# print('30')
from keybinders.ctrl_z import bind_key_z
bind_key_z(bindings, repl)
# ###################### ctrl+z
# print('31')
# # @bindings.add("f1")
# # def _(event):
# # 	print_markdown_file(r'C:\work\ciledug\ciledug\fmusperintah\HELP.md')


@bindings.add("f7")  # utk run /ketik)
def _(event):
    # event.app.current_buffer.insert_text("penekanan f7 oleh user...")
    # alert(event.app.current_buffer.text)
    yang_diketik = event.app.current_buffer.text.strip()
    if yang_diketik:
        # event.app.current_buffer.text = ''
        repl.process("#ketik#" + yang_diketik)
        repl.our_history.append_string(yang_diketik)
        # event.app.current_buffer.text = ''
        terima_prompt(event)
    else:
        print("[ketik-fmus] nothing to type")


@bindings.add("f8")  # utk run fmus (keren bisa call fmuslang dari cli)
def _(event):
    yang_diketik = event.app.current_buffer.text.strip()
    if yang_diketik:
        # event.app.current_buffer.text = ''
        repl.process("#run#" + yang_diketik)
        repl.our_history.append_string(yang_diketik)
        # event.app.current_buffer.text = ''
        terima_prompt(event)
    else:
        print("[run-fmus] nothing to run")


@bindings.add("f9")  # utk chdir ke dir_stack => ganti jalankan fmusserver
def _(event):
    # ini ternyata blocking?
    # from schnell.gui.fmusserver import main
    # main()
    pemanggilan = "python C:\\Users\\usef\\work\\sidoarjo\\schnell\\gui\\fmusserver.py"
    repl.process("#ketik#" + pemanggilan)
    # repl.process(";r /ngetik)auto:ctrl,shift,t|" + pemanggilan) => gak jalan
    terima_prompt(event)


# from schnell.app.autoutils import alert
@bindings.add("f10")  # utk open url => 3000, any url
def _(event):
    # event.app.current_buffer.insert_text("penekanan f7 oleh user...")
    # alert(event.app.current_buffer.text)
    yang_diketik = event.app.current_buffer.text.strip()
    original_yang_diketik = yang_diketik
    if yang_diketik:
        if yang_diketik.isdigit():
            yang_diketik = "http://localhost:" + yang_diketik
        elif not yang_diketik.startswith("http"):
            yang_diketik = "http://" + yang_diketik

        repl.process("#url#" + yang_diketik)
        repl.our_history.append_string(original_yang_diketik)
        # event.app.current_buffer.text = ''
        terima_prompt(event)


@bindings.add("f10")
def _(event):
    # from keybinders.launcher import run_launcher
    # from keybinders.launcher_tk import run_launcher
    from keybinders.launcher import run_launcher2 as run_launcher
    run_launcher()


@bindings.add("f12")
def _(event):
    r"""
    assignment atribut ini ada di
    C:\Users\usef\work\sidoarjo\schnell\creator\repl_language\generator.py
    """
    if hasattr(repl_service, "last_file") and repl_service.last_file:
        filepath = repl_service.last_file
        # print_json(appconfig)
        if schnell_appconfig["last_expand_linktag"] is not None:
            # langsung consume
            filepath = schnell_appconfig["last_expand_linktag"]
            schnell_appconfig["last_expand_linktag"] = None
        if hasattr(repl_service, "last_lineno"):
            edit_entry(filepath, repl_service.last_lineno)
        else:
            os.system(f"vscode {filepath}{background}")
    elif repl.last_file and repl.last_lineno:
        edit_entry(repl.last_file, repl.last_lineno)
    elif repl.last_file:
        os.system(f"vscode {repl.last_file}")


def configure_app():
    global last_file_not_passed_arguments
    # print(sys.argv)
    parser = argparse.ArgumentParser(description="Configure App")

    # Add the positional argument for dirpath (optional, so nargs='?')
    parser.add_argument('dirpath', nargs='?', type=str, help='Set the working directory')

    parser.add_argument('-H', '--height', type=int, help='Set the height of the text area')
    parser.add_argument('-n', '--nomulti', action='store_true', help='No multicolumn dropdown menu')

    # parse
    args = parser.parse_args()
    # print(args)

    # positional proses duluan
    # Change working directory if dirpath is provided
    if args.dirpath:
        if os.path.isdir(args.dirpath):
            # os.chdir(args.dirpath)
            last_file_not_passed_arguments = False
        else:
            print(f"Error: The directory {args.dirpath} does not exist.")
            sys.exit(1)  # Exit if the directory is invalid
    # print(last_file_not_passed_arguments)
    # config_app = {
    #     "show_textarea_editor": True,
    #     "text_area_height": args.height if args.height else 100,  # Default height is 100
    # }
    if args.height:
        config_app["show_textarea"] = True
        config_app["text_area_height"] = args.height
        repl.refresh_completer()
    if args.nomulti:
        config_app["multicolumn"] = False
        repl.refresh_completer()


if __name__ == "__main__":
    configure_app()
    try:
        repl.run()
    except Exception as err:
        print("[fmusperintah:main]❌", err)
        print(traceback.format_exc())
