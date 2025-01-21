import copy, os
from schnell.app.appconfig import programming_data
from schnell.app.printutils import (
  indah, indah0, indah4,
)
from schnell.app.specialcmd import SpecialCommand
from schnell.app.utils import (
	trycopy,
	trypaste,
	yesno,
	env_get,
  env_int,
	env_exist,
	# env_expand,
	# perintahsp_outerr,
	# perintahsp_outerr_as_shell,
)
from .common import Common, input_keyword


# elif item.type == 'special_command':
def special_command(root_tree, item, self_debug):
  '''
  kita bikin di sini case dimana gak perlu nanya apa mau diexec:
  diawali dg * <- pastikan special_command bs handle char *
    &*showtext
  env var ULIBPY_FORCEABLE_YES == 1
  jawab yes pd prompt
  '''
  is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
  os.chdir(item.workdir)
  run_command = False
  if item.command .startswith('*'):
    # item.command = item.command.replace('*', '', 1).strip()
    run_command = True

  # replace showtext=input -> input dg nilai dari user
  cmd, cari = None, None
  if '=' in item.command:
    cmd, cari = item.command.split('=', 1)  
  if is_debugging:
    self_debug(f'[special_command] cmd = [{cmd}], cari = [{cari}]\n')
    self_debug(f'[special_command] root = [{root_tree}]\n')
    self_debug(f'[special_command] item = [{item}]\n\n')
    indah4(f'[special_command] run_command = [{run_command}]', warna='white')
  # if cmd == 'showtext' and hasattr(root_tree, 'variables') and hasattr(root_tree, 'input_keys') and hasattr(root_tree, 'input_keys_index') and root_tree.input_keys[root_tree.input_keys_index] in root_tree.variables:

  if input_keyword in item.command:
    if cmd == 'showtext' and cari == input_keyword:
      '''utk showtext input, minta input dari user di sini'''
      ganti = cari
      done = False
      while not done:
        self_debug(f'\n[special_command] showtext=input => requesting input: [{item}]...\n')
        indah4(f'Masukkan kunci utk showtext:', warna='yellow')
        masukan = input(' ')
        if masukan:
          ganti = masukan
          done = True
          self_debug(f'\n[special_command] showtext=input => getting output: [{item}]...\n')
          self_debug(f"\t[special_command] stats: root = [{root_tree}]\n")
          # self_debug(f"\tstats: repl = [{self.run_configuration['replacer']}]\n")
      item.command = '='.join([cmd, ganti])
      indah4(f'[special_command] ganti = [{ganti}], item = [{item}]\n', warna='green')

    elif cmd .startswith('ujian'):
      # root = [AnyNode(counter=0, 
      # input_keys=['__judul_tulisan'], 
      # input_keys_index=0,
      # variables={'__judul_tulisan': 'satukan'}, workdir='/tmp/sample/nulis')]
      if hasattr(root_tree, 'input_keys') \
        and hasattr(root_tree, 'input_keys_index') \
        and hasattr(root_tree, 'variables'):
        terindeks = root_tree.input_keys[root_tree.input_keys_index]
        if terindeks in root_tree.variables:
          pengganti = root_tree.variables[terindeks]
          if is_debugging:
            indah0(f"[special_command] Ganti item.command '{input_keyword}' menjadi '{pengganti}'.", warna='white', bold=True, newline=True)
          item.command = item.command.replace(input_keyword, pengganti, 1)
          if is_debugging:
            indah0(f"[special_command] item.command = '{item.command}'.", warna='white', bold=True, newline=True)

  # if env_exist('ULIBPY_FORCEABLE_YES') and env_int('ULIBPY_FORCEABLE_YES') == 1:
  if programming_data['j']['schnell']['app']['configuration']['ULIBPY_FORCEABLE_YES']:
    run_command = True

  elif not run_command:
    indah0('-- Special command "')
    indah0(item.command, warna='bright_red', bold=True)
    if is_debugging:
      indah0(f'" in [{item.workdir}] (item = [{item}], root = [{root_tree}]) y[n]?')
    else:
      indah0(f'" in [{item.workdir}] y[n]?')
    yesno_input = input(' ').strip()
    if yesno_input and yesno_input.lower() == 'y':
      run_command = True

  if is_debugging:
    indah0(f'[special_command] run_command = [{run_command}] -- sblm exec SpecialCommand [{item.command}]', warna='white', newline=True)

  if run_command:
    salin = copy.deepcopy(item)
    if salin.command.startswith('*'):
      salin.command = salin.command.replace('*', '', 1).strip()

    if is_debugging:
      indah0(f'[special_command] run_command node = [{salin}]', warna='white', newline=True)

    SpecialCommand(salin).run()
