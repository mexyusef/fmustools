from schnell.app.dirutils import exists_in_dir, not_exists_in_dir
from schnell.app.printutils import indah0, indah4
from schnell.app.utils import trycopy, env_int
from .treehelper import get_all_tree_children


def branching(root_tree, item):
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f"\n[branching] item: {item}\n", warna='green')
  # input('...branching...')
  # baik true atau false hrs iterate children dan set skip
  skip = item.skip
  if hasattr(item, 'branch_condition'):
    '''
    dari processor peta_nilai:
    'binary_no': 0,
    'binary_yes': 1,
    'binary_input': 2,
    jk code:
    ~if
      ...
    maka ini setara dg binary_input
    '''
    if len(item.branch_condition) == 0:
      condition = 2 # input dari user
    else:
      condition = item.branch_condition[0] # yes (exec) or no (skip)

    # indah4(f"[branching] condition: {condition}\n", warna='green')

    if condition == 1: # yes
      skip = False # execute
    elif condition == 0: # no
      skip = True # dont execute
    elif condition == 2: # input
      try:
        indah0(item.replacer['__FILE__'], warna='red', layar='black', bold=True, newline=True)
      except:
        print('file:', item.replacer['__FILE__'])
      print_ready = [item.level*'  ' + item.original for item in get_all_tree_children(item)]
      print_ready = '\n'.join(print_ready)
      indah0(print_ready, warna='black', layar='white', bold=True, newline=True)
      unskip = input('Apakah mau EXECUTE branch ini? y[n] ')
      if unskip and unskip == 'y' or unskip == '1':
        skip = False
    else:
      if env_int('ULIBPY_FMUS_DEBUG')>1:
        indah4(f'[branching] condition adlh: [{condition}]', warna='yellow')
      _, filepath = condition.split('=',1)
      skip = True
      if condition.startswith('exist_filedir'):
        if env_int('ULIBPY_FMUS_DEBUG')>1:
          indah4(f"[branching] exists_in_dir({item.workdir}, {filepath}) = {exists_in_dir(item.workdir, filepath)}", warna='cyan')
        # input(' ... ')
        if exists_in_dir(item.workdir, filepath):
          skip = False
      elif condition.startswith('dont_exist_filedir'):
        if env_int('ULIBPY_FMUS_DEBUG')>1:
          indah4(f"[branching] not_exists_in_dir({item.workdir}, {filepath}) = {not_exists_in_dir(item.workdir, filepath)}", warna='cyan')
        # input(' ... ')
        if not_exists_in_dir(item.workdir, filepath):
          skip = False

  else:
    '''
    else hanya bisa 1 binary condition y, n atau input/ask
    branch_info berisi: id, counter, conditions
    '''
    # jk 'else' dan gak ada branch maka "consult" parent = cari tau skip atau tidaknya
    counter = item.branch_counter
    branch_id = item.branch_id
    branch_info_index = counter - 1
    if hasattr(root_tree, 'branch_info'):
      info = [inf for inf in root_tree.branch_info if inf['id']==branch_id] [0]
      conds = info['conditions']
      # hanya consult jk index branch else kita ada/masuk dlm conditions tercantum utk branch id ybs
      if len(conds) >= counter:
        cond = conds[branch_info_index]
        skip = bool(cond)

  # unskip
  children = get_all_tree_children(item)
  print_ready = [node.level*'  ' + node.original for node in children]
  print_ready = '\n'.join(print_ready)
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah0(f"branching children => harus oprek 'skip' menjadi '{skip}' utk:\n[{print_ready}].", 
      warna='magenta', newline=True)
  for anak in children:
    anak.skip = skip
