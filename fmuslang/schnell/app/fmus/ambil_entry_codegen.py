import ast
from schnell.app.dirutils import isfile
from schnell.app.fileutils import (
	replace_from,
	replace_at,
	insert_after,
	insert_before,
	remove_lines,
	replace_entry,
	replace_between,
	replace_string_in_file,
	tab_to_space_start,
)
from schnell.app.printutils import indah, indah0, indah3
from schnell.app.utils import (
	# trycopy,
	# trypaste,
	yesno,
	env_get,
  env_int,
	env_exist,
	env_expand,
	# perintahsp_outerr,
	# perintahsp_outerr_as_shell,
)
from schnell.creator.repl_language.replify import replify
from .common import Common, input_keyword
from .write_file_with_variable_expansion import write_file_with_variable_expansion



# elif oper .startswith('ambil_entry_codegen'):
def ambil_entry_codegen(oper, item, root_tree, self_debug, self_run_configuration):
  '''
  oper: ambil_entry_codegen={'mkfilepath': 'baris_entry'}
    di sini, dict_file_baris.items() hanya satu tentunya
  mkfilepath  -> src, utama, main, dll
  baris_entry -> program/001/fm.us dll

  kita pengen stlh dapat entry dari mkfilepath::baris_entry, kita oprek replacer.
  write_file_with_variable_expansion

  update:
  kita tambah 4 operasi insert before/after/replace at/from
  dg 2 kunci:
  insert_replace = 1/2/3/4
  line_indicator = baris utk jadi indicator to insert/replace
  '''
  # oper => ambil_entry_codegen={'mkfilepath': 'baris_entry'}
  print(f"""
  ambil_entry_codegen terima oper:
  oper = >>{oper}<<
  kita mau: dict_file_baris = oper.split('=') [1] lalu ast.literal_eval
  """)

  dict_file_baris = oper.split('=') [1]
  dict_file_baris = ast.literal_eval(dict_file_baris)

  #spy gak terlalu ribut
  #indah0(json.dumps(root_tree.variables, indent=4), warna='red', layar='white', newline=True)
  original_template_file = list(dict_file_baris.keys())[0]
  for kunci, nilai in dict_file_baris.items():
    '''
    sebetulnya items cuma ada 1 pair k,v dimana k = file template, v = cari baris
    file template bisa berisi % variables: e=src=baris
    atau replacer: e=__FILE__=baris
    tapi gak bisa keduanya.

    ada masalah jk spt ini:
    ambil_entry_codegen={'__FILE__': 'pythoncode', 'langchoice': 'py'}
    template_file jadi bernilai langchoice
    '''
    # mk_filepath
    template_file = kunci
    if hasattr(root_tree, 'variables') and kunci in root_tree.variables:
      pengganti = root_tree.variables[kunci]
      # indah0('<REPLACE #1> kunci: ' + kunci + ', baris: '+ nilai + ', asal: ' + template_file + ', baru: ' + pengganti , newline=True)
      template_file = pengganti
    else:
      for k,v in self_run_configuration['replacer'].items():
        '''file template bisa berisi __CURDIR atau __FILE
        '''
        pengganti = v
        # indah0('<REPLACE #2> kunci: ' + kunci + ', baris: '+ nilai + ', asal mula: ' + k + ', baru: ' + pengganti + f' => {template_file}', newline=True)
        template_file = template_file.replace(k, v)

    if isfile(template_file):
      original_template_file = template_file

    if not isfile(original_template_file):
      '''
      kadang:
      e=ULIBPY_BYLANGSDIR/springboot/cepat.mk=hello groovy/groovy
      ULIBPY_BYLANGSDIR belum diexpand
      '''
      original_template_file = env_expand(original_template_file, bongkarin=True)

    # ini adlh content utk menulis file
    # nilai = baris_cari, baris_entry, entry_baris -> default, index/fm.us dll
    # bisa langsung content hasil list_grep atau [] krn ketemu bbrp entries
    print(f"""[ambil_entry_codegen]
    baris cari = {nilai}
    mk filepath = {original_template_file}
    item = {item}
    """)
    # list_grep => []
    # definisi => ''
    entries = Common.list_grep(nilai, original_template_file)
    if env_int('ULIBPY_FMUS_DEBUG')>=1:
      indah0(f'[ambil_entry_codegen] Cek apa butuh replace workdir, root = {root_tree}.',
        warna='red', bold=True, newline=True)
      indah0(f'[ambil_entry_codegen] Cek apa butuh replace workdir, item = {item.workdir}.',
        warna='white', bold=True, newline=True)

    if input_keyword in item.workdir \
      and hasattr(root_tree, 'input_keys') \
      and hasattr(root_tree, 'input_keys_index') \
      and hasattr(root_tree, 'variables'):
      terindeks = root_tree.input_keys[root_tree.input_keys_index]
      if terindeks in root_tree.variables:
        pengganti = root_tree.variables[terindeks]
        if env_int('ULIBPY_FMUS_DEBUG')>=1:
          indah0(f"[ambil_entry_codegen] Ganti item.workdir '{input_keyword}' menjadi '{pengganti}'.",
            warna='white', bold=True, newline=True)
        item.workdir = item.workdir.replace(input_keyword, pengganti, 1)
        if env_int('ULIBPY_FMUS_DEBUG')>=1:
          indah0(f"[ambil_entry_codegen] item.workdir = '{item.workdir}'.", warna='white', bold=True, newline=True)


    # utk codegen, kita lempar ke repl language
    langchoice = item.operations_langchoice
    if entries and len(entries) == 1:
      hasil = entries[0]
      konten = Common.definisi(hasil, original_template_file)
      isi = replify(konten, item.workdir, language_to_choose=langchoice)
      write_mode = 'w' if not hasattr(item, 'appending_mode') else 'a'
      if hasattr(root_tree, 'variables'):
        write_file_with_variable_expansion(self_debug,
          self_run_configuration, item.workdir, write_mode, isi, root_tree.variables)
      else:
        write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi)
