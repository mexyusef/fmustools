

def trim(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['node_antd', 'node_antd_mongo']:
    kembali += f'trim: true'

  return kembali
