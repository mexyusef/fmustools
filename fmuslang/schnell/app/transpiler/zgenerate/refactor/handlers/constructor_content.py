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

from schnell.app.transpiler.zgenerate.refactor.handlers import function_param
from schnell.app.transpiler.zgenerate.refactor.handlers import function_content
from schnell.app.transpiler.zgenerate.refactor.handlers.common import inc, dec, tabify_content

def constructor_content(tree, structname=None, language='py'):
  kembali = ''

  ctorparam, ctorcontent = '',''
  for item in anak(tree):
    if data(item) == 'constructor_config':
      pass
    if data(item) == 'function_param':
      ctorparam = function_param.function_param(item, language=language)
    if data(item) == 'function_content':
      # kok bisa ada 2 kembalian?
      # C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\handlers\function_content.py
      ctorcontent, jumlah_statement = function_content.function_content(item, language=language)
      if not jumlah_statement:
        ctorcontent = '{}'
      else:
        inc()
        # @my{>(){?+satu}}
        kiri = '{\n'
        kanan = '\n}'
        ctorcontent = kiri + tabify_content(ctorcontent) + kanan
        dec()

  kembali = f'{structname}{ctorparam} {ctorcontent}'
  inc()
  kembali = tabify_content(kembali)
  dec()
  
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
