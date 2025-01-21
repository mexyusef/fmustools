import json, redis
from uuid import uuid4
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *


DEFAULT_DB = 8

redis_connection_keys = {}


class RedisSubscriber(QThread):
	"""
	self.subscriber = RedisSubscriber()
	self.subscriber.incoming_data.connect(self.incomingData)
	self.subscriber.start()

	self.quick_subscriber = RedisSubscriber('quicklang_channel', 'quicklang_redisconfig')
	self.quick_subscriber.incoming_data.connect(self.incomingData)
	self.quick_subscriber.start()
	
	def incomingData(self, data):
		# print('[searcher incomingData]', str(data))
		text = str(data)
		self.completer.note.show_and_print(text, self.markdown_mode)
		pyperclip.copy(text)
		resize_screen_ratio(self.completer.viewer, self.screenw, self.screenh,
							posx_ratio=1/2, posy_ratio=0.9, w_ratio=1, h_ratio=0.7)
		self.completer.viewer.show()
		to_top(self.completer.viewer.winId())

	def handle_publish_to_redis(message):
		channel = 'quicklang_channel'

		r = try_redis_connect_return(configkey, db=0)
		r.publish(channel, message.encode())

	"""

	incoming_data = pyqtSignal(object)

	def __init__(self, channel='replservice_response', callback=None, listen_db=0, host='localhost', port=6379, password=None, *args, **kwargs):
		"""
		https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible
		"""
		super(RedisSubscriber, self).__init__(*args, **kwargs)
		self.channel = channel
		# # print('pubsub #1')
		# self.r = get_connection(redis_config_key)
		# # print('pubsub #2')
		# try:
		#   self.pubsub = self.r.pubsub()
		#   # print('pubsub #3')
		# except Exception as err:
		#   print(err)
		self.listen_db = listen_db
		# self.pubsub = get_cached_pubsub(conn=redis_config_key, db=self.listen_db)
		self.callback = callback
		conn_params = {
			'host': host,
			'port': port,
			'db': self.listen_db,
		}
		if password is not None:
			conn_params.update({
				'password': password,
			})

		# r = redis.Redis(**conn_params)

		cache_key = f"{host}/{port}/{listen_db}/{channel}"
		if cache_key in redis_connection_keys and redis_connection_keys[cache_key]:
			r = redis_connection_keys[cache_key]
		else:
			r = redis.Redis(**conn_params)
			redis_connection_keys[cache_key] = r

		self.pubsub = r.pubsub()
		self.pubsub.subscribe(self.channel)

	def run(self):
		"""
		https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible
		.get_message() over .listen()
		"""
		try:
			# print('pubsub #5')
			for message in self.pubsub.listen():

				if message.get('type') == 'message':
					msgdata = message.get('data')

					print(f'[redisguiutils][RedisSubscriber] message = {message}, data = {msgdata}, jenis = {type(msgdata)}\n')

					try:
						data = json.loads(msgdata)
					except:
						data = msgdata

					# print(f'[searcher][RedisSubscriber] data = {data}, jenis = {type(data)}\n')

					if isinstance(data, (bytes, bytearray, str)):
						if not isinstance(data, str):
							data = data.decode('utf8')
						if data in ['quit', 'bye', 'exit', 'q', 'x']:
							return  # perlukah keluar?
						else:
							# tampilkan di self.note, dg emit signal
							if self.callback:
								print(f'[redisguiutils][RedisSubscriber] calling callback for data = {data}.')
								self.callback(data)
							else:
								self.incoming_data.emit(data)
					elif isinstance(data, (dict, list)):
						# jk awalnya dict, handler jadikan json.dumps, di sini kita loads, jadi dict lagi
						# maka jadikan lagi string...
						data = json.dumps(data, indent=4)
						if self.callback:
							self.callback(data)
						else:
							self.incoming_data.emit(data)

		except Exception as err:
			print(err)


image_publish_db = 1
image_publish_channel = 'image_publish_channel'


def redis_subscribe2(channel=image_publish_channel, callback=None, listen_db=image_publish_db, host='localhost', port=6379, password=None):
	subscriber = RedisSubscriber(channel=channel, callback=callback, listen_db=listen_db, host=host, port=port, password=password)
	subscriber.start()


def redis_subscribe(channel = 'quicklang_channel', callback=None, listen_db=0, host='localhost', port=6379, password=None):
	subscriber = RedisSubscriber(channel=channel, callback=callback, listen_db=listen_db, host=host, port=port, password=password)
	subscriber.start()
	return subscriber


def redis_publish(message, channel = 'quicklang_channel', listen_db=0, host='localhost', port=6379, password=None):
	conn_params = {
		'host': host,
		'port': port,
		'db': listen_db,
	}
	if password is not None:
		conn_params.update({
			'password': password,
		})
	cache_key = f"{host}/{port}/{listen_db}/{channel}"
	if cache_key in redis_connection_keys and redis_connection_keys[cache_key]:
		r = redis_connection_keys[cache_key]
	else:
		r = redis.Redis(**conn_params)
		redis_connection_keys[cache_key] = r

	data = message.encode()
	r.publish(channel, data)
	print(f'publishing [{data}] to channel {channel}.')


def redis_publish_image(filepath):
	redis_publish(filepath, image_publish_channel, image_publish_db)


def redis_subscribe_image(callback=None):
	return redis_subscribe(image_publish_channel, listen_db=image_publish_db, callback=callback)
