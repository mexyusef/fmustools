

def min_length(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['node_antd', 'node_antd_mongo']:
    nilai = column.min_length
    kembali += f'minlength: [{nilai}, "Value too short"]'

  return kembali
