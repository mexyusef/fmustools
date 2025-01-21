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

from schnell.app.transpiler.zgenerate.refactor.handlers import condition_while
from schnell.app.transpiler.zgenerate.refactor.handlers import condition_body
from schnell.app.transpiler.zgenerate.refactor.handlers.common import inc, dec, tabify_content

def while_statement(tree, language='py'):
  kembali = ''

  wconfig = ''
  wheader, wbody = '', ''
  for item in anak(tree):
    if data(item) == 'while_keyword':
      pass
    elif data(item) == 'while_config':
      pass
    elif data(item) == 'condition_while':
      wheader = condition_while.condition_while(item, language=language)
    elif data(item) == 'condition_body':
      wbody = condition_body.condition_body(item, language=language)
  kembali += f'while ({wheader}) {{\n'
  inc()
  kembali += tabify_content(wbody)
  dec()
  kembali += '\n}'

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
