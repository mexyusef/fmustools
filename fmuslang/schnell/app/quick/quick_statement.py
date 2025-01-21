from anytree import RenderTree
from schnell.app.redisutils import handle_publish_to_redis
from schnell.app.printutils import print_json, print_list_warna, indah4
from schnell.app.treeutils import (
	data,
	token,
	child1,
	child2,
	child3,
	child4,
	child,
	chdata,
	chtoken,
	anak,
	ispohon, istoken,
	beranak,
	sebanyak,
	jumlahanak,
)
from schnell.app.dirutils import (
	create_if_empty_dir,
	joiner,
	timestamp,
	isfile,
	isdir,
	isabsolute,
	ayah,
	walk_fullpath,
	getcwd,
)
from schnell.app.utils import (
	import_module, 
	env_get,
	env_int,
	perintah_shell, perintah,
	wslpath2winpath_condition,
)
from schnell.app.fileutils import file_content, view_lines_between
from schnell.langs.ucsv import processor as ucsv_processor
from .common import program_config


backend_config = {}


def peek_file(program):
	"""
	program = %lokasi|start|end
	TODO:
	ada versi publish ke yellow note
	skrg hanya berguna utk /ketik)u -e "/%........." dan harus gunakan __PP utk |
		harus bisa bikin versi ctrl+k juga
	%
	%$ utk lihat di schnelldir
	%$* utk di atas + edit file
	"""
	if program.startswith('%'):
		request = program.removeprefix('%')
		basedir = getcwd()
		# print('basedir:', basedir, 'request:', request)
		if request.startswith('$'):
			request = request.removeprefix('$')
			# basedir = env_get('ULIBPY_BASEDIR')
			from constants import schnelldir
			basedir = schnelldir

		if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
			print('[quick_statement:peek_file] basedir:', basedir, 'request:', request)

		pecah = [item.strip() for item in request.split('|')]
		if isabsolute(pecah[0]) and isfile(pecah[0]):
			# jk diberikan absolute file, maka daftarfile cuma 1
			daftarfile = [pecah[0]]
		else:
			daftarfile = walk_fullpath(basedir)
		relativefiles = [item.removeprefix(basedir + '/') for item in daftarfile]
		# cari_relative = [item for item in relativefiles if filepattern in item]
		# cari_absolute = [item for item in daftarfile if filepattern in item]
		edit_file = False

		# indah4(f'''[app.quick.quick_statement]
		# pecah = {pecah}
		# len(pecah) = {len(pecah)}
		# relativefiles = {relativefiles[:10]}
		# ''', warna='green')

		if len(pecah) == 3:
			filepattern, start, end = pecah
			if filepattern.startswith('*'):
				filepattern = filepattern.removeprefix('*')
				edit_file = True
			cari_absolute = [item for item in daftarfile if filepattern in item]
			if cari_absolute and len(cari_absolute)==1:
				if env_int('ULIBPY_FMUS_DEBUG')>1:
					indah4(f'[quick_statement:peek_file] 1[pat = {filepattern}] => {cari_absolute}, start [{start}], end [{end}].', warna='green', layar='black')
				filepath = cari_absolute[0]
				content = view_lines_between(filepath, start, end)
				if content:
					indah4('-'*40, warna='red', layar='white')
					indah4(''.join(content), warna='green', layar='black')
					# jk specify file+baris awal+baris akhir, view atau view+edit
					if edit_file:
						filepath = wslpath2winpath_condition(filepath)
						if env_int('ULIBPY_FMUS_DEBUG')>1:
							indah4(f'[quick_statement:peek_file] editing {filepath}', warna='yellow', layar='black')
						perintah(f'vscode {filepath}')

		elif len(pecah) == 2:
			filepattern, start = pecah
			if filepattern.startswith('*'):
				filepattern = filepattern.removeprefix('*')
				edit_file = True
			cari_absolute = [item for item in daftarfile if filepattern in item]
			if cari_absolute and len(cari_absolute)==1:
				if env_int('ULIBPY_FMUS_DEBUG')>1:
					indah4(f'[quick_statement:peek_file] 2[pat = {filepattern}] => {cari_absolute}', warna='green', layar='black')
				filepath = cari_absolute[0]
				content = view_lines_between(filepath, start)
				if content:
					indah4('-'*40, warna='red', layar='white')
					indah4(''.join(content), warna='green', layar='black')
					# jk specify file+baris awal, view atau view+edit
					if edit_file:
						filepath = wslpath2winpath_condition(filepath)
						if env_int('ULIBPY_FMUS_DEBUG')>1:
							indah4(f'[quick_statement:peek_file] editing {filepath}', warna='yellow', layar='black')
						perintah(f'vscode {filepath}')

		elif len(pecah) == 1 and pecah[0]:
			filepattern = pecah[0]
			if filepattern.startswith('*'):
				filepattern = filepattern.removeprefix('*')
				edit_file = True

			cari_relative = [item for item in relativefiles if filepattern in item]

			# indah4(f'''[app.quick.quick_statement]
			# cari_relative = {cari_relative}
			# ''', warna='yellow')

			if cari_relative:

				if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
					indah4(f'[quick_statement:peek_file] 3[{filepattern}] => {cari_relative}', warna='green', layar='black')

				filepath_relative = cari_relative[0]

				cari_absolute = [item for item in daftarfile if filepattern in item]

				# indah4(f'''[app.quick.quick_statement]
				# cari_absolute = {cari_absolute}
				# ''', warna='red')

				if cari_absolute and len(cari_absolute)==1:
					# indah4(f'found #2 [{filepattern}] => {cari_absolute}', warna='green', layar='black')
					filepath = cari_absolute[0]
					content = file_content(filepath)
					if content:
						# jk specify hanya file, maka either: view or edit
						if edit_file:
							filepath = wslpath2winpath_condition(filepath)
							if env_int('ULIBPY_FMUS_DEBUG')>1:
								indah4(f'[quick_statement:peek_file] editing {filepath}', warna='yellow', layar='black')
							# perintah(f'vscode {filepath_relative}') # jk absolute dari wsl gak bisa dibuka code
							perintah(f'vscode {filepath}')
						else:
							indah4('-'*40, warna='red', layar='white')
							indah4(content, warna='green', layar='black')
				elif len(cari_absolute)>1:
					print_list_warna(cari_absolute)

			else:
				indah4(f'[quick_statement:peek_file] no [{filepattern}]', warna='white', layar='red')

		else:
			print_list_warna(daftarfile)


def quick_statement(tree):
	# print('[quick_statement] data(tree):', data(tree))
	# print('[quick_statement] program_config:', program_config)

	# dummy_argument = tree
	# if program_config['config']['be'] in generator_utils.keys():
	# 	print(f'lihat struktur tree hrs berisi csv program:')
	# 	print('jenis adlh:', type(tree))
	# 	print('jk dia adlh token:', tree)
	# 	if data(tree) == 'quick_statement':
	# 		if chdata(tree) == 'program_backend':
	program = chtoken(tree)
	if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
		print('\n\n[quick_statement] program:', program)

	if program:
		if len(program)==1:
			'''
			u -e/H/1 -> 1 adlh dummy csvcode, len(program)==1
			'''
			if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
				print('[quick_statement] dummy ucsv program')
			RootNode = tree

		else:
			indah4(f'ucsv for: {program}', warna='cyan')			
			RootNode = ucsv_processor(program, print)

		generator_module = import_module(program_config['modulename'], program_config['generator'])
		generator = generator_module.Coordinator(RootNode)
		generator.generate()

		if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
			print('[quick_statement] program_config:', program_config)

	backend_config.update({
		'filepath': generator.output(),
		'baris_entry': 'index/fmus',
	})
	return backend_config
