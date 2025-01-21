import datetime, json, os, pathlib, re, stat
from pathlib import Path
from shutil import copyfile, copytree, copy as shutil_copy

from .utils import trycopy, trypaste, env_get, env_int, env_exist, env_expand


def chmod(filepath, stringmode='600'):
	"""
	https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu
	"""
	os.chmod(filepath, int(stringmode, base=8))


def chmodrwx(filepath):
	"""Removes 'group' and 'other' perms. Doesn't touch 'owner' perms.
	S_IRUSR  (00400)  read by owner
	S_IWUSR  (00200)  write by owner
	S_IXUSR  (00100)  execute/search by owner
	S_IRGRP  (00040)  read by group
	S_IWGRP  (00020)  write by group
	S_IXGRP  (00010)  execute/search by group
	S_IROTH  (00004)  read by others
	S_IWOTH  (00002)  write by others
	S_IXOTH  (00001)  execute/search by others

	Note: Although Windows supports chmod(), you can only set the file’s read-only flag with it (via the stat.S_IWRITE and stat.S_IREAD constants or a corresponding integer value). All other bits are ignored.

	"""
	mode = os.stat(filepath).st_mode
	mode -= (mode & (stat.S_IRWXG | stat.S_IRWXO))
	os.chmod(filepath, mode)


def get_umask():
	umask = os.umask(0)
	os.umask(umask)
	return umask


def chmod_plus_x(filepath):
	"""
	https://stackoverflow.com/questions/12791997/how-do-you-do-a-simple-chmod-x-from-within-python/55591471#55591471
	"""
	os.chmod(filepath, os.stat(filepath).st_mode |
		(
			(
				stat.S_IXUSR |
				stat.S_IXGRP |
				stat.S_IXOTH
			)
			& ~get_umask()
		)
	)


def to_absolute(filepath):
	return os.path.abspath(filepath)


def absolute(filepath):
	return os.path.isabs(filepath)


def is_absolute(filepath):
	return os.path.isabs(filepath)


def is_not_absolute(filepath):
	return not os.path.isabs(filepath)


def editfile(dir_or_file):
	os.system(f"code {dir_or_file}")


def copy_file(src, dst):
	copyfile(src, dst)


def copy_with_createdir(src, dest):
	"""
	https://stackoverflow.com/questions/2793789/create-destination-path-for-shutil-copy-files

	src = 'C:\\work\\fmusify\\flask-black-dashboard\\apps\\static\\assets\\gulpfile.js' 
	dst = 'static\\assets\\gulpfile.js'
	cw(src, dst) 
	"""

	import errno
	try:
		copyfile(src, dest)
	except IOError as e:		
		# ENOENT(2): file does not exist, raised also on missing dest parent dir
		if e.errno != errno.ENOENT:
			raise
		# try creating parent directories
		os.makedirs(os.path.dirname(dest))
		copyfile(src, dest)


def copy_file_list(file_list, source_folder_prefix, targetdir):
	"""
	file_list adlh list of abs filepath
	setiap abs filepath harus diprefix dg: source_folder_prefix
	"""
	
	# from .dirutils import dirname, basename, joiner

	for _file in file_list:
		# namafile = basename(_file)
		tujuan_pada_curdir_awal = _file.removeprefix(source_folder_prefix).removeprefix('\\').removeprefix('/')
		tujuan_pada_curdir = os.path.join(targetdir, tujuan_pada_curdir_awal)
		# print(f'[copy_file_list] copy {_file} ke {tujuan_pada_curdir}, targetdir = {targetdir}, awalnya: {tujuan_pada_curdir_awal}')
		copy_with_createdir(_file, tujuan_pada_curdir)


def copy_tree(src, dst):
	copytree(src, dst)


def copy_content(filepath):
	trycopy(file_content(filepath))


def json_file_content(json_filepath):
	try:
		with open(json_filepath) as fd:
			return json.load(fd)
	except Exception as err:
		print(f'[fileutils] opening: {json_filepath}', err)
		return None


def json_file_print(json_filepath):
	json_body = json_file_content(json_filepath)
	print(json.dumps(json_body, indent=4))
	return json_body


def json_from_string(content):
	return json.loads(content)


def json_stringify(content, indent=True):
	if indent:
		return json.dumps(content, indent=4)
	return json.dumps(content)


def file_sentences(filepath):
	data = None
	with open(filepath, 'r', encoding='utf-8') as fd:
		data = fd.read().replace('\n', '')

	return data


def file_content(filepath):
	"""
	retval berupa segelondongan text/string
	https://stackoverflow.com/questions/45529507/unicodedecodeerror-utf-8-codec-cant-decode-byte-0x96-in-position-35-invalid
	update utk:
	'utf-8' codec can't decode byte 0x93 in position 68384: invalid start byte
	errors='ignore'
	"""
	return pathlib.Path(filepath).read_text(encoding='utf8', errors='ignore')


def file_content_binary(filepath):
	import io
	content = None
	with io.open(filepath, 'rb') as binary_file:
		content = binary_file.read()
	return content


def file_content_ascii(filepath):
	return pathlib.Path(filepath).read_text(encoding="utf-8")


def file_content_safe(filepath):
	"""
	retval berupa segelondongan text/string
	kadang kasus https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
	invalid start byte.
	"""
	# return pathlib.Path(filepath).read_text(encoding='utf-8')
	path_obj = pathlib.Path(filepath)
	try:
		content = path_obj.read_text(encoding='utf-8')
	except Exception as err:
		# https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
		# bisa jadi dia utf16
		content = path_obj.read_bytes()
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print('file_content:', filepath, 'PRE decode bytes to utf8')
		content = content.decode("utf-16")
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print('file_content:', filepath, 'POST decode bytes to utf8')
	return content


def file_content_old(filepath):
	"""
	retval berupa segelondongan text/string
	"""
	content = None
	with open(filepath, encoding='utf-8') as fd:
		content = fd.read()

	return content


def file_copy(lama, baru):
	file_write(baru, file_content(lama))


def count_lines(filepath):
	return len(file_lines(filepath))


def file_length(filepath, mode='line'):
	"""
	bisa char/byte atau lines...
	default mode lines...
	"""
	if mode == 'line':
		return len(file_lines(filepath))
	else:
		return len(file_content(filepath))


def content_length(content, mode='line'):
	"""
	bisa char/byte atau lines...
	default mode lines...
	"""
	if mode == 'line':
		return len(content.splitlines())
	else:
		return len(content)


def file_lines(filepath, strip_newline=True, skip_emptylines=False):
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


def file_blocks(filepath, delimiter='#####', strip_newline=False):
	"""
	kembalikan list of block dlm file terpisah delimiter
	digunakan di app.transpiler.snippets utk cari di dalam snippets.txt
	"""
	content = file_content(filepath)
	content = content.split(delimiter)
	return [item.strip() if strip_newline else item for item in content if item.strip()]


def non_empty_lines(lines):
	return [item for item in lines if item.strip()]


def file_words(filepath):
	"""
	kembalikan list of words
	pd gabung, empty line jadi extra space
	dg split(), multiple space setara satu space, jadi hilang dlm hasil akhir
	"""
	content = file_lines(filepath)
	# hilangkan empty lines
	# bisa juga [item for item in content if item.strip()]
	gabung = ' '.join([item.strip() for item in content])
	return gabung.split()


def line_contains(filepath, kunci):
	return [item for item in file_lines(filepath) if kunci in item]


def create_if_empty_file(filepath):
	if not os.path.exists(filepath):
		pathlib.Path(filepath).touch()


def touch_file(filepath):
	pathlib.Path(filepath).touch()


def file_touch(filepath):
	touch_file(filepath)


def get_extension(filepath, no_dot=True):
	"""
	with_dot	-> .txt
	no_dot 		-> txt
	"""
	if no_dot:
		return pathlib.Path(filepath).suffix [1:]

	return pathlib.Path(filepath).suffix


def change_file_extension(filepath, source_extension, target_extension):
	"""
	Change the file extension of a given file.

	Parameters:
	- filepath (str): The path of the file.
	- source_extension (str): The current file extension.
	- target_extension (str): The desired file extension.

	Returns:
	- str: The path of the modified file.
	"""
	# Check if the file exists
	if not os.path.exists(filepath):
		raise FileNotFoundError(f"The file '{filepath}' does not exist.")

	# Check if the file has the correct source extension
	_, current_extension = os.path.splitext(filepath)
	if current_extension != source_extension:
		raise ValueError(f"The file '{filepath}' does not have the expected source extension '{source_extension}'.")

	# Create the new filepath with the target extension
	new_filepath = os.path.splitext(filepath)[0] + target_extension

	# Rename the file
	os.rename(filepath, new_filepath)

	return new_filepath


def test_change_file_extension():
	source_filepath = "/path/to/example.json"
	source_extension = ".json"
	target_extension = ".fmus"
	changed_filepath = change_file_extension(source_filepath, source_extension, target_extension)
	print(f"The file extension has been changed. New filepath: {changed_filepath}")


def change_file_extension_in_path(filepath, source_extension, target_extension):
	"""
	Change the file extension in the given file path.

	Parameters:
	- filepath (str): The path of the file.
	- source_extension (str): The current file extension.
	- target_extension (str): The desired file extension.

	Returns:
	- str: The modified file path.
	"""
	# Check if the file path has the correct source extension
	_, current_extension = os.path.splitext(filepath)
	if current_extension != source_extension:
		raise ValueError(f"The file path '{filepath}' does not have the expected source extension '{source_extension}'.")

	# Create the new file path with the target extension
	new_filepath = os.path.splitext(filepath)[0] + target_extension

	return new_filepath


def test_change_file_extension_in_path():
	source_filepath = "/path/to/myfile.json"
	source_extension = ".json"
	target_extension = ".fmus"

	changed_filepath = change_file_extension_in_path(source_filepath, source_extension, target_extension)
	print(f"The file path has been changed. New filepath: {changed_filepath}")


def get_filename_full(filepath):
	"""
	renaming path_filename
	/home/usef/untitled.txt -> untitled.txt
	"""
	return os.path.basename(filepath)


def get_filename_part(filepath):
	"""
	get_filename dg nama yg benar
	"""
	return pathlib.Path(filepath).stem


def get_filename(filepath):
	"""
	harusnya dinamai: get_filename_part
	path_filename			-> untitled.txt
	get_filename			-> untitled

	biasanya os.path.splitext(path)[0]
	lebih baik pake Path
	>>> Path('/a/b/c/d/untitled.txt').stem
	'untitled'

	untitled.txt -> untitled
	"""
	return pathlib.Path(filepath).stem


def get_lastpath_and_filename(filepath):
	"""
	ini beresiko jk parent gak dapat etc
	"""
	# return pathlib.Path(filepath).stem
	return pathlib.Path(filepath).parent.stem +'/'+ pathlib.Path(filepath).stem


def path_filename(filepath):
	"""
	/home/usef/untitled.txt -> untitled.txt
	"""
	return os.path.basename(filepath)


def path_dirname(filepath):
	"""
	/home/usef/untitled.txt -> /home/usef
	"""
	return os.path.dirname(filepath)


def get_dirname(filepath):
	return path_dirname(filepath)


def hapus_file(filepath):
	file_to_rem = pathlib.Path(filepath)
	try:
		file_to_rem.unlink(missing_ok=False)
	except Exception as err:
		print(f"[hapus_file] {err}")


def file_remove(filepath):
	"""
	os.remove() removes a file.
		If the file doesn't exist, os.remove() throws an exception, so it may be necessary to check os.path.isfile() first, or wrap in a try
		the exception thrown by os.remove() if a file doesn't exist is FileNotFoundError
		missing_ok=True, added in 3.8 solves that!
	os.rmdir() removes an empty directory.

	shutil.rmtree() deletes a directory and all its contents.

	Path objects from the Python 3.4+ pathlib module also expose these instance methods:

	pathlib.Path.unlink() removes a file or symbolic link.
		file_to_rem = pathlib.Path("/tmp/<file_name>.txt")
		file_to_rem.unlink()

		Path.unlink(missing_ok=False)
		Unlink method used to remove the file or the symbolik link.

		If missing_ok is false (the default), FileNotFoundError is raised if the path does not exist.
		If missing_ok is true, FileNotFoundError exceptions will be ignored (same behavior as the POSIX rm -f command).
		Changed in version 3.8: The missing_ok parameter was added.
	pathlib.Path.rmdir() removes an empty directory.
	"""
	if os.path.exists(filepath):
		os.remove(filepath)
	# else:
	# 	print(f'[app.fileutils.file_remove] {filepath} not found')


def dir_remove(dirpath):
	os.rmdir(dirpath)


def write_list(filepath, daftar, combiner='\n'):
	with open(filepath, mode='w', encoding='utf8') as fd:
		fd.write(combiner.join(daftar))


def write_file(filepath, text, write_mode='w'):
	with open(filepath, mode=write_mode, encoding='utf8') as fd:
		fd.write(text)


def file_write(filepath, text, write_mode='w'):
	write_file(filepath, text, write_mode=write_mode)


def file_name_timestamped(filepath, formatter='%Y%m%d_%H%M%S'):
	timestamp = datetime.datetime.now().strftime(formatter)
	filename, extension = os.path.splitext(filepath)
	newfilename = f"{filename}-{timestamp}{extension}"
	return newfilename


def file_write_timestamped(filepath, text, write_mode='w', formatter='%Y%m%d_%H%M%S'):
	timestamp = datetime.datetime.now().strftime(formatter)
	filename, extension = os.path.splitext(filepath)
	newfilename = f"{filename}-{timestamp}{extension}"
	if write_mode=='a' and not os.path.isfile(newfilename):
		touch_file(newfilename)
	write_file(newfilename, text, write_mode=write_mode)
	return newfilename


def file_write_timestamped_under_rootdir(filename, content, foldername='data/guilang-output', formatter='%Y%m%d_%H%M%S', write_mode='w'):
	from .dirutils import file_under_rootdir
	namafile = file_under_rootdir(foldername, filename)
	namafile = file_write_timestamped(namafile, text=content, write_mode=write_mode, formatter=formatter)
	return namafile


def file_write_lines(filepath, lines):
	with open(filepath, 'w', encoding='utf-8') as fd:
		fd.writelines(lines)


def append_file(filepath, text):
	with open(filepath, mode='a', encoding='utf8') as fd:
		fd.write(text)


def file_append(filepath, text):
	with open(filepath, mode='a', encoding='utf8') as fd:
		fd.write(text)


def file_append_lines(filepath, lines):
	with open(filepath, 'a', encoding='utf-8') as fd:
		fd.writelines(lines)


def file_append_ensure_newline(filepath, text):
	content = file_content(filepath)
	if content.strip() and not content.endswith('\n'):
		text = '\n' + text
	file_append(filepath, text)


def file_prepend(filepath, text):
	# Read the existing content of the file
	try:
		with open(filepath, mode='r', encoding='utf8') as fd:
			existing_content = fd.read()
	except FileNotFoundError:
		# If the file doesn't exist, create a new one with the provided text
		with open(filepath, mode='w', encoding='utf8') as fd:
			fd.write(text)
		return

	# Prepend the new text to the existing content
	new_content = text + existing_content

	# Write the updated content back to the file
	with open(filepath, mode='w', encoding='utf8') as fd:
		fd.write(new_content)


def test_file_prepend():
	file_prepend('example.txt', 'This text will be prepended.\n')


def prepend_datetime_to_file(filepath):
	tanggal = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S, %A')
	baris = f"[{tanggal}]"
	with open(filepath, 'r+', encoding='utf-8') as fd:
		content = fd.read()
		fd.seek(0)
		fd.write(baris + '\n' + content)


def prepend_comments_to_line(filepath, baris_cari, comment='#', num_lines=1, uncomment=False, space=' ', num_spaces=1):
	"""
	bisa comment atau uncomment
	uncomment hanya jk sudah tercomment
	# something
	// something
	capek deh, ternyata dah ada comment_file dan uncomment_file
	"""
	tanggal = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S, %A')
	baris = f"[{tanggal}]"
	with open(filepath, 'r+', encoding='utf-8') as fd:
		content = fd.read()
		fd.seek(0)
		fd.write(baris + '\n' + content)


def clipboard_to_file(filepath):
	content = trypaste()
	with open(filepath, 'w', encoding='utf-8') as fd:
		fd.write(content)


def del_lines(filepath, baris_regex):
	"""
	https://stackoverflow.com/questions/4710067/using-python-for-deleting-a-specific-line-in-a-file
	contoh baris_regex: "^p$" atau "^p\\s*$"
	tentu juga:
	"^#"
	"""
	with open(filepath, mode='r+', encoding='utf8') as fd:
		content = fd.readlines()
		fd.seek(0)
		for line in content:
			m = re.match(baris_regex, line)
			if not m:
				fd.write(line)
		fd.truncate() # hapus sisa baris2


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


# as str
def skip_lines(filepath, baris_regex, isFiltering=False):  
	hasil = skip_lines_aslines(filepath, baris_regex, isFiltering)
	return ''.join(hasil)


# as []
def lines_skip_lines_aslines(barisan, baris_regex, isFiltering=False, before=0, after=0):
	filtered = []
	for idx, line in enumerate(barisan):
		if isFiltering and baris_regex in line:
			if before:
				lines_before_lst = barisan[(idx-before if idx>=before else 0):idx]
				lines_before_str = '\n'.join(lines_before_lst)
				# print(f'fileutils before idx={idx}, line={line}, before={before}={lines_before_str}')
				line = lines_before_str + '\n' + line
			if after:
				maks = len(barisan)
				lines_after_lst = barisan[idx+1:(idx+after+1 if (idx+after<=maks) else maks)]
				lines_after_str = '\n'.join(lines_after_lst)
				# print(f'fileutils before idx={idx}, line={line}, after={after}={lines_after_str}')
				line = line + '\n' + lines_after_str
			filtered.append(line)
	
	return filtered


# as str
def lines_skip_lines_from_string(barisan_string, baris_regex, isFiltering=False, before=0, after=0):
	barisan = barisan_string.splitlines()
	hasil = lines_skip_lines_aslines(barisan, baris_regex, isFiltering, before=before, after=after)
	# if not return_str:
	# 	return hasil
	return '\n'.join(hasil)


# as []
def filter_lines_aslines(filepath, baris_regex):
	"""
	filter lines, kembalikan sbg [baris1, baris2, ...]
	"""
	hasil = skip_lines_aslines(filepath, baris_regex, True)
	return hasil


# as str
def filter_lines(filepath, baris_regex):
	"""
	filter lines, kembalikan sbg baris1+baris2+baris3+...
	asumsikan tiap baris sudah diakhiri dg \n
	"""
	hasil = skip_lines(filepath, baris_regex, isFiltering=True)
	# print(f'hasil filter adlh: [{hasil}]')
	return hasil


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


# as str
def filter_lines_transform(filepath, baris_regex, transformer=lambda baris:baris.replace('#', '', 1)):
	hasil = filter_lines_transform_aslines(filepath, baris_regex, transformer)
	return ''.join(hasil)


def get_definition_aslist(filepath, start_regex, end_regex):
	"""
	actor file:
		end_word = re.search(f'{KUNCI} (.*)', line)
		start_word = re.search(f'{KUNCI}\\s*({kata_dicari}.*)\\s*$', line)
	"""
	result = []
	collecting = False
	with open(filepath, encoding='utf-8') as fd:
		for line in fd.readlines():			
			if collecting:
				if re.search(end_regex, line):
					return result
				result.append( line )
			else:
				if re.search(start_regex, line):
					collecting = True

	return result


def get_definition_from_content(content, baris, delimiter='\n'):
	"""
	delimiter cukup "" krn tiap line sudah punya newline
	"""
	kunci_start='^--%'
	kunci_end='^--#'
	start_regex='--% '
	end_regex='--#'

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

	# definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)

	definisi = []
	collecting = False
	for line in content.splitlines():
		try:
			if collecting:
				if re.search(kunci_end, line):
					# return definisi
					break
				definisi.append( line )
			else:
				# if start_line in line:
				if re.search(start_regex_modified, line):
					collecting = True
		except Exception as err:
			print('[EXC] get_definition_from_content:', err)

	if len(definisi) == 0:
		# lets start all over again with diff start regex
		start_regex_modified = f'{kunci_start}\s+(.*){baris}'
		# definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)
		collecting = False
		for line in content.splitlines():
			try:
				if collecting:
					if re.search(kunci_end, line):
						# return definisi
						break
					definisi.append( line )
				else:
					# if start_line in line:
					if re.search(start_regex_modified, line):
						collecting = True
			except Exception as err:
				print('[EXC] get_definition_from_content:', err)

	return delimiter.join(definisi)


def get_daftar_from_content(content, stringified=False, kunci='--%'):
	"""
	get baris2 kunci yg diawali dg kunci
	kembalikan ter-transform tanpa kunci => berupa list entries
	"""
	# utk re.match
	FILTER_CONDITION = f'^{kunci}\s+'

	def transformer(baris):
		# hapus --%\s+ di awal entry
		return baris.replace(kunci, '', 1).strip()
	
	# content = filter_lines_transform_aslines(filepath, FILTER_CONDITION, transformer)
	# hasil = skip_lines_aslines(filepath, baris_regex, isFiltering=True)
	isFiltering=True
	hasil_skip_lines = []
	# with open(filepath, 'r', encoding='utf-8') as fd:
	temp_content = content.splitlines()
	for line in temp_content:
		m = re.match(FILTER_CONDITION, line)
		if (not m and not isFiltering) or (m and isFiltering):
			hasil_skip_lines.append(line)
	
	# return filtered
	# hasil_skip_lines = skip_lines_aslines(filepath, FILTER_CONDITION, isFiltering=True)
	content = list(map(transformer, hasil_skip_lines))
	if stringified:
		return '\n'.join(content)
	return content


def get_definition_exactline_aslist(filepath, start_regex, end_regex):
	"""
	actor file:
		end_word = re.search(f'{KUNCI} (.*)', line)
		start_word = baris yg dicari sbg substring
			// ini gak bener tapinya...krn bisa content orang jg masuk

	ada masalah jk file .mk berisi [ apapun - apapun ] spt wkt main xpath di selenium
	--% select div[class=card-body] yang kedua
	hrs diganti jadi:
	--% select div class=card-body yang kedua
	maka jadi re.error: bad character range
	"""
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
				ini biasanya disebabkan di start_regex ada backslash
				hrs perbaiki generator wmc/gen/reversefm utk replace semua backslash dg slash
					sudah diperbaiki dg: relative = relative.replace('\\', '/')
					di: def file_entry(self, subindent, filename, fullpath, basedir)
				atau lakukan secara manual
				"""
				print('// get_definition_exactline_aslist mengalami exception:', err)
				print(f"""
				filepath: {filepath}
				baris: {line}
				start_regex: {start_regex}
				end_regex: {end_regex}
				""")
	return result


def get_lineno_of_barisentry(filepath, barisentry):
	start_regex = f'^--%\s+(.*){barisentry}'
	end_regex='^--#'
	lineno = -1
	collecting = False
	with open(filepath, encoding='utf-8') as fd:
		for index, line in enumerate(fd.readlines()):
			if collecting:
				if re.search(end_regex, line):
					return lineno
			else:
				if re.search(start_regex, line):
					collecting = True
					lineno = index+2

	return lineno


def get_definition_exactline_aslist_with_lineno(filepath, start_regex, end_regex):
	"""
	actor file:
		end_word = re.search(f'{KUNCI} (.*)', line)
		start_word = baris yg dicari sbg substring
			// ini gak bener tapinya...krn bisa content orang jg masuk
	"""
	result = []
	collecting = False
	lineno = -1
	with open(filepath, encoding='utf-8') as fd:
		for index, line in enumerate(fd.readlines()):
			if collecting:
				if re.search(end_regex, line):
					return result, lineno
				result.append( line )
			else:
				if re.search(start_regex, line):
					collecting = True
					lineno = index+2

	return result, lineno


def get_definition(filepath, start_regex, end_regex='^--#'):
	"""
	utk file berisi entries spt:
	-- entry 1
	-- entry 2
	dst
	kita pengen ambil isi antara entry 1 dan entry 2
	perlu start regex dan end regex.
	
	coder file:
	start: ^.*{kata_dicari}.*$
	nope: start = exact string
	end: ^--

	contoh definitor:
	return get_definition(filepath, f'^{self.KUNCI}\s+{baris}\s+$', f'^{self.KUNCI}')
	return get_definition(filename, f'^{kunci}\s+{baris}\s+$', f'^{kunci}')

	kadang lebih baik:
	f'^{kunci}\s+{baris}\s+$'
	jadi bisa ada karakter2 lain stlh start_regex

	"""
	# print(f"get_definition_permissive_start/3, file [{filepath}], end_regex [{end_regex}].")
	definisi = get_definition_exactline_aslist(filepath, start_regex, end_regex)
	# print(f"{filepath} peroleh [start {start_regex}, end {end_regex}], definisi {definisi}")
	return ''.join(definisi)


def get_definition_permissive_start(filepath, start_regex, end_regex):
	start_regex_modified = f'^{start_regex}'
	# print(f"get_definition_permissive_start/2, file [{filepath}], end_regex [{end_regex}].")
	definisi = get_definition_exactline_aslist(filepath, start_regex_modified, end_regex)
	return ''.join(definisi)


def get_definition_by_key_permissive_start(filepath, baris, kunci_start='^--%', kunci_end='^--#', as_list=False):
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
	if env_int('ULIBPY_FMUS_DEBUG') > 2:
		print(f'[fileutils] get_definition_by_key_permissive_start {filepath}: [{start_regex_modified}...{kunci_end}]')
	definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)
	if len(definisi) == 0:
		start_regex_modified = f'{kunci_start}\s+(.*){baris}'
		if env_int('ULIBPY_FMUS_DEBUG') > 2:
			print('hasil get_definition_exactline_aslist #1 berpanjang:', \
				len(definisi), \
				f'coba lagi dg modify start regex menjadi {start_regex_modified}')
		definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)
	if env_int('ULIBPY_FMUS_DEBUG') > 2:
		print('[fileutils] hasil get_definition_exactline_aslist berpanjang:', len(definisi))
	# if as_list:
	# 	return definisi
	return ''.join(definisi)


# alias:start
def mkfile_entry(filepath, baris):
	return get_definition_by_key_permissive_start(filepath, baris)


def fmusfile_entry(filepath, baris):
	return get_definition_by_key_permissive_start(filepath, baris)
# alias:end


def get_definition_fmusfile_barisentry(filepath_barisentry):
	filepath, barisentry = [item.strip() for item in filepath_barisentry.split('=', 1)]
	return get_definition_by_key_permissive_start(filepath, barisentry)


def get_definition_filepath_barisentry(filepath_barisentry):
	return get_definition_fmusfile_barisentry(filepath_barisentry)


# new alias agar gampang ingat
def define_filepath_barisentry(filepath, barisentry):  # (filepath.fmus, barisentry)
	return get_definition_by_key_permissive_start(filepath, barisentry)


def define_filepath_equal(filepath):  # (filepath.fmus=barisentry)
	return get_definition_fmusfile_barisentry(filepath)


def define_filepath_barisentry_with_lineno(filepath, barisentry):  # (filepath.fmus, barisentry)
	return get_definition_by_key_permissive_start_with_lineno(filepath, barisentry)


def define_filepath_equal_with_lineno(filepath):  # (filepath.fmus=barisentry)
	filepath, barisentry = [item.strip() for item in filepath.split('=', 1)]
	return get_definition_by_key_permissive_start_with_lineno(filepath, barisentry)
#

def get_definition_by_key_permissive_start_with_lineno(filepath, baris):
	"""
	berikut ini versi restrictive:
	start_regex_modified = f'^{kunci}\s+{baris}\s+$'
	"""
	kunci_start = '^--%'
	kunci_end = '^--#'
	# debug=False

	# agar regex berjalan normal
	# masih kurang utk | () dst
	# ESCAPE
	# USE THIS: ini yg digunakan waktu baca dg /cari
	# instead of				: get_definition_by_key_permissive_start
	# escape regex di		: get_definition_by_key_permissive_start_with_lineno
	if '\\' in baris:
		# ini oprek backslash hrs diawal krn yg lain menambahkan backslash
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
	if '<' in baris:
		baris = baris.replace('<', '\<')
	if '>' in baris:
		baris = baris.replace('>', '\>')
	if '?' in baris:
		baris = baris.replace('?', '\?')
	if '$' in baris:
		baris = baris.replace('$', '\$')
	if '|' in baris:
		baris = baris.replace('|', '\|')
	# if ':' in baris:
	# 	baris = baris.replace(')', '\:')
	# if '"' in baris:
	# 	baris = baris.replace(')', '\"')
	"""
	TODO:
	tambah, cek jk baris mengandung |
	jk ya, maka kita split...
	definisi = []
	lineno
	for idx, item in baris.split(|)
		if idx==0
			temukan, nobaris = get_definition_exactline_aslist_with_lineno(item)
			definisi = temukan
			lineno = nobaris
		else
			definisi = [elem for elem in definisi if item in elem]
	"""	
	start_regex_modified = f'{kunci_start}\s+{baris}'
	if env_int('ULIBPY_FMUS_DEBUG') > 2:
		print(f'get_definition_by_key_permissive_start {filepath}: [{start_regex_modified}...{kunci_end}]')
	lineno = 0
	definisi, lineno = get_definition_exactline_aslist_with_lineno(filepath, start_regex_modified, kunci_end)

	if len(definisi) == 0:
		'''
		jk gak ketemu 
			--% sesuatu
		kita coba
			--% <apapun>sesuatu
		'''
		start_regex_modified = f'{kunci_start}\s+(.*){baris}'
		if env_int('ULIBPY_FMUS_DEBUG') > 2:
			print('hasil get_definition_exactline_aslist berpanjang:', \
				len(definisi), \
				f'coba lagi dg modify start regex menjadi {start_regex_modified}')
		definisi, lineno = get_definition_exactline_aslist_with_lineno(filepath, start_regex_modified, kunci_end)

	lineno += len(definisi)
	# 28/12/22
	from schnell.creator.context import context as global_context
	if global_context['fmus_expansion_mode']:
		definisi = replace_links_show_imgs(definisi)
	# definisi = show_if_contain_imgs(definisi)

	if env_int('ULIBPY_FMUS_DEBUG') > 2:
		print('hasil get_definition_exactline_aslist berpanjang:', len(definisi))
	# return ''.join(definisi).strip(), lineno
	return ''.join(definisi), lineno


def replace_links_show_imgs(definisi):
	show_if_contain_imgs(definisi)
	definisi = replace_if_contain_links(definisi)
	return definisi


def check_replace_if_contain_links(content, need_separator=False):
	"""
	kita tambah dg show images...
	"""
	from schnell.app.appconfig import programming_data
	gambar = programming_data['j']['schnell']['app']['configuration']['ULIBPY_IMGTAG'] # env_get('ULIBPY_IMGTAG')
	cari = programming_data['j']['schnell']['app']['configuration']['ULIBPY_LINKTAG'] # env_get('ULIBPY_LINKTAG')

	if gambar in content:
		print(f'GAMBAR in content #1')
		show_if_contain_imgs(content.splitlines())
	
	if cari in content:
		print(f'LINK in content #1')
		content = replace_if_contain_links(content.splitlines())
		return ('\n' if need_separator else '').join(content)
	else:
		return content


def show_if_contain_imgs(definisi):	
	# snipdir = env_get('ULIBPY_SNIPPETS')
	from schnell.app.mediautils import lihat_gambar
	from .dirutils import isfile
	from schnell.app.appconfig import programming_data
	cari = programming_data['j']['schnell']['app']['configuration']['ULIBPY_IMGTAG']
	# cari = env_get('ULIBPY_IMGTAG')

	found = [(idx,baris.strip()) for idx,baris in enumerate(definisi) if baris.startswith(cari)]
	# print(f'GAMBAR in content #2, found:', found)
	if found:
		for index,ketemu in found:
			'''
			$$img=namafilegambar.jpg
			'''
			href = ketemu.split('=', 1)
			if len(href) == 2:
				# filepath = href[1].replace('ULIBPY_SNIPPETS', snipdir)
				filepath = env_expand(href[1])
				if isfile(filepath):
					lihat_gambar(filepath)


def replace_if_contain_links(definisi):
	# cari = env_get('ULIBPY_LINKTAG')
	from schnell.app.appconfig import programming_data
	cari = programming_data['j']['schnell']['app']['configuration']['ULIBPY_LINKTAG']
	from .dirutils import isfile, normy

	found = [(idx,baris.strip()) for idx,baris in enumerate(definisi) if baris.startswith(cari)]
	if found:
		for index,ketemu in found:
			# print('replace_if_contain_links => found', ketemu)
			href = ketemu.split('=', 1)
			if len(href) == 2:
				if href[1].count('=')>0:
					# 28/12/22
					# $$link=filepath.txt=baris_entry
					# bisa rekursif...
					fileentry, barisentry = href[1].split('=')
					fileentry = env_expand(fileentry)
					# fileentry = normy(fileentry)
					# (content, lineno)
					content = get_definition_by_key_permissive_start_with_lineno(fileentry, barisentry) [0]
					if isfile(fileentry) and content:
						definisi = definisi[:index] + [content] + definisi[index+1:]
				else:
					# filepath = href[1].replace('ULIBPY_SNIPPETS', snipdir)
					filepath = env_expand(href[1])
					# filepath = normy(filepath)
					if isfile(filepath):
						# update: save last expanded linktag agar bisa buka
						from .appconfig import appconfig
						appconfig['last_expand_linktag'] = filepath
						# content = file_content(filepath).splitlines()
						content = file_lines(filepath)
						if content:
							definisi = definisi[:index] + content + definisi[index+1:]
					else:
						print(filepath, 'bukan file')

	return definisi


def get_definition_double_entry_aware(filepath, baris, kunci_start='^--%', kunci_end='^--#'):
	"""
	TODO:
	- buat link + replacer
	link=<path to replacer> bisa __CURDIR__ etc
	proses per line
	"""
	result = []
	collecting = False
	content = []
	if '+' in baris:
		baris = baris.replace('+', '\+')

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	start_regex_modified = f"{kunci_start}\s+{baris}"	
	matches = [baris for baris in content if re.match(start_regex_modified, baris)]

	if len(matches)>1:
		tersingkat = min(matches, key=len)
		for line in content:
			if collecting:
				if re.search(kunci_end, line):
					return ''.join(result)				
				result.append( line )			
			else:
				if line == tersingkat:
					collecting = True
		return ''.join(result)
	else:
		definisi = get_definition_exactline_aslist(filepath, start_regex_modified, kunci_end)
		return ''.join(definisi)


def get_daftar(filepath, stringified=False, kunci='--%'):
	"""
	get baris2 kunci yg diawali dg kunci
	kembalikan ter-transform tanpa kunci => berupa list entries
	"""
	# utk re.match
	FILTER_CONDITION = f'^{kunci}\s+'

	def transformer(baris):
		# hapus --%\s+ di awal entry
		return baris.replace(kunci, '', 1).strip()
	
	content = filter_lines_transform_aslines(filepath, FILTER_CONDITION, transformer)
	if stringified:
		return '\n'.join(content)
	return content


get_daftar_isi = get_daftar
get_toc = get_daftar


def mk_file_to_dict(filepath, reverse=True):
	"""
	utk auto completer agar

	int main() { ..	| main function
	"""
	dictionary_result = {}
	dictionary_result_reverse = {}

	entry_header = None
	entry_body = []
	collecting = False
	with open(filepath, encoding='utf-8') as fd:
		for line in fd.readlines():
			if collecting:
				if re.search(r'^--#', line):
					entry_content = ''.join(entry_body)
					entry_content = entry_content.strip()

					dictionary_result.update({
						entry_header: entry_content
					})
					dictionary_result_reverse.update({
						entry_content: entry_header
					})
					entry_body = []
					collecting = False
				else:
					entry_body.append( line )
			elif re.search(r'^\s*--%\s+', line):
				# entah kenapa entry kedua dst suka \n--% baris
				entry_header = line.replace('--%', '', 1).strip()
				collecting = True

	if reverse:
		return dictionary_result_reverse

	return dictionary_result


def mkfile_to_dict(filepath):
	daftars = get_daftar(filepath)
	result = {}
	for baris_entry in daftars:
		result[baris_entry] = get_definition_by_key_permissive_start(filepath, baris_entry)

	return result


def dict_to_mkfile(the_dict, filepath):
	file_write(filepath, '')  # kosongkan dulu, otherwise double+ content
	for k,v in the_dict.items():
		append_entry_tofile(filepath, k, v)


def replace_entry_in_mkfile(baris_entry, new_content, filepath):
	from .dirutils import isfile
	from schnell.app.appconfig import programming_data
	cari = programming_data['j']['schnell']['app']['configuration']['ULIBPY_LINKTAG']
	# cari = env_get('ULIBPY_LINKTAG')
	the_dict = mkfile_to_dict(filepath)
	if baris_entry in the_dict:
		# cek apakah old content itu link
		old_content = the_dict[baris_entry]
		if old_content.startswith(cari):
			tag, filepath = old_content.split('=', 1)
			# danger zone
			# OSError: [Errno 22] Invalid argument: 'C:\\Users\\usef\\work\\sidoarjo/data/work-frontend.txt\n'
			filepath = env_expand(filepath.strip())  # pastikan strip extra whitespace
			if isfile(filepath):
				# update filepath dg new content
				file_write(filepath, new_content)
		else:
			the_dict[baris_entry] = new_content
			dict_to_mkfile(the_dict, filepath)
	else:
		print(f'"{baris_entry}" not found in {filepath}')


def entrify_lines(filepath, header_body_delimiter='###', start='--%', end='--#'):
	"""
	dipake oleh `@ dari repl, membaca clipboard berisi lines
	ini utk 1 entry 1 baris
	"""
	from .dirutils import isfile
	def entrify(baris):
		header, body = baris.split(header_body_delimiter)
		return f'{start} {header}\n' + body + f'\n{end}'
	if isfile(filepath):
		lines = file_lines(filepath)
		if lines:
			return [entrify(baris) for baris in lines]


def entrify_blocks(filepath, block_delim='@@@', header_body_delimiter='###', start='--%', end='--#'):
	"""
	filepath berisi:
	header
	###
	body
	@@@
	header
	###
	body

	masing2	menjadi:
	--% header
	body
	--#
	"""
	from .dirutils import isfile
	def entrify(baris):
		header, body = baris.split(header_body_delimiter)
		return f'{start} {header.strip()}\n' + body + f'\n{end.strip()}'
	if isfile(filepath):
		content = file_content(filepath).split(block_delim)
		if content:
			return [entrify(baris) for baris in content]


def entrify_line(baris, judul=None, start='--%', end='--#'):
	if judul is None:
		judul = baris.replace('\n', '').strip() [:40]

	res = f'{start} {judul}\n' + baris.strip() + f'\n{end}\n\n'

	return res


def append_entry_tofile(filepath, header, body, start = '--%', end = '--#'):
	"""
	ini utk bikin entry
	--% header
	body
	--#
	ke dalam sebuah file mk filepath
	"""
	if not body.endswith('\n'):
		body += '\n'
	entry_model = f'\n{start} {header}\n' + body + f'{end}\n'
	append_file(filepath, entry_model)
	return entry_model


def append_entry_tostring(content, header, body, pemisah='\n\n', start = '--%', end = '--#'):
	"""
	ini utk bikin entry
	--% header
	body
	--#
	ke dalam sebuah file mk filepath
	"""
	if not body.endswith('\n'):
		body += '\n'
	entry_model = f'\n{start} {header}\n' + body + f'{end}\n'	
	return content + pemisah + entry_model


def write_entry_tofile(filepath, header, body, start = '--%', end = '--#'):
	"""
	ini utk bikin entry
	--% header
	body
	--#
	ke dalam sebuah file mk filepath
	"""

	entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
	file_write(filepath, entry_model)
	return entry_model


def kurangi(banyak, dikit):
	"""
	string arithmetic:
	kurangi(sebuah_nama_panjang, sebuah_nama)
	hasilkan: _panjang
	"""
	return banyak.replace(dikit, '', 1).strip()


def insert_at(filepath, nomor_baris, content_to_insert):
	"""
	insert at line, bisa 0 (top), -1 (bottom), dst.
	insert('/path/to/capcay.txt', 0, 'tulisan baru')
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	if isinstance(nomor_baris, str):
		nomor_baris = int(nomor_baris)
	content = None
	kembalian = (None,)
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		if nomor_baris == 0:
			content = content_to_insert + content
		elif nomor_baris == -1:
			content =  content + content_to_insert
		else:
			content =  content[0:nomor_baris] + content_to_insert + content[nomor_baris:]
		kembalian = (True, 'OK')
	else:
		# boleh insert ke file kosong jk insert di 0
		if nomor_baris == 0:
			content = content_to_insert
			kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{filepath} has no content')

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)

	return kembalian


def insert_before(filepath, baris_cari, content_to_insert):
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	content = None
	kembalian = (None,)
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if baris_cari in item]
		if saring:
			# kita paksa walau ada bbrp item yg match kita ambil yg pertama saja
			saring = saring[0]
			index_saring = content.index(saring)
			# content = content[:index_saring+1] + content_to_insert + content[index_saring+1:]
			content = content[:index_saring] + content_to_insert + content[index_saring:]
			kembalian = (True, 'OK')
			# if len(saring) > 1:
			# 	kembalian = (None, 'please choose pattern: ' + str(saring))
			# elif len(saring) == 1:
			# 	saring = saring[0]
			# 	index_saring = content.index(saring)
			# 	content = content[:index_saring] + content_to_insert + content[index_saring:]
			# 	kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{baris_cari} not found.')
	else:
		kembalian = (None, f'{filepath} has no content')

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def insert_after(filepath, baris_cari, content_to_insert):
	"""
	strategi insert
	1) paling sederhana
	semua jadikan lines
	baris 1
	baris 2
	cari
	baris 3 
	baris 4
	[:cari_index] + [cari_index:]
	ini adlh [1,2][cari,3,4]
	cocok utk insert_before
	kita pengen
	[1,2,cari][3,4]
	jadi
	[:cari_index+1] + (posisi insert) + [cari_index+1:]
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	content = None
	kembalian = (None,)
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if baris_cari in item]
		if saring:
			# kita paksa walau ada bbrp item yg match kita ambil yg pertama saja
			saring = saring[0]
			index_saring = content.index(saring)
			content = content[:index_saring+1] + content_to_insert + content[index_saring+1:]
			kembalian = (True, 'OK')
			# if len(saring) > 1:
			# 	kembalian = (None, 'please choose pattern: ' + str(saring))
			# elif len(saring) == 1:
			# 	saring = saring[0]
			# 	index_saring = content.index(saring)
			# 	content = content[:index_saring+1] + content_to_insert + content[index_saring+1:]
			# 	kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{baris_cari} not found.')
	else:
		kembalian = (None, f'{filepath} has no content')

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def insert_after_by_regex(filepath, initial_pattern_multibaris_cari, content_to_insert):
	"""
	contoh:
	InitializeComponent\(\);\s*\}\s*
	namespace cepat_csharp_wpf
	{
		public partial class MainWindow : Window
		{
			public MainWindow()
			{
				InitializeComponent();
			}
		}
	}
	u -e"/file)iax//__SL__SL ini cuma komentar saja|MainWindow.xaml.cs"
	prompt => InitializeComponent();\s*}\s*
	"""
	initial_pattern_multibaris_cari = (initial_pattern_multibaris_cari
					.replace('(', '\(')
					.replace(')', '\)')
					.replace('}', '\}')
					.replace('{', '\{')
					)
	with open(filepath, 'r', encoding='utf-8') as file:
		filepath_content = file.read()

	final_pattern_multibaris_cari = rf'(\s*{initial_pattern_multibaris_cari}\s*)' # kita wrap all yg jadi bahan cari dg ()

	new_content = re.sub(final_pattern_multibaris_cari, rf'\1{content_to_insert}\n', filepath_content)

	print(f"""[fileutils:insert_after_by_regex]
		final_pattern_multibaris_cari: [{final_pattern_multibaris_cari}]
		content_to_insert: [{content_to_insert}]
		new_content: [{new_content}]
		""")

	with open(filepath, 'w', encoding='utf-8') as file:
		file.write(new_content)


def replace_by_regex(filepath, initial_pattern_multibaris_cari, content_to_insert):
	"""
	contoh:
	InitializeComponent\(\);\s*\}\s*
	namespace cepat_csharp_wpf
	{
		public partial class MainWindow : Window
		{
			public MainWindow()
			{
				InitializeComponent();
			}
		}
	}
	u -e"/file)riax//__SL__SL ini cuma komentar saja|MainWindow.xaml.cs"
	prompt => InitializeComponent();\s*}\s*
	"""
	initial_pattern_multibaris_cari = (initial_pattern_multibaris_cari
					.replace('(', '\(')
					.replace(')', '\)')
					.replace('}', '\}')
					.replace('{', '\{')
					)
	with open(filepath, 'r', encoding='utf-8') as file:
		filepath_content = file.read()
	final_pattern_multibaris_cari = rf'(\s*{initial_pattern_multibaris_cari}\s*)' # kita wrap all yg jadi bahan cari dg ()

	new_content = re.sub(final_pattern_multibaris_cari, rf'{content_to_insert}\n', filepath_content)

	print(f"""[fileutils:insert_after_by_regex]
		final_pattern_multibaris_cari: [{final_pattern_multibaris_cari}]
		content_to_insert: [{content_to_insert}]
		new_content: [{new_content}]
		""")

	with open(filepath, 'w', encoding='utf-8') as file:
		file.write(new_content)


def replace_string_in_file(filepath, old_string, new_string, replace_count=1):
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'"{filepath}" not found'
	content = None
	kembalian = (None, 'NOK')
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.read()

	if content:
		if replace_count == -1:
			content = content.replace(old_string, new_string)
		else:
			content = content.replace(old_string, new_string, replace_count)
		kembalian = (True, 'OK')
	
	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.write(content)
	
	# print(f'[fileutils/replace_string_in_file] [{filepath}] => from "{old_string}" to "{new_string}" => kembalian adlh:', kembalian, '\n')
	return kembalian


def replace_at(filepath, baris_cari, content_to_insert, how_many_lines_to_replace=1, pick_first_item=False):
	"""
	di sini kita hanya replace satu baris
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	content = None
	kembalian = (None,)
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if baris_cari in item]
		if saring:
			if len(saring) > 1:
				if pick_first_item:
					saring = saring[0]
					index_saring = content.index(saring)
					content = content[:index_saring] + content_to_insert + content[index_saring+how_many_lines_to_replace:]
					kembalian = (True, 'OK')
				else:
					kembalian = (None, 'please choose pattern: ' + str(saring))
			elif len(saring) == 1:
				saring = saring[0]
				index_saring = content.index(saring)
				content = content[:index_saring] + content_to_insert + content[index_saring+how_many_lines_to_replace:]
				kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{baris_cari} not found.')
	else:
		kembalian = (None, f'{filepath} has no content')

	# print('kembalian replace_at adlh:', kembalian)

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def replace_from(filepath, baris_cari, content_to_insert):
	"""
	kita replace dari ketemu baris sampai akhir file
	| "rf" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_from
	singkat utk peroleh content_to_insert
	MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE utk peroleh baris_cari
		yg adlh marker dlm target utk direplaced oleh singkat/content
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	content = None
	kembalian = (None,)
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if baris_cari in item]
		if saring:
			if len(saring) > 1:
				kembalian = (None, 'please choose pattern: ' + str(saring))
			elif len(saring) == 1:
				saring = saring[0]
				index_saring = content.index(saring)
				content = content[:index_saring] + content_to_insert
				kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{baris_cari} not found.')
	else:
		kembalian = (None, f'{filepath} has no content')

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def replace_until(filepath, baris_cari, content_to_insert):
	"""
	kita replace dari ketemu baris sampai akhir file
	| "rf" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_from
	singkat utk peroleh content_to_insert
	MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE utk peroleh baris_cari
		yg adlh marker dlm target utk direplaced oleh singkat/content
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	content = None
	kembalian = (None,)
	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if baris_cari in item]
		if saring:
			if len(saring) > 1:
				kembalian = (None, 'please choose pattern: ' + str(saring))
			elif len(saring) == 1:
				saring = saring[0]
				index_saring = content.index(saring)
				# line yg dispecify tidak masuk ke output, tentunya
				content = content_to_insert + content[index_saring+1:]
				kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{baris_cari} not found.')
	else:
		kembalian = (None, f'{filepath} has no content')

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def replace_entry(filepath, baris_cari, content_to_insert, start_regex='^--%', end_regex='^--#'):
	"""
	yg belum teratasi:
	jk match entry ada 2
	sementara kita ambil item yg pertama terscan dalam file
	TODO:
	bisa bikin versi search dari atas atau dari bawah
		- kadang kita tau yg pengen kita replace ada dari bawah atau dari atas
	bisa bikin versi match dari match terpanjang atau dari tersingkat

	| "re" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_entry
	setara dg replace_from utk replace_entry
	bedanya replace_from sampai akhir file
	replace_entry sampai akhir entry
	"""
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	sebelum = []
	sesudah = []
	word_mulai = ''
	word_akhir = ''
	index_mulai = -1
	index_akhir = -1
	collecting = False
	content = []
	start_regex_modified = f'{start_regex}\s+{baris_cari}'

	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()	

	# print('original:', content)
	for index, line in enumerate(content):
		if collecting:
			if re.search(end_regex, line):
				index_akhir = index
				word_akhir = line
				break # supaya gak terus2 sampai ke bawah...
		else:
			if re.search(start_regex_modified, line):
				collecting = True
				index_mulai = index
				word_mulai = line

	awal = content[:index_mulai]
	akhir = content[index_akhir+1:]
	tengah = [word_mulai] + content_to_insert + [word_akhir]
	# print('\n\n\n', '='*40, filepath)
	# print('awal:', awal)
	# print('tengah:', tengah)
	# print('index_mulai:', index_mulai)
	# print('index_akhir:', index_akhir)
	# print('akhir:', akhir)
	# print('='*40, '\n\n\n')
	content = awal + tengah + akhir
	if content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)


def replace_string_in_entry(filepath, baris_entry, string_lama, string_baru):
	entry_lama = get_definition_by_key_permissive_start(filepath, baris_entry)
	entry_baru = entry_lama.replace(string_lama, string_baru)
	replace_entry(filepath, baris_entry, entry_baru)


def replace_between(filepath, baris_cari_start, baris_cari_end, content_to_insert):
	"""
	kita replace dari ketemu baris cari start sampai baris cari end
	hrs ada:
	- singkat utk peroleh content sbg replacer
	- 2 marker di target
	| "rb" "=" jumlah_hapus "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_between
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		print(f'[fileutils:replace_between] {filepath} not found')
		return None, f'{filepath} not found'
	if isinstance(content_to_insert, str):
		content_to_insert = [content_to_insert]
	content = None
	kembalian = (None,)

	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()

	original_content = content
	if content:
		mulai = [item for item in content if baris_cari_start in item]
		akhir = [item for item in content if baris_cari_end in item]
		if len(mulai) >= 1 and len(akhir) >= 1: # ambil yg pertama match
			mulai = mulai[0]
			akhir = akhir[0]
			index_mulai = content.index(mulai)
			index_akhir = content.index(akhir)
			content = content[:index_mulai] + content_to_insert + content[index_akhir+1:]
			kembalian = (True, 'OK')

		else:
			kembalian = (None, f'{baris_cari_start} => {mulai}, {baris_cari_end} => {akhir}.')
	else:
		kembalian = (None, f'{filepath} has no content')

	# print('original:', content)
	# print('\n\n\n', '='*40, filepath)	
	# print('mulai:', mulai)
	# print('akhir:', akhir)
	# print('index_mulai:', index_mulai)
	# print('index_akhir:', index_akhir)
	# print('content now:', content)
	# print('='*40, '\n\n\n')
	print(f"""[fileutils:replace_between]
		original 	[{original_content}]
		new 			[{content}]
		content_to_insert	[{content_to_insert}]
		baris_cari_start [{baris_cari_start}]
		baris_cari_end	[{baris_cari_end}]
		filepath		[{filepath}]
		mulai		[{mulai}]
		akhir		[{akhir}]
		""")

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def remove_lines(filepath, baris_cari, how_many_lines_to_replace=1):
	from .dirutils import isfile
	if not isfile(filepath):
		return None, f'{filepath} not found'
	content = None
	kembalian = (None,)

	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()

	# print('REMOVE LINES original:', content)
	# print('\n\n\n', '='*40, filepath)

	if content:
		saring = [item for item in content if baris_cari in item]
		if saring:
			# if len(saring) > 1:
			# 	kembalian = (None, 'please choose pattern: ' + str(saring))
			if len(saring) >= 1:
				saring = saring[0] # hanya satu baris
				index_saring = content.index(saring)
				content = content[:index_saring] + content[(index_saring+how_many_lines_to_replace):]
				kembalian = (True, 'OK')
		else:
			kembalian = (None, f'{baris_cari} not found.')
	else:
		kembalian = (None, f'{filepath} has no content')
	
	# print('content now:', content)
	# print('='*40, '(REMOVED)\n\n\n')

	if kembalian[0] and content:
		with open(filepath, 'w+', encoding='utf-8') as fd:
			fd.writelines(content)
	return kembalian


def remove_lines_by_prefix(filepath, prefix_pattern, how_many_lines=1, re_prefixer='^'):
	"""
	dipake utk
	/file>-/table_name/1|target.txt
	"""
	prefix_pattern = re_prefixer + prefix_pattern
	result = []	
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	if how_many_lines==1:
		result = [baris for baris in content if not re.search(prefix_pattern, baris)]
	elif how_many_lines>1:
		content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
		hapus = []
		for idx,brs in content_with_indexes:
			if re.search(prefix_pattern, brs):
				for i in range(how_many_lines):
					hapus.append(idx+i)
		result = [b for (i,b) in content_with_indexes if i not in hapus]

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
		print(f'remove_lines_by_prefix {filepath} OK')


def replace_file_content(filepath, content):
	file_write(filepath, content)
	return (True, 'OK')


def remove_lines_by_no(filepath, barisno, how_many_lines=1):
	result = []
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	left = content[:barisno]
	right = content[barisno+how_many_lines:]
	result = left + right

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'remove_lines_by_no {filepath} OK')


def replace_line_by_no(filepath, barisno, content_to_replace):
	result = []
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	left = content[:barisno]
	middle = [content_to_replace]
	right = content[barisno+1:]
	result = left + middle + right

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'replace_line_by_no {filepath} OK')


def join_lines(filepath, barisno, how_many_lines=1):
	"""
	perlu bisa rstrip line barisno dan lstrip line berikutnya
	dipake utk:
	u -e"/file>j/2/5,__PWD/contoh.txt"
	"""
	result = []
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	left = content[:barisno]
	# middle = content[barisno:barisno+1+how_many_lines]
	middle = [content[barisno].rstrip()]
	for i in range(how_many_lines):
		indexer = barisno+i+1
		if indexer > len(content)-1:
			break
		k = content[indexer]
		if i<how_many_lines-1:
			k = k.rstrip()
		middle.append(k)
	
	# right = content[barisno+1+how_many_lines:]
	end = barisno+1+how_many_lines
	if end > len(content)-1:
		# end = len(content)-1
		right = []
	else:
		right = content[end:]

	result = left + middle + right

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'join_lines {filepath} OK')


def join_lines_by_prefix(filepath, prefix_pattern, how_many_lines=1, re_prefixer='^', join_if_not_empty_lines=False):
	"""
	perlu bisa rstrip line barisno dan lstrip line berikutnya
	dipake utk:
	u -e"/file>j/2/5,__PWD/contoh.txt"
	"""
	prefix_pattern = re_prefixer + prefix_pattern

	result = []
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	# how_many_lines=3
	# pattern ketemu di baris no 1,7,30
	# [ [1,2,3], [7,8,9], [30,31,32] ]
	# kita gabungkan 1,2,3 (1 dan 2 rstrip newline) lalu 7,8,9, (7 dan 8 rstrip newline)...
	list_of_list = [
		[idx+i for i in list(range(how_many_lines+1))]
		for (idx,baris) in content_with_indexes
		if re.search(prefix_pattern, baris)
	]
	print('[join_lines_by_prefix] lol:', list_of_list)
	if list_of_list and list_of_list[0]:
		first_found = list_of_list[0][0]
		last_found = list_of_list[-1][-1]
		result = content[:first_found] # left
		for j,item in enumerate(list_of_list):
			if j>0:
				# jk sudah minimal 1 iterasi
				prev_last_index = list_of_list[j-1][-1]
				cur_index = list_of_list[j][0]
				result += content[prev_last_index+1:cur_index]
			temp = '' # joined jd string
			for i,indiv in enumerate(item):
				k = content[indiv]
				if i<len(item)-1:
					k = k.rstrip('\n')
				temp += k
			result += [temp]
		result += content[last_found+1:] # right

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'join_lines_by_prefix {filepath} OK')


def line_number_expression(content_length, line_expression, line_startat_one=False, inclusive_end=False):
	"""
	@parameters
	memproses expression spt berikut:
		1
		~
		1-5,17,~
		17-~
	~ setara last item atau [-1]
	28/12/22, kita perkenalkan:
	~2 utk [-2], ~n utk [-n]

	content_length dibutuhkan utk tau nilai dari -1

	@returns: 
	list of line numbers indexed from 0

	kita tambah 
	line_startat_one, default baris dimulai dari 0, jadi 1-3 akan hasilkan 0,1,2
	inclusive_end, default end tidak include, jadi 1-3 akan max sampai 2.
	ok something is not right here...

	@usage:
	content = file read lines
	line_nos = line_number_expression(len(content), line_expression)
		kita butuh len(content) krn butuh representasi ~ sbg last line
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(process(baris) if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		write lines to file(result)
	"""
	pengurang = 1 if not line_startat_one else 0  # if index starts from 0, subtract 1
	range_end = 0 if not inclusive_end else 1
	result = []
	# content_length = len(line_of_contents)
	for expr in [item.strip() for item in line_expression.split(',')]:
		if '-' in expr:
			start, end = [item.strip() for item in expr.split('-')]
			start = int(start) - pengurang
			if end == '~':
				end = content_length # krn utk range
			elif end.startswith('~'):
				end = content_length - int(end.removeprefix('~'))
			else:
				end = int(end)
			for k in range(start, end+range_end):
				result.append(k)
		else:
			if expr == '~':
				k = content_length - pengurang # krn utk indexing
			elif expr.startswith('~'):
				# ~1 = ~ = [-1]
				# ~2 = [-2]
				# int(expr.removeprefix('~')) berperan sbg pengurang
				k = content_length - int(expr.removeprefix('~'))
			else:
				k = int(expr) - pengurang
			result.append(k)
	return result


def comment_file_by_linenumber(filepath, linenumber_list, comment='# '):
	"""
	u -e"/file>c/2,3/'-- '|__PWD/contoh.txt"
	u -e"/file>c/1,4-6/'-- '|__PWD/contoh.txt"

	u -e"/file>c/1-~/'(?P<'|__PWD/field.txt"

	utk repr last line = ~, misal 1-~
	"""
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	lines = []
	for lnxpr in linenumber_list.split(','):
		if '-' in lnxpr:
			start,end=lnxpr.split('-')
			start = int(start)-1
			if end == '~':
				end = len(content) # krn utk range
			else:
				end = int(end)
			for k in range(start,end):
				lines.append(k)
		else:
			if lnxpr == '~':
				k = len(content) - 1 # krn utk indexing
			else:
				k = int(lnxpr)-1
			lines.append(k)

	if not lines:
		return

	result = []
	
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [(comment+baris if index in lines else baris) for (index,baris) in content_with_indexes]

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'comment_file_by_linenumber {filepath} OK')


def append_file_by_linenumber(filepath, linenumber_list, appender='#'):
	"""
	u -e"/file>a/2,3/'-- '|__PWD/contoh.txt"
	u -e"/file>a/1,4-6/'-- '|__PWD/contoh.txt"
	u -e"/file>a/1-~/'>)'|__PWD/field.txt"

	utk repr last line = ~, misal 1-~
	"""
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	lines = []
	for lnxpr in linenumber_list.split(','):
		if '-' in lnxpr:
			start,end=lnxpr.split('-')
			start = int(start)-1
			if end == '~':
				end = len(content) # krn utk range
			else:
				end = int(end)
			for k in range(start,end):
				lines.append(k)
		else:
			if lnxpr == '~':
				k = len(content) - 1 # krn utk indexing
			else:
				k = int(lnxpr)-1
			lines.append(k)

	if not lines:
		return

	result = []
	
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [(baris.replace('\n', appender+'\n') if index in lines else baris) for (index,baris) in content_with_indexes]

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'line append by line-expr (append_file_by_linenumber) {filepath} OK')


def append_file_by_content(filepath, content_filter, appender='#'):
	"""
	/file)aa/find me/#|targetfile
	"""
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	result = []	
	result = [(baris.replace('\n', appender+'\n') if content_filter in baris else baris) for baris in content]

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'line append by content-filter (append_file_by_linenumber) {filepath} OK')


def append_file_by_content_regex(filepath, content_filter_regex, appender='#'):
	"""
	/file)aarx/regex find me/#|targetfile
	"""
	# content = []
	# with open(filepath, encoding='utf-8') as fd:
	# 	content = fd.readlines()

	# result = []
	
	# # re.match
	# result = [(baris.replace('\n', appender+'\n') if content_filter_regex in baris else baris) for baris in content]

	# if result:
	# 	with open(filepath, 'w', encoding='utf-8') as fd:
	# 		fd.writelines(result)
	# 		print(f'line append by content-filter (append_file_by_linenumber) {filepath} OK')


def prepend_line_by_content(filepath, content_filter, appender='#'):
	"""
	/file)bb/find me/#|targetfile
	"""
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	result = []	
	# result = [(baris.replace('\n', appender+'\n') if content_filter in baris else baris) for baris in content]
	result = [(appender+baris if content_filter in baris else baris) for baris in content]

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			print(f'line append by content-filter (append_file_by_linenumber) {filepath} OK')


def comment_file_by_prefix(filepath, prefix_pattern, comment='# ', re_prefixer='^'):
	"""
	"""
	prefix_pattern = re_prefixer + prefix_pattern
	result = []	
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	# matches = [item for item in content_with_indexes if re.search(prefix_pattern, item[1])]
	result = [(comment+baris if re.search(prefix_pattern, baris) else baris) \
		for (index,baris) in content_with_indexes]

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
		print(f'comment_file_by_prefix {filepath} OK')
		# print(f'comment_file_by_prefix {filepath} OK [{prefix_pattern} => {result}]')


def comment_file(filepath, baris_cari, comment='#', space='', how_many_lines=1, skip_starting_whitespace=False):
	"""
	- harus bisa tambah space
	- harus bs bbrp lines dari mulai baris ketemu
	"""
	# from schnell.app.printutils import indah4
	# collecting = False
	result = []	
	content = []

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	# matches = [(index, baris) for (index, baris) in enumerate(content) if re.match(baris_cari, baris)]
	# ternyata jangan pake re.match
	matches = [item for item in content_with_indexes if re.search(baris_cari, item[1])]
	
	# sementara ini belum digunakan
	matches_lines = [item[1] for item in matches]

	if len(matches)>1:
		'''
		berbasis: panjang string matches terpendek
		bisa juga yg pertama dijumpai
		'''
		# indah4(f'comment file: ketemu matches sebanyak {len(matches)}', warna='white')
		tersingkat = min(matches, key=len)
		tersingkat_index, tersingkat_baris = tersingkat
		if how_many_lines == 1:
			if env_int('ULIBPY_FMUS_DEBUG') > 1:
				print(f'multi matches [{matches}] disaring menjadi [{tersingkat_baris}].')
			result = content[:tersingkat_index] + [comment+space+tersingkat_baris] + content[tersingkat_index+1:]
		else:
			'''
			'''
			to_modify = content[tersingkat_index:tersingkat_index+how_many_lines]
			if env_int('ULIBPY_FMUS_DEBUG') > 1:
				print(f'temukan match [{to_modify}].')
			modified_lines = [comment+space+item for item in to_modify]
			result = content[:tersingkat_index] + modified_lines + content[tersingkat_index+how_many_lines+1:]
	elif len(matches)==1:
		'''
		'''
		# indah4(f'comment file: ketemu matches sebanyak 1', warna='white')
		tersingkat = matches[0] # (nomor_baris, isi_baris)
		tersingkat_index, tersingkat_baris = tersingkat

		if how_many_lines == 1:
			if env_int('ULIBPY_FMUS_DEBUG') > 1:
				print(f'temukan match [{tersingkat_baris}].')
			commented_out_line = [comment+space+tersingkat_baris]
			if skip_starting_whitespace:
				commented_out_line = [comment+space+tersingkat_baris]
				b = re.match(r'(\s+)(.*)', tersingkat_baris)
				if b:
					spaceprefix = b.group(1)
					nonspacecontent = b.group(2)
					if tersingkat_baris[-1] == '\n' and nonspacecontent[-1] != '\n':
						nonspacecontent += '\n'
					commented_out_line = [spaceprefix+comment+space+nonspacecontent]			
			result = content[:tersingkat_index] + commented_out_line + content[tersingkat_index+1:]
		else:
			'''
			'''
			to_modify = content[tersingkat_index:tersingkat_index+how_many_lines]
			if env_int('ULIBPY_FMUS_DEBUG') > 1:
				print(f'temukan match [{to_modify}].')
			modified_lines = [comment+space+item for item in to_modify]
			result = content[:tersingkat_index] + modified_lines + content[tersingkat_index+how_many_lines+1:]
	else:
		# indah4(f'comment file: no matches', warna='white')
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print(f'no matches untuk [{baris_cari}] di [{filepath}].')

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print(f'comment_file {filepath} OK')


def uncomment_file(filepath, baris_cari, comment='#', how_many_lines=1, by_tersingkat=False, by_pertama=True):
	"""
	kita pisah baris_cari dan comment
	jadi pemanggilan fungsi ini jangan sampai "comment" dimasukkan ke baris_cari
	ingat bentuk: f"{comment}\s*{baris_cari}"
	"""
	result = []	
	content = []
	# collecting = False

	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()

	terkomen = f"{comment}\s*{baris_cari}"
	matches = [(index, baris) for (index, baris) in enumerate(content) if re.match(terkomen, baris)]
	matches_lines = [item[1] for item in matches]
	if len(matches)>1:
		from rich.pretty import pprint
		pprint(matches)
		if by_pertama:
			tersingkat = matches[0]
		elif by_tersingkat:
			tersingkat = min(matches, key=len)
		else:
			tersingkat = matches[0]
		tersingkat_index, tersingkat_baris = tersingkat # (index, baris)
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print(f'multi matches [{matches}] disaring menjadi [{tersingkat_baris}].')
		if how_many_lines == 1:
			result = content[:tersingkat_index] + [tersingkat_baris.lstrip(comment)] + content[tersingkat_index+1:]
		else:
			to_modify = content[tersingkat_index:tersingkat_index+how_many_lines]
			modified_lines = [item.lstrip(comment) for item in to_modify]
			result = content[:tersingkat_index] + modified_lines + content[tersingkat_index+how_many_lines+1:]

	elif len(matches)==1:
		tersingkat = matches[0]
		tersingkat_index, tersingkat_baris = tersingkat
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print(f'temukan match [{to_modify}].')
		if how_many_lines == 1:
			result = content[:tersingkat_index] + [tersingkat_baris.lstrip(comment)] + content[tersingkat_index+1:]
		else:
			to_modify = content[tersingkat_index:tersingkat_index+how_many_lines]
			modified_lines = [item.lstrip(comment) for item in to_modify]
			result = content[:tersingkat_index] + modified_lines + content[tersingkat_index+how_many_lines+1:]

	else:
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print(f'no matches untuk [{baris_cari}] di [{filepath}].')

	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			print(f'uncomment_file {filepath} OK')


def against_regex(regexfile, filepath):
	"""
	u -e"/file>rx/rx.txt|users.txt"
	isi rx.txt:
	(?P<id>\d+)\t(?P<firstname>\w+)\t(?P<lastname>\w+|\-|\s)\t(?P<phone>\d+)\t(?P<email>[\.\w+]+@[\w]+\.[\w]+)\t(?P<pwd>[\w\$\/\.]+)\t(?P<enabled>1|0)\t(?P<activated>1|0)\t(?P<token>\w+|\\N)\t(?P<confirm_code>\d+)\t(?P<note>\\N)\t(?P<cr_date>[\d\-]+\s[\d:]+\.[\d\+]+)\t(?P<activated_date>[\d\-]+\s[\d:]+\.[\d\+]+|\\N)\t(?P<old_email>\\N)\t(?P<old_email_verify_code>\\N)\t(?P<old_phone>\\N)\t(?P<old_phone_verify_code>\\N)\t(?P<new_email>\\N)\t(?P<new_email_verify_code>\\N)\t(?P<new_phone>\\N)\t(?P<new_phone_verify_code>\\N)\t(?P<kyc_flag>1|0)\t(?P<setuju_snk>1|0)\t(?P<tgl_setuju_snk>[\d\-]+\s[\d:]+\.[\d\+]+|\\N)\t(?P<progres_registrasi>\d+)\t(?P<progres_kyc>\d+)\t(?P<lastlogin>[\d\-]+\s[\d:]+\.[\d\+]+|\\N)\t(?P<customerno>\\N)\t(?P<flag_login>1|0)\t(?P<fcm_token>[\w\d\-_:]+|\\N)\t(?P<role>\w+|\\N)\t(?P<referral_code>\w+|\\N)\t(?P<referrer_id>\\N)\t(?P<profile_image>[\w\d:\/\.]+|\\N)\t(?P<change_data_info>\\N)
	"""
	from .dirutils import isfile
	# from .printutils import indah4
	if not isfile(regexfile) and isfile(filepath):
		print(f'no regexfile {regexfile} and no targetfile {filepath}')
		return
	regexpattern = file_content(regexfile).strip()
	content = file_lines(filepath)
	# indah4(f'''[against_regex]
	# pattern = [{regexpattern}]
	# ''', warna='white')
	result = []
	# content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	# result = [(baris.replace('\n', appender+'\n') if index in lines else baris) for (index,baris) in content_with_indexes]
	match_counter = 0
	for (index,baris) in enumerate(content):
		# coba = re.match(regexpattern, baris)
		coba = re.search(regexpattern, baris)
		if coba:
			match_counter += 1
			result.append((index,baris))
	return result


def view_lines_between(filepath, baris_cari_start, baris_cari_end=None):
	"""
	print lines antara /baris_cari_start/ dan /baris_cari_end/
	"""
	from .dirutils import isfile
	if not isfile(filepath):
		print(f'{filepath} not found')
		return None

	content = None

	with open(filepath, 'r', encoding='utf-8') as fd:
		content = fd.readlines()

	# print('content:', content if len(content)<10 else f'{len(content)} lines')
	# print('\n\n\n', '='*40, filepath)

	if content:
		mulai = [item for item in content if baris_cari_start in item]
		mulai = mulai[-1] # mulai paling late
		index_mulai = content.index(mulai)
		if baris_cari_end:
			akhir = [item for item in content if baris_cari_end in item]
			if len(mulai) >= 1 and len(akhir) >= 1: # ambil yg pertama match
				# mulai = mulai[0]
				# print('found akhir:', akhir)
				# get akhir yg > mulai
				filtered_bigger = [item for item in akhir if content.index(item)>=index_mulai]
				if filtered_bigger:
					akhir = filtered_bigger[0] # akhir paling early
					index_akhir = content.index(akhir)
					# print(f'index mulai {index_mulai} dan index akhir {index_akhir}')
					content = content[index_mulai:index_akhir+1]
					return content
		else:
			return content[index_mulai:]

	return None


def tab_to_space_all(filepath, tabstop=2):
	content = file_content(filepath)
	write_file(filepath, content.replace('t', tabstop*' '))


def tab_to_space_start(filepath, tabstop=2):
	from schnell.app.appconfig import programming_data
	if (tabstop <= 0 or not tabstop):
		tabstop = programming_data['j']['schnell']['app']['configuration']['ULIBPY_TABSPACE']

	content = file_content(filepath)
	baca = content.splitlines()
	hasil = []
	for line in baca:
		m = re.match('^(\s+)(\S.*)+', line)
		if m:
			ubah = m.group(1)
			isi = m.group(2)
			# print(line, f' => [{ubah}]')
			hasil.append(ubah.replace('\t', tabstop*' ') + isi)
		else:
			# print('*no*', line)
			hasil.append(line)

	result = '\n'.join(hasil)

	write_file(filepath, result)


def space_to_tab_start(filepath, tabstop=2):
	from schnell.app.appconfig import programming_data
	tabstop = programming_data['j']['schnell']['app']['configuration']['ULIBPY_TABSPACE']

	content = file_content(filepath)
	baca = content.splitlines()
	hasil = []
	for line in baca:
		m = re.match('^(\s+)(\S.*)+', line)
		if m:
			ubah = m.group(1)
			isi = m.group(2)
			# print(line, f' => [{ubah}]')
			# hasil.append(ubah.replace('\t', tabstop*' ') + isi)
			hasil.append(ubah.replace(tabstop*' ', '\t') + isi)
		else:
			# keep line as is
			hasil.append(line)

	result = '\n'.join(hasil)

	write_file(filepath, result)


def space_to_space_start(filepath, space_old=2, space_new=4):
	# if env_exist('ULIBPY_TABSPACE'):
	# 	tabstop = env_int('ULIBPY_TABSPACE')
	# from schnell.app.appconfig import programming_data
	# tabstop = programming_data['j']['schnell']['app']['configuration']['ULIBPY_TABSPACE']

	content = file_content(filepath)
	baca = content.splitlines()
	hasil = []
	for line in baca:
		# harus ganti ke ^(\s) yg at least "space_old" size
		m = re.match('^(\s+)(\S.*)+', line)
		if m:
			ubah = m.group(1)  # prefix spaces, misal 10 spaces
			isi = m.group(2)  # non-space content
			# print(line, f' => [{ubah}]')
			# hasil.append(ubah.replace('\t', tabstop*' ') + isi)
			# bener gak nih?
			# '....' harusnya jadi '........'
			# dlm ubah=space 10, replace semua 2*' ' dg 4*' '
			hasil.append(ubah.replace(space_old*' ', space_new*' ') + isi)
		else:
			# keep line as is
			hasil.append(line)

	result = '\n'.join(hasil)

	write_file(filepath, result)


def find_entry_by_content(filepath, content_pattern, search_with_in=True):
	"""
	utk content-based search
	teknik sementara: 
	if content_pattern in baris
	"""
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	if search_with_in:
		lokasi = [(index, item) for (index, item) in enumerate(content) if content_pattern in item]
	else:
		# search dg regex
		lokasi = [(index, item, re.match(content_pattern, item)) for (index, item) in enumerate(content) if re.match(content_pattern, item)]

	if lokasi:
		ketemu = lokasi[0]
		if len(lokasi) > 1:
			print(f'multi {len(lokasi)} matches:', lokasi)

	# cari top, for item in reversed(list[:mundur])
	# cari bottom, for item in list[maju:]


def file_content_add_newline(filepath):
	content = file_content(filepath)
	if not content.endswith('\n'):
		return content + '\n'
	return content


def indent_file(filepath, line_expression, use_tab=True, num_tab=1, space_size=2):
	"""
	use_tab=False => use_space dg space_size default = 2

	line_nos = line_number_expression(len(content), line_expression)
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(process(baris) if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	"""
	from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
	tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	from .printutils import indah4

	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	line_nos = line_number_expression(len(content), line_expression)
	if not line_nos:
		indah4(f'[fileutils][indent_file] {line_nos} gak menghasilkan pada {filepath}', warna='red')
		return
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(tabber + baris if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'indent_file {filepath} OK', warna='green')


def dedent_file(filepath, line_expression, use_tab=True, num_tab=1, space_size=2):
	from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
	tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	from .printutils import indah4

	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	line_nos = line_number_expression(len(content), line_expression)
	if not line_nos:
		indah4(f'[fileutils][dedent_file] {line_nos} gak menghasilkan pada {filepath}', warna='red')
		return
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]

	def process(baris):
		if baris.startswith(tabber):
			baris = baris.removeprefix(tabber)
		else:
			baris = baris.lstrip() # hapus semua spasi dikiri
		return baris

	result = [
		(process(baris) if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'dedent_file {filepath} OK', warna='green')


def remove_prefix_by_regex(filepath, regex_expression):
	"""
	hanya beroperasi pada baris yg memenuhi regex_expression
	"""
	from .printutils import indah4
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	# line_nos = line_number_expression(len(content), line_expression)
	modified_content = [re.sub(regex_expression, '', line) for line in content]
	if modified_content == content:
		indah4(f'[fileutils] modified_content == content pada {filepath}', warna='red')
		return
	# content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	# result = [
	# 	(tabber + baris if index in line_nos else baris) 
	# 	for (index, baris) in content_with_indexes]
	if modified_content:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(modified_content)
			indah4(f'remove_prefix_by_regex {filepath} OK', warna='green')


def remove_prefix_by_lineno_and_regex(filepath, line_expression, regex_expression):
	"""
	line_number_expression(content_length, line_expression)

	kita lihat contoh indent file
	def indent_file(filepath, line_expression, use_tab=True, num_tab=1, space_size=2):

	from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
	tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)	

	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	line_nos = line_number_expression(len(content), line_expression)
	if not line_nos:
		indah4(f'[fileutils] {line_nos} gak menghasilkan pada {filepath}', warna='red')
		return
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(tabber + baris if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'indent_file {filepath} OK', warna='green')
	"""
	from .printutils import indah4
	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	line_nos = line_number_expression(len(content), line_expression)
	if not line_nos:
		indah4(f'[fileutils][remove_prefix_by_lineno_and_regex] {line_nos} gak menghasilkan pada {filepath}', warna='red')
		return
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(re.sub(regex_expression, '', baris) if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'remove_prefix_by_lineno_and_regex {filepath} OK', warna='green')


def sort_lines(filepath, start, end):
	"""
	sort_lines(somefile, 50, 70)
	"""
	# from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
	# tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	from .printutils import indah4

	# TODO: guard hanya ada 1 range: m-n

	content = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	# line_nos = line_number_expression(len(content), line_expression)
	# if not line_nos:
	# 	indah4(f'[fileutils] {line_nos} gak menghasilkan pada {filepath}', warna='red')
	# 	return
	# content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	kiri = content[:start]
	kanan = content[end+1:]
	tengah = sorted(content[start:end+1])
	result = kiri + tengah + kanan
	# result = [
	# 	(tabber + baris if index in line_nos else baris) 
	# 	for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'sort_lines {filepath} OK', warna='green')


def indent_file_by_pattern(filepath, search_pattern, use_tab=True, num_tab=1, space_size=2):
	"""
	use_tab=False => use_space dg space_size default = 2

	line_nos = line_number_expression(len(content), line_expression)
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(process(baris) if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	"""
	# from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
	# tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	from .printutils import indah4
	from .stringutils import tab_space2, tab_space4, tab_tab
	tabber = tab_tab if use_tab else (tab_space2 if space_size==2 else tab_space4)

	content = []
	line_nos = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if search_pattern in item]
		if saring:
			if len(saring) > 1:
				# kembalian = (None, 'please choose pattern: ' + str(saring))
				indah4(f'''[fileutils][indent_file_by_pattern]
				ketemu terlalu banyak pattern "{search_pattern}" match: "{saring}"
				''', warna='red')
				return
			elif len(saring) == 1:
				saring = saring[0]
				index_saring = content.index(saring)
				line_nos.append(index_saring)
		else:
			indah4(f'''[fileutils][indent_file_by_pattern]
			"{search_pattern}" tidak ketemu dalam {filepath}
			''', warna='red')
			return

	# line_nos = line_number_expression(len(content), line_expression)
	if not line_nos:
		indah4(f'[fileutils][indent_file_by_pattern] {line_nos}|{search_pattern} gak menghasilkan pada {filepath}', warna='red')
		return
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]
	result = [
		(tabber + baris if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'indent_file_by_pattern {filepath} OK', warna='green')


def dedent_file_by_pattern(filepath, search_pattern, use_tab=True, num_tab=1, space_size=2):
	# from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)	
	# tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	from .printutils import indah4
	from .stringutils import tab_space2, tab_space4, tab_tab
	tabber = tab_tab if use_tab else (tab_space2 if space_size==2 else tab_space4)

	content = []
	line_nos = []
	with open(filepath, encoding='utf-8') as fd:
		content = fd.readlines()
	if content:
		saring = [item for item in content if search_pattern in item]
		if saring:
			if len(saring) > 1:
				# kembalian = (None, 'please choose pattern: ' + str(saring))
				indah4(f'''[fileutils][dedent_file_by_pattern]
				ketemu terlalu banyak match: "{saring}"
				''', warna='red')
				return
			elif len(saring) == 1:
				saring = saring[0]
				index_saring = content.index(saring)
				line_nos.append(index_saring)
		else:
			indah4(f'''[fileutils][dedent_file_by_pattern]
			"{search_pattern}" tidak ketemu dalam {filepath}
			''', warna='red')
			return
	if not line_nos:
		indah4(f'[fileutils][dedent_file_by_pattern] {line_nos}|{search_pattern} gak menghasilkan pada {filepath}', warna='red')
		return
	content_with_indexes = [(index, baris) for (index, baris) in enumerate(content)]

	def process(baris):
		if baris.startswith(tabber):
			baris = baris.removeprefix(tabber)
		else:
			baris = baris.lstrip() # hapus semua spasi dikiri
		return baris

	result = [
		(process(baris) if index in line_nos else baris) 
		for (index, baris) in content_with_indexes]
	if result:
		with open(filepath, 'w', encoding='utf-8') as fd:
			fd.writelines(result)
			indah4(f'dedent_file_by_pattern {filepath} OK', warna='green')


def backup_file(filepath, timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')):
	"""
	rolling dg tanggal, spt gaya dulu
	kita gunakan utk: IDEA, TODO, ulib.hist
	"""
	dirpart, filepart = os.path.dirname(filepath), os.path.basename(filepath)
	filename, extension = os.path.splitext(filepart)	
	newfilename = f"{filename}-{timestamp}{extension}"
	newfilepath = os.path.join(dirpart, newfilename)
	os.rename(filepath, newfilepath)
	Path(filepath).touch()


def ulib_history():
	# import sys, tempfile
	disini = os.path.realpath(__file__)
	disini = os.path.dirname(disini) # schnell/app
	disini = os.path.join(disini, os.pardir, os.pardir, 'data')
	disini = os.path.abspath(disini)
	filename = 'ulibpy.hist'
	file_location = os.path.join(disini, filename)
	# print('ulib_history', file_location)
	# if env_exist('ULIBPY_HISTORY_FILE'):
	# 	file_location = env_get('ULIBPY_HISTORY_FILE')
	# 	if sys.platform == 'win32' and env_exist('ULIBPY_HISTORY_FILE_WIN32'):
	# 		file_location = os.path.join(tempfile.gettempdir(), env_get('ULIBPY_HISTORY_FILE_WIN32'))
	return file_location


def backup_ulib_history():
	histfile = ulib_history()
	backup_file(histfile)


def insert_at_lineno_then_tabify(filepath, ops_with_args, use_tab = True, num_tab = 1, space_size = 2):
	"""
	ini baru insert line_number, harusnya bisa juga berdasarkan pattern
	opts_with_args
		_
		line_number
		perlu_filepath_samadengan_barisentry
		s_t
		num_tab
		space_size
	"""
	from .dirutils import isfile, joiner
	from .fmusutils import fmus, filepath_samadengan_barisentry
	from .stringutils import sanitize_chars
	from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)

	line_number, perlu_filepath_samadengan_barisentry = ops_with_args[1], ops_with_args[2]
	if not line_number.startswith('-') and not line_number=='0':
		# -1 utk last line, 0 utk first line, jd jangan di -1
		line_number = int(line_number)-1
	else:
		line_number = int(line_number)
	if not isfile(filepath):
		# jk gak ketemu, coba prefix dg current cwd
		if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
			filepath = joiner(fmus.get_cwd_pwd(), filepath)
			print(f'[fileutils][insert_at_lineno_then_tabify] new filepath from cwd: {filepath}')
	content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
	content_to_insert = sanitize_chars(content_to_insert)
	# indah4(f'[file>insert] barisno {line_number}, content [{content_to_insert.strip()[:100]}...] filepath {filepath}', warna='cyan')
	# skrg content kita tabify dulu...	
	s_t = ops_with_args[3]
	if s_t.lower() == 's':
		use_tab = False
	if len(ops_with_args) == 5:
		num_tab = int(ops_with_args[4])
	elif len(ops_with_args) == 6 and not use_tab:
		num_tab = int(ops_with_args[4])
		space_size = int(ops_with_args[5])

	tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	content_to_insert = [tabber+baris for baris in content_to_insert.splitlines()]
	content_to_insert = '\n'.join(content_to_insert)
	insert_at(filepath, line_number, content_to_insert)


def insert_after_then_tabify(filepath, ops_with_args, use_tab = True, num_tab = 1, space_size = 2, modify_content_callback=None):
	"""
	opts_with_args
		_
		pattern_to_search
		perlu_filepath_samadengan_barisentry
		s_t
		num_tab
		space_size
	"""
	from .dirutils import isfile, joiner
	from .fmusutils import fmus, filepath_samadengan_barisentry
	from .printutils import indah4
	from .stringutils import sanitize_chars
	from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)
	pattern_to_search, perlu_filepath_samadengan_barisentry = ops_with_args[1],ops_with_args[2]

	if not isfile(filepath):
		# jk gak ketemu, coba prefix dg current cwd
		if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
			filepath = joiner(fmus.get_cwd_pwd(), filepath)
			print(f'[fileutils][insert_after_then_tabify] new filepath from cwd: {filepath}')

	content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
	content_to_insert = sanitize_chars(content_to_insert)
	s_t = ops_with_args[3]
	if s_t.lower() == 's':
		use_tab = False
	if len(ops_with_args) == 5:
		num_tab = int(ops_with_args[4])
	elif len(ops_with_args) == 6 and not use_tab:
		num_tab = int(ops_with_args[4])
		space_size = int(ops_with_args[5])
	# tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=space_size*' ', use_space=True)
	tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=' ', space_size=space_size, use_space=True)
	# indah4(f"🐲 [fileutils][insert_after_then_tabify] tab = [{tabber}]", warna='green', layar='black')
	indah4(f"🐲🐲🚨 [fileutils][insert_after_then_tabify] tabber = [{tabber}] num [{num_tab}] tab [{use_tab}] space [{not use_tab}] size [{space_size}]", warna='green', layar='black')
	content_to_insert = [tabber+baris for baris in content_to_insert.splitlines()]
	content_to_insert = '\n'.join(content_to_insert) + '\n'
	if modify_content_callback:
		content_to_insert = modify_content_callback(content_to_insert)
	insert_after(filepath, pattern_to_search, content_to_insert)


def insert_before_then_tabify(filepath, ops_with_args, use_tab = True, num_tab = 1, space_size = 2, modify_content_callback=None):
	"""
	opts_with_args
		_
		pattern_to_search
		perlu_filepath_samadengan_barisentry
		s_t
		num_tab
		space_size
	WARNING:
	utk perlu_filepath_samadengan_barisentry
	perlu kasih newline stlh content_to_insert
	"""
	from .dirutils import isfile, joiner
	from .fmusutils import fmus, filepath_samadengan_barisentry
	from .printutils import indah4
	from .stringutils import sanitize_chars
	from .usutils import tab # tab(num=1, space=TAB_SPACE_MULT*' ', tab='\t', use_space=True)
	pattern_to_search, perlu_filepath_samadengan_barisentry = ops_with_args[1],ops_with_args[2]

	if not isfile(filepath):
		# jk gak ketemu, coba prefix dg current cwd
		if isfile(joiner(fmus.get_cwd_pwd(), filepath)):
			filepath = joiner(fmus.get_cwd_pwd(), filepath)
			print(f'[fileutils][insert_after_then_tabify] new filepath from cwd: {filepath}')

	content_to_insert = filepath_samadengan_barisentry(perlu_filepath_samadengan_barisentry)
	content_to_insert = sanitize_chars(content_to_insert)
	s_t = ops_with_args[3]
	if s_t.lower() == 's':
		use_tab = False
	if len(ops_with_args) == 5:
		num_tab = int(ops_with_args[4])
	elif len(ops_with_args) == 6 and not use_tab:
		num_tab = int(ops_with_args[4])
		space_size = int(ops_with_args[5])
	tabber = tab(num=num_tab, use_space=False) if use_tab else tab(num=num_tab, space=' ', space_size=space_size, use_space=True)
	indah4(f"🐲🚒🐲 [fileutils][insert_before_then_tabify] tabber = [{tabber}] num [{num_tab}] tab [{use_tab}] space [{not use_tab}] size [{space_size}]", warna='green', layar='black')
	content_to_insert = [tabber+baris for baris in content_to_insert.splitlines()]
	content_to_insert = '\n'.join(content_to_insert) + '\n'
	if modify_content_callback:
		content_to_insert = modify_content_callback(content_to_insert)
	# indah4(f"🐲🚒🐲 [fileutils][insert_before_then_tabify] content_to_insert [{content_to_insert}]", warna='green', layar='black')
	insert_before(filepath, pattern_to_search, content_to_insert)


def prepend_folder_to_filelist(folder, filelist=[]):
	from .dirutils import joiner
	return [joiner(folder, item) for item in filelist]


def is_binary(filepath):
	"""
	https://stackoverflow.com/questions/44584829/how-to-determine-if-file-is-opened-in-binary-or-text-mode
	https://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
	"""
	try:
		with open(filepath, 'tr', encoding='utf8') as check_file:  # try open file in text mode
			check_file.read()
			return False
	except:  # if fail then file is non-text (binary)
		return True


def not_binary(filepath):
	return not is_binary(filepath)


# dari reversefm:
TEXTCHARS = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})


def is_file_binary(filepath):
	fd = open(filepath, 'rb')
	bytes_terbaca = fd.read(1024)
	kembali = bool(bytes_terbaca.translate(None, TEXTCHARS))
	fd.close()
	return kembali


def is_file_not_binary(filepath):
	return not is_file_binary(filepath)


def older_than(timedelta_spec):
	res = False
	return res


def newer_than(timedelta_spec):
	res = False
	return res


def handle_content_start_end(content, STARTER='__CONTENT_START__', ENDER='__CONTENT_END__'):
	"""
	file_write_timestamped_under_rootdir(filename, content, foldername='data/guilang-output', formatter='%Y%m%d_%H%M%S', write_mode='w')
	from .dirutils import tempdir
	"""
	# print(f"""[handle_content_start_end]
	# {content}""")
	result = content
	if STARTER in result and ENDER in result:
		from .dirutils import tempdir
		jumlah_content_start = content.count(STARTER)
		jumlah_content_end = content.count(ENDER)

		if jumlah_content_start == jumlah_content_end:
			mulai = 0
			result = []

			contentlines = content.splitlines()
			indexed_contentlines = [(i,item) for i,item in enumerate(contentlines)]
			start_indices = [(i,item) for (i,item) in indexed_contentlines if STARTER in item]
			end_indices = [(i,item) for (i,item) in indexed_contentlines if item.strip()==ENDER]
			if env_int('ULIBPY_FMUS_DEBUG') > 1:
				print(f"[fileutils][handle_content_start_end] start_indices = {start_indices}\n\nend_indices = {end_indices}.")

			for i,start in enumerate(start_indices):				
				# skip __CONTENT_START, sblm _CONTENT_END
				filecontent = contentlines[start[0]+1:end_indices[i][0]]
				filepath = file_write_timestamped_under_rootdir('content_start_end.txt', '\n'.join(filecontent), foldername=tempdir(), formatter=f'{i}_%Y%m%d_%H%M%S')
				modified_content_start_line = contentlines[start[0]].replace(STARTER, filepath)
				result += contentlines[mulai:start[0]] + [modified_content_start_line]
				mulai = end_indices[i][0]+1
			result += contentlines[end_indices[-1][0]+1:]
			result = '\n'.join(result)

			# handle __INPUT__ dan $00, $01 dll utk wiekes
			from .clipboardutils import replace_keyword, replace_input
			result = replace_input(result)
			result = replace_keyword(result, wieke_prefix='__wieke')

		else:
			print(f"""[fileutils][handle_content_start_end] gak sama:
			jumlah_content_start {jumlah_content_start} == jumlah_content_end {jumlah_content_end}
			""")
	if env_int('ULIBPY_FMUS_DEBUG') > 1:
		print(f"""[handle_content_start_end] result =\n[{result}]""")
	return result


def copy_to_files(source_file, dest_files):
    # Convert source file path to absolute path
    source_file = os.path.abspath(source_file)

    # Read the content of the source file
    with open(source_file, 'r') as file:
        content = file.read()

    # Iterate over the list of destination files
    for dest_file in dest_files:
        # Convert destination file path to absolute path
        dest_file = os.path.abspath(dest_file)

        # Write the content to the destination file
        with open(dest_file, 'w') as file:
            file.write(content)


def test_copy_to_files():
	source_file = 'source.txt'
	dest_files = ['dest1.txt', 'dest2.txt']
	copy_to_files(source_file, dest_files)


def sudah_ada(filepath):
	# Check if the file already exists
	if os.path.isfile(filepath):
		# Get the timestamp in ISO 8601 format
		timestamp = datetime.datetime.now().isoformat(timespec='milliseconds')
		# Append the timestamp to the file name
		base_name, ext = os.path.splitext(filepath)
		sudah_ada_filepath = f"{base_name}_{timestamp}{ext}"
	else:
		sudah_ada_filepath = filepath
	
	return sudah_ada_filepath
