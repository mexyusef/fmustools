# from .common import Common, input_keyword
# from schnell.app.dirutils import (
# 	abs_dir,
# 	ayah, bongkar,
# 	create_dir,
# 	find_patterns,
# 	here,
# 	isdir, isfile,
# 	doesexist,
# 	joiner,
# 	normy,	
# 	tempdir, 
#   file_under_tempdir,
# 	exists_in_dir,
# )
from schnell.app.fileutils import (
  check_replace_if_contain_links,
  write_file,
	# replace_from, 
	# replace_at, 
	# insert_after, 
	# insert_before, 
	# remove_lines,
	# replace_entry,
	# replace_between,
	# replace_string_in_file,
	# tab_to_space_start,
)
from schnell.app.printutils import (
  indah, indah0, indah4,
)
from schnell.app.utils import (
	trycopy,
	trypaste,
	yesno,
	env_get, env_int,
	env_exist,
	env_expand,
	# perintahsp_outerr,
	perintahsp_outerr_as_shell,
)
from schnell.app.fmusutils import replace_from_configuration_replacer


def write_file_with_variable_expansion(
  self_debug,
  self_run_configuration,
  filepath,
  write_mode,
  content,
  dictionary=None
  ):
  """
  sekarang belum distandardkan name2 variables yg diizinkan
  pengennya: __TEMPLATE_STR1, __TEMPLATE_STR2, __TEMPLATE_NUM1, __TEMPLATE_NUM2, dst.

  update:
  kita tambah bisa tulis file spt
  web/src/pages/post/[id].tsx
  utk handle next.js
  err, no: kita handle di namafile utk "e" di grammar
  """
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah0(f"[write_file_with_variable_expansion] Memasukkan kode di bawah diapit <<...>> ke {filepath}:\n", warna='green', newline=True)
    # ini hanya dipake wkt nulis .fmus atau .mk file
    # jk nulis file biasa (js, txt, dll) gak ada guna
    content = check_replace_if_contain_links(content)
    indah0(f"<<{content[:100]}>>", warna='white', bold=True, newline=True)

  if dictionary:
    for k,v in dictionary.items():
      '''
      TODO:
      cek apa ini perlu prefix? bukannya skrg sudah non prefix?
      '''
      # if (k.startswith('TEMPLATE') or k.startswith('__TEMPLATE') or k.startswith('__TPL')) and (k in content):
      if k in content:
        content = content.replace(k, v)

  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f"[write_file_with_variable_expansion][{filepath}] content sblm replacer config: [{content[:100]}]\n", warna='green', layar='black')

  # for k,v in self_run_configuration['replacer'].items():
  #   content = content.replace(k, v)
  content = replace_from_configuration_replacer(content, self_run_configuration['replacer'])
  
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    indah4(f"[write_file_with_variable_expansion][{filepath}] content stlh replacer config: [{content[:100]}]\n", warna='green', layar='black')

  # with open(filepath, write_mode) as fd:
  #   fd.write(content)
  write_file(filepath, content, write_mode)
