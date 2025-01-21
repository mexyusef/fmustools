

def auto_now(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'auto_now={column.auto_now}'
  # elif provider == 'flask':
  #   kembali += f'flask kosong: auto_now_add'
  return kembali
