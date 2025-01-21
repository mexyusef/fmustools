import os, sys, time
from multiprocessing import Process
from dotenv import load_dotenv

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent)
sys.path.append(sidoarjodir)

from constants import sidoarjodir, schnelldir
from startup import initialize_programming_data
from schnell.app.appconfig import programming_data
from schnell.creator.repl_language.ocr import ocr
from schnell.gui.system.searcher.common import ULIBPY_BASEDIR
from schnell.db.myredis import redis_config
from schnell.db.myredis_extension import subscribe_header, redis_subscribe_getmessage
from schnell.app.utils import Launcher


def run_gui(main_func, gui_folder, args=None):
	lokasi = os.path.join(ULIBPY_BASEDIR, gui_folder)
	sys.path.append(lokasi)
	if args:
		print("args:", args)
		p = Process(target=main_func, args=args)
	else:
		p = Process(target=main_func)
	p.daemon = True
	p.start()


def run_blocking(main_func, gui_folder, args=None):
	lokasi = os.path.join(ULIBPY_BASEDIR, gui_folder)
	sys.path.append(lokasi)
	if args:
		main_func(args)
	else:
		main_func()


def run_os_system(app_filepath):
	lokasi = os.path.join(ULIBPY_BASEDIR, app_filepath)
	os.system(f'python {lokasi}')


class ServerSearchThread(QThread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.channel = redis_config['request_kanal']
		# try_redis_connect()
		# perlu load dulu .env, klo gak, bermasalah dg get definition etc
		load_dotenv(os.path.join(schnelldir, '.env'))

		self.printer = None
		# 'from_client'		: 'ulang',
		self.channel = redis_config['from_client'] # search channel
		self.pubsub = subscribe_header(self.channel)

	def setPrinter(self, printer):
		if printer:
			self.printer = printer

	def run(self):
		print('ServerSearchThread id', QThread.currentThread())
		# i = 0
		while not self.isInterruptionRequested():
			# masalahnya ini blocking...jadi gak bisa distop, harus pake .get_message() bukan .listen()
			# redis_subscribe(self.channel, redis_config['r'])
			redis_subscribe_getmessage(self.channel, self.pubsub, self.printer)
			time.sleep(0.001)
			# QThread.msleep(500)
		if self.printer:
			self.printer('ServerSearchThread "ulang" quit.')


class ServerCommandThread(QThread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.channel = redis_config['request_kanal']
		# try_redis_connect()
		# perlu load dulu .env, klo gak, bermasalah dg get definition etc		
		load_dotenv(os.path.join(schnelldir, '.env'))

		self.printer = None
		self.channel = redis_config['request_kanal']
		self.pubsub = subscribe_header(self.channel)

	def setPrinter(self, printer):
		if printer:
			self.printer = printer

	def run(self):
		"""
		ServerCommandThread id <menu_runner.ServerCommandThread object at 0x000002222D8EDBD0>
		QObject::connect: Cannot queue arguments of type 'QTextCursor'
		(Make sure 'QTextCursor' is registered using qRegisterMetaType().)
		"""
		print('ServerCommandThread id', QThread.currentThread())
		# i = 0
		while not self.isInterruptionRequested():
			# masalahnya ini blocking...jadi gak bisa distop, harus pake .get_message() bukan .listen()
			# redis_subscribe(self.channel, redis_config['r'])
			redis_subscribe_getmessage(self.channel, self.pubsub, self.printer)
			time.sleep(0.001)
			# QThread.msleep(500)
		if self.printer:
			self.printer('ServerCommandThread "replservice_request" quit.')


class ServerForCreatorService(QThread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.channel = redis_config['request_kanal']
		# try_redis_connect()
		# perlu load dulu .env, klo gak, bermasalah dg get definition etc
		from dotenv import load_dotenv
		load_dotenv(os.path.join(schnelldir, '.env'))

		self.printer = None
		self.channel1 = 'service_creator_request'
		# self.channel2 = redis_config['request_kanal']
		self.pubsub1 = subscribe_header(self.channel1)
		# self.pubsub2 = subscribe_header(self.channel2)

	def setPrinter(self, printer):
		if printer:
			self.printer = printer

	def run(self):
		"""
		ServerCommandThread id <menu_runner.ServerCommandThread object at 0x000002222D8EDBD0>
		QObject::connect: Cannot queue arguments of type 'QTextCursor'
		(Make sure 'QTextCursor' is registered using qRegisterMetaType().)
		"""
		print('ServerForCreatorService id', QThread.currentThread())
		# i = 0
		while not self.isInterruptionRequested():
			# masalahnya ini blocking...jadi gak bisa distop, harus pake .get_message() bukan .listen()
			# redis_subscribe(self.channel, redis_config['r'])
			redis_subscribe_getmessage(self.channel1, self.pubsub1, self.printer, reply_channel='service_creator_response')
			# redis_subscribe_getmessage(self.channel2, self.pubsub2, self.printer)
			time.sleep(0.001)
			# QThread.msleep(500)
		if self.printer:
			self.printer('ServerForCreatorService quit.')

server_command_thread = ServerCommandThread()
server_search_thread = ServerSearchThread()
redis_for_creator_thread = ServerForCreatorService()

def running(menu, printer=None):
	if menu in ['m', 'mmm']:
		# daemon process gak boleh punya children, https://github.com/apache/airflow/issues/14896
		# run_gui(mmm_main, 'gui/system/launcher')		
		# event loop sudah jalan
		# run_blocking(mmm_main, 'gui/system/launcher')
		run_os_system('gui/system/launcher/mmm.py')
	elif menu in ['h']:
		run_os_system('gui/system/help/helper.py')
	elif menu in ['ghrepo']:
		run_os_system('gui/system/launcher/helper/repoall.py')
	elif menu in ['ghgist']:
		run_os_system('gui/system/launcher/helper/gistall.py')
	elif menu in ['ghissue']:
		run_os_system('gui/system/launcher/helper/issue.py')
	elif menu in ['ghpull']:
		run_os_system('gui/system/launcher/helper/pullrequest.py')
	elif menu in ['qedit']:
		run_os_system('gui/system/editor/editor.py')
	elif menu in ['tkedit']:
		run_os_system('gui/system/editor/tkeditor.py')
	elif menu in ['S', 'sub']:
		# ini bikin non responding...
		# run_os_system('db/myredis.py')
		print('Starting command server...') # server_search_thread
		server_command_thread.setPrinter(printer)
		server_command_thread.start()
	elif menu in ['stop']:
		print('Stopping command server...')
		server_command_thread.requestInterruption()
		server_command_thread.quit()
	elif menu in ['server_search_start']:
		print('Starting search server...')
		server_search_thread.setPrinter(printer) # ulang
		server_search_thread.start()
	elif menu in ['server_search_stop']:
		print('Stopping search server...')
		server_search_thread.requestInterruption()
		server_search_thread.quit()
	elif menu in ['redis_for_creator_start']:
		print('Starting redis_for_creator_thread...')
		redis_for_creator_thread.setPrinter(printer) # ulang
		redis_for_creator_thread.start()
	elif menu in ['redis_for_creator_stop']:
		print('Stopping redis_for_creator_thread...')
		redis_for_creator_thread.requestInterruption()
		redis_for_creator_thread.quit()
	elif menu in ['ocr']:
		ocr()		
	elif menu in ['ocr_google']:
		ocr(True)
	elif menu .startswith('l '):
		code = menu.removeprefix('l ')
		Launcher.launch(code)
