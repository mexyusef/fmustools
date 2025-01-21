from schnell.creator.repl_language.replify import replify
from ..write_file_with_variable_expansion import write_file_with_variable_expansion



def ambil_replify_here(oper, item, root_tree, self_debug, self_run_configuration):
    """
    myfile.py,f(code[py]=ff)
    "code" langchoice "=" ISI_FILE_TERMASUK_KOMA_TAMBAH_PERSEN -> ambil_replify_here
    NewNode.operations_codecontent = codecontent
    NewNode.operations_langchoice = langchoice
    """
    codecontent = item.operations_codecontent
    langchoice = item.operations_langchoice

    isi = replify(codecontent, item.workdir, language_to_choose=langchoice)
    write_mode = 'w' if not hasattr(item, 'appending_mode') else 'a'
    if hasattr(root_tree, 'variables'):
        write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi, root_tree.variables)
    else:
        write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi)
