

def lower(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['node_antd', 'node_antd_mongo']:
    kembali += f'lowercase: true'

  return kembali
