from app.libpohon.columnify import (
  columnify_and_transform,
  transform_columns,
  columnify,
)
from app.stringutils import tabify_content_tab, tabify_content, tabify_contentlist, tab_tab, tab_space2, tab_space4
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
    self.provider = 'react_bootstrap_form1'
    self.hasil_columnify = columnify(self.tables, self.provider, skip_columns={})

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
    self.mkfile_input_content = self.mkfile_input_content.replace('__NILAI_CLIENT_PORT__', self.root.clientport)

  def app_content(self):
    from app.libpohon.app_content import app_content
    template_node_app_content = app_content(self.tables, self.node_app_content, tab=tab_tab)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_CONTENT', template_node_app_content)

  def mkfile(self):
    self.change_projectdir()
    self.db_init()
    self.app_init()
    self.app_content()
    print('hasil mkfile:', self.mkfile_output)

  def model(self):
    from app.libpohon import acfile, acmfile
    for tbl in self.tables:
      tablename = tbl.model
      tablename_lower = tbl.model.lower()
      # create
      header = f'/{tablename_lower}/create'
      per_table = acmfile(tablename, disini, 'app_create.tpl')
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # list
      header = f'/{tablename_lower}/list'
      per_table = acmfile(tablename, disini, 'app_list.tpl')
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # item
      header = f'/{tablename_lower}/item'
      per_table = acmfile(tablename, disini, 'app_item.tpl')
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # detail
      header = f'/{tablename_lower}/detail'
      per_table = acmfile(tablename, disini, 'app_detail.tpl')
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # update
      header = f'/{tablename_lower}/update'
      per_table = acmfile(tablename, disini, 'app_update.tpl')
      per_table = self.generate_fields(per_table, tablename, '__FIELDS__')
      cari_lokasi_states = '__TEMPLATE_USESTATES' # utk useState's
      per_table = per_table.replace(cari_lokasi_states, self.generate_usestates(tablename))
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
      # delete
      header = f'/{tablename_lower}/delete'
      per_table = acmfile(tablename, disini, 'app_delete.tpl')
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content, header, per_table)
    print('hasil model:', self.mkfile_output)

  # per_table = self.generate_fields(per_table, '__FIELDS__')
  def generate_fields(self, per_table, tablename, field_keyword='__FIELDS__'):    
    generated_fields = columnify_and_transform(self.tables, self.provider, tablename)
    generated_fields = tabify_content_tab(generated_fields, num_tab=2)
    # input(f"\n\nHasil tabify utk form adlh: [{generated_fields}]")
    return per_table.replace(field_keyword, generated_fields)

  def generate_usestates(self, tablename):
    states = []
    # table_info = self.hasil_columnify[tablename]['columns_names']
    # for idx,col in enumerate(table_info):
    #   pass
    for i,tbl in enumerate(self.tables):
      if tbl.model == tablename:
        for j,col in enumerate(tbl.children):
          if col.type not in ['django_foreign_key', 'django_one_to_one', 'auto']:
            nilai_awal = '""'
            if col.type == 'boolean':
              nilai_awal = 'false'
            elif col.type in ['auto', 'bigint', 'decimal', 'double', 'float', 'integer', 'number']:
              nilai_awal = 0
            bentuk = f"const [{col.label}, set{col.label[0].upper()+col.label[1:]}] = useState({nilai_awal})"
            states.append(bentuk)
    return tabify_content_tab('\n'.join(states))

  def save_file(self):
    file_write(self.mkfile_output, self.mkfile_input_content)
    print('hasil save file:', self.mkfile_output)

  def after_model(self):
    # __TEMPLATE_APP_IMPORTS
    # __TEMPLATE_APP_ROUTES
    appimports = []
    approutes = []
    for tbl in self.tables:
      tablename = tbl.model
      tablename_lower = tbl.model.lower()
      # import ProductCreate from './apps/product/create.js'
      appimports.append(f"import {tablename}Create from './apps/{tablename_lower}/create'")
      appimports.append(f"import {tablename}List from './apps/{tablename_lower}/list'")
      appimports.append(f"import {tablename}Item from './apps/{tablename_lower}/item'")
      appimports.append(f"import {tablename}Detail from './apps/{tablename_lower}/detail'")
      appimports.append(f"import {tablename}Update from './apps/{tablename_lower}/update'")
      appimports.append(f"import {tablename}Delete from './apps/{tablename_lower}/delete'")

      # <Route path='/admin/product/create' component={ProductCreate} />
      approutes.append(f"<Route path='/admin/{tablename_lower}/create' component={{{tablename}Create}} />")
      # <Route path='/admin/product/list' component={ProductList} />
      approutes.append(f"<Route path='/admin/{tablename_lower}/list' component={{{tablename}List}} />")
      approutes.append(f"<Route path='/admin/{tablename_lower}/item' component={{{tablename}Item}} />")
      # <Route path='/admin/product/:id/edit' component={ProductUpdate} />
      approutes.append(f"<Route path='/admin/{tablename_lower}/:id/edit' component={{{tablename}Update}} />")
      # <Route path='/admin/product/:id/delete' component={ProductDelete} />
      approutes.append(f"<Route path='/admin/{tablename_lower}/:id/delete' component={{{tablename}Delete}} />")
      # ini memakan edit dan delete, jd hrs paling bawah
      # <Route path='/product/:id' component={ProductDetail} />
      # approutes.append(f"<Route path='/admin/{tablename_lower}/:id' component={{{tablename}Detail}} />")
      approutes.append(f"<Route path='/{tablename_lower}/:id?' component={{{tablename}Detail}} />")
      approutes.append('\n') # pemisah

    appimportslines = '\n'.join(appimports)
    # approuteslines = '\n'.join(approutes)
    approuteslines = tabify_contentlist(approutes, self_tab=tab_tab, num_tab=5)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_IMPORTS', appimportslines)
    self.mkfile_input_content = self.mkfile_input_content.replace('__TEMPLATE_APP_ROUTES', approuteslines)

  def generate(self):
    self.mkfile()
    self.model()
    self.after_model()
    self.save_file()
    print('selesai generate routes')
