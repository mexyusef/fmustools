import enum, json, os

from schnell.app.dirutils import (
	dirs, files,
	joiner,
  isfile,
)
from schnell.app.utils import env_get, env_int, env_exist, platform
from schnell.app.printutils import indah4
from .context_langdirs import subdirs as context_subdirs


class Lang(enum.Enum):
  CPP       = 'cpp'
  CS        = 'cs'
  CLJ       = 'clj'
  DART      = 'dart'
  ELIXIR    = 'elixir'
  ELM       = 'elm'
  ERLANG    = 'erlang'
  FS        = 'fs'
  GO        = 'go'
  GROOVY    = 'groovy'
  HS        = 'hs'
  JAVA      = 'java'
  JS        = 'js'
  KT        = 'kt'
  PHP       = 'php'
  PL        = 'pl'
  PY        = 'py'
  R         = 'r'
  RB        = 'rb'
  RS        = 'rs'
  SCALA     = 'scala'
  SWIFT     = 'swift'
  TS        = 'ts'
  ZIG       = 'zig'

  AWK       = 'awk'
  BASH      = 'bash'
  BATCH     = 'batch'
  CSS       = 'css'
  LESS      = 'less'
  SASS      = 'sass'
  SED       = 'sed'

languages = [item.value for item in Lang]

class Declang(enum.Enum):
  ANTD      = 'antd'
  ANTDI     = 'antd.icon'
  BS4       = 'bs4'
  HTML      = 'html'
  MUI       = 'mui'
  MUII      = 'mui.icon'
  QML       = 'qml'
  REACT     = 'react'
  RN        = 'react.native'
  WPF       = 'wpf'

declanguanges = [item.value for item in Declang]

class Guilang(enum.Enum):
  GOPROMPT    = 'go-prompt'
  GTK         = 'gtk'
  GTKCS       = 'gtkcs'
  PYGAME      = 'pygame'
  PYQT5       = 'pyqt5'
  PYPROMPT    = 'python-prompt'
  QT          = 'qt'
  RSCURSIVE   = 'rs-cursive'
  TKINTER     = 'tkinter'
  URWID       = 'urwid'
  WPF         = 'wpf'
  WX          = 'wx'
  WXP         = 'wxpython'

guilanguanges = [item.value for item in Guilang]

class Mobilelang(enum.Enum):
  ANDROID     = 'android'
  FLUTTER     = 'flutter'
  REACTNATIVE = 'reactnative'

mobilelanguanges = [item.value for item in Mobilelang]

class Chartlang(enum.Enum):
  BIZCHART    = 'bizchart'
  ECHART      = 'echart'
  HIGHCHART   = 'highchart'

chartlanguanges = [item.value for item in Chartlang]

from context import global_context as context
# # harus berasosiasi dg config.json
# # krn context hanya overwrite yg ada di config.json
# # kita gunakan ? utk ganti-ganti nilai context
# context = {
#   # 'current_chart'               : Chartlang.HIGHCHART.value,
#   'current_chart'               : 'highchart',
#   # 'current_gui'                 : Guilang.PYQT5.value,
#   'current_gui'                 : 'pyqt5',
#   # 'current_language'            : Lang.PY.value,
#   'current_language'            : 'py',

#   # mestinya jk invoke flutter program, nilai ini jg langsung berubah
#   # 'current_mobile'              : Mobilelang.FLUTTER.value,
#   'current_mobile'              : 'flutter',
#   # 'current_declarative'         : Declang.REACT.value,
#   'current_declarative'         : 'react',

#   'override_language'           : None,
#   # ini utk `react itu hasilkan baris entry react utk vscode atau tampilkan entry bahasa react?
#   'petik_vscode'                : True,
#   'pyautogui_input'             : None,

#   # 'print_after_process'         : True,
#   # tujuannya utk generate file dll
#   'working_folder'              : None,

#   # $$link= dan $$img= apakah diaktifkan
#   'fmus_expansion_mode'         : True,

#   'fmus_editor_folding'        : True,

#   # 'fmus_expansion_mode'         : False,
#   'clock_reminder'              : False,

#   'quick_viewer_folding'        : True,

#   # /ketik)
#   'characters_per_minute'       : 8000,
#   # ctrl alt p di fmus editor
#   'current_active_language'     : 'py',
# }

def toggle_anything(kunci):
  if not kunci in context:
    print(context.keys())
    return

  context[kunci] = not context[kunci]
  print(json.dumps(context, indent=2))

def set_anything(kunci, value):
  if not kunci in context:
    print(context.keys())
    return

  if value.isdigit():
    value = int(value)

  context[kunci] = value
  print(json.dumps(context, indent=2))

def toggle_reminder():
  context['clock_reminder'] = not context['clock_reminder']
  indah4(f"""[creator.context]
  context['clock_reminder'] = {context['clock_reminder']}
  """, warna='cyan')

def decl_filename(language):
  return '_decl.' + language

def current_decl_filename():
  return 'decls/' + '_decl.' + context['current_declarative']

modifiers_ = [
  "public",
  "private",
  "protected",

  # types
  "bool", "char", "double", "float", "int", "str",
  # "string",

  # keywords
  # hati2...krn kita bisa bikin file loh!
  # wkt tambah di sini, pastikan kita gak bakal bikin file
  # keyword.bhs.mk

  # "annotation",
  # "async", # wah jangan dong...
  # "decorator",
  "await",
  "extern",
  "final",
  "def", "fn", "fun",
  # "func",
  # "function",
  "internal",
  "static",
  "volatile",
]

def modifiers(word):
  return word in modifiers_

def embeddable(word):
  """
  keywords grammar yg itemnya hasilkan ' ' space instead of newline
  jk digabung dg item lain
  """
  return modifiers(word) # and embed1(word) and embed2(word)

# jk fu/evt dll gak ketemu, oprek ini...

if not env_exist('ULIBPY_BYLANGSDIR'):
  # basedir = '/home/usef/work/ulibs/database/by-langs'
  # # print('platform:', platform())
  # if platform() in ['win32', 'windows', 'desktop']:
  #   basedir = 'c:/work/refactor/database/by-langs'
  #   if platform() == 'windows': # acer
  #     basedir = 'C:/Users/usef/work/sidoarjo/database/by-langs'
  #   if not isdir(basedir): # desktop
  #     basedir = 'c:/work/sidoarjo/database/by-langs'
  #     if not isdir(basedir): # acer
  #       basedir = 'C:/Users/usef/work/sidoarjo/database/by-langs'
  # elif platform() == 'termux':
  #   basedir = '/data/data/com.termux/files/home/sidoarjo/database/by-langs'
  # elif not isdir(basedir):
  #   basedir = '/home/usef/work/sidoarjo/database/by-langs'
  #   # print(f'forcing by-langs to {basedir}')
  # import os
  creatordir = os.path.dirname(__file__)
  schnelldir = os.path.join(creatordir, os.pardir)
  sidoarjodir = os.path.join(schnelldir, os.pardir)
  basedir = os.path.join(sidoarjodir, 'database/by-langs')

else:
  basedir = env_get('ULIBPY_BYLANGSDIR')

def get_replaceable():
  """
  fu/web
  fu/evt
  gak diproses krn ini kah???
  """
  # self.replaceable = list(set([item.split('.')[0] for item in files(joiner(self.createdir, 'by-langs'))]))

  # cek culprit bisa jadi salah baca bylangs-dir....

  # print('[creator.context][get_replaceable] basedir:', basedir)

  daftar_files = files(basedir)
  # get filenames dari bylangs/, tapi skip yg hidden files
  daftar_files_noext = [item.split('.')[0] for item in daftar_files if not item.startswith('.')]
  daftar_files_unik = list(set(daftar_files_noext))
  # biar gampang didebug dan dibaca, sort dulu
  daftar_files_unik = sorted(daftar_files_unik)

  # tambah subfolders di bylangs/
  daftar_dirs = dirs(basedir, skip_hidden=True)
  for folder in daftar_dirs:
    tambahan = files(joiner(basedir, folder))
    tambahan_noext = [folder + '_' + item.split('.')[0] for item in tambahan]
    tambahan_unik = list(set(tambahan_noext))
    daftar_files_unik += tambahan_unik

  return daftar_files_unik

def get_filepath(konstruk, lang):
  """
  cli.mk
  -> konstruk = cli
  springboot/create.mk
  -> konstruk = springboot_create

  utk subdirektori buat dulu di
  context_langdirs.py/subdirs
  """
  basedir = env_get('ULIBPY_BYLANGSDIR')
  if not basedir:
    # jk dipanggil dari app yg gak loading .env
    # import os
    curdir = os.path.dirname(__file__)
    schnelldir = os.path.join(curdir, '..')
    sidoarjodir = os.path.join(schnelldir, '..')
    basedir = os.path.join(sidoarjodir, 'database/by-langs/')

  default_filename = konstruk + '.' + lang + '.mk'
  default_filepath = joiner(basedir, default_filename)

  if isfile(default_filepath):
    filepath = default_filepath
  else:
    # jk konstruk = dataframe (file) tapi ada subdir = 'data' mak is_konstruk_subdir true,
    # padahal harusnya false
    is_konstruk_subdir = [subdir for subdir in context_subdirs if konstruk.startswith(subdir)]
    if env_int('ULIBPY_FMUS_DEBUG')>1:
      print(f"""[schnell/creator/context][get_filepath]
      is_konstruk_subdir = {is_konstruk_subdir}
      [subdir for subdir in context_subdirs if konstruk.startswith(subdir)]
      {[subdir for subdir in context_subdirs if konstruk.startswith(subdir)]}
      """)
    if is_konstruk_subdir:
      if len(is_konstruk_subdir)>1:
        tambahan = max(is_konstruk_subdir)  # ['spring', 'springboot']
      else:
        tambahan = is_konstruk_subdir[0]  # misal springboot, android, dll
      # konstruk misalnya springboot_create
      basedir = joiner(basedir, tambahan)
      # springboot_create menjadi create
      # konstruk = kurangi(konstruk, tambahan)
      konstruk = konstruk.replace(tambahan + '_', '', 1).strip()
      filepath = joiner(basedir, konstruk + '.mk')
    else:
      print(f"""[creator.context] get_filepath
      konstruk = {konstruk}, lang = {lang}
      context_subdirs = [{context_subdirs}]
      pastikan kategori yg diinginkan ada di {context_subdirs}.
      default_filepath = {default_filepath} NOT FOUND!  
      """)
      filepath = default_filepath

  return filepath
