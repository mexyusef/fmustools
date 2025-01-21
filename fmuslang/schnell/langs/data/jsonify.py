import json, decimal, datetime, numpy, enum, bson

class MyJsonify(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, set):
      return list(obj)
    elif isinstance(obj, decimal.Decimal):
      return float(obj)
    elif isinstance(obj, (datetime.date, datetime.datetime)):
      return obj.isoformat()
    # elif isinstance(obj, datetime.datetime):
    #     return obj.strftime("%Y-%m-%d %H:%M:%S")
    # elif isinstance(obj, datetime.date):
    #     return obj.strftime("%Y-%m-%d")
    elif isinstance(obj, numpy.int64):
      return int(obj)
    elif isinstance(obj, numpy.integer):
      return int(obj)
    elif isinstance(obj, numpy.floating):
      return float(obj)
    elif isinstance(obj, numpy.ndarray):
      return obj.tolist()

    elif isinstance(obj, enum.Enum):
      return obj.value
    elif isinstance(obj, bson.objectid.ObjectId):
      return str(obj)

    # return super(MyJsonify, self).default(obj)
    return json.JSONEncoder.default(self, obj)
