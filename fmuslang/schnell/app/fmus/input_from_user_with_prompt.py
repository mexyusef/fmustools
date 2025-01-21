import os
from schnell.app.fmusutils import get_input_from_user_gui


# elif oper == 'input_from_user_with_prompt':
def input_from_user_with_prompt(item, self_debug):
  """
  somefile.txt,f(i=)
  """
  # terima = ''
  isifile = get_input_from_user_gui()
  # self_debug(f"Masukkan isi file [{item.workdir}] dan akhiri dengan one line of dot")
  # while terima != '.':
  #   terima = input("  .. ")
  #   if terima != '.':
  #     isifile += terima + "\n"
  if isifile:
    with open(item.workdir, 'w', encoding='utf8') as fd:
      fd.write(isifile)

  self_debug(os.listdir(os.path.dirname(item.workdir))) # workdir adlh file
