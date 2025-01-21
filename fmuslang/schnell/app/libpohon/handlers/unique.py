

def unique(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'unique={column.unique}'
  elif provider == 'flask':
    kembali += f'unique={column.unique}'
  return kembali
