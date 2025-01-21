import datetime, re

from schnell.app.dirutils import (
	joiner,
	isfile, isdir,
)
from schnell.app.fileutils import (
	file_content,
	file_lines,
)
from schnell.app.greputils import system_grep, system_grep_limitchars
from schnell.app.printutils import (
	indah4
)
from schnell.app.stringutils import (
	get_first_punctuation_index,
	punctuation_in_string,
)
from schnell.app.utils import (
	ambil,
	sampling,
	perintahsp_outerr_as_shell,
)
from .config import (
	KUNCI, PENGGANTI, VOCALS,
	MAXIMUM_ZAU,
	mmm_zau_folder,
)
from .actor_handler import actor_name

CACHED_RESULT = []


def sanitize(self, line):
	bersih = line \
		.replace('(','') \
		.replace(')','') \
		.replace('?','') \
		.replace(';','') \
		.replace('\t','')
	# read_actor_result = ''
	# try:
	#   read_actor_result = bersih.encode('latin-1', 'replace') # ignore
	# except Exception as e:
	#   print(f'Eksepsi sanitizing: {e}')
	# return read_actor_result
	return bersih


def number_filepath(angka):
	"""
	angka hrs int, jk str alignment error
	"""
	angka = int(angka) if not isinstance(angka, int) else angka
	return joiner(mmm_zau_folder, f'{angka:03}.txt')


def word_filepath(word):
	bilangan = word_to_zaunumber(word)
	filepath = number_filepath(bilangan)
	return filepath


def zau_filepath(zau):
	bilangan = zau_to_number(zau)
	filepath = number_filepath(bilangan)
	return filepath


def zau_all_filepaths(start=0, end=999):
	return [number_filepath(item) for item in range(start,end+1)]


def get_daftar(zau_filepath):
	result = []
	try:
		content = file_content(zau_filepath)
		for baris in content:
			m = re.search(f'{KUNCI} (.*)', baris)
			if m:
				entry = m.group(1)
				result.append( sanitize(entry) )
	except FileNotFoundError as err:
		print(f'Eksepsi file-not-found grepper: {err}')

	except Exception as e:
		print(f'Eksepsi get_daftar: {e}')

	return result


def get_words_in_file(filepath):
	"""
	ini sama dg get_daftar...
	"""
	result = []
	if not isfile(filepath):
		return None

	content = file_lines(filepath)

	for line in content:
		m = re.search(f'{KUNCI}\\s*(.*)$', line)
		if m and m.group(1):
			word = m.group(1).strip()
			result.append(word)

	return result



# def get_words_in_file(filepath):
# 	"""
# 	filepath adlh item dari zau_all_filepaths(0,999)
# 	"""
# 	content = file_lines(filepath)

# 	result = []
# 	for line in content:
# 		m = re.search(f'{KUNCI}\\s*(.*)$', line)
# 		if m and m.group(1):
# 			word = m.group(1).strip()
# 			result.append(word)

# 	return result


def get_words_from_number(angka):
	return get_words_in_file(number_filepath(angka))


def get_words_from_zau(zau):
	return get_words_in_file(zau_filepath(zau))


def word_to_zau(word, stringify=False):
	"""
	sequential menjadi ['S','E','U'] atau 'SEU' jk stringify  
	"""
	if punctuation_in_string(word, with_space=False, allow_dash=True):
		idx = get_first_punctuation_index(word, with_space=False, allow_dash=True)
		# print('punctuation_in_string:', word, 'index:', idx)
		if idx:
			# print('punc pd index:', idx)
			word = word[:idx] # dari punc ke kanan abaikan...kita proses dari awal sampai punc

	word = word[:1].upper() + word[1:].upper().replace('Y','I')
	fo = filter(lambda x: x in VOCALS, word[1:])
	tempres = [word[0]] + list(fo)[:2]

	if len(tempres) < 3:
		tempres += ['A']

	if stringify:
		return ''.join(tempres)

	return tempres  # [word[0]] + list(fo)[:2]


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


def date_to_zau(asstring=True):
	doy = datetime.datetime.now().strftime('%j')
	return number_to_zau(doy, asstring=asstring)


def word_to_zaunumber(word):
	word_zau = word_to_zau(word)
	word_number = zau_to_number(word_zau)
	# print(f"""word_to_zaunumber => {word}
	# word_zau = {word_zau}
	# word_number = {word_number}
	#    """)
	return word_number


def get_definition(filepath, word, aslist=False, delimiter='\n'):
	result = []
	collecting = False
	lines = file_lines(filepath)
	for line in lines:
		if collecting:
			if re.search(f'{KUNCI} (.*)', line):
				# ketemu entry berikutnya, selesai collecting
				return delimiter.join(result)
			result.append( line )
		else:
			prefix_word = re.search(f'{KUNCI}\\s*({word}.*)\\s*$', line)
			if prefix_word:
				kata = prefix_word.group(1)
				bilangan = word_to_zaunumber(kata)
				indah4(f"{' '*40}{kata} / {bilangan} / {actor_name(bilangan)}", warna='yellow', layar='black')
				collecting = True

	if aslist:
		return result
	return delimiter.join(result)


def get_definition_byword(word):
	# bilangan = word_to_zaunumber(word)
	# filepath = number_filepath(bilangan)
	filepath = word_filepath(word)
	# print('get_definition_byword filepath:', filepath)
	result = get_definition(filepath, word)
	# print(f'get_definition_byword {word} => {filepath} =>\n{result}.')
	return result


def get_all_words_in_existing_files(reload=False):
	global CACHED_RESULT

	if reload:
		CACHED_RESULT = []

	if not CACHED_RESULT:
		for filepath in zau_all_filepaths(0,999):
			if isfile(filepath):
				CACHED_RESULT += get_words_in_file(filepath)

	return CACHED_RESULT


def ambil_acak(jumlah=1):
	jumlah = int(jumlah) if not isinstance(jumlah, int) else jumlah
	daftar_kata = get_all_words_in_existing_files()
	if len(daftar_kata) == 0:
		indah4(f'''[app.writers.file_handler]
		daftar kata kosong!
		coba cek folder {mmm_zau_folder}
		''', warna='cyan')
		return None
	if jumlah < 1:
		return None
	elif jumlah == 1:
		return ambil(daftar_kata)
	else:
		return sampling(daftar_kata, jumlah, stringify=True)


def is_zau(text):
	if len(text) == 3 and text[1].upper() in VOCALS and text[2].upper() in VOCALS:
		return True

	return False


def terdeteksi(cmd):
	words = get_all_words_in_existing_files()
	return [word for word in words if cmd in word]


def search_word(pattern,
	case_sensitive=False,
	horizontal_context_limit=0,
	before=0,
	after=0,
	suppress_longfoldername=True,
	no_color=False):
	"""
	system_grep(basedir, pattern, case_sensitive=False, context=0, before=0, after=0, capture=False):
	system_grep_limitchars(basedir, pattern, limit=10, case_sensitive=False, capture=False):

	horizontal_context_limit, misal nilai 10
	maksudnya mungkin /terutama
	kalau kita terutama sekali makan ayam
	     <-----|       |-----> sebanyak 10 chars ke kiri dan kanan
	krn "context" itu "vertical"

	capture: kembalikan string output, krn mau kita lempar ke vscode
	"""
	# mmm_zau_folder
	if horizontal_context_limit:
		out, err = system_grep_limitchars(mmm_zau_folder, pattern, case_sensitive=case_sensitive, limit=horizontal_context_limit, capture=True, no_color=no_color)
	else:
		out, err = system_grep(mmm_zau_folder, pattern, case_sensitive=case_sensitive, capture=True, no_color=no_color, before=before, after=after)

	if suppress_longfoldername and out:
		out = out.replace(mmm_zau_folder, '')

	return out, err
