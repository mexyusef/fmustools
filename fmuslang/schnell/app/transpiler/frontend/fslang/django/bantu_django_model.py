# from app.fileutils import (
# 	file_content,
# 	append_file,
# )
from app.usutils import tab
# from ..common import (
#   tab,
#   sequelize_type_mapper,
# )
from app.appconfig import libpohon_data
from .common import append_entry, django_model_template

TIMESTAMPED_BASE_MODEL = 'TimestampedModel'
DEFAULT_BASE_MODEL = 'models.Model'


def generate_model(tables):
  """
  unused lihat __init__.py/generate_model()
  """

  for index, tbl in enumerate(tables,1):
    
    import_part = ['from django.db import models']
    
    # body_part = []
    # footer_part = []
    
    model = {}

    for colidx, column in enumerate(tbl.children):

      # print('gen_django_models => col:', column)

      tipe_model = sequelize_type_mapper.get(column.type, column.type)
      model[column.label] = tipe_model
      col_attrs = []

      if hasattr(column, 'relTo'):
        relation_model = column.relTo
        col_attrs.append(relation_model)
        # Field defines a relation with the model 'auth.User', which has been swapped out.
        # HINT: Update the relation to point at 'settings.AUTH_USER_MODEL'.
        # user_aum = 'from django.contrib.auth.models import User'
        # if (user_aum not in import_part) and relation_model == 'User':
        # 	import_part.append(user_aum)
        # else:
        # 	cek apa sudah diimport
        # 	from apps.applower.models import App

        ada = [item for item in import_part if item.endswith(relation_model)]
        if not ada:
          appname = relation_model.lower()
          import_part.append(f'from apps.{appname}.models import {relation_model}')

      if hasattr(column, 'allowNull'):
        col_attrs.append(f'null={column.allowNull}')

      if hasattr(column, 'auto_increment'):
        col_attrs.append(f'auto_increment={column.auto_increment}')

      if hasattr(column, 'auto_now'):
        col_attrs.append(f'auto_now={column.auto_now}')
        # now_import = 'from django.utils.timezone import now'
        # if now_import not in import_part:
        #   import_part.append(now_import)

      if hasattr(column, 'auto_now_add'):
        col_attrs.append(f'auto_now_add={column.auto_now_add}')
        
      if hasattr(column, 'blank'):
        col_attrs.append(f'blank={column.blank}')

      if hasattr(column, 'editable'):
        col_attrs.append(f'editable={column.editable}')

      if hasattr(column, 'defaultValue'):
        col_attrs.append(f'default="{column.defaultValue}"')
        if column.defaultValue == 'now' and tipe_model == 'models.DateTimeField':
          now_import = 'from django.utils.timezone import now'
          if now_import not in import_part:
            import_part.append(now_import)

      if hasattr(column, 'db_index'):
        col_attrs.append(f'db_index={column.db_index}')

      if hasattr(column, 'foreignKeyOnDelete'):
        # nilai models.CASCADE atau SET_NULL ditentukan di ucsv/processor:95
        col_attrs.append(f'on_delete={column.foreignKeyOnDelete}')

      if hasattr(column, 'max_length'):
        col_attrs.append(f'max_length={column.max_length}')

      if hasattr(column, 'max_digits'):
        col_attrs.append(f'max_digits={column.max_digits}')

      if hasattr(column, 'decimal_places'):
        col_attrs.append(f'decimal_places={column.decimal_places}')

      if hasattr(column, 'related_name'):
        col_attrs.append(f'related_name={column.related_name}')

      if hasattr(column, 'verbose_name'):
        col_attrs.append(f'verbose_name={column.verbose_name}')

      if hasattr(column, 'primaryKey'):
        col_attrs.append('primary_key=True')
        # type ganti ke AutoField

      if hasattr(column, 'unique'):
        col_attrs.append(f'unique={column.unique}')

      if hasattr(column, 'values'):
        '''
        handle enums yg nodenya berisi values dan default
        '''
        values = [item.replace('$$$', '') for item in column.values]
        values = str(values)
        col_attrs.append('choices=' + values)
        # print('\nenum?', column, 'values:', values, 'col attrs so far:', col_attrs)

        if hasattr(column, 'default'):
          col_attrs.append('default=' + column.default.replace('$$$', ''))

      # if not col_attrs and tipe_model == 'models.CharField':
      # 	col_attrs = ['max_length=255']
      if tipe_model == 'models.CharField':
        ada_maxlen = [item for item in col_attrs if item.startswith('max_length')]
        if not ada_maxlen:
          col_attrs .append('max_length=255')

      # contoh:
      # model[username] = String
      # model[username] += (required=true, ...)
      # menjadi model[username] = String(required=true, ...)
      model[column.label] += "(" + ', '.join(col_attrs) + ")"
      # print('model result:', model[column.label])

    formatted = []
    for k,v in model.items():
      field = f"{k.ljust(10)} = {v}"
      formatted.append(field)

    first_column = tbl.children[0].label
    hasil = '\n'.join([tab()+item for item in formatted])
    
    basemodel = TIMESTAMPED_BASE_MODEL if hasattr(tbl, 'timestamp') else DEFAULT_BASE_MODEL
    timestamp_import = 'from main.helpers import TimestampedModel'

    if hasattr(tbl, 'timestamp'):
      basemodel =  TIMESTAMPED_BASE_MODEL
      import_part.append(timestamp_import)
    else:
      basemodel =  DEFAULT_BASE_MODEL
    hasil = django_model_template \
      .replace('__TABLENAME__', tbl.model) \
      .replace('__IMPORTS__', '\n'.join(import_part)) \
      .replace('__COLNAME__', first_column) \
      .replace('__FIELDS__', hasil) \
      .replace('__TABLE_BASEMODEL__', basemodel)
    # replace tab hrs diakhir krn makan "table" dst
    hasil = hasil..replace('__TAB', tab(1))

    per_table = hasil # '\n' + hasil + '\n'
    print('*'*40)
    print(per_table)
    print('~'*40)
    entrify = append_entry(tbl.model, per_table, entry_name='models')
