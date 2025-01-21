from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from datetime import datetime
import itertools

from common import lcs
from utils import Query
NAME_LIMIT = 60

"""
TODO:
bisa load ke redis db no 8, krn no 7 terlalu banyak entry...
tampilkan hasil di new window...dan juga dong masuk text editor...

gunakan pyqt5keybinding + small taskbar icon utk running in background.
"""


from make_redis_help import try_redis_connect, all_redis_keys, redis_config, get_definition_by_key_permissive_start, split_by_pos
# di awal
try_redis_connect()

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
			return '...' + berkas[10:] + '...' + baris
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
		print(f'berkas {task.berkas}, baris {task.baris}')
		content = get_definition_by_key_permissive_start(task.berkas, task.baris)
		print(content)
		QApplication.quit()

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
		return 'redis'


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
				self.data_callback_for_select(query, all_redis_keys(redis_config['r']))[:upper_bound]
			),
			catch=finished,
			main=True
		)

	# def get_dummy_data(self):
	# 	return data

	def act(self):
		print('redis worker, act dipanggil waktu tekan Enter')

