from schnell.app.stringutils import DQ, QuoteChar
from schnell.app.appconfig import libpohon_data

import_part = libpohon_data['import_part']

def defaultvalue(column, provider):
  kembali = ''
  # col_attrs.append(f'null={column.allowNull}')
  # images: { type: Array, required: false, default: [] },
  default_value = column.defaultValue.strip()
  if provider == 'default':
    kembali += ''
  elif provider in ['django', 'django_mongo']:
    from app.libpohon.handlers import get_tipe_kolom
    tipe_kolom = get_tipe_kolom(column, provider)
    if default_value.isdigit():      
      nilai = f'default={default_value}'
    elif default_value in ['__EMPTY', 'EMPTY', '__EMPTY__', 'kosong', 'empty']:
      if column.type == 'array_of':
        nilai = f'default=[]'
      elif column.type == 'string':
        nilai = f'default=""'
      else:
        nilai = f'default=""'
    elif default_value in ['false', 'true']:
      '''
      konversi ke js
      '''
      replacement = 'False' if default_value == 'false' else 'True'
      nilai = f'default={replacement}'
    else:
      nilai = f'default="{default_value}"'
    # col_attrs.append(f'default="{default_value}"')    
    if default_value == 'now' and tipe_model == 'models.DateTimeField':
      # import_part = ['from django.db import models']
      now_import = 'from django.utils.timezone import now'
      if now_import not in import_part:
        import_part.append(now_import)  
    # input(f"""
    # ketemu defaultvalue untuk mungkin sebuah enum
    # default ==> [{nilai}]
    # PRESS ANY KEY...
    # """)
    kembali += nilai
  elif provider == 'flask':
    kembali += f'default="{column.defaultValue}"'
  elif provider == 'nest_mongo':
    kembali += f'default: {default_value}'
  elif provider in ['node_antd', 'node_antd_mongo', 'proshop_mongo']:
    replacement = column.defaultValue.replace(QuoteChar, DQ)
    if replacement in ['False', 'True', 'false', 'true']:
      '''
      konversi ke js
      '''
      replacement = 'false' if replacement == 'False' else 'true'
      kembali = f"default: {replacement}"
    elif replacement.isdigit():
      kembali = f"default: {replacement}"
    else:
      kembali = f"default: '{replacement}'"    
  return kembali
