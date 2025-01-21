from app.fileutils import (
  file_copy,
  replace_entry,
  get_definition_by_key_permissive_start,
  replace_string_in_entry,
)
from .common import program_config, disini


def process_routes_after_sidebar_menu():
  filepath = frontend_config['routes_file']
  baris = frontend_config['routes_entry']
  content = get_definition_by_key_permissive_start(filepath, baris)
  if content:
    frontend_config['routes'] = content

def process_sidebar():
  template = program_config['fe']
  filepath = joiner(disini, f'{template}/sidebar.mk')
  baris = '/react-light/src/components/Sidebar/Sidebar.js'
  content = get_definition_by_key_permissive_start(filepath, baris)
  if content:
    frontend_config['sidebar'] = content

  process_routes_after_sidebar_menu()



def process_menu_item(item, group):
  # global frontend_config
  component_path = f'{group}-{item["name"]}'
  # frontend_config['user-components'].add(component_path)
  frontend_config['user-components'].append(component_path)
  kembali = f'{{ title:"{item["name"]}", path:"{component_path}", icon: <IoIcons.IoIosPaper /> }}'
  return kembali

def process_group(item):
  nama = item["name"]
  kembali = '{'
  kembali += f'title:"{item["name"]}", path:"{item["name"]}", '
  kembali += """
  icon: <AiIcons.AiFillHome />,
  iconClosed: <RiIcons.RiArrowDownSFill />,
  iconOpened: <RiIcons.RiArrowUpSFill />,
  """  
  items = [process_menu_item(anak, nama) for anak in item['children']]
  if items:
    kembali += 'subNav: ['+', '.join(items)+']'
  kembali += '\n}'
  return kembali

def process_section(item):
  kembali = ''
  kembali += f'const {item["name"]} = ['
  groups = [process_group(anak) for anak in item['children']]
  if groups:
    kembali += ', '.join(groups)
  kembali += '\n]'
  return kembali

def menu_calls(items):
  a = map(lambda i: f"<SidebarBottom judul='{i['name']}' data={{{i['name']}}}/>", items)
  b = list(a)
  c = '\n<hr className="my-4 md:min-w-full" />\n'.join(b)
  return c

def create_menu(items):
  """
  """
  calls = menu_calls(items)
  # print('calls:')
  # print(calls)
  sections = []
  for item in items:
    section = process_section(item)
    # print('section:')
    # print(section)
    sections.append(section)
  return calls, sections
