

def db_index(column, provider):
  """
  col_attrs.append(f'db_index={column.db_index}')
  """
  kembali = ''
  if provider == 'default':
    pass
  elif provider == 'django':
    kembali += f'db_index={column.db_index}'
  elif provider == 'flask':
    kembali += f'index={column.db_index}'
  return kembali

