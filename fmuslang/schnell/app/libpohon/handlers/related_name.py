

def related_name(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'related_name={column.related_name}'

  return kembali
