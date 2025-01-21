import os
from schnell.app.printutils import indah0
from schnell.app.utils import trycopy


# elif item.type == 'komentar_untuk_instruksi_selanjutnya':
def komentar_untuk_instruksi_selanjutnya(item):
  '''ini dari #(file=baris)
  item.content adlh hasil get definition di BaseDefinitor
  '''
  indah0(item.content, warna='white', newline=True)
  trycopy(item.content)

  sumber = '...press Return '
  baris = ''
  if hasattr(item, 'source'):
    namafile = os.path.basename(item.source)
    if hasattr(item, 'baris'):
      baris = '|' + item.baris
    sumber = f'[{namafile}{baris}] '

  input(f'{sumber}>> ')
