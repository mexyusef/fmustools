

def verbose_name(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'verbose_name={column.verbose_name}'

  return kembali
