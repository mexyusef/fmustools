

def primarykey(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['django', 'django_mongo']:
    kembali += 'primary_key=True'
  elif provider == 'flask':
    kembali += f'primary_key={column.primaryKey}'
  elif provider in ['node_antd', 'node_antd_mongo']:
    nilai = 'true' if column.primaryKey else 'false'
    kembali += f'primaryKey: {nilai}'

  return kembali
