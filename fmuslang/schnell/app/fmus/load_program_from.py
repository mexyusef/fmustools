import copy, json
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import isfile, abs_dir, normy
from schnell.app.fileutils import get_lastpath_and_filename
from schnell.app.fmusutils import replace_from_configuration, get_input_generic_if_input_not_from_template
from schnell.app.jsonutils import MyJsonify
from schnell.app.printutils import indah0, indah4
from schnell.app.utils import env_int
from .common import Common
from .fmus import Fmus
from .treehelper import get_all_tree_children


def load_program_from(root_tree, oper, item, self_debug, self_run_configuration):
  '''
  %tempate_anak=__CURDIR/file_anak.mk
  somedir,d(/load=__CURDIR/file.mk=cari-program/fm.us)
  somedir,d(/load=tempate_anak=cari-program/fm.us)

  for k,v in self_run_configuration['replacer'].items():
    template_file = root_tree.variables[kunci]

  harusnya bisa temukan cara shg gak perlu __CHILD*
  misal dg save dulu replacer parent...
  stlh proses child selesai maka balikkan replacer nya.
  sptnya yg perlu disave
  replacer
  projectdir
  initial_rootvars
  '''
  #shortcut,d(/load=__CURDIR__/2021/present/be_sharp/sharp.mk=index/fm.us)
  _, program_source, cari_baris = oper.split('=')
  is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
  # is_debugging = 2

  forced_entry = False

  if cari_baris.endswith('*'):
    forced_entry = True
    cari_baris = cari_baris[:-1]

  # UPD 3 mei 2022, bisa __INPUT__,d(/load=...)
  if '__INPUT__' in item.workdir:
    old_dir = item.workdir
    # item.workdir = replace_from_configuration_new_replacer_input_if_input(self_run_configuration, \
    #   item.workdir, original=item.workdir, \
    #   remove_prefix='', pengirim='load_program_from', check_absdir=True)
    item.workdir = get_input_generic_if_input_not_from_template(item.workdir, item.parent, 'load_program_from')
    # input(f'[load_program_from] press: item.workdir {old_dir} => {item.workdir}: ')
    for anak in get_all_tree_children(item):
      anak.workdir = anak.workdir.replace(old_dir, item.workdir)

  if is_debugging:
    indah4(f'''[load_program_from]
    item = {item}
    root = {root_tree}
    workdir = {item.workdir}
    program_source = {program_source}
    ''', warna='yellow')
  ################################################################################
  # jk type = dir, name = input and 'input' in workdir
  # jk hasattr(root_tree, 'variables')
  # jk hasattr(item, 'old_name') and item.old_name in root_tree.variables
  # ganti name dan workdir
  # doubt = apakah sekarang item.workdir sudah dibuat?
  ################################################################################
  # baru: coba gaya backup
  self_backup_configuration = copy.deepcopy(self_run_configuration)
  # terlalu rame
  # self_debug('\tsaving configuration', self.backup_configuration)

  # for k,v in self_run_configuration['replacer'].items():
  #   # UPDATE:
  #   # normy
  #   # print(f'replacing {k} dengan {v}')
  #   program_source = program_source.replace(k, v)
  program_source = replace_from_configuration(program_source, self_run_configuration)
  program_source = normy(program_source)

  if is_debugging:
    self_debug('[load_program_from] post replace, pre root.vars, program_source =', program_source)

  if hasattr(root_tree, 'variables'):
    for k,v in root_tree.variables.items():
      program_source = program_source.replace(k, v)

  if is_debugging:
    self_debug('[load_program_from] post root.vars, program_source =', program_source)

  if isfile(program_source):
    '''
    di sini generator hrs bisa akses fmus class.
    kita kasih __CHILDFILE dan __CHILDCURDIR krn
    __FILE dan __CURDIR masih mengarah ke parent/ancesor
    '''
    # content = file_content(program_source)
    content = Common.definisi(cari_baris, program_source)
    if content:
      replacer_for_child = copy.deepcopy(self_run_configuration['replacer'])
      replacer_for_child['__CHILDFILE__'] = program_source
      replacer_for_child['__CHILDFILE'] = program_source
      replacer_for_child['__CHILDCURDIR__'] = abs_dir(program_source)
      replacer_for_child['__CHILDCURDIR'] = abs_dir(program_source)

      replacer_for_child['__FILE__'] = program_source
      replacer_for_child['__FILE'] = program_source
      replacer_for_child['__CURDIR__'] = abs_dir(program_source)
      replacer_for_child['__CURDIR'] = abs_dir(program_source)
      child_program = Fmus(is_debugging)
      # ternyata item.workdir bisa salah utk anak, krn ngikutin parent
      # harus ikutin workdir dari item.parent.
      child_program_params = {
        'item skrg adlh'							  :	item,
        'root dari item sekarang adlh'	:	item.parent,
        # ternyata projectdir menjadi initial value utk workdir, item.parent adlh item di atas /load=file=entry, biasanya folder
        # workdir utk child hrs ngikutin workdir dia utk benar sesuai alur program
        # 'projectdir'									  : item.workdir,
        'projectdir'									  : item.parent.workdir,
        'replacer'										  :	replacer_for_child, 
      }
      if hasattr(root_tree, 'variables'):
        child_program_params.update({
          'rootvars': root_tree.variables
        })
      if is_debugging:
        indah4(f"""[load_program_from] child_program_params utk child_program = Fmus(env_int('ULIBPY_FMUS_DEBUG'))
        {json.dumps(child_program_params, indent=2, cls=MyJsonify)}
        """, warna='yellow')

      lanjut = True
      confirm = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_CONFIRM_CHILD_PROGRAM"] # env_int('ULIBPY_CONFIRM_CHILD_PROGRAM')
      if (not forced_entry) and confirm:
        lanjut = False
        indah0(f'\n{"="*40} ', warna='bright_yellow')
        indah0(get_lastpath_and_filename(program_source), warna='bright_yellow', reverse=True, newline=True)
        pesan_jalankan_child_program = f"""[load_program_from] Exec child program [{program_source}][{cari_baris}]
        \nParams ke child program = [{str(child_program_params)[:100]}]
        \nLokasi = [{item.workdir}]
        \n"{content[:100]}..."
        \ny[n]?"""
        indah0(pesan_jalankan_child_program, warna='magenta', bold=True)
        yesno = input(' ')
        if yesno == 'y' or yesno == 'yes' or yesno == 'Y':
          lanjut = True

      if lanjut:
        short_content = content[:40].replace('\n','\\n').replace('\t','\\t')
        indah0(f"""[load_program_from#L143]
          Executing child program [{short_content}...] dg "child_program.process(content, **child_program_params)"
          root_tree       = {root_tree}
          item            = {item}
          child_program_params = {json.dumps(child_program_params, indent=2, cls=MyJsonify)}
          """, warna='magenta', bold=True, newline=True)
        child_program.process(content, **child_program_params)

    else:
      # cari_baris, program_source
      indah0(f"\n[load_program_from] {program_source} tidak berisi [{cari_baris}]...",
             warna='bright_red', bold=True)
      input(' ')

  else:
    indah0(f"\n[load_program_from] {program_source} tidak ditemukan...",
           warna='bright_red', bold=True)
    input(' ')

  # baru: restore
  self_run_configuration = copy.deepcopy(self_backup_configuration)
