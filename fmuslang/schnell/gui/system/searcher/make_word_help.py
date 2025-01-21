import os, re, string, sys

# from .config import (
# 	KUNCI,
#     PENGGANTI,
#     VOCALS,
# 	MAXIMUM_ZAU,
# 	mmm_zau_folder,
# )


if __name__ == 'make_word_help':
	from filehelper import walk_fullpath, file_content
	from make_redis_help import redis_config, try_redis_connect, redis_deletes
else:
	from gui.system.searcher.filehelper import walk_fullpath, file_content
	from gui.system.searcher.make_redis_help import redis_config, try_redis_connect, redis_deletes


mmm_zau_folder    = r'c:\work\flaskfaker\flaskapp\mmm\zau'
PYWALKER_PREFIX='englisch:'
KUNCI       = '►'
VOCALS      = ['A','E','I','O','U']
PENGGANTI = [
  "a'", # 65+
  "b'", # 67+
  "c'", # 70+
  "d'", # 72+
  "e'", # 75+
  "f'", # 77+
]

MAXIMUM_ZAU = 649 # ZUU
CACHED_RESULT = []




def number_filepath(angka):
	"""
	angka hrs int, jk str alignment error
	"""
	angka = int(angka) if not isinstance(angka, int) else angka
	return os.path.join(mmm_zau_folder, f'{angka:03}.txt')


def zau_all_filepaths(start=0, end=999):
	return [number_filepath(item) for item in range(start,end+1)]


def file_lines(filepath, strip_newline=False, skip_emptylines=False):
	"""
	retval [line1, line2, ...]
	"""
	content = None
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	if skip_emptylines:
		content = [item for item in content if item.strip()]

	if strip_newline:
		return [item.rstrip() for item in content]
	else:		
		return content


def get_words_in_file(filepath):
	"""
	ini sama dg get_daftar...
	"""
	result = []
	if not os.path.isfile(filepath):
		return None

	content = file_lines(filepath)

	for line in content:
		m = re.search(f'{KUNCI}\\s*(.*)$', line)
		if m and m.group(1):
			word = m.group(1).strip()
			result.append(word)

	return result


def get_all_words_in_existing_files(reload=False):
	global CACHED_RESULT

	if reload:
		CACHED_RESULT = []

	if not CACHED_RESULT:
		for filepath in zau_all_filepaths(0,999):
			if os.path.isfile(filepath):
				CACHED_RESULT += get_words_in_file(filepath)

	return CACHED_RESULT


def punctuation_in_string(text, with_space = False):
	allow_underscore = string.punctuation.replace('_', '')
	if with_space:
		allow_underscore += ' '
	return [kar in allow_underscore for kar in text]


def get_first_punctuation_index(text, with_space = False):
	nonwords = r'[^\w]+'
	if with_space:
		nonwords = r'[^\w\s]+'
	all = re.findall(nonwords, text)
	# print('all puncs', all)
	if all:
		return text.index(all[0])
	return None


def word_to_zau(word, stringify=False):
	"""
	sequential menjadi ['S','E','U'] atau 'SEU' jk stringify  
	"""
	if punctuation_in_string(word, True):
		
		idx = get_first_punctuation_index(word, True)
		# print('punctuation_in_string:', word, 'index:', idx)
		if idx:
			# print('punc pd index:', idx)
			word = word[:idx] # dari punc ke kanan abaikan...

	word = word[:1].upper() + word[1:].upper().replace('Y','I')
	fo = filter(lambda x: x in VOCALS, word[1:])
	tempres = [word[0]] + list(fo)[:2]

	if len(tempres) < 3:
		tempres += ['A']

	if stringify:
		return ''.join(tempres)

	return tempres # [word[0]] + list(fo)[:2]


def zau_to_number(zau):
	"""
	zau = ['S','E','U']
	kembalian = '123'
	"""
	zau = [item.upper() for item in zau]
	pertama = (ord(zau[0]) - ord('A')) * 25
	kedua = (VOCALS.index(zau[1])) * 5
	ketiga = VOCALS.index(zau[2])
	return pertama + kedua + ketiga


def number_to_zau(angka, asstring=False):
	angka = int(angka)

	if angka > MAXIMUM_ZAU:
		return angka

	index_z = int(angka / 25) + ord('A')
	try:
		if index_z > ord('Z'):
			index_z -= ord('Z') + 1
			z = PENGGANTI[index_z]
		else:
			z = chr( index_z )
	except:
		return angka
	sisa = angka % 25
	a = VOCALS[int(sisa / 5)]
	u = VOCALS[sisa % 5]
	if asstring:
		return f"{z}{a}{u}"
	return (z, a, u)


def word_to_zaunumber(word):
	return zau_to_number(word_to_zau(word))


def word_filepath(word):
	bilangan = word_to_zaunumber(word)
	filepath = number_filepath(bilangan)
	return filepath


def get_definition(filepath, word, aslist=False):
	result = []
	collecting = False
	lines = file_lines(filepath)
	for line in lines:
		
		if collecting:
			if re.search(f'{KUNCI} (.*)', line):
				# ketemu entry berikutnya, selesai collecting
				return ''.join(result)
			result.append( line )
		
		else:
			prefix_word = re.search(f'{KUNCI}\\s*({word}.*)\\s*$', line)
			if prefix_word:
				kata = prefix_word.group(1)
				bilangan = word_to_zaunumber(kata)
				print(f"{' '*40}{kata} / {bilangan}")
				collecting = True

	if aslist:
		return result
	return ''.join(result)


def get_definition_byword(word):
	# bilangan = word_to_zaunumber(word)
	# filepath = number_filepath(bilangan)
	filepath = word_filepath(word)
	# print('get_definition_byword filepath:', filepath)
	result = get_definition(filepath, word)
	# print(f'get_definition_byword {word} => {filepath} => [{result}]')
	return result


def get_all_words_in_existing_files_redis():
	check_keys = redis_config['r3'].keys(f'{PYWALKER_PREFIX}*')
	check_values = []
	if not check_keys:
		print(f"check_keys empty, nulis filesystem ke redis...START")
		check_values = get_all_words_in_existing_files()
		# harusnya berikut ini masuk ke thread/QThread 
		for pyfile in check_values:
			superkey = PYWALKER_PREFIX + pyfile
			redis_config['r3'].set(superkey, pyfile)
			# check_values.append(redis_config['r3'].get(k))
		print(f"check_keys empty, nulis filesystem ke redis...END")
	else:
		for k in check_keys:
			check_values.append(redis_config['r3'].get(k).decode('utf8'))
	return check_values


def word_load():
	# newpath = isdir(code)
	redis_deletes(redis_config['r3'], f'{PYWALKER_PREFIX}*', confirm=False)
	get_all_words_in_existing_files_redis()
	print(f'word_load selesai...')
