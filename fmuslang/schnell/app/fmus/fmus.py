import ast, copy, shutil, sys
import json, os, re
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.search import find, findall

# original local imports
# from schnell.app.grammar import (
# 	base_grammar,
# 	bahasa,
# 	filedir_bahasa,
# )
# local imports
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import (
	abs_dir,
	ayah,
	create_dir,
	# find_patterns,
	here,
	isdir, isfile,
	joiner,
	normy,
	# does_exist,
	tempdir, file_under_tempdir,
	# exists_in_dir,
	get_cwd,
)
from schnell.app.fileutils import (
	write_file,
)
from schnell.app.printutils import (
	Debug,
	indah, indah0, indah4,
)
from schnell.app.utils import (
	trycopy,
	trypaste,
	yesno,
	env_get,
	env_set,
	env_exist,
	env_int,
)
from schnell.app.autoutils import confirm as autogui_confirm
from schnell.app.netutils import CURRENT_IP_ETH0
# from schnell.app.communication import start_client
# from schnell.app.configuration import Configuration as Konfigurasi
# from schnell.app.punctuation import Punctuation
from .common import Common
from .processor import Processor
from .generator import Generator


class Fmus:


	def load_and_process(self, filepath):
		if isfile(filepath):
			with open(filepath, 'r') as fd:
				program = fd.read().strip() + "\n"
				self.process(program)


	def pre_process(self, content):
		"""
		gak bisa deh
		soalnya: content clipboard harus pure fmus
		gak bisa pake --% dan --# di dalamnya
		"""
		result = content
		if '__FILE__' in content:
			temp_file = file_under_tempdir()
			newcontent = content.replace('__FILE__', temp_file) # .replace('__FILE', temp_file)
			write_file(temp_file, newcontent)
			result = newcontent

		return result


	def clipboard_load_and_process(self, replacer_untuk_file=None):
		content = trypaste()
		if content:
			if '__FILE__' in content:
				if replacer_untuk_file and isfile(replacer_untuk_file):
					self.set_file_dir_template(replacer_untuk_file)
				else:
					set_mk_file = input('__FILE__ dalam clipboard, mau set .mk file? ')
					if set_mk_file == 'y':
						basedir = input('Masukkan basedir biar cepat: ')
						if isdir(basedir):
							from schnell.app.generator import Generator as FileChooser
							filepath = FileChooser.openfile(basedir)
							# input('press any key => kita terima: ' + filepath + ' ')
							if isfile(filepath):
								self.set_file_dir_template(filepath)

			indah0(f'Execute: \n[{content}]\n? y[n]', warna='magenta', bold=True)
			yesno = input(' ')
			if yesno == 'y' or yesno == 'yes' or yesno == 'Y':
				# content hrs berakhir dg newline agar parser melihat ada DEDENT
				if not content.endswith('\n'):
					content += '\n'

				# harus ada preprocess, jk ada __FILE__ atau __FILE di content
				# maka buat temp file dulu.
				# self.process(self.pre_process(content))
				self.process(content)


	def initial_projectdir(self):
		# self.run_configuration['projectdir'] = normy(joiner(self.run_configuration['projectbase'], self.run_configuration['projectname']))
		self.run_configuration['projectdir'] = self.get_cwd_pwd()


	def __init__(self, debug=True, file_template=None):
		# autogui_confirm('fmus step 1')
		if debug:
			debug = env_int('ULIBPY_FMUS_DEBUG')
		heredir = normy(here(__file__))
		compete = ayah(heredir, 1)
		programsdir = joiner(compete, 'programs')

		self.run_configuration = {
			'debug': debug,
			'filemanager': heredir,
			'cwd': heredir,
			'compete': compete,
			# 'programsdir': programsdir,
			'templatesdir': joiner(heredir, 'templates'), # utk copy relative
			'projectname': 'sample',
			# 'projectbase': '/tmp',
		}

		self.run_configuration['replacer'] = {
			# '__TEMPLATES': joiner(programsdir, 'templates'),
			# '__PROJECTS': joiner(compete, 'projects'),
			# '__HERE': programsdir,
			# '__PROGRAMS': programsdir,
			# '__DAILY': joiner(programsdir, 'daily'),
			# '__INTERNET': joiner(programsdir, 'internet'),
			# '__ISO': joiner(programsdir, 'isomorphic'),
			# '__TOPCODER': joiner(programsdir, 'topcoder'),
			# '__COMPETE': compete,
			# '__FM': heredir,
			# '__FMPROGS': joiner(heredir, 'programs'),
		}

		self.initial_projectdir()

		self.run_configuration['original_projectdir'] = self.run_configuration['projectdir']	

		self.stdout = None
		self.stderr = None

		# lihat dulu config
		# self.debug(json.dumps(self.run_configuration, indent=4))
		# input('...press any key...')

		if file_template:
			'''utk replace __FILE__ pada program string'''
			self.set_file_template(file_template)

		self.debug = Debug(env_int('ULIBPY_FMUS_DEBUG')>0)
		self.processor = Processor(self.run_configuration)
		self.generator = Generator(self.run_configuration, self)



	def set_outerr(self, stdout, stderr):
		self.stdout = stdout
		self.stderr = stderr


	def set_env_template(self):
		from schnell.app.utils import env_ulibpy
		env_vars = env_ulibpy()
		env_dict = dict(zip(env_vars, list(map(env_get, env_vars))))
		# self.debug('update env dg:', env_dict)
		self.run_configuration['replacer'].update(env_dict)


	def change_pwd(self, new_folder):
		"""
		sementara dipanggil manual 
		dan perlu digunakan sebelum set_file_dir_template etc
		krn agar get_cwd_pwd merujuk ke new_folder
		"""
		from schnell.app.dirutils import chdir
		if isdir(new_folder):
			chdir(new_folder)


	def get_cwd_pwd(self):
		cwd_pwd = get_cwd()
		if env_exist('ULIBPY__PWD__'):
			cwd_pwd = env_get('ULIBPY__PWD__')
		return cwd_pwd


	def set_dir_template(self, dir_template, start_fresh=False):
		if start_fresh: # paksa, sebelum dipake oleh self.get_cwd_pwd()
			env_set('ULIBPY__PWD__', get_cwd())
			self.run_configuration['projectdir'] = get_cwd()
		if not dir_template:
			indah4(f'''[app.fmus.fmus]
			set_dir_template(dir_template) => dir_template is None.
			''', warna='red')
			input('>>> ')
		self.run_configuration['replacer'].update({
			'__CURDIR__': dir_template,
			# '__CURDIR': dir_template,
			'__PWD__': get_cwd() if start_fresh else self.get_cwd_pwd(),
			'__PWD': get_cwd() if start_fresh else self.get_cwd_pwd(),
		})


	def set_dir_template_from_file(self, file_template, start_fresh=False):
		if start_fresh: # paksa, sebelum dipake oleh self.get_cwd_pwd()
			env_set('ULIBPY__PWD__', get_cwd())
			self.run_configuration['projectdir'] = get_cwd()
		if not file_template:
			indah4(f'''[app.fmus.fmus]
			set_dir_template_from_file(file_template) => file_template is None.
			''', warna='red')
			input('>>> ')
		dir_template = ayah(file_template, 1)
		self.run_configuration['replacer'].update({
			'__CURDIR__': dir_template,
			# '__CURDIR': dir_template,
			'__PWD__': get_cwd() if start_fresh else self.get_cwd_pwd(),
			'__PWD': get_cwd() if start_fresh else self.get_cwd_pwd(),
		})


	def set_file_template(self, file_template, start_fresh=False):
		if start_fresh: # paksa, sebelum dipake oleh self.get_cwd_pwd()
			env_set('ULIBPY__PWD__', get_cwd())
			self.run_configuration['projectdir'] = get_cwd()
		self.run_configuration['replacer'].update({
			'__FILE__': file_template,
			# '__FILE': file_template,
			'__IF_ETH0': CURRENT_IP_ETH0,
			'__SYS_TEMP2': tempdir(True), # diakhiri dg /
			'__SYS_TEMP': tempdir(),
			'__PWD__': get_cwd() if start_fresh else self.get_cwd_pwd(),
			'__PWD': get_cwd() if start_fresh else self.get_cwd_pwd(),
		})
		# indah4(f'set_file_template pwd = {self.get_cwd_pwd()}', warna='cyan')
		self.set_env_template()


	def set_file_dir_template(self, file_template, dir_template=None, start_fresh=False):
		"""
		upd 17/8/22
		kita tambah "start_fresh" krn utk bypass __ULIBPY_PWD jk bener2 baru dari awal
		(misal dari FM jk klik kanan direktori, copy mk, dan exec mk)
		"""
		is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1

		if not dir_template and file_template:
			dir_template = ayah(file_template, 1)
		else:
			if is_debugging:
				indah4(f'[fmus][set_file_dir_template] terima dir template: {dir_template}', warna='blue', layar='black')
		if start_fresh: # paksa, sebelum dipake oleh self.get_cwd_pwd()
			env_set('ULIBPY__PWD__', get_cwd())
			self.run_configuration['projectdir'] = dir_template
		data_replacer = {
			'__FILE__': file_template,
			# '__FILE': file_template,
			'__IF_ETH0': CURRENT_IP_ETH0,
			'__SYS_TEMP2': tempdir(True), # diakhiri dg /
			'__SYS_TEMP': tempdir(),
			# upd 23/8/2022, awalnya dari /tmp/deleteme, lalu di /tmp, masih juga get_cwd() /tmp/deleteme, jd mending ubah ke dir_template agar hasilkan /tmp
			'__PWD__': get_cwd() if start_fresh else self.get_cwd_pwd(),
			'__PWD': get_cwd() if start_fresh else self.get_cwd_pwd(),
			'__CURDIR__': dir_template,
			# '__CURDIR': dir_template,
		}
		self.run_configuration['replacer'].update(data_replacer)
		if is_debugging:
			indah4(f'''[fmus][set_file_dir_template]
			informasi cwd utk pwd:
			os.get_cwd	: {os.getcwd()}
			get_cwd		: {self.get_cwd_pwd()}
			start_fresh	: {start_fresh}
			self.run_configuration['replacer']['__PWD__'] = {self.run_configuration['replacer']['__PWD__']}
			''', warna='cyan')
		if is_debugging:
			indah4(f'[fmus][set_file_dir_template] set_file_dir_template => update replacer file+dir => {data_replacer}', warna='red')
		self.set_env_template()
		# indah4(f'set_file_dir_template pwd = {self.get_cwd_pwd()}', warna='cyan')


	def process_mkfile(self, filepath, baris_entry='index/fm.us', basepath=None):
		"""
		utk misal peroleh mkfile output utk django dari bantu-django
		"""
		from schnell.app.fileutils import get_definition_double_entry_aware
		# ini bikin __PWD dan __CURDIR bisa beda, krn gak respect dir_template
		self.set_file_dir_template(file_template=filepath, dir_template=basepath)

		# indah4(f'''process_mkfile:
		# 	replacer:
		# 	{self.run_configuration['replacer']}
		# ''')

		program = get_definition_double_entry_aware(filepath, baris_entry)
		if not program:
			return None

		self.process(program)

		return program


	def process(self, program, projectdir=None, replacer=None, rootvars=None, capture_outerr=False, *args, **kwargs):
		"""
		fmus:process ini utk handle program Fmus
		juga biasanya dipanggil oleh child program dari program Fmus

		processor
		generator

		sementara rootvars blm diproses krn gimana cara masukkan??
		"""
		is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
		# is_debugging = 2
		short_program = program[:100].replace('\n','\\n').replace('\t','\\t')

		if is_debugging:
			indah(f'''***** FMUS *****
	 		program = {short_program}
			projectdir = {projectdir}
			replacer = {replacer}
			rootvars = {rootvars}
			self.run_configuration['replacer'] = {self.run_configuration['replacer']}
			''', warna='magenta', layar='black', newline=True, bold=True, blink=True)
		# indah4(f"[fmus] #3 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		if projectdir:
			if isdir(projectdir):
				# ini dipake utk rekursif dari Generator
				if is_debugging:
					self.debug('*** [fmus:process] #1a setting projectdir utk item.workdir ke:', projectdir)
				self.run_configuration['projectdir'] = projectdir
			else:
				if is_debugging:
					self.debug('*** [fmus:process] #1b not yet dir:', projectdir, '...creating...')
				# per 10 jan, kita buat dulu dir
				# ini biasanya krn kita bikin child project
				indah4(f'\n\n[fmus:process][create_dir] {projectdir} is not dir (yet), creating...\n\n')
				create_dir(projectdir)
				self.run_configuration['projectdir'] = projectdir

		# autogui_confirm('fmus process #2')

		if replacer:
			self.run_configuration['replacer'].update(replacer)
			# TODO:
			# update juga run_configuration yg dipake generator
			self.generator.update_config_replacer(replacer)

		# indah4(f'''
		# 	fmus replacer sebelum rootvars:
		# 	{self.run_configuration['replacer']}
		# ''')
		# indah4(f"[fmus] #5 self.run_configuration['projectdir']={self.run_configuration['projectdir']}", warna='cyan')

		if rootvars:
			self.run_configuration['initial_rootvars'] = rootvars

		# indah4(f'''
		# 	fmus replacer sesudah rootvars, sblm memanggil processor:
		# 	{self.run_configuration['replacer']}
		# ''')

		if is_debugging:
			self.debug(f'[fmus:process] #2 calling processor.process_language() with program = [{program}]\n')

		pohon = self.processor.process_language(program)

		if is_debugging:
			self.debug(f'[fmus:process] #3 calling pre_generator sblm generate, AnyNode:\n')
			indah4(str(RenderTree(pohon)), warna='yellow', layar='blue')
		# wait for input key atau modify pohon utk loncat
		confirm = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_CONFIRM_PREGENERATOR"]
		if confirm:
			pohon = self.pre_generator(pohon)

		# cek __FILE__ sama antara fmus dan generator
		if '__FILE__' in self.run_configuration['replacer']:
			'''
			jk dari clipboard gak ada __FILE__
			'''
			file1 = self.run_configuration['replacer']['__FILE__']
			file2 = self.generator.run_configuration['replacer']['__FILE__']
			if file1 != file2:
				pesan = f'fmus __FILE__ \n{file1}\nberbeda dg generator __FILE__ \n{file2}'
				indah0(pesan, warna='cyan', bold=True, newline=True)
				indah0('Tekan "y" utk replace generator:', warna='magenta', bold=True)
				yesno = input(' ')
				if yesno == 'y':
					self.generator.run_configuration['replacer'].update(self.run_configuration['replacer'])
					indah0(f"nilai replacer generator skrg: {self.generator.run_configuration['replacer']}", newline=True, bold=True)

		if is_debugging:
			self.debug('[fmus:process] #4 calling generator.py:generate()\n')

		self.generator.generate(pohon, capture_outerr=capture_outerr)
		self.post_generator()
		indah4(f"✅[{short_program}]", warna='green', layar='black')


	def attrs_value(self, pohon):
		"""
		[['counter: 1', 'name: f'],
		['counter: 2', 'name: b'],
		['counter: 3', 'name: a'],
		['counter: 4', 'name: d'],
		['counter: 5', 'name: c'],
		['counter: 6', 'name: e'],
		['counter: 7', 'name: g'],
		['counter: 8', 'name: i'],
		['counter: 9', 'name: h']]
		"""
		return [f"{item}: {getattr(pohon, item)}" for item in dir(pohon) if not item.startswith('_') and not item in Common.keywords]


	def attrs_value_iter(self, pohon):
		"""
		gimana jk node di pohon gak punya attr counter.
		"""
		result = None
		try:
			result = [self.attrs_value(node) for node in PreOrderIter(pohon)]
			result = json.dumps(result, indent=4)
		except Exception as err:
			return None

		return result


	def filter_children(self, pohon, value, upperbound=None):
		if upperbound:
			children = findall(pohon, lambda node: value <= node.counter <= upperbound)
		else:
			children = findall(pohon, lambda node: node.counter >= value)
		if children:
			pohon.children = children

		return pohon


	def pre_generator(self, pohon=None):
		if pohon:
			counters = [node.counter for node in PreOrderIter(pohon) if node.counter >= 0]
			attributes = self.attrs_value_iter(pohon)
			projectdir = self.run_configuration['projectdir']

			self.debug('\n'*3)
			self.debug('*'*10, 'pre_generator:')
			self.debug('\n'*2)
			done = False
			while not done:
				indah0(f'[app.fmus] Pilih counter utk jadi root tree atau skip: {counters}', warna='magenta')
				indah0(f"\nProjectdir = {projectdir}", warna='yellow', bold=True, blink=True)
				pilih = input(" >> ")
				if pilih in counters:
					# pohon = find_counter(pohon, pilih)
					pohon = self.filter_children(pohon, pilih)
					done = True
				elif '-' in pilih:
					m = re.match(r'^\s*(\d+)\s*-\s*(\d+)', pilih)
					if m:
						start = int(m.group(1))
						end = int(m.group(2))
						if start in counters and end in counters:
							pohon = self.filter_children(pohon, start, end)
							done = True
						else:
							self.debug(f'{start} dan {end} di luar range counters.')
				elif isinstance(pilih, str) and pilih.isdigit():
					pilih = int(pilih)
					if pilih in counters:
						# pohon = find_counter(pohon, pilih)
						pohon = self.filter_children(pohon, pilih)
						done = True
				elif pilih == 'g' or pilih == 'graph':
					self.debug(RenderTree(pohon))
				elif pilih == 'l' or pilih == 'ls':
					indah0(attributes, warna='green', newline=True)
				elif pilih.startswith('/') and pilih != '/':
					projectdir = pilih
					if isdir(pilih):
						projectdir = abs_dir(pilih)					
					# ternyata di sini item.workdir sudah masuk anytree
					# jadi gak lagi baca run_configuration
					allnodes = findall(pohon)
					def modifier(node):
						original = node.workdir
						node.workdir = normy(node.workdir.replace(original, projectdir, 1))
						return node
					
					modified = list(map(modifier, allnodes))
					# self.run_configuration['projectdir'] = projectdir
					# self.generator.config['projectdir'] = projectdir
					self.generator.run_configuration['projectdir'] = projectdir
					indah0(f'new projectdir {projectdir}', warna='green', bold=True, newline=True)
					done = True
				elif pilih == '':
					done = True
				else:
					self.debug('pilihan adlh:', pilih)

		return pohon


	def post_generator(self):
		# if env_int('ULIBPY_FMUS_DEBUG') and env_int('ULIBPY_FMUS_DEBUG_SHOW_TREE'):
		if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_FMUS_DEBUG_SHOW_TREE"]:
			os.system(f'tree -L 2 -I "node_modules" {self.run_configuration["projectdir"]}')
