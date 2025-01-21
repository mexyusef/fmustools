import os
from schnell.app.utils import (
	trycopy,
	trypaste,
)


# elif oper == 'paste_from_clipboard_with_pause':
def paste_from_clipboard_with_pause(item, self_debug, pause=True):
  """
  somefile.txt,f(c=)
  """
  if pause:
    input(f'Siapkan untuk exec item [{item}] content clipboard utk dimasukkan ke file [{item.workdir}].\n\n')
  content = trypaste()
  if content:
    with open(item.workdir, 'w', encoding='utf8') as fd:
      fd.write(content)

    self_debug(os.listdir(os.path.dirname(item.workdir)))  # workdir adlh file
