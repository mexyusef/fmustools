import os
from schnell.app.dirutils import (
  bongkar,
  isfile,
)
from schnell.app.fileutils import (
	replace_from, 
	replace_at, 
	insert_after, 
	insert_before, 
	remove_lines,
)
from schnell.app.fmusutils import replace_from_configuration_replacer
from schnell.app.printutils import indah4
from schnell.app.utils import env_int
from .common import Common


# elif oper .startswith ('load_from_file_absolute'):
def load_from_file_absolute(oper, item, root_tree, self_run_configuration):
  """
  load_from_file_absolute
  F=source
  """
  source = oper.split('=', 1) [1]
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f'[load_from_file_absolute] name: {item.name} => source: [{source}]')

  # bongkar dulu krn bisa ULIBPY_ROOTDIR/...
  source = bongkar(source)

  data = ''

  if not isfile(source):
    indah4(f"[load_from_file_absolute] file/dir tidak ditemukan = [{source}]", warna='red')
  else:
    source = isfile(source) # bongkar dulu jk file ada (otherwise = False)
    binary_mode = '' if not hasattr(item, 'binary_mode') else 'b'
    with open(source, 'r'+binary_mode, encoding='utf8') as fd:
      data = fd.read()

  if data:
    # 18-12-22, ambil dari quick_command
    # utk kasus F=__CONTENT_START__ dan di dalamnya ada %__TEMPLATE_WHATEVER
    # kita pengen direplace
    # if self_run_configuration['replacer']:
    #   # request mungkin ada __FILE__ atau __CURDIR__
    #   # misal: /D>=filepath=barisentry
    #   print(f"""\n\n\n*** *** ***\n[F]\n{self_run_configuration['replacer']}""")
    #   data = replace_from_configuration_replacer(data, self_run_configuration['replacer'])
    if root_tree is not None and hasattr(root_tree, 'variables'):
      for k,v in root_tree.variables.items():
        data = data.replace(k, v)
        if env_int('ULIBPY_FMUS_DEBUG')>1:
          print(f"[load_from_file_absolute] replacing {k} with {v} in {data}.")
    with open(item.workdir, 'w'+binary_mode, encoding='utf8') as fd:
      fd.write(data)

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    # workdir adlh file
    # print('[load_from_file_absolute]', os.listdir(os.path.dirname(item.workdir)))
    print(f"""[load_from_file_absolute]
    dir content = {os.listdir(os.path.dirname(item.workdir))}
    oper = {oper}
    item = {item}
    root_tree = {root_tree}
    """)

  # tambah handle insert/replace
  if hasattr(item, 'line_indicator') \
    and hasattr(item, 'line_content') \
    and hasattr(item, 'insert_replace'):

    if env_int('ULIBPY_FMUS_DEBUG')>1:
      print('[load_from_file_absolute] Masuk ada line_indicator etc')

    # from .fileutils import replace_from, replace_at, insert_after, insert_before, remove_lines

    replacer_file = self_run_configuration['replacer']['__FILE__']
    pengisi = Common.definisi(item.line_content, replacer_file)

    # item.line_indicator berarti di sini literal ya...bukan dari entry file
    if item.insert_replace == 1:
      insert_before(item.workdir, item.line_indicator, pengisi)
    elif item.insert_replace == 2:
      insert_after(item.workdir, item.line_indicator, pengisi)
    elif item.insert_replace == 3:
      replace_at(item.workdir, item.line_indicator, pengisi)
    elif item.insert_replace == 4:
      replace_from(item.workdir, item.line_indicator, pengisi)
    elif item.insert_replace == 5:
      remove_lines(item.workdir, item.line_indicator, int(item.jumlah_hapus))
