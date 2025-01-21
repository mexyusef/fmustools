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


from schnell.app.transpiler.zgenerate.refactor.handlers import literal_bool
from schnell.app.transpiler.zgenerate.refactor.handlers import literal_char
from schnell.app.transpiler.zgenerate.refactor.handlers import literal_dict
from schnell.app.transpiler.zgenerate.refactor.handlers import literal_list
from schnell.app.transpiler.zgenerate.refactor.handlers import literal_number
from schnell.app.transpiler.zgenerate.refactor.handlers import literal_string
from schnell.app.transpiler.zgenerate.refactor.handlers import template_string

def literal(tree, language='py'):
  kembali = ''
  print('literal')
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'literal_string':
      kembali += literal_string.literal_string(item, language=language)
    elif jenis == 'literal_char':
      kembali += literal_char.literal_char(item, language=language)
    elif jenis == 'literal_number':
      kembali += literal_number.literal_number(item, language=language)
    elif jenis == 'literal_list':
      hasil_list = literal_list.literal_list(item, language=language)
      kembali += str(hasil_list).replace("'",'')
    elif jenis == 'literal_dict':
      kembali += literal_dict.literal_dict(item, language=language)
    elif jenis == 'template_string':
      kembali += template_string.template_string(item, language=language)
    elif jenis .startswith('boolean'):
      kembali += literal_bool.literal_bool(item, language=language)

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
