

def foreignkeyondelete(column, provider):
  """
  # nilai models.CASCADE atau SET_NULL ditentukan di ucsv/processor:95
  col_attrs.append(f'on_delete={column.foreignKeyOnDelete}')

  """
  kembali = ''
  if provider == 'default':
    pass
  elif provider in ['django', 'django_mongo']:
    kembali += f'on_delete={column.foreignKeyOnDelete}'
  return kembali

