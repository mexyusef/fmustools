import sys
from multiprocessing import Process
from .features import features, lalang
from .gitor import gitor
from .gitdetail import git_detail
from schnell.app.utils import (
	perintahsp_simple_chdir,
	env_get,
	perintahsp_simple,
	perintah_shell,
	is_windows,
	winpath_to_wslpath,
	linuxify,
)
from schnell.app.printutils import print_list_warna
from schnell.app.dirutils import joiner, chdir
from schnell.app.envvalues import schnelldir
from schnell.vendor.upython import main as upypthon
from constants import GOOGLESEARCH
from startup import buka

list_startswiths = [
	'.D',
	'g/',
	'l ',
	':',
	'|',
	'img',
	# 'lang',
	'repl',
	'wmc',
	'backup',
	'calendar',
	'features',
	'gitor', # editor + git
	'gitail', # git detail (issues, pr)	
	'inter.',
	'lalang',
	'micro',
	'sched.',
	'qt.',
]


def run_discordo(command = 'go run main.go'):
	discodir = joiner(schnelldir(), 'vendor', 'discordo')
	perintahsp_simple_chdir(command, discodir)


def run_acdsee():

	# https://stackoverflow.com/questions/49123439/python-how-to-run-process-in-detached-mode
	from schnell.gui.acdsee.acdsee import main

	lokasi = joiner(env_get('ULIBPY_BASEDIR'), 'gui/acdsee')
	sys.path.append(lokasi)
	p = Process(target=main)
	p.daemon = True
	p.start()
	# print('[creator.repl_language][run_clock] done')


def run_clock():
	# https://stackoverflow.com/questions/49123439/python-how-to-run-process-in-detached-mode
	from schnell.gui.clock.clock import main
	lokasi = joiner(env_get('ULIBPY_BASEDIR'), 'gui/clock')
	sys.path.append(lokasi)
	p = Process(target=main)
	p.daemon = True
	p.start()
	# print('[creator.repl_language][run_clock] done')


banner = r"""
uuuuuu    uuuuuu  ppppp   ppppppppp   yyyyyyy           yyyyyyy
u::::u    u::::u  p::::ppp:::::::::p   y:::::y         y:::::y 
u::::u    u::::u  p:::::::::::::::::p   y:::::y       y:::::y  
u::::u    u::::u  pp::::::ppppp::::::p   y:::::y     y:::::y   
u::::u    u::::u   p:::::p     p:::::p    y:::::y   y:::::y    
u::::u    u::::u   p:::::p     p:::::p     y:::::y y:::::y     
u::::u    u::::u   p:::::p     p:::::p      y:::::y:::::y      
u:::::uuuu:::::u   p:::::p    p::::::p       y:::::::::y       
u:::::::::::::::uu p:::::ppppp:::::::p        y:::::::y        
 u:::::::::::::::u p::::::::::::::::p          y:::::y         
  uu::::::::uu:::u p::::::::::::::pp          y:::::y          
	uuuuuuuu  uuuu p::::::pppppppp           y:::::y           
				   p:::::p                  y:::::y            
				   p:::::p                 y:::::y             
				  p:::::::p               y:::::y              
				  p:::::::p              y:::::y               
				  p:::::::p             yyyyyyy                
				  ppppppppp
"""


def wrap_upy():
	"""
	agar bisa dibaca di upy...
	>>> mynumber
	42
	>>> __file__
	'C:\\Users\\usef\\work\\sidoarjo\\schnell\\interactive\\dummy.py'
	>>>
	"""
	import os
	upy_loaded_file = 'interactive/upy.py' # asumsikan kita berada di schnell...otherwise hrs manual
	upy_loaded_file = os.path.join(schnelldir(), upy_loaded_file)
	print(f"""[wrap_upy]
	schnelldir = {schnelldir()}
	upy_loaded_file = {upy_loaded_file}
	""")
	__file__ = upy_loaded_file
	with open(upy_loaded_file) as fd:
		exec(fd.read())
	upypthon(banner=banner, locals_=locals())


def run_qute():
	import subprocess, threading
	program = joiner(env_get('ULIBPY_BASEDIR'), 'vendor/browser/qute.py')
	x = threading.Thread(target=subprocess.run, kwargs={'args':f'python {program}'.split()})
	x.start()


def run_flix():
	import subprocess, threading
	program = joiner(env_get('ULIBPY_BASEDIR'), 'gui/system/searcher/widgets/flix.py')
	x = threading.Thread(target=subprocess.run, kwargs={'args':f'python {program}'.split()})
	x.start()


list_equals = {
	'acdsee': run_acdsee,
	'clock': run_clock,
	'disco': run_discordo, # mending disco
	'qute': run_qute,
	'upy': wrap_upy,
	'flix': run_flix,
}


def run_gui(main_func, gui_folder, args=None):
	lokasi = joiner(env_get('ULIBPY_BASEDIR'), gui_folder)
	sys.path.append(lokasi)
	if args:
		print("args:", args)
		p = Process(target=main_func, args=args)
	else:
		p = Process(target=main_func)
	p.daemon = True
	p.start()


def run_blocking(main_func, gui_folder, args=None):
	lokasi = joiner(env_get('ULIBPY_BASEDIR'), gui_folder)
	sys.path.append(lokasi)
	if args:
		main_func(args)
	else:
		main_func()


def handled_by_repl(text):
	"""
	belum digunakan
	agar repl.py bisa panggil fungsi ini saja alih2 cek if ... sendiri
	"""
	return any([text.startswith(item) for item in list_startswiths]) \
		or any([text == item for item in list_equals.keys()])
		# or any([text == item for item in list_equals])


def repl_service(text):

	if text.startswith('features'):
		code = text.removeprefix('features').strip()
		if code:
			# code = code.removeprefix('|').strip()
			features(code)
		else:
			features()

	elif text.startswith('lalang'):
		code = text.removeprefix('lalang').strip()
		if code:
			# code = code.removeprefix('|').strip()
			lalang(code)
		else:
			lalang()

	elif text.startswith('gitor'):
		code = text.removeprefix('gitor').strip()
		if code:
			# code = code.removeprefix('|').strip()
			gitor(code)
		else:
			gitor()

	elif text.startswith('gitail'):
		code = text.removeprefix('gitail').strip()
		if code:
			git_detail(code)

	elif text .startswith(':'):
		from schnell.app.executor import LANGUAGES, ExecFile, FileExecutor
		code = text.replace(':', '', 1).strip()
		if code:
			if code in LANGUAGES:
				# ExecFile.exec(code)
				FileExecutor().exec(code)

	elif text .startswith('|'):
		'''
		print latest file spt di vscode dan fast
		'''
		from schnell.creator.repl_help import latest_file_handler
		latest_file_handler(text)

	elif text.startswith('.D'):
		code = text.removeprefix('.D')
		from schnell.creator.repl_docker import repl_docker
		repl_docker(code)

	elif text .startswith('l '):
		code = text.replace('l ', '', 1).strip()
		from schnell.app.utils import Launcher
		Launcher.launch(code)

	elif text.startswith('g/'):
		code = text.removeprefix('g/').strip()
		__TEXTPLACEHOLDER__ = code.replace(' ', '+')
		alamat = GOOGLESEARCH.replace('__TEXTPLACEHOLDER__', __TEXTPLACEHOLDER__)
		buka(alamat)

	elif text .startswith('img'):
		from schnell.creator.imghandler import imghandler
		imghandler(text)

	# elif text .startswith ('lang'):
	# 	from schnell.creator.repl_help import lang_helper
	# 	lang_helper(text, self.langsdir, self.config.run_configuration)

	elif text .startswith('repl'):
		'''
		repl* -> code <file/folder>
		'''
		from schnell.creator.repl_help import repl_handler
		repl_handler(text)

	# elif text .startswith ('wmc'):
	# 	'''
	# 	bisa edit wmc.py dan fmus.py lewat wmc* dan wmc**
	# 	tambah: .env -> wmc***
	# 	'''
	# 	code = text.removeprefix('wmc')
	# 	from schnell.creator.repl_help import wmc_handler
	# 	wmc_handler(text, code if code else self.langsdir)

	elif text .startswith ('wmc'):
		'''
		bisa edit wmc.py dan fmus.py lewat wmc* dan wmc**
		tambah: .env -> wmc***
		'''
		# code = text.removeprefix('wmc')
		from schnell.creator.repl_help import wmc_handler
		# wmc_handler(text, code if code else self.langsdir)
		wmc_handler(text)

	# elif text.startswith('history'):
	# 	code = text.removeprefix('history').strip()
	# 	if code:
	# 		git_detail(code)
	# 	else:
	# 		# https://stackoverflow.com/questions/56944869/python-reversed-function-return-object-with-list-function-doesnt-work-well
	# 		sejarah = list(self.our_history.load_history_strings())
	# 		balik = sejarah[::-1]
	# 		print_list_warna(balik)

	elif text.startswith('calendar'):
		from schnell.app.datetimeutils import waktu
		from .repl_calendar import repl_calendar
		code = text.removeprefix('calendar').strip()
		if code:
			# git_detail(code)
			tahun = waktu('year')
			if code:
				tahun = code
			repl_calendar(tahun)

	elif text.startswith('backup'):
		from schnell.app.fileutils import backup_ulib_history, backup_file
		zhelpdir = joiner(env_get('ULIBPY_ROOTDIR'), 'database/zhelps')
		code = text.removeprefix('backup').strip()
		if code == 'hist' or code == 'history':
			backup_ulib_history()
		elif code == 'idea':
			ideafile = joiner(zhelpdir, 'IDEA')
			backup_file(ideafile)
		elif code == 'todo':
			ideafile = joiner(zhelpdir, 'TODO')
			backup_file(ideafile)
		elif code == 'help':
			ideafile = joiner(zhelpdir, 'HELP')
			backup_file(ideafile)
		elif code == 'diary':
			ideafile = joiner(zhelpdir, 'DIARY')
			backup_file(ideafile)

	elif text.startswith('micro'):
		'''
		TODO:
		bisa open/baca/tulis file dari dalam repl
		'''
		code = text.removeprefix('micro').strip()
		# microdir = joiner(schnelldir(), 'vendor/micro/micro')
		# if is_windows:
		# 	microdir = linuxify(microdir)
		# 	perintah_shell(f'wsl {microdir}')
		from schnell.app.utils import micro
		if code:
			micro(code)
		else:
			micro()

	elif text.startswith('inter.'):
		from schnell.interactive import run_simple, run_schnell
		code = text.removeprefix('inter.').strip()
		if code:
			if code == 'simple':
				run_simple()
			elif code == 'schnell':
				run_schnell()

	elif text.startswith('sched.'):
		from schnell.app.schedulerutils import handle_scheduler
		code = text.removeprefix('sched.').strip()
		if code:
			handle_scheduler(code)

	elif text.startswith('qt.'):
		'''
		qt.dialog
		qt.notif
		'''
		code = text.removeprefix('qt.').strip()
		if code:
			if code == 'dialog':
				from schnell.gui.misc.dialog_frameless import main
				run_gui(main, 'gui/misc')
			elif code in ['B', 'buttons', 'button', 'font', 'fonts']:
				from schnell.gui.misc.buttons import main
				run_gui(main, 'gui/misc')
			elif code in ['C', 'clock']:
				from schnell.gui.primitives.noticontainer import main
				run_gui(main, 'gui/primitives')
			elif code in ['clr', 'color']:
				from schnell.gui.misc.color_picker import main
				run_blocking(main, 'gui/misc')
			elif code in ['e', 'edit', 'editor']:
				from schnell.gui.system.editor.editor import main
				# run_gui(main, 'gui/system/editor')
				run_blocking(main, 'gui/system/editor')
			elif code .startswith('g '):
				cmd = code.removeprefix('g ').strip()
				if cmd == 'repoall':
					from schnell.gui.system.launcher.helper.repoall import main
					run_gui(main, 'gui/system/launcher/helper')
				elif cmd == 'gistall':
					from schnell.gui.system.launcher.helper.gistall import main
					run_gui(main, 'gui/system/launcher/helper')
				elif cmd == 'issue':
					from schnell.gui.system.launcher.helper.issue import main
					run_gui(main, 'gui/system/launcher/helper')
				elif cmd == 'pull':
					from schnell.gui.system.launcher.helper.pullrequest import main
					run_gui(main, 'gui/system/launcher/helper')
			elif code in ['h', 'help', 'he', 'hr', 'hg'] or code .startswith('h '):
				from schnell.gui.system.help.helper import main
				from schnell.app.envvalues import dirjoiner, sidoarjo, schnelldir
				if code == 'he':
					filepath = dirjoiner(schnelldir(), 'gui/system/help/README.md')
					perintah_shell(f'code {filepath}')
				elif code == 'hr':
					# baca refcards
					filepath = dirjoiner(sidoarjo(), 'database/refcards/capcay.mk')
					# print(f'opening {filepath}')
					perintah_shell(f'code {filepath}')
				elif code == 'hg':
					filepath = dirjoiner(sidoarjo(), 'data/github/README.md')
					perintah_shell(f'code {filepath}')
				else:
					if code .startswith('h '):
						code = code.removeprefix('h ').strip()
						if code:
							run_blocking(main, 'gui/system/help', code)
					else:
						# run_gui(main, 'gui/system/help')
						run_blocking(main, 'gui/system/help')
			elif code .startswith('ie'):
				from schnell.gui.misc.ie import main
				alamat = code.removeprefix('ie').strip()
				if alamat:
					if not alamat.startswith('http'):
						alamat = 'https://' + alamat
						# print('IE alamat:', alamat)
					run_gui(main, 'gui/misc', args=(alamat,))
				else:
					run_gui(main, 'gui/misc')
			elif code in ['l', 'launch', 'launcher']:
				from schnell.gui.system.launcher.launcher import main
				run_gui(main, 'gui/system/launcher')
			elif code in ['m', 'mmm']:
				from schnell.gui.system.launcher.mmm import main
				run_gui(main, 'gui/system/launcher')
			elif code == 'notif':
				from schnell.gui.misc.notif import main
				run_gui(main, 'gui/misc')
			elif code == 'pdf':
				from schnell.gui.misc.pdf import main
				run_gui(main, 'gui/misc')
			elif code == 's':
				from schnell.gui.system.searcher.searcher import main
				run_gui(main, 'gui/system/searcher')
			elif code == 'so' or code.startswith('so '):
				'''
				todo
				bisa 2 args:
				qt.so 2
					page 2
				qt.so python 5
					tag python page 5
				qt.so rust
					tag rust
				'''
				from schnell.gui.primitives.notabner import main
				if code.startswith('so '):
					args = code.removeprefix('so ').strip()
					# run_gui(main, 'gui/primitives', tuple(args.split()))
					run_gui(main, 'gui/primitives', (args,))
				else:
					run_gui(main, 'gui/primitives')
			elif code in ['v', 'video']:
				from schnell.gui.misc.videoplayer import main
				run_gui(main, 'gui/misc')
			elif code in ['w', 'w2f']:
				from schnell.gui.system.windower.windower import main
				run_gui(main, 'gui/system/windower')
			elif code == '?':
				from schnell.app.printutils import indah4
				indah4("""
qt.dialog
qt.C/clock
qt.clr/color
qt.e/edit/editor
qt.h/help
qt.ie url
qt.l/launch/launcher
qt.notif
qt.pdf
qt.so tag page
qt.v/video
qt.w2f
				""", warna='white', layar='blue')

	elif text in list_equals.keys():
		list_equals[text] () # discordo, no args
