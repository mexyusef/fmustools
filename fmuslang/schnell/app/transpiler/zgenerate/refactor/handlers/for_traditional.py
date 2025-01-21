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

from schnell.app.transpiler.zgenerate.refactor.handlers import for_start
from schnell.app.transpiler.zgenerate.refactor.handlers import for_end
from schnell.app.transpiler.zgenerate.refactor.handlers import for_step

def for_traditional(tree, language='py'):
  kembali = ''

  keyname, forstart, forend, forstep = '','','',''
  for item in anak(tree):
    if data(item) == 'for_start':
      keyname, forstart = for_start.for_start(item, language=language)
    elif data(item) == 'for_end':
      forend = for_end.for_end(item, language=language)
    elif data(item) == 'for_step':
      forstep = for_step.for_step(item, language=language)
  kembali += f'(let {keyname}={forstart}; {forend}; {forstep})'

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
