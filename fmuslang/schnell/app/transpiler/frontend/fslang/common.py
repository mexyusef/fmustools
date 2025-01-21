from app.dirutils import (
  joiner, ayah
)
from app.utils import env_int
from app.printutils import print_json

program_config = {
  'config': {
	  'fe': 'react-light',
  }
}

disini = joiner(ayah(__file__,1))
# original_frontend_config = {
def original_frontend_config():
  if env_int('ULIBPY_FMUS_DEBUG')>1:
    '''
    spy gak diexec setiap kali
    from app.transpiler.frontend.fullstack import process_language
    '''
    print('common/original_frontend_config => FE sekarang:', program_config["config"]["fe"])
    print_json(program_config)
  return {
  'filepath': joiner(disini, f'{program_config["config"]["fe"]}/index.mk'),
  # 'filepath-input': joiner(disini, f'{program_config["config"]["fe"]}/index-input.mk'),
  'baris_entry': 'index/fmus',

  'sidebar': '',
  # 'sidebartpl': '__TEMPLATE_SIDEBAR',

  'header': '',
  'header_left': [],
  'header_right': [],
  # 'headertpl': '__TEMPLATE_HEADER',
  'header_file': joiner(disini, f'{program_config["config"]["fe"]}/header.mk'),
  'header_file-input': joiner(disini, f'{program_config["config"]["fe"]}/header-input.mk'),
  'header_entry': '/react-light/src/components/Navbars/AdminNavbar.js',

  'sidebar_file': joiner(disini, f'{program_config["config"]["fe"]}/sidebar.mk'),
  'sidebar_file-input': joiner(disini, f'{program_config["config"]["fe"]}/sidebar-input.mk'),
  'sidebar_entry': '/react-light/src/components/Sidebar/Sidebar.js',

  'content': '',
  'content_rows': [],
  'content_file': joiner(disini, f'{program_config["config"]["fe"]}/dashboard.mk'),
  'content_file-input': joiner(disini, f'{program_config["config"]["fe"]}/dashboard-input.mk'),
  'content_entry': '/react-light/src/views/Dashboard.js',

  'footer': '',
  'footer_items': [],
  'footer_copyright': '',
  'footer_file': joiner(disini, f'{program_config["config"]["fe"]}/footer.mk'),
  'footer_file-input': joiner(disini, f'{program_config["config"]["fe"]}/footer-input.mk'),
  'footer_entry': '/react-light/src/components/Footer/Footer.js',

  'rightbar': '',
  'rightbar_file': joiner(disini, f'{program_config["config"]["fe"]}/layout.mk'),
  'rightbar_file-input': joiner(disini, f'{program_config["config"]["fe"]}/layout-input.mk'),
  'rightbar_entry': '/react-light/src/layouts/Admin.js',

  'floating': '',
  # 'floatingtpl': '__TEMPLATE_FLOATING',

  # 'user-components': set(),
  'user-components': list(),
  'routes': '',
  'routes_file': joiner(disini, f'{program_config["config"]["fe"]}/user-components.mk'),
  'routes_file-input': joiner(disini, f'{program_config["config"]["fe"]}/user-components-input.mk'),
  'routes_entry': '/react-light/src/routes.js',
  }
