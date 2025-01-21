

def max_digits(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'max_digits={column.max_digits}'

  return kembali
