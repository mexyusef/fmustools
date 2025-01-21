from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from datetime import datetime
import itertools

# gui.system.searcher.make_redis vs make_redis
# print('ini bakal gagal, lihat siapa name:', __name__)
if __name__ == 'make_redis':
	from common import lcs
	from utils import Query
	
	from make_redis_help import try_redis_connect, all_redis_keys, redis_config, get_definition_by_key_permissive_start, split_by_pos
else:
	from schnell.gui.system.searcher.common import lcs
	from schnell.gui.system.searcher.utils import Query
	from schnell.gui.system.searcher.make_redis_help import try_redis_connect, all_redis_keys, redis_config, get_definition_by_key_permissive_start, split_by_pos

NAME_LIMIT = 60

"""
TODO:
bisa load ke redis db no 8, krn no 7 terlalu banyak entry...
tampilkan hasil di new window...dan juga dong masuk text editor...

gunakan pyqt5keybinding + small taskbar icon utk running in background.
"""


# di awal
try:
	try_redis_connect(rconn='r2')
except Exception as err:
	import os, sys, time
	envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
	from dotenv import load_dotenv
	load_dotenv(envfile)
	schnelldir = os.environ['ULIBPY_BASEDIR']
	sys.path.extend([schnelldir, '..'])
	from schnell.app.windowsutils import hide_window,create_register_commandprompt as c,ketik_by_index as ki,fill_in_hwnds as fill,cmd_register_list as l,get_command_prompt_data_index_from_uuidtitle,get_hwnd_from_uuidtitle
	from schnell.app.autoutils import alert
	id = c()
	fill()
	l() # print
	# cek id ada
	index_or_none = get_command_prompt_data_index_from_uuidtitle(id)
	if not index_or_none:
		print(f'ERR...please fill secara manual! karena get_command_prompt_data_index_from_uuidtitle({id}) masih kosong...')
	else:
		hwnd = get_hwnd_from_uuidtitle(id)
		while not hwnd:
			fill()
			time.sleep(0.5)
			hwnd = get_hwnd_from_uuidtitle(id)
	ki(1, 'wsl')
	time.sleep(1.5)
	ki(1, 'SSD')
	# alert('silahkan isi dulu password...lalu tekan OK utk lanjutkan', 'enter password')
	time.sleep(0.5)
	ki(1, 'docker start fmus')
	input('Press Enter utk coba konek lagi ke redis>> ')
	# alert('press to hide terminal...', 'press to continue')
	window_handle = get_hwnd_from_uuidtitle(id)
	if window_handle:
		hide_window(window_handle)
	try_redis_connect(rconn='r2')


class Task(object):

	def __init__(self, entry, query, usetime):
		# print(f'START: selesai buat task...utk item {entry}')
		self.entry = entry
		self.query = query # Query dibuat utk popup mendekati yg diminta
		self.usetime = usetime
		self.path_windows = False
		if self.entry.lower().startswith("c:"):
			self.path_windows = True

	def split(self):
		if self.path_windows:
			# berkas, baris = self.entry.split(':', 1)
			berkas, baris = split_by_pos(self.entry, ':', 2)
		else:
			berkas, baris = self.entry.split(':', 1)
		return berkas, baris

	def use(self):
		self.usetime = datetime.now()

	@property
	def full_name(self):
		return self.entry

	@property
	def berkas(self):
		berkas, baris = self.split()
		return berkas


	@property
	def baris(self):
		berkas, baris = self.split()
		return baris

	@property
	def name(self):
		# print('terima:', self.entry)
		if ':' in self.entry:
			berkas, baris = self.split()
			return '...' + berkas[10:] + ' | ' + baris
		return self.entry

	@property
	def digest(self):
		# if len(self.name) > NAME_LIMIT:
		# 	# shortname = self.name[:NAME_LIMIT - 3] + '...'
		# 	# shortname = '...' + self.name[NAME_LIMIT - 3:] # dari belakang/kanan
		# 	shortname = self.name
		# else:
		# 	shortname = self.name
		# return shortname
		return self.name


class WindowModel(QAbstractListModel):

	NAME_ROLE = Qt.DisplayRole
	HWND_ROLE = Qt.UserRole

	def __init__(self, items):
		self.super.__init__()
		self.items = items
		# print('WindowModel init menerima items', items)

	@property
	def super(self):
		return super(WindowModel, self)

	def rowCount(self, parent):
		return len(self.items)

	def columnCount(self, parent):
		return 1

	def data(self, index, role=Qt.UserRole):
		# print('make redis, asking data:', index.row())
		if not index.isValid():
			# print('index not valid')
			return None
		if role == Qt.TextAlignmentRole:
			return int(Qt.AlignLeft | Qt.AlignVCenter)
		elif role == Qt.DisplayRole:
			# ternyata ini yg dipake olhe popup, jd hrs ada prop "digest" di task
			return self.items[index.row()].digest 
		# elif role == Qt.DecorationRole:
		# 	return self.items[index.row()].icon
		elif role == Qt.UserRole:
			return self.items[index.row()].name
		else:
			return None


class RedisWorker(object):

	def __init__(self, worker):
		self.tasks = {}
		self.mutex = QMutex()
		self.worker = worker
		# self.client = client
	
	def select(self, content, index):
		# self.completer.activated[QModelIndex].connect(self.select)
		# def select(self, index): self.plugins[cmd].select(content=self.completer.content, index=index)
		# if content.data(index, WindowModel.HWND_ROLE) == hwnd:
		task = content.items[index.row()]
		# print(f'[make_redis][select] berkas {task.berkas}, baris {task.baris}')
		content = get_definition_by_key_permissive_start(task.berkas, task.baris)
		# print(content)
		# QApplication.quit()
		return content

	def update_usetime(self, entry):
		"""Update with one time delay."""
		if hasattr(self, 'after_select') and self.after_select:
			self.after_select()
		self.after_select = self.tasks[entry].use

	def data_callback_for_select(self, user_query, _data):
		with QMutexLocker(self.mutex):
			self._refresh_tasks(user_query, _data)
			active_tasks = [self.tasks[h] for h in _data]
			if not user_query:
				return sorted(active_tasks, key=lambda t: t.usetime, reverse=True)
			# field name pada Task utk indexing/choosing
			titles = [task.name.lower() for task in active_tasks] # ut list of string, task = string
			def f(task, title):
				return task.query.distance_to(title)
			ds = [f(task, title) * (10 ** len(user_query)) for task, title in zip(active_tasks, titles)]
			best = ds[0]
			for i in itertools.takewhile(lambda i: ds[i] == best, range(len(ds))):
				ds[i] -= len(lcs(user_query, titles[i]))
			return [task for i, task in sorted(enumerate(active_tasks), key=lambda i: ds[i[0]])]


	@property
	def name(self):
		return 'R'


	def _refresh_tasks(self, query, _data):
		for item in _data:
			# print(f'_refresh_tasks [{item}] task skrg [{self.tasks}] pada data:', _data)
			if item not in self.tasks:
				# print("[not in tasks] refresh item:", item)
				item_query = Query(
					text='' if query is None else query,
					insertion_cost=1,
					first_insertion_cost=50,
					prepend_first_insertion_cost=5,
					append_first_insertion_cost=10,
					deletion_cost=100,
					substitution_cost=100,
					transposition_cost=10
				)
				# print("[not in tasks] selesai buat query:", item_query)
				try:
					self.tasks[item] = Task(
						entry = item, 
						query=item_query, 
						usetime=datetime.now()
					)
				except Exception as err:
					import traceback					
					print('gagal buat Task:', err)
					print(traceback.format_exc())
				# print(f'    _refresh_tasks [{item}] task skrg [{self.tasks}]\n\n')
			elif not (query is None):
				# print("[update task] refresh item:", item)
				# hitung jarak task ke user query
				self.tasks[item].query.update(query.lower())
			# else:
			#     print("[else] refresh item:", item)


	def lit(self, query, upper_bound, finished, *args, **kargs):
		self.worker.do(
			# make=self.get_dummy_data,
			make=lambda: WindowModel(
				# self.data_callback_for_select(query, data)[:upper_bound]
				self.data_callback_for_select(query, all_redis_keys(redis_config['r2'])) [:upper_bound]
			),
			catch=finished,
			main=True
		)

	# def get_dummy_data(self):
	# 	return data

	def act(self):
		print('[make_redis][act] redis worker, act dipanggil waktu tekan Enter')

