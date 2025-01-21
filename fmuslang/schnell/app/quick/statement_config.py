from schnell.app.dirutils import joiner
from schnell.app.treeutils import (
  data, 
  token,
  child1,
  child2,
  child3,
  child4,
  child,
  chdata,
  chtoken,
  anak, 
  ispohon, istoken,
  beranak,
  sebanyak,
  jumlahanak,
)
from schnell.app.utils import env_get

def statement_config_list(tree):  
  kembali = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'run_fmus':
      # kembali = 'run_fmus nih ye|'
      kembali.update({
        'fmus': 'execute'
      })
    elif jenis == 'info':
      kembali.update({
        'operation': 'info_quick'
      })
    elif jenis == 'toc':
      kembali.update({
        'operation': 'list_statement_config_items'
      })
    elif jenis .startswith ('fslang_'):
      folder = jenis.replace('_','/')
      parent = 'app/transpiler/frontend'
      absdir = joiner(env_get('ULIBPY_BASEDIR'), parent)
      workabsdir = joiner(absdir, folder)
      # ini artinya hanya bisa 1 fe sekali invocation
      kembali.update({
        'work': folder, # fslang/path/to/target
        'modulename': jenis, # fslang_path_to_target, fslang_z_quick_django
        'generator': joiner(workabsdir, '__init__.py'),
        'fmusfile': joiner(workabsdir, 'index-input.mk'),
        'workabs': workabsdir,
      })

  return kembali


def statement_config(tree):
  # print('statement_config')
  kembali = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'statement_config_list':
      res = statement_config_list(item)
      # print('hasil statement_config_list', res)
      kembali.update(res)
    elif jenis == '':
      pass

  return kembali
