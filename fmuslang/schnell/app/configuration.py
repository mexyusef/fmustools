import datetime, json, os, re

from .appconfig import programming_data
from .dirutils import (
	abs_dir,
	abs_pardir,
	absolute,
	here,
	ayah,
	tree,
	joiner,
	isdir, isfile,
	dirs, sdirs, files, sfiles, only_files,
	
)
from .printutils import indah0, print_copy_file, print_list_warna
from .utils import complete_from_list, env_get

class Configuration:

	def __init__(self, mmm=None, completing=True, abs_basedir=None):
		self.changedir_maps = {
			'.'		: abs_pardir(__file__),
			'fast'	: programming_data['j']['schnell']['app']["configuration"]["ULIBPY_COMPETITIVEDIR"],
			'frepl'	: programming_data['j']['schnell']['app']["configuration"]["ULIBPY_FAKERDIR"],
			'urepl'	: programming_data['j']['schnell']['app']["configuration"]["ULIBPY_ULANGDIR"],
			'vrepl'	: programming_data['j']['schnell']['app']["configuration"]["ULIBPY_VSCODEDIR"],
		}
		self.all_configs = {
			'cetak_waktu'						: False, 	# tm, time
			'case_insensitive_pattern_search'	: True,		# case
			'find_dirs_also'					: False,	# dirs
			'pygments'							: False,	# pyg
			# utk tampilkan hasil search ';'
			'maximum_result'					: 10,		# max
			'lexer'								: 'py',		# lex
			'last_result'						: None,
			'last_cat_filepath'					: None,
			'comma_dot_resolver_index'			: -1,
		}
		if abs_basedir:
			self.basedir = abs_basedir
		else:
			self.basedir = abs_pardir(__file__)

		self.completing = completing
		self.tab_complete = None
		self.set_curdir(self.basedir)
		self.mmm = mmm # utk dapat word of the day dst

	def in_basedir(self, code):
		return code in self.changedir_maps.keys()

	def change_basedir(self, code):
		dirpath = self.changedir_maps[code]
		self.set_curdir(dirpath)

	def is_dir_relative(self, code):
		return isdir(joiner(self.curdir, code))

	def is_file_relative(self, code):
		return isfile(joiner(self.curdir, code))

	def get_file_relative(self, code):
		return joiner(self.curdir, code)

	def waktu(self):
		# return self.all_configs['cetak_waktu']
		return programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_LATEST_SHOW_TIME"]

	@property
	def config(self):
		return self.all_configs

	def change_config(self, code):
		"""
		?time = toggle cetak waktu...
		"""
		if code == '':
			print(json.dumps(self.all_configs, indent=4))
			instruksi = """
			?tm 				toggle cetak wkt
			?case				toggle case sensitive search
			?pyg				toggle pygments
			?max 10				max result = 10
			?lex lexname		change lexer to lexname
			"""
			indah0(instruksi, warna='bright_yellow', newline=True)
		elif code == 'tm' or code == 'time':
			self.all_configs['cetak_waktu'] = not self.all_configs['cetak_waktu']
		elif code == 'case':
			self.all_configs['case_insensitive_pattern_search'] = not self.all_configs['case_insensitive_pattern_search']
		elif code == 'dirs':
			self.all_configs['find_dirs_also'] = not self.all_configs['find_dirs_also']
		elif code == 'pyg':
			self.all_configs['pygments'] = not self.all_configs['pygments']
		elif code .startswith('max '):
			code = code.replace('max ', '', 1).strip()
			if code.isdigit():
				self.all_configs['maximum_result'] = int(code)
		elif code .startswith('lex '):
			code = code.replace('lex ', '', 1).strip()
			if code in self.lexers:
				self.all_configs['lexer'] = code

	def set_curdir(self, newpath):
		"""
		setiap kali set curdir baru...termasuk di awal
		kita ambil daftar dir pd curdir, dan masukkan ke tab completer
		"""
		# berikut ini masih perlu bahkan jk tidak tab completing ?1
		self.tab_complete = dirs(newpath)
		if self.completing:			
			# mungkin bisa bentrok dg ppt?
			complete_from_list(self.tab_complete)
		
		self.curdir = newpath

	def chdir(self, newdir):
		newdir = joiner(self.curdir, newdir)
		if isdir(newdir):
			self.set_curdir(newdir)


	def dirs(self):
		# print('Dirs isi', self.curdir)
		return sdirs(self.curdir)


	def files(self):
		# print('Files isi', self.curdir)
		return sfiles(self.curdir)


	def reload_files(self):
		return only_files(self.curdir)


	def peek(self, code):
		peekpath = joiner(self.curdir, code)
		return sdirs(peekpath), sfiles(peekpath)


	def cwd(self):
		return self.curdir

	def print_file(self, filename, pygments=True):
		filepath = filename if absolute(filename) else joiner(self.curdir, filename)
		if isfile(filepath):
			print_copy_file(filepath, warna='bright_red', pygments=pygments, lexer=self.config['lexer'])

	def prompt(self):
		indah0(self.mmm.prompt + '|', warna='magenta')
		if self.all_configs['cetak_waktu']:
			waktos = str (datetime.datetime.now().time())
			indah0(waktos)
		indah0(self.curdir)

	def ask_edit_file_filename(self, filename):
		minta = input(f'Mau edit {filename}? y[n] ')
		if minta == 'y':
			edit_file(self.get_file_relative(filename))


	def ask_edit_file(self, filename_or_number):
		if not filename_or_number:
			filepath = self.config['last_cat_filepath']
			if filepath:
				self.ask_edit_file_filename(filepath)
			else:
				print('Tidak tau file apa yg hrs diedit. Cek dlm config berikut')
				print(self.config)

		elif filename_or_number.isdigit():
			# digit bisa 2 kasus: yg dihandle di sini atau nama file memang digit
			if filename_or_number in self.files():
				filepath = self.get_file_relative(filename_or_number)
				self.ask_edit_file_filename(filepath)
			else:
				filename_or_number = int(filename_or_number)
				if 1 <= filename_or_number <= len(self.files()):
					pilih = self.files() [ filename_or_number-1 ]
					self.ask_edit_file_filename(pilih)

		else:
			'''
			file gak perlu sudah ada dulu di cwd
			bisa file baru
			'''
			# print('ask_edit_file non-digit', filename_or_number)
			pilih = filename_or_number
			mungkin_ada_beberapa = [item for item in self.files() if item.startswith(filename_or_number)]
			if mungkin_ada_beberapa:
				pilih = min(mungkin_ada_beberapa, key=len)
			self.ask_edit_file_filename(pilih)


	def digit_process(self, code):
		print('vrepl/contiki: digit_process utk', code)
		m = re.match(r'^(\d+)\s*((t|d)\s*(\d+)?)?$', code)

		if code in self.files():
			filepath = self.get_file_relative(code)
			self.config['last_cat_filepath'] = filepath
			print('baca:', filepath)
			print_copy_file(filepath)
		
		elif m and m.group(1):
			print('matches:', m.groups())
			index = int(m.group(1))
			# masalahnya belum ada tempat dimana last_result di set.
			filelist = self.config['last_result']
			if filelist:
				# print(f"all {m.group()}, {m.group(0)}, start: {m.start()}, end: {m.end()}, 1={m.group(1)}, 2={m.group(2)}, 3={m.group(3)}, 4={m.group(4)}")
				# all 99t2, 99t2, start: 0, end: 4, 1=99, 2=t2, 3=t, 4=2
				filepath = filelist[index % len(filelist)]
				filepath = joiner(self.curdir, filepath)

				if isfile(filepath):
					if m.group(2): # jk 0t atau 0d
						dirpath = ayah(filepath)
						if m.group(4): # jk (\d+) terakhir -> 0t0 atau 0d0
							depth = int(m.group(4))
							while depth>0:
								dirpath = ayah(dirpath)
								depth -= 1
						if m.group(3) == 't':
							os.system(f"tree /A /F {dirpath}") # ini windows
						elif m.group(3) == 'd':
							os.system(f"dir {dirpath}")
					else: # jk digit saja
						self.config['last_cat_filepath'] = filepath
						self.config['comma_dot_resolver_index'] = index
						print_copy_file(filepath, warna='bright_red', pygments=self.config['pygments'], lexer=self.config['lexer'])
				else:
					self.config['comma_dot_resolver_index'] = index
					print(f"{filepath} is not a file for index {index}.")
