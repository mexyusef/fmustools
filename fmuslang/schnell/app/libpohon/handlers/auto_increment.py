from schnell.app.appconfig import libpohon_data
# django_auto_request = libpohon_data['django_auto_request']

def auto_increment(column, provider):
  kembali = ''

  if provider == 'default':
    kembali += ''
  elif provider in ['django', 'django_mongo']:
    # kembali += f'auto_increment={column.auto_increment}'
    # mending kita kasih tau global context/var: gunakan models.AutoField
    # hrs ada yg "remove after use"
    # django_auto_request = True # ini jadi copy, bukan aslinya
    libpohon_data['django_auto_request'] = True
    kembali += ''
  elif provider == 'flask':
    kembali += f'default=datetime.utcnow'
  return kembali
