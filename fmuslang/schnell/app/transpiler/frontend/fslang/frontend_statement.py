from pprint import pprint as pp
import copy
from schnell.app.printutils import print_json
from schnell.app.dirutils import joiner, ayah
from schnell.app.fileutils import (
  file_copy,
  replace_entry,
  get_definition_by_key_permissive_start,
  replace_string_in_entry,
)
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

# from schnell.app.stringutils import tabify_content
from schnell.app.usutils import tab, append_entry, tabify_contentlist
from schnell.app.usutils import tab

from .common import original_frontend_config, disini
from .sidebar import process_sidebar, create_menu
from .header import process_header, header_left, header_right, header_title, header_search, header_account, header_logout, header_dropdown_badge, header_dropdown_color
from .content import process_content, create_dashboard
from .footer import process_footer, footer_copyright, footer_item, footer_list
from .rightbar import process_rightbar, process_floating

"""
sidebar
header
  drop1
  drop2
  searchbar
  profile
  title
content
footer
  copyright
  link1
  link2
  ...
-rightbar
floating
"""


def element_children(tree):
  """
  element_children
    program_frontend
      declarative_element
        element_name        search
      declarative_element
        element_name        drop1
      declarative_element
        element_name        drop2
      declarative_element
        element_name        profile
  """
  kembali = ''
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'program_frontend':
      kembali = program_frontend(item)
    elif jenis == '':
      pass
    elif jenis == '':
      pass
  # kembali += f''
  return kembali # program_frontend

def element_name(tree):
  kembali = token(tree)
  return kembali

def declarative_element(tree):
  """
  kembalian adlh dict
  """
  kembali = {
    'name': '',
    'children': '',
    'config': '',
  }

  for item in anak(tree):
    jenis = data(item)
    if jenis == 'element_name':
      kembali ['name'] = element_name(item)
    elif jenis == 'element_children':
      kembali ['children'] = element_children(item)
    elif jenis == 'element_config':
      pass
    elif jenis == 'cdata_text':
      pass
  # kembali += f''
  return kembali

def program_frontend(tree):
  """
  list of decl elemnets
  """
  kembali = []
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'declarative_element':
      res = declarative_element(item) # dict
      kembali.append(res) # list of dicts

  return kembali

# frontend_config = copy.copy(original_frontend_config)
# frontend_config = original_frontend_config
frontend_config = {}

def salin():
  global frontend_config
  frontend_config = copy.copy(original_frontend_config())

salin()


def frontend_process(program, level=0, parent=''):
  """
  utk menu kita perkenalkan
  section
    group
      item
  """
  for item in program:
    nama = item['name']
    print(f'{tab(level)}process:', item['name'], 'level:', level)
    # proses parent utk letakkan placeholder
    if level == 1:
      if item['name'] == 'sidebar':
        process_sidebar()
      if item['name'] == 'header':
        process_header()
      if item['name'] == 'content':
        process_content()
      if item['name'] == 'footer':
        process_footer()
      if item['name'] == 'rightbar':
        process_rightbar()
      if item['name'] == 'floating':
        process_floating()
    # proses anak utk mengisi placeholder
    # proses anak header
    elif level == 2:
      if parent == 'header':
        # __TEMPLATE_NAV_ITEMS_LEFT
        # __TEMPLATE_NAV_ITEMS_RIGHT
        if nama == 'left':
          print(f'\t* left = mr-auto')
          tmp = frontend_config['header'].replace('__TEMPLATE_NAV_ITEMS_LEFT', header_left)
          frontend_config['header'] = tmp
        elif nama == 'right':
          print(f'\t* right = ml-auto')
          tmp = frontend_config['header'].replace('__TEMPLATE_NAV_ITEMS_RIGHT', header_right)
          frontend_config['header'] = tmp

      elif parent == 'sidebar':
        if nama == 'menu':
          '''
          process: menu level: 2
            process: section1 level: 3
              process: group1 level: 4
                process: item1 level: 5
                process: item2 level: 5
            process: section2 level: 3
              process: group5 level: 4
                process: item5 level: 5
                process: item6 level: 5
          '''
          print('oprek menu')
          # print_json(item['children'])
          calls, declares = create_menu(item['children'])
          if calls and declares:
            declarations = '\n'.join(declares)
            tmp = frontend_config['sidebar'] \
              .replace('__TEMPLATE_MENU_DECLARE', declarations) \
              .replace('__TEMPLATE_MENU_CALL', calls)
            frontend_config['sidebar'] = tmp

      elif parent == 'content':
        '''
        process: layout level: 0
          process: content level: 1
            process: row level: 2
              process: col6 level: 3
                process: item1 level: 4
              process: col6 level: 3
                process: item2 level: 4
            process: row level: 2
              process: col12 level: 3
                process: item3 level: 4
        '''
        print('content:')
        print_json(item)

        # rows = []
        if nama == 'row':
          result = create_dashboard(item['children'])
          frontend_config['content_rows'].append(result)

      elif parent == 'footer':
        print('footer:')
        print_json(item)
        if nama == 'copy':
          frontend_config['footer_copyright'] = footer_copyright
        else:
          barang = footer_item.replace('__TITLE__', nama)
          frontend_config['footer_items'].append(barang)

    elif level == 3:
      # which = '__TEMPLATE_HEADER_LEFT_CONTENT' if parent=='left' else '__TEMPLATE_HEADER_RIGHT_CONTENT'
      which = 'left' if parent=='left' else 'right'
      if nama == 'title':
        # tmp = frontend_config['header'].replace(which, header_title+'\n'+which)
        # frontend_config['header'] = tmp
        print('***              appending title, coba hitung aku berapa kali muncul')
        print('                 btw, nilai header L/R yg sudah ada:')
        print_json(frontend_config[f'header_{which}'])
        frontend_config[f'header_{which}'].append(header_title)
      elif nama == 'search':
        # tmp = frontend_config['header'].replace(which, header_search+'\n'+which)
        # frontend_config['header'] = tmp
        frontend_config[f'header_{which}'].append(header_search)
      elif nama == 'account':
        # tmp = frontend_config['header'].replace(which, header_account+'\n'+which)
        # frontend_config['header'] = tmp
        frontend_config[f'header_{which}'].append(header_account)
      elif nama == 'logout':
        # tmp = frontend_config['header'].replace(which, header_logout+'\n'+which)
        # frontend_config['header'] = tmp
        frontend_config[f'header_{which}'].append(header_logout)
      elif nama == 'drop1':
        # tmp = frontend_config['header'].replace(which, header_dropdown_badge+'\n'+which)
        # frontend_config['header'] = tmp
        frontend_config[f'header_{which}'].append(header_dropdown_badge)
      elif nama == 'drop2':
        # tmp = frontend_config['header'].replace(which, header_dropdown_color+'\n'+which)
        # frontend_config['header'] = tmp
        frontend_config[f'header_{which}'].append(header_dropdown_color)

    if item['children']:
      frontend_process(item['children'], level+1, parent=item['name'])

# F<<layout(header(drop,profile),sidebar(menu(level1a(level2a,level2b),level1b)))>>
# F<<layout(header(drop,profile),sidebar(menu(level1a(level2a,level2b),level1b)),content,footer)>>
# F<<layout(header(drop,profile),sidebar(menu(level1a(level2a,level2b),level1b)),content,footer,floating)>>

def frontend_header():
  global frontend_config
  if frontend_config['header_left'] or frontend_config['header_right']:
    # global frontend_config
    if frontend_config['header_left']:
      kiri = '\n'.join(frontend_config['header_left'])
      # print('nilai kiri adlh:')
      # print(kiri)
      # print('nilai header __TEMPLATE_HEADER_LEFT_CONTENT yg mau diganti adlh adlh:')
      # print(frontend_config['header'])
      # input('...lanjut...#3')
      tmp = frontend_config['header'].replace('__TEMPLATE_HEADER_LEFT_CONTENT', kiri)
      frontend_config['header'] = tmp
      # print('nilai header stlh kiri adlh:')
      # print(frontend_config['header'])
      # input('...lanjut...#2')

    if frontend_config['header_right']:
      kanan = '\n'.join(frontend_config['header_right'])
      # print('nilai kanan adlh:')
      # print(kanan)
      tmp = frontend_config['header'].replace('__TEMPLATE_HEADER_RIGHT_CONTENT', kanan)
      frontend_config['header'] = tmp
      # print('nilai header stlh kanan adlh:')
      # print(frontend_config['header'])
      # input('...lanjut...#3')
    
    replace_entry(frontend_config['header_file'], frontend_config['header_entry'], frontend_config['header'])
    # print('ini sblm header, header/left, header/right dikosongkan')
    frontend_config['header'] = ''
    frontend_config['header_left'] = []
    frontend_config['header_right'] = []
    # print('header')
    # print_json(frontend_config[f'header'])
    # print('left')
    # print_json(frontend_config[f'header_left'])
    # print('right')
    # print_json(frontend_config[f'header_right'])
    # input('harusnya di atas jadi kosong...')


def frontend_sidebar():
  global frontend_config
  if frontend_config['sidebar']:
    replace_entry(frontend_config['sidebar_file'], frontend_config['sidebar_entry'], frontend_config['sidebar'])
    frontend_config['sidebar'] = ''


def normalize_component_to_file(item):
  return item.capitalize().replace('-','_')


def frontend_create_views_components(items):
  # replace_entry(frontend_config['routes_file'], frontend_config['routes_entry'], tmp2)
  indexfmus = '.,d\n'
  # namafile.js,f(e=__FILE__=namafile.js)
  def barisentry(item):
    return 'component-create' if item.lower().endswith('create') else 'component-list'
  # entries = [f'{normalize_component_to_file(item)}.js,f(e=__FILE__={normalize_component_to_file(item)}.js)' for item in items]
  entries = [f'{normalize_component_to_file(item)}.js,f(e=__FILE__={barisentry(item)})' for item in items]
  indexfmus += tabify_contentlist(entries) + '\n'
  replace_entry(frontend_config['routes_file'], 'index/fmus', indexfmus)


def frontend_routes():
  global frontend_config

  if frontend_config['user-components']:
    # import Upgrade from "views/Upgrade.js";
    imports = [f'import {normalize_component_to_file(item)} from "views/{normalize_component_to_file(item)}.js";' for item in frontend_config['user-components']]
    imports = '\n'.join(imports)
    tmp = frontend_config['routes'].replace('__TEMPLATE_ROUTES_IMPORT', imports)
    # f'{ path: "/{item}", name: "Notifications", icon: "nc-icon nc-bell-55", component: {normalize_component_to_file(item)}, layout: "/admin", },'
    routes = [f'{{ path: "/{item}", name: "{normalize_component_to_file(item)}", icon: "nc-icon nc-bell-55", component: {normalize_component_to_file(item)}, layout: "/admin", }},' for item in frontend_config['user-components']]
    routes = '\n'.join(routes)
    tmp2 = tmp.replace('__TEMPLATE_ROUTES_USE', routes)
    # frontend_config['routes'] = tmp2
    replace_entry(frontend_config['routes_file'], frontend_config['routes_entry'], tmp2)
    frontend_config['routes'] = ''
    # buat user-components.mk/index/fmus
    frontend_create_views_components(frontend_config['user-components'])
    frontend_config['user-components'] = []


def frontend_content():
  global frontend_config
  if frontend_config['content_rows']:
    result = '\n\n'.join(frontend_config['content_rows'])
    tmp = frontend_config['content'] \
      .replace('__TEMPLATE_CONTENT_DASHBOARD', result)
    frontend_config['content'] = tmp
    replace_entry(frontend_config['content_file'], frontend_config['content_entry'], frontend_config['content'])
    frontend_config['content'] = ''
    frontend_config['content_rows'] = []


def frontend_footer():
  global frontend_config
  if frontend_config['footer_items'] or frontend_config['footer_copyright']:
    footer = ''
    if frontend_config['footer_copyright']:
      footer += frontend_config['footer_copyright']
    if frontend_config['footer_items']:
      result = '\n\n'.join(frontend_config['footer_items'])
      footer += footer_list.replace('__ITEMS__', result)

    tmp = frontend_config['footer'] \
      .replace('__TEMPLATE_FOOTER_ITEMS', footer)
    frontend_config['footer'] = tmp
    replace_entry(frontend_config['footer_file'], frontend_config['footer_entry'], frontend_config['footer'])
    frontend_config['footer'] = ''
    frontend_config['footer_copyright'] = ''
    frontend_config['footer_items'] = []


def frontend_rightbar():
  """
  layout.mk => /react-light/src/layouts/Admin.js
  __TEMPLATE_RIGHTBAR
  diganti dg:
  rightbar.mk => index/fmus
  """
  global frontend_config
  if frontend_config['rightbar']:
    # replace_entry(frontend_config['rightbar_file'], frontend_config['rightbar_entry'], tmp)
    replace_string_in_entry(frontend_config['rightbar_file'], frontend_config['rightbar_entry'], '__TEMPLATE_RIGHTBAR', frontend_config['rightbar'])
    frontend_config['rightbar'] = ''
    # frontend_config['content_rows'] = []


def frontend_initialize():
  global frontend_config
  # sblm process header, buat baru dulu file header.mk
  frontend_config = original_frontend_config()
  # salin()
  file_copy(frontend_config['header_file-input'], frontend_config['header_file'])
  file_copy(frontend_config['sidebar_file-input'], frontend_config['sidebar_file'])
  file_copy(frontend_config['routes_file-input'], frontend_config['routes_file'])
  file_copy(frontend_config['content_file-input'], frontend_config['content_file'])
  file_copy(frontend_config['footer_file-input'], frontend_config['footer_file'])
  file_copy(frontend_config['rightbar_file-input'], frontend_config['rightbar_file'])


def frontend_statement(tree):
  # global frontend_config
  print('frontend_statement:', data(tree))
  kembali = ''
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'program_frontend':
      kembali = program_frontend(item)
    elif jenis == '':
      pass

  frontend_initialize()

  frontend_process(kembali)

  # print('header kiri adlh:', frontend_config['header_left'], 'sepanjang:', len(frontend_config['header_left']))
  # print('header kanan adlh sepanjang:', len(frontend_config['header_right']))
  # pp(frontend_config['header_right'])
  # print('sblm oprek kiri dan kanan, HEADER adlh')
  # print(frontend_config['header'])
  # input('...lanjut...')
  # stlh proses cek jk header ada, sidebar ada, dst. maka replace dulu sblm fmus exec
  frontend_header()

  frontend_sidebar()

  frontend_routes()

  frontend_content()

  frontend_footer()

  frontend_rightbar()

  print('frontend_statement => final result:')
  print_json(frontend_config)
  return frontend_config
