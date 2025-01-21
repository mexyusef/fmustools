from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

from datetime import datetime
import itertools

# gui.system.searcher.make_redis vs make_redis
# print('ini bakal gagal, lihat siapa name:', __name__)
if __name__ == 'make_repl':
	from common import lcs
	from utils import Query
	from make_redis_help import try_redis_connect, all_redis_keys, redis_config, get_definition_by_key_permissive_start, split_by_pos, redis_publish
	from make_py_help import all_python_files, all_python_files_from_redis
	from make_word_help import get_all_words_in_existing_files_redis, get_definition_byword
	from filehelper import file_content
else:
	from gui.system.searcher.common import lcs
	from gui.system.searcher.utils import Query
	from gui.system.searcher.make_redis_help import try_redis_connect, all_redis_keys, redis_config, get_definition_by_key_permissive_start, split_by_pos, redis_publish
	from gui.system.searcher.make_py_help import all_python_files, all_python_files_from_redis
	from gui.system.searcher.make_word_help import get_all_words_in_existing_files_redis, get_definition_byword
	from gui.system.searcher.filehelper import file_content



class REPLWorker(object):


	def __init__(self, worker):
		self.tasks = {}
		self.mutex = QMutex()
		self.worker = worker
		# self.client = client


	def select(self, content, index):
		return None


	def update_usetime(self, entry):
		pass


	def data_callback_for_select(self, user_query, _data):
		pass


	@property
	def name(self):
		return ',' # \, kan lebih cepat...


	def _refresh_tasks(self, query, _data):
		pass


	def act(self, query):
		"""
		jadi pada dasarnya, jk ngetik ff atau /cari sesuatu itu cuma redis_pusblish query.
		dan pada dasarnya publish ke channel
		dapat jawaban juga dari redis channel, dan selanjutnya ke pyqt signal lalu ke yellownote.
		C:/Users/usef/work/sidoarjo/schnell/db/myredis_extension.py
		berisi kode publish reply, sbb:
		from db.replservice import ReplService, repl_service
		answer, _ = repl_service.process(data)
		redis_publish(answer, response_kanal)
		jadi db.replservice.repl_service adlh pemproses /.clearload, /search dll.


		channel = 'replservice_request'
		redis_config = {
			'from_client'		: 'ulang',
			'from_server'		: 'ulang/fromserver',
			'search_service'	: 'ulang/search_service',
			'mapper_service'	: 'ulang/mapper_service',
			'scheduler'         : 'kanal/scheduler',
			'command'           : 'kanal/command',
			'request_kanal' 	: "replservice_request",
			'response_kanal' 	: "replservice_response",
		}
		menu_runner berisi
		ServerSearchThread
			self.channel = redis_config['from_client']
			redis_subscribe_getmessage(self.channel, self.pubsub, self.printer)
		ServerCommandThread
			self.channel = redis_config['request_kanal']
		ServerForCreatorService
			self.channel1 = 'service_creator_request'

		"""
		print(f'[make_repl] act is being requested for [{query}]...')
		redis_publish(query)


	def lit(self, query, upper_bound, finished, *args, **kargs):
		# print('[make_repl] lit is being requested...')
		# redis_publish(query) # wah jangan nih...why? krn setiap ngetik a, ab, abc, itu 3x lit...
		pass
