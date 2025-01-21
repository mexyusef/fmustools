
from app.dirutils import (
  ayah, here, joiner, isfile
)
from app.fileutils import file_content
from app.fmus import Fmus
from app.utils import env_int, tidur
from app.printutils import print_json, print_file
disini = here(__file__)


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

# | "1" -> setup
# | "2" -> register
# | "3" -> login
# | "4" -> product_list
# | "5" -> product_detail
# | "6" -> cart_create
# | "7" -> cart_update
# | "8" -> cart_delete
# | "9" -> middleware_create_order
# | "10" -> profile_reset_password
# | "11" -> update_avatar_name
# | "12" -> orders
# | "13" -> payment
# | "14" -> admin_order_manager
# | "15" -> admin_user_manager
# | "16" -> admin_category_manager
# | "17" -> admin_create_product
# | "18" -> admin_update_product
# | "19" -> admin_delete_product
# | "20" -> load_more
# | "21" -> filter_sort_search

def setup(tree):
  kembali = 'setup'
  for item in anak(tree):
    jenis = data(item)
    if jenis == '':
      pass
    elif jenis == '':
      pass
    elif jenis == '':
      pass
  kembali += f''
  return kembali


def register(tree):
  kembali = 'register'
  for item in anak(tree):
    jenis = data(item)
    if jenis == '':
      pass
    elif jenis == '':
      pass
    elif jenis == '':
      pass
  kembali += f''
  return kembali


def semua_file(tree, pilihan='setup'):
  kembali = pilihan
  for item in anak(tree):
    jenis = data(item)
    if jenis == '':
      pass
    elif jenis == '':
      pass
    elif jenis == '':
      pass
  kembali += f''
  return kembali

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
    elif jenis == '':
      pass
  # kembali += f''
  return kembali


def statement_config(tree):
  # print('statement_config')
  kembali = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'statement_config_list':
      res = statement_config_list(item)
      kembali.update({
        'config': res
      })
    elif jenis == '':
      pass
    elif jenis == '':
      pass
  # kembali += f''
  return kembali


def handler(tree):
  """
  statement
    statement_config
      statement_config_list
        run_fmus
    setup

  filename_input = 'bantu_sql'
  filename_input_ext = f'{filename_input}.mk'
  filepath_input = joiner(disini, filename_input_ext)
  """  
  kembali = ''
  config = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'statement_config':
      res = statement_config(item)
      # kembali += 'hasil config: ' + str(res)
      config.update(res)
    elif jenis in [
      'setup', 
      'register', 
      'login', 
      'product_list', 
      'product_detail', 
      'cart_create', 
      'cart_update', 
      'cart_delete', 
      'middleware_create_order', 
      'profile_reset_password', 
      'update_avatar_name', 
      'orders', 
      'payment',
      'admin_order_manager',
      'admin_user_manager',
      'admin_category_manager',
      'admin_create_product',
      'admin_update_product',
      'admin_delete_product',
      'load_more',
      'filter_sort_search',
      ]:
      res = semua_file(item, jenis)
      config.update({
        'run': res
      })
    # elif jenis == 'setup':
    #   res = setup(item)
    #   config.update({
    #     'run': res
    #   })
    # elif jenis == 'register':
    #   res = register(item)
    #   config.update({
    #     'run': res
    #   })
    elif jenis == '':
      pass
  kembali += str(config)
  # print_json(config)
  if 'run' in config:
    filename = config['run'] + '.mk'
    filepath  = joiner(disini, filename)
    print(filename, filepath)
    if isfile(filepath):
      # print_file(filepath)
      # program = file_content(filepath)
      fmus = Fmus(debug=True)
      fmus.set_file_dir_template(filepath)
      # fmus.process(program)
      fmus.process_mkfile(filepath, baris_entry='index/fmus')

  return kembali
