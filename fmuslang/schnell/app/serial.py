import json, pickle

# from schnell.app.serial import kirim, terima

technique_mapper = {
  'json': {
    'rx': json.loads,
    'tx': json.dumps,
    # to file
    'rf': json.load,
    'tf': json.dump,
  },
  'pickle': {
    'rx': pickle.loads,
    'tx': pickle.dumps,
    # to file
    'rf': pickle.load,
    'tf': pickle.dump,
  },
}


def serialize(anything):
  return pickle.dumps(anything)


def deserialize(data):
  return pickle.loads(data)


def kirim(data, file_handle=None, technique='pickle'):
  """
  dari dalam sistem kirim ke luar
  """
  if technique in technique_mapper:
    if file_handle:
      return technique_mapper[technique].get('tf')(data, file_handle)
    return technique_mapper[technique].get('tx')(data)

  return data


def terima(file_handle=None, technique='pickle'):
  """
  dari luar masuk sistem
  """
  if technique in technique_mapper:
    if file_handle:
      return technique_mapper[technique].get('rf')(file_handle)
    return technique_mapper[technique].get('rx')()

  return None
