import json, datetime, re
from schnell.langs.data.fakesey import palsu
from .jsonutils import MyJsonify


format_date = '%Y/%m/%d'
format_datetime = '%Y/%m/%d %H:%M:%S'
faker = palsu.faker


def getfakers(funcname, callnum=1, funcargs=None, kwfuncargs=None, as_string=False, as_list=False, as_is=False, quote_string=False,format_date=format_date,format_datetime=format_datetime):
  # print('getfakers meminta sebanyak:', callnum)
  hasil = []
  for _ in range(callnum):
    if funcargs:
      ok = getattr(faker, funcname)(*funcargs)
    elif kwfuncargs:
      ok = getattr(faker, funcname)(**kwfuncargs)
    else:
      ok = getattr(faker, funcname)()

    if not as_is:
      if isinstance(ok, int):
        ok = str(ok)
      elif isinstance(ok, list):
        ok = str(ok)
      elif isinstance(ok, dict):
        ok = json.dumps(ok, indent=2, cls=MyJsonify)

    if quote_string and (isinstance(ok, str) or isinstance(ok, datetime.datetime) or isinstance(ok, datetime.date)):
      if isinstance(ok, datetime.datetime):
        ok = ok.strftime(format_datetime)
      elif isinstance(ok, datetime.date):
        ok = ok.strftime(format_date)
      ok = '"' + ok + '"'

    # TODO
    # mugkin jk callnum=1, langsung saja, return ok ?
    if callnum==1:
      return ok

    hasil.append(ok)

  if as_string:
    return ', '.join(hasil)
  elif as_list:
    return hasil
  return '[' + ', '.join(hasil) + ']'

faker_mapper = {
  'bool'    : 'pybool',
  'boolean' : 'pybool',
  # 'date'    : 'date', # dt
  # 'date'    : 'date_this_year', # dt
  'date'    : 'date_between', # dt

  'decimal' : 'pydecimal',
  'DECIMAL' : 'pydecimal',
  'float'   : 'pyfloat',

  'int'     : 'pyint',
  'integer' : 'pyint',

  'dict'    : 'pydict',
  'list'    : 'pylist',
  'set'     : 'pyset',

  'number'  : 'pyint',
  'string'  : 'word',

  # date_time_between(start_date='-15y', end_date='now')
  # 'timestamp': 'date_time', # ts
  # 'timestamp': 'date_time_this_year', # ts
  'timestamp': 'date_time_between', # ts
  'time.Time': 'date_time_between', # ts

  'contain_age': 'random_int',
  'contain_city': 'city',
  'contain_country': 'country',
  'contain_email': 'email',
  'contain_address': 'address',
  'contain_name': 'name',
  'contain_phone': 'phone_number',
  'contain_firstname': 'first_name',
  'contain_lastname': 'last_name',  
  'contain_malename': 'name_male',
  'contain_femalename': 'name_female',
}


def get_by_datatypes(tipedata, callnum=1, funcargs=None, kwfuncargs=None, as_string=False, as_list=False, as_is=False, quote_string=False):
  hasil = getfakers(faker_mapper[tipedata], callnum=callnum, funcargs=funcargs, kwfuncargs=kwfuncargs, as_string=as_string, as_list=as_list, as_is=as_is, quote_string=quote_string)
  return hasil


def get_by_type_or_name(tipedata, namadata, callnum=1, funcargs=None, kwfuncargs=None, as_string=False, as_list=False, as_is=False, quote_string=False,format_date=format_date,format_datetime=format_datetime):
  """
  bisa juga manual
  get_by_type_or_name('random_element', funcargs=['satu','dua','tiga'])
  """
  pengunci = tipedata
  # print('tipedata', tipedata)
  if tipedata == 'timestamp' or tipedata == 'date':
    quote_string=True
    kwfuncargs = {'end_date':'now', 'start_date':'-3y'}
  if 'email' in namadata.lower():
    pengunci = 'contain_email'
  elif 'address' in namadata.lower():
    pengunci = 'contain_address'
  elif 'age' in namadata.lower():
    pengunci = 'contain_age'
    funcargs = [1,99]
  elif 'city' in namadata.lower():
    pengunci = 'contain_city'
  elif 'country' in namadata.lower():
    pengunci = 'contain_country'
  elif 'first' in namadata.lower() and 'name' in namadata.lower():
    pengunci = 'contain_firstname'
  elif 'last' in namadata.lower() and 'name' in namadata.lower():
    pengunci = 'contain_lastname'
  elif 'male' in namadata.lower() and 'name' in namadata.lower():
    pengunci = 'contain_malename'
  elif 'female' in namadata.lower() and 'name' in namadata.lower():
    pengunci = 'contain_femalename'
  elif 'name' in namadata.lower():
    pengunci = 'contain_name'
  elif 'phone' in namadata.lower():
    pengunci = 'contain_phone'
  # experimental
  elif 'dict' in namadata.lower():
    pengunci = 'dict'
  elif 'list' in namadata.lower():
    pengunci = 'list'
    # print('list name:', namadata)
    if 'int' in namadata.lower() and 'str' in namadata.lower():
      kwfuncargs = {'value_types':[str,int]}
    elif 'int' in namadata.lower():
      kwfuncargs = {'value_types':[int]}
    elif 'float' in namadata.lower():
      # print('tipe list of floats')
      kwfuncargs = {'value_types':[float]}
    else:
      kwfuncargs = {'value_types':[str]}
    if 'num' in namadata:
      # print(f'num in {namadata}')
      get = re.match(r'^.*num(\d+).*$', namadata)
      if get:        
        jumlah = get.group(1)
        # print(f'match num in {get.groups()}, jumlah = {jumlah}')
        kwfuncargs['nb_elements'] = int(jumlah)
        kwfuncargs['variable_nb_elements'] = False

  petakan = pengunci # misal text, paragraph yg gak ada peta nya
  if pengunci in faker_mapper:
    petakan = faker_mapper[pengunci]
  hasil = getfakers(petakan, callnum=callnum, funcargs=funcargs, kwfuncargs=kwfuncargs, as_string=as_string, as_list=as_list, as_is=as_is, quote_string=quote_string,format_date=format_date,format_datetime=format_datetime)
  return hasil
