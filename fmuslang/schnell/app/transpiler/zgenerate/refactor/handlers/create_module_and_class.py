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

from schnell.app.transpiler.zgenerate.refactor.handlers.common import inc, dec, tabify_content

def create_module_and_class(ifacename, ifacecontent, language='py'):
  kembali = ''

  kembali = f'interface {ifacename} {{\n'
  inc()
  kembali += tabify_content(ifacecontent)
  dec()
  kembali += '\n}'
  
  kembali += '\n'*3

  kembali += f'type {ifacename} = {{\n'
  inc()
  kembali += tabify_content(ifacecontent)
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
