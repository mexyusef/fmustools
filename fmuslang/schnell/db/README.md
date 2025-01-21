# bgm hubungan myredis.py dan replservice.py?
dimulai dari handle pub sub /S dari <repl>:
if channel:
	redis_subscribe(channel)
else:
	redis_subscribe(redis_config['from_client'])
jadi kuncinya di redis_subscribe
selanjutnya panggil:

ketemu message: {'type': 'message', 'pattern': None, 'channel': b'ulang', 'data': b'{"content":"*!help","meta":{...}}}'}

data = json.loads(message.get('data'))
redis_repl_from_vscode(data)
dan di dalamnya:
if content.startswith('/'):
		code = content.removeprefix('/').strip()
		hasil, meta = redis_repl_search_service(code)
		data = {
			'content': hasil,
			'meta': meta,
			'original': metacontent,
		}
		redis_publish(data, redis_config['search_service'])
elif content .startswith('fastmapper:'): <- ctrl+n di vscode
else
		hasil, meta = repl_service.process(content, meta_input=metacontent)
		data = {
			'content': hasil,
			'meta': meta,
			'original': metacontent,
		}
		redis_publish(data, redis_config['from_server'])

jadi kita tinggal tambah:
if content.startswith(','): utk handle lalang.
			from app.transpiler.lalang import process_language
			code = text.removeprefix(',')
			process_language(code)
kita hrs balikkan hasil proses lalang...dan redis_publish-kan.
# capcay
data: {
	'content': 'fs', 
	'meta': {
		'metaDocument': {
			'filename': 'Untitled-1', 
			'fsPath': 'Untitled-1', 
			'path': 'Untitled-1', 
			'language': 'plaintext'
		}
	}
}

if meta_input:
	docinfo = meta_input['metaDocument']
	filepath = docinfo['filename']
	if isfile(filepath):
data: {
	'content': 'fM', 
	'meta': {
		'metaWorkspacesFspath': ['/tmp/coba'], 
		'metaWorkspacesPath': ['/tmp/coba'], 
		'metaDocument': {
			'filename': '/tmp/coba/main.go', 
			'fsPath': '/tmp/coba/main.go', 	
			'path': '/tmp/coba/main.go', 
			'language': 'go'
		}
	}
}
dg demikian kita bisa:
compile per bahasa
jalankan terminal
jalankan fmus

		elif text .startswith('img'):
			code = text.replace('img', '', 1).strip()						
			if code .startswith('s'):
				'''
				imgs filepath: show image filepath
				   s = show
				'''
				code = code.replace('s', '', 1).strip()
				code = env_expand(code)
				if isfile(code):
					lihat_gambar(code)
			elif code .startswith('c'):
				'''
				capture gambar dg select area, jadikan/masuk ke filename
				imgc filepath
				   c = capture, but not showing
				'''
				code = code.replace('c', '', 1).strip()
				code = env_expand(code)
				if code and isfolder_dir(code):
					filename = code
				else:
					filename = '/tmp/lihat.jpg'
				print('saved screenshot:', filename)
				capture_gambar(filename)
			elif code .startswith('C'):
				'''
				imgC filepath = capture gambar + show hasil
				   C = capture+show
				'''
				code = code.replace('C', '', 1).strip()
				code = env_expand(code)
				print('received imgC:', code)
				if code and isfolder_dir(code):
					filename = code
				else:
					filename = '/tmp/lihat.jpg'
				print('saved screenshot:', filename)
				capture_lihat_gambar(filename)
			elif code .startswith('64'):
				'''
				img64 filepath = capture gambar + kembalikan stringified base64 encoded
				   64 = base64 kan file, ready to put into mk file
				'''
				code = code.replace('64', '', 1).strip()
				code = env_expand(code)
				# code = env_expand_removeprefix(code, '64')
				if code and isfolder_dir(code):
					filename = code
				else:
					filename = '/tmp/lihat.jpg'
				print('saved screenshot:', filename)
				capture_lihat_stringified_image_asb64(filename)
			elif code .startswith('u '):
				'''
				imgu alamat
				   u = from url
				'''
				alamat = code.replace('u ', '', 1).strip()
				if alamat:
					# get_lihat_stringified_image_asb64(alamat)
					requests_get_lihat_stringified_image_asb64(alamat)
			elif isfile(code):
				'''
				img filepath: printclipboard base64 encoded dari image
				'''
				stringified_image_asb64(code)


		elif text .startswith(':'):
			from app.executor import LANGUAGES, ExecFile, FileExecutor
			code = text.replace(':', '', 1).strip()
			if code:
				if code in LANGUAGES:
					# ExecFile.exec(code)
					FileExecutor().exec(code)

		elif text .startswith ('['):
			# mulai scraper
			from app.scrape.scraper import process
			code = text.replace('[','',1).strip()
			if code:
				process(code)
			else:
				print('not scraping...')

import os, sys
# .
curdir = os.getcwd()
# ..
pardir = os.path.abspath(os.pardir)
# ../..
grandpardir = os.path.dirname(pardir)
# ../../..
greatgrandpardir = os.path.dirname(grandpardir)

schnelldir = '/home/usef/danger/ulib/schnell'
sys.path.extend([schnelldir, '..'])

from app.dirutils import (
	ayah, joiner, here, exists_in_dir_bypattern,
  walk_fullpath,
  isfile,
)
from app.fileutils import (
	file_content,
  get_definition_by_key_permissive_start,
  get_definition_double_entry_aware,
  get_daftar
    
)
from app.utils import (
	env_exist, env_get, env_int,
  env_load,
)

from db import (
  redis_connect,
  redis_keys,
  redis_keys_recurse,
  load_bylangs,
  redis_value,
  redis_value_recurse,
)


env_load()
r = redis_connect()

# jk belum ada content di redis
# jk pengen reload utk file baru di filesystem ke redis
load_bylangs(r)

redis_keys(r, 'size*box*height')
redis_value(r, 'size*box*height')
redis_keys_recurse(r, 'crack search matrix q0')
redis_value_recurse(r, 'crack search matrix q0')
