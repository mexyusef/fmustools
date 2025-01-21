import json, pickle, redis
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import walk_fullpath
from schnell.app.fileutils import file_content
from schnell.app.printutils import indah4
# from schnell.app.utils import env_get, env_int


def connect(host=None, port=None, db=None, password=None, strict=False):
	"""
	utk aplikasi terpisah, env_load() terlebih dahulu, baru panggil fungsi ini
	"""
	if host is None:
		host = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_HOST'] # env_get('ULIBPY_REDIS_HOST')
	if port is None:
		port = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_PORT'] # env_int('ULIBPY_REDIS_PORT')
	if db is None:
		db = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_DBNO'] # env_int('ULIBPY_REDIS_DBNO')
	# if not host:
	# 	host = 'localhost'
	# if not port:
	# 	port = 6379
	# if not db:
	# 	db = 0
	conn_params = {
		'host': host,
		'port': port,
		'db': db,
	}
	# print('[app.redisutils] redis connect:', conn_params)
	if password is not None:
		conn_params.update({
			'password': password,
		})

	if strict:
		r = redis.StrictRedis(**conn_params)
	else:
		r = redis.Redis(**conn_params)
	return r


def kasih(r, k, v):
  r.set(k, v)
# set=kasih


def ambil(r, k):
  return r.get(k)
# get=ambil


saved_connection = {}


def savedconn(dbno=0):
	if dbno in saved_connection:
		return saved_connection[dbno]
	else:
		r = connect(db=dbno)
		saved_connection[dbno] = r
		return r


def setdict(dbno, k, v, mode='json'):
	r = savedconn(dbno)
	data = json.dumps(v) if mode=='json' else pickle.dumps(v)
	r.set(k, data)


def getdict(dbno, k, mode='json'):
	r = savedconn(dbno)
	try:
		v = r.get(k)
		data = json.loads(v) if mode=='json' else pickle.loads(v)
		return data
	except:
		return None


def redis_publish(data, r, channel=None):
	"""
	digunakan oleh make_repl utk ngirim request repl_service ke kbrepl
	"""
	if not channel:
		channel = 'replservice_request'

	r.publish(channel, json.dumps(data))


class ConsoleData():
	"""
	ConsoleData mau digunakan utk ganti from schnell.app.appconfig import command_prompt_data
	"""
	def __init__(self, dbno=12, keyname='console_data'):
		self.dbno = dbno
		self.keyname = keyname
		# self.r = savedconn(self.dbno)
	def __call__(self, data=None):
		if not data:
			return getdict(self.dbno, self.keyname)
		else:
			setdict(self.dbno, self.keyname, data)
	def __getitem__(self, key):
		data = getdict(self.dbno, self.keyname)
		return data[key]
	def __setitem__(self, key, value):
		data = getdict(self.dbno, self.keyname)
		data[key] = value
		setdict(self.dbno, self.keyname, data)


def hapus(r, keys):
	return r.delete(keys)


def masuk(r, key, values, depan=True):
	"""
	https://pythontic.com/database/redis/list
	lpush masuk di head ~ insert(0, ..)
	rpush masuk di tail
	"""
	if not depan:
		r.rpush(r, key, *values)
	else:
		r.lpush(r, key, *values)


def keluar(r, key, depan=True):
	if not depan:
		return r.rpop(key)
	return r.lpop(key)


def didalam(r, key):
	return r.llen(key)


def ubah(r, listkey, index, value):
	return r.lset(listkey, index, value)


def terletak(r, key, index=0):
	"""
	lpush(kota, 'jakarta', 'bandung', 'surabaya')
	lindex       0          1          2
	"""
	return r.lindex(index)


def ltrim(r, listkey, values):
	return r.ltrim(listkey, *values)


def rtrim(r, listkey, values):
	return r.rtrim(listkey, *values)


def ada(r, names):
	return r.exists(names)


def search_keys(r, pattern, decode=False):
	if decode:
		return [item.decode() for item in r.keys(pattern)]
	return r.keys(pattern)


def search_keys_cached(pattern, dbno=7):
	"""
	pengen bisa cepat search keyword spt ULIBPY_ROOTDIR*stream.py.mk* dsb
	"""
	r = savedconn(dbno)
	# print(f'r adlh {r} dg kunci sebanyak {len(r.keys("*"))}')
	return search_keys(r, pattern, decode=True)


def search_bongkar(pattern, dbno=7):
	"""
	pengen bisa cepat search keyword spt ULIBPY_ROOTDIR*stream.py.mk* dsb
	"""
	from .stringutils import bongkar_string
	pattern2 = bongkar_string(pattern)
	# utk redis, \ gak bisa sendiri
	pattern2 = pattern2.replace('\\', '\\\\')
	# print(f'[redisutils] input: [{pattern}], output: [{pattern2}]')
	r = savedconn(dbno)
	return search_keys(r, pattern2, decode=True)


def search_values(r, pattern: str, start=0, limit=10000):
	result = []
	all = r.keys('*')
	if limit and len(all)>limit:
		all = all[start:start+limit]
	for k in all:
		v = r.get(k)
		if pattern in v:
			entry = (k, v)
			result .append(entry)

	return result


def load_file_content(r, basedir: str):
	allfiles = walk_fullpath(basedir, skip_ends=['.pyc'])
	for filepath in allfiles:
		kasih(r, filepath, file_content(filepath))

	indah4(f"{len(allfiles)} files loaded", warna='white')


# next = lpush/rpush/lrange, sadd/smembers, hmset/hgetall


def push(value):
	# lush(queuename, value)
	pass


def pop():
	# lrange(queuename, 0, 0)
	# rpop(queuename)
	# brpop(queuename, timeout=0)
	# ada juga lmove dan blmove sbg pengganti rpop dan brpop utk pattern reliable queue
	pass


def handle_publish_to_redis(message: str):
	channel = 'quicklang_channel'
	configkey = 'quicklang_redisconfig'
	from schnell.gui.system.searcher.make_redis_help import try_redis_connect_return
	r = try_redis_connect_return(configkey, db=0)
	r.publish(channel, message.encode())
