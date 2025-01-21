import json, os, re, redis, time

from schnell.db.mapper import map_input
from schnell.db.redis_config import redis_config
from schnell.db.search import (
	search_algo1,
	search_algo2,
	search_algo3,
)
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import isfile, walk_fullpath
from schnell.app.fileutils import (
	get_daftar,
	get_definition_by_key_permissive_start,
	get_definition_by_key_permissive_start_with_lineno,
)
from schnell.app.osutils import is_linux_path_on_windows_and_convert
from schnell.app.printutils import print_list_warna, indah4
from schnell.app.utils import env_get, env_int, perintahsp_simple



algorithm = {
	'1': search_algo1,
	'2': search_algo2,
	'3': search_algo3,
}

SubKey = 'Sub'
PubKey = 'Pub'


curdir = os.path.dirname(__file__)
default_ulibpy_snippets = os.path.normpath(os.path.join(curdir, '..'))
default_ulibpy_databasedir = os.path.normpath(os.path.join(curdir, '../../database'))
default_ulibpy_bylangsdir = os.path.normpath(os.path.join(curdir, '../../database/by-langs/'))
default_refcards = os.path.normpath(os.path.join(default_ulibpy_databasedir, 'refcards'))
default_geura = os.path.normpath(os.path.join(default_ulibpy_databasedir, 'geura'))
default_ageh = os.path.normpath(os.path.join(default_ulibpy_databasedir, 'ageh'))
# C:\Users\usef\work\sidoarjo\database\quicks\languages\typescript
default_quicks = os.path.normpath(os.path.join(default_ulibpy_databasedir, 'quicks'))

default_ulibpy_search_algo = '3'
default_rediscontainername='fmus2'
SEARCH_ALGO_INDEX = programming_data['j']['schnell']['app']['configuration']['ULIBPY_SEARCH_ALGO']
# SEARCH_ALGO_INDEX=env_get('ULIBPY_SEARCH_ALGO', default_ulibpy_search_algo)
# def searcher():
# 	SEARCH_ALGO = env_get('ULIBPY_SEARCH_ALGO')
# 	return algorithm[SEARCH_ALGO]
pengurutan = lambda tempres, keylist: algorithm[SEARCH_ALGO_INDEX](tempres, keylist)

# utk ULIBPY_REDISKEY_SHORTVIEW
SNIPPETSDIR = programming_data['j']['schnell']['app']['configuration']['ULIBPY_SNIPPETS']
BYLANGSDIR = programming_data['j']['schnell']['app']['configuration']['ULIBPY_BYLANGSDIR']
CREATORDBDIR = programming_data['j']['schnell']['app']['configuration']['ULIBPY_CREATORDBDIR']
wiekesym = programming_data['j']['schnell']['app']['configuration']['ULIBPY_WIEKES_TEMPLATE_PREFIX']
# SNIPPETSDIR = env_get('ULIBPY_SNIPPETS', default_ulibpy_snippets)
# BYLANGSDIR = env_get('ULIBPY_BYLANGSDIR', default_ulibpy_bylangsdir)
# CREATORDBDIR = env_get('ULIBPY_CREATORDBDIR', r'C:\Users\usef\work\sidoarjo\schnell\creator\createdb')
# wiekesym = env_get('ULIBPY_WIEKES_TEMPLATE_PREFIX', '__wieke')

shortens = {
	'$': SNIPPETSDIR,
	'@': BYLANGSDIR,
}
shorten_keys = list(shortens.keys())
# there are no duplicate values
# https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
replacens = dict(zip(shortens.values(), shortens.keys()))
key_delimiter = ':'


def get_connection(conn='r'):
	"""
	database r0 utk pub/sub yg https://github.com/luin/ioredis/issues/74
	butuh db no 0
	[[object Object]]ERR invalid DB index

	ReplyError: ERR invalid DB index
	at parseError (/home/usef/danger/ulib/schnell/terminal/js/vscode-ext/
	node_modules/redis-parser/lib/parser.js:179:12)
	"""
	return redis_config[conn]


def redis_connect(host=None, port=None, db=None, password=None):
	"""
	utk aplikasi terpisah, env_load() terlebih dahulu, baru panggil fungsi ini
	"""
	if host is None:
		host = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_HOST'] # env_get('ULIBPY_REDIS_HOST', 'localhost')
	if port is None:
		port = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_PORT'] # env_int('ULIBPY_REDIS_PORT', 6380)
	if db is None:
		db = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_DBNO'] # env_int('ULIBPY_REDIS_DBNO', 0)

	conn_params = {
		'host': host,
		'port': port,
		'db': db,
	}
	if password is not None:
		conn_params.update({
			'password': password,
		})

	# redis_cloud = 'redis://default:scgMpVthMe3em4Uv1qWzY4tN2TkeZ0Mc@redis-14126.c295.ap-southeast-1-1.ec2.redns.redis-cloud.com:14126'
	redis_cloud_ulumus = 'redis://default:WCK5eUXksSwS1ieJC2zZs05Rlm7nliAd@redis-19975.c89.us-east-1-3.ec2.redns.redis-cloud.com:19975'
	# r = redis.Redis(**conn_params)
	# r = redis.Redis(redis_cloud)
	r = redis.Redis.from_url(redis_cloud_ulumus)
	return r


def try_redis_connect():
	redis_config['r'] = redis_connect()
	# https://stackoverflow.com/questions/12857604/python-how-to-check-if-redis-server-is-available
	redis_config['r'].ping()
	redis_config['pub'] = redis_connect(db=0)
	redis_config['sub'] = redis_connect(db=0)
	# return redis_config['r']


def redis_publish(data, channel, r=None):
	if not r:
		r = get_connection('pub')

	r.publish(channel, json.dumps(data))


def docker_start_redis():
	redisname = programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDIS_CONTAINERNAME'] # env_get('ULIBPY_REDIS_CONTAINERNAME', default_rediscontainername)
	indah4('starting redis...', warna='yellow')
	perintahsp_simple(f'docker start {redisname}')
	time.sleep(0.5)
	indah4('...started now', warna='yellow')
	perintahsp_simple('docker ps')


def load_mkfile_to_redis(r, filepath):
	for baris_kunci in get_daftar(filepath):
		superkey = f"{filepath}:{baris_kunci}"
		supervalue = 1
		r.set(superkey, supervalue)


def load_bylangs_internal(r, langsdir, filtered='.mk'):
	# print(f"""load_bylangs_internal
	# langsdir={langsdir}
	# filtered={filtered}
    # """)
	if filtered:
		if isinstance(filtered, list):
			allfiles = walk_fullpath(langsdir, filtered_end_list=filtered)
		else:
			allfiles = walk_fullpath(langsdir, filtered_ends=filtered)
	else:
		allfiles = walk_fullpath(langsdir)

	# print(f'load_bylangs_internal {filtered} allfiles:', allfiles)
	for filekey in allfiles:
		# print(f'loading {filekey}')
		for baris_kunci in get_daftar(filekey):
			# print(f'\t{baris_kunci}')
			superkey = f"{filekey}:{baris_kunci}"
			# supervalue = get_definition_by_key_permissive_start(filekey, baris_kunci)
			# 19-7-2022, utk percepat, dan krn value gak dipake
			supervalue = 1
			r.set(superkey, supervalue)


def load_bylangs(r, with_snippets=True, langsdir = None):
	load_bylangs_internal(r, langsdir if langsdir else BYLANGSDIR)
	# geura, ageh, refcards
	# load_bylangs_internal(r, langsdir, filtered='.mk')
	# for folder in [default_quicks, default_ageh, default_geura, default_refcards]:
	if not langsdir:
		for folder in programming_data["j"]["schnell"]["db"]["myredis_common"]["load_bylangs_folder"]:
			load_bylangs_internal(r, folder, filtered=programming_data["j"]["schnell"]["db"]["myredis_common"]["load_bylangs_filtered_extensions"])
	else:
		load_bylangs_internal(r, langsdir, filtered=programming_data["j"]["schnell"]["db"]["myredis_common"]["load_bylangs_filtered_extensions"])
	if with_snippets:
		'''
		utk snippets hanya .mk file yg kita proses
		'''
		langsdir = SNIPPETSDIR
		load_bylangs_internal(r, langsdir, filtered=programming_data["j"]["schnell"]["db"]["myredis_common"]["load_bylangs_filtered_extensions"])


def all_redis_keys(r):
	return [item.decode('utf8') for item in r.keys('*')]


def redis_keys_recurse(r, cari, sort=False, mapper=False):
	"""
	tujuan: jk cari pattern terdiri dari bbrp keyword terpisah spasi
	kita pengen kembalikan redis keys yg punya semua item dlm pattern
	mengingat ini gak jalan jk lempar/kasih as is/literally whole pattern
	--
	recurse ini misnomer	
	misal:
	redis_keys_recurse(r, 'satu dua tiga')
	kita cari 'satu' -> res0
	lalu cari 'dua' dalam res0 -> res1
	lalu cari 'tiga' dlm res1 -> res2
	kembalikan res2
	"""
	if mapper:
		cari = map_input(cari)
		# from .mapper import input_mapper
		# for k,v in input_mapper.items():
		#   cari = cari.replace(k, v)
		# print('input after mapper:', cari)

	# tempres = []
	keylist = cari.split()

	# for kunci in keylist:
	# 	if not tempres:
	# 		tempres = [item.decode('utf8') for item in r.keys(f'*{kunci}*')]
	# 	else:
	# 		tempres = [item for item in tempres if kunci in item]
	kuncis = all_redis_keys(r)
	antipatterns = [item.removeprefix('-') for item in keylist if re.match(r'^-[\w\d]+', item)]
	patterns = [item for item in keylist if not re.match(r'^-[\w\d]+', item)]
	# print(f"keylist: {keylist}, anti {antipatterns} pat {patterns}")
	# /flutter create -> semua flutter dapat krn create diperoleh dari createdb
	# potongawalan = '/home/usef/danger/ulib/schnell/creator/createdb'
	potongawalan = CREATORDBDIR
	# tempres = filter(lambda fullpath: all([item in fullpath for item in patterns]), kuncis)
	tempres = filter(lambda fullpath: all([item in fullpath.removeprefix(potongawalan) \
		for item in patterns]), kuncis)
	if antipatterns:
		# tempres = filter(lambda fullpath: all([item not in fullpath for item in antipatterns]), tempres)
		tempres = filter(lambda fullpath: all([item not in fullpath.removeprefix(potongawalan) \
			for item in antipatterns]), tempres)
	tempres = list(tempres)
	# print(f"result: {tempres[:10]} sebanyak {len(tempres)}")

	# if env_int('ULIBPY_REDISKEY_SHORTVIEW', 1):
	if programming_data['j']['schnell']['app']['configuration']['ULIBPY_REDISKEY_SHORTVIEW']:
		# prefix = env_get('ULIBPY_BYLANGSDIR')
		# tempres = [item.removeprefix(prefix) for item in tempres]
		tempres = [item \
			.replace(BYLANGSDIR, replacens[BYLANGSDIR]) \
			.replace(SNIPPETSDIR, replacens[SNIPPETSDIR]) \
			for item in tempres]

	# jk semua entry keylist ada di bagian filepath (filepath:baris_cari) maka dia muncul lebih atas
	# coba review algo di sini
	# katanya pengen item di keylist ada di filepath (sama dengan PLUS subset/in)
	# lebih baik lagi jk filepath nya paling pendek
	# tempres = search_algo1(tempres, keylist)
	# tempres = search_algo2(tempres, keylist)
	# coba disable 13/12/22
	# tempres = search_algo3(tempres, keylist)
	tempres = pengurutan(tempres, keylist)
	# pprint.pprint(tempres)

	if sort:
		return sorted(tempres)

	return tempres


def redis_value_recurse(r, key, key_delimiter=':', mapper=False, is_fullkey=False, print_keys=False, REPL=None, get_from_db=False):
	"""
	selalu kembalikan list
	terima 
	string is_fullkey=F (default) -> hrs r.keys dulu
	atau
	string is_fullkey=T -> sudah berbentuk filepath:baris_cari
	"""
	if not is_fullkey:
		full_key = redis_keys_recurse(r, key, sort=False, mapper=mapper)
		if not full_key:
			return None

		if print_keys:
			print_list_warna(full_key)
	
		full_key = full_key[0]
	else:
		full_key = key
		# print('input fullkey:', full_key)

	# jk full_key dimulai dg C: maka kita split dari ... yg kedua...
	filepath, baris_cari = full_key.split(key_delimiter, 1)
	if full_key.lower().startswith('c:'):
		from schnell.app.stringutils import split_by_pos
		# : pertama = C: of filepath
		# : kedua baru filepath:baris_cari
		pecah = split_by_pos(full_key, key_delimiter, 2)
		# print('pecah', pecah)
		filepath, baris_cari = pecah

	if get_from_db:
		superkey = f"{filepath}:{baris_cari}"
		result = r.get(superkey)
		if REPL:
			REPL.last_file = filepath
		return result
	elif isfile(filepath):
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print(f'[db.myredis][redis_value_recurse] {filepath}:{baris_cari}')
		# return get_definition_by_key_permissive_start(filepath, baris_cari)
		result, lineno = get_definition_by_key_permissive_start_with_lineno(filepath, baris_cari)
		if REPL:
			REPL.last_file = filepath
			REPL.last_lineno = lineno
		return result
	else:
		islinuxpath, wslfilepath = is_linux_path_on_windows_and_convert(filepath)
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			indah4(f"""[myredis][redis_value_recurse]
			NOT get_from_db
			NOT isfile(filepath) = {filepath} = {isfile(filepath)}
			islinuxpath, wslfilepath = {islinuxpath}, {wslfilepath}
			""", warna='magenta', layar='green')
		if islinuxpath:
			result, lineno = get_definition_by_key_permissive_start_with_lineno(wslfilepath, baris_cari)
			if REPL:
				REPL.last_file = wslfilepath
				REPL.last_lineno = lineno
			return result

	return None


def redis_get_daftar(r, key, key_delimiter=':'):
	full_key = redis_keys_recurse(r, key)
	if not full_key:
		return None
	full_key = full_key[0]
	# di sini full_key adlh b'', hrs konversi dulu ke str
	if isinstance(full_key, (bytes, bytearray)):
		full_key = full_key.decode('utf8')
	filepath, baris_cari = full_key.split(key_delimiter, 1)
	return get_daftar(filepath)

