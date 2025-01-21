

def upper(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['node_antd', 'node_antd_mongo']:
    kembali += f'uppercase: true'

  return kembali
