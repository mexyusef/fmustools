import os, pathlib, re, shutil, sys, time
from .appconfig import programming_data
from .dirutils import (
	create_if_empty_dir,
	joiner,
	timestamp,
	isabsolute,
	isfile,
	isdir,
	ayah,
	walk_fullpath,
	getcwd,
	bongkar,
)
from .fileutils import (
	entrify_line,
	file_content,
	get_definition_by_key_permissive_start,
	get_definition_double_entry_aware,
	create_if_empty_file,
	view_lines_between,
)
from .mediautils import ImageHandler
from .printutils import (
	indah,
	indah0,
	indah4,
	print_list_warna,
)
from .redisutils import handle_publish_to_redis
from .utils import (
	double_backslash,
	input_until_end,
	perintah_shell, perintah,
	quad_backslash,
	trycopy, trypaste,
	# env_get, env_exist, env_int,
	env_ulibpy, env_replace_filepath,
	platform,
	run_in_server,
	LANGUAGES,
	wslify,
	wslpath2winpath,
	wslpath2winpath_condition,
)
from .stringutils import jsonify
try:
	from .showtext import main_process, code_editor, show_file_window
except Exception as err:
	pass

SCHNELL_DIR = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"]

konten_ngetik = """
aku adalah binatang jalang
yang masih lajang
serasa terbuang
melakukan hal terlarang
"""

class SpecialCommand:
	"""
	fitur:
	- bisa jalankan program python
	- bisa jalankan program java bahkan
	- bisa select window by title
	- bisa select window by click
	- bisa typing di window terpilih
	"""

	Context = {}
	last_processed_line = None

	def __init__(self, item):
		"""
		cmd_params = {
			'name'			: 'special_command',
			'type'			: 'special_command',
			'counter' 	: self.run_configuration['counter'],
			'command'		: nama_operasi, 
			'workdir'		: workdir, 
			'level'			: parentLevel
		}
		"""
		if programming_data["debug"]:
			from .printutils import print_tree
			indah4("SpecialCommand args:", warna='white')
			print_tree(item)

		self.source = item
		self.workdir = item.workdir
		self.command = item.command
		self.replacer = item.replacer
		self.input = {
			'title': None,
		}
		self.bahasa = None
		self.showtext_delimiter = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_DELIMITER"]
		self.image_delimiter = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_IMAGEDELIMITER"]
		# self.imagefile_start = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_IMAGEFILE_DELIMITER_START"]
		# self.imagefile_end = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_IMAGEFILE_DELIMITER_END"]
		self.compiler_delimiter = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_COMPILERDELIMITER"]
		# go<delim>isi code
		self.codelang_delimiter = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_LANG_CODE_DELIMITER"]

		if (not self.replacer) and (not 'dir' in SpecialCommand.Context):
			'''
			**wait=1 gak perlu masuk sini dan self.replacer = {}
			'''
			basedir = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_GENDIR"]
			if '__CURDIR__' not in self.replacer:
				pesan = f"[specialcmd] __CURDIR__ tidak ada dalam {jsonify(self.replacer)}"
				indah4(pesan, warna='red')
				from .printutils import get_tree
				nodesumber = get_tree(self.source)
				pesan = f"\n[specialcmd] source/item adlh {nodesumber}"
				indah4(pesan, warna='red')
				pesan2 = f"[specialcmd] workdir adlh {self.workdir}"
				indah4(pesan2, warna='magenta')
				indah4('='*40 + '\n\n', warna='red')
				self.replacer['__CURDIR__'] = self.workdir

			basedir = joiner(self.replacer['__CURDIR__'], programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_GENDIR_NAME"])
			create_if_empty_dir(basedir)
			workdirname = 'session'
			workdir = joiner(basedir, workdirname)
			create_if_empty_dir(workdir)
			SpecialCommand.Context['dir'] = workdir

	def file_ujian(self, baris_cari):
		"""
		spasi dll konversi ke _
		jk dia specify ada dot spt .py .txt dll maka diasumsikan "file language"
		"""
		filename = re.sub('[^0-9a-zA-Z_\-\.]+', '_', baris_cari)
		if '.' in filename:
			fullname = filename
		else:
			fullname = filename + "-" + timestamp() + '.txt'
		# return joiner(SpecialCommand.Context['dir'], fullname)
		return joiner(self.replacer['__CURDIR__'], fullname)

	@staticmethod
	def set_session_file(filename='session'):
		session_file = filename + "-" + timestamp() + '.mk'
		SpecialCommand.Context['file'] = joiner(SpecialCommand.Context['dir'], session_file)		

	@staticmethod
	def write_session_file(content, filepath=None, mode='append'):
		if not content.strip():
			print('[specialcmd] No content.')
			return

		if not filepath:
			filepath = SpecialCommand.Context['file']

		mode = 'a' if mode=='append' else 'w'
		with open(filepath, mode) as fd:
			fd.write(content)

	def random1(self, text=None):
		if text:
			ImageHandler().open_draw_show_image(text)
		else:
			ImageHandler().open_show_image()

	def random2(self, text=None):
		if text:
			ImageHandler().open_draw_show_image(text, url_random=2)
		else:
			ImageHandler().open_show_image(url_random=2)

	def show_random_image_if_prefixed(self, line):
		"""
		jadi dg &append kita bisa 
		#1 utk lihat gambar dst?
		"""
		if line .startswith ('#1'):
			line = line.replace('#1', '', 1).strip()
			if line:
				self.random1(line)
			else:
				self.random1()
			return False # jangan masukkan line ke 'result' -> append to file
		elif line .startswith ('#2'):
			line = line.replace('#2', '', 1).strip()
			if line:
				self.random2(line)
			else:
				self.random2()
			return False # jangan masukkan line ke 'result' -> append to file
		elif line == '#save':
			# line = line.replace('#save, '', 1).strip()
			ImageHandler().ask_save(SpecialCommand.Context['dir'], 'image-'+timestamp())

		return True

	def showtext_get_title_and_images(self, args, program_source_file):
		"""
		program_source_file adlh file berisi fm.us yg berisi &showtext=title###image1
		"""
		images = []
		title = None
		if programming_data['debug']:
			indah4(f"""[specialcmd] showtext_get_title_and_images
			args = {args}
			program_source_file = {program_source_file}
			""")
		# input('Press... ')

		#  args = =ULIBPY_ROOTDIR/data/karya/showtext.mk
		#  args = =ULIBPY_ROOTDIR/data/karya/showtext.mk=apa itu
		file_baris = [item.strip() for item in args.split(self.showtext_delimiter) [1:]] # skip '' hasil split showtext#file#baris
		if programming_data["debug"]:
			print("[specialcmd] titles and images:", file_baris)
		# trycopy(args)
		# baca file, ambil baris, copy ke clipboard
		# ini jadi gak bisa jk parent-child dan showtext ada di child
		# if len(file_baris) == 1 and isfile(self.replacer['__FILE__']):
		if len(file_baris) == 1 and isfile(program_source_file):
			# showtext=cari-baris-content [###image1###image2]
			entry_title = file_baris[0]						
			if self.image_delimiter in entry_title:
				pecah = entry_title.split(self.image_delimiter)
				entry_title = pecah[0]
				images = pecah[1:] # ini daftar filenames

			# program = get_definition_by_key_permissive_start(program_source_file, entry_title)
			program = get_definition_double_entry_aware(program_source_file, entry_title)			
			if program:
				trycopy(program)
				# test clipboard berhasil
				coba = trypaste()
				counter = 1
				while not coba and counter < 10:
					print(f'[specialcmd] {counter}. sleeping until done')
					time.sleep(.5)
					trycopy(program)
					coba = trypaste()
					counter += 1
			else:
				print('[specialcmd] NO PROGRAM!!!')

			SpecialCommand.last_processed_line = entry_title
			title = entry_title
		elif len(file_baris) == 2:
			# showtext=filepath=cari-baris-content
			filepath, entry_title = file_baris
			filepath = bongkar(filepath)
			program = get_definition_by_key_permissive_start(filepath, entry_title)
			trycopy(program)
			if programming_data["debug"]:
				indah4(f'[specialcmd] copying [{program[:40]}...]', warna='green')
			SpecialCommand.last_processed_line = entry_title
			title = entry_title
		
		return title, images

	def run(self):
		# print('aku menerima original:', self.source)
		# print('aku harus handle:', self.command)
		# print('aku sendiri berada di:', os.getcwd())
		# harusnya parsing self.command, tapi sementara cuma 1 jenis command saja

		if self.command == 'android':
			from schnell.app.special.android import AndroidTemplate
			android = AndroidTemplate(self.workdir)
			android.solve()

		elif self.command == 'append':
			if not 'file' in SpecialCommand.Context:
				SpecialCommand.set_session_file()

			content = input_until_end(line_callback=self.show_random_image_if_prefixed)
			content = entrify_line(content)
			SpecialCommand.write_session_file(content)

		elif self.command .startswith ('showtext') or self.command .startswith ('showfile'):
			'''
			ini butuh teknik tersendiri
			&showtext#pola file#pola baris
			atau 
			&showtext/pola file/pola baris
			kita bisa gunakan:
			SpecialCommand.Context['dir'] yg setara __CURDIR tentunya?
			nope, kita masukkan ke sini saja
			self.replacer = item.replacer
			'''
			images = []
			title = None
			# args = self.command.replace('showtext', '', 1).strip()
			args = self.command.removeprefix('showtext').strip()
			
			filepath = None
			show_file = True if self.command.startswith('showfile') else False
			if show_file:
				# args = self.command.replace('showfile', '', 1).strip()
				args = self.command.removeprefix('showfile').strip()

			if args:
				if self.showtext_delimiter in args:
					'''
					jika ada '=' di arg spt:
					showtext=file=baris
						=> len(file_baris) == 2
					showtext=baris
						=> len(file_baris) == 1
					butuh juga:
					showtext=baris content###baris image
					showtext=baris content###baris image1###baris image2
					di sini args adlh: =baris_cari###image_baris_cari
					kita pengen bisa masukkan __CURDIR__/otherfile, dst... (sementara baru bisa __CURDIR__)
					jadi bentuk awal bisa
					showtext=baris content###<<filename>>baris image1###<<filename>>baris image2
					'''
					if '__FILE__' in self.replacer:
						program_source_file = self.replacer['__FILE__']
					else:
						'''
						jk gak ada __FILE__ maka biasanya dari clipboard
						cek jk command='showtext=/home/usef/danger/ulib/schnell/creator/createdb/by-langs/repl.py.mk=lesson learned dari kerjaan'

						command : showtext=/home/usef/danger/ulib/schnell/creator/createdb/by-langs/repl.py.mk=lesson learned dari kerjaan
						args 		: =/home/usef/danger/ulib/schnell/creator/createdb/by-langs/repl.py.mk=lesson learned dari kerjaan
						'''
						mungkin_berisi_file = args.split(self.showtext_delimiter)[1:]
						program_source_file = mungkin_berisi_file[0].strip()
						if len(mungkin_berisi_file) == 2:
							'''
							0 = /home/usef/danger/ulib/schnell/creator/createdb/by-langs/repl.py.mk
							1 = lesson learned dari kerjaan
							'''
							harus_file = mungkin_berisi_file[0]
							if isfile(harus_file):
								indah0('command bernilai ' + self.command, warna='yellow', newline=True)
								indah0('args bernilai ' + args, warna='yellow', newline=True)
								indah0('harus_file bernilai ' + harus_file, warna='yellow', newline=True)
								# yesno = input(f'Masukkan "y" untuk set program_source_file ke [{harus_file}]: ')
								# if yesno == 'y':
								# 	program_source_file = harus_file
								program_source_file = harus_file
					if isfile(program_source_file):
						program_source_file = bongkar(program_source_file)
					if show_file:
						'''
						**showfile=filepath
						**showfile=filepath###image1###image2
						image1 dst hrs namafile yg di current dir ya?
						atau item.workdir dimana showfile diexec?

						self.showtext_delimiter = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_DELIMITER"]
							=
						self.image_delimiter = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_SHOWTEXT_IMAGEDELIMITER"]
							###
						'''
						file_baris = args.split(self.showtext_delimiter) [1:] 
						# skip '' hasil split showtext#file#baris
						filepath = file_baris[0]
						if len(file_baris) == 1 and isfile(program_source_file):
							entry_title = file_baris[0]
							if self.image_delimiter in entry_title:
								pecah = entry_title.split(self.image_delimiter)
								filepath = pecah[0]
								images = pecah[1:]
						title = f"{filepath} [{self.workdir}]"
					else:
						title, images = self.showtext_get_title_and_images(args, program_source_file)
						title = f"{title} [{self.workdir}]"
			
			if programming_data["debug"]:
				print(f"[specialcmd] Before invoke, filepath = [{filepath}], title = [{title}]")
			# TODO: jadikan threading sbg pilihan (default pengen ngeblock)
			func = show_file_window if show_file else main_process
			args = {
				'title': title,
			}
			if images:
				args.update({
					'images': images,
				})
			if show_file:
				args.update({
					'filepath': filepath,
				})
			# func(**args)
			from .threadutils import mulai
			mulai(func, kwargs=args)

		elif self.command .startswith ('ujian'):
			args = self.command.replace('ujian', '', 1).strip()
			jawaban = None
			if args:
				print(f'[specialcmd] ujian args [{args}]')
				# jk specify ujian|py|=cari
				if self.compiler_delimiter in args:
					before, self.bahasa, after = args.split(self.compiler_delimiter)
					args = before + after
				# jk ujian=...
				if self.showtext_delimiter in args:
					# jk berbentuk ujian=baris_cari
					# ini jangan jadi condition check pertama
					file_baris = args.split(self.showtext_delimiter) [1:]
					if len(file_baris) == 1 and isfile(self.replacer['__FILE__']):
						entry_title = file_baris[0]
						# ujian=baris_cari -> ini ada content
						# ujian=ngawur -> ini content kosong
						isi_awal = get_definition_by_key_permissive_start(self.replacer['__FILE__'], entry_title)
						if isi_awal:
							isi_awal += f"\n#{'*'*40}\n"
						else:
							# entry_title bisa berisi .py .go dst, berarti dia minta bahasa
							if '.' in entry_title:
								_, bahasa = entry_title.split('.')
								if bahasa:
									isi_awal = f'{bahasa}\n' + self.codelang_delimiter + '\n'
							else:
								isi_awal = '' # ini utk nulis bebas dari ujian=ngawur...
						jawaban = self.file_ujian(entry_title)
			else:
				# gunakan baris_cari dari command sblmnya 
				# yg menset last_processed_line (showtext)
				# tapi watchout: suka dari program yg berbeda masuk sini
				# UPDATE:
				# ini jadi ngawur jk sebuah mk hanya punya ujian, jadi last_processed_line diambil dari mk lain
				# yg gak ada hubungan 
				if SpecialCommand.last_processed_line:
					jawaban = self.file_ujian(SpecialCommand.last_processed_line)
					# biar bisa specify bahasa
					isi_awal = 'py\n' + self.codelang_delimiter + '\n'

				print('[specialcmd] ujian no args, peroleh jawaban:', jawaban)

			if jawaban:
				SpecialCommand.write_session_file(isi_awal, jawaban)
				print('[specialcmd] File ditulis ke', jawaban)
				code_editor(isi_awal, jawaban)
				# di sini jawaban file path ke hasil edit user
				# bisa panggil compiler etc
				# cek jk hasil ketikan user berisi bahasa<delim>content
				# maka akan override self.bahasa dari ujian|bahasa|=cari
				from .executor import ExecFile, FileExecutor
				latest_content = file_content(jawaban)
				if self.codelang_delimiter in latest_content:
					calon_bahasa, clean_content = latest_content.split(self.codelang_delimiter)
					calon_bahasa = calon_bahasa.strip()
					if calon_bahasa in LANGUAGES:
						trycopy(clean_content)
						FileExecutor(calon_bahasa).execute()
					elif self.bahasa in LANGUAGES:
						# ExecFile.exec(code)
						FileExecutor(self.bahasa).execFile(jawaban)
			else:
				print('[specialcmd] nuthing to process')

		elif self.command .startswith ('server'):
			args = self.command.replace('server', '', 1).strip()

			if args:
				file_baris = args.split(self.showtext_delimiter) [1:]
				# print('specialcmd server:', args, 'file_baris:', file_baris)	
				if len(file_baris) == 1:
					_perintah = file_baris[0]
					run_in_server(_perintah)
				else:
					print('[specialcmd] Format: **server=<perintah>')

		elif self.command.startswith('wnd_create'):
			'''
			**wnd_create=qterminal
			'''
			from schnell.app.medias import window_manager
			_, aplikasi = self.command.split('=', 1)
			window_manager.create_window(aplikasi)
			if programming_data["debug"]:
				indah4(f'[specialcmd] post wnd_create: {aplikasi}', warna='yellow')

		elif self.command.startswith('wnd_left'):
			'''
			**wnd_left=qterminal
			'''
			from schnell.app.medias import window_manager
			_, aplikasi = self.command.split('=', 1)
			window_manager.create_left(aplikasi)

		elif self.command.startswith('wnd_right'):
			'''
			**wnd_right=gedit
			'''
			from schnell.app.medias import window_manager
			_, aplikasi = self.command.split('=', 1)
			window_manager.create_right(aplikasi)

		elif self.command.startswith('wnd_sbs'):
			'''
			**wnd_sbs=qterminal,gedit
			'''
			from schnell.app.medias import window_manager
			_, apps = self.command.split('=', 1)
			if ',' in apps:
				app1,app2 = apps.split(',',1)
				window_manager.create_sidebyside(app1,app2)

		elif self.command.startswith('wnd_vert'):
			'''
			**wnd_vert=sakura,gedit
			'''
			from schnell.app.medias import window_manager
			_, apps = self.command.split('=', 1)
			if ',' in apps:
				app1,app2 = apps.split(',',1)
				window_manager.create_topbottom(app1,app2)

		elif self.command.startswith('wnd_focus'):
			'''
			**wnd_focus=judul_window_utk_focus
			'''
			from schnell.app.medias import window_manager
			_, judul = self.command.split('=', 1)
			window_manager.focus(judul)

		elif self.command.startswith('wnd_title'):
			'''
			**wnd_title=Untitled=judul baru
			**wnd_title=judul_window_utk_aktivasi
			'''
			from schnell.app.medias import window_manager
			_, judul = self.command.split('=', 1)
			if '=' in judul: # Untitled=judul baru
				lama, baru = judul.split('=', 1)
				window_manager.title(baru, lama)
			else: # judul baru
				window_manager.set_title_activewindow(judul)

		elif self.command.startswith('wait'):
			'''
			**wait=2
			'''
			_, detik = self.command.split('=', 1)
			if detik.isdigit():
				waktu = int(detik)
				time.sleep(waktu)

		elif self.command.startswith('elapsed'):
			'''
			'''
			from schnell.app.datetimeutils import epoch, epoch_diff, epoch2dtstr
			from schnell.app.treeutils import get_root
			root = get_root(self.source)
			current = epoch()
			elapsed = epoch_diff(root.epoch, current)
			print(f'[specialcmd] elapsed time {elapsed}s from {epoch2dtstr(root.epoch)} to {epoch2dtstr(current)}.')

		elif self.command.startswith('pause'):
			'''
			**pause
			**pause=isi pesan utk ditampilkan
			'''
			pesan = 'Press any key...'
			if '=' in self.command:
				_, pesan = self.command.split('=', 1)
				if pesan:
					'''
					**pause=TABisi pesan utk ditampilkanSPCSPCNL
					'''
					pesan = pesan.replace('SPC', ' ').replace('TAB', '\t').replace('NL', '\n')

			# input(pesan)
			from schnell.app.showtext import show_content_window
			judul='Menunggu proses'
			show_content_window(title=judul, content_text=pesan)
			time.sleep(1.0)

		elif self.command.startswith('wsltype'):
			'''
			**wsltype=kata2 langsung
			u -e "**wsltype=kata2 langsung"
			'''
			_, tulisan = self.command.split('=', 1)
			from schnell.app.medias import window_manager
			from schnell.app.medias import typewriter
			# from schnell.app.medias.wsltype import ngetik_dari_wsl
			window_manager.special_cmd = self
			typewriter.special_cmd = self
			# ngetik_dari_wsl(yang_diketik, command = 'cmd.exe', speed=2000):
			# ngetik_dari_wsl(tulisan, command = 'cmd.exe', speed=2000)
			# python_command = 'cmd.exe /c start cmd.exe /k "python C:/work/ulibs/schnell/app/medias/wsltype.py'
			python_command = f'cmd.exe /k "python {SCHNELL_DIR}/app/medias/wsltype.py'
			# perintah_shell(f'{python_command} \\\\\\\\wsl$\\\\Ubuntu-20.04\\\\home\\\\usef\\\\work\\\\ulibs\\\\schnell\\\\app\\\\transpiler\\\\frontend\\\\react\\\\setup.mk coba tulis"')
			tulisan = tulisan.replace(' ', '__SPACE')
			# python_command_lengkap = f'{python_command} \"{tulisan}\" notepad.exe"' # hwnd tdk ditemukan
			python_command_lengkap = f'{python_command} \"{tulisan}\""'
			print(f'[specialcmd] kita pengen ini: [{python_command_lengkap}]')
			perintah_shell(python_command_lengkap)

		elif self.command.startswith('wsl_ngetik'):
			'''
			**wsl_ngetik=filepath=baris-entry
			'''
			from schnell.app.medias import window_manager
			from schnell.app.medias import typewriter
			# agar bisa "elapsed", self kasih self.root
			window_manager.special_cmd = self
			typewriter.special_cmd = self
			# skip '=' pertama yg memisahkan wnd_ngetik=...konten...
			_, judul = self.command.split('=', 1)
			filepath, baris_cari = judul.split('=')
			# def ngetik_dari_wsl(filepath, baris_entry='index/fmus', command = 'cmd.exe', speed=2000):
			# from schnell.app.medias.ketik_windows import ngetik_dari_wsl
			# ngetik_dari_wsl(filepath, baris_cari, 'cmd.exe', speed=4000)
			# python app/medias/ketik_windows mkfilepath baris_entry
			# /home/usef/work/ulibs/schnell/app/transpiler/frontend/react/setup.mk

			# wslpath = wslify(filepath, manual=True, rewindows=True, no_double_back=False)
			# quad_wslpath = quad_backslash(wslpath)
			# double_wslpath = double_backslash(wslpath)

			# print(f"inilah yg kita cari: [{filepath}] => [{wslpath}], [{baris_cari}]")
			# print(f'here we go: [{quad_backslash(wslpath)}]')

			double_wslpath = wslpath2winpath(filepath)

			# python_command = 'cmd.exe /c start cmd.exe /k "python \\\\\\\\wsl$\\\\Ubuntu-20.04\\\\home\\\\usef\\\\work\\\\ulibs\\\\schnell\\\\app\\\\medias\\\\ketik_windows.py'			
			python_command = f'cmd.exe /c start cmd.exe /k "python {SCHNELL_DIR}/app/medias/ketik_windows.py'
			# perintah_shell(f'{python_command} \\\\\\\\wsl$\\\\Ubuntu-20.04\\\\home\\\\usef\\\\work\\\\ulibs\\\\schnell\\\\app\\\\transpiler\\\\frontend\\\\react\\\\setup.mk coba tulis"')
			python_command_lengkap = f'{python_command} {double_wslpath} {baris_cari}"'
			print(f'[specialcmd] kita pengen ini: [{python_command_lengkap}]')
			perintah_shell(python_command_lengkap)

		elif self.command.startswith('wnd_ngetik'):
			'''
			ngetik pd window berjudul (ada 3 =):
			**wnd_ngetik=judulwindow=filepath=bariscari
			**wnd_ngetik=judulwindow=#fast#filepath=bariscari
			**wnd_ngetik=*namaaplikasi=filepath=bariscari

			ngetik pd aktif window, bahaya suka masuk wmc (ada 2 =):
			**wnd_ngetik=judulwindow=filepath
			**wnd_ngetik=judulwindow=#fast#filepath
			**wnd_ngetik=*namaaplikasi=filepath
			'''
			from schnell.app.medias import window_manager
			from schnell.app.medias import typewriter
			
			# agar bisa "elapsed", self kasih self.root
			window_manager.special_cmd = self
			typewriter.special_cmd = self

			# skip '=' pertama yg memisahkan wnd_ngetik=...konten...
			_, judul = self.command.split('=', 1)
			if '=' in judul:
				'''
				jk ada = stlh skip '=' pertama
				maka ada 2 kemungkinan: jumlah '=' 2 utk judul=file=entry
				atau jumlah '=' 1 utk judul=file

				wnd_ngetik=judul=filepath=baris-entry
				wnd_ngetik=judul=filepath
				command='wnd_ngetik=monyong=ULIBPY_SNIPPETS/lanjut
				                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
														judul
				'''
				jumlah_samadengan = judul.count('=')
				if jumlah_samadengan == 2: 
					# wnd_ngetik=judul_window=filepath=baris-entry
					judul, filepath, baris_cari = judul.split('=')
					if programming_data["debug"]:
						indah4(f'[specialcmd] judul: {judul}, filepath: {filepath}, baris: {baris_cari}', warna='yellow')
					byWindowID = False # wnd_ngetik=*qterminal=filepath
					isFast = False
					# cek #fast#
					if filepath.startswith('#fast#'):
						filepath = filepath.removeprefix('#fast#')
						isFast = True
					if judul.startswith('*'):
						'''
						kita aktifkan window by id
						wnd_ngetik=*sakura=...
						wnd_ngetik=*gedit=...
						'''
						judul = judul.removeprefix('*')
						byWindowID = True
					filepath = env_replace_filepath(filepath)
					if programming_data["debug"]:
						indah4(f'[specialcmd] sblm wm focus, filepath: {filepath}', warna='yellow')
					if isfile(filepath):
						if byWindowID:
							window_manager.focus_by_wid(judul)
						else:
							window_manager.focus(judul)
						program = get_definition_double_entry_aware(filepath, baris_cari)
						typewriter.text_with_newline(program, pause=0 if isFast else None)
					else:
						print('[specialcmd] ngetik=judul=filepath=entry --> file not found:', filepath)

				elif jumlah_samadengan == 1:
					# wnd_ngetik=judul_window=filepath
					judul, filepath = judul.split('=')
					byWindowID = False # wnd_ngetik=*qterminal=filepath
					isFast = False
					# cek #fast#
					if filepath.startswith('#fast#'):
						filepath = filepath.removeprefix('#fast#')
						isFast = True
					if judul.startswith('*'):
						judul = judul.removeprefix('*')
						byWindowID = True

					filepath = env_replace_filepath(filepath)

					if isfile(filepath):
						if byWindowID:
							window_manager.focus_by_wid(judul)
						else:
							window_manager.focus(judul)
						content = file_content(filepath)
						typewriter.text_with_newline(content, pause=0 if isFast else None)
					else:
						print('[specialcmd] ngetik=judul=filepath --> file not found:', filepath)

			else:
				'''
				wnd_ngetik=judulwindow
				wnd_ngetik=*judulwindow
				'''
				if judul.startswith('*'):
					judul = judul.removeprefix('*')
					window_manager.focus_by_wid(judul)
				else:
					window_manager.focus(judul)
				isi_clipboard = trypaste()
				if isi_clipboard:
					typewriter.text_with_newline(isi_clipboard)
				else:
					typewriter.text_with_newline(konten_ngetik)

		elif self.command.startswith('picsum'):
			"""
			**picsum
			**picsum=tulisan
			**picsum=atas||bawah
			"""
			from schnell.app.special.unsplash import handle_unsplash, handle_picsum
			handle_picsum(self.command)
			# from schnell.app.mediautils import random_picsum
			# if '=' in self.command:
			# 	picsum, text = self.command.split('=')
			# 	random_picsum(text.strip())
			# else:
			# 	random_picsum()

		elif self.command.startswith('unsplash'):
			"""
			**unsplash
			**unsplash=tulisan
			**unsplash=atas||bawah
			"""
			from schnell.app.special.unsplash import handle_unsplash, handle_picsum
			handle_unsplash(self.command)
			# from schnell.app.mediautils import random_unsplash
			# if '=' in self.command:
			# 	picsum, text = self.command.split('=')
			# 	random_unsplash(text.strip())
			# else:
			# 	random_unsplash()

		elif self.command.startswith('favico'):
			"""
			originalfile hrs pada curdir, bisa dari filename.png,f(img=art1) atau filename.png,f(img=ava1)
			**favico=originalfile

			filename.png,f(img=ava1)
			**favico=filename.png
			u -e ".,d\n\tfilename.png,f(img=ava1)\n\t**favico=filename.png"
			.,d
        filename.png,f(img=ava1)
        **favico=filename.png
			"""
			from schnell.app.mediautils import faviconGenerator, make_favicon
			# code = self.command.removeprefix('favico')
			_, text = self.command.split('=', 1)
			if not '=' in text:
				originalfile = text
				# output1 = 'pillow'
				# output2 = 'pilkit'
				faviconGenerator(originalfile, '.')
				make_favicon(originalfile, '.')

		elif self.command.startswith('favgen'):
			"""
			u -e ".,d\n\tfilename1.png,f(img=ava1)\n\t**favgen=filename1.png"
			.,d
				filename1.png,f(img=ava1)
        **favgen=filename1.png
			"""
			from schnell.app.mediautils import faviconGenerator, make_favicon
			_, text = self.command.split('=', 1)
			if not '=' in text:
				originalfile = text
				faviconGenerator(originalfile, '.')

		elif self.command.startswith('favmake'):
			"""
			u -e ".,d\n\tfilename2.png,f(img=ava1)\n\t**favmake=filename2.png"
			.,d
				filename2.png,f(img=ava1)
        **favmake=filename2.png
			"""
			from schnell.app.mediautils import faviconGenerator, make_favicon
			_, text = self.command.split('=', 1)
			if not '=' in text:
				originalfile = text
				make_favicon(originalfile, '.')

		elif self.command.startswith('notif'):
			"""
			u -e "**notif=judul=pesan"
			**notif=judul=pesan
			**notif2=judul=pesan
			"""
			kode,judul,pesan = self.command.split('=', 2)
			if judul and pesan:
				if kode == 'notif2':
					from schnell.app.notifutils import pynotif
					pynotif(judul, pesan)
				else:
					from schnell.app.notifutils import notifpy
					notifpy(judul, pesan)

		elif self.command.startswith('sccap'):
			"""
			u -e "**screc=filepath"
			**sccap=filepath
			"""
			from schnell.app.videoutils import capture_screen
			import pyautogui
			screc = self.command.split('=')
			pyautogui.hotkey('winleft', 'd')
			if len(screc) == 2:
				# python C:\work\ulibs\schnell\wmcer.py -e "**screc=rekam.mp4"
				kode, filepath = screc
				input(f'{screc}: Press any key when ready... ')
				capture_screen(filepath)

		elif self.command.startswith('screc'):
			"""
			u -e "**screc=filepath"
			**screc=filepath
			**screc=filepath=long
			**screc=filepath=long=br
			"""
			from schnell.app.videoutils import record_screen
			import pyautogui
			# record_screen(filepath='recording.mp4', long_seconds=60, frame_rate=30, bit_rate=2, hardware=True)
			screc = self.command.split('=')
			pyautogui.hotkey('winleft', 'd')
			if len(screc) == 4:
				# python C:\work\ulibs\schnell\wmcer.py -e "**screc=rekam.mp4=10=3"
				kode, filepath, howlong, bitrate = screc
				input(f'{screc}: Press any key when ready... ')
				record_screen(filepath, int(howlong), int(bitrate))
			elif len(screc) == 3:
				# python C:\work\ulibs\schnell\wmcer.py -e "**screc=rekam.mp4=10"
				kode, filepath, howlong = screc
				input(f'{screc}: Press any key when ready... ')
				record_screen(filepath, int(howlong))
			elif len(screc) == 2:
				# python C:\work\ulibs\schnell\wmcer.py -e "**screc=rekam.mp4"
				kode, filepath = screc
				input(f'{screc}: Press any key when ready... ')
				record_screen(filepath)

		elif self.command.startswith('W='):
			"""
			u -e "**W=code"
			**W=code
			code:
			load
			123
			/cari
			/*cari-case-sensitive
			/10/cari				10 before, 10 after
			/10*/cari
			/3,0/cari				3 before, 0 after
			#define-word
			*edit-word
			$1			get one randomly
			$1*		get one randomly + definition
			neo
			vert, tion
			"""
			from db.writer_service import process_writer
			request = self.command.removeprefix('W=')
			process_writer(request, print_result=True)

		elif self.command.startswith('*'):
			"""
			***fs/C^{@User=#5}username,s^
			***mrcli/B
			***mrcli/B^kode^
			juga belum manfaatkan frontend lang yg adlh decl lang...
			"""
			request = self.command.removeprefix('*')
			from schnell.app.transpiler.frontend.fullstack import process_language
			process_language(request)

		elif self.command.startswith('@'):
			"""
			wm -e'**@pris/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s'
			"""
			request = self.command.removeprefix('@')
			from schnell.app.transpiler.mycsv.process import process_language
			process_language(request)

		elif self.command.startswith('/'):
			"""
			**/search-repl
			"""
			request = self.command.removeprefix('/')
			from db import redis_repl
			redis_repl(request, None)

		elif self.command.startswith('l '):
			"""
			u -e'**l o goog|ufc events'
			"""
			request = self.command.removeprefix('l ')
			from schnell.app.utils import Launcher
			Launcher.launch(request)

		elif self.command.startswith('>'):
			"""
			**>...
			"""
			request = self.command.removeprefix('>')
			from .special import genfile
			genfile(request)

		elif self.command.startswith('%'):
			"""
			%filename
			%filename|baris pertama|baris akhir
			view_lines_between(filepath, baris_cari_start, baris_cari_end)
			walk_fullpath(basedir, skip_ends=None, filtered_ends=None)

			u -e'**%metafile|Company|Product'
			u -e'**%metafile|Company'
			u -e'**%metafile'

			tambah $ utk SCH sbg basedir...jadi bs panggil dari direktori manapun
			"""
			print(f'[specialcmd] %: ==>{self.command}<==')
			request = self.command.removeprefix('%')
			pecah = [item.strip() for item in request.split('|')]

			if pecah and isabsolute(pecah[0]) and isfile(pecah[0]):
				print(f'[specialcmd] %: filepath ==>{pecah[0]}<==')
				if len(pecah) in [2,3]:
					content = view_lines_between(*pecah)
				else:
					print(f'[specialcmd] %: tidak ditemukan "start baris" ==>{pecah}<==')
					return
				if content:
					content = ''.join(content)
					# indah4('-'*40, warna='red', layar='white')
					# # indah4(''.join(content), warna='green', layar='black')
					# indah4(content, warna='green', layar='black')

					handle_publish_to_redis(content)
				return

			basedir = getcwd()
			print(f'[specialcmd] %: basedir {basedir} request {request}')
			if request.startswith('$'):
				request = request.removeprefix('$')
				basedir = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"]

			print(f'[specialcmd] %: basedir {basedir} request {request}')
			
			daftarfile = walk_fullpath(basedir)
			
			relativefiles = [item.removeprefix(basedir + '/') for item in daftarfile]
			# cari_relative = [item for item in relativefiles if filepattern in item]
			# cari_absolute = [item for item in daftarfile if filepattern in item]
			edit_file = False

			print(f'[specialcmd] %: len(pecah)={len(pecah)}, pecah={pecah}.')

			if len(pecah) == 3:
				filepattern, start, end = pecah
				if filepattern.startswith('*'):
					filepattern = filepattern.removeprefix('*')
					edit_file = True

				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 1[pat = {filepattern}] => {cari_absolute}, start [{start}], end [{end}].', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = view_lines_between(filepath, start, end)
					if content:
						content = ''.join(content)
						indah4('-'*40, warna='red', layar='white')
						# indah4(''.join(content), warna='green', layar='black')
						indah4(content, warna='green', layar='black')

						handle_publish_to_redis(content)

						# jk specify file+baris awal+baris akhir, view atau view+edit
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')

			elif len(pecah) == 2:
				filepattern, start = pecah
				if filepattern.startswith('*'):
					filepattern = filepattern.removeprefix('*')
					edit_file = True

				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 2[pat = {filepattern}] => {cari_absolute}', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = view_lines_between(filepath, start)
					if content:
						# if isinstance(content, list):
						# 	content = ''.join(content)
						content = ''.join(content)
						indah4('-'*40, warna='red', layar='white')
						indah4(content, warna='green', layar='black')

						handle_publish_to_redis(content)

						# jk specify file+baris awal, view atau view+edit
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')

			elif len(pecah) == 1 and pecah[0]:
				filepattern = pecah[0]
				if filepattern.startswith('*'):
					filepattern = filepattern.removeprefix('*')
					edit_file = True

				# cari_relative = [item for item in relativefiles if filepattern in item]
				cari_relative = [item for item in relativefiles if filepattern in item and '__pycache__' not in item]

				if cari_relative:
					indah4(f'[specialcmd] 3[pat = {filepattern}] => {cari_relative}', warna='green', layar='black')
					filepath_relative = cari_relative[0]
					
					# cari_absolute = [item for item in daftarfile if filepattern in item]
					cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

					if cari_absolute and len(cari_absolute)==1:
						# indah4(f'found #2 [{filepattern}] => {cari_absolute}', warna='green', layar='black')
						filepath = cari_absolute[0]
						content = file_content(filepath)
						if content:
							# jk specify hanya file, maka either: view or edit
							if edit_file:
								filepath = wslpath2winpath_condition(filepath)
								indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
								# perintah(f'code {filepath_relative}') # jk absolute dari wsl gak bisa dibuka code
								perintah(f'code {filepath}')
							else:
								indah4('-'*40, warna='red', layar='white')
								indah4(content, warna='green', layar='black')
								handle_publish_to_redis(content)

				else:
					indah4(f'[specialcmd] no [{filepattern}]', warna='white', layar='red')

			else:
				print_list_warna(daftarfile)

		elif self.command.startswith('term'):
			if self.command == 'term':
				perintah('cmd.exe /c start wt.exe -d .')
			elif self.command == 'term1':
				perintah('cmd.exe /c start cmd.exe /k')
			elif self.command.startswith('term '):
				args = self.command.removeprefix('term ').strip()
				fullcmd = f'cmd.exe /c start cmd.exe /k "cd {args} && dir"'
				indah4(f'''
				term 
				args = {args}
				cmd = {fullcmd}
				''', warna='white')
				perintah(fullcmd)

		elif self.command.startswith('VF'):
			daftarfile = walk_fullpath(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"])
			edit_file = False
			if self.command.endswith('*'):
				self.command = self.command.removesuffix('*')
				edit_file = True
			if self.command == 'VFS':
				start = 'statement_config_item'
				end = 'backend_statement'
				filepattern = 'fullstack.py'

				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 4[pat = {filepattern}] => {cari_absolute}, start [{start}], end [{end}].', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = view_lines_between(filepath, start, end)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')

			elif self.command .startswith('VFG'):
				from schnell.app.special import view_file
				filepath = 'app/grammar.py'
				if self.command == 'VFGi':
					view_file(daftarfile, filepath, 'instruction start', 'instruction end')
				if self.command == 'VFGf':
					view_file(daftarfile, filepath, 'file specifier start', 'file specifier end')
				if self.command == 'VFGd':
					view_file(daftarfile, filepath, 'dir specifier start', 'dir specifier end')
				if self.command == 'VFGo':
					view_file(daftarfile, filepath, 'file operation start', 'file operation end')
				if self.command == 'VFGb':
					view_file(daftarfile, filepath, 'branching start', 'branching end')

			elif self.command == 'VFC':
				start = 'csv_item'
				end = 'csv_code'
				filepattern = 'csv_operation.py'
				
				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 5[pat = {filepattern}] => {cari_absolute}, start [{start}], end [{end}].', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = view_lines_between(filepath, start, end)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')
			elif self.command == 'VFCG':
				start = 'tipe kolom start'
				end = 'tipe kolom end'
				filepattern = 'ucsv/grammar/grammar.py'
				
				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 6[pat = {filepattern}] => {cari_absolute}, start [{start}], end [{end}].', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = view_lines_between(filepath, start, end)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')
			elif self.command == 'VFCG2':
				start = 'constraint start'
				end = 'constraint end'
				filepattern = 'ucsv/grammar/grammar.py'
				
				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 7[pat = {filepattern}] => {cari_absolute}, start [{start}], end [{end}].', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = view_lines_between(filepath, start, end)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')
			elif self.command == 'VFCGS':
				filepattern = 'ucsv/grammar/subclass_string.py'
				
				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 8[pat = {filepattern}] => {cari_absolute}.', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = file_content(filepath)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')
			elif self.command == 'VFCGN':
				filepattern = 'ucsv/grammar/subclass_number.py'
				
				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 9[pat = {filepattern}] => {cari_absolute}.', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = file_content(filepath)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')
			elif self.command == 'VFCGD':
				filepattern = 'ucsv/grammar/subclass_date.py'
				
				# cari_absolute = [item for item in daftarfile if filepattern in item]
				cari_absolute = [item for item in daftarfile if filepattern in item and '__pycache__' not in item]

				if cari_absolute and len(cari_absolute)==1:
					indah4(f'[specialcmd] 10[pat = {filepattern}] => {cari_absolute}.', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = file_content(filepath)
					if content:
						indah4('-'*40, warna='red', layar='white')
						indah4(''.join(content), warna='green', layar='black')
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							indah4(f'[specialcmd] editing {filepath}', warna='yellow', layar='black')
							perintah(f'code {filepath}')

		elif self.command.startswith('lalang'):
			"""
			wm -e**lalang
			wm -e**lalang*
			"""
			#lalangdir = env_get('ULIBPY_LALANG_WSL' if platform() == 'wsl' else 'ULIBPY_LALANG_WIN32')
			lalangdir = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_LALANG_WIN32"]
			print('[specialcmd] lalangdir:', lalangdir)
			sys.path.extend([
				lalangdir,
				ayah(lalangdir,1) # agar bisa from lalang.*
				])
			from schnell.app.transpiler.lalang import myrepl
			# from schnell.app.transpiler.main import myrepl
			if self.command == 'lalang':
				myrepl()
			elif self.command == 'lalang*':
				# if platform() == 'wsl':
				# 	lalangdir = wslpath2winpath(lalangdir)
				lalangdir = wslpath2winpath_condition(lalangdir)
				perintah(f'code {lalangdir}')

		elif self.command.startswith('decl'):
			"""
			wm -e**decl
			ini adlh keluarga 4 bahasa BCDF: decl, css, flu, be bersama lalang jadi 5: BCDFL
			"""
			code = self.command.removeprefix('decl')
			if code == '*':
				dirpath = joiner(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"], 'app/transpiler/frontend')
				targetdirpath = wslpath2winpath_condition(dirpath)
				perintah(f'code {targetdirpath}')
			else:
				from schnell.app.transpiler.frontend.main import myrepl
				myrepl()

		elif self.command.startswith('css'):
			"""
			wm -e**css
			"""
			code = self.command.removeprefix('css')
			if code == '*':
				dirpath = joiner(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"], 'app/transpiler/css')
				targetdirpath = wslpath2winpath_condition(dirpath)
				perintah(f'code {targetdirpath}')
			else:
				from schnell.app.transpiler.css.main import myrepl
				myrepl()

		elif self.command.startswith('be'):
			"""
			wm -e**be
			"""
			code = self.command.removeprefix('be')
			if code == '*':
				dirpath = joiner(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"], 'app/transpiler/backend')
				targetdirpath = wslpath2winpath_condition(dirpath)
				perintah(f'code {targetdirpath}')
			else:
				from schnell.app.transpiler.backend.main import myrepl
				myrepl()

		elif self.command.startswith('flu'):
			"""
			wm -e**flu
			"""
			code = self.command.removeprefix('flu')
			if code == '*':
				dirpath = joiner(programming_data['j']['schnell']['app']["configuration"]["ULIBPY_BASEDIR"], 'langs/flutter')
				targetdirpath = wslpath2winpath_condition(dirpath)
				perintah(f'code {targetdirpath}')
			else:
				from schnell.langs.flutter.main import myrepl
				myrepl()

		elif self.command.startswith('E'):
			"""
			wm -e**Edbg=0/1
			"""
			# indah4(f'[specialcmd] calling {self.command}')
			from .special.envplay import envplay
			envplay(self.command.removeprefix('E'))

