from schnell.app.stringutils import DQ, QuoteChar

def values(column, provider):
  """
  values = [item.replace('$$$', '') for item in column.values]
  values = str(values)
  col_attrs.append('choices=' + values)
  # print('\nenum?', column, 'values:', values, 'col attrs so far:', col_attrs)

  if hasattr(column, 'default'):
    col_attrs.append('default=' + column.default.replace('$$$', ''))
  """
  kembali = ''
  enum_values = column.values
  if provider == 'default':
    kembali += ''
  elif provider in ['django', 'django_mongo']:
    # values = [item.replace('$$$', '') for item in enum_values]
    # kembali = 'choices=' + str(values)
    values_temp = [item.replace('$$$', '') for item in enum_values]
    values = [f"('{item}', '{item.capitalize()}')" for item in values_temp]
    # kembali = 'choices=' + str(values)
    kembali = 'choices=' + '[' + ', '.join(values) + ']'
  elif provider in ['node_antd', 'node_antd_mongo', 'proshop_mongo']:
    '''
    values dan default menandakan enumvalues dan stringenumvalues
    item di dalamnya diapit QuoteChar $$$
    django perlu ganti $$$ ke empty
    node sequelize perlu ganti $$$ ke "

    hasilkan:
    shipping: { type: String, enum: ['"Yes"', '"No"'] },
    jk replace ke DQ
    '''
    replacement = [item.replace(QuoteChar, '') for item in column.values]
    kembali = f"enum: {replacement}"
  return kembali
