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

from schnell.app.transpiler.zgenerate.refactor.handlers import tipe_identifier_array
from schnell.app.transpiler.zgenerate.refactor.handlers import object_type
from schnell.app.transpiler.zgenerate.refactor.handlers.common import peta_tipe_data

def tipe_data_semua(tree, language='py'):
  kembali = ''

  for item in anak(tree):
    if data(item) == 'array':
      kembali = tipe_identifier_array.tipe_identifier_array(item, language=language)
    elif data(item) == 'object_type':
      kembali = object_type.object_type(item, language=language)
    else:
      jenis = data(item)
      kembali = peta_tipe_data[language].get(jenis, jenis)
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
