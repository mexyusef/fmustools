from anytree import (
	# AnyNode,
	# AsciiStyle,
	# Node,
	PreOrderIter,
	# RenderTree,
)
from anytree.search import find, findall
from schnell.app.printutils import print_copy, indah0, indah_enumerate, indah4
from schnell.app.utils import env_int, env_get
from schnell.app.dirutils import isfile
from schnell.app.fileutils import (
	file_content,
	get_definition_by_key_permissive_start_with_lineno,
	get_daftar,
)
from schnell.creator.context import (
	embeddable, 
	get_replaceable,
  get_filepath,
)
from schnell.db.replservice import repl_service
from startup import programming_data  # initialize_programming_data() hrs sudah dipanggil


wieke_prefix    = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_TEMPLATE_PREFIX'] # env_get('ULIBPY_WIEKES_TEMPLATE_wieke_prefix')
wieke_capper    = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_CAPITALIZE_SYMBOL'] # env_get('ULIBPY_WIEKES_CAPITALIZE_SYMBOL')
wiekeplural     = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_PLURALIZE_SYMBOL'] # env_get('ULIBPY_WIEKES_PLURALIZE_SYMBOL')
wiekelower      = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_LOWERIZE_SYMBOL'] # env_get('ULIBPY_WIEKES_LOWERIZE_SYMBOL')
wiekeupper      = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_UPPERIZE_SYMBOL'] # env_get('ULIBPY_WIEKES_UPPERIZE_SYMBOL')
wieke_space     = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_SPACECHAR'] # env_get('ULIBPY_WIEKES_SPACECHAR')
cari_separator  = programming_data['j']['schnell']['app']['configuration']['ULIBPY_BARIS_CARI_SEPARATOR'] # env_get('ULIBPY_BARIS_CARI_SEPARATOR')
replaceable = get_replaceable()


def process_type_dahan(dahan, langchoice, callback):
  dahanz = [] # daftar keyword file yg diproses
  daftarz = []
  filepath_terprocezz = []
  content = ''
  for node in PreOrderIter(dahan):
    if embeddable(node.name):
      pass
    elif node.type == 'dahan' and node.name in replaceable:
      # langchoice in use
      # ini bisa digunakan utk peroleh berbagai language version
      # jk langchoice contains ',' maka loop utk hasilkan filepaths
      filepath = get_filepath(node.name, langchoice)
      if isfile(filepath):
        baris = 'default'
        if hasattr(node, 'baris_cari'):
          baris = node.baris_cari.rstrip()
          # cek jk ada bentuk: cari1~cari2~cari3 maka semuanya jadi kondisi          
          if cari_separator in baris:
            daftar = get_daftar(filepath)
            temu = [item for item in daftar
              if all([elem in item for elem in baris.split(cari_separator)])]
            print(f'{baris} terpisah {cari_separator} = {temu}')
            if temu and len(temu)==1:
              baris = temu[0]
            elif len(temu) > 1:
              indah_enumerate(temu)
              indah0('Masukkan pilihan:', warna='cyan', bold=True)
              pilih = input(' ')
              if pilih.isdigit() and int(pilih) in range(len(temu)):
                baris = temu[int(pilih)]

        result, lineno = get_definition_by_key_permissive_start_with_lineno(filepath, baris)
        result = result.strip()
        # lineno jangan di awal barisentry, tapi di akhir
        # 27/11/2023 kita pindah ini ke get_definition_by_key_permissive_start_with_lineno
        # lineno += len(result.splitlines())
        repl_service.set_last_file_lineno(filepath, lineno)

        # if hasattr(node, 'show_only_toc') or hasattr(node, 'only_toc'):
        if hasattr(node, 'show_only_toc'):
          result = get_daftar(filepath, stringified=True)
        elif hasattr(node, 'show_content'):
          result = file_content(filepath)

        # last_lineno = lineno

        if hasattr(node, 'wiekes'):
          replacers = node.wiekes
          # __wiekes01, __wiekes02 krn gak mungkin sampai > 100
          templates = [wieke_prefix + str(angka).zfill(2) for angka in range(1,len(replacers)+1)]
          for index, wieke in enumerate(replacers):
            result = result.replace(templates[index]+wieke_capper, wieke.capitalize())
            result = result.replace(templates[index]+wiekeplural, wieke + 's')
            result = result.replace(templates[index]+wiekelower, wieke.lower())
            result = result.replace(templates[index]+wiekeupper, wieke.upper())
            result = result.replace(templates[index], wieke)
            # expand space di result
            result = result.replace(wieke_space, ' ')

        if hasattr(node, 'edit_fmus'):
          from schnell.creator.repl import edit_entry
          # input(f"[creator.repl] Now is the time to edit_fmus utk {filepath} => {baris}.\nPress Enter... ")
          edit_entry(filepath, lineno)

        # if hasattr(node, 'exec_fmus'):
        #   input(f"[creator.repl] Now is the time to exec_fmus utk {filepath} => {baris}.\nPress Enter... ")
        #   jalankan = lambda: process_fmus(filepath, baris)
        #   run_in_terminal(jalankan)
        #   # pause utk lihat output
        #   input(f"[creator.repl] Press Enter to continue... ")

        dahanz .append(f"{node.name}/{baris}")

        if filepath not in filepath_terprocezz:
          daftarz .append(get_daftar(filepath))
        filepath_terprocezz.append(filepath)
        content += result + '\n'

    elif hasattr(node, 'library_usage'):
      pass
    elif not node.name in replaceable:
      pass
    if callback:
      # pohon.operations=['content_file='+content]
      callback(content)
  # pohon.children = []

  return content


def generate(pohon, langchoice='py'):
  # dahanz = []  # daftar keyword file yg diproses
  # daftarz = []
  # filepath_terprocezz = []
  files_clipboard_content = ''

  for dahan in findall(pohon, lambda node: node.type == 'dir'):
    dahan.operations=['create_dir']

  # ini maksudnya jk f.csv dll
  # tapi kadang kita pengen scala/.csv dst.
  def callback(content):
    pohon.operations=['content_file='+content]

  find_all_type_files = findall(pohon, lambda node: node.type == 'file')

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    print(f"[schnell.creator.repl_language.generator:generate] find_all_type_files = {find_all_type_files}")

  if not find_all_type_files:
    # jk tidak diawali f, misalnya scala/.csv, js/@c dst. (alih2 biasanya \scala dan f.csv, \js dan f@c)
    files_clipboard_content = process_type_dahan(pohon, langchoice, callback)

  # ini hanya jk f.csv, ff, dst. (diawali f)
  for dahan in find_all_type_files:
    dahan.workdir += '/' + dahan.filename

    # content = ''

    content = process_type_dahan(dahan, langchoice, callback)

    pohon.children = []

    files_clipboard_content += content

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f"""[creator.repl_language.generator][generate]
    result = {files_clipboard_content}
    """)
  return files_clipboard_content
