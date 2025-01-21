

def max_length(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider == 'django':
    kembali += f'max_length={column.max_length}'
  elif provider in ['node_antd', 'node_antd_mongo']:
    nilai = column.max_length
    kembali += f'maxlength: [{nilai}, "Value too Long"]'

  return kembali
