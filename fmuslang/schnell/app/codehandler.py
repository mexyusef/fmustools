"""
get list of languages = filenames
"""
from .dirutils import (
  files,
  sfiles,
  joiner,
)
from .fileutils import (
  absolute,
  get_daftar,
  get_definition,
  get_filename,
)
from .utils import  (
  env_get
)

EXT0 = 'mk'
EXT = '.mk'

def assign_filenames(BASEDIR):
  DATADIR = joiner(BASEDIR, 'data')
  WORKDIR = joiner(DATADIR, 'completer')
  # print(f'''[codehandler][assign_filenames]
  #   BASEDIR [{BASEDIR}]
  #   DATADIR [{DATADIR}]
  #   WORKDIR [{WORKDIR}]
  # ''')
  FILENAMES = [get_filename(item) for item in sfiles(WORKDIR)]
  return FILENAMES

BASEDIR = env_get('ULIBPY_BASEDIR')
if BASEDIR:
  FILENAMES = assign_filenames(BASEDIR)
  # DATADIR = joiner(BASEDIR, 'data')
  # WORKDIR = joiner(DATADIR, 'completer')
  # print(f'''[codehandler]
  #   BASEDIR [{BASEDIR}]
  #   DATADIR [{DATADIR}]
  #   WORKDIR [{WORKDIR}]
  # ''')
  # FILENAMES = [get_filename(item) for item in sfiles(WORKDIR)]
else:
  FILENAMES = []

need_escape = [
  '+',
  '*',
  '^',
  '$',
  '(',
  ')',
  '?',

  '-',
  '[',
  ']',
  '.',
  '\\',
  '|',
]

def get_entries(filename, key='q/'):
  if not filename.endswith(EXT):
    filename += EXT

  filepath = joiner(WORKDIR, filename)
  daftar = get_daftar(filepath)
  matches = [item for item in daftar if item.startswith(key)]
  return matches

class CodeHandler:
  def __init__(self, initial_filename='project-iot'):
    self.current_filename = initial_filename

  @property
  def filename(self):
    "apa ini getter saja?"
    return self.current_filename

  def set_filename(self, filename):
    self.current_filename = filename

  @property
  def filepath(self):
    if not self.current_filename.endswith(EXT):
      self.current_filename += EXT

    return joiner(WORKDIR, self.current_filename)

  def normalize(self, filename):
    if not self.current_filename.endswith(EXT):
      self.current_filename += EXT

    if not absolute(filename):
      filename = joiner(WORKDIR, self.current_filename)

    return filename

  def handle(self, key='q', filename=None, toc_key='~'):
    filename = self.current_filename if not filename else filename

    if key == toc_key:
      return get_daftar(self.normalize(filename)) # butuh .mk

    res = get_entries(filename, key + '/')
    return res

  def entry_for_line(self, baris):
    if baris[0] in need_escape:
      baris = '\\' + baris
    definisi = get_definition(self.filepath, start_regex=f'^--% {baris}')
    # print('code entry for', baris, '=', definisi)
    return definisi

"""
usef@kali:~/danger/ulib/schnell$ python -m'app.codehandler'
['q/tujuan', 'q/info/struktur', 'q/info/backend', 'q/info/web', 'q/info/mobile', 'q/info/edge', 'q/info/sensor', 'q/fm.us']
"""
if __name__ == '__main__':
  res = get_entries('project-iot')
  print(res)
  print()
  print(FILENAMES)
