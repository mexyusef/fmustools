import pickle
import threading

from .utils import platform
if platform() not in ['termux']:
  from multiprocessing.connection import Client
  from multiprocessing.connection import Listener

from .serial import serialize, deserialize

def start_simple_server(port, host='localhost', secret=b'rahasia'):
  address = (host, port)
  listener = Listener(address, authkey=secret)
  conn = listener.accept()
  while True:
    data = conn.recv()
    msg = deserialize(data)
    if msg == 'close':
      conn.close()
      break

  listener.close()

def start_simple_server_thread(port, host='localhost', secret=b'rahasia'):
  threading.Thread(target=start_simple_server, args=(host, port, secret)).start()


def create_simple_client(port, host='localhost', secret=b'rahasia'):
  address = (host, port)
  client = Client(address, authkey=secret)
  return client

def client_send(client, msg):
  data = serialize(msg)
  client.send(data)

class RPCProxy():
  def __init__(self, connection):
    self._connection = connection

  def __getattr__(self, name):
    def do_rpc(*args, **kwargs):
      self._connection.send(pickle.dumps((name, args, kwargs)))
      result = pickle.loads(self._connection.recv())
      if isinstance(result, Exception):
        raise result
      return result
    return do_rpc

class RPCHandler:
  """
  idenya adlh semua fungsi masukkan ke dict
  dan di-key dg func.__name__
  jd client hanya tau/share func.__name__ saja
  """
  def __init__(self):
    self._functions = {}

  def register_function(self, func):
    # print('registering name:', func.__name__)
    self._functions[func.__name__] = func

  def handle_connection(self, connection):
    try:
      while True:
        func_name, args, kwargs = pickle.loads(connection.recv())
        try:
          r = self._functions[func_name](*args, **kwargs)
          connection.send(pickle.dumps(r))
        except Exception as e:
          connection.send(pickle.dumps(e))
    except EOFError:
      pass

def rpc_server(rpc_handler, address, authkey):
  sock = Listener(address, authkey=authkey)
  while True:
    client = sock.accept()
    t = threading.Thread(target=rpc_handler.handle_connection, args=(client,))
    t.daemon = True
    t.start()

def status():
  message = 'server is alive'
  return message

def create_rpc_handler():
  handler = RPCHandler()

  handler.register_function(status)

  return handler

default_address = '0.0.0.0'
default_port = 17000
default_auth = b'rahasia'

def start_client(port=default_port, host=default_address, password=default_auth):
  c = Client((host, port), authkey=password)
  p = RPCProxy(c)
  return p

def start_server(rpc_handler, port=default_port, host=default_address, password=default_auth):
  # print ('RPC Server listening on %s:%d' % (host,port))
  rpc_server(rpc_handler, (host, port), authkey=password)

