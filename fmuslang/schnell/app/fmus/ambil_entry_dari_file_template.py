import ast
from schnell.app.dirutils import isdir, isfile, dirname, normy, create_if_empty_dir
from schnell.app.printutils import indah, indah0, indah3, indah4
from schnell.app.utils import env_int, env_expand
from schnell.app.fmusutils import replace_from_configuration_replacer
from .common import Common, input_keyword
from .write_file_with_variable_expansion import write_file_with_variable_expansion


# elif oper .startswith('ambil_entry_dari_file_template'):
def ambil_entry_dari_file_template(oper, item, root_tree, self_debug, self_run_configuration):
  '''
  TODO: bersih2...

  oper: ambil_entry_dari_file_template={'template': 'cari1024'}
    di sini, dict_file_baris.items() hanya satu tentunya
  template -> src, utama, main, dll
  cari1024: program/001/fm.us dll

  kita pengen stlh dapat entry dari template::cari1024, kita oprek replacer.
  write_file_with_variable_expansion

  update:
  kita tambah 4 operasi insert before/after/replace at/from
  dg 2 kunci:
  insert_replace = 1/2/3/4
  line_indicator = baris utk jadi indicator to insert/replace
  '''
  is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
  dict_file_baris = oper.split('=') [1] # e=file=baris => {file:baris}
  dict_file_baris = ast.literal_eval(dict_file_baris)
  kunci_yang_cuma_berjumlah_satu = list(dict_file_baris.keys())[0]
  fmus_barisentry = dict_file_baris[kunci_yang_cuma_berjumlah_satu]
  template_file = kunci_yang_cuma_berjumlah_satu

  # for fmus_filepath, fmus_barisentry in dict_file_baris.items(): # fmus_filepath, fmus_barisentry sebetulnya filepath=barisentry
  #   '''sebetulnya items cuma ada 1 pair k,v dimana k = file template, v = cari baris
  #   file template bisa berisi % variables: e=src=baris
  #   atau replacer: e=__FILE__=baris
  #   tapi gak bisa keduanya.

  #   misal e=__FILE__=barisentry
  #   fmus_filepath = __FILE__, fmus_barisentry = barisentry
  #   '''

  if is_debugging:
    indah4(f"""[ambil_entry_dari_file_template] before replace
    item = {item}
    item.workdir = {item.workdir}
    root_tree = {root_tree}
    template_file = {template_file}
    fmus_barisentry = {fmus_barisentry}
    self_run_configuration['replacer'] = {self_run_configuration['replacer']}
    """, warna='red', layar='white')

  template_file = replace_from_configuration_replacer(template_file, self_run_configuration['replacer'])

  # perlu ubah: item.workdir jika ada root_tree.item, template_file/kunci jika ada di root_tree.item
  if hasattr(root_tree, 'variables'):
    for varkunci, varnilai in root_tree.variables.items():
      item.workdir = normy(item.workdir.replace(varkunci, varnilai))
      # # filepath bisa sama dengan varkunci
      # if template_file==varkunci:
      #   template_file = root_tree.variables[template_file]
      template_file = normy(template_file.replace(varkunci, varnilai))
      fmus_barisentry = fmus_barisentry.replace(varkunci, varnilai) # misal masukkan __TABLENAME__ ke "dynamic" barisentry

  if is_debugging:
    indah4(f"""[ambil_entry_dari_file_template] after replace
    item.workdir = {item.workdir}
    template_file = {template_file}
    fmus_barisentry = {fmus_barisentry}
    """, warna='red', layar='white')

  if not isfile(template_file):
    '''
    kadang:
    e=ULIBPY_BYLANGSDIR/springboot/cepat.mk=hello groovy/groovy)
    ULIBPY_BYLANGSDIR belum diexpand
    '''
    template_file = env_expand(template_file, bongkarin=True)

  # ini adlh content utk menulis file
  # update dg code baru: get_definition...
  entries = Common.list_grep(fmus_barisentry, template_file)

  if is_debugging:
    indah0(f'[ambil_entry_dari_file_template] Cek apa butuh replace workdir, root = {root_tree}.', warna='red', bold=True, newline=True)
    indah0(f'[ambil_entry_dari_file_template] Cek apa butuh replace workdir, item = {item.workdir}.', warna='white', bold=True, newline=True)

  if input_keyword in item.workdir \
    and hasattr(root_tree, 'input_keys') \
    and hasattr(root_tree, 'input_keys_index') \
    and hasattr(root_tree, 'variables'):
    terindeks = root_tree.input_keys[root_tree.input_keys_index]
    if terindeks in root_tree.variables:
      pengganti = root_tree.variables[terindeks]
      if is_debugging:
        indah0(f"[ambil_entry_dari_file_template] Ganti item.workdir '{input_keyword}' menjadi '{pengganti}'.", warna='white', bold=True, newline=True)
      # item.workdir = item.workdir.replace(input_keyword, pengganti, 1)
      # ternyata __INPUT__ bisa banyak dalam item.workdir...
      item.workdir = item.workdir.replace(input_keyword, pengganti)
      if is_debugging:
        indah0(f"[ambil_entry_dari_file_template] item.workdir = '{item.workdir}'.", warna='white', bold=True, newline=True)

  # kita mau nulis ke item.workdir, tapi hrs cek dirname exist krn klo tidak akan error
  # ini bisa terjadi jk spec file berada dalam nested folder1/folder2/folder3,d lalu filename.txt,f...
  # jk folder2 atau 3 blm ada akan error
  basefolder = dirname(item.workdir)
  if not isdir(basefolder):
    indah4(f"[ambil_entry_dari_file_template] creating non-empty dirname of item.workdir = {basefolder}", warna='blue', layar='yellow')
    create_if_empty_dir(basefolder)

  if entries:
    if len(entries) == 1:
      hasil = entries[0]
      isi = Common.definisi(hasil, template_file)
      write_mode = 'w' if not hasattr(item, 'appending_mode') else 'a'
      if is_debugging:
        indah4(f"""[ambil_entry_dari_file_template] writing to file
          nulis ke {item.workdir}
          baca isi dari {template_file}:{hasil}
          write_mode {write_mode}
          root_tree (punya vars?) {root_tree}
          """, warna='green', layar='black')
      if hasattr(root_tree, 'variables'):
        write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi, root_tree.variables)
      else:
        write_file_with_variable_expansion(self_debug, self_run_configuration, item.workdir, write_mode, isi)
    else:
      '''kita bisa ambil match yg paling pendek
      ini biasanya jk file panjang muncul duluan dari file pendek
      1| sang_bumi_ruwa_jurai,f(..)
      2| sang_bumi,f(..)
      maka dapat 2 entries pas proses line 2
      '''
      if is_debugging:
        print('[ambil_entry_dari_file_template] Entry ada > 1:', len(entries), '=>', entries)
      terpendek = min(entries, key=len)
      isi = Common.definisi(terpendek, template_file)
      # binary_mode = '' if not hasattr(item, 'binary_mode') else 'b'
      write_mode = 'w' if not hasattr(item, 'appending_mode') else 'a'
      if hasattr(root_tree, 'variables'):
        write_file_with_variable_expansion(
          self_debug, self_run_configuration, item.workdir, write_mode, isi, root_tree.variables)
      else:
        write_file_with_variable_expansion(
          self_debug, self_run_configuration, item.workdir, write_mode, isi)
      # with open(item.workdir, write_mode) as fd:
      # 	fd.write(isi)
  else:
    indah0(f"[ambil_entry_dari_file_template] {fmus_barisentry} tidak ditemukan di {template_file}\nCek apa benar ada.", warna='magenta', newline=True)
