

def requiredvalidation(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['node_antd', 'node_antd_mongo']:
    message = column.requiredWithValidation
    kembali += f'required: "{message}"'

  return kembali
