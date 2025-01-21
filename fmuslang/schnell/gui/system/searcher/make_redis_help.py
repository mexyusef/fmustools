import json, os, re, redis
from pprint import pprint
# import time

if __name__ == 'make_redis_help':
	from filehelper import walk_fullpath, bongkar
else:
	from schnell.gui.system.searcher.filehelper import walk_fullpath, bongkar

DEFAULT_DB = 8

redis_config = {
	'r'					: None,
	'r2'				: None,
	'r3'				: None,
	'pub'				: None,
	'sub'				: None,
	'from_client'		: 'ulang',
	'from_server'		: 'ulang/fromserver',
	'search_service'	: 'ulang/search_service',
	'mapper_service'	: 'ulang/mapper_service',

    'scheduler'         : 'kanal/scheduler',
    'command'           : 'kanal/command',

	'request_kanal' 	: "replservice_request",
	'response_kanal' 	: "replservice_response",
}

# redis_config['r'] = redis_connect()
# # https://stackoverflow.com/questions/12857604/python-how-to-check-if-redis-server-is-available
# redis_config['r'].ping()
# redis_config['pub'] = redis_connect(db=0)
# redis_config['sub'] = redis_connect(db=0)

# for filekey in allfiles:
# 	# print(f'loading {filekey}')
# 	for baris_kunci in get_daftar(filekey):
# 		# print(f'\t{baris_kunci}')
# 		superkey = f"{filekey}:{baris_kunci}"
# 		supervalue = get_definition_by_key_permissive_start(filekey, baris_kunci)
# 		# print(f'\t\t{supervalue[:50]}')
# 		r.set(superkey, supervalue)


# a = redis_keys_recurse(redis_config['r'], code, mapper=True)
# if (is_choosing is not None) and (0<=is_choosing<=len(a)):
#     filepath = a[is_choosing]
#     filepath_filepart, filepath_barispart = filepath.split(':', 1)
#     b = redis_value_recurse(redis_config['r'], filepath, print_keys=True, is_fullkey=True, REPL=REPL)
#     indah3(b)


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


def get_cached_connection(conn='r', db=0):
	"""
	kembalikan redis_config[conn]
	"""	
	print(f"get_cached_connection, conn = {conn}, db = {db}")
	if conn in redis_config and redis_config[conn]:
		return redis_config[conn]
	print(f"get_cached_connection, try_redis_connect")
	r = try_redis_connect_return(conn, db)
	# time.sleep(1.0)
	return r


def get_cached_pubsub(conn='r', db=0):
	r = get_cached_connection(conn, db)
	return r.pubsub()


def env_int(kunci):
	if kunci in os.environ:
		return int(os.environ[kunci])
	return 0


def env_get(kunci, default=None):
	if kunci in os.environ:
		return os.environ[kunci]
	return default


def redis_connect(host='localhost', port=6379, db=DEFAULT_DB, password=None):
	"""
	utk aplikasi terpisah, env_load() terlebih dahulu, baru panggil fungsi ini
	"""
	# if host is None:
	# 	host = env_get('ULIBPY_REDIS_HOST')
	# if port is None:
	# 	port = env_int('ULIBPY_REDIS_PORT')
	# if db is None:
	# 	db = env_int('ULIBPY_REDIS_DBNO')

	conn_params = {
		'host': host,
		'port': port,
		'db': db,
	}
	if password is not None:
		conn_params.update({
			'password': password,
		})

	r = redis.Redis(**conn_params)
	return r


def redis_keys(r, cari=None, sort=True):
	if cari is None:
		kuncis = r.keys('*')
	else:
		kuncis = r.keys(f'*{cari}*')

	kuncis = [item.decode('utf8') for item in kuncis]

	if sort:
		return sorted(kuncis)

	return kuncis


def all_redis_keys(r, keys='*'):
	return [item.decode('utf8') for item in r.keys(keys)]


def try_redis_connect(rconn = 'r', db=DEFAULT_DB):
	redis_config[rconn] = redis_connect(db=db)
	# https://stackoverflow.com/questions/12857604/python-how-to-check-if-redis-server-is-available
	redis_config[rconn].ping()


def try_redis_connect_return(rconn = 'r', db=DEFAULT_DB):
	redis_config[rconn] = redis_connect(db=db)
	# https://stackoverflow.com/questions/12857604/python-how-to-check-if-redis-server-is-available
	redis_config[rconn].ping()
	return redis_config[rconn]


def try_pubsub_connect():
	redis_config['pub'] = redis_connect(db=0)
	redis_config['sub'] = redis_connect(db=0)


def get_definition_exactline_aslist(filepath, start_regex, end_regex):

	result = []
	collecting = False
	with open(filepath, encoding='utf-8') as fd:
		for line in fd.readlines():
			# print(f"""proses baris [{line}] dg start [{start_regex}] dan end [{end_regex}]""")
			try:
				if collecting:
					if re.search(end_regex, line):
						# print(f"""proses baris [{line}] dg start [{start_regex}] dan end [{end_regex}]""")
						return result
					result.append( line )
				else:
					# if start_line in line:
					if re.search(start_regex, line):
						collecting = True
			except Exception as err:
				"""
				"""
				print('// get_definition_exactline_aslist mengalami exception:', err)
				print(f"""
				filepath: {filepath}
				baris: {line}
				start_regex: {start_regex}
				end_regex: {end_regex}
				""")
	return result


def get_definition_by_key_permissive_start(filepath, baris, kunci_start='^--%', kunci_end='^--#', debug=False):
	"""
	berikut ini versi restrictive:
	start_regex_modified = f'^{kunci}\s+{baris}\s+$'
	"""
	# kadang baris berisi + yg dimakan oleh regex
	if '\\' in baris:
		baris = baris.replace('\\', '\\\\')
	if '+' in baris:
		baris = baris.replace('+', '\+')
	if '*' in baris:
		baris = baris.replace('*', '\*')
	if '(' in baris:
		baris = baris.replace('(', '\(')
	if ')' in baris:
		baris = baris.replace(')', '\)')
	if '[' in baris:
		baris = baris.replace('[', '\[')
	if ']' in baris:
		baris = baris.replace(']', '\]')
	if '{' in baris:
		baris = baris.replace('{', '\{')
	if '}' in baris:
		baris = baris.replace('}', '\}')
	if '?' in baris:
		baris = baris.replace('?', '\?')
	if '|' in baris:
		baris = baris.replace('|', '\|')
	# if '=' in baris:
	# 	baris = baris.replace(')', '\=')
	# if ':' in baris:
	# 	baris = baris.replace(')', '\:')
	# if '"' in baris:
	# 	baris = baris.replace(')', '\"')
	# if filepath.endswith('.mk'):
	# 	kunci_start = '^--%'
	# 	kunci_end = '^--#'

	start_regex_modified = f'{kunci_start}\s+{baris}'
	if env_int('ULIBPY_FMUS_DEBUG') > 1:
		print(f'[fileutils] get_definition_by_key_permissive_start {filepath}: [{start_regex_modified}...{kunci_end}]')
	definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)
	if len(definisi) == 0:
		start_regex_modified = f'{kunci_start}\s+(.*){baris}'
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print('hasil get_definition_exactline_aslist #1 berpanjang:', \
				len(definisi), \
				f'coba lagi dg modify start regex menjadi {start_regex_modified}')
		definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)
	if env_int('ULIBPY_FMUS_DEBUG') > 1:
		print('[fileutils] hasil get_definition_exactline_aslist berpanjang:', len(definisi))
	return ''.join(definisi)


def split_by_pos(strng, sep, pos):
    """
    https://stackoverflow.com/questions/36300158/split-text-after-the-second-occurrence-of-character

    >>> strng = 'some-sample-filename-to-split'
    >>> split(strng, '-', 3)
    ('some-sample-filename', 'to-split')
    >>> split(strng, '-', -4)
    ('some', 'sample-filename-to-split')
    >>> split(strng, '-', 1000)
    ('some-sample-filename-to-split', '')
    >>> split(strng, '-', -1000)
    ('', 'some-sample-filename-to-split')
    """
    strng = strng.split(sep)
    return sep.join(strng[:pos]), sep.join(strng[pos:])


def isdir(filepath, do_bongkar=True, strip=False):
	if strip:
		filepath = filepath.strip()
	if do_bongkar:
		# return os.path.isdir(bongkar(filepath))
		pecah = bongkar(filepath)
		false_or_path = os.path.isdir(pecah)
		if false_or_path:
			# kembalikan full path hasil bongkar
			return pecah
		return false_or_path
	return os.path.isdir(filepath)


def search_algo3(tempres, keylist):
	r"""
	/QTreeWid
	repl run() err: string index out of range
	Traceback (most recent call last):
	File "C:\Users\usef\work\sidoarjo\schnell\creator\repl.py", line 301, in run
		self.process(text)
	File "C:\Users\usef\work\sidoarjo\schnell\creator\repl.py", line 395, in process
		redis_repl(code, self)
	File "C:\Users\usef\work\sidoarjo\schnell\db\myredis.py", line 963, in redis_repl
		a = redis_keys_recurse(redis_config['r'], code, mapper=True)
	File "C:\Users\usef\work\sidoarjo\schnell\db\myredis.py", line 195, in redis_keys_recurse
		tempres = search_algo3(tempres, keylist)
	File "C:\Users\usef\work\sidoarjo\schnell\db\search.py", line 24, in search_algo3
		return sorted(tempres, key=lambda item:item.split(':', 1)[0].count('/')*100 + ord(item.split(':', 1)[0][1]))
	File "C:\Users\usef\work\sidoarjo\schnell\db\search.py", line 24, in <lambda>
		return sorted(tempres, key=lambda item:item.split(':', 1)[0].count('/')*100 + ord(item.split(':', 1)[0][1]))
	IndexError: string index out of range

	di sini ada \\ tapi gak ada /
	121. C:\Users\usef\work\sidoarjo\database\refcards\pyqt5_references.mk:QTreeWidget

	walau ini berhasil, tapi gagal "baca"
	/QTreeWid/0 <- gak berhasil baca...
	"""
	try:
		return sorted(tempres, key=lambda item:item.split(':', 1)[0].count('/')*100 + ord(item.split(':', 1)[0][1]))
	except:
		return sorted(tempres)


def redis_keys_recurse(r, cari, sort=False, mapper=False, search_algo=False):
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
	potongawalan = env_get('ULIBPY_CREATORDBDIR', '')
	# tempres = filter(lambda fullpath: all([item in fullpath for item in patterns]), kuncis)
	tempres = filter(lambda fullpath: all([item in fullpath.removeprefix(potongawalan) \
		for item in patterns]), kuncis)
	if antipatterns:
		# tempres = filter(lambda fullpath: all([item not in fullpath for item in antipatterns]), tempres)
		tempres = filter(lambda fullpath: all([item not in fullpath.removeprefix(potongawalan) \
			for item in antipatterns]), tempres)
	tempres = list(tempres)
	# print(f"result: {tempres[:10]} sebanyak {len(tempres)}")

	# if env_int('ULIBPY_REDISKEY_SHORTVIEW'):
	# 	# prefix = env_get('ULIBPY_BYLANGSDIR')
	# 	# tempres = [item.removeprefix(prefix) for item in tempres]
	# 	tempres = [item \
	# 		.replace(BYLANGSDIR, replacens[BYLANGSDIR]) \
	# 		.replace(SNIPPETSDIR, replacens[SNIPPETSDIR]) \
	# 		for item in tempres]

	# jk semua entry keylist ada di bagian filepath (filepath:baris_cari) maka dia muncul lebih atas
	# coba review algo di sini
	# katanya pengen item di keylist ada di filepath (sama dengan PLUS subset/in)
	# lebih baik lagi jk filepath nya paling pendek
	# tempres = search_algo1(tempres, keylist)
	# tempres = search_algo2(tempres, keylist)
	if search_algo:
		tempres = search_algo3(tempres, keylist)
	# tempres = pengurutan(tempres, keylist)
	# pprint.pprint(tempres)

	if sort:
		return sorted(tempres)

	return tempres


def redis_deletes(r, cari, recurse=False, confirm=True):
	"""
	https://stackoverflow.com/questions/21975228/redis-python-how-to-delete-all-keys-according-to-a-specific-pattern-in-python

	for key in x: cache.delete(key)

	Using redis-python package you can do that such way: cache.delete(*keys)
	"""
	if recurse:
		kuncis = redis_keys_recurse(r, cari)
	else:
		kuncis = redis_keys(r, cari)
	
	if kuncis:
		if confirm:
			try:
				pprint(kuncis)
			except:
				'''[BlockingIOError: [Errno 11] write could not complete without blocking]
				File "/home/usef/work/sidoarjo/schnell/db/myredis.py", line 122, in redis_deletes
					pprint(kuncis)
				File "/home/usef/.local/lib/python3.9/site-packages/rich/pretty.py", line 925, in pprint
					_console.print(
				File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 1683, in print
					self._buffer.extend(new_segments)
				File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 838, in __exit__
					self._exit_buffer()
				File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 796, in _exit_buffer
					self._check_buffer()
				File "/home/usef/.local/lib/python3.9/site-packages/rich/console.py", line 2005, in _check_buffer
					self.file.write(text)
				'''				
				pprint(kuncis)
			print(f"""[myredis][redis_deletes] Sure to delete ({len(kuncis)} items) ? """, end='')
			yesno = input(' ')
			if yesno.lower() == 'y':
				r.delete(*kuncis)
		else:
			r.delete(*kuncis)


def redis_clear_db(r, all_db=False):
	if all_db:
		r.flushall()
		return 1
	
	r.flushdb()
	return 1


# as []
def skip_lines_aslines(filepath, baris_regex, isFiltering=False):
	"""
		isFilter = filter bukan skip
		baris_regex = "^#"

		kita kadang:
		- hilangkan lines diawali #
		- hanya ambil lines berawal --
	"""
	filtered = []
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
		for line in content:
			m = re.match(baris_regex, line)
			if (not m and not isFiltering) or (m and isFiltering):
				filtered.append(line)
	
	return filtered


# as []
def filter_lines_transform_aslines(filepath, baris_regex, transformer=lambda baris:baris.replace('#', '', 1)):
	"""
	2 operasi:
		filter lines dan peroleh [baris1, baris2, ...]
			contoh: 
			--% entry1
			--% entry2
			menjadi:
			[--% entry1, --% entry2]
		petakan item dg transformer, misal:
			[entry1, entry2]
	"""
	hasil = skip_lines_aslines(filepath, baris_regex, isFiltering=True)
	return list(map(transformer, hasil))


def get_daftar(filepath, kunci='--%', stringified=False):
	"""
	get baris2 kunci yg diawali dg kunci
	kembalikan ter-transform tanpa kunci => berupa list entries
	"""
	# utk re.match
	FILTER_CONDITION = f'^{kunci}\s+'

	def transformer(baris):
		"""
		hapus --%\s+ di awal entry
		"""
		return baris.replace(kunci, '', 1).strip()
	
	content = filter_lines_transform_aslines(filepath, FILTER_CONDITION, transformer)
	if stringified:
		return '\n'.join(content)
	return content


def redis_publish(data, channel=None, r=None):
	"""
	digunakan oleh make_repl utk ngirim request repl_service ke kbrepl
	"""
	if not channel:
		channel = 'replservice_request'
	if not r:
		r = get_connection('pub')  # redis_config['pub]
		if not r:
			print(f"r = get_connection('pub') gagal dapatkan r")
			r = redis_connect() # bener gak nih? 11-dec-22

	r.publish(channel, json.dumps(data))


def load_bylangs_internal(r, langsdir, filtered='.mk'):
	if filtered:
		allfiles = walk_fullpath(langsdir, filtered_ends=filtered)
	else:
		allfiles = walk_fullpath(langsdir)
	
	# print(f'load_bylangs_internal {filtered} allfiles:', allfiles)
	for filekey in allfiles:
		# print(f'loading {filekey}')
		for baris_kunci in get_daftar(filekey):
			# print(f'\t{baris_kunci}')
			superkey = f"{filekey}:{baris_kunci}"
			supervalue = get_definition_by_key_permissive_start(filekey, baris_kunci)
			# print(f'\t\t{supervalue[:50]}')
			r.set(superkey, supervalue)


def load_bylangs(r, with_snippets=True, langsdir = env_get('ULIBPY_BYLANGSDIR')):
	load_bylangs_internal(r, langsdir)
	if with_snippets:
		'''
		utk snippets hanya .mk file yg kita proses
		'''
		langsdir = env_get('ULIBPY_SNIPPETS')
		load_bylangs_internal(r, langsdir, filtered='.mk')


def clearload(code=r'c:\Users\usef\work\sidoarjo\database\refcards', rconn = 'r2'):
	"""
	gak pake default spt aslinya, hrs specify code/dirpath berisi mk files
	"""
	if code:
		if isdir(code):
			newpath = isdir(code)
			redis_deletes(redis_config[rconn], f'{newpath}*', confirm=False)
			load_bylangs(redis_config[rconn], with_snippets=False, langsdir=newpath)
			print(f'[myredis] clear + load {newpath}...')
		else:
			print(f'[myredis] {code} is not dir')
	# else:
	# 	redis_clear_db(redis_config['r'])
	# 	load_bylangs(redis_config['r'])
	# 	print('[myredis] clear + load...')


def clear_db_7():
	redis_connect(db=7).flushdb()
	return 1


def clear_db_8():
	redis_config['r2'].flushdb()
	return 1


def clear_db_9():
	redis_config['r3'].flushdb()
	return 1

