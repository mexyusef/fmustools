from schnell.app.stringutils import DQ, QuoteChar

def default(column, provider):
  """
  default utk enum
  column.values
  column.default

  if hasattr(column, 'values'):
    '''
    handle enums yg nodenya berisi values dan default
    '''
    values = [item.replace('$$$', '') for item in column.values]
    values = str(values)
    col_attrs.append('choices=' + values)
    # print('\nenum?', column, 'values:', values, 'col attrs so far:', col_attrs)

    if hasattr(column, 'default'):
      col_attrs.append('default=' + column.default.replace('$$$', ''))
  """
  kembali = ''
  nilai_enum_default = column.default
  if provider == 'default':
    kembali += ''
  elif provider in ['django', 'django_mongo']:
    nilai_default = nilai_enum_default.replace('$$$', '')
    # if column.type == 'models.CharField':
    #   nilai_default = f'"{nilai_default}"'
    if not nilai_default.isdigit():
      nilai_default = f'"{nilai_default}"'
    default = 'default=' + nilai_default
    kembali += default
  elif provider in ['node_antd', 'node_antd_mongo', 'proshop_mongo']:
    '''
    values dan default menandakan enumvalues dan stringenumvalues
    item di dalamnya diapit QuoteChar $$$
    django perlu ganti $$$ ke empty
    node sequelize perlu ganti $$$ ke "
    '''
    replacement = column.default.replace(QuoteChar, DQ)
    kembali = f"default: {replacement}"
  return kembali
