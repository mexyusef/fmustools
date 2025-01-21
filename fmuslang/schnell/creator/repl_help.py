from schnell.app.dirutils import (
  ayah,
  dirs,
  here,
  isfile,
  joiner,
)
from schnell.app.printutils import filter_print_latest_files
from schnell.app.utils import env_get, env_int, perintah
from .context import context_subdirs
from .helper import CODE


def lang_helper(text, self_langsdir, self_config_run_configuration):
  code = text.replace('lang', '', 1).strip()
  if not code:
    filepath = joiner(self_config_run_configuration['cwd'], 'grammar', 'lang.py')
    filepath2 = joiner(self_config_run_configuration['cwd'], 'grammar', 'lang_head.py')
    filepath3 = joiner(self_config_run_configuration['cwd'], 'grammar', 'lang_body.py')
    perintah(f'{CODE} {filepath} {filepath2} {filepath3}')
  elif code == '*':
    perintah(f'{CODE} {__file__}')
  elif code == '**':
    filepath = joiner(env_get('ULIBPY_BASEDIR'), 'app/writers/README.md')
    perintah(f'{CODE} {filepath}')
  elif code == '***':
    filepath = joiner(env_get('ULIBPY_BASEDIR'), 'db/writer_service.py')
    perintah(f'{CODE} {filepath}')
  elif code == '@':
    filepath1 = joiner(env_get('ULIBPY_BASEDIR'), 'creator/declarative/handler.py')
    filepath2 = joiner(env_get('ULIBPY_BASEDIR'), 'creator/grammar/decl.py')
    perintah(f'{CODE} {filepath1} {filepath2}')
  elif code == '$':
    '''
    ,$
    '''
    # workdir = abs_dir(__file__)
    # workdir = joiner(abs_dir(__file__), 'createdb', 'by-langs')
    workdir = self_langsdir
    # perintah(f'qterminal 2>/dev/null -w {workdir} &')
    from .utils import terminal
    terminal_cmd = terminal(workdir)
    print('repl_help/lang_helper/perintah:', terminal_cmd)
    perintah(terminal_cmd)
  elif code == '%':
    filepath = joiner(env_get('ULIBPY_BYLANGSDIR'), 'mapper/HELP.txt')
    perintah(f'{CODE} {filepath}')
  elif code == '%%':
    filepath = joiner(env_get('ULIBPY_BASEDIR'), 'app/transpiler/grammar.py')
    perintah(f'{CODE} {filepath}')
  elif code == '%%%':
    filepath = joiner(env_get('ULIBPY_BASEDIR'), 'db/bantuan')
    perintah(f'{CODE} {filepath}')
  elif code in dirs(self_langsdir): # context_subdirs:
    # lang next => C:\Users\usef\work\sidoarjo\schnell\creator\grammar\lang_next.py
    filepath = joiner(self_config_run_configuration['cwd'], 'grammar', f'lang_{code}.py')
    if not isfile(filepath):
      filepath = joiner(self_config_run_configuration['cwd'], 'grammar', 'languages', f'lang_{code}.py')
    perintah(f'{CODE} {filepath}')
  else:
    print(f'{code} tidak diproses')


def wmc_handler(text, self_langsdir=None):
  '''
  bisa edit wmc.py dan fmus.py lewat wmc* dan wmc**
  tambah: .env -> wmc***
  '''
  # from schnell.app.utils import perintah
  # from os import system as komando
  # code = text.replace('wmc', '', 1).strip()
  code = text.removeprefix('wmc').strip()
  if code == '*':
    filepath = joiner(ayah(__file__, 2), 'app', 'wmc.py')
    perintah(f'{CODE} {filepath}')

  elif code == '**':
    filepath = joiner(ayah(__file__, 2), 'app', 'fmus', 'fmus.py')
    perintah(f'{CODE} {filepath}')

  elif code == '***':
    filepath = joiner(ayah(__file__, 2), '.env')
    perintah(f'{CODE} {filepath}')

  elif code == '@':
    filepath = joiner(ayah(__file__, 2), 'app', 'grammar.py')
    perintah(f'{CODE} {filepath}')

  elif code == '%':
    filepath = joiner(ayah(__file__, 2), 'langs', 'flutter', 'flumain.py')
    perintah(f'{CODE} {filepath}')

  elif code == '%%':
    filepath = joiner(ayah(__file__, 2), 'langs', 'ucsv', 'ucsv.py')
    perintah(f'{CODE} {filepath}')

  elif code == '%%%':
    filepath = joiner(ayah(__file__, 2), 'langs', 'data', 'main.py')
    perintah(f'{CODE} {filepath}')

  # elif code == '^':
  #   # kita update flutter/form.mk
  #   # filepath = joiner(ayah(__file__, 2), 'creator/createdb/by-langs/flutter', 'form.mk')
  #   print('self_langsdir utk akses flutter/form.mk:', self_langsdir)
  #   filepath = joiner(self_langsdir, 'flutter', 'form.mk')
  #   perintah(f'{CODE} {filepath}')

  else:
    from schnell.app.wmc import main as wmc_main
    wmc_main()


def repl_handler(text):
  code = text.replace('repl', '', 1).strip()
  if not code:
    filepath = joiner(ayah(__file__, 1), 'repl.py')
    perintah(f'{CODE} {filepath}')
  elif code == '*':
    '''bindings keys
    pilihan:
    *, **, ***
    %,
    ^
    '''
    filepath = joiner(here(__file__), 'bindings', 'karya.py')
    perintah(f'{CODE} {filepath}')
  elif code == '**':
    filepath = joiner(here(__file__), 'mybindings.py')
    perintah(f'{CODE} {filepath}')
  elif code == '***':
    filepath = joiner(ayah(__file__, 2), 'app', 'fileutils.py')
    perintah(f'{CODE} {filepath}')
  elif code == '@':
    filepath = joiner(ayah(__file__, 2), 'db', 'myredis.py')
    perintah(f'{CODE} {filepath}')
  elif code == '%':
    filepath = joiner(ayah(__file__, 2), 'db', 'mapper.py')
    perintah(f'{CODE} {filepath}')
  elif code == '%%':
    filepath = joiner(ayah(__file__, 2), 'db', 'replservice.py')
    perintah(f'{CODE} {filepath}')
  else:
    print(text, '=>', code)


def ulib_helper(text):
  code = text.replace('ulib', '', 1).strip()
  if not code:
    perintah(f'{CODE} {ayah(__file__,3)}')
  elif code == '*':
    perintah(f"code {joiner(ayah(__file__,3), 'upy/ulibpy/xcurse/codes')}")
  elif code == '**':
    folder = env_get('ULIBPY_SNIPPETS')
    perintah(f'{CODE} {folder}')
  elif code == '***':
    perintah(f"code /home/usef/dahsyat/bantuan")
  elif code == '@':
    bylangs = env_get('ULIBPY_BYLANGSDIR')
    mapperdir = joiner(bylangs, 'mapper')
    perintah(f"code {mapperdir}")    
  elif code == '%':
    perintah(f"code /home/usef/common/working/")
  elif code == '%%':
    perintah(f"code /home/usef/_dahsyat")


def latest_file_handler(text):
  code = text.replace('|', '', 1).strip()

  # basedir = env_get('ULIBPY_BASEDIR')
  basedir = env_get('ULIBPY_BYLANGSDIR')

  if code.startswith('*'):
    code = code.replace('*', '', 1).lstrip()
    basedir = env_get('ULIBPY_BASEDIR')

  def internal():
    hasil = filter_print_latest_files(code, basedir, env_int('ULIBPY_WMC_LATEST_SHOW_TIME'))

  internal()


def bahasa_entry(text):
  """
  bantuan utk
  `tailwind
  `*tailwind
  """
  prefix = 'H' if text .startswith ('H') else '`'
  from .grammar import bahasa
  baris = [item for item in bahasa.splitlines() if item and ':' in item and 'HURUF' not in item and item.endswith('"')]
  if text .startswith (f'{prefix}*'):
    '''
    `*tailwind
    H*tailwind
    '''
    baris = sorted(baris)
    code = text.replace(f'{prefix}*', '', 1).strip()
  else:
    '''
    `tailwind
    Htailwind
    '''
    code = text.replace(f'{prefix}', '', 1).strip()

  if code:
    baris = [item for item in baris if code in item]
  
  return '\n'.join(baris)
