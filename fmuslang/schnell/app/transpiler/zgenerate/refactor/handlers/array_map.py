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

from schnell.app.transpiler.zgenerate.refactor.handlers import anonymous_function

def array_map(tree, language='py'):
  kembali = ''

  kembali = ''
  for item in anak(tree):
    if data(item) == 'anonymous_function':
      kembali = anonymous_function.anonymous_function(item, language=language)
  # return kembali

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
