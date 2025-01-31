from schnell.app.treeutils import (
  data, 
  token, 
  child1, 
  child2, 
  child3, 
  child4,
  child,
  chdata,
  chtoken,
  anak, 
  ispohon, istoken,
  beranak,
  sebanyak,
  jumlahanak, 
)

from schnell.app.transpiler.zgenerate.refactor.handlers import tipe_identifier
from schnell.app.transpiler.zgenerate.refactor.handlers import tipe_identifier_array

def nama_jenis_identifier(tree, language='py'):
  kembali = ''

  idnama, idjenis = '', ''
  for item in anak(tree):
    if data(item) == 'nama_identifier':
      idnama = token(item)
    elif data(item) == 'tipe_identifier':
      idjenis = tipe_identifier.tipe_identifier(item, language=language)
      # print('nama jenis identifier, jenis:', idjenis)
    elif data(item) == 'array':
      idjenis = tipe_identifier_array.tipe_identifier_array(item, language=language)

  kembali = f'{idnama}: {idjenis}'
  
  if language == 'py':
    pass
  elif language == 'ts':
    pass
  elif language == 'rs':
    pass
  elif language == 'java':
    pass
  elif language == 'kt':
    pass
  elif language == 'go':
    pass
  elif language == 'rb':
    pass
  elif language == 'v':
    pass
  elif language == 'dart':
    pass
  elif language == 'cpp':
    pass
  elif language == 'cs':
    pass
  elif language == 'hs':
    pass
  elif language == 'clj':
    pass
  elif language == 'scala':
    pass
  elif language == 'php':
    pass
  elif language == 'swift':
    pass
  elif language == 'elixir':
    pass
  elif language == 'erlang':
    pass
  return kembali
