from .printutils import indah0
from .utils import yesno
from .fileutils import (
  file_lines,
)
from .dirutils import (
  ayah, joiner, abs_dir, here
)
import os, re

TEMPLATE = """
--%
.,d(/mk)
\t%src=__FILE__
  #(src=701)
  #(src=702)
  #(src=703)
--#
--% 701
something
--#
--% 702
something
--#
--% 703
something
--#

butuh flashcard_name, n_start, n_stop
"""
PROGRAM = """--% program/main/fm.us
.,d
\t%src=__FILE__

__TABBED_ENTRIES

--#

"""

# TAB_ENTRY = """\t#(src=__BILANGAN)\n"""
TAB_ENTRY = """\t@(src=__BILANGAN)\n"""

ENTRY = """--% __BILANGAN
__ACTOR
--#

"""

from schnell.app.appconfig import programming_data
ACTORFILE = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_ACTORFILE"] # '/home/usef/danger/ulib/upy/ulibpy/compete/actor.txt'
# GENERATED_DIR = joiner(abs_dir(__file__), 'codes', 'additional', 'misc', 'generated')
# if 'ULIBPY_WMC_GENDIR' in os.environ:
# 	GENERATED_DIR = os.environ.get('ULIBPY_WMC_GENDIR')
GENERATED_DIR = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_GENDIR"]


class FlashCard:
  def __init__(self, filename, start, stop):
    self.start = start
    self.stop = stop
    self.filename = filename
    # .gitignore
    # self.basedir = joiner(ayah(__file__, 1), 'codes', 'additional', 'misc', 'generated')
    self.actorlines = file_lines(ACTORFILE)

  @property
  def basedir(self):
    return GENERATED_DIR

  @staticmethod
  def ask():
    text = 'Masukan filename,start,stop (default 0-999)'
    done = False
    filename = None
    start = 0
    end = 999
    while not done:
      indah0(text, warna='bright_green')
      terima = input('>> ')
      if not ',' in terima:
        filename = terima
        # print(terima)
      else:
        m = re.match(r'^\s*([A-Za-z0-9 \-_\.]+)\s*,\s*([\d]+)\s*(,\s*([\d]+))?', terima)
        if m:
          filename = m.group(1)
          start = int(m.group(2))
          end = int(m.group(4))
          print(m.groups())

      if filename:
        if yesno(f'Puas dengan file={filename}, start={start}, end={end}? y[n]'):
          done = True
        else:
          filename = None
          start = 0
          end = 999

    print(filename, start, end)
    return filename, start, end

  def create_tabbed_entries(self):
    tabbed_entries = ''
    for counter in range(self.start, self.stop+1):
      entry = TAB_ENTRY.replace('__BILANGAN', str(counter).zfill(3))
      tabbed_entries += entry

    return tabbed_entries

  def create_program(self):
    tabbed_entries = self.create_tabbed_entries()
    header = PROGRAM.replace('__TABBED_ENTRIES', tabbed_entries)
    return header

  def generate(self, basedir=None):
    # basedir = GENERATED_DIR # self.basedir if not basedir else basedir
    self.filename = self.filename+'.mk' if not self.filename.endswith('.mk') else self.filename
    filepath = joiner(GENERATED_DIR, self.filename)
    with open(filepath, 'w') as fd:
      header = self.create_program()
      fd.write(header)
      for counter in range(self.start, self.stop+1):
        entry = ENTRY.replace('__BILANGAN', str(counter).zfill(3)).replace('__ACTOR', self.actorlines[counter])
        fd.write(entry)


if __name__ == '__main__':
  filename, start, end = FlashCard.ask()
  if filename and (start >=0 ) and (end >= 0):
    FlashCard(filename, start, end).generate()
