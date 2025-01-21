from schnell.app.autoutils import alert
from schnell.app.fmusutils import replace_from_configuration_new_replacer_input_if_input
from schnell.app.notifutils import notifpy, pynotif
from schnell.app.printutils import indah4
# from .common import input_keyword
# from rich.pretty import pprint


def pesan_instruksi(item, self_run_configuration=None, is_debugging=0):
  """
  .,d
    %NAME=__INPUT__
    @your name is NAME*
  ini jadi 2 kali diminta input...
  padahal harusnya bisa peroleh dari sibling...
  """
  root_tree = item.parent
  pesan = item.content

  if is_debugging:
    indah4(f"""[pesan_instruksi]
      pesan = {pesan}
      item = {item}
      root_tree = {root_tree}
      """, warna='green')

  # replace __PWD dst
  if hasattr(item, 'replacer'):
    for k,v in item.replacer.items():
      # if not k.startswith('ULIBPY_'):
      #   indah4(f'[pesan_instruksi] replacing {k} with {v}', warna='cyan')
      pesan = pesan.replace(k, str(v))

  pesan = pesan.replace('__WORKDIR__', item.workdir)

  # if input_keyword in item.content \
  #   and hasattr(root_tree, 'variables'):
  #   pengganti = ''
  #   for k,v in root_tree.variables.items():
  #     if k in item.original:
  #       pengganti = v
  #   if pengganti:
  #     pesan = pesan.replace(input_keyword, pengganti)
  #     indah4(f'''[pesan_instruksi]
  #     replacing "{input_keyword}" pada item.content=pesan dg "{pengganti}"
  #     ''', warna='cyan')
  if hasattr(root_tree, 'variables'):
    for kunci, nilai in root_tree.variables.items():
      if kunci in item.content:
        # indah4(f"replacing [{kunci}] with [{nilai}] in [{pesan}]", warna='white', layar='red')
        pesan = pesan.replace(kunci, nilai)

  # ini bermasalah, jika value diberikan oleh sibling
  pesan = replace_from_configuration_new_replacer_input_if_input(
    self_run_configuration, pesan, item.original, pengirim='pesan_instruksi')
  # fungsi utama adlh menampilkan, sebaiknya kita ubah ke notify
  if not hasattr(item, 'forced_entry') or not item.forced_entry:
    alert(body=f'{pesan}\n\nPress any Enter to continue...', header='pesan_instruksi')
  else:
    notifpy(judul='pesan_instruksi', pesan=pesan)
  # indah4(pesan, warna='yellow', layar='blue')
  # # jk tdk diakhiri dg *, maka sebaiknya gunakan message alert
  # sumber = '...(press Return to continue) '
  # # sumber = f'...selesai oprek [{item}], press Return utk keluar...'
  # if hasattr(item, 'source'):
  #   sumber = f'[{item.source}] '
  # # if hasattr(item, 'forced_entry') and not item.forced_entry:
  # # if not hasattr(item, 'forced_entry'):
  # paksa = False
  # if hasattr(item, 'forced_entry') and item.forced_entry:
  #   paksa = True
  # if not paksa:
  #   indah0(f'{sumber}', warna='blue', layar='white', bold=True, blink=True)
  #   input('>> ')
