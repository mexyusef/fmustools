from schnell.app.dirutils import (
  joiner,
  only_files,
  files_noext,
  files_noext_filter_by_ext,
)
from schnell.app.fileutils import (
	get_daftar,
	get_definition_by_key_permissive_start,
	get_definition_by_key_permissive_start_with_lineno,
  mkfile_to_dict,
)
from schnell.app.stringutils import (
  list_startswith,
  list_contains,
  list_stringify,
  gabung_kunci,
)
from schnell.app.utils import (
  env_expand,
  env_get,
)
# from .general import mapper


class FastMapper:
  def __init__(self):
    self.bylangs = env_get('ULIBPY_BYLANGSDIR')
    self.mapperdir = joiner(self.bylangs, 'mapper')
    self.general = joiner(self.mapperdir, 'general.mk')
    self.mapper = mkfile_to_dict(self.general)
    self.current_choice = self.general

  def reload(self):
    self.mapper = mkfile_to_dict(self.current_choice)

  def edit(self):
    from schnell.app.utils import perintah
    perintah(f"code {self.mapperdir}")

  def toc(self):
    return gabung_kunci(self.mapper) # '\n'.join(self.mapper.keys())

  def files(self):
    the_list = files_noext_filter_by_ext(self.mapperdir)
    return list_stringify(the_list) # '\n'.join(files_noext_filter_by_ext(self.mapperdir))

  def load(self, filename):
    print('loading mk file:', filename)
    if filename in files_noext_filter_by_ext(self.mapperdir):
      self.current_choice = joiner(self.mapperdir, filename+'.mk')
      self.mapper = mkfile_to_dict(self.current_choice)      

  def process(self, code):
    result = self.mapper.get(code, '').strip()
    print(f"\n...mapping {code} into [{result}]\n")
    if not result:
      '''
      kita pengen kembalikan list yg match...
      1) dimulai dg code
      2) code ada di item list
      '''
      # the_list = list_startswith(self.mapper.keys(), code)
      # return list_stringify(the_list)
      meta_input = list_startswith(self.mapper.keys(), code)
      print('meta_input adlh:', meta_input)
      return result, meta_input
        
    return result, None

fast_mapper = FastMapper()
