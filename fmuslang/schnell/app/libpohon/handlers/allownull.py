def allownull(column, provider):
  kembali = ''
  # col_attrs.append(f'null={column.allowNull}')
  # images: { type: Array, required: false, default: [] },
  boleh_isi_null = column.allowNull
  if provider == 'default':
    kembali += ''
  elif provider in ['django', 'django_mongo']:
    kembali += f'null={column.allowNull}'
  elif provider == 'flask':
    kembali += f'nullable={column.allowNull}'
  elif provider in [
    # 'node_antd',
    'proshop_mongo',
    'node_antd_mongo',]:
    required = 'true' if not boleh_isi_null else 'false'
    kembali += f'required: {required}'
  elif provider in ['nest', 'nest_mongo']:
    required = 'true' if not boleh_isi_null else 'false'
    kembali += f'required: {required}'

  return kembali
