from app.libpohon.columnify import (
  columnify_and_transform,
  transform_columns,
  columnify,
)
from app.libpohon.app_content import app_content
from app.libpohon.app_content_model import app_content as app_content_model
from app.stringutils import tabify_content, tabify_contentlist, tab_tab, tab_space2, tab_space4
from app.treeutils import tables_from_rootnode
# from app.usutils import tab, tab_tab
from app.fileutils import (
  file_content,
  append_entry_tostring,
  # append_entry_tofile,
  file_write,
)
from app.dirutils import (
  get_cwd, 
  joiner, 
  here,
)
from app.fileutils import get_definition_by_key_permissive_start
from app.fmus import Fmus


disini = here(__file__)


class Coordinator:

  def __init__(self, RootNode, project_dir='__INPUT__'):
    self.root = RootNode
    self.tables = tables_from_rootnode(self.root)
    self.project_dir = project_dir
    self.mkfile_input = joiner(disini, 'index-input.mk')
    self.mkfile_output = joiner(get_cwd(), 'index.mk')
    self.mkfile_input_content = file_content(self.mkfile_input)
    self.node_app_content = file_content(joiner(disini, 'appcontent.tpl'))

  def output(self):
    return self.mkfile_output

  def change_projectdir(self):
    self.mkfile_input_content = self.mkfile_input_content.replace('__REPLACE_WITH_PROJECT_DIR_OR_INPUT__', self.project_dir)

  def db_init(self):
    from app.libpohon.db_init import db_init
    template_db_init = db_init(self.root)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_DB_INIT', template_db_init)

  def app_init(self):
    from app.libpohon.app_init import app_init
    template_app_init = app_init(self.tables)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)

  def app_content(self):    
    template_node_app_content = app_content(self.tables, self.node_app_content, tab=tab_tab)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_CONTENT', template_node_app_content)

  def mkfile(self):
    self.change_projectdir()
    self.db_init()
    self.app_init()
    self.app_content()
    print('hasil mkfile:', self.mkfile_output)

  def model(self):
    for tbl in self.tables:
      tablename = tbl.model
      tablename_lower = tbl.model.lower()
      # create
      header = f'/{tablename_lower}/create'
      per_table = '// ini isi create'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # list
      header = f'/{tablename_lower}/list'
      per_table = '// ini isi list'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # detail
      header = f'/{tablename_lower}/detail'
      per_table = '// ini isi detail'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # update
      header = f'/{tablename_lower}/update'
      per_table = '// ini isi update'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # delete
      header = f'/{tablename_lower}/delete'
      per_table = '// ini isi delete'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
    print('hasil model:', self.mkfile_output)

  def save_file(self):
    file_write(self.mkfile_output, self.mkfile_input_content)
    print('hasil save file:', self.mkfile_output)

  def after_model(self):
    # __TEMPLATE_APP_IMPORTS
    # __TEMPLATE_APP_ROUTES
    appimports = []
    approutes = []
    approutessidebar = []
    for tbl in self.tables:
      tablename = tbl.model
      tablename_lower = tbl.model.lower()
      # import ProductCreate from './apps/product/create.js'
      appimports.append(f"import {tablename}Create from './apps/{tablename_lower}/create'")
      appimports.append(f"import {tablename}List from './apps/{tablename_lower}/list'")
      appimports.append(f"import {tablename}Detail from './apps/{tablename_lower}/detail'")
      appimports.append(f"import {tablename}Update from './apps/{tablename_lower}/update'")
      appimports.append(f"import {tablename}Delete from './apps/{tablename_lower}/delete'")

      # {{ path: "/product/create", name: "Create", icon: "ni ni-circle-08 text-pink", component: ProductCreate, layout: "/admin", }},
      approutes.append(f'{{ path: "/{tablename_lower}/create", name: "Create", icon: "ni ni-circle-08 text-pink", component: {tablename}Create, layout: "/admin", }},')
      # {{ path: "/product/list", name: "List", icon: "ni ni-circle-08 text-pink", component: ProductList, layout: "/admin", }},
      approutes.append(f'{{ path: "/{tablename_lower}/list", name: "List", icon: "ni ni-circle-08 text-pink", component: {tablename}List, layout: "/admin", }},')
      # {{ path: "/product/:id", name: "Detail", icon: "ni ni-circle-08 text-pink", component: ProductDetail, layout: "/admin", }},
      approutes.append(f'{{ path: "/{tablename_lower}/:id", name: "Detail", icon: "ni ni-circle-08 text-pink", component: {tablename}Detail, layout: "/admin", }},')
      # {{ path: "/product/:id/edit", name: "Update", icon: "ni ni-circle-08 text-pink", component: ProductUpdate, layout: "/admin", }},
      approutes.append(f'{{ path: "/{tablename_lower}/:id/edit", name: "Update", icon: "ni ni-circle-08 text-pink", component: {tablename}Update, layout: "/admin", }},')
      # {{ path: "/product/:id/delete", name: "Delete", icon: "ni ni-circle-08 text-pink", component: ProductDelete, layout: "/admin", }},
      approutes.append(f'{{ path: "/{tablename_lower}/:id/delete", name: "Delete", icon: "ni ni-circle-08 text-pink", component: {tablename}Delete, layout: "/admin", }},')

      approutessidebar.append(app_content_model(tablename, file_content(joiner(disini, 'sidebarroute.tpl'))))

    appimportslines = '\n'.join(appimports)
    # approuteslines = '\n'.join(approutes)
    approuteslines = tabify_contentlist(approutes, self_tab=tab_tab, num_tab=1)
    approutessidebarlines = tabify_contentlist(approutessidebar, self_tab=tab_tab, num_tab=1)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_IMPORTS', appimportslines)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_ROUTES', approuteslines)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_SIDEBAR_ROUTES', approutessidebarlines)

  def generate(self):
    self.mkfile()
    self.model()
    self.after_model()
    self.save_file()
    print('selesai generate routes')
