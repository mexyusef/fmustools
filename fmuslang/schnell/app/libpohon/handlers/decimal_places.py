

def decimal_places(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'decimal_places={column.decimal_places}'

  return kembali
