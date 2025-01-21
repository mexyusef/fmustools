

def auto_now_add(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'auto_now_add={column.auto_now_add}'
  elif provider == 'flask':
    kembali += f'default=datetime.utcnow'
  return kembali
