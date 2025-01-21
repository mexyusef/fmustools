import json, pprint
# from db.bantuan.common import (
# 	# append_entry,
# 	tab,
# )
from app.usutils import tab
from app.fileutils import (
  file_content,
  append_entry_tostring,
  append_entry_tofile,
)
from .createform import create_form
from .updateform import update_form
from .formlist import form_list
from .formmodal import form_modal
from .formprovider import form_provider
from .formwrapper import form_wrapper
from .model import form_model

from .menujson import menu_json, menu_item_template
from .approutes import app_route_item, app_routes

# import { 
#   Button, 
#   Col, 
#   DatePicker,
# https://ant.design/components/date-picker/
# https://ant.design/components/time-picker/
#   Form, 
# https://ant.design/components/form/
#   Input, 
# https://ant.design/components/input/
#   InputNumber,
#   Modal,
#   Radio,
# https://ant.design/components/radio/
# https://ant.design/components/checkbox/
#   Row,
#   Select,
# https://ant.design/components/select/
#   Switch,
# https://ant.design/components/switch/
# } from 'antd';
# https://ant.design/components/rate/
# https://ant.design/components/slider/
# https://ant.design/components/transfer/
# https://ant.design/components/cascader/

text_input = """
<Form.Item name='__ITEM_NAME_LOWER' label="__ITEM_NAME_TITLED">
  <Input />
</Form.Item>
"""

textarea_input = """
<Form.Item name='__ITEM_NAME_LOWER' label="__ITEM_NAME_TITLED">
  <Input.TextArea rows={4} />
</Form.Item>
"""

# https://ant.design/components/input-number/
# float: https://stackoverflow.com/questions/58943805/how-to-limit-the-input-number-to-max-of-two-decimals-with-ant-design
text_input_number = """
<Form.Item name='__ITEM_NAME_LOWER' label="__ITEM_NAME_TITLED">
  <InputNumber />
</Form.Item>
"""

text_input_number_float = """
<Form.Item name='__ITEM_NAME_LOWER' label="__ITEM_NAME_TITLED">
  <InputNumber />
</Form.Item>
"""

text_input_date = """
<Form.Item name='__ITEM_NAME_LOWER' label="__ITEM_NAME_TITLED">
  <DatePicker />
</Form.Item>
"""

text_input_date_time = """
<Form.Item name='__ITEM_NAME_LOWER' label="__ITEM_NAME_TITLED">
  <DatePicker showTime />
</Form.Item>
"""

# ini belum memasukkan default
select_option = lambda title, data: f"""
<Form.Item name='{title.lower()}' label='{title.replace('_', ' ').title()}'>
  <Select>
  {{
    {[item.replace('$$$','') for item in data]}.map((item, index) => {{
      return <Select.Option key={{index}} value={{item}}>{{item}}</Select.Option>
    }})
  }}
  </Select>
</Form.Item> 
"""

model_item_to_form_item = {
  'array_of':     textarea_input,
  'empty_array':  textarea_input,
	'bigint':       text_input,
	'boolean':      text_input,
	'date':         text_input_date,
  'decimal':      text_input,
	'double':       text_input,
	'enum':         text_input,
	'float':        text_input,
  'image':        text_input,
	'integer':      text_input_number,
	'number':       text_input_number,
	'string':       text_input,
	'text':       	text_input,

  'timestamp':    text_input_date_time,
	'uuid':       	text_input,
	'uuid1':       	text_input,
	'uuid4':       	text_input,
	'varchar':      text_input,

  # 'django_foreign_key':			  '{ type: mongoose.Schema.ObjectId, ref: ModelRujukan, required: true, }',
  # 'django_foreign_key':			  '{ type: STRING, allowNull: false, references: "ModelRujukan", }',
  # 'django_many_to_many':		  '[{ type: String }]',	
  'auto':         text_input,
	'slug':         text_input,
}


class AntdModel:


  def __init__(self, configuration, mkfile_input_content):
    # self.configuration = {
    #   'table_nodes': tables,
    #   'root_node': RootNode,
    # }
    self.configuration = configuration
    self.mkfile_input_content = mkfile_input_content


  def generate_createform(self):
    """
    createform dan updateform berisi form items spt Input, Input.TextArea dan InputNumber
    templatenya di model_item_to_form_item
    utk kolom yg berisi values dan default -> enum diterjemahkan ke Select/Option
    jadi utk enum:
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      for colidx, column in enumerate(tbl.children):
        column hasattr: values dan optionally default

    di sini kita iterate lewat self.configuration['models'] yg hanya berisi label+type
    """
    # form __TEMPLATE_FORM_ITEM_LIST
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      form_items = []
      # for model_item in self.configuration['models'][tbl.model]:
      #   item = model_item_to_form_item[model_item['type']]
      #   item = item.replace('__ITEM_NAME_LOWER', model_item['name'].lower())
      #   item = item.replace('__ITEM_NAME_TITLED', model_item['name'].title())
      #   form_items.append(item)
      for colidx, column in enumerate(tbl.children):
        if column.type in ['django_foreign_key', 'django_one_to_one', 'django_one_to_many', 'django_many_to_many']:
          continue
        # select_option
        if hasattr(column, 'values'):
          # belum masukkan default di sini
          item = select_option(column.label, column.values)
        else:
          item = model_item_to_form_item[column.type]
          item = item.replace('__ITEM_NAME_LOWER', column.label.lower())
          item = item.replace('__ITEM_NAME_TITLED', column.label.title())

        form_items.append(item)

      form_item_delim = '\n\n'
      __TEMPLATE_FORM_ITEM_LIST = form_item_delim.join(form_items)
      content = create_form.replace('__TEMPLATE_FORM_ITEM_LIST', __TEMPLATE_FORM_ITEM_LIST)
      # header = f'/np/node-postgres/src/apps/{tbl.model.lower()}/models/postgres.js'
      header = f'/np/react-antd/components/modules/{tbl.model}/CreateForm.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_formprovider(self):
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      content = form_provider.replace('__TEMPLATE_modelname', tbl.model.lower())
      header = f'/np/react-antd/components/modules/{tbl.model}/FormProvider.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_formwrapper(self):
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      content = form_wrapper
      header = f'/np/react-antd/components/modules/{tbl.model}/FormWrapper.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_formlist(self):
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      content = form_list.replace('__TEMPLATE_modelname', tbl.model.lower())
      header = f'/np/react-antd/components/modules/{tbl.model}/List.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_formmodal(self):
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      content = form_modal
      header = f'/np/react-antd/components/modules/{tbl.model}/Modal.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_updateform(self):
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      form_items = []
      for model_item in self.configuration['models'][tbl.model]:
        if model_item['type'] in ['django_foreign_key', 'django_one_to_one', 'django_one_to_many', 'django_many_to_many']:
          continue
        item = model_item_to_form_item[model_item['type']]
        item = item.replace('__ITEM_NAME_LOWER', model_item['name'].lower())
        item = item.replace('__ITEM_NAME_TITLED', model_item['name'].title())
        form_items.append(item)

      form_item_delim = '\n\n'
      __TEMPLATE_FORM_ITEM_LIST = form_item_delim.join(form_items)
      content = update_form.replace('__TEMPLATE_FORM_ITEM_LIST', __TEMPLATE_FORM_ITEM_LIST)
      # header = f'/np/node-postgres/src/apps/{tbl.model.lower()}/models/postgres.js'
      header = f'/np/react-antd/components/modules/{tbl.model}/UpdateForm.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)

    # print('='*80)
    # print('coba lihat update form')
    # pprint.pprint(self)


  def generate_the_model(self):
    tables = self.configuration['table_nodes']
    for index, tbl in enumerate(tables,1):
      content = form_model.replace('__TEMPLATE_modelname', tbl.model.lower())
      content = content.replace('__TEMPLATE_Modelname', tbl.model)

      header = f'/np/react-antd/components/modules/{tbl.model}/{tbl.model}.js'
      self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_menu_json(self):
    tables = self.configuration['table_nodes']
    menu_items = []
    for index, tbl in enumerate(tables,1):
      model_low = tbl.model.lower()
      model_cap = tbl.model
      content = menu_item_template.replace('__TEMPLATE_Modelname', model_cap)
      content = content.replace('__TEMPLATE_modelname', model_low)
      menu_items.append(content)

    menu_content = '\n'.join(menu_items)
    content = menu_json.replace('__TEMPLATE_APP_MENU', menu_content)
    header = f'/np/react-antd/assets/menu.json'
    self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_app_routes(self):
    tables = self.configuration['table_nodes']
    import_parts = []
    route_parts = []
    for index, tbl in enumerate(tables,1):
      model_low = tbl.model.lower()
      model_cap = tbl.model

      # import Task from 'modules/Task/Task';
      import_parts.append(f"import {model_cap} from 'modules/{model_cap}/{model_cap}';")
      route_part = app_route_item.replace('__TEMPLATE_Modelname', model_cap).replace('__TEMPLATE_modelname', model_low)
      route_parts.append(route_part)

    __TEMPLATE_APP_ROUTE_IMPORT_ITEMS = '\n'.join(import_parts)
    __TEMPLATE_APP_ROUTE_ITEMS = '\n'.join(route_parts)
    content = app_routes.replace('__TEMPLATE_APP_ROUTE_IMPORT_ITEMS', __TEMPLATE_APP_ROUTE_IMPORT_ITEMS)
    content = content.replace('__TEMPLATE_APP_ROUTE_ITEMS', __TEMPLATE_APP_ROUTE_ITEMS)
    header = f'/np/react-antd/components/Route/Routes.js'
    self.mkfile_input_content = append_entry_tostring(self.mkfile_input_content,	header, content)


  def generate_react_component(self):
    self.generate_createform()
    self.generate_formprovider()
    self.generate_formwrapper()
    self.generate_formlist()
    self.generate_formmodal()
    self.generate_updateform()
    self.generate_the_model()


  def latest(self):
    return self.mkfile_input_content
