import json, os
from schnell.app.dirutils import (
	ayah,
	isdir,
	here,
	joiner,
)
from .context import (
	context, 
	Lang,
	languages,
	declanguanges,
)


class Configuration:
	CONFIG = 'config.json'
	default_configuration = {}
	# string_keys = []
	# number_keys = []
	# bool_keys = []

	def __init__(self, repl_object):
		self.run_configuration = {}
		self.repl = repl_object
		here = os.path.dirname(__file__) # os.getcwd()
		# print(__file__, os.path.dirname(__file__), os.path.basename(__file__))
		config_file = os.path.join(here, Configuration.CONFIG)
		with open(config_file) as json_file:
			Configuration.default_configuration = json.load(json_file)
	
		Configuration.default_configuration['default']['cwd'] = here
		self.read_config()


	def read_config(self):
		"""
		os.path.join(self.run_configuration['outputdir']
			/tmp
		self.run_configuration['output']
			target
		"""
		self.run_configuration = Configuration.default_configuration['default']
		# ULIBPY_FMUS_DEBUG override verbose
		if 'ULIBPY_FMUS_DEBUG' in os.environ:
			debug = int(os.environ.get('ULIBPY_FMUS_DEBUG'))
			self.run_configuration['verbose'] = debug
			# print(f"\n\n\n************ debug = {self.run_configuration['verbose']} = {debug} ************\n\n\n")


	def print_config(self):
		config = json.dumps(self.run_configuration, indent=4)
		print(config)
		# self.client_to_host.comm_handler(config)


	def change_config_string(self, code, key, callback=None):
		nilai = code.replace(key, '', 1).strip()
		if nilai:
			self.run_configuration[key] = nilai

	def change_config_number(self, code, key, callback=None):
		nilai = code.replace(key, '', 1).strip()
		if nilai and nilai.isdigit():
			self.run_configuration[key] = int(nilai)

	def change_config_toggle(self, key, callback=None):
		self.run_configuration[key] = not self.run_configuration[key]

	def change_configuration(self, code=None):
		"""
		ada 2 jenis config
		toggle -> gunakan if ==
		string -> gunakan if startswith
		number -> gunakan if startswith
		"""
		# print('change_configuration')
		if not code:
			pass

		elif code .startswith('lang') or code .startswith('L'):
			'''
			lang go|py utk ganti language
			'''						
			if code .startswith('lang'):
				pilihan = code.replace('lang', '', 1).strip()
			else:
				pilihan = code.replace('L', '', 1).strip()

			if pilihan != '' and pilihan in languages:
				jawab = pilihan
			else:
				jawab = self.repl.temporary_prompt(choices=languages)
			# print('peroleh:', jawab)
			if jawab:
				self.run_configuration['current_language'] = jawab
				context['current_language'] = jawab

		elif code .startswith('decl'):
			'''
			decl react|wpf|html|antd utk ganti declarative language style
			'''			
			jawab = self.repl.temporary_prompt(choices=declanguanges)
			if jawab:
				self.run_configuration['current_declarative'] = jawab
				context['current_declarative'] = jawab

		elif code .startswith('u') or code == 'u':
			pilihan = sorted([item for item in os.environ if item.startswith('ULIBPY')])
			jawab = self.repl.temporary_prompt(choices=pilihan)
			if jawab:
				# self.run_configuration['current_declarative'] = jawab
				# context['current_declarative'] = jawab
				lama = os.environ.get(jawab)
				nilai_baru = input(f'Nilai lama = {lama}. Masukkan nilai baru untuk {jawab}: ')
				if nilai_baru:
					# os.environ.set(jawab, nilai_baru)
					os.environ[jawab] = nilai_baru

		elif code .startswith('gui'):
			'''
			gui gtk, pyqt5, rs-cursive
			'''			
			jawab = self.repl.temporary_prompt(choices=declanguanges)
			if jawab:
				self.run_configuration['current_gui'] = jawab
				context['current_gui'] = jawab

		elif code == 'out':
			self.run_configuration['print_after_process'] = not self.run_configuration['print_after_process']

		elif code .startswith('wf'):
			code = code.replace('wf', '', 1).strip()
			if code:
				if isdir(code):
					self.run_configuration['working_folder'] = code
					context['working_folder'] = code
			else:
				done = False
				while not done:
					terima = input('New working folder: ').strip()
					if not terima:
						print('Enter valid folder')
					elif isdir(terima):
						self.run_configuration['working_folder'] = terima
						context['working_folder'] = terima
						done = True
					elif terima == 'no' or terima == 'x':
						done = True
					else:
						print('Enter valid folder')

		self.print_config()
