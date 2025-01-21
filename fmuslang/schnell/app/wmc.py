import json, os, re, shutil, sys, traceback
from dotenv import load_dotenv
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.application.current import get_app

# appdir = os.path.dirname(__file__)
# ENV_FILE = os.path.join(appdir, os.pardir, '.env')
# load_dotenv(ENV_FILE)
# schnelldir = os.environ.get('ULIBPY_BASEDIR', os.getcwd())
# sys.path.insert(0, schnelldir) # hrs duluan dari appdir

from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(sidoarjodir)
from schnell.app.appconfig import programming_data

from schnell.app.fmus import Fmus
from schnell.app.greputils import (
	curdir_grep, system_grep, system_grep_limitchars, system_find,
)
from schnell.app.dirutils import (
	ayah,
	find_patterns,
	isdir, isfile,
	joiner,
	getcwd,
	# filter_print_latest_files,
)
from schnell.app.executor import script_handler
from schnell.app.fileutils import (
	get_daftar,
	get_extension,
	get_definition_by_key_permissive_start,
	get_definition_double_entry_aware,
)
from schnell.app.printutils import (
	Debug,
	dir_w,
	filter_print_latest_files,
	indah0, indah3,
	print_file,
	indah_file,
	print_copy,
	print_copy_enumerate,
	print_copy_enumerate_list,
	print_copy_file,
	print_list_warna,
)
from schnell.app.utils import (
	env_get, env_int,
	env_expand,
	env_get_fuzzy,
	yesno,
	perintah,
)
from schnell.app.communication import start_client
from schnell.app.configuration import Configuration as Konfigurasi
from schnell.app.punctuation import Punctuation

from multiprocessing.connection import Client
from schnell.app.communication import start_client # client ke host

GUEST_CLI_HOST = 'localhost'
GUEST_CLI_PORT = 17101
GUEST_CLI_PASS = b'rahasia'

HELP_LINE = '\n'
# HELP_LINE += '?;?swi;?type;?title judul;?key ctrl+v;#judul lama#judul baru\n'
# HELP_LINE += '-3 atau +3;+3* (exec file);+3/1 print;+3 1 (exec entry 1)'

motd_hide = """
https://codeforces.com/?locale=en
https://leetcode.com/
https://skillenza.com/
https://www.challenge.gov/
https://www.codechef.com/
https://www.coderbyte.com/
https://www.codewars.com/
https://www.codingame.com/
https://www.hackerearth.com/
https://www.hackerrank.com/
https://www.interviewbit.com/contests/
https://www.kaggle.com/
https://www.topcoder.com/
http://www.hpcodewars.org/
http://www.programmr.com/
"""

motd = """
__/\\\______________/\\\_        __/\\\\____________/\\\\_        ________/\\\\\\\\\_        
 _\/\\\_____________\/\\\_        _\/\\\\\\________/\\\\\\_        _____/\\\////////__       
	_\/\\\_____________\/\\\_        _\/\\\//\\\____/\\\//\\\_        ___/\\\/___________      
	 _\//\\\____/\\\____/\\\__        _\/\\\\///\\\/\\\/_\/\\\_        __/\\\_____________     
		__\//\\\__/\\\\\__/\\\___        _\/\\\__\///\\\/___\/\\\_        _\/\\\_____________    
		 ___\//\\\/\\\/\\\/\\\____        _\/\\\____\///_____\/\\\_        _\//\\\____________   
			____\//\\\\\\//\\\\\_____        _\/\\\_____________\/\\\_        __\///\\\__________  
			 _____\//\\\__\//\\\______        _\/\\\_____________\/\\\_        ____\////\\\\\\\\\_ 
				______\///____\///_______        _\///______________\///__        _______\/////////__

"""


motd_list = motd.strip().splitlines()


class WmCurse:

	W = 1366
	H = 768

	def __init__(self, initial_basepath=None):
		self.done = False
		self.config = {

			# gedit dan mousepad gak reflek perubahan external
			'logviewer': ['code', 'mousepad', 'gedit', 'atom'],
			'viewerindex': 0,
			# outputdir dipake jk kita mau generate file (dari /tmp/work.txt)
			'outputdir': '/tmp',

			'workdir': '/tmp',
			'workfile': 'work.txt',

			'initial_source': 'tensorflow.tpl',
			'use_atom': False, # jk code lagi ngawur

			'switch_window': False,
			'switch_window_title': 'untitled',
			'typing_mode': False,
			'paste_keys': 'ctrl+v',
			'toc_line_limit': 10,
			'toc_sort': True,
		}
		is_debugging = programming_data['debug']
		self.debug = Debug(is_debugging)
		self.fmus = Fmus(debug=is_debugging)
		self.ubuntu = Punctuation()
		self.setup_handlers()

		CODES = '' # pathlib.Path(here(__file__)) / 'codes'
		# overriding basedir jk dari command line atau dari env
		if len(sys.argv) == 2 and isdir(sys.argv[1]):
			CODES = os.path.abspath(sys.argv[1])
		else:
			# dirname = xcurse, pardir = ulibpy
			if 'ULIBPY_WMC_DIR' in os.environ:
				# print(f"ganti fmdir dari {CODES} ke {programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_DIR"]}")
				CODES = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_DIR"]

		if initial_basepath and isdir(initial_basepath):
			CODES = initial_basepath

		self.konfigurasi = Konfigurasi(abs_basedir=CODES)
		# self.rpc_server_port = 17001
		address = (GUEST_CLI_HOST, GUEST_CLI_PORT)
		try:
			if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
				self.client = Client(address, authkey=GUEST_CLI_PASS)
				self.client_to_host = start_client()
		except Exception as err:
			print('Jika jalan standalone kita skip:', err)
			self.client = None
			self.client_to_host = None
		# conn.send('close')
		# can also send arbitrary objects:
		# conn.send(['a', 2.5, None, int, sum])
		# conn.close()


	def fmus_list_entries(self, m1):
		choice = int(m1.group(1)) - 1
		
		pilihan = self.konfigurasi.files()[choice]

		# daftar_file = self.konfigurasi.reload_files()
		# pilihan = daftar_file[choice]
		# yesno = input(f'Anda pilih {pilihan}? Tekan "y" utk lanjut... ')

		pilihan = self.konfigurasi.get_file_relative(pilihan)
		entries = get_daftar(pilihan)
		print_list_warna(entries)
		# print di textarea
		if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
			self.client_to_host.comm_handler(entries)


	def fmus_print_entry(self, m3):
		choice = int(m3.group(1)) - 1
		baris = int(m3.group(2))
		
		# TODO
		# di sini bahaya: jk file mk ditambah pd satu dir, files masih sama
		# daftar_file = self.konfigurasi.files()
		# pilihan = self.konfigurasi.files()[daftar_file]

		daftar_file = self.konfigurasi.reload_files()
		pilihan = daftar_file[choice]
		# yesno = input(f'Anda pilih {pilihan}? Tekan "y" utk lanjut... ')
		# if yesno != 'y':
		# 	return

		pilihan = self.konfigurasi.get_file_relative(pilihan)
		# spt -<digit>, ambil daftar dulu
		entries = get_daftar(pilihan)
		if 0 <= baris < len(entries):
			entry_title = entries[baris]
			# start_regex = entry_title
			start_regex = '^--% '
			end_regex = '^--#'
			# if pilihan.endswith('.mk'):
			# 	start_regex = '^--% '
			# 	end_regex = '^--#'

			if env_int('ULIBPY_FMUS_DEBUG'):
				print('start_regex:', start_regex, 'end_regex:', end_regex, 'file:', pilihan, 'baris:', entry_title)
			# program = get_definition(pilihan, start_regex, end_regex)
			# program = get_definition_by_key_permissive_start(pilihan, entry_title)
			program = get_definition_double_entry_aware(pilihan, entry_title)
			indah0(entry_title, warna='yellow', newline=True, bold=True)
			print_copy_enumerate(program)
			if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
				self.client_to_host.comm_handler(program)


	def fmus_exec_entry(self, m2):
		choice = int(m2.group(1)) - 1
		baris = int(m2.group(2))

		# pilihan = self.konfigurasi.files()[choice]

		daftar_file = self.konfigurasi.reload_files()
		pilihan = daftar_file[choice]
		pilihan = self.konfigurasi.get_file_relative(pilihan)
		entries = get_daftar(pilihan)
		indah0(f'Anda pilih "{pilihan} | {entries[baris]}"?\nTekan "y" utk lanjut:', warna='cyan', bold=True)
		yesno = input(' ')
		if yesno != 'y':
			return
		
		self.fmus.set_file_template(pilihan) # __FILE
		self.fmus.set_dir_template(self.konfigurasi.cwd()) # __CURDIR/file.tpl di program
		# print('m2, pilihan:', pilihan, 'jumlah entries:', len(entries))
		if 0 <= baris < len(entries):
			entry_title = entries[baris]
			# start_regex = entry_title
			start_regex = '^--%'
			end_regex = '^--#'
			# if pilihan.endswith('.mk'):
			# 	start_regex = '^--% '
			# 	end_regex = '^--#'
			
			if env_int('ULIBPY_FMUS_DEBUG'):
				print('fmus_exec_entry start_regex:', start_regex, 'end_regex:', end_regex)
			# program = get_definition(pilihan, start_regex, end_regex)
			# program = get_definition_by_key_permissive_start(pilihan, entry_title)
			program = get_definition_double_entry_aware(pilihan, entry_title)
			if env_int('ULIBPY_FMUS_DEBUG'):
				print('fmus_exec_entry get program:', program[:40])
			self.fmus.process(program)


	def fmus_exec_file(self, m):
		choice = int(m.group(1)) - 1
		# pilihan = self.konfigurasi.files()[int(code)-1]
		pilihan = self.konfigurasi.files()[choice]
		pilihan = self.konfigurasi.get_file_relative(pilihan)
		self.fmus.load_and_process(pilihan)


	def handle_fmus_program(self, code):
		"""
		bikin ini krn lebih singkat dari fm <fileno> <entryno>
		menjadi +<fileno> <entryno>
		"""
		self.debug('handle_fmus_program:', code)
		if code:
			m = re.match(r'^\s*(\d+)\*\s*$', code) # execute fm <fileno>*
			m1 = re.match(r'^\s*(\d+)\s*$', code) # list entries: fm <fileno>
			m2 = re.match(r'^\s*(\d+)\s+(\d+)$', code) # fm <fileno> <entryno> = exec fm.us from entry
			m3 = re.match(r'^\s*(\d+)\s*/\s*(\d+)$', code) # fm <fileno> / <entryno> = print entry (bisa fm.us atau apa saja)

			if m:
				'''
				+1*
				'''
				self.debug('fmus_exec_file:', code, 'match m0:', m.groups())
				self.fmus_exec_file(m)
			elif m1:
				'''
				+1
				'''
				self.debug('fmus_list_entries:', code, 'match m1:', m1.groups())
				self.fmus_list_entries(m1)
			elif m2:
				'''
				+1 0
				'''
				self.debug('fmus_exec_entry:', code, 'match m2:', m2.groups())
				self.fmus_exec_entry(m2)
			elif m3:
				'''
				+1/0
				'''
				self.debug('fmus_print_entry:', code, 'match m3:', m3.groups())
				self.fmus_print_entry(m3)
			else:
				self.debug('code:', code, 'tdk ada yg match')


	def change_configuration(self, code=None):
		"""
		'switch_window': True,
		'switch_window_title': 'untitled',
		'typing_mode': False,
		'paste_keys': 'ctrl+v',

		toggle: 
			swi
			type
		string:
			title <title dari window utk di switch>
			key <key utk paste stlh switching window>
		"""
		# self.debug('change_configuration')
		if not code:
			pass
			# self.print_config()

		elif code .startswith('title '):
			title = code.replace('title ', '', 1).strip()
			if title:
				self.config['switch_window_title'] = title

		elif code .startswith('key '):
			key = code.replace('key ', '', 1).strip()
			if key:
				self.config['paste_keys'] = key
		
		elif code == 'T' or code == 'type':
			self.config['typing_mode'] = not self.config['typing_mode']

		elif code == 'S' or code == 'sw' or code == 'swi' or code == 'switch':
			self.config['switch_window'] = not self.config['switch_window']

		elif code == 'ts' or code == 'tsort' or code == 'toc_sort': # ?atom
			self.config['toc_sort'] = not self.config['toc_sort']

		elif code == 'atom': # ?atom
			self.config['use_atom'] = not self.config['use_atom']

		elif code .startswith('toc'):
			key = code.replace('toc', '', 1).strip()
			if key and key.isdigit():
				key = int(key)
				if key:
					self.config['toc_line_limit'] = key

		self.print_config()


	def handle_clipboard_program(self, code=None):
		"""
		di sini __FILE gak ada tapi __CURDIR ok
		harusnya ask user: mau set __FILE? jk ya maka __CURDIR set dari situ
		"""
		#self.fmus.set_file_template(pilihan) # __FILE
		# cek __FILE
		self.fmus.set_dir_template(self.konfigurasi.cwd()) # __CURDIR/file.tpl di program
		self.fmus.clipboard_load_and_process()


	def lakukan(self, perintah):
		"""
		!*bash akan masuk lokasi wmc saat itu
		bukan cwd waktu launch wmp/term
		"""
		if perintah.startswith('*'):
			perintah = perintah.replace('*', '', 1).strip()
			# os.chdir(self.konfigurasi.cwd())
			perintah = f'cd {self.konfigurasi.cwd()} && ' + perintah
		os.system(perintah)


	def setup_handlers(self):
		# self.ubuntu.set_handler('`', self.activate_xcurse) # keluar/masuk xcurse dg `
		# self.ubuntu.set_handler('-', self.list_entries)
		self.ubuntu.set_handler(':', lambda bahasa: script_handler(bahasa))
		self.ubuntu.set_handler('+', self.handle_fmus_program)
		# self.ubuntu.set_handler('!', lambda lakukan: os.system(lakukan))
		self.ubuntu.set_handler('!', self.lakukan)
		self.ubuntu.set_handler('?', self.change_configuration)
		self.ubuntu.set_handler('#', lambda fileno: self.edit_file(fileno))
		# harus menerima code=None, klo gak gak diexec
		self.ubuntu.set_handler('%', self.handle_clipboard_program)
		self.ubuntu.set_handler('/', lambda cari: system_grep(self.konfigurasi.cwd(), cari))
		self.ubuntu.set_handler('\\', lambda cari: curdir_grep(self.konfigurasi.cwd(), cari))
		self.ubuntu.set_handler('<', lambda cari: self.system_grep_charlimit(cari))
		self.ubuntu.set_handler('>', lambda cari: system_find(self.konfigurasi.cwd(), cari))
		# terakhir adlh cetak waktu, lihat ulibpy/vrepl/vrepl.py 113
		# self.ubuntu.set_handler('|', lambda cari: filter_print_latest_files(self.konfigurasi.cwd(), False))


	def system_grep_charlimit(self, cari, delimiter='/'):
		"""
		<10/something to find
		"""
		cari = cari.replace('G/', '', 1).strip()
		batas, pola = cari.split(delimiter)
		if batas.isdigit() and pola:
			system_grep_limitchars(self.konfigurasi.cwd(), pola, batas)


	@property
	def prompt(self):
		return f'wmc|{self.konfigurasi.cwd()}>'


	def print_config(self):
		config = json.dumps(self.config, indent=4)
		self.debug(config)
		if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
			self.client_to_host.comm_handler(config)


	def edit_file(self, code):
		"""
		code.isdigit() and int(code) in range(1,len(self.konfigurasi.files())+1):
		"""
		from .utils import platform
		if code.isdigit() and int(code) in range(1,len(self.konfigurasi.files())+1):
			zero_index = int(code)-1
			pilihan = self.konfigurasi.files()[zero_index]
			pilihan = self.konfigurasi.get_file_relative(pilihan)
			# indah_file(pilihan)
			if platform() == 'wsl':
				os.system(f'touch "{pilihan}" && code "{pilihan}"')
			else:
				os.system(f'code "{pilihan}"')
		else:
			if code in self.konfigurasi.files():
				pilihan = self.konfigurasi.get_file_relative(code)
				if platform() == 'wsl':
					os.system(f'touch "{pilihan}" && code "{pilihan}"')
				else:
					os.system(f'code "{pilihan}"')
			elif [filename for filename in self.konfigurasi.files() if code.lower() in filename.lower()]:
				daftar = [filename for filename in self.konfigurasi.files() if code.lower() in filename.lower()]
				if len(daftar) == 1:
					pilihan = self.konfigurasi.get_file_relative(daftar[0])
					if platform() == 'wsl':
						os.system(f'touch "{pilihan}" && code "{pilihan}"')
					else:
						os.system(f'code "{pilihan}"')
				else:
					print('Please choose a closer match:')
					print_list_warna(daftar)
			else:
				# create one?
				indah0(f'Create {code}?', warna='white', newline=False)
				yesno = input(' ')
				if yesno == 'y' or yesno == 'Y':
					pilihan = self.konfigurasi.get_file_relative(code)
					if platform() == 'wsl':
						os.system(f'touch "{pilihan}" && code "{pilihan}"')
					else:
						os.system(f'code "{pilihan}"')


	def fastcoder(self, code):

		self.debug(f"wmc: {code}\n")

		if code and code[0] in self.ubuntu.handled_punctuations():
			self.ubuntu.execute(code)

		elif code .startswith('|'):
			code = code.replace('|', '', 1).strip()
			def internal():
				# hasil = filter_print_latest_files(code, self.konfigurasi.cwd(), self.konfigurasi.waktu())
				hasil = filter_print_latest_files(code, self.konfigurasi.cwd(), programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_LATEST_SHOW_TIME"])
			# self.konfigurasi.config['last_result'] = hasil
			# perlu konfig utk run in prompt toolkit or not
			# run_in_terminal(internal)
			internal()

		elif code .startswith(';'):
			def internal():
				find_patterns(code.replace(';', '', 1), self.konfigurasi.cwd(), self.konfigurasi.config)
				# self.debug('returning from terminal...')
			# get_app() # ternyata dapatnya dummy app
			# run_in_terminal(internal)
			internal()
		
		elif code .startswith('.'):
			"""
			pindah direktori
			hanya proses dot, walaupun bisa kasih .some..thing.and...more...
			"""
			# self.debug('masuk dot di wmcurse...')
			times = code.count('.')
			par = ayah(self.konfigurasi.curdir, times)
			self.konfigurasi.chdir(par)
			self.debug(par + '\n')

		elif code .startswith('cd '):

			code = code.replace('cd ', '', 1).strip()
			
			self.debug(f'pindah ke {code}\n')

			if isdir(code):
				self.konfigurasi.chdir(code)
			else:
				# ini utk cd sej => masuk ke sejarah
				# tapi berbasis pada daftar sejarah
				fuzzy = env_get_fuzzy(code)
				if fuzzy:
					fuzzy_dir = env_expand(fuzzy, bongkarin=True)
					indah3(f'try fuzzy: {code} => {fuzzy} => {fuzzy_dir}')
					if isdir(fuzzy_dir):
						self.konfigurasi.chdir(fuzzy_dir)
						code = fuzzy_dir
				elif env_expand(code):
					xpdir = env_expand(code, bongkarin=True)
					if code == xpdir:
						from schnell.app.utils import env_ulibpy_values
						envulibs = env_ulibpy_values()
						print_list_warna([item for item in envulibs if code.lower() in item.lower()])
					else:
						indah3(f'expanding {code} => {xpdir}')
						if isdir(xpdir):						
							self.konfigurasi.chdir(xpdir)
							code = xpdir
				else:
					indah3(f'donno how to play with {code}', warna='red')

			self.debug(code + '\n')

		elif code == 'tx':
			'''send message to guest cli'''
			self.client.send(self.konfigurasi.cwd())

		elif code == 'chooselang':
			from schnell.app.prompter import RadioInput
			pilihan = RadioInput().run()
			# self.debug(type(pilihan))
			command = {
				'type': 'apply_lexer',
				'language': pilihan[1],
				'lexer': pilihan[0],
			}
			if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
				self.client_to_host.comm_handler(command)

		elif code == 'choosefile':
			from schnell.app.prompter import GetFilename
			pilihan = GetFilename().run()
			command = {
				'type': 'save_filename',
				'filename': pilihan,
				# 'language': pilihan[1],
				# 'lexer': pilihan[0],
			}
			if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
				self.client_to_host.comm_handler(command)

		elif code .startswith('del '):
			code = code.replace('del ', '', 1).strip()
			m = re.match(r'^(\d+)(\s*,\s*(\d+))?', code)
			if m:
				start = int(m.group(1))
				params = [start]
				if m.group(3):
					end = int(m.group(3))
					params += [end]
				
				command = {
					'type': 'hapus_baris',
					'args': params
				}
				if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
					self.client_to_host.comm_handler(command)

		elif code == 'E' or code == 'A':
			'''
			skrg bisa buka coder sesuai navigasi contiki...
			'''
			editor = 'code' if code == 'E' else 'atom'
			os.system(f"{editor} {self.konfigurasi.cwd()}")

		# elif code == 'K':
		# 	buka_tutup = '--% \n--#'
		# 	print_copy(buka_tutup)

		elif code in ['atom', 'mp', 'ge', 'npp', 'vi', 'vim']:
			background = '&'
			editor = 'mousepad'
			folder = ''
			if code == 'atom':
				editor = 'atom'
				folder = self.konfigurasi.cwd()
				background = ''
			elif code == 'ge':
				editor = 'gedit'
			elif code == 'vi' or code == 'vim':
				editor = 'gvim'
				folder = self.konfigurasi.cwd()

			os.system(f"{editor} {folder}{background}")

		elif code .startswith('gen ') or code == 'gen':
			'''
			self.konfigurasi.curdir
			'''
			from schnell.app.generator import Generator
			from schnell.app.dirutils import absolute
			# Generator().ask()
			code = code.replace('gen', '', 1).strip()
			if code == '':
				Generator().ask_with_qt()
			elif isdir(code):
				'''code adlh basedir'''
				if not absolute(code):
					code = joiner(self.konfigurasi.curdir, code)
				Generator().ask_with_qt(code)

		elif code .startswith('entrify ') or code == 'entrify':
			from schnell.app.entryfier import Generator
			code = code.replace('entrify', '', 1).strip()
			if code == '':
				Generator().ask_with_qt()
			elif isdir(code):
				Generator().ask_with_qt(code)

		elif code .startswith('flash'):
			pass
			from schnell.app.flashcard import FlashCard
			code = code.replace('flashcard', '', 1).strip()
			code = code.replace('flash', '', 1).strip()
			filename, start, end = FlashCard.ask()
			if filename and (start >=0 ) and (end >= 0):
				flasher = FlashCard(filename, start, end)
				flasher.generate()
				self.debug(flasher.basedir)
				yesno(f'Pindah ke {flasher.basedir}? y[n]', lambda: self.konfigurasi.chdir(flasher.basedir))

		elif code == 'ls' or code == 'll':
			hanya_file = self.konfigurasi.files()
			if code == 'ls':
				# dir_w(hanya_file, warna='yellow')
				dir_w(hanya_file, warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOREGROUND"])
			elif code == 'll':
				# dir_w([f"{n}. {i}" for n,i in enumerate(hanya_file,1)], warna='bright_blue', layar='white')
				dir_w([f"{n}. {i}" for n,i in enumerate(hanya_file,1)], warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOREGROUND"], layar=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_BACKGROUND"])
		
		elif code .startswith ('L'):
			code = code.strip()
			if code == 'L':
				res = self.konfigurasi.dirs()
				# dir_w(res)
				# dir_w([item for item in hanya_direktori], warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOLDERCOLOR"])
				dir_w(res, warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOLDERCOLOR"])
			else:
				hanya_file = self.konfigurasi.files()
				args = code.replace('L', '', 1).strip()
				if args and args.isdigit():
					'''dari sebuah file template (bukan file program)
					kita pengen list daftar entries nya...
					nanti kita bisa print juga: definisi utk entry yg dipilih
					L<digit utk filename>
					L<digit utk filename>,<digit utk entry>
					'''
					if (int(args) in range(1,len(hanya_file)+1)):
						self.debug('L + digit')
						# pilih = os.path.join(konfigurasi.cwd(), hanya_file[int(args)-1])
						pilih = self.konfigurasi.get_file_relative(hanya_file[int(args)-1])
						print_list_warna(get_daftar(pilih))
				else:
					self.debug('L + dirname')
					dirs, files = self.konfigurasi.peek(args)
					dir_w(dirs)
					dir_w(files, warna='yellow')

		elif code == 'l':
			dir_w(self.konfigurasi.dirs(), warna='yellow')
			# dir_w(self.konfigurasi.files(), warna='yellow')
			# dir_w([f"{n}. {i}" for n,i in enumerate(self.konfigurasi.files(),1)], warna='bright_blue', layar='white')
			dir_w([f"{n}. {i}" for n,i in enumerate(self.konfigurasi.files(),1)], warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOREGROUND"], layar=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_BACKGROUND"])

		elif code == 'size':
			ukuran = shutil.get_terminal_size()
			w = ukuran.columns
			h = ukuran.lines
			self.debug(f"Screen {w}x{h}")

		elif code == 'reload':
			from schnell.app.utils import env_reload
			env_reload()

		elif code == 'c' or code == 'cls' or code == 'clear':
			os.system('clear')
			# if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_WITHIN_GUI"]:
			# 	self.client_to_host.comm_handler('cls')
	
		elif code in self.konfigurasi.tab_complete:
			'''tab complete kita isi daftar dir'''
			self.konfigurasi.chdir(code)

		elif code.isdigit() and int(code) in range(1,len(self.konfigurasi.files())+1):
			'''digit hrs duluan dari 'parts of file'
			jk 20 utk minta python.mk
			jangan dikasih 2021.mk
			'''
			try:
				zero_index = int(code)-1
				pilihan = self.konfigurasi.files()[zero_index]
				pilihan = self.konfigurasi.get_file_relative(pilihan)
				indah_file(pilihan)
				# originally ini cursing...
				# self.debug('siap xcursing:', pilihan)
				# self.client.send({
				# 	'type': 'xcurse',
				# 	'filepath': pilihan,
				# })
			except Exception as err:
				indah3(f'Dont know how to process {code} => {err}.')

		elif code and [item for item in self.konfigurasi.files() if item.startswith(code.removesuffix('*') if code.endswith('*') else code)]:
			'''
			jk user ketik py dan ada python.mk di files()
			maka ask: mau 'xcurse' python.mk?
			update: kita ubah 
			- print isi file
			- open dg code jk diakhiri *

			jk user ketik:
			sejarah nama*
			maka edit file yg filenamenya berisi "sejarah nama"
			'''
			# print('mau open atau edit:', code)
			is_edit = False
			if code.endswith('*'):
				is_edit = True
				code = code.removesuffix('*')
				# print('code now:', code)

			mungkin_ada_beberapa = [item for item in self.konfigurasi.files() if item.startswith(code)]
			# ubah
			# old: ambil 1 dari daftar yg paling match dan either print atau edit (jk diakhiri *)
			# skrg, jk ada bbrp maka print daftar
			if len(mungkin_ada_beberapa) == 1:
				pilihan = self.konfigurasi.get_file_relative(mungkin_ada_beberapa[0])
				if is_edit:
					os.system(f'code "{pilihan}"')
				else:
					print_copy_file(pilihan)
			else:
				print('Please choose a closer match:')
				print_list_warna(mungkin_ada_beberapa)

			# ambil_1 = min(mungkin_ada_beberapa, key=len)
			# # self.konfigurasi.print_file(ambil_1, False)
			# filepath = self.konfigurasi.get_file_relative(ambil_1)
			# # entries = get_daftar(filepath)
			# # print_list_warna(entries)
			# # yesno(f'Cursing {filepath}? y[n]', lambda: self.activate_xcurse(filepath))
			# if isfile(filepath):
			# 	if is_edit:
			# 		os.system(f'code {filepath}')
			# 	else:
			# 		print_copy_file(filepath)

		elif code .startswith('o '):
			code = code.replace('o ', '', 1).strip()
			cari = [item for item in motd_list if code in item]
			if cari:
				import webbrowser
				webbrowser.get('firefox').open(cari[0])

		elif code == 'codegen':
			'''file manager utk generated'''
			editor = 'code'
			# folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_GENDIR"]
			if sys.platform == 'win32':
				folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_GENDIR_WIN32"]
			else:
				folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_GENDIR"]
			os.system(f"{editor} {folderpath}")

		elif code .startswith ('cdgen'):
			'''pindah ke dir generator utk cdgen dan utk cdgen* pindah ke default dir'''
			code = code.replace('cdgen', '', 1).strip()

			# /home/usef/danger/ulib/upy/ulibpy/xcurse/codes
			if sys.platform == 'win32':
				folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_GENDIR_WIN32"]
			else:
				folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_GENDIR"]

			if code == '*':
				# /home/usef/danger/ulib/upy/ulibpy/xcurse/codes
				if sys.platform == 'win32':
					folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_DIR_WIN32"]
				else:
					folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_WMC_DIR"]

			elif code == '_':
				# /home/usef/danger/ulib/schnell
				if sys.platform == 'win32':
					folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_BASEDIR_WIN32"]
				else:
					folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_BASEDIR"]

			elif code == '$':
				# pindah ke snippets dir, sementara blm ada versi win32
				folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_SNIPPETS"]
			elif code == '%':
				folderpath = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_BANTUAN_TPLS"]

			self.konfigurasi.chdir(folderpath)

		elif code .startswith('cddata'):
			# cddata = cdgen_/data
			# cddata* = cdgen_
			code = code.replace('cddata', '', 1).strip()
			# folderpath = joiner(getcwd(), 'data')
			if sys.platform == 'win32':
				env_basedir = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_BASEDIR_WIN32"]
			else:
				env_basedir = programming_data['j']['schnell']['app']["wmc"]["ULIBPY_BASEDIR"]

			folderpath = joiner(env_basedir, 'data')
			if code == '*':
				folderpath = env_basedir

			self.konfigurasi.chdir(folderpath)

		elif code .startswith('H'):
			'''
			help 
			help*
			'''
			code = code.replace('H', '', 1)
			filepath = joiner(ayah(__file__, 1), 'HELP')
			if not code:
				print_copy_file(filepath)
			elif code == '*':
				perintah(f'code {filepath}')
		
		else:
			cek_folder = joiner(self.konfigurasi.cwd(), code)
			if isdir(cek_folder):
				self.konfigurasi.chdir(cek_folder)
				self.debug(cek_folder + '\n')
			else:
				from schnell.app.dirutils import files_with_pattern
				files = files_with_pattern(self.konfigurasi.cwd(), code)
				print_list_warna(files)


	def repl(self):
		while not self.done:
			# di sini gak bisa ctrl+c dll
			hanya_direktori = self.konfigurasi.dirs()
			hanya_file = self.konfigurasi.files()
			# indah0(HELP_LINE, warna='green', newline=True)
			# baris_menu = '~o~ MENU ~o~' + f' {self.konfigurasi.cwd()}'
			# indah0(baris_menu, warna='bright_green', bold=True, newline=True)
			if programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_ALWAYS"]:
				# dir_w([item for item in hanya_direktori], warna='yellow')
				dir_w([item for item in hanya_direktori], warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOLDERCOLOR"])
				# dir_w([f"{n}. {i}" for n,i in enumerate(hanya_file,1)], warna='bright_blue', layar='white')
				dir_w([f"{n}. {i}" for n,i in enumerate(self.konfigurasi.files(),1)], warna=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_FOREGROUND"], layar=programming_data['j']['schnell']['app']["wmc"]["ULIBPY_DIR_W_BACKGROUND"])
			warna = 'bright_white' #if (not self.config['switch_window']) else 'bright_magenta'
			indah0(self.prompt, warna=warna)
			code = input('>> ')
			code = code.strip()

			try:
				if code != '' and code != 'x':
					self.fastcoder(code)
			except Exception as err:
				print(f'Eksepsi wmc/repl:65x: [{err}]')
				just_the_string = traceback.format_exc()
				print(just_the_string)


def main(basedir=None):
	"""
	from schnell.app.wmc import main as wmc_main
	wmc_main()
	"""
	# sys.path.append(os.getcwd())
	# indah3(f'debug={env_int("ULIBPY_FMUS_DEBUG")}', warna='yellow')
	print(motd)
	wmc = WmCurse(basedir)
	try:
		wmc.repl()
	except Exception as err:
		print('wmc.py err:', err)
		just_the_string = traceback.format_exc()
		print(just_the_string)


if __name__ == '__main__':
	# from dotenv import load_dotenv
	# load_dotenv(os.path.join(os.path.dirname(__file__), os.pardir, '.env'))
	# sys.path.append(os.environ.get('ULIBPY_BASEDIR', os.getcwd()))
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		main()
