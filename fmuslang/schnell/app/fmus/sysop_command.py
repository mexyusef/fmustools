import os, time
from rich.pretty import pprint
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import isfile, isdir, ayah, create_if_empty_dir
from schnell.app.fmusutils import replace_from_configuration_new_replacer_input_if_input
from schnell.app.fmusutils import replace_from_configuration_replacer
from schnell.app.notifutils import notifpy
from schnell.app.printutils import indah, indah0, indah4
from schnell.app.utils import (
	expand_ulib_path,
  env_int,
	env_exist,
	# env_expand,
	# perintahsp_outerr,
	perintahsp_outerr_as_shell,
)
from .common import Common, input_keyword
from .treehelper import get_all_tree_children


def sysop_command(root_tree, item, capture_outerr, self_debug, self_parent_fmus, self_run_configuration):
  '''
  kok bisa belum masuk direktori item.workdir ???
  lihat pemrosesan generate
  for item in tree
    proses jk item.operations
    proses jk type=dir
      create if dont exist
      chdir
    proses jk type=$
    proses jk type=&
    proses jk type=%%%
    proses jk type=@
    proses jk type=#
    proses jk type=%
  '''
  if programming_data['debug']:
    indah4(f'''[sysop_command]
    root = {root_tree}
    item = {item}
    workdir = {item.workdir}
    replacer = {self_run_configuration['replacer']}
    ''', warna='green')
    pprint(self_run_configuration)

  item.command = replace_from_configuration_replacer(
    item.command,
    self_run_configuration['replacer'])
  # strip $ utk sysop, / utk quick...
  if programming_data['debug']:
    indah4(f'[sysop_commad] sblm replace item.command: {item.command}, item.original: {item.original}',
      warna='yellow')

  item.command = replace_from_configuration_new_replacer_input_if_input(
    self_run_configuration,
    item.command, item.original, '$', pengirim='sysop_command-1',
    parent=root_tree)

  # ini mungkin gak terjadi salah __INPUT||somethng di workdir???
  # UPDATE: krn menginput di sini maka jk belum ada hrs dibuat dulu
  if programming_data['debug']:
    indah4(f'[sysop_commad] stlh replace item.command: {item.command}, item.original: {item.original}',
      warna='yellow')


  # TODO 3 mei 2022, bisa $* cp ULIPBY_ROOTDIR/somefile.txt .
  if 'ULIBPY_' in item.command:
    # coba mungkin ada butuh expand path
    item.command = expand_ulib_path(item.command)

  old_dir = item.workdir
  if programming_data['debug']:
    indah4(f'[sysop_commad] sblm replace item.workdir: {item.workdir}', warna='yellow')
  item.workdir = replace_from_configuration_new_replacer_input_if_input(
    self_run_configuration,
    item.workdir, item.workdir, pengirim=item.original+'|sysop_command-2',
    parent=root_tree)
  if programming_data['debug']:
    indah4(f'[sysop_commad] stlh replace item.workdir: {item.workdir}', warna='yellow')

  # semua anak hrs diganti dari __INPUT__ ke baru
  # if not isdir(item.workdir) and not isfile(item.workdir) and old_dir != item.workdir:
  # if not isdir(item.workdir) <- ini jangan krn kadang terbuat __TEMPLATE_SOMETHING
  if old_dir != item.workdir:
    # indah4(f'membuat dir {item.workdir}', warna='blue')
    create_if_empty_dir(item.workdir)
    for anak in get_all_tree_children(item):
      # print('set workdir utk item:', anak, f'dari {old_dir} ke {item.workdir}')
      anak.workdir = anak.workdir.replace(old_dir, item.workdir)
  else:
    if programming_data['debug']:
      indah4(f"""[sysop_command] masuk else {item.name} {item.original}
      not isdir(item.workdir)     {not isdir(item.workdir)}
      not isfile(item.workdir)    {not isfile(item.workdir)}
      old_dir != item.workdir     {old_dir != item.workdir}
      {item.workdir}
      """, warna='red')

  # bisa juga item/node itu type=file, workdir=path/to/file
  if isfile(item.workdir) and not isdir(item.workdir):
    workdir = ayah(item.workdir,1)
    os.chdir(workdir)
  else:
    os.chdir(item.workdir)

  run_command = False
  if item.command .startswith('*'):
    # item.command = item.command.replace('*', '', 1).strip()
    run_command = True


  if programming_data['j']['schnell']['app']['configuration']['ULIBPY_FORCEABLE_YES']:
    run_command = True
  elif not run_command:
    # self_debug(f"\t[sysop_command] stats: root = [{root_tree}]\n")
    # self_debug(f"\t[sysop_command] stats: item = [{item}]\n")
    indah0('-- Running "')
    indah0(item.command, warna='yellow', bold=True)
    indah0(f'" in [{item.workdir}] y[n]?')
    yesno = input(' ')
    # yesno = prompt('~~> ')
    # PromptSession().prompt('~~~> ')
    if yesno == 'y' or yesno == 'Y':
      run_command = True

  if run_command:
    if programming_data['debug']:
      debug_msg = f'item adlh [{item}]\nparent adlh [{item.parent}]'
      indah(f"""[sysop_command] 
            Exec command [{item.command}] 
            di [{item.workdir}]
            debug_msg [{debug_msg}]""",
        warna='magenta', bold=True, newline=True)

    bersihkan_star = item.command
    if bersihkan_star.startswith('*'):
      bersihkan_star = item.command.replace('*', '', 1).strip()

    start = time.time()
    if capture_outerr:
      out, err = perintahsp_outerr_as_shell(bersihkan_star)
      # print('perintahsp_outerr_as_shell, out=', out, 'err=', err)
      if self_parent_fmus:
        self_parent_fmus.set_outerr(out, err)
        # print('after setting, parent.out=', self.parent_fmus.stdout)
    else:
      os.system(bersihkan_star)

    end = time.time()
    elapsed = end - start
    if programming_data['notification']:
      notifpy('Selesai', f'"{bersihkan_star}" selesai dengan waktu {elapsed} detik.')
