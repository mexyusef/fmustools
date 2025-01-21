import glob, os, re, subprocess
from .dirutils import (
	tempdir,
	under_tempdir,
	timestamp,
	joiner,
)
# from schnell.app.dirutils import under_tempdir, timestemp, joiner
from .clipboardutils import trypaste
from .printutils import indah0, indah4
from .utils import (
	PBPASTE,
	PBCOPY,
	LANGUAGES,
	platform,
)
from .fileutils import file_write, file_content


BASE_CONFIG = {
  'current_workdir': None,
  'grep_context': 0,
  'grep_case_insensitive': False, # default W dan w berbeda
}
# https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.4/
# https://mvnrepository.com/artifact/com.typesafe.akka/akka-http-core

# SCALA_VERSION = "2.13.2"
# SCALA_VERSION = "2.13.3"
# SCALA_VERSION = "2.13.14"
SCALA_VERSION = '2.13.0'

# akka_http_version [10.2.1]:
# kka_grpc_version [1.0.2]:
# akka_version [2.6.10]:
# sbt_version [1.4.4]:

# default_configuration = {
#   'technologies': TECHNOLOGIES,
#   'default_technology': 'react',
# }
PREFIX_SETUP  = '00'
PREFIX_EDIT   = '01'
PREFIX_EXEC   = '02'


SBT_TEMPLATE = """name := "__NAME__"
version := "__VERSION__"
organization := "__ORG__"
scalaVersion := "__SCALA__"
"""

SCALA_SBT_CHOICELIST = [
'sbt/scala-seed.g8',
'playframework/play-scala-seed.g8',
'akka/akka-grpc-quickstart-scala.g8',
'akka/akka-http-quickstart-scala.g8',
'akka/akka-quickstart-scala.g8',
'scalafx/scalafx.g8',
'manual'
]
SCALA_SBT_CHOICES = f"""Choose SBT project type:
1. {SCALA_SBT_CHOICELIST[0]}
2. {SCALA_SBT_CHOICELIST[1]}
3. {SCALA_SBT_CHOICELIST[2]}
4. {SCALA_SBT_CHOICELIST[3]}
5. {SCALA_SBT_CHOICELIST[4]}
6. {SCALA_SBT_CHOICELIST[5]}
7. {SCALA_SBT_CHOICELIST[6]}
"""

PROGRAMS = {
	'ff': '/usr/bin/firefox -no-remote -P',
	'chr': 'chromium-browser',
	'term': 'qterminal',
	'term2': 'gnome-terminal',
	'term3': 'xterm',
}


def run_in_folder(basedir, command):
	perintah = f"cd {basedir} && {command}"
	# print('===>', perintah)
	indah0(f"{'='*20} {perintah}", warna='yellow', newline=True)
	os.system(perintah)


hapus = "del /F" if platform() in ['win32', 'windows', 'desktop'] else "rm -f"


def create_folder_and_run(basedir, command):
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	perintah = f"cd {basedir} && {command}"
	# print('===>', perintah)
	indah0(f"{'='*20} {perintah}", warna='yellow', newline=True)
	os.system(perintah)
	os.system(f'tree {basedir}')


def create_project(basedir, sbt_template):
	# cek basedir jk blm ada create
	# if not os.path.exists(basedir):
	# 	os.makedirs(dirpath)
	# perintah = f"cd {basedir} && sbt new {sbt_template}"
	# print('===>', perintah)
	# os.system(perintah)
	# os.system(f'tree {basedir}')
	create_folder_and_run(basedir, f"sbt new {sbt_template}")


def sbt_new(basedir, sbt_template):
	# perintah sbt new ada input user, jd gak bisa masuk thread
	# thr = threading.Thread(target=create_project, args=(basedir, sbt_template))
	# thr.start()
	create_project(basedir, sbt_template)


def create_project_manual(basedir, projectname):
	cmd1 = f'mkdir -p {basedir}' + '/src/{main,test}/{java,resources,scala}'
	cmd2 = f'mkdir {basedir}' + '/{lib,project,target}'
	name = input(f'Masukkan nama proyek [{projectname}]: ')
	name = name if name else projectname
	version = input('Masukkan version [1.0.0]: ')
	version = version if version else "1.0.0"
	org = input('Masukkan nama organisasi [be.fulgent]: ')
	org = org if org else "be.fulgent"
	build_sbt_content = SBT_TEMPLATE \
		.replace('__NAME__', name) \
		.replace('__VERSION__', version) \
		.replace('__ORG__', org) \
		.replace('__SCALA__', SCALA_VERSION)

	build_sbt = os.path.join(basedir, 'build.sbt')
	with open(build_sbt, 'w', encoding='utf-8') as fd:
		fd.write(build_sbt_content)

	# utk bisa {a,b,c} hrs pake bash, gak bisa sh
	os.system(f'''/bin/bash -c "{cmd1}"''')
	os.system(f'''/bin/bash -c "{cmd2}"''')
	print('Hasil SBT Manual:')
	os.system(f'ls -al {basedir}')
	os.system(f'tree {basedir}')


def sbt_manual(basedir, projectname):
	""" krn ada input IO gak bisa pake thread...
	"""
	create_project_manual(basedir, projectname)
	# thr = threading.Thread(target=create_project_manual, args=(basedir,))
	# thr.start()


def rust_clipboard_to_project(libraries=None, cmdargs=None):
	"""
	folder/
		Cargo init
	"""
	projectdir = f'project_{timestamp()}'
	prompt = f"Enter folder name or Return for default ({projectdir}): "
	projectname = input(prompt)
	if not projectname:
		projectname = projectdir
	project_folder = under_tempdir(projectname)

	run_in_folder(project_folder, 'cargo init')
	toml = os.path.join(project_folder, 'Cargo.toml')
	mainrs = os.path.join(project_folder, 'src', 'main.rs')
	print('main.rs:', mainrs)
	dependencies = '\n'.join([item.replace('-','',1) for item in libraries])
	with open(toml, 'a') as fd:
		fd.write(dependencies)

	command = f"{PBPASTE} > {mainrs}"
	os.system(command)
	run_in_folder(project_folder, 'cargo run')

class Configuration:

    myself = os.path.abspath(__file__)
    config_dir = os.path.dirname(os.path.abspath(__file__))
    ulibpy_dir = os.path.normpath(os.path.join(config_dir, os.path.pardir))
    data_dir = os.path.join(ulibpy_dir, 'data')
    ulib_dir = os.path.normpath(os.path.join(ulibpy_dir, os.path.pardir))  


    @classmethod
    def google_file(cls, GOOGLE_JSONFILE='google.json'):
        """
        *.Configuration.google_file()
	schnell.app.google.json
	"type": "service_account",
	"project_id": "urepl-072018",
	"client_id": "101946434507733514522",
        """
        return os.path.join(Configuration.config_dir, GOOGLE_JSONFILE)


    def __init__(self, *args, **kwargs):
        self.default_config = BASE_CONFIG
        self.running_config = BASE_CONFIG
        if kwargs:
            if 'base' in kwargs:
                self.chdir(kwargs['base'])


    def reset(self):
        self.running_config = BASE_CONFIG


    def get(self):
        return self.running_config


    def value(self, key):
        if key in self.running_config:
            return self.running_config[key]

        return None


    def keys(self):
        return list(self.running_config.keys())


    def cwd(self):
        return self.running_config['current_workdir']


    def getcwd(self):
        return self.running_config['current_workdir']


    def chdir(self, newdir, absolute=False):
        if (not self.running_config['current_workdir']) or absolute:
            self.running_config['current_workdir'] = newdir
        else:
            newabsdir = os.path.join(self.running_config['current_workdir'], newdir)
            if os.path.isdir(newabsdir):
                self.running_config['current_workdir'] = newabsdir
            else:
                print(f"Not a dir: {newabsdir}.")


    def up(self):
        if self.running_config['current_workdir']:
            newdir = os.path.join(self.running_config['current_workdir'], os.path.pardir)
            self.chdir(newdir)
            print("Current workdir =", self.running_config['current_workdir'])
        else:
            print("Current workdir is not set", self.running_config['current_workdir'])


    def uptimes(self, times):
        """
        cd ../../.. = uptimes(3)
        """
        if self.running_config['current_workdir']:
            for _ in range(times):
                self.up()
            print("Current workdir =", self.running_config['current_workdir'])
        else:
            print("Current workdir is not set", self.running_config['current_workdir'])

# class Configuration:

#   myself = os.path.abspath(__file__)
#   config_dir = os.path.dirname(os.path.abspath(__file__))
#   ulibpy_dir = os.path.normpath(os.path.join(config_dir, os.path.pardir))
#   data_dir = os.path.join(ulibpy_dir, 'data')
#   ulib_dir = os.path.normpath(os.path.join(ulibpy_dir, os.path.pardir))  


#   @classmethod
#   def google_file(cls, GOOGLE_JSONFILE='google.json'):
#     """
#     *.Configuration.google_file()
# 	schnell.app.google.json
# 	"type": "service_account",
# 	"project_id": "urepl-072018",
# 	"client_id": "101946434507733514522",
#     """
#     return os.path.join(Configuration.config_dir, GOOGLE_JSONFILE)


#   def __init__(self, *args, **kwargs):
#     self.default_config = BASE_CONFIG
#     self.running_config = BASE_CONFIG
#     if kwargs:
#       if 'base' in kwargs:
#         self.chdir(kwargs['base'])


#   def reset(self):
#     self.running_config = BASE_CONFIG


#   def get(self):
#     return self.running_config


#   def value(self, key):
#     if key in self.running_config:
#       return self.running_config[key]

#     return None


#   def keys(self):
#     return list(self.running_config.keys())


#   def cwd(self):
#     return self.running_config['current_workdir']


#   def getcwd(self):
#     return self.running_config['current_workdir']


#   def chdir(self, newdir, absolute=False):
#     if (not self.running_config['current_workdir']) or absolute:
#       self.running_config['current_workdir'] = newdir
#     else:
#       newabsdir = os.path.join(self.running_config['current_workdir'], newdir)
#       if os.path.isdir(newabsdir):
#         self.running_config['current_workdir'] = newabsdir
#       else:
#         print(f"Not a dir: {newabsdir}.")


#   def up(self):
#     if self.running_config['current_workdir']:
#       newdir = os.path.join(self.running_config['current_workdir'], os.path.pardir)
#       self.chdir(newdir)
#       print("Current workdir =", self.running_config['current_workdir'])
#     else:
#       print("Current workdir is not set", self.running_config['current_workdir'])


#   def uptimes(self, times):
#     """
#     cd ../../.. = uptimes(3)
#     """
#     if self.running_config['current_workdir']:
#       for _ in range(times):
#         self.up()
#       print("Current workdir =", self.running_config['current_workdir'])
#     else:
#       print("Current workdir is not set", self.running_config['current_workdir'])


class FileExecutor:

	def newfilename(self, custom_filename=None):
		self.filename_noext = f'delete_{timestamp()}'
		if custom_filename:
			self.filename_noext = custom_filename # HelloWorld

		extension = 'cpp' if self.language == 'clang' else self.language
		self.filename = self.filename_noext + '.' + extension # HelloWorld.java
		self.filepath = os.path.join(self.folder, self.filename)


	def assign(self, newdir=tempdir()):
		self.folder = newdir
		self.contiki = Configuration(self.folder)
		self.newfilename() # krn self.folder dibutuhkan utk hasilkan self.filepath


	@property
	def bahasa(self):
		return LANGUAGES
		

	def cleanup(self, bahasa):
		if bahasa not in LANGUAGES:
			for lang in LANGUAGES: # bahasa py/sc, lang = python/scala
				if lang.startswith(bahasa):
					return lang
		# elif bahasa == 'py':
		# 	return 'python'
		else:
			return bahasa

		return 'py'


	def set_language_filename(self, bahasa):
		self.language = self.cleanup(bahasa)
		#self.project_language = self.cleanup(bahasa)


	def __init__(self, bahasa='py', *args, **kwargs):

		# self.set_language_filename(bahasa)
		self.language = self.cleanup(bahasa)
		self.assign()

		# if args:
		# 	for item in args:
				# print('*args', item)

		if kwargs:
			if 'base' in kwargs:
				if os.path.isdir(kwargs['base']):
					self.assign(kwargs['base'])
			for k,v in kwargs.items():
				print('**kwargs, k=', k, 'v=', v)

		# print(f'Language {self.language} at {self.folder}.')


	def execFile(self, filepath):
		from .fileutils import copy_content
		copy_content(filepath)
		self.execute()


	def exec(self, language=None):
		"""
		kita tambah command line arguments dan optional libraries
		terutama utk cpp
		tapi gimana formatnya
		clang -lpthread echo 9070 0.0.0.0
		"""
		libraries = None
		cmdargs = None
		if ' ' in language:
			print(f'[app.executor.FileExecutor::exec] terima bahasa [{language}].')
			arguments = language.split()
			language = arguments[0]
			libraries = [item for item in arguments if item.startswith('-')]
			cmdargs = [item for item in arguments[1:] if not item.startswith('-')]

		if language:
			'''
			normalize language yg diinput user
			misal dari py ke python
			'''
			self.language = self.cleanup(language)
			self.newfilename() # termasuk set self.filepath

		# print(f'exec: cleaned terima bahasa {self.language}.')
		self.execute()


	def execute(self, language=None, content=None):
		"""
		kita tambah command line arguments dan optional libraries
		terutama utk cpp
		tapi gimana formatnya
		clang -lpthread echo 9070 0.0.0.0
		"""
		libraries = None
		cmdargs = None
		if language:
			if ' ' in language:
				# ini utk kasih options...
				print(f'[app.executor.FileExecutor::execute]: terima bahasa {language}.')
				arguments = language.split()
				language = arguments[0]
				libraries = [item for item in arguments if item.startswith('-')]
				cmdargs = [item for item in arguments[1:] if not item.startswith('-')]

			self.language = self.cleanup(language)
			self.newfilename() # termasuk set self.filepath

		# print(f'exec: cleaned terima bahasa {self.language}.')
		if self.language in ['python', 'py']:
			self.handle_py(content=content)
		elif self.language == 'go':
			self.handle_go()
		elif self.language == 'cpp':
			self.handle_cpp(libraries, cmdargs)
		elif self.language == 'clang':
			self.handle_clang(libraries, cmdargs)
		elif self.language == 'rs':
			print('handle rust #0')
			self.handle_rust(libraries, cmdargs)
		elif self.language == 'java':
			self.handle_java()
		elif self.language == 'kt':
			self.handle_kotlin()
		elif self.language == 'cs':
			self.handle_csharp()
		elif self.language == 'clj':
			self.handle_clojure()
		elif self.language == 'js':
			self.handle_js()
		elif self.language == 'sh':
			self.handle_sh()
		elif self.language == 'hs':
			self.handle_haskell()
		elif self.language == 'scala':
			self.handle_scala()


	def print_info(self, command):
		print(f"Mau jalankan {command}.")
		indah0(f"{'='*20} {self.filepath}", warna='yellow', bold=True, newline=True)


	def handle_cpp(self, libraries=None, cmdargs=None, filepath=None):
		# print('create random C++ file in temp, compile, run, wait until press continue')
		# filename = f'cpp_{timestamp()}'
		# outputfilepath = under_tempdir(filename) + '.exe'
		outputfilepath = os.path.join(self.folder, self.filename_noext + '.exe')
		# filepath = under_tempdir(filename) + '.cpp'
		# os.system(f"{PBPASTE} > {filepath} && go run {filepath}")
		kompilasi = f"g++ {self.filepath} -o {outputfilepath}"
		if libraries:
			kompilasi += ' ' + ' '.join(libraries)
		command = f"{PBPASTE} > {self.filepath} && {kompilasi} && {outputfilepath}"
		if cmdargs:
			command += ' ' + ' '.join(cmdargs)
		self.print_info(command)
		os.system(command)


	def handle_clang(self, libraries=None, cmdargs=None, cppstd='c++1z'):
		outputfilepath = os.path.join(self.folder, self.filename_noext + '.exe')
		kompilasi = f"clang++ {self.filepath} -o {outputfilepath} -Wall -Wextra -std={cppstd} -g"
		if libraries:
			kompilasi += ' ' + ' '.join(libraries)
		command = f"{PBPASTE} > {self.filepath} && {kompilasi} && {outputfilepath}"
		if cmdargs:
			command += ' ' + ' '.join(cmdargs)
		self.print_info(command)
		os.system(command)


	def handle_rust(self, libraries=None, cmdargs=None):
		print('rust #1')
		if libraries:
			rust_clipboard_to_project(libraries, cmdargs)
			return
		outputfilepath = os.path.join(self.folder, self.filename_noext + '.exe')
		kompilasi = f"rustc {self.filepath} -o {outputfilepath}"
		# kompilasi = f"rustc {self.filepath}"
		command = f"{PBPASTE} > {self.filepath} && {kompilasi} && {outputfilepath}"
		self.print_info(command)
		os.system(command)


	def handle_haskell(self, filepath=None):
		outputfilepath = os.path.join(self.folder, self.filename_noext + '.exe')
		kompilasi = f"ghc -o {outputfilepath} {self.filepath}"
		command = f"{PBPASTE} > {self.filepath} && {kompilasi} && {outputfilepath}"
		self.print_info(command)
		os.system(command)


	def handle_csharp(self, filepath=None):
		# handle ms windows
		libraries0 = '-r:System.Windows.Forms.dll -r:System.Drawing.dll'
		# handle gtk
		libraries1 = '-pkg:gtk-sharp-3.0'
		libraries = f'{libraries0} {libraries1}'

		outputfilepath = os.path.join(self.folder, self.filename_noext + '.exe')
		# kompilasi = f"mcs {self.filepath} -o {outputfilepath}"
		kompilasi = f"mcs {self.filepath} {libraries}"
		command = f"{PBPASTE} > {self.filepath} && {kompilasi} && {outputfilepath}"
		self.print_info(command)
		os.system(command)


	def handle_go(self, filepath=None):
		content = trypaste()
		if 'github' in content:  # ada import github berarti pake module
			foldername = 'go_'+timestamp()
			projectdir = under_tempdir(foldername)
			filename = 'main.go'
			file_write(joiner(projectdir, filename), content)
			subprocess.run(f'go mod init {foldername}'.split(), shell=True, check=True, cwd=projectdir)
			subprocess.run('go mod tidy'.split(), shell=True, check=True, cwd=projectdir)
			subprocess.run(f'go run {filename}'.split(), shell=True, check=True, cwd=projectdir)
		else:
			command = f"{PBPASTE} > {self.filepath} && go run {self.filepath} && {hapus} {self.filepath}"
			self.print_info(command)
			os.system(command)


	def handle_java(self, filename=None):
		'''
		khusus java, nama file harus sama dg nama class dlm file
		'''
		print('create random JAVA file in temp, compile, run, wait until press continue')
		while not filename:
			filename = input("Masukkan nama file: ")
			self.newfilename(filename)

		lokasi = self.folder
		# Failed to change permissions on C:\Users\mexus\.scalac\fsc_port. The compilation daemon requires a secure directory; use -nc to disable the daemon.
		command = f"({PBPASTE} > {self.filepath} && javac {self.filepath} && cd {lokasi} && java {self.filename_noext})" #" && rm -f {filepath}"
		self.print_info(command)
		os.system(command)


	def handle_kotlin(self, filename=None):
		lokasi = self.folder
		command = f"({PBPASTE} > {self.filepath} && cd {lokasi} && kotlinc {self.filename} -include-runtime -d {self.filename_noext}.jar && java -jar {self.filename_noext}.jar)" #" && rm -f {filepath}"
		self.print_info(command)
		os.system(command)


	def handle_clojure(self, filepath=None):
		# command = f"({PBPASTE} > {self.filepath} && cd {self.folder} && clj -M {self.filename})"
		command = f"({PBPASTE} > {self.filepath} && cd {self.folder} && clj {self.filename})"
		self.print_info(command)
		os.system(command)


	def handle_py(self, content=None):
		# errno = os.system(f"{PBPASTE} | python3")
		# if errno:
		# 	print(f"non-zero errno from running Python code: {errno}.")
		if content:
			file_write(self.filepath, content)
			command = f"python {self.filepath} && {hapus} {self.filepath}"
		else:
			command = f"{PBPASTE} > {self.filepath} && python {self.filepath} && {hapus} {self.filepath}"
		self.print_info(command)
		os.system(command)


	def handle_js(self, filepath=None):
		errno = os.system(f"{PBPASTE} | node")
		if errno:
			print(f"non-zero errno from running JS code: {errno}.")


	def handle_sh(self, filepath=None):
		errno = os.system(f"{PBPASTE} | bash")
		if errno:
			print(f"non-zero errno from running BASH code: {errno}.")


	def handle_scala(self, filepath=None):
		command = f"{PBPASTE} > {self.filepath} && scala -nc {self.filepath}" #" && rm -f {filepath}"
		self.print_info(command)
		os.system(command)


ExecFile = FileExecutor()

def script_handler(bahasa=None):
    if bahasa:
        ExecFile.exec(bahasa.strip())
    else:
        print('Usage: :py atau :cpp dst.\n\tMasukkan code ke dlm clipboard terlebih dahulu.\n\nBahasa:', ExecFile.bahasa)


def handle_bash(code):
    """
    sementara baru bisa handle bash
    """
    return subprocess.Popen(code, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').strip()
