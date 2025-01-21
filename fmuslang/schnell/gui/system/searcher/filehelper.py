import os, pathlib


def walk_fullpath(basedir, skip_ends=None, filtered_ends=[]):
	"""
	skip_ends='.pyc' skip file2 berekstensi pyc
	filtered_ends='.py' hanya file2 berekstensi py
	"""
	# return [os.path.join(dp,f) for dp,dn,fn in os.walk(basedir) for f in fn]
	if skip_ends:
		# return [os.path.join(dp, f) for dp, _, fn in os.walk(basedir) for f in fn if not f.endswith(skip_ends)]
		return [os.path.join(dp, f) for dp, _, fn in os.walk(basedir) for f in fn if not all(f.endswith(lewat) for lewat in skip_ends)]
	elif filtered_ends:
		# return [os.path.join(dp, f) for dp, _, fn in os.walk(basedir) for f in fn if f.endswith(filtered_ends)]
		return [os.path.join(dp, f) for dp, _, fn in os.walk(basedir) for f in fn if any(f.endswith(lewat) for lewat in filtered_ends)]
	return [os.path.join(dp, f) for dp, _, fn in os.walk(basedir) for f in fn]


def file_content(filepath):
	"""
	retval berupa segelondongan text/string
	https://stackoverflow.com/questions/45529507/unicodedecodeerror-utf-8-codec-cant-decode-byte-0x96-in-position-35-invalid
	update utk:
	'utf-8' codec can't decode byte 0x93 in position 68384: invalid start byte
	errors='ignore'
	"""
	return pathlib.Path(filepath).read_text(encoding='utf8', errors='ignore')



def normy(path):
	return os.path.normpath(path)


def bongkar(filepath, normalize=True, debug=False):
	"""
	@returns: string bongkared filepath

	intinya: expanduser dan expandvars
	https://docs.python.org/3/library/os.path.html#os.path.expandvars
	$name
	${name}
	%name% (win32)
	~
	UPDATE 14-6-2022, kita tambah bisa __PWD
	"""
	if '__PWD' in filepath:
		if 'ULIBPY__PWD__' in os.environ:
			filepath = filepath.replace('__PWD', os.environ.get('ULIBPY__PWD__', os.getcwd()))
		else:
			filepath = filepath.replace('__PWD', os.getcwd())

	pertama = os.path.expanduser(filepath)
	kedua = os.path.expandvars(pertama)

	if filepath == kedua and filepath.startswith('ULIBPY'):
		from .utils import env_replace_filepath
		kedua = env_replace_filepath(kedua)

	if normalize:
		kedua = normy(kedua)

	if debug:
		from rich.pretty import pprint
		pprint(os.environ)

		print(f'''[dirutils.bongkar]
		input filepath = {filepath}
		kedua skrg adlh = {kedua}
		cwd adlh = {os.getcwd()}
		''')

	return kedua

