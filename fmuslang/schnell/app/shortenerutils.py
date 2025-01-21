# https://pyshorteners.readthedocs.io/en/latest/
import pyshorteners

# https://app.bitly.com/settings/api/
mykey = '465b3fe657fbb330e2a58aee8961d4b2cfd8bdcf'
s = pyshorteners.Shortener()
t = pyshorteners.Shortener(api_key=mykey)

def tinyurl(alamat):
	r = s.tinyurl.short(alamat) # https://tinyurl.com/264bpq
	return r


def osdb(alamat):
	# s = pyshorteners.Shortener()
	a = s.osdb.short(alamat) # 'https://osdb.link/TEST'
	# print(a) # http://osdb.link/6ay6
	# s.osdb.expand('http://osdb.link/TEST') # 'https://www.google.com'
	return a


def isgd(alamat):
	a = s.isgd.short(alamat) # 'http://is.gd/TEST'
	# print(a) # https://is.gd/WzFWtC
	# s.isgd.expand('http://is.gd/TEST') # 'http://www.google.com'
	return a


def clickru(alamat):
	a = s.clckru.short(alamat) # 'http://clck.ru/TEST'
	# print(a) # https://clck.ru/0v
	# s.clckru.expand('http://clck.ru/TEST') # 'http://www.google.com'
	return a


def dagd(alamat):
	a = s.dagd.short(alamat) # 'http://da.gd/TEST'
	# print(a) # https://da.gd/2UoqA
	# s.dagd.expand('http://da.gd/TEST') # 'http://www.google.com'
	return a


def bitly(alamat):
	a = t.bitly.short(alamat) # 'http://bit.ly/TEST'
	# print(a) # https://bit.ly/3nQbnzL
	# s.bitly.expand('https://bit.ly/TEST') # 'http://www.google.com'
	# s.bitly.total_clicks('https://bit.ly/TEST') # 10
	return a
