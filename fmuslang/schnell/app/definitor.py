import glob, os, re

from .dirutils import abs_dir
from .fileutils import (
	skip_lines,
	filter_lines,
	filter_lines_transform,
	filter_lines_transform_aslines,
	get_definition,
)
from .printutils import (
	print_copy,
	print_enumerate,
	indah0,
	print_file,
)
from .utils import complete_from_list


KUNCI = '►'
default_glob_prefixes = [
	# 'algo-*',
	# 'baca-*', # utk baca buku
	# 'challenge-*',
	# 'insn-*',
	# 'sample-*',
	# 'tools-*',
	# 'work-*',
	'*',
]

class BaseDefinitor:
	"""
	<invoker>: D, S
	
	perintah:
	<invoker>ulnr
		u = current file itu apa
		l = print files apa saja dlm working folder
			D = frameworks
			S = samples
		n = print isi current file
		r = reload current file dan working folder...krn entry baru atau file baru
		pref=XXX
			change invoker ke XXX secara dinamis.
	<invoker>FN
		F = filter bari di current file dg arg
		N = buat file baru di working folder dg arg 
			(lebih cepat dibanding buat dari visual studio code)
	<invoker><keyword>
		ganti current file ke file lain dalam working folder
	<keyword> (berlaku utk D dan S)
		print isi entry berisi keyword
		dlm keyword bisa gunakan pattern dan antipattern (implementasi list_grep)
		andr -mani -> ada kata andr dan gak boleh ada kata mani pada entry yg difilter

	application utk template
	S:find1 -dont find1 ~ var1 var2 var3

	"""
	INVOKER = {}
	TEMPLATE_PREFIX = '__TEMPLATE_'
	APPLY_TEMPLATE = '/' # D/func find obj -first_func ~ var1 var2 var3

	def repl(self, code):
		# print('repl:', code)
		if code == 'l': # list files di working folder
			self.print_daftar_files()
		elif code .startswith('pref='):
			newprefix = code.replace('pref=', '', 1).strip()
			if newprefix:
				self.change_prefix(newprefix)
				print('Prefix is now:', newprefix)

		elif code .startswith(BaseDefinitor.APPLY_TEMPLATE):
			code = code.replace(BaseDefinitor.APPLY_TEMPLATE, '', 1).strip()
			if code:
				self.apply_template(code)
		elif code == 'L': # list entries di current file
			content = self.get_cached()
			print_enumerate(content)
			print(BaseDefinitor.INVOKER)
		elif code == 'n':
			content = self.get_file_content()
			print_enumerate(content.splitlines())
		elif code == 'u': # current file
			print(self.data_dir + '/' + self.DEFAULT_FILE)
			print(BaseDefinitor.INVOKER)
		elif code .startswith('N') and code != 'N': # current file
			filename = code.replace('N', '', 1).strip()
			if filename:
				filepath = os.path.join(self.data_dir, filename)
				os.system(f'code "{filepath}"')
		elif code .startswith('F') and code != 'F': # current file
			hasil = filter_lines(self.DEFAULT_FILEPATH, '^.*' + code.replace('F', '', 1).strip() + '.*')
			print(hasil)
		elif code == 'r':
			self.reload()
		elif code == 'e': # current file
			os.system(f'code {self.DEFAULT_FILEPATH}')
		elif code.strip().isdigit():
			content = self.get_cached()
			baris = content[int(code)]
			result = self.definisi(baris).strip()
			print('-'*40, baris)
			print_copy(result)
		else:
			found = [item for item in self.daftar_files if code in item]
			if found:
				if len(found) == 1:
					print('change to:', found[0])
					self.change_file(found[0])
				else:
					print('choose between:', found)
			elif ' ' in code:
				search = code.split()
				found = [item for item in self.daftar_files if all([cari in item for cari in search])]
				if found:
					if len(found) == 1:
						print('change by step 2 to:', found[0])
						self.change_file(found[0])
					else:
						print('choose by step 2 between:', found)

	def reload(self):
		print('reloading D...')
		self.daftar_files = self.load_dir()
		self.clear_key(self.DEFAULT_FILE)
		if self.TAB_COMPLETE:
			complete_from_list(self.get_cached())


	def load_dir(self):
		files_grabbed = []
		for arsip in self.GLOB_PATTERNS:
			files_grabbed.extend(glob.glob(self.data_dir + '/' + arsip))
		return [os.path.basename(item) for item in files_grabbed]


	def __init__(self, default_file='scala',
		data_dir='samples', 
		kunci=KUNCI, 
		tab_completer=False,
		glob_patterns=default_glob_prefixes,
		default_prefix='D'):
		self.DEFAULT_FILE = default_file
		self.DATA_DIR = data_dir
		self.data_dir = os.path.join(abs_dir(__file__), self.DATA_DIR)
		self.DEFAULT_FILEPATH = os.path.join(self.data_dir, self.DEFAULT_FILE)

		self.RE_SKIP_COMMENT = r'^(//.*)|$'
		self.CACHED_KEYS = {}
		self.KUNCI = kunci
		self.TAB_COMPLETE = tab_completer
		self.GLOB_PATTERNS = glob_patterns
		self.daftar_files = self.load_dir()
		if self.TAB_COMPLETE:
			complete_from_list(self.get_cached())

		self.PREFIX = default_prefix
		BaseDefinitor.INVOKER[id(self)] = self.PREFIX


	def change_prefix(self, newprefix):
		self.PREFIX = newprefix
		BaseDefinitor.INVOKER[id(self)] = self.PREFIX
		# try:
		# 	BaseDefinitor.INVOKER[str(id(self))] = self.PREFIX
		# except Exception as err:
		# 	print('gagal indexing id', str(id(self)), err)


	def get_daftar_files(self):
		return self.daftar_files


	def print_daftar_files(self):
		print_enumerate(self.daftar_files)


	def get_file_content(self):
		"""
		skip //
		skip ^$
		"""
		filename = self.DEFAULT_FILEPATH
		content = skip_lines(filename, self.RE_SKIP_COMMENT)
		return content


	def change_file(self, newfile):
		self.DEFAULT_FILE = newfile
		self.DEFAULT_FILEPATH = os.path.join(self.data_dir, self.DEFAULT_FILE)
		if self.TAB_COMPLETE:
			complete_from_list(self.get_cached()) # dari default_filepath baru
		return self.DEFAULT_FILEPATH


	def get_daftar(self):
		"""get baris2 kunci yg diawali dg self.KUNCI
		kembalikan ter-transform tanpa self.KUNCI
		"""
		filename = self.DEFAULT_FILEPATH
		FILTER_CONDITION = f'^{self.KUNCI}\s+'
		def transformer(baris):
			return baris.replace(self.KUNCI, '', 1).strip()
		content = filter_lines_transform_aslines(filename, FILTER_CONDITION, transformer)
		return content


	def get_cached(self):
		keyfile = self.DEFAULT_FILE
		if keyfile not in self.CACHED_KEYS:
			# fullpath = self.change_file(keyfile)
			result = self.get_daftar()
			self.CACHED_KEYS[keyfile] = result
			return self.CACHED_KEYS[keyfile]
		else:
			return self.CACHED_KEYS[keyfile]


	def clear_cache(self, ):
		# globals() [CACHED_KEYS] = {}
		self.CACHED_KEYS = {}


	def clear_key(self, keyfile):
		# global CACHED_KEYS
		del self.CACHED_KEYS[keyfile]


	def reload_cache(self, keyfile):
		self.clear_key(keyfile)
		return self.get_cached(keyfile)


	def definisi(self, baris):
		filename = self.DEFAULT_FILE
		filepath = os.path.join(self.data_dir, filename)
		# print('definisi utk', filepath)
		return get_definition(filepath, f'^{self.KUNCI}\s+{baris}\s+$', f'^{self.KUNCI}')


	def list_grep(self, code, haystack):
		"""code berisi [cari -jangan cari -jangan]
		haystack adlh baris yg diperoleh dari file: self.KUNCI isi-baris
		result lalu kita ambil dari haystack
		kurangi yg ada antipatterns
		filter hanya yg ada patterns
		"""
		antipatterns = [item.replace('-','',1) for item in code 
			if re.match(r'^-[\w\d]+', item)]
		patterns = [item for item in code 
			if not re.match(r'^-[\w\d]+', item)]

		# print('anti:', antipatterns)
		# print('pat:', patterns)

		result = haystack

		if antipatterns:
			result = filter(lambda line_item: all(
				[item not in line_item for item in antipatterns]), result)

		result = filter(lambda line_item: all(
			[item in line_item for item in patterns]), result)
		
		return list(result)


	@staticmethod
	def manual_definisi(baris, filename, kunci_start=KUNCI, kunci_end=None):
		"""
		filename di sini adlh filepath...
		"""
		kunci_end = f'^{kunci_start}' if not kunci_end else kunci_end
		return get_definition(filename, f'^{kunci_start}\s+{baris}\s+$', kunci_end)


	@staticmethod
	def manual_list_grep(code, filename, kunci_start='--%', kunci_end='--#'):
		"""
		filename di sini adlh filepath...

		ini agar bisa dipanggil spt fungsi
		code hrs kita jadikan list dulu!

		code berisi [cari -jangan cari -jangan]
		haystack adlh baris yg diperoleh dari file: self.KUNCI isi-baris
		result lalu kita ambil dari haystack
		kurangi yg ada antipatterns
		filter hanya yg ada patterns
		"""
		
		# code dlm bentuk list
		if isinstance(code, str):
			code = [code]

		# kunci_end = f'^{kunci_start}' if not kunci_end else kunci_end
		# FILTER_CONDITION = f'^{kunci_start}\s+'
		FILTER_CONDITION = f'^{kunci_start}\s+'

		def transformer(baris):
			return baris.replace(kunci_start, '', 1).strip()

		# get daftar isi		
		haystack = filter_lines_transform_aslines(filename, FILTER_CONDITION, transformer)

		antipatterns = [item.replace('-','',1) for item in code
			if re.match(r'^-[\w\d]+', item)]
		patterns = [item for item in code 
			if not re.match(r'^-[\w\d]+', item)]

		# print('manual_list_grep => anti:', antipatterns)
		# print('manual_list_grep => pat:', patterns)

		result = haystack

		if antipatterns:
			result = filter(lambda line_item: all(
				[item not in line_item for item in antipatterns]), result)

		result = filter(lambda line_item: all(
			[item in line_item for item in patterns]), result)

		return list(result)

	def apply_template(self, code):
		"""
		konsepnya:
		Dcari -jangan cari jangan ~ var1 var2 var3
		"""
		if '~' in code:
			pencarian, variables = code.split('~')
			hasil = self.list_grep(pencarian.split(), self.get_cached())
			if len(hasil) == 1: # sementara jk hanya ketemu 1 yg match
				# print('apakah ini list?')
				content = self.definisi(hasil[0]).strip()
				if BaseDefinitor.TEMPLATE_PREFIX in content:
					for index, item in enumerate(variables.split(), 1):
						content = content.replace(BaseDefinitor.TEMPLATE_PREFIX + str(index), item)

				indah0(('-'*40) + hasil[0], warna='yellow', layar='black', newline=True)
				print_copy(content)
				return True

		return False
