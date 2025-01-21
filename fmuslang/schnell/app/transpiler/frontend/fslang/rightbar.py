from app.fileutils import (
  file_copy,
  replace_entry,
  get_definition_by_key_permissive_start,
  replace_string_in_entry,
)
from .common import program_config, disini

def process_rightbar():
  """
  hasil bacanya akan masuk 'rightbar' yg akan dimasukkan ke layout.mk/Admin.js
  mereplace TEMPLATE_RIGHTBAR
  """
  template = program_config['fe']
  filepath = joiner(disini, f'{template}/rightbar.mk')
  baris = 'index/fmus'
  content = get_definition_by_key_permissive_start(filepath, baris)
  if content:
    frontend_config['rightbar'] = content


def process_floating():
  template = program_config['fe']
  filepath = joiner(disini, f'{template}/floating.mk')
  baris = 'index/fmus'
  content = get_definition_by_key_permissive_start(filepath, baris)
  if content:
    frontend_config['floating'] = content

