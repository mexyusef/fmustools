import datetime, decimal, json


TAB_SPACE_MULT = 2
TAB = ' ' * TAB_SPACE_MULT
JSON_INDENT = TAB_SPACE_MULT
TABS = TAB * 2


class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			# return (str(o) for o in [o])
			# return float(o)
			return str(o)
		elif isinstance(o, (datetime.date, datetime.datetime)):
			return o.isoformat()
		return super(DecimalEncoder, self).default(o)


class RecordEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return str(o)
		elif isinstance(o, Record):
			return {k:v for (k,v) in o.__dict__.items() if not k.startswith('__')}
		elif isinstance(o, (datetime.date, datetime.datetime)):
			return o.isoformat()
		return super(RecordEncoder, self).default(o)


class Record:
	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		# for k,v in self.__dict__.items():
		# 	if v is None:
		# 		self.__dict__[k] = ''

	def __str__(self):
		return json.dumps(self.__dict__, indent=TAB_SPACE_MULT, cls=DecimalEncoder)

	def __repr__(self):
		return json.dumps(self.__dict__, indent=TAB_SPACE_MULT, cls=DecimalEncoder)

	def keys_vals(self):
		return self.__dict__.keys(), self.__dict__.values()

	def values(self):
		return self.__dict__.values()

	def csv(self):
		"""
		pastikan semua values berbentuk str
		"""
		stringified = [str(item) for item in self.__dict__.values()]
		return ', '.join(stringified)

