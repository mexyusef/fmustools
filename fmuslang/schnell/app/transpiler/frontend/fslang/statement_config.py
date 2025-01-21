from app.dirutils import joiner
from app.treeutils import (
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
      code_info = ''
    elif jenis .startswith ('fe_'):
      folder = jenis.removeprefix('fe_').replace('_','-')
      # ini artinya hanya bisa 1 fe sekali invocation
      kembali.update({
        'fe': folder
      })
    elif jenis .startswith ('be_'):
      '''
      statement
        statement_config
          statement_config_list
            be_django
        csv_statement
          program_csv [usef:rahasia@localhost:27017/tempdb]{@Product=#5}name,s;brand,s;model,s
      '''
      # skrg gunakan _ sesuai asilnya
      # folder = jenis.removeprefix('be_').replace('_','-')
      folder = jenis.removeprefix('be_')
      kembali.update({
        'be': folder
      })
    elif jenis .startswith ('misc_'):
      '''
      '''
      folder = jenis.removeprefix('misc_')
      kembali.update({
        # 'be': joiner('misc', folder)
        'be': folder, # digunakan oleh: get_konfigurasi_backend() => program_config['config']['be']
      })
    elif jenis .startswith ('utils_'):
      '''
      '''
      folder = jenis.removeprefix('utils_')
      kembali.update({
        'be': folder, # digunakan oleh: get_konfigurasi_backend() => program_config['config']['be']
      })
    elif jenis == 'fullstack':
      '''
      statement
        statement_config
          statement_config_list
            fullstack
        csv_statement
          program_csv [usef:rahasia@localhost:27017/tempdb]{@Product=#5}name,s;brand,s;model,s
      '''
      kembali.update({
        'be': 'fullstack'
      })
  # kembali += f''
  return kembali


def statement_config(tree):
  # print('statement_config')
  kembali = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'statement_config_list':
      res = statement_config_list(item)
      print('[s.a.t.fe.fs.statement_config.statement_config] statement_config_list:', res, 'berjenis:', type(res))
      if 'fmus' in res:
        kembali.update({
          'config': res
        })
      elif 'fe' in res or 'be' in res:
        """
        {
          'fe': ...
        }
        atau
        {
          'be': ...
        }
        """
        kembali.update(res)
    elif jenis == '':
      pass
  # kembali += f''
  return kembali

# def statement_config(tree):
#   print('statement_config:', data(tree))
