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

from schnell.app.transpiler.zgenerate.common import typescript_enum_info
from schnell.app.transpiler.zgenerate.refactor.handlers import enum_body
from schnell.app.transpiler.zgenerate.refactor.handlers.common import inc, dec

def enum_declaration(tree, language='py'):
  kembali = ''

  nama_enum, isi_enum = '', ''
  for item in anak(tree):
    if data(item) == 'nama_identifier':
      nama_enum = token(item).capitalize()
    elif data(item) == 'enum_body':
      inc()
      isi_enum = enum_body.enum_body(item, language=language)
      dec()

  
  hasil = typescript_enum_info
  hasil = ['// ' + item for item in hasil.splitlines()]
  hasil = '\n'.join(hasil) + '\n'
  hasil += f'enum {nama_enum} {{\n{isi_enum}\n}}'
  kembali += hasil

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
