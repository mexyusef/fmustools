import os
from os import sep, walk
from os.path import basename, isdir

from .appconfig import programming_data
from .fileutils import file_content, append_file, write_file
from .mediautils import get_stringified_image_asb64
from .printutils import Debug
from .utils import trycopy, env_exist, env_get


FIRST_ENTRY=programming_data['j']['schnell']['app']["reversefm"]["ULIBPY_WMC_ROOTENTRYNAME"] # 'index/fmus'
# if env_exist('ULIBPY_WMC_ROOTENTRYNAME'):
#   FIRST_ENTRY=env_get('ULIBPY_WMC_ROOTENTRYNAME')
TAB = '\t' # configurable ke space2, space4
TEXTCHARS = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})

skip_dirs = ['node_modules', '__pycache__', 'build', 'target', '.git', 'dist', 'bin']
skip_extension = ['.o', '.bin', '.out']
skip_files = ['package-lock.json', 'yarn.lock', 'yarn-error.log', '.DS_Store']

if programming_data['j']['schnell']['app']["reversefm"]["ULBPY_WMC_SKIPDIRS"]:
  skip_dirs = [item.strip() for item in programming_data['j']['schnell']['app']["reversefm"]["ULBPY_WMC_SKIPDIRS"].split(',')]
  skip_extension = [item.strip() for item in programming_data['j']['schnell']['app']["reversefm"]["ULBPY_WMC_SKIPEXTS"].split(',')]
  skip_files = [item.strip() for item in programming_data['j']['schnell']['app']["reversefm"]["ULBPY_WMC_SKIPFILES"].split(',')]

class ReverseFM:

  def __init__(self, basedir=None, debug=True):
    if basedir:
      self.basedir = basedir
    self.content = {}
    self.debug = Debug(debug)
    self.projectname = None # kita samakan dg nama root dir yg mau diambil
    self.copy_after_generate = False # jangan, bisa jadi fmus file sangat besar

  def print(self, value, key=FIRST_ENTRY):
    if not key in self.content:
      self.content[key] = [value]
    else:
      self.content[key].append(value)

  def is_binary(self, bytes):
    return bool(bytes.translate(None, TEXTCHARS))

  def is_file_binary(self, filepath):
    baca = open(filepath, 'rb').read(1024)
    return self.is_binary(baca)

  def dir_entry(self, indent, root):
    """
    perlu handle @namadir hrs jadi __AT__namadir
    lihat app.fmus.processor:542 yg panggil app.fmus.helper.decode_filename
    yg panggil app.stringutils.sanitize_chars
    """
    namadir = basename(root)
    # if namadir.startswith('@'):
    #   namadir = namadir.replace('@','__AT__',1)
    if '@' in namadir or '[' in namadir or ']' in namadir:
      namadir = namadir.replace('@','__AT__').replace('[','__LK__').replace(']','__RK__')
    cetak = '%s%s,d(/mk)'%(indent, namadir)
    self.print(cetak)

  def entrify(self, key):
    """
    self.content[header]=body
    """
    lines = self.content[key]
    # stringified = '\n'.join(lines)
    stringified = '\n'.join(lines).rstrip() # hapus whitespaces di akhir file
    header = '--% ' + key
    footer = '--#'
    text = f"{header}\n{stringified}\n{footer}\n\n"
    return text

  def file_entry(self, subindent, filename, fullpath, basedir):
    relative = os.path.relpath(fullpath, basedir)
    # pastikan \ menjadi /
    relative = relative.replace('\\', '/')
    relative = self.projectname + '/' + relative
    biner = self.is_file_binary(fullpath)
    text_binary = 'b64' if biner else 'e'
    filerepr = f'{filename},f({text_binary}=__FILE__={relative})'
    cetak = "%s%s" % (subindent, filerepr)
    self.print(cetak)
    if biner:
      nilai = get_stringified_image_asb64(fullpath)
    else:
      nilai = file_content(fullpath)
    self.content[relative] = [nilai]

  def projectdir(self, root):
    """
    utk root, kita kasih __PWD, shg output ke current working directory, bukan ke schnell/**
    """
    # self.dir_entry('', '__PWD/' + root)
    self.dir_entry('', root)
    self.projectname = root
    # rootvars = f"{TAB}%utama=__FILE__"
    # self.print(rootvars)

  def walk(self, startpath=None, skip_dirs=skip_dirs, skip_files=skip_files, skip_ext=skip_extension):
    """
    for root, subdirs, files in walk(startpath) if ...:
    https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
    """
    startpath = self.basedir if not startpath else startpath

    for root, subdirs, files in walk(startpath, topdown=True):
      subdirs[:] = [d for d in subdirs if d not in skip_dirs]
      # files = [os.path.join(root, f) for f in files if not f.endswith('.txt')]
      # files = [f for f in files if not [ext for ext in skip_ext if f.endswith(ext)]]
      files = [f for f in files if (not (f in skip_files) and not ([ext for ext in skip_ext if f.endswith(ext)]))]
      level = root.replace(startpath, '').count(sep)
      if level == 0:
        # root adlh basename utk nama root/base folder
        self.projectdir(root)
      else:
        indent = TAB * (level)
        self.dir_entry(indent, root)
      subindent = TAB * (level+1)
      for f in files:
        fullpath = os.path.join(root, f)
        self.file_entry(subindent, f, fullpath, startpath)

  def generate(self, target_filepath=None):
    # for k,v in self.content.items():
    for k in self.content.keys():
      entry = self.entrify(k)
      if target_filepath:
        append_file(target_filepath, entry)
      else:
        print(entry)

  def walkgen(self, choosedir, target_filepath):
    # self.debug('walkgen #START\n')
    self.walk(startpath=choosedir)
    self.generate(target_filepath)
    if self.copy_after_generate:
      trycopy(file_content(target_filepath))
      print(f'Content {target_filepath} copied...')

  def tree(self, startpath=None, print_files=True):
    startpath = self.basedir if not startpath else startpath
    for root, subdirs, files in walk(startpath):
      level = root.replace(startpath, '').count(sep)
      indent = '  |' * (level-1) + '  \- ' if root != startpath else ''
      cetak = '%s%s/'%(indent, basename(root))
      print(cetak)
      if print_files:
        subindent = '  |' * (level) + '  +- '
        for f in files:
          cetak = "%s%s" % (subindent, f)
          print(cetak)

if __name__ == '__main__':
  path = input('Masukkan path folder: ')
  if not path:
    path = '/tmp/hapus/go-backend'
  rev = ReverseFM(path)
  rev.walk()
  rev.generate('/tmp/hapus/generated.mk')
