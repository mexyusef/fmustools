from anytree import RenderTree
from app.usutils import (
	# gen_template_db_init,
	# gen_template_app_init,
	# generate_app_content,
	# write_mkfile,
	tab,
)
from db.bantuan.generate_faker import generate_faker


entity_field_map = {	
	'boolean':      'BOOL',
	'enum':         'GANTI',

	'double':       'FLOAT',
	'float':        'FLOAT', # float(n), n = 0-24 utk float
	'number':       'NUMERIC', # numeric(left,right)
	'decimal':			'NUMERIC', # numeric(left,right)
	
	# 'image':				'GANTI',

	'auto':					'SERIAL',
	'bigint':       'INT',
	'integer':      'INT',	

	# 'string':       'CHAR', # char(n), char itu fixed size
	'string':       'VARCHAR', # char(n), char itu fixed size
	'text':         'TEXT',
	'varchar':      'VARCHAR', # varchar(n)

	'date':         'DATE',
	'time':         'TIME',
	'timestamp':    'TIMESTAMP',
	# 'timestamp':    'TIMESTAMPTZ',

	'django_foreign_key':			'INT FOREIGN KEY REFERENCES',
	'django_one_to_one':			'GANTI',
	'django_one_to_many':			'GANTI',
	'django_many_to_many':		'GANTI',

	# 'email':        'GANTI',
	# 'slug':         'GANTI',
}

insert_statement = """
INSERT INTO __TABLE__ (__COLUMNS__)
VALUES (__VALUES__);
"""

def self_namify(name, quoting=True, quote='"'):
  if quoting:
    return f'{quote}{name}{quote}'
  return name

def generate_sql_insert(tbl):
  self_insert_body = []
  table_fields = []
  table_plural = tbl.model.lower() + 's'
  if hasattr(tbl, 'faker'):
    records = []
    for angka in range(tbl.faker):
      print('pre generate_faker: oprekking sql:', RenderTree(tbl))
      kwargs = generate_faker(table=tbl, init_counter=0 if angka==0 else None)
      bentuk_values = []
      for _, col in enumerate(tbl.children):
        is_string = col.type == 'string' or col.type == 'varchar' or col.type == 'text' or col.type == 'date' or col.type == 'timestamp'
        item = kwargs[col.label]
        
        # enum diberi $$$ oleh ucsv/processor:358
        if is_string:
          if isinstance(item, str) and '$$$' in item:
            # item = item.replace('$$$', '"')
            item = item.replace('$$$', "'")
          else:
            '''
            postgres minta ' utk string
            '''
            # item = f'"{item}"'
            item = f"'{item}'"

        bentuk_values.append(f'{item}')

      stmt = insert_statement.replace('__TABLE__', table_plural) \
        .replace('__COLUMNS__', ', '.join([item for item in kwargs.keys()])) \
        .replace('__VALUES__', ', '.join(bentuk_values))

        # .replace('__VALUES__', ', '.join([item for item in kwargs.values()]))
      self_insert_body.append(stmt)

  return self_insert_body

def generate_sql_body(table):
  self_entity_body = []
  table_fields = []
  primary_key = None
  for column_no, field in enumerate(table.children, 1):
    fieldspec = '@Column (__COLUMN_CONSTRAINT)'
    fieldspec_constraint_object = []
    # fieldspec_constraint_nonobject = ''

    # utk array, sql-nya apa? relation?
    # if hasattr(field, 'subtype'):
    # 	column = column.replace('__SUBTYPE__', entity_field_map.get(field.subtype, field.subtype))
    # 	if field.type == 'array_of':
    # 		fieldspec_constraint_nonobject = "'simple-array'"

    if hasattr(field, 'primaryKey'):
      '''
      primary key kita tambahkan di akhir para kolom gaya sql
      '''
      # fieldspec_constraint_object .append ('PRIMARY KEY')
      primary_key = f"PRIMARY KEY ({self_namify(field.label)})"

    jenis_data = entity_field_map.get(field.type, field.type)

    if field.type == 'django_foreign_key' and hasattr(field, 'relTo'):
      relation = field.relTo
      if '.' in relation and relation.count('.') == 1:
        relation = relation.strip('"') # hilangkan semua dq dulu
        foreign_table, foreign_column = relation.split('.')
        # city_id INT FOREIGN KEY REFERENCES city(id)
        jenis_data += ' ' + f'{foreign_table}({foreign_column})'
      else:
        jenis_data += ' ' + relation

    if hasattr(field, 'max_length') or hasattr(field, 'typenum'):
      if field.type == 'string' or field.type == 'varchar':
        
        if hasattr(field, 'max_length'):
          maxlen = field.max_length
        elif hasattr(field, 'typenum'):
          maxlen = field.typenum
        jenis_data = f'{jenis_data}({maxlen})'

    column = f"{self_namify(field.label)} {jenis_data}__CONSTRAINTS_HOLDER__"

    if hasattr(field, 'allowNull'):
      fieldspec_constraint_object.append('NULL' if field.allowNull else 'NOT NULL')

    if hasattr(field, 'defaultValue'):
      '''
      konversi False ke false
      juga utk time
      timestamp,dt,dbi,df=datetime.utcnow
      perlu konversi ke sql...nonpython...
      '''
      nilai_default = field.defaultValue
      if nilai_default == 'empty':
        nilai_default = "''"
      if field.type == 'boolean' and nilai_default.lower() in ['false', 'true']:
        nilai_default = nilai_default.lower()
      if (field.type == 'string' or field.type.startswith('varchar')) and nilai_default.count('"') == 0 and nilai_default.count("'") == 0:
        nilai_default = '"' + nilai_default + '"'
      fieldspec_constraint_object .append ('DEFAULT ' + nilai_default)

    stringified_fieldspec_constraint_object = ''
    if fieldspec_constraint_object:
      # kasih space stlh jenis kolom
      stringified_fieldspec_constraint_object = ' ' + ' '.join(fieldspec_constraint_object)

    # stringified_nonobject = ', '.join([fieldspec_constraint_nonobject])
    # print('stringified_nonobject:', stringified_nonobject)
    # fieldspec_constraint = stringified_nonobject + stringified_fieldspec_constraint_object
    fieldspec = column.replace('__CONSTRAINTS_HOLDER__', stringified_fieldspec_constraint_object)
    table_fields.append(fieldspec)

  if primary_key is not None:
    table_fields.append(primary_key)
  stringified_fields = ',\n'.join([tab(1)+item for item in table_fields])
  # nama_table = table.model.lower()
  # nama_entity = f"{table.model}Entity"
  sql_statement_terminator = ';'
  table_plural = table.model.lower() + 's'
  temp = f"\nCREATE TABLE IF NOT EXISTS {self_namify(table_plural)} (\n"
  temp += stringified_fields
  temp += f'\n){sql_statement_terminator}'
  self_entity_body.append(temp)

  return self_entity_body


def generate_table(table):
  self_entity_body = generate_sql_body(table)
  self_insert_body = generate_sql_insert(table)
  first = '\n'.join(self_entity_body)
  second = '\n'.join(self_insert_body)
  return first + '\n' + '-- ' + '*'*40 + '\n' + second
