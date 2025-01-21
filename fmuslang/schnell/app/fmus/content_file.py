# import os
from schnell.app.treeutils import get_all_parent_variables, item_workdir_has_input, replace_if_input_and_parent_is_dir
from schnell.app.printutils import indah4
from schnell.app.fileutils import file_write
from schnell.app.utils import env_int
from schnell.app.stringutils import sanitize_chars
from schnell.app.fmusutils import get_input_generic_if_input_not_from_template


# | "n"	"="	ISI_CONTENT_FILE_BISA_URL		-> content_file
def content_file(oper, item, root_tree, self_run_configuration=None):
  content = oper.split('=', 1) [1]

  content = sanitize_chars(content)
  # cek jk ada input tapi bukan dari template
  # workdir diminta input duluan dibanding content, jangan kebolak
  item.workdir = get_input_generic_if_input_not_from_template(item.workdir, item.parent, 'content_file')
  content = get_input_generic_if_input_not_from_template(content, item.parent, 'content_file')

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f'[content_file] content utk {item.workdir}: {content}')

  # proses replacer biar bisa masukkan __FILE, __IF_ETH0 dst
  if hasattr(item, 'replacer'):
    for k,v in item.replacer.items():
      content = content.replace(k, str(v))

  if root_tree is not None and hasattr(root_tree, 'variables'):
    for k,v in root_tree.variables.items():
      content = content.replace(k, v)
      if env_int('ULIBPY_FMUS_DEBUG')>1:
        print(f"[content_file] replacing {k} with {v} in {content}.")

  # cek __INPUT__ di workdir
  node_variables = get_all_parent_variables(item, {})
  filepath = item.workdir
  if item_workdir_has_input(item):    
    filepath = replace_if_input_and_parent_is_dir(item)

  write_mode = 'w' if not hasattr(item, 'appending_mode') else 'a'
  file_write(filepath, content, write_mode)

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    # workdir adlh file
    indah4('[content_file] END.')
