import ast
from schnell.app.treeutils import (
    get_all_parent_variables,
    item_workdir_has_input,
    replace_if_input_and_parent_is_dir,
)
from schnell.app.dirutils import isdir, isfile, dirname, normy, create_if_empty_dir
from schnell.app.printutils import indah4, indah0
from schnell.app.fileutils import file_write
from schnell.app.utils import env_int, env_expand
from schnell.app.stringutils import sanitize_chars
from schnell.app.fmusutils import get_input_generic_if_input_not_from_template
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_active
from schnell.app.fmusutils import replace_from_configuration_replacer
from .common import Common, input_keyword
from .write_file_with_variable_expansion import write_file_with_variable_expansion
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_active

# | "Q" "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 				-> query_active_llm_from_fmus_from_fmus
def query_active_llm_from_fmus(oper, item, root_tree, self_debug, self_run_configuration=None):
    print('query_active_llm_from_fmus')
    print(f"""
    oper = {oper}
    item = {item}
    root_tree
    self_debug
    self_run_configuration
    """)
    # operasi_value = str({fmus_file:baris_entry})
    dict_file_baris = oper.split("=", 1)[1] # str({fmus_file:baris_entry})
    dict_file_baris = ast.literal_eval(dict_file_baris)
    fmus_file = list(dict_file_baris.keys())[0]
    barisentry = dict_file_baris[fmus_file]
    fmus_file = replace_from_configuration_replacer(fmus_file, self_run_configuration['replacer'])


    if hasattr(root_tree, 'variables'):
        for varkunci, varnilai in root_tree.variables.items():
            item.workdir = normy(item.workdir.replace(varkunci, varnilai))
            fmus_file = normy(fmus_file.replace(varkunci, varnilai))
            barisentry = barisentry.replace(varkunci, varnilai) # misal masukkan __TABLENAME__ ke "dynamic" barisentry
    if not isfile(fmus_file):
        fmus_file = env_expand(fmus_file, bongkarin=True)

    entries = Common.list_grep(barisentry, fmus_file)


    if input_keyword in item.workdir \
        and hasattr(root_tree, 'input_keys') \
        and hasattr(root_tree, 'input_keys_index') \
        and hasattr(root_tree, 'variables'):
        terindeks = root_tree.input_keys[root_tree.input_keys_index]
        if terindeks in root_tree.variables:
            pengganti = root_tree.variables[terindeks]
        # if is_debugging:
        #     indah0(f"[ambil_entry_dari_file_template] Ganti item.workdir '{input_keyword}' menjadi '{pengganti}'.", warna='white', bold=True, newline=True)
        # item.workdir = item.workdir.replace(input_keyword, pengganti, 1)
        # ternyata __INPUT__ bisa banyak dalam item.workdir...
        item.workdir = item.workdir.replace(input_keyword, pengganti)
        # if is_debugging:
        #     indah0(f"[ambil_entry_dari_file_template] item.workdir = '{item.workdir}'.", warna='white', bold=True, newline=True)

    basefolder = dirname(item.workdir)
    if not isdir(basefolder):
        # indah4(f"[ambil_entry_dari_file_template] creating non-empty dirname of item.workdir = {basefolder}", warna='blue', layar='yellow')
        create_if_empty_dir(basefolder)


    if entries:
        if len(entries) == 1:
            hasil = entries[0]
            content = Common.definisi(hasil, fmus_file)
        else:
            terpendek = min(entries, key=len)
            content = Common.definisi(terpendek, fmus_file)
        
        # content = sanitize_chars(content)
        isi = invoke_llm_active(content, verbose=False)
        indah4(f"content [{content[:100]}] menjadi [{isi[:100]}]", layar='white', warna='magenta')
        write_mode = 'w' if not hasattr(item, 'appending_mode') else 'a'
        if hasattr(root_tree, 'variables'):
            write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi, root_tree.variables)
        else:
            write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi)
    else:
        indah0(f"[ambil_entry_dari_file_template] {barisentry} tidak ditemukan di {fmus_file}\nCek apa benar ada.", warna='magenta', newline=True)
