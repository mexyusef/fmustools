from schnell.app.appconfig import libpohon_data

def relto(column, provider, tablename):
  kembali = ''
  relation_model = column.relTo
  if provider == 'default':
    pass
  elif provider in ['django', 'django_mongo']:
    # col_attrs.append(relation_model)
    kembali += relation_model
    # import_part = ['from django.db import models']
    import_part = libpohon_data['import_part']
    # sudah_ada = [item for item in import_part if item.endswith(relation_model)]
    # ini salah krn berbentuk "from apps.user.models import User" dan kita hanya punya "User"
    appname = relation_model.lower()
    guard_exist = f'from apps.{appname}.models import {relation_model}'
    # sudah_ada = [item for item in import_part if item==relation_model]
    sudah_ada = [item for item in import_part if item==guard_exist]
    if not sudah_ada:
      # import_part.append(f'from apps.{appname}.models import {relation_model}')
      import_part.append(guard_exist)
    # gimana cara kembalikan import_part???

    if tablename not in libpohon_data['import_part_by_table']:
      libpohon_data['import_part_by_table'][tablename] = ['from django.db import models']

    # guard_exist = f'from apps.{appname}.models import {relation_model}'
    sudah_ada = [item for item in libpohon_data['import_part_by_table'][tablename] if item==guard_exist]
    if not sudah_ada:
      libpohon_data['import_part_by_table'][tablename].append(guard_exist)

  elif provider in ['flask', 'flask_mongo']:
    if '.' in relation_model:
      # jika sudah berbentuk 'user.id'
      kembali = relation_model
    else:
      # jika masih 'User'
      kembali = f"('{relation_model.lower()}.id')"
  elif provider in ['proshop_mongo']:
    kembali = f"ref: '{relation_model}'"
  return kembali

