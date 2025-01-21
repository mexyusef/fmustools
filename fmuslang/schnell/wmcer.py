import argparse, os, sys, pathlib

current_file = pathlib.Path(__file__).resolve()
schnelldir = current_file.parent
sidoarjodir = str(schnelldir.parent)
schnelldir = str(schnelldir)
disini = os.path.dirname(__file__)

envfile = os.path.join(disini, '.env')
# perlu cek jk envfile not isfile
if not os.path.isfile(envfile):
  print(f'{envfile} not found')
  if sys.platform == 'win32':
    envfile = 'C:/work/ulibs/schnell/.env'
  else:
    envfile = '/home/usef/work/ulibs/schnell/.env'
  print(f'using {envfile}')

sys.path.insert(0, sidoarjodir)

from dotenv import load_dotenv
load_dotenv(envfile)

if 'ULIBPY_BASEDIR' not in os.environ:
  print("""
  'ULIBPY_BASEDIR' not in os.environ
  perlu utk akses library fmus.
  """)
  sys.exit(0)

# sblm import fmusutils dll, pastikan programming_data sudah terinit
from startup import initialize_programming_data
initialize_programming_data()

from schnell.app.appconfig import programming_data
from schnell.app.dirutils import isfile, absolutify, isdir, make_folder, chdir
from schnell.app.fileutils import file_content, handle_content_start_end
from schnell.app.fmus import Fmus
from schnell.app.fmusutils import run_fmus_for_content
from schnell.app.printutils import indah4
from schnell.app.utils import trypaste, env_int, tidur

parser = argparse.ArgumentParser(description="FMUS executor")
group = parser.add_mutually_exclusive_group()
# https://stackoverflow.com/questions/39092149/argparse-how-to-make-mutually-exclusive-arguments-optional/39092229
# group.add_argument("file", nargs=1, help="File fmus")
group.add_argument("file", nargs='?', help="File fmus")
group.add_argument("--exec", "-e", help="Execute code")

parser.add_argument("--outputfolder", "-o", help="Output folder", default=os.getcwd())
parser.add_argument("--baris", "-b", help="Baris entry", default='index/fmus')
parser.add_argument("--mkfile", "-m", help="Proses sebagai MK file, bukan US/entry file", action="store_true")

args = parser.parse_args()

content = None
filepath = None

os.environ['ULIBPY__PWD__'] = os.getcwd()

def expand_path(filepath):
  # print('old filepath:', filepath)
  if 'ULIBPY' in filepath:
    from schnell.app.utils import env_replace_filepath
    filepath = env_replace_filepath(filepath, normalize=True)
    # print('new filepath:', filepath)
  return filepath

if args.file:
  # u file.us
  # print('args file:', args.file)
  if isinstance(args.file, list):
    if isfile(args.file[0]):
      filepath = args.file[0]
      # filepath = expand_path(filepath)
      content = file_content(filepath)
  else:
    if 'ULIBPY' in args.file:
      filepath = expand_path(args.file)
      if isfile(filepath):
        content = file_content(filepath)
      else:
        print(f'{filepath} not found')
    elif isfile(args.file):
      filepath = args.file
      # filepath = expand_path(filepath)
      content = file_content(filepath)
    else:
      print(f'{args.file} not found')
  # print('[wmcer:content#0a]', content)
elif args.exec:
  content = args.exec
  # utk /quick-command, skip converting, krn bisa jadi c:\path\to\folder\name\tfilename.txt
  if not content.startswith('/'):
    content = content.replace('\\n', '\n').replace('\\t', '\t')
  # print('[wmcer:content#0b]', content)
  os.chdir(os.getcwd())
  # print(f"""args.exec: [{content}]""")
else:
  content = trypaste()
  # print('[wmcer:content#0c]', content)
  indah4(f'[{args.outputfolder}] clipboard: [{content[:500]}...]', warna='yellow')

# print('[wmcer:content#1]', content)
content = handle_content_start_end(content)
if content and not content.endswith('\n'):
  content += '\n'

# # jika quick command, maka escape \n \r \t
# if content.startswith('/'):
#   # content = content.replace('\n', '\\n').replace('\t', '\\t')
#   content = content.replace('\\', '/')
# print('[wmcer:content#2]', content)

if content:
  fmus = Fmus(programming_data['debug'])
  if filepath:
    # kita absolute kan filepath agar tidak ./config.js, ./input.txt dst.
    # kasus: jk WM -m ../program.us, di sini dir filepath berbeda dg os.getcwd()
    # jadi harus bisa: __FILE dan __CURDIR berbeda
    # set_file_dir_template(self, file_template, dir_template=None) di fmus.py
    filepath = absolutify(filepath)
    fmus.set_file_dir_template(filepath, os.getcwd())
    # if args.outputfolder:
    #   '''
    #   sayangnya ini gak berhasil
    #   output selalu sama dg lokasi file MK
    #   mungkin krn kita gak chdir dulu ke sini
    #   '''
    #   fmus.set_dir_template(args.outputfolder)
    #   print('__CURDIR di:', args.outputfolder)
    if args.mkfile:
      # print('Memilih proses MK/FMUS file, baris entry adlh', args.baris)
      # kita specify dir_template krn bisa beda dir dari file_template dg PWD/CWD
      fmus.process_mkfile(filepath, args.baris, os.getcwd())
    else:
      # print(f"""[wmcer:fmus.process(content)] filepath, !args.mkfile
      # content = [{content}]
      # """)
      fmus.process(content)
  else:
    # indah4(f"""{content}""", warna='magenta')
    if args.exec:
      # print(f"""[wmcer:fmus.process(content)] args.exec
      # content = [{content}]
      # """)
      fmus.set_dir_template(args.outputfolder)
      fmus.process(content)
    else:
      confirm = env_int('ULIBPY_CONFIRM_CLIPBOARD_EXECUTION')
      if confirm:
        yesno = input('Press [y] jk pengen execute clipboard: ')
      if not confirm or yesno == 'y':
        # input('running from clipboard ')
        # fmus.set_dir_template(args.outputfolder)
        # fmus.process(content)
        run_fmus_for_content(content, dirpath=args.outputfolder, start_fresh=True)

# percobaan cukup dg ls
# alias WM="python /home/usef/work/ulibs/schnell/wmcer.py"
# alias WM="python C:\work\ulibs\schnell\wmcer.py"
# python C:\work\ulibs\schnell\wmcer.py .\next-ts2.mk -m  -> utk mkfile + index/fmus
# python C:\work\ulibs\schnell\wmcer.py .\next-ts2.mk   -> utk file berisi content baris_entry
