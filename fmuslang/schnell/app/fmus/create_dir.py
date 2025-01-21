import os
from anytree.search import findall
from schnell.app.dirutils import isdir_simple, joiner, bongkar, isdir, absolutify, isabsolute
from schnell.app.fmusutils import replace_from_configuration_new_replacer_input_if_input
from schnell.app.printutils import indah0, indah4
from schnell.app.utils import env_get, linuxify, not_the_same_folder, platform, env_int
from .common import Common, input_keyword
from .treehelper import get_all_tree_children
from rich.pretty import pprint


def create_dir(root_tree, item, projectdir, self_debug, self_run_configuration=None):
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f'''[create_dir]
      root        {root_tree}
      workdir     {item.workdir}
      projectdir  {projectdir}
      item        {item}
      ''', warna='yellow')
    # self_debug('[create_dir] root:', root_tree)
    # self_debug('[create_dir] workdir:', item.workdir)
    # self_debug('[create_dir] projectdir:', projectdir)
    # self_debug('[create_dir] item #1 (pre process "input"):', item)						
  ################################################################################
  # jk type = dir, name = input and 'input' in workdir 
  # jk hasattr(root_tree, 'variables')
  # jk hasattr(item, 'old_name') and item.old_name in root_tree.variables
  # ganti name dan workdir
  # doubt = apakah sekarang item.workdir sudah dibuat?

  # if hasattr(item, 'forced_operation'):
  # 	workdir_lama = item.workdir
    
  # 	kunci = item.old_name
  # 	newname = root_tree.variables[kunci]
  # 	item.workdir = newname

  # 	# ini gak sedirect ini, hrs modify semua children
  # 	# gunakan teknik dari https://anytree.readthedocs.io/en/latest/api/anytree.search.html
  # 	anakcucu = findall(item, filter_=lambda anak: workdir_lama in anak.workdir)
  # 	for oprek in anakcucu:
  # 		oprek.workdir = oprek.workdir.replace(workdir_lama, newname)

  # 	# projectdir hrs dimodified krn akan dibaca oleh child program nantinya
  # 	projectdir = projectdir.replace(workdir_lama, newname)
  # 	# # coba debug dulu sebentar
  # 	print(RenderTree(item))
  # 	input('Debug sementara... ')

  if item.type == 'dir' \
    and item.name == input_keyword \
    and input_keyword in item.workdir:

    self_debug("[create_dir] item.type == 'dir' and item.name == input_keyword and input_keyword in item.workdir\n")

    if hasattr(root_tree, 'variables'):
      '''
      direktori bernama input
      dan parent/root_tree punya variables yg ngasih tau nama baru untuk workdir
      '''
      if hasattr(item, 'old_name') and item.old_name in root_tree.variables:
        kunci = item.old_name
        newname = root_tree.variables[kunci]
        # input dari user bisa absolute path spt /tmp/hapus/latihan
        # maka ini jadi new workdir
        item.name = newname
        if newname.startswith('/'):
          workdir_lama = item.workdir
          item.workdir = newname
          # ini gak sedirect ini, hrs modify semua children
          # gunakan teknik dari https://anytree.readthedocs.io/en/latest/api/anytree.search.html
          anakcucu = findall(item, filter_=lambda anak: workdir_lama in anak.workdir)
          for oprek in anakcucu:
            oprek.workdir = oprek.workdir.replace(workdir_lama, newname)

          # projectdir hrs dimodified krn akan dibaca oleh child program nantinya
          # projectdir = projectdir.replace(workdir_lama, newname)
          # # coba debug dulu sebentar
          # print(RenderTree(item))
          # input('Debug sementara... ')
        else:										
          item.workdir = item.workdir.replace(input_keyword, newname, 1)

        indah4(f'[create_dir] new name = [{item.name}] and workdir = [{item.workdir}]\n', warna='black', layar='white')

    else:
      indah4(f"[create_dir] direktori bernama {input_keyword} dan ada {input_keyword} di workdir tapi 'root_tree gak punya variables'", warna='red')
      # agar tidak pake newline
      indah0(f"[create_dir] Masukkan nama direktori utk jadi basedir di {item.workdir}:", warna='white', bold=True)
      dirname = input(' ')
      old_dir = item.workdir
      dirabsolute = False

      if dirname:
        dirname = bongkar(dirname, True)
        item.name = dirname

        # set item.workdir
        if isabsolute(dirname): # dirname .startswith('/'):
          item.workdir = dirname
          dirabsolute = True
          indah4(f'[create_dir] ganti dir dari {old_dir} ke absdir: {item.workdir}', warna='yellow')
        else:
          # cek jk dimulai dg . maka kita gabungkan dulu ke os.getcwd
          # agar hasil dari mk process gak sama dg dir dari mk file
          # if dirname .startswith ('.'):
          #   dirname = absolutify(dirname)
          #   dirname = joiner(os.getcwd(), dirname)
          # CEK: lihat jk ada akibatnya, jadi /home....

          item.workdir = item.workdir.replace(input_keyword, dirname, 1).strip()
        
        # use item.workdir
        # oprek workdir anak
        # print('\n\n========================')
        for anak in get_all_tree_children(item):
          anak.workdir = anak.workdir.replace(old_dir, item.workdir)

  elif '__INPUT__' in item.workdir:
    old_dir = item.workdir
    # replace_from_configuration_new_replacer_input_if_input
    # (self_run_configuration, content_command_request, original=None, remove_prefix='', pengirim='')
    item.workdir = replace_from_configuration_new_replacer_input_if_input(self_run_configuration, \
      item.workdir, original=item.workdir, \
      remove_prefix='', pengirim='create_dir', check_absdir=True, parent=root_tree)
    for anak in get_all_tree_children(item):
      anak.workdir = anak.workdir.replace(old_dir, item.workdir)

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f"""[create_dir]""", warna='green')
    pprint(item)

  ################################################################################
  if not_the_same_folder(projectdir, item.workdir):
    if isabsolute(item.workdir):
      targetdir = item.workdir
    else:
      targetdir = joiner(projectdir, item.workdir)
    if env_int('ULIBPY_FMUS_DEBUG')>1:
      indah4(f"[create_dir] {projectdir} >< {item.workdir}, jadi targetdir = {targetdir}")
  else:
    targetdir = item.workdir
    if env_int('ULIBPY_FMUS_DEBUG')>1:
      indah4(f"[create_dir] {projectdir} == {item.workdir}, jadi bypass targetdir = joiner")

  dir_exist = False

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    print('[create_dir] platform:', platform(), 'linuxifying:', linuxify(targetdir))
  if platform() == 'wsl' and isdir_simple(linuxify(targetdir)):
    if env_int('ULIBPY_FMUS_DEBUG')>1:
      print('[create_dir] linuxifying:', linuxify(targetdir))
    dir_exist = True
  elif isdir_simple(targetdir):
    dir_exist = True

  if not dir_exist:
    try:
      os.makedirs(targetdir)
    except Exception as err:
      indah4(f'''[create_dir] exception = {err}
      item.workdir = {item.workdir}
      projectdir = {projectdir}
      isdir_simple({targetdir}) = {isdir_simple(targetdir)}
      => Creating folder: [{targetdir}]\n''', 
      warna='cyan')
  else:
    if env_int('ULIBPY_FMUS_DEBUG')>1:
      indah4(f'[create_dir] isdir_simple({targetdir})={isdir_simple(targetdir)} => Folder: [{targetdir}] sudah ada\n', warna='cyan')
