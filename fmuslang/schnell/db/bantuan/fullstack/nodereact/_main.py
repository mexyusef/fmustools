from app.dirutils import (
  within_same_folder
)
from app.fileutils import (
  file_content,
  file_write
)
from app.printutils import (
	indah3
)
from app.treeutils import (
  get_tables
)
from ...common import (
  tab,
)
from db.bantuan.config import output_folder
from .config import (
  template_appjson_filepath,
  template_node_appcontent_filepath,
  template_react_appcontent_file,
)

field_map = {
	'string'						: 'string',
	'float'							: 'number',
}


input_template = within_same_folder(__file__, 'node-pg-antd.mk')
output_mkfile = joiner(output_folder, 'node-pg-antd-output.mk')

class KategoriOutput:

	def __init__(self, RootNode):
		self.root = RootNode
		self.tablenames = []
    self.result_body = []
    self.result_header = []
    self.result_footer = []

    self.generate_mkfile()

	def generate(self):
		separator = '\n\n// ' + '*' * 40 + '\n'
		return 'OK'


  def gen_template_db_init(self):
    result = ''

    dblines = []
    dbinfo = RootNode
    if hasattr(dbinfo, 'username'):
      # dbvalues['username'] = dbinfo.username
      dblines.append(f"%__TEMPLATE_DBUSER={dbinfo.username}")

    if hasattr(dbinfo, 'password'):
      # dbvalues['password'] = dbinfo.password
      dblines.append(f"%__TEMPLATE_DBPASS={dbinfo.password}")

    if hasattr(dbinfo, 'host'):
      # dbvalues['host'] = dbinfo.host
      dblines.append(f"%__TEMPLATE_DBHOST={dbinfo.host}")
      
    if hasattr(dbinfo, 'port'):
      # dbvalues['port'] = dbinfo.port
      dblines.append(f"%__TEMPLATE_DBPORT={dbinfo.port}")

    if hasattr(dbinfo, 'dbname'):
      # dbvalues['dbname'] = dbinfo.dbname
      dblines.append(f"%__TEMPLATE_DBNAME={dbinfo.dbname}")

    # %__TEMPLATE_DBUSER=usef
    # %__TEMPLATE_DBPASS=rahasia
    # %__TEMPLATE_DBHOST=gisel.ddns.net
    # %__TEMPLATE_DBPORT=9022
    # %__TEMPLATE_DBNAME=ecomm
    result = '\n'.join([tab(1)+item for item in dblines])
    print('='*20, 'dblines')
    print(result)

    self.template_content = self.template_content.replace('__TEMPLATE_DB_INIT', result)


  def gen_template_app_init(self):
    result = ''
    applines = []
    for index, tbl in enumerate(self.tables,1):
      # AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
      appidx = str(index).zfill(2)
      # tablename = tbl.tables['tablename']
      tablename = tbl.model
      # perlu utk lower...ini akan jadi nama direktori utk masing2 app
      # %__TEMPLATE_APP01=task
      # %__TEMPLATE_APP02=user
      applines.append(f"%__TEMPLATE_APP{appidx}={tablename.lower()}")

    result = '\n'.join([tab(1)+item for item in applines])
    print('='*20, 'applines')
    print(result)

    self.template_content = self.template_content.replace('__TEMPLATE_APP_INIT', result)


  def generate_nodepg_app_content(self):
    result = ''
    contentlines = []
    for index, tbl in enumerate(self.tables,1):
      # AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
      appidx = str(index).zfill(2)
      # tablename = tbl.tables['tablename']
      tablename = tbl.model

      content = file_content(template_node_appcontent_filepath)
      content = content \
        .replace('__TAB(6)', tab(6)) \
        .replace('__TAB(5)', tab(5)) \
        .replace('__TAB(4)', tab(4)) \
        .replace('__TAB(3)', tab(3)) \
        .replace('__TAB(2)', tab(2)) \
        .replace('__TAB(1)', tab(1))
      content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
      content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
      # content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
      content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.upper())
      content = content.replace('$$GANTI_DENGAN_MODEL_TITLE$$', tablename)
      content = content.replace('$$GANTI_DENGAN_MODEL_LOWER$$', tablename.lower())
      content = content.replace('$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$', tablename + 's')
      content = content.replace('$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$', tablename.lower() + 's')
      contentlines.append(content)

    # result = '\n'.join([tab(2)+item for item in contentlines])
    result = '\n'.join([item for item in contentlines])
    print('='*20, 'contentlines')
    print(result)

    self.template_content = self.template_content.replace('__TEMPLATE_SERVER_APP_CONTENT', result)


  def generate_reactantd_app_json(self):
    result = ''
    contentlines = []
    for index, tbl in enumerate(self.tables,1):
      # AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
      appidx = str(index).zfill(2)
      # tablename = tbl.tables['tablename']
      tablename = tbl.model

      content = file_content(template_appjson_filepath)
      content = content \
        .replace('__TAB(6)', tab(6)) \
        .replace('__TAB(5)', tab(5)) \
        .replace('__TAB(4)', tab(4)) \
        .replace('__TAB(3)', tab(3)) \
        .replace('__TAB(2)', tab(2)) \
        .replace('__TAB(1)', tab(1))
      content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
      # content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
      content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.upper())
      content = content.replace('$$GANTI_DENGAN_MODEL_TITLE$$', tablename)
      content = content.replace('$$GANTI_DENGAN_MODEL_LOWER$$', tablename.lower())
      content = content.replace('$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$', tablename + 's')
      content = content.replace('$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$', tablename.lower() + 's')
      contentlines.append(content)

    # template_app_content = '\n'.join([tab(2)+item for item in contentlines])
    result = '\n'.join([item for item in contentlines])
    print('='*20, 'contentlines')
    print(result)

    self.template_content = self.template_content.replace('__TEMPLATE_CLIENT_JSON_MODEL', result)


  def generate_reactantd_app_content(self):
    result = ''
    contentlines = []
    for index, tbl in enumerate(self.tables,1):
      # AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
      appidx = str(index).zfill(2)
      # tablename = tbl.tables['tablename']
      tablename = tbl.model

      content = file_content(template_react_appcontent_file)
      content = content \
        .replace('__TAB(6)', tab(6)) \
        .replace('__TAB(5)', tab(5)) \
        .replace('__TAB(4)', tab(4)) \
        .replace('__TAB(3)', tab(3)) \
        .replace('__TAB(2)', tab(2)) \
        .replace('__TAB(1)', tab(1))
      content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)
      # content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
      content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.upper())
      content = content.replace('$$GANTI_DENGAN_MODEL_TITLE$$', tablename)
      content = content.replace('$$GANTI_DENGAN_MODEL_LOWER$$', tablename.lower())
      content = content.replace('$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$', tablename + 's')
      content = content.replace('$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$', tablename.lower() + 's')
      contentlines.append(content)

    # result = '\n'.join([tab(2)+item for item in contentlines])
    result = '\n'.join([item for item in contentlines])
    print('='*20, 'contentlines')
    print(result)
    self.template_content = self.template_content.replace('__TEMPLATE_CLIENT_APP_CONTENT', result)


	def generate_mkfile(self):

    self.tables = get_tables(self.root)
    self.template_content = file_content(input_template)

		self.gen_template_db_init()
    self.gen_template_app_init()
    self.generate_nodepg_app_content()
    self.generate_reactantd_app_json()
    self.generate_reactantd_app_content()

    self.write_mk_file()

  def write_mk_file(self):
    file_write(output_mkfile, self.template_content)

  def gen_model_nodejs():
    for index, tbl in enumerate(self.tables,1):
      model = {}
      for colidx, column in enumerate(tbl.children):
        tipe_model = sequelize_type_mapper[column.type]
        if hasattr(column, 'relTo'):
          relation_model = column.relTo
          tipe_model = tipe_model.replace('ModelRujukan', relation_model)

        if column.type == 'varchar' and hasattr(column, 'typenum'):
          tipe_model += f'({column.typenum})'

        if hasattr(column, 'hasConstraint') and column.hasConstraint == True:
          model[column.label] = { 'type': tipe_model }
        else:
          model[column.label] = tipe_model

        if hasattr(column, 'unique'):
          model[column.label] .update({ 'unique': column.unique })

        if hasattr(column, 'allowNull'):
          model[column.label] .update({ 'allowNull': column.allowNull })

        if hasattr(column, 'references'):
          replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
          model[column.label] .update({ 'references': replacement })

        if hasattr(column, 'referencesKey'):
          replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
          model[column.label] .update({ 'referencesKey': replacement })

        if hasattr(column, 'primaryKey'):
          model[column.label] .update({ 'primaryKey': column.primaryKey })

        if hasattr(column, 'values'):
          '''
          values dan default menandakan enumvalues dan stringenumvalues
          item di dalamnya diapit QuoteChar $$$
          django perlu ganti $$$ ke empty
          node sequelize perlu ganti $$$ ke "
          '''
          replacement = [item.replace(QuoteChar, ReplaceQuoteChar) for item in column.values]
          model[column.label] .update({ 'values': replacement })

        if hasattr(column, 'default'):
          '''
          values dan default menandakan enumvalues dan stringenumvalues
          item di dalamnya diapit QuoteChar $$$
          django perlu ganti $$$ ke empty
          node sequelize perlu ganti $$$ ke "
          '''
          replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
          model[column.label] .update({ 'default': replacement })

        if hasattr(column, 'defaultValue'):
          replacement = column.defaultValue.replace(QuoteChar, ReplaceQuoteChar)
          if replacement in ['False', 'True']:
            '''
            konversi ke js
            '''
            replacement = 'false' if replacement == 'False' else 'true'
          model[column.label] .update({ 'defaultValue': replacement })
        
        if column.type not in skipped_column_types:
          configuration['models'][tbl.model].append({
            'name': column.label,
            'type': column.type,
          })

      # ini key dan val jadi ada " sedangkan sequelize fields gak pake quote
      hasil = json.dumps(model, indent=4)
      # kita masukkan ke config (columns) utk digunakan oleh react apps/components
      # sewaktu bikin form
      
      # gak perlu krn ada via tbl.children -> column

      # setiap "STRING", "NUMBER" dll menjadi STRING dan NUMBER
      # kita punya __DQTIMESTAMP__DQ dari pemetaan timestamp
      # stlh omit " kita jg kasih " utk field type yg diapit __DQ
      hasil = hasil.replace(ReplaceQuoteChar, '').replace('__DQ', '"')
      per_table = nodejs_sequelize_model_template
      per_table = per_table.replace('__TABLENAME__', tbl.model)
      per_table = per_table.replace('__TABLENAME_LOWER__', tbl.model.lower())
      per_table = per_table.replace('__TABLENAME_UPPER__', tbl.model.upper())
      per_table = per_table.replace('__TABLENAME_LOWER_PLURAL__', tbl.model.lower() + 's')
      per_table = per_table.replace('__TABLENAME_UPPER_PLURAL__', tbl.model.upper() + 's')
      per_table = per_table.replace('__TABLENAME_CAP_PLURAL__', tbl.model.capitalize() + 's')

      per_table = per_table.replace('__FIELDS__', hasil)
      per_table = per_table.replace('__TAB', tab(1))

      print('*'*40)
      print(per_table)
      print('~'*40)
      header = f'/np/node-postgres/src/apps/{tbl.model.lower()}/models/postgres.js'
      entrify = append_entry(filepath_output,	header, per_table)

  def gen_model_react_():
    """
    assets/<model>.json
    digunakan utk konfigurasi table di CRUD/get/list
    """
    for index, tbl in enumerate(tables,1):      
      # per_table = react_antd_app_route_template
      # per_table = per_table.replace('__TABLENAME__', tbl.model)		
      # per_table = per_table.replace('__TABLENAME_LOWER__', tbl.model.lower())
      # per_table = per_table.replace('__TABLENAME_UPPER__', tbl.model.upper())
      # per_table = per_table.replace('__TABLENAME_LOWER_PLURAL__', tbl.model.lower() + 's')
      # per_table = per_table.replace('__TABLENAME_UPPER_PLURAL__', tbl.model.upper() + 's')
      # per_table = per_table.replace('__TABLENAME_CAP_PLURAL__', tbl.model.capitalize() + 's')
      # per_table = per_table.replace('__FIELDS__', hasil)
      # per_table = per_table.replace('__TAB', tab(1))

      model_low = tbl.model.lower()
      model_cap = tbl.model.capitalize()
      # columns = []
      # for colidx, column in enumerate(tbl.children):
      # 	columns.append(column.label)
      columns = [tab(2)+f'"{col.label}"' for col in tbl.children]
      pengganti = ',\n'.join(columns) + ',\n'
      content = react_antd_app_asset_json.replace('__TEMPLATE_APP_ASSET_JSON', pengganti)
      # review.json,f(e=utama=/np/react-antd/assets/review.json)
      header = f'/np/react-antd/assets/{tbl.model.lower()}.json'
      entrify = append_entry(filepath_output,	header, content)

  def gen_model_nodejs_specific():
    pass

  def gen_model_react_specific_menus():
    pass

  def gen_model_react_specific_routes():
    pass

  def gen_model_react_specific():
    self.gen_model_react_specific_menus()
    self.gen_model_react_specific_routes()

	def generate_models(self):
		self.gen_model_nodejs()
    self.gen_model_react()
    self.gen_model_nodejs_specific()
    self.gen_model_react_specific()

def bantu_nodereact(RootNode):
	indah3('bantu_nodereact', warna='white')
	generator = KategoriOutput(RootNode)
	return generator.generate()
