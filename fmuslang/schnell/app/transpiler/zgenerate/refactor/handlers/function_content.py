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


from schnell.app.transpiler.zgenerate.refactor.handlers import functioncontentlist
from schnell.app.transpiler.zgenerate.refactor.handlers.common import self_tab

def function_content(tree, language='py'):
  print('function_content')
  kembali = ''
  empty_content = f'{self_tab()}// pass'
  if beranak(tree):
    # functioncontentlist
    _functioncontentlist = child1(tree)
    hasil = functioncontentlist.functioncontentlist(_functioncontentlist, language=language)
    if hasil:
      kembali += hasil
    else:
      kembali += empty_content
  else:
    kembali += empty_content

  # C:\Users\usef\work\sidoarjo\schnell\app\transpiler\zgenerate\refactor\handlers\constructor_content.py
  # minta 2 kembalian dg jumlah statement utk tabify content
  if language == 'py':
    pass
  elif language == 'ts':
    kembali = kembali, 1
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
