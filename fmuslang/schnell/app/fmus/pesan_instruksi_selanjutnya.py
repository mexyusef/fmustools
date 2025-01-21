import os
from schnell.app.printutils import indah
# from schnell.app.utils import trycopy



def pesan_instruksi_selanjutnya(item):
  '''dari @(file=baris)
  '''
  indah(item.content, width=0, warna='yellow', layar='white', bold=True, newline=True)

  sumber = '...press Return '
  baris = ''
  if hasattr(item, 'source'):
    namafile = os.path.basename(item.source)
    if hasattr(item, 'baris'):
      baris = '|' + item.baris
    sumber = f'[{namafile}{baris}] '
  # if hasattr(item, 'forced_entry') and not item.forced_entry:
  paksa = False
  if hasattr(item, 'forced_entry') and item.forced_entry:
    paksa = True
  if not paksa:
    input(f'{sumber}>> ')
