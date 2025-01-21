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

from schnell.app.transpiler.zgenerate.refactor.handlers import for_traditional
from schnell.app.transpiler.zgenerate.refactor.handlers import for_each
from schnell.app.transpiler.zgenerate.refactor.handlers import for_in
from schnell.app.transpiler.zgenerate.refactor.handlers import for_of

def for_variation(tree, language='py'):
  kembali = ''

  varian = child1(tree)
  if data(varian) == 'for_traditional':
    # hasil = for_traditional(varian)
    # output += hasil
    kembali = for_traditional.for_traditional(varian, language=language)
  elif data(varian) == 'for_each':
    kembali = for_each.for_each(varian, language=language)
  elif data(varian) == 'for_in':
    kembali = for_in.for_in(varian, language=language)
  elif data(varian) == 'for_of':
    kembali = for_of.for_of(varian, language=language)
  else:
    kembali = ''
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
