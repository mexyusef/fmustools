
import os, re, redis

redis_config = {
	'r'					: None,
	'pub'				: None,
	'sub'				: None,
	'from_client'		: 'ulang',
	'from_server'		: 'ulang/fromserver',
	'search_service'	: 'ulang/search_service',
	'mapper_service'	: 'ulang/mapper_service',

    'scheduler'         : 'kanal/scheduler',
    'command'           : 'kanal/command',
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


def env_int(kunci):
	if kunci in os.environ:
		return int(os.environ[kunci])
	return 0


def env_get(kunci, default=None):
	if kunci in os.environ:
		return os.environ[kunci]
	return default


def redis_connect(host='localhost', port=6380, db=7, password=None):
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


def all_redis_keys(r):
	return [item.decode('utf8') for item in r.keys(f'*')]


def try_redis_connect():
	redis_config['r'] = redis_connect()
	# https://stackoverflow.com/questions/12857604/python-how-to-check-if-redis-server-is-available
	redis_config['r'].ping()
	redis_config['pub'] = redis_connect(db=0)
	redis_config['sub'] = redis_connect(db=0)

# try_redis_connect()



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

