--% getting started
ayo pahami dg baik.
request searcher dihandle oleh make_runner servers...
--#

--% make_redis_help
```
def redis_publish(data, channel=None, r=None):
	"""
	digunakan oleh make_repl utk ngirim request repl_service ke kbrepl
	"""
	if not channel:
		channel = 'replservice_request'
	if not r:
		r = get_connection('pub') # redis_config['pub]

	r.publish(channel, json.dumps(data))
```
--#

--% make_repl
```
from make_redis_help import (try_redis_connect, all_redis_keys, redis_config, get_definition_by_key_permissive_start, split_by_pos, 
    redis_publish)

class REPLWorker(object):

    def act(self, query):
        print(f'[make_repl] act is being requested for [{query}]...')
        redis_publish(query)
```
--#

--% make_runner
```
def running(menu, printer=None):
    elif menu in ['S', 'sub']:
        # ini bikin non responding...
        # run_os_system('db/myredis.py')
        print('Starting command server...') # server_search_thread
        server_command_thread.setPrinter(printer)
        server_command_thread.start()

    elif menu in ['server_search_start']:
        print('Starting search server...')
        server_search_thread.setPrinter(printer) # ulang
        server_search_thread.start()
```

```
class ServerSearchThread(QThread):
    self.channel = redis_config['from_client'] # search channel
    def run(self):
        print('ServerSearchThread id', QThread.currentThread())
        # i = 0
        while not self.isInterruptionRequested():
            # masalahnya ini blocking...jadi gak bisa distop, harus pake .get_message() bukan .listen()
            # redis_subscribe(self.channel, redis_config['r'])
            redis_subscribe_getmessage(self.channel, self.pubsub, self.printer)
            time.sleep(0.001)
```

```
class ServerCommandThread(QThread):
    self.channel = redis_config['request_kanal']
    def run(self):
        print('ServerCommandThread id', QThread.currentThread())
        while not self.isInterruptionRequested():
            redis_subscribe_getmessage(self.channel, self.pubsub, self.printer)
            time.sleep(0.001)
```

input di handle dg:
`from db.myredis_extension import redis_subscribe_getmessage`
dimana kita lihat:
```
# jadi semua input dg kanal berbeda2, outputnya di kanal yg sama ??? bukannya kurang bagus?
response_kanal = redis_config['response_kanal'] # searcher hrs mendengar di sini
answer, _ = repl_service.process(data)
redis_publish(answer, response_kanal)
```

kita lihat `repl_service.process(data)` di `db.replservice`
bagaimana dia bisa handle terutama f12 yg pegang state "lineno".
```
elif text == 'f12':
    indah4(f'[db.replservice] oprek f12 => [{self.last_file}]', warna='magenta')
    from app.utils import vscode_edit_at_line
    if self.last_file and isfile(self.last_file):
        vscode_edit_at_line(self.last_file, self.last_lineno)
elif text.startswith('/'): # handle search
    from .redis_repl_search_service import redis_repl_search_service
    code = text.removeprefix('/').strip()
    hasil, meta = redis_repl_search_service(code)
    self.output += hasil
else: # handle ulang/program/ff/whatever namanya.
    self.run_program(text)

```
di sini dia bergantung pada `self.last_lineno`.
utk `ff` dsb yg dihandle oleh `generate_file(self, generate_fmus=True)` memang terset.
tp gimana dg search?

kita ubah signature
`def redis_repl_search_service(code)`
menjadi
`def redis_repl_search_service(code, REPL = None)`
```
elif text.startswith('/'):
from .redis_repl_search_service import redis_repl_search_service
code = text.removeprefix('/').strip()
hasil, meta = redis_repl_search_service(code) # ubah jadi (code, self)
self.output += hasil
```
--#
