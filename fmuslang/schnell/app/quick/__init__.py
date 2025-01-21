import datetime, json, os, re, sys, traceback
import schnell.vendor.lark as lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)
from schnell.vendor.lark.indenter import Indenter

# schnelldir = '/home/usef/work/ulibs/schnell'
app_quick = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
schnelldir = os.path.join(app_quick, '../..')
sidoarjodir = os.path.join(schnelldir, os.pardir)
ciledugdir = r'c:\work\ciledug'
sys.path.extend([sidoarjodir, ciledugdir, schnelldir, '..'])

from perintah import perintah as process_perintah
from schnell.app.autoutils import alert, gugu_type, sample_pandas_code
from schnell.app.dirutils import (
	joiner,
	ayah,
	walk_fullpath,
	isfile, sdirs, sfiles,
	isabsolute,
	is_valid_path,
	walk_fullpath_skipdirs,
	walk_fulldirs,
	bongkar,
	isdir,
	bongkar_ulibpy
)
from schnell.app.fileutils import get_definition_by_key_permissive_start, file_content, mkfile_entry
# from schnell.app.fmus import Fmus
from schnell.app.fmusutils import fmus, filepath_samadengan_barisentry, replace_from_configuration_replacer, get_input_from_user_gui
from schnell.app.fmusutils import run_fmus_for_file
from schnell.app.fmusutils import reverse_folder, reverse_folder_onlydirs
from schnell.app.printutils import indah4, indah3
from schnell.app.redisutils import handle_publish_to_redis
from schnell.app.searchutils import word_content_search, system_find, pattern_search_list
from schnell.app.stringutils import sanitize_chars, split_safe_quote
from schnell.app.systemutils import execute_command, execute_command2, grep_text, find_files
from schnell.app.treeutils import (
	child,
	child1,
	anak,
	jumlahanak,
	beranak,
	data,
	token,
	chtoken,
	chdata,
)
from schnell.app.utils import (
	trycopy, env_exist, env_reload, env_set,
	env_int, env_get, platform,
	wslify,
	linuxify,
	trypaste,
	perintahsp_simple,
)
from schnell.app.wcmderutils import create_cmd_and_type_away


from .bahasa import bahasa as quick_bahasa
from .fileops import fileops
from .quick_statement import quick_statement
from .statement_config import statement_config

from .common import program_config
from .common import folder_expand
from .scraper import scraper
from .selena import selena
from .notebook import notebook
from .reflect import panggil
from .crunner import crunner
from .crunner import lister
from .crunner import filers
from .crunner import treelers
from .crunner import fmusrunner
from schnell.app.devoputils.packagejsonutils import retrieve_and_print_json
from schnell.app.appconfig import programming_data
skipdirs=['.git', '__pycache__', 'node_modules']
# fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))
# BLITZ_PREFIX = 'b>'
BLITZ_PREFIX = 'b)'


def handler(tree):
	"""
	statement
		statement_config
			statement_config_list
				fe_react_light
		quick_statement
			program_backend     satu
		frontend_statement
			program_frontend    dua
	"""
	# print('handler:', data(tree))
	# print(tree.pretty())

	kembali = ''	
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'statement_config':
			res = statement_config(item)
			program_config.update(res)
		elif jenis == 'quick_statement':
			res = quick_statement(item)
			program_config.update(res)
		# elif jenis == 'csv_statement':
		# 	res = csv_statement(item)
		# 	program_config.update(res)
		# elif jenis == 'frontend_statement':
		# 	'''
		# 	F: frontend_config => program_config
		# 	'''
		# 	res = frontend_statement(item)
		# 	program_config.update(res)

	# cek apa perlu jalankan fmus: {'config': {'fmus': 'execute'}}
	# print('cek apa perlu jalankan fmus:', program_config)
	return kembali


class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines


def print_info(filename='info.txt', warna='green'):
	disini = ayah(__file__, 1)
	filepath = joiner(disini, filename)
	filecontent = file_content(filepath)
	indah4(filecontent, warna=warna)


# def handle_publish_to_redis(message):
# 	channel = 'quicklang_channel'
# 	configkey = 'quicklang_redisconfig'
# 	from schnell.gui.system.searcher.make_redis_help import try_redis_connect_return
# 	r = try_redis_connect_return(configkey, db=0)
# 	r.publish(channel, message.encode())


def handle_quicklang_publish(request, item):
	"""
	/p)
	/p)$
	"""
	if request.startswith('$'):
		import subprocess
		perintah = request.removeprefix('$').strip()
		perintah = bongkar_ulibpy(perintah)
		cwd = item.workdir if os.path.isdir(item.workdir) else os.path.dirname(item.workdir)
		pecah = split_safe_quote(perintah)
		result = subprocess.run(pecah, cwd=cwd, capture_output=True, text=True)
		# result.stdout
		# result.stderr
		message = f'== stdout\n{result.stdout}\n== stderr\n{result.stderr}'  # .encode()
	else:
		message = request  # .encode()
	# kita bikin gini /p)data-text, /p)$ perintah utk diexec
	# self.quick_subscriber = RedisSubscriber('quicklang_channel', 'quicklang_redisconfig')
	try:
		handle_publish_to_redis(message)
	except:
		pass
	indah4(message, warna='yellow')


def replace_root_tree_variables(root_tree, item_command_or_content):
	if hasattr(root_tree, 'variables'):
		for kunci, nilai in root_tree.variables.items():
			item_command_or_content = item_command_or_content.replace(kunci, nilai)
	return item_command_or_content


def process_language(code, root_tree=None, item=None, self_run_configuration_replacer=None):

	global program_config

	if env_int('ULIBPY_FMUS_DEBUG')>1:
		# pass
		indah4(f"""[quick.__init__:process_language] INITIAL
		root_tree   = {root_tree}
		item        = {item}
		code		= {code}
		""", warna='cyan')

	if not code:
		'''
		u -e/
		'''
		filename = 'choice.fmus'
		disini = ayah(__file__, 1)
		filepath = joiner(disini, filename)
		# print(f'run mkfile: {filepath}')
		fmus.process_mkfile(filepath, baris_entry='index/fmus')
		return

	elif code.startswith('%'):
		'''
		u -e'/%specialcmd.py'
		u -e'/%$specialcmd.py'
		u -e'/%$*specialcmd.py'
		'''
		# from schnell.app.quick.quick_statement import peek_file
		from .quick_statement import peek_file
		peek_file(code)
		return

	elif code.startswith('@'): # /@mycsvcode
		'''
		u -e'/@code'
		'''
		request = code.removeprefix('@')
		from schnell.app.transpiler.mycsv.process import process_language
		process_language(request)
		return

	elif code.startswith('>'):
		'''
		u -e'/>json|json2|csv|sql,namafile|csvcode'
		u -e'/>dc,pg|mg|my|ma|ms|redis'
		'''
		request = code.removeprefix('>')
		from schnell.app.special import genfile
		genfile(request)
		return

	elif code.startswith('tar>'):
		'''
		u -e'/tar>foldername|node_modules'		foldername.tar
		u -e'/tar>foldername*|node_modules'		foldername.tgz
		'''
		request = code.removeprefix('tar>')
		from .tarprovider import tarprovider
		tarprovider(request)
		return

	elif code.startswith('D)'):
		'''
		u -e'/D)dj|[/tempdb]{@Todo}title,s;description,t;done,b'
		u -e'/D)=filepath=barisentry'
		'''
		from .dahsyater import dahsyater

		request = code.removeprefix('D)')

		# handle /D)=filepath=barisentry
		if request.startswith('=') and request.count('=') == 2:
			request = request.removeprefix('=')
			request = filepath_samadengan_barisentry(request)
			indah4(f'''[app.quick]
			hasil filepath_samadengan_barisentry:
			request sudah menjadi [{request}]
			''', warna='blue')
			if not request:
				indah4('[app.quick] not processing for empty dahsyat request', warna='red')
				return

		dahsyater(request)
		return

	elif code.startswith(BLITZ_PREFIX):
		'''
		u -e'/b>cpp/cm1|recipe05.cpp'
		u -e'/b>cpp/cm1|recipe05.cpp,output.exe'
		'''
		request = code.removeprefix(BLITZ_PREFIX)
		from .blitz import blitz
		blitz(request)
		return

	elif code.startswith('F)'): # /F) new fullstack
		'''
		/F)fqdn coordinator|csvcode
		'''
		request = code.removeprefix('F)')
		if request:
			from coords import new_fullstack
			if '|' in request:
				new_fullstack(*request.split('|'))
			else:
				new_fullstack(request, '[/todo]{@Todo}title,s;description,t;completed,b,df=false;createdAt,dt:dt;updatedAt,dt:dt')
		return

	elif code.startswith('vamp)'):
		'''
		/vamp)coords.djangomindtales|ecommerce.dat|kuda.fmus=index/fmus,babi.fmus=index/fmus,rusa.fmus=index/fmus
		TODO:
		bisa copy??? bisa generate??? utk template sederhana
		'''
		request = code.removeprefix('vamp)')
		if request:
			from coords import vampire
			vampire(request)
		return

	elif code.startswith('fmus)'):
		'''
		/fmus)rusa.fmus=index/fmus
		masih bermasalah
		krn jalankan di tempat rusa.fmus
		padahal pengen di curdir
		TODO:
		/fmus)rusa.fmus=index/fmus|output_folder
		'''
		request = code.removeprefix('fmus)').strip()
		if request:			
			filepath = request
			baris_entry='index/fmus'
			fresh=True
			if '=' in request:
				filepath, baris_entry = request.split('=')
				if ',' in baris_entry:
					baris_entry, fresh = [item.strip() for item in baris_entry.split(',')]
					fresh = bool(fresh)

			filepath = bongkar(filepath)
			run_fmus_for_file(filepath, baris_entry, fresh, change_to_current_directory=True)
		return

	elif code.startswith('reverse)'):
		'''
		/reverse)basefolder
			dirs+files
		/reverse)*basefolder
			dirs only

		/reverse)basefolder|outputfmusname
		generate subfolders
		/reverse)*basefolder|outputfmusname
		'''
		request = code.removeprefix('reverse)').strip()
		if request:
			kwargs = {}
			if request.startswith('['):
				configs, request = [item.strip() for item in request.removeprefix('[').split(']',1)]
				# config item kita pisah dengan /
				# 	=> skip_dirs=.../skip_files=.../skip_ext=...
				# skip_dirs=.pnpm-store,.git,.next,.vs,__pycache__,bin,build,dist,logs,node_modules,out,obj,target
				# /skip_files=.gitignore,package-lock.json,pnpm-lock.yaml,yarn.lock
				# /skip_ext=.o,.out,.exe,.bin
				skip_folders= [
					".pnpm-store",
					".git",
					".next",
					".vs",
					"__pycache__",
					"bin",
					"build",
					"dist",
					"logs",
					"node_modules",
					"out",
					"obj",
					"target",
				]
				skip_files= [
					".gitignore",
					"package-lock.json",
					"pnpm-lock.yaml",
					"yarn.lock",
				]
				skip_ext=[".o", ".out", ".exe", ".bin"]
				for config in [item.strip() for item in configs.split('/')]:
					if config.startswith('skip_dirs'):
						datadirs = config.removeprefix('skip_dirs').strip()
						skip_folders=[item.strip() for item in datadirs.split(',')]
						kwargs.update({ 'skip_folders': skip_folders })
					elif config.startswith('skip_files'):
						datafiles = config.removeprefix('skip_dirs').strip()
						skip_files=[item.strip() for item in datafiles.split(',')]
						kwargs.update({ 'skip_files': skip_files })
					elif config.startswith('skip_ext'):
						dataexts = config.removeprefix('skip_dirs').strip()
						skip_ext=[item.strip() for item in dataexts.split(',')]
						kwargs.update({ 'skip_ext': skip_ext })
			basefolder = request
			output_fmus = None
			dirsonly = False
			if '|' in request:  # /reverse)folder|outputfilename
				basefolder, output_fmus = [item.strip() for item in request.split('|')]
			else:
				# indah4(f"output_fmus [{output_fmus}] kosong. masukkan nama apa saja, gak perlu filepath, cukup filename. misal '<whatever>.fmus'", warna='red')
				# return
				output_fmus = os.path.basename(basefolder) + '.fmus'

			if basefolder.startswith('*'):
				basefolder = basefolder.removeprefix('*')
				dirsonly = True

			output_fmus = bongkar(output_fmus)
			kwargs.update({ 'base_folder': basefolder, 'output_fmus': output_fmus })
			if dirsonly:
				# reverse_folder_onlydirs(basefolder, output_fmus)
				reverse_folder_onlydirs(**kwargs)
			else:
				# reverse_folder(basefolder, output_fmus, create_index=True)
				kwargs.update({ 'create_index': True })
				# reverse_folder(basefolder, output_fmus, create_index=True)
				reverse_folder(**kwargs)
		else:  # add 28/7/23
			reverse_folder(item.workdir)
		return

	elif code.startswith('parsetree)'):
		'''
		parse python program
		/parsetree)
		/parsetree)basefolder
		/parsetree)basefolder|outputfile.fmus
		'''
		from schnell.app.ivyutils import folder_to_parsetree
		request = code.removeprefix('parsetree)')
		if request:
			basefolder = request
			output_fmus = None
			if '|' in request:
				basefolder, output_fmus = [item.strip() for item in request.split('|')]
			folder_to_parsetree(basefolder, output_fmus)
		else:
			indah4(f"[{code}] => folder_to_parsetree(item.workdir) = folder_to_parsetree({item.workdir})", warna='green')
			folder_to_parsetree(item.workdir)
		return

	elif code.startswith('coord)'):
		'''
		create coord from template
		/coord)mycoord.py,MyCoordinator,myplay-input.fmus
		/coord)mycoord.py,MyCoordinator,myplay-input.fmus,myplay-output.fmus
		/coord)mycoord.py,MyCoordinator,myplay-input.fmus,myplay-output.fmus,appcontent.tpl
		/coord)mycoord.py,MyCoordinator,myplay-input.fmus,myplay-output.fmus,appcontent.tpl,node_antd
		/coord)mycoord.py,MyCoordinator,myplay-input.fmus,myplay-output.fmus,appcontent.tpl,node_antd,index-fmus
		'''
		request = code.removeprefix('coord)')
		jumlah_koma = request.count(',')
		if request and jumlah_koma>=2:
			from coords import clone_coordinator_here
			args = [item.strip() for item in request.split(',')]
			# kwargs = {}
			# if jumlah_koma == 6:
			# 	pass
			# elif jumlah_koma == 5:
			# 	pass
			# elif jumlah_koma == 4:
			# 	pass
			# elif jumlah_koma == 3:
			# 	pass
			# elif jumlah_koma == 2:
			# 	pass
			clone_coordinator_here(*args)
		return

	elif code.startswith('file)'):
		'''
		/file)j/17|__PWD/contoh.txt
			join baris no 17 sebanyak 1 (dg next line)
		/file)j/17/5|__PWD/contoh.txt
			join baris no 17 sebanyak 5 baris
		
		u -e"/file)c/2,3/'-- '|__PWD/contoh.txt"
		u -e"/file)c/1,4-6/'-- '|__PWD/contoh.txt"
					 ^^^^^ line expression
		u -e"/file)C/TEXT/'-- '|__PWD/s_users.sql"

		C tidak terima leading space
		C2 bisa leading space

		c:\work>u -e"/file)C/SET/'-- '|__PWD/s_users.sql"
		comment_file_by_prefix c:\work/s_users.sql OK

		c:\work>u -e"/file)C/ALTER TABLE/'-- '|__PWD/s_users.sql"
		comment_file_by_prefix c:\work/s_users.sql OK

		c:\work>u -e"/file)C/ALTER SEQUENCE/'-- '|__PWD/s_users.sql"
		comment_file_by_prefix c:\work/s_users.sql OK

		c:\work>u -e"/file)C/SELECT /'-- '|__PWD/s_users.sql"
		comment_file_by_prefix c:\work/s_users.sql OK

		c:\work>u -e"/file)j/72/6|__PWD/s_users.sql"
		join_lines c:\work/s_users.sql OK

		c:\work>u -e"/file)C2/ADD CONSTRAINT /'-- '|__PWD/s_users.sql"
		comment_file_by_prefix c:\work/s_users.sql OK

		tambah:
		di-regex kan...tiap baris
		/file)re/fileregex|__PWD/filetarget
		/file)re/fileregex|filetarget
		disini kita bikin versi 'us' file, jadi gak pake entry

		remove lines
		u -e"/file)-/<pola prefix>/<jumlah hapus>|<target file>"
		u -e"/file)-/SELECT /3|__PWD/s_users.sql"

		replace strings in lines
		/file)repl/string pertama/string kedua|filetarget

		TODO:
		ada increment dan ada size
		misal kita I/D sebanyak 2 spaces...bisa 2x, 3x, dst.		
		default increment = 1
		bisa by_lineno dan bisa by_prefix
		indent_tab(inc=1)
		indent_space(inc=1, size=2)
		dedent_tab(inc=1)
		dedent_space(inc=1, size=2)

		file>>lineexpr,t|filepath
		file>>lineexpr,t,1|filepath
			indent pada line nos = lineexpr, gunakan tab sebanyak 1
		file>>lineexpr,s|filepath
			indent pada line nos = lineexpr, gunakan space sebanyak 1 (default) dg space size = 2 (default)
		file>>lineexpr,s,1,4|filepath
			indent pada line nos = lineexpr, gunakan space sebanyak 1 dg space size = 4
		file><lineexpr,t,1|filepath
		file><lineexpr,s,1,4|filepath
		
		juga: (tentu ini apply to whole file)
		convert tab to space
		file>ts|filepath
		file>ts/4|filepath
		convert space to tab
		file>st|filepath
		file>st/4|filepath
		'''
		request = code.removeprefix('file)')
		# indah4(f'''
		# mau lempar fileops: {request}
		# ''', warna='blue')

		if not request:
			from .common import file_instruction
			indah4(f'''[app.quick][/file)]\n{file_instruction}''', warna='cyan')
			return
		if hasattr(root_tree, 'variables'):
			request = replace_from_configuration_replacer(request, root_tree.variables)
		fileops(request, root_tree, item, self_run_configuration_replacer)
		return

	elif code.startswith('sc)'):
		"""
		fm//sc)colly/selection/operasi/object|url
		fm//sc)colly/selection/operasi/object|url
			operasi dan object adlh dummy utk sementara ini, maka selalu diakhiri //|url

		sc_provider = {
			'.'     :'colly',
			'c'     :'colly',
			'gq'    :'goquery',
			'b'     :'bs4',
			'j'     :'jsoup',
			's'     :'scrapy',
		}
		../sc)colly/.article__title//|https://www.scmp.com/
		scrapy sshell
		../sc)https://www.scmp.com/

		lihat juga app.scrape
		"""
		request = code.removeprefix('sc)')
		if not request:
			from .common import scraper_instruction
			indah4(f'''[app.quick][/sc)]\n{scraper_instruction}''', warna='yellow')
			return
		if request.startswith('http'):
			'''
			panggil scrapy shell saja
			'''
			from schnell.app.utils import perintahsp_simple
			perintahsp_simple(f'scrapy shell {request}')
			return
		scraper(request)
		return

	elif code.startswith('sel)'):
		"""
		/sel)config|find|oper|find|oper|...|url

		Rp. 2.405,8600 19 April 2022
		<span class="normal ng-binding">Rp.</span> 2.405,8600
		<span class="date ng-binding">19 April 2022</span>

		nop/wt=css=span.normal.ng-binding

		../sel)hless,chr|css=span.normal.ng-binding/txt|https://pasardana.id/fund/2789
		../sel)hless,chr|css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt|https://pasardana.id/fund/2789
		../sel)hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt|https://pasardana.id/fund/2789
		../sel)hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/css=a.btn.btn-signin/c|https://pasardana.id/fund/2789

		../sel)hless,chr| nop/wt=css=span.normal.ng-binding/   nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt / css=a.btn.btn-signin/c|https://pasardana.id/fund/2789
		"""
		request = code.removeprefix('sel)')
		if not request:
			indah4('''[app.quick][sel)]
			/sel)config|find|oper|find|oper|...|url

			../sel)hless,chr|css=span.normal.ng-binding/txt/nop/q|https://pasardana.id/fund/2789
			../sel)hless,chr|css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/nop/q|https://pasardana.id/fund/2789
			../sel)hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/nop/q|https://pasardana.id/fund/2789
			../sel)hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/css=a.btn.btn-signin/c/nop/q|https://pasardana.id/fund/2789
			../sel)hless,chr| nop/wi/nop/wt=css=span.normal.ng-binding=Rp./css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt / css=a.btn.btn-signin/c /nop/q|https://pasardana.id/fund/2789

			../sel)|nop/wi|up1
			''', warna='yellow')
			return
		selena(request)
		return

	elif code.startswith('nb)'):
		"""
		/nb)fmusfile=barisentry
		/nb)content/content/content/content
			default notebook.ipynb
		/nb)content/content/content/content|filename
			di %temp% => ganti 23/12/23 ke item.workdir
		/nb)content/content/content/content|filepath
			di dirpath+filepath
		"""
		request = code.removeprefix('nb)')
		if not request:
			indah4('''[app.quick][nb)]
			../nb)content/content/content/content|filepath
			''', warna='yellow')
			return
		notebook(request, item, default_location=item.workdir)
		return

	elif code.startswith('cepat)'):
		"""
		/cepat) adlh pengganti mycsv/ucsv
			berarti setara /@
		/cepat){@User}username,s
		"""
		request = code.removeprefix('cepat)').strip()
		if request:
			from ciledug.cepat.cepat import processor_mycsv
			result = processor_mycsv(request, returning=True)
			# print(f"terima jenis {type(result)} => {result}.")
			if isinstance(result, list):
				result = '\n'.join(result)
			# handle_quicklang_publish(result, item)
			indah3(result, warna='yellow', layar='blue')
		return

	elif code.startswith('palsu)'):
		"""
		/palsu)i
		/palsu)s/5
		"""
		request = code.removeprefix('palsu)').strip()
		if request:
			from ciledug.palsu.palsu import process_palsu_language
			# def process_palsu_language(code, returning=True, current_handler=handler_palsu):
			result = process_palsu_language(request, returning=True)
			# print(f"/palsu) terima jenis {type(result)} => {result}.")
			if isinstance(result, list):
				result = '\n'.join(result)
			if not isinstance(result, str):
				result = str(result)
			# handle_quicklang_publish(result, item)
			indah3(result, warna='yellow', layar='blue')
		return

	elif code.startswith('yellow)'):
		"""
		publish ke yellow note
		/yellow)data_atau_content_atau_text
		"""
		request = code.removeprefix('yellow)')
		if not request:
			indah4('''[app.quick][yellow)]
			/yellow)message
			''', warna='yellow')
			return
		handle_quicklang_publish(request, item)
		return

	elif code.startswith('ls)'):
		"""
		/ls)
		"""
		request = code.removeprefix('ls)')
		if not request:
			indah4('''[app.quick][ls)]
			/ls)message
			''', warna='yellow')
			return

		filter_files = [] # /ls)folderpath|contain1,contain2
		if '|' in request:
			folder_path, filter_files = [e.strip() for e in request.split('|')]
			if ',' in filter_files:
				filter_files = [e.strip() for e in filter_files.split(',')]
			else:
				filter_files = [filter_files]
			
			folder_path = bongkar(folder_path)
			print(f'[quick.init] #1 folder_path = {folder_path}, filter_files = {filter_files}')
		else:
			folder_path = bongkar(request)

		print(f'[quick.init] #2 folder_path = {folder_path}, filter_files = {filter_files}')

		if isdir(folder_path):
			# Get a list of all files in the folder
			if filter_files:
				files = [item for item in os.listdir(folder_path) if any([x for x in filter_files if x.lower() in item.lower()])]
				print(f'[quick.init] filtering {folder_path} with {filter_files} => {files}.')
			else:
				files = os.listdir(folder_path)
			# Create a list of absolute file paths
			absolute_paths = [os.path.join(folder_path, file) for file in files]
			# Normalize each path
			normalized_paths = [os.path.normpath(path) for path in absolute_paths]
			# Sort the list of paths so that folders appear first
			sorted_paths = sorted(normalized_paths, key=lambda path: not os.path.isdir(path))
			# Join the list of sorted file paths with newlines
			sorted_paths_string = '\n'.join(sorted_paths)
			try:
				handle_publish_to_redis(sorted_paths_string)
			except:
				pass
			indah4(sorted_paths_string, warna='blue')
		return

	elif code.startswith('grep'):
		"""
		execute_command(command)
		execute_command2(command, working_dir=None)
		grep_text(sometext, somefolder=".")
		find_files(sometext, somefolder=".")
		/grep)text
		/grep)text|folder
		versi case_sensitive:
		/grep*)text
		/grep*)text|folder
		"""	
		case_sensitive = False
		if code.startswith('grep)'):
			request = code.removeprefix('grep)')
		elif code.startswith('grep*)'):
			request = code.removeprefix('grep*)')
			case_sensitive = True
		else:
			print(f'unknown /grep) => {request}.')
			return
		if '|' in request:
			sometext, somefolder = [e.strip() for e in request.split('|')]
			somefolder = bongkar(somefolder)
			result, err = grep_text(sometext, somefolder, case_sensitive=case_sensitive)
		else:
			result, err = grep_text(request, case_sensitive=case_sensitive)
		kembalian = result if result else (err if err else 'EMPTY')
		try:
			handle_publish_to_redis(kembalian)
		except:
			pass
		indah4(kembalian)
		return

	elif code.startswith('find)'):
		"""
		/find)text
		/find)text|folder
		versi case_sensitive:
		/find*)text
		/find*)text|folder
		"""
		case_sensitive = False
		if code.startswith('find)'):
			request = code.removeprefix('find)')
		elif code.startswith('find*)'):
			request = code.removeprefix('find*)')
			case_sensitive = True
		else:
			print(f'unknown /find) => {request}.')
			return
		if '|' in request:
			sometext, somefolder = [e.strip() for e in request.split('|')]
			somefolder = bongkar(somefolder)
			result, err = find_files(sometext, somefolder, case_sensitive=case_sensitive)
		else:
			result, err = find_files(request, case_sensitive=case_sensitive)
		kembalian = result if result else err
		try:
			handle_publish_to_redis(kembalian)
		except:
			pass
		indah4(kembalian)
		return

	elif code.startswith('exec)'):
		request = code.removeprefix('exec)')
		if '|' in request:
			command, working_dir = [e.strip() for e in request.split('|')]
			# command bisa berisi __PP utk hindari | yg dipake utk specify workingdir
			command = sanitize_chars(command)
			somefolder = bongkar(working_dir)
			result, err = execute_command2(command, working_dir)
		else:
			# command bisa berisi __PP
			request = sanitize_chars(request)
			result, err = execute_command(request)
		kembalian = result if result else err
		try:
			handle_publish_to_redis(kembalian)
		except:
			pass
		indah4(kembalian)
		return

	elif code.startswith('xp)'):
		request = code.removeprefix('xp)').replace('/', '\\')
		request = bongkar(request)
		if request:
			os.system(f'explorer {request}')
		return

	elif code.startswith('acd)'):
		"""
		"""
		request = code.removeprefix('acd)').strip()
		# QObject::startTimer: Timers can only be used with threads started with QThread
		# QBasicTimer::start: QBasicTimer can only be used with threads started with QThread
		# ini sama dg **showtext atau **showfile
		from schnell.gui.acdsee.acdsee import acdsee, acdsee_app
		# acdsee_app(request if request else os.getcwd())
		acdsee()
		# if request:
		# 	acdsee_app(request)
		# else:
		# 	acdsee_app()
		# w.showMaximized()
		return

	elif code.startswith('clip)'):
		"""
		manipulate string data di clipboard
		harus ada content dan operation
		operation: tabspec, prefix, suffix, remove x dst

		contoh:
		g "/clip)"
		lalu copy 
		42||...isi file...
		maka akan diperoleh isi file baru yang sudah dikonversi dari 4 tab ke 2 tab
		"""
		request = code.removeprefix('clip)').strip()
		from schnell.app.clipboardutils import manipulate, manipulate_clip, process_clipboard
		# if request:
		# 	manipulate(request)
		# else:
		# 	manipulate_clip()
		hasil = process_clipboard(request)
		indah3(hasil, warna='cyan')
		return

	elif code .startswith('R)'):
		'''
		replify
		R)ff
		R)py/ff
		'''
		request = code.removeprefix('R)')
		from schnell.creator.repl_language.replify import replify
		from database.langnew import bahasa
		# replify(text, workdir, langchoice='py')
		# lama, perintah = [item.strip() for item in request.split('|')]
		# nantisystem(lama, perintah)

		# wait up bisa /R)py/something, tapi jk /R)/wieke ini pengen cari...
		lang = 'py'
		# jk /R)py/ tapi bukan /R)/... yg minta cari
		if '/' in request and not request.startswith('/'):
			_lang, _request = request.split('/', 1)  # bisa /R)f//sass?e, jadi gak selalu /R)scala/ff
			if _lang in bahasa:
				lang = _lang
				request = _request
		hasil = replify(request, item.workdir, lang)
		try:
			handle_publish_to_redis(hasil)
		except:
			pass
		indah4(hasil)
		return

	elif code.startswith('ocr)'):
		"""
		/ocr)
		/ocr)data
		"""
		request = code.removeprefix('ocr)')
		from schnell.app.ocrutils import ocr_screenshot
		if not request:
			ocr_screenshot()
		else:
			if '|' in request:
				# def ocr_screenshot(output_file = None, DATADIR = env_get('ULIBPY_MEMO_DATADIR'), delay=1.0):
				# /ocr)filenameoutput|datadir|delay
				ocr_screenshot(*request.split('|'))
			else:
				ocr_screenshot(request)
		return

	elif code.startswith('ref)'):
		"""
		../ref)file/fungsi/args
		../ref)file/fungsi/k=v|k=v
		/ref)schnell.app.githubutils/get_repos_from_githubusername/hendisantika
		/ref)schnell.app.wcmderutils/create_fill_set_with_id_index
		"""
		request = code.removeprefix('ref)')
		if not request:
			indah4('''[schnell.app.quick.__init__]
			/ref)file/fungsi/args
			/ref)notfutils/notifypy/judul-judulan, isi-isian euy...
			/ref)notfutils/pynotif/judul-judulan, isi-isian euy...
			''', warna='yellow')
			return
		
		if request.count('/') >= 2:  # /ref)filename/fungsi/arg1|arg2, args bisa juga berisi /, jadi >=2
			filename, fungsi, args = request.split('/', 2)
		elif request.count('/') == 1:  # /ref)filename/fungsi
			filename, fungsi = request.split('/', 2)
			args = None
		else:
			indah4('/ref)harus berbentuk /ref)file/fungsi atau /ref)file/fungsi/arg1|arg2|arg3')
			return
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			indah4(f"""[quick:/ref)]
		filename = {filename}
		fungsi = {fungsi}
		args = {args}
		""", warna='green')
		args_delimiter = '|'  # agar tiap arg bisa punya ,
		if args:  # file/fungsi/arg1|arg2
			if '=' in args:  # filename/fungsi/arg1=val1|arg2=val2
				args = args.split(args_delimiter)
				# args = {k:v for k,v in item.split('=') for item in args}
				kv = {}
				# internal schnell.app.dbutils.mysqlutils/connect_list_all_databases/host=localhost|user=root|password=sakila
				for item in args:
					k,v = item.split('=')
					# UPD: 24/11/23
					# jika v berisi koma, maka kita konversi ke list dulu, karena dia minta list tentunya
					if v.count(','):
						v = [item.strip() for item in v.split(',')]
					# UPD: END
					kv[k] = v
				if env_int('ULIBPY_FMUS_DEBUG')>1:
					indah4(f"""[quick:/ref)] panggil(filename, fungsi, kwargs=kv)
		filename = {filename}
		fungsi = {fungsi}
		kv = {kv}
		""", warna='green')
				# panggil(filename, fungsi, kwargs=kv)
				panggil(filename, fungsi, **kv)
			else:  # filename/fungsi/arg1|arg2
				args = args.split(args_delimiter)
				# print('masuk list')
				panggil(filename, fungsi, *args)
		else:  # file/fungsi
			# print('masuk empty')
			panggil(filename, fungsi)
		return

	elif code.startswith('s)'):
		'''
		search
		../s)  ...search code...

		u -e"/s)package main|__PWD"
		u -e"/s)~~main.go|__PWD"
			~~main.go 	files only
		u -e"/s)~src/|__PWD"
			~src/ 		dirs only
		u -e"/s)~main|__PWD"
			~main		files+dirs
		u -e"/s)#main|__PWD"
			#main		search dg wsl find

		word_content_search(basefolder, code)
		system_find(basedir, pattern, capture=False, find_cmd='find', case_insensitive=True)
			pattern adlh filename yg akan menjadi: *filename*
		s)cari_string|file
		s)#cari_namafile|file
		s)~cari_namafile_dg_pattern|file
		files = walk_fullpath_skipdirs(basedir, skipdirs=['.git', '__pycache__'])
		dirs = walk_fulldirs(basedir, skipdirs=['.git', '__pycache__'])
		'''
		request = code.removeprefix('s)').strip()
		if not request:
			from .common import search_instruction
			indah4(f'''[app.quick][s)] searching...\n{search_instruction}''', warna='yellow')
			return

		######################################
		pola, basefolder = request.split('|')

		basefolder = bongkar(basefolder)
		if not '@' in basefolder:
			if not isdir(basefolder):
				# fmus.get_cwd_pwd() suka diakhiri schnell
				# basefolder jk @s... maka dimulaidg schnell
				# jadi double schnell
				basefolder = joiner(fmus.get_cwd_pwd(), basefolder)
			original_dir = basefolder # sblm linuxify
			basefolder = linuxify(basefolder) # krn mau pake grep, bukan grab...apalagi gojek
		######################################
		elif not isdir(basefolder) and '@' in basefolder:
			'''
			agar bisa @c, @d, @s, dst.
			krn kita prefix dg rootdir, maka hanya proses jk ada @ di folder name

			../s)~feat.fmus|@saqb
			search /mnt/c/Users/usef/work/sidoarjo/schnell/@saqb
			search ...
			find files: dirs+files
			ngawur nih soal wsl path, dsb
			'''
			print('search', basefolder)
			basefolder = folder_expand(basefolder, force_pemisah='/', prefix_with_rootdir=True)
			print('search', basefolder)
			original_dir = basefolder # sblm linuxify
			basefolder = linuxify(basefolder) # krn mau pake grep, bukan grab...apalagi gojek

		# indah4(f'''
		# dirops: {request}
		# pola: {pola}
		# base: {basefolder}
		# ''', warna='blue')
		if pola.startswith('#'):
			'''
			s)# search filename with find command
			'''
			pola = pola.removeprefix('#')
			kembali = system_find(basefolder, pola, capture=True, find_cmd='wsl find')
		elif pola.startswith('~'):
			'''
			s)~ search filename with pattern/antipattern
			ada dirs+files		~pola
			ada dirs only		~pola/
			ada files only		~~pola
			ada sorted
			ada nonsorted
			'''
			pola = pola.removeprefix('~')
			if pola.endswith('/'):
				# print('find files: dirs only')
				pola = pola.removesuffix('/')
				dirs = walk_fulldirs(original_dir, skipdirs)
				# print('2find files: dirs only', dirs)
				kembali = pattern_search_list([item.removesuffix('*') for item in dirs], pola)
				# print('3find files: dirs only', kembali)
			elif pola.startswith('~'):
				# print('1find files: files only')
				pola = pola.removeprefix('~')
				files = walk_fullpath_skipdirs(original_dir, skipdirs)
				# print('2find files: files only', files)
				kembali = pattern_search_list(files, pola)
				# print('3find files: files only', kembali)
			else:
				print('find files: dirs+files')
				dirs = walk_fulldirs(original_dir, skipdirs)
				files = walk_fullpath_skipdirs(original_dir, skipdirs)
				kembali = pattern_search_list(dirs+files, pola)
		else:
			'''
			search text/content
			'''
			kembali = word_content_search(basefolder, pola)
		indah4(kembali, warna='yellow')
		return

	elif code.startswith('run>'):

		rawcode = code.removeprefix('run>')

		if not rawcode:
			indah4('''[app.quick][run>]
			../run>>
				@s lihat dirs di @s
			../run>#
				@s lihat files di @s
			../run>^
				@s tree di @s
			../run>*					run file
				filename.fmus
				filename.fmus | index/loop
				*content.fm
				semua di atas bisa diakhiri * (kecuali yg diakhiri index/loop) 
					utk edit, contoh ../run>*@d/1stop.fmus*
			../run>*@satff/flask
					berarti coba jalankan flask.fmus di @satff
					utk jalankan coordinator:
					../run>@satff/flask
					(tanpa *)
			../run>					run coordinator
				@satff/flask
					input csvcode utk buat flask
				@satff/flask|csvcode
					buat flask dg given csvcode
			''', warna='yellow')
			return

		if rawcode.startswith('>'):
			'''
			run>>@s
				lihat dirs schnell
			'''
			lokasi = rawcode.removeprefix('>')
			lister(lokasi)
			return
		elif rawcode.startswith('#'):
			'''
			run>#@s
				lihat files di schnell
			'''			
			lokasi = rawcode.removeprefix('#')
			filers(lokasi)
			return
		elif rawcode.startswith('^'):
			'''
			run>^@s
				wsl tree di schnell
			'''			
			lokasi = rawcode.removeprefix('^')
			treelers(lokasi)
			return
		elif rawcode.startswith('*'):
			'''
			run>*...
				run fmus=mk atau fm file
			'''			
			lokasi = rawcode.removeprefix('*')
			fmusrunner(lokasi)
			return
		if not '|' in rawcode:
			dummycsvcode = '[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s;description,s;done,b'
			csvcode = get_input_from_user_gui('csv code to process', dummycsvcode)
			if csvcode:
				rawcode += '|' + csvcode
			else:
				rawcode += '|' + dummycsvcode
		# print(f'rawcode dari quick sblm crunner', rawcode)
		crunner(rawcode)
		return

	elif code.startswith('hope)'):
		'''
		hope>perintah|harap|kirim|harap|kirim
		../hope>scp2|.*password:|usef
		'''
		request = code.removeprefix('hope)').lstrip()
		if not request:
			indah4('''[app.quick][hope)]
			hope>perintah|harap|kirim|harap|kirim
			''', warna='yellow')
		from .crunner import harap
		harap(request)
		return

	elif code.startswith('fmb)'):
		'''
		menjalankan fmus file, default dari @c/appgen
		filepath = folder_expand('@c/appgen', prefix_with_rootdir=True)
		run_fmus_for_file(file_choice)
		'''
		from .fmusbrowser import fmusbrowser
		filepath = code.removeprefix('fmb)')
		fmusbrowser(filepath)
		return

	elif code.startswith('gz)'):
		request = code.removeprefix('gz)')
		if not request:
			from .common import compressor_instruction
			indah4(f'''[app.quick][/l)]\n{compressor_instruction}''', warna='cyan')
			return
		from .compressor import compressor
		compressor(request)
		return

	elif code.startswith('bz)'):
		request = code.removeprefix('bz)')
		if not request:
			from .common import compressor_instruction
			indah4(f'''[app.quick][/l)]\n{compressor_instruction}''', warna='cyan')
			return
		from .compressor import compressor
		from schnell.app.compressutils import bz, unbz
		compressor(request, bz, unbz)
		return

	elif code.startswith('zip)'):
		request = code.removeprefix('zip)')
		if not request:
			from .common import compressor_instruction
			indah4(f'''[app.quick][/l)]\n{compressor_instruction}''', warna='cyan')
			return
		from .compressor import compressor, zip, unzip
		# from schnell.app.compressutils import bz, unbz
		# contoh u -e"/zip)<python.zip*"
		compressor(request, zip, unzip)
		return

	elif code .startswith('T)'):
		'''
		u -e"/T)5|cmd /k start"
		../T)5|python -m webbrowser -t https://youtube.com/
		'''
		request = code.removeprefix('T)')
		from schnell.app.concurrentutils import nantisystem
		lama, perintah = [item.strip() for item in request.split('|')]
		if perintah.startswith('https://') or perintah.startswith('http://'):
			perintah = f'python -m webserver -t {perintah}'
		nantisystem(lama, perintah)
		return

	elif code .startswith('l)'):
		'''
		l)alamat
		l)default-release|alamat
		'''
		request = code.removeprefix('l)').strip()
		from .launcher import launcher
		from startup import buka
		
		if not request:
			# from .common import launcher_instruction
			# indah4(f'''[app.quick][/l)]\n{launcher_instruction}''', warna='cyan')
			from schnell.app.utils import PROGRAMS
			os.system(PROGRAMS['ff'])
		elif '|' in request:
			from schnell.app.systemutils import firefox_profiles, open_url_with_firefox
			urlpath = request
			if '|' in urlpath:
				firefox_profiles_ = firefox_profiles()
				firefox_profile, url = [e.strip() for e in urlpath.split("|")]
				if firefox_profile == '*':  # *|url utk list profile
					content = '\n'.join(firefox_profiles_)
					print(content)
				else:
					wanted = firefox_profile.lower()
					if wanted in firefox_profiles_:
						open_url_with_firefox(url, wanted)
					else:
						found = [item for item in firefox_profiles_ if wanted in item]
						if found:
							wanted = found[0]
							open_url_with_firefox(url, wanted)
		else:
			if '__PROMPT' in request:
				# from schnell.app.promptutils import autoprompt, gui_masuk
				from schnell.app.guipromptutils import gui_masuk
				# jk 2x manggil hasilkan gini
				# Tcl_AsyncDelete: async handler deleted by the wrong thread
				# data = autoprompt('Masukkan nilai untuk __PROMPT:')
				data = gui_masuk('Masukkan nilai untuk __PROMPT:')
				request = request.replace('__PROMPT', data)
			# launcher(request)
			buka(request) # agar bisa chrome, ff, opera, dll sesuai config
		return

	elif code .startswith('aws)'):
		request = code.removeprefix('aws)')
		if not request:
			from .common import cloudia_instruction
			indah4(f'''[app.quick][/:]\n{cloudia_instruction}''', warna='cyan')
			return
		from .cloudia import cloudia
		cloudia(request)
		return

	elif code .startswith('dot)'):
		'''
		/dot)@
			dari clipboard
		/dot)[filename.jpg]dotcode
		/dot)dotcode
		'''
		request = code.removeprefix('dot)').strip()
		from .languages.dotlang import dotlang
		if request:
			if request == '@': # ../dot)@
				dotlang(trypaste())
			elif request.startswith('['):
				'''
				/dot)[filename.jpg]...kode...
				'''
				filepath, imagecode = request.removeprefix('[').split(']', 1)
				if not isabsolute(filepath):
					filepath = joiner(item.workdir, filepath)
				dotlang(imagecode, filepath)
			else:
				dotlang(request)
		else:
			dotlang()
		return

	elif code .startswith('img)'):
		"""
		sayangnya di sini, gak bisa ada newline pada code yg diberikan...
		jadi hrs ada 2 proses.
		encode newline ke __NL__ di sini
		decode __NL__ ke newline sblm diproses imagelang.
		"""
		request = code.removeprefix('img)').strip()
		from .languages.imagelang import imagelang
		if request:
			# bisa dari clipboard dg ../img)@
			if request == '@':
				imagelang(trypaste())
			elif request.startswith('['):
				'''
				/img)[filename.jpg]...kode...
				'''				
				filepath, imagecode = request.removeprefix('[').split(']', 1)
				if not isabsolute(filepath):
					filepath = joiner(item.workdir, filepath)
				imagelang(imagecode, filepath)
			else:
				# request = request.replace('\n', '__NL__')
				# indah4(f"imagelang code dari quick [{request}]")
				imagelang(request)
		else:
			imagelang()  # default code
		return

	elif code .startswith('G)'):
		request = code.removeprefix('G)').strip()
		from .languages.guilang import guilang
		if request:
			# bisa dari clipboard dg ../G)@
			if request == '@':
				guilang(trypaste())
			else:
				guilang(request)
		else:
			guilang() # /G) saja bisa jalankan yg default...
		return

	elif code .startswith('au)'):
		request = code.removeprefix('au)').strip()
		from schnell.autolang import process_language as autolang_process, myrepl as autolang_repl
		if request:
			autolang_process(request)
		else:
			autolang_repl()
		return

	elif code .startswith('chart)'):
		request = code.removeprefix('chart)').strip()
		from .languages.chartlang import chartlang
		if request:
			if request == '@': # ../chart)@
				chartlang(trypaste())
			else:
				chartlang(request)
		else:
			chartlang()
		return

	elif code .startswith('meme)'):
		'''
		/meme)<#60>ini tulisan dibawah ya...
		'''
		request = code.removeprefix('meme)').strip()
		from schnell.gui.system.searcher.widgets.editor_fmus_helper import create_and_show_meme
		if request:
			request = request.strip()
			filepath = None
			if request.startswith('*'):
				'''
				/meme)*filepath|...
				'''
				request = request.removeprefix('*') # "*filepath|"
				filepath, the_rest = request.split('|',1) # "filepath|"
				request = the_rest

			if request.startswith('['):
				'''
				utk minta warna
				/meme)[255,0,0]...kode...
				'''
				warna, memecode = request.removeprefix('[').split(']', 1)
				tuple_ = tuple(int(x) for x in warna.split(","))
				create_and_show_meme(memecode, warna=tuple_, filepath=filepath)
			else:
				create_and_show_meme(request, filepath=filepath)
		return

	elif code .startswith('gif)'):
		'''
		/gif)tulisan|file_url_input
		kita perkenalkan, bisa resize gif.
		fileinput,2.5 -> berarti resize 2.5
		'''
		request = code.removeprefix('gif)').strip()
		from schnell.app.mediautils import write_text_on_gif_animation, write_text_on_gif_animation_from_url
		from schnell.app.gifutils import screen_capture_to_gif
		if request:
			'''
			'''
			request = request.strip()
			if request.startswith('capture|'):
				'''
				/gif)capture|output|timeout,fps,fullscreen
				'''
				request = request.removeprefix('capture|').strip()
				if not '|' in request:
					screen_capture_to_gif(request) # default 10s, 15.0 fps, bbox
				else:
					output_gif, specs = [e.strip() for e in request.split('|')]
					timeout_fps_fs = [e.strip() for e in specs.split(',')]
					kwargs = {}
					if len(timeout_fps_fs)==3:
						timeout, fps, fs = timeout_fps_fs
						kwargs = {
							'timeout': int(timeout),
							'fps': float(fps),
							'fullscreen': bool(int(fs)),
						}
					elif len(timeout_fps_fs)==2:
						timeout, fps = timeout_fps_fs
						kwargs = {
							'timeout': int(timeout),
							'fps': float(fps),
							# 'fullscreen': bool(fs),
						}
					else:
						kwargs = {
							'timeout': int(timeout_fps_fs),
						}
					screen_capture_to_gif(output_gif, **kwargs)
			else:
				# format: text|fileinput
				# text bisa berisi | banyak
				resize = 1.0
				if re.match(r'.*\|\s*\d+\.\d+$', request):
					# jumlah | bisa variable, kita detek jk diakhiri digit
					text, fileinput, resize = [item.strip() for item in request.rsplit('|', 2)]
					resize = float(resize)
				else:
					text, fileinput = [item.strip() for item in request.rsplit('|', 1)]
				# request = <.1>aku senang|<.2>aku selalu senang|<.6>aku gak suka kamu|<.8>bisa kah kukatakan itu| https://media.tenor.com/yHrdC0x10XkAAAAC/winning-donald-trump.gif|3.5, 
				# text = <.1>aku senang|<.2>aku selalu senang|<.6>aku gak suka kamu|<.8>bisa kah kukatakan itu| https://media.tenor.com/yHrdC0x10XkAAAAC/winning-donald-trump.gif, 
				# fileinput = 3.5
				
				# if re.match(r'\d+\.\d+', fileinput.strip()):
				# 	text, fileinput, resize = [item.strip() for item in request.rsplit('|', 2)]
				# 	resize = float(resize)
				# no way, ternyata url bisa berisi ,
				print(f"/gif) request = {request}, text = {text}, fileinput = {fileinput}")
				# if '|' in fileinput:
				# 	# deprecated: /gif)tulisan|fileinput,2.5 # resize fileinput to 2.5x
				# 	# /gif)tulisan|fileinput|2.5 # resize fileinput to 2.5x
				# 	fileinput, resize_ = [i.strip() for i in fileinput.split('|',1)]
				# 	resize = float(resize_)
				if fileinput.startswith('http') and '://' in fileinput:
					write_text_on_gif_animation_from_url(text=text, alamat=fileinput, resize=resize)
				else:
					write_text_on_gif_animation(text=text, filepath_input=fileinput, resize=resize)
		return

	elif code .startswith('imgutils)'):
		'''
		imgutils)
			shot|
			merge|
			2png|
			scale|input
			scale|input|factor
			square|input
			square|input|output
		'''
		request = code.removeprefix('imgutils)').strip()
		if request:
			from schnell.app.imageutils2 import merge_images, merge_images2, screen_capture
			from schnell.app.imageutils3 import convert_jpeg_to_transparent_png, scale_image_file, image_to_square, overlay_image, write_text_on_image
			if request.startswith('shot'):
				# fullscreen = False
				request = request.removeprefix('shot').strip()
				if request.startswith('*'): # /imgutils)shot*|output
					# fullscreen = True
					output_file = request.removeprefix('*|').strip()
					screen_capture(output_file, True)
				else: # /imgutils)shot*|output
					screen_capture(request.removeprefix('|').strip())
			elif request.startswith('merge'):
				request = request.removeprefix('merge|').strip()
				if '|' in request:
					if request.count('|')==2: # jk imagelist|output|v atau h
						image_list, output_image, method = [e.strip() for e in request.split("|")]
						image_list = [e.strip() for e in image_list.strip().split(',')]
						method = 'vertical' if method == 'v' else 'horizontal'
						merge_images2(image_list, output_image, method)
					else:
						image_list, output_image = [e.strip() for e in request.split("|")]
						image_list = [e.strip() for e in image_list.strip().split(',')]
						merge_images2(image_list, output_image)
				else:
					image_list = [e.strip() for e in request.strip().split(',')]
					merge_images2(image_list)
			elif request.startswith('2png'):
				request = request.removeprefix('2png|').strip()
				if '|' in request:
					jpeg_input, png_output = [e.strip() for e in request.split('|')]
					convert_jpeg_to_transparent_png(jpeg_input, png_output)
				else:
					convert_jpeg_to_transparent_png(request)
			elif request.startswith('scale'):
				request = request.removeprefix('scale|').strip()
				if '|' in request:
					image_input, scale_factor = [e.strip() for e in request.split('|')]
					scale_image_file(image_input, float(scale_factor))
				else:
					scale_image_file(request)
			elif request.startswith('square'):
				request = request.removeprefix('square|').strip()
				if '|' in request:
					image_input, image_output = [e.strip() for e in request.split('|')]
					image_to_square(image_input, image_output)
				else:
					image_to_square(request)
			elif request.startswith('ovl'):
				'''
				/imgutils)ovl|
				==1
				/imgutils)ovl|imgsource|imgoverlay
				==2
				/imgutils)ovl|imgsource|imgoverlay|x,y
				/imgutils)ovl|imgsource|imgoverlay|x,y,scale_or_trans
				/imgutils)ovl|imgsource|imgoverlay|x,y,scale,trans
				/imgutils)ovl|imgsource|imgoverlay|scale
				/imgutils)ovl|imgsource|imgoverlay|trans
				overlay_image(original_image, overlay_image, output_path=None, transparency=1.0, scale_percent=100, x=0.5, y=0.5)
				'''
				request = request.removeprefix('ovl|').strip()
				if '|' in request:
					if request.count('|')==1:
						print(f"1 overlay_image|src|ovl")
						imgsource, imgoverlay = [e.strip() for e in request.split('|')]
						overlay_image(imgsource, imgoverlay)
					elif request.count('|')==2:
						imgsource, imgoverlay, xy = [e.strip() for e in request.split('|')]
						if ',' in xy:
							if xy.count(',')==1: # ...|x,y
								print(f"2 overlay_image|src|ovl|x,y")
								x,y = [float(e.strip()) for e in xy.split(',')]
								overlay_image(imgsource, imgoverlay, x=x, y=y)
							elif xy.count(',')==2: # ...|x,y,scale
								print(f"3 overlay_image|src|ovl|x,y,scale")
								x,y,scale_or_trans = [e.strip() for e in xy.split(',')]
								x=float(x)
								y=float(y)
								if '.' in scale_or_trans:
									overlay_image(imgsource, imgoverlay, x=x,y=y,transparency=float(scale_or_trans))
								else:
									overlay_image(imgsource, imgoverlay, x=x,y=y,scale_percent=int(scale_or_trans))
							elif xy.count(',')==3: # ...|x,y,scale,trans
								print(f"4 overlay_image|src|ovl|x,y,scale,trans")
								x,y,scale,trans = [float(e.strip()) for e in xy.split(',')]
								overlay_image(imgsource, imgoverlay, x=x,y=y,scale_percent=int(scale), transparency=trans)
						elif '.' in xy:
							print(f"5 overlay_image|src|ovl|trans")
							overlay_image(imgsource, imgoverlay, transparency=float(xy))
						else:
							print(f"6 overlay_image|src|ovl|scale")
							overlay_image(imgsource, imgoverlay, scale_percent=int(xy))
				else:
					pass
			elif request.startswith('text'):
				'''
				/imgutils)text|content|fileinput
				/imgutils)text|content|fileinput,fileoutput <= pake koma
				write_text_on_image(text, filepath_input, filepath_output=None, huruf=DEFAULT_FONT, ukuranhuruf=40, warna=(255,255,255))
				'''
				request = request.removeprefix('text|').strip()
				text, fileinput = [item.strip() for item in request.rsplit('|', 1)]
				fileoutput = None
				if ',' in fileinput:
					fileinput, fileoutput = [e.strip() for e in fileinput.split(',')]
				print(f"/imgutils) request = {request}, text = {text}, fileinput = {fileinput}")
				write_text_on_image(text=text, filepath_input=fileinput, filepath_output=fileoutput)

		return

	elif code .startswith('video)'):
		r'''membuat video dari screen capture
		/video)
		/video)outputfilepath
		/video)outputfilepath\timeout

		sekarang ganti gini
		/video)outputfilepath\timeout\<x,y,scale,warna>tulisan|<x,y,scale,warna>tulisan
		'''
		pemisah_item = '\\'
		pemisah_tulisan = '|'
		request = code.removeprefix('video)').strip()
		# video_capture = fullscreen, video_capture_grab = bbox
		from schnell.app.videocapture import video_capture, video_capture_grab
		# fullscreen = False
		penangkap = video_capture_grab
		if request.startswith('*'):
			# fullscreen = True
			request = request.removeprefix('*')
			penangkap = video_capture
		if request:
			request = request.strip()
			if request.startswith('['):
				pass
				# warna, memecode = request.removeprefix('[').split(']', 1)
				# tuple_ = tuple(int(x) for x in warna.split(","))
				# create_and_show_meme(memecode, warna=tuple_)
			else:
				if pemisah_item in request: # ada specify outputfilepath
					if request.count(pemisah_item)==1:
						r'''
						/video)filepath\10 
							timeout 10s
						/video)filepath\30.0
							fps=30
						'''
						filepath, timeout = [item.strip() for item in request.split(pemisah_item)]
						if ',' in timeout:
							# filepath\timeout, fps
							timeout, fps = [item.strip() for item in timeout.split(',')]
							penangkap(filepath, timeout=int(timeout), fps=fps)
						elif '.' in timeout:
							# filepath\fps
							fps = float(timeout)
							penangkap(filepath, fps=fps)
						elif timeout.isdigit():
							# filepath\timeout
							timeout = int(timeout)
							penangkap(filepath, timeout)
					elif request.count(pemisah_item)==2:
						# jika filepath\\timeout\\tulisan|tulisan|tulisan
						filepath, timeout, texts = [item.strip() for item in request.split(pemisah_item)]
						penangkap(filepath, timeout=int(timeout), text=texts)
				else:
					# gak ada pemisah item \ maka cuma /video)30 atau /video) saja
					if request.isdigit():
						'''
						/video)30
						bikin video 30 detik
						'''
						from schnell.app.dirutils import file_under_tempdir
						namafile = file_under_tempdir(ext='.mp4', touch_file=False)
						penangkap(namafile, timeout=int(request))
					else:
						'''
						/video)filepath
						'''
						penangkap(request)
		else:
			'''
			/video)
			'''
			from schnell.app.dirutils import file_under_tempdir
			namafile = file_under_tempdir(ext='.mp4', touch_file=False)
			penangkap(namafile, timeout=10)
		return

	elif code .startswith('vidutils)'):
		'''
		'''
		request = code.removeprefix('vidutils)').strip()
		from schnell.app.videoutils import reverse_mp4, merge_videos, merge_videos_to_gif
		from schnell.app.videoutils2 import add_overlay2, add_overlay3, write_shots, screenshots_grid, create_image_grid3, draw_rectangles_on_video
		from schnell.app.videoutils3 import video_to_images, video_to_clip, video_to_clip_seconds, video_to_images_seconds
		from schnell.app.videoutils4 import images_to_video
		if request:
			request = request.strip()
			if request.startswith('['):
				'''
				'''
				pass
			else:
				if request.startswith('rev'):
					'''
					/vidutils)rev|path
					/vidutils)rev|path|out
					/vidutils)rev|path|fps
					/vidutils)rev|path|out|fps
					'''
					parts = request.split('|')
					if len(parts)==2:
						_, video_inputpath = parts
						reverse_mp4(video_inputpath)
					elif len(parts)==3:
						_, video_inputpath, video_outputpath = parts
						if re.match(r'(\d+(\.\d+)?)', video_outputpath):
							fps = float(video_outputpath)
							reverse_mp4(video_inputpath, fps = fps)
						else:
							reverse_mp4(video_inputpath, video_output = video_outputpath)
					elif len(parts)==4:
						_, video_inputpath, video_outputpath, fps = parts
						reverse_mp4(video_inputpath, video_outputpath, float(fps))

				elif request.startswith('merge'):
					'''
					/vidutils)merge|path1,path2,path3
					'''
					paths = request.removeprefix('merge').strip().removeprefix('|').strip()
					videos = [i.strip() for i in paths.split(',')]
					merge_videos(videos)

				elif request.startswith('2gif'):
					'''
					/vidutils)2gif|gifoutput|path1,path2,path3
					'''
					gifoutput, paths = [e.strip() for e in request.removeprefix('2gif').strip().removeprefix('|').strip().split('|',1)]
					videos = [i.strip() for i in paths.split(',')]
					merge_videos_to_gif(videos, gifoutput)

				elif request.startswith('img2vid'):
					'''
					/vidutils)
						img2vid|
							output|img1,img2,img3
							output|img1,img2,img3|fps
							output|<inputfolder
							output|<inputfolder|fps
					17-1-24 kita ganti |> ke |< krn potongify kanan di fmusperintah
					'''
					request = request.removeprefix('img2vid|').strip()
					vidinput_specchar = '<'
					print('img2vid => request:', request)
					parts = [e.strip() for e in request.split('|')]
					if request.count('|')==2:
						print("jumlah | adlh 2 => ada spec fps dan/atau delay")
						vidoutput, vidinput, fps = parts
						extra_args = {}
						if ',' in fps:
							print("if ',' in fps:")
							for e in [e.strip() for e in fps.split(',')]:
								if '.' in e:
									extra_args['fps'] = float(e)
								else:
									extra_args['delay'] = int(e)
						else:
							if '.' in fps:
								extra_args['fps'] = float(fps)
							else:
								extra_args['delay'] = int(fps)
						if vidinput.startswith(vidinput_specchar):
							print("vidinput.startswith(vidinput_specchar)")
							image_folder = vidinput.removeprefix(vidinput_specchar)
							images_to_video(vidoutput, image_folder=image_folder, **extra_args)
						else:
							print("not/else vidinput.startswith(vidinput_specchar)")
							list_of_images = [e.strip() for e in vidinput.split(',')]
							images_to_video(vidoutput, list_of_images=list_of_images, fps=fps)
					else:
						vidoutput, vidinput = parts
						if vidinput.startswith(vidinput_specchar):
							image_folder = vidinput.removeprefix(vidinput_specchar)
							images_to_video(vidoutput, image_folder=image_folder)
						else:
							list_of_images = [e.strip() for e in vidinput.split(',')]
							images_to_video(vidoutput, list_of_images=list_of_images)

				elif request.startswith('ovl'):
					'''
					/vidutils)ovl|image_to_overlay|videopath
					/vidutils)ovl|image_to_overlay|videopath|x,y
					/vidutils)ovl|image_to_overlay|videopath|scale = 0-100
					/vidutils)ovl|image_to_overlay|videopath|trans = 0.0-1.0
					'''
					request = request.removeprefix('ovl|').strip()
					# image_to_overlay, videopath = [e.strip() for e in request.removeprefix('ovl').strip().removeprefix('|').strip().split('|',1)]
					if request.count('|')==2: # a|b|c
						image_to_overlay, videopath, xy = [e.strip() for e in request.split('|')]
						if ',' in xy:
							if xy.count(',')==1: # ...|x,y
								x,y = [float(e.strip()) for e in xy.split(',')]
								add_overlay2(videopath, image_to_overlay, x=x, y=y)
							elif xy.count(',')==2: # ...|x,y,scale
								x,y,scale = [float(e.strip()) for e in xy.split(',')]
								add_overlay3(videopath, image_to_overlay, x=x,y=y,scale_percent=int(scale))
							elif xy.count(',')==3: # ...|x,y,scale,trans
								x,y,scale,trans = [float(e.strip()) for e in xy.split(',')]
								add_overlay3(videopath, image_to_overlay, x=x,y=y,scale_percent=int(scale), transparency=trans)
						elif '.' in xy:
							# 0.0-1.0 = trans
							add_overlay3(videopath, image_to_overlay, transparency=float(xy))
						else:
							# 0-100 = scale
							add_overlay2(videopath, image_to_overlay, scale_percent=int(xy))
					else: # a|b
						image_to_overlay, videopath = [e.strip() for e in request.split('|')]
						add_overlay2(videopath, image_to_overlay)

				elif request.startswith('shots'):
					'''
					/vidutils)shots|videopath
					/vidutils)shots|videopath|4
					'''
					code = request.removeprefix('shots').strip().removeprefix('|').strip()
					if '|' in code:
						videopath, jumlahshots = [e.strip() for e in code.split('|')]
						videopath = bongkar(videopath)
						write_shots(videopath, int(jumlahshots))
					else:
						videopath = bongkar(code)
						write_shots(videopath)

				elif request.startswith('grid'):
					'''
					/vidutils)grid|imgpath1,imgpath2,imgpath3
					/vidutils)grid|imgpath1,imgpath2,imgpath3|0.3
					'''
					request = request.removeprefix('grid|').strip()
					if '|' in request:
						images, scale = [e.strip() for e in request.split('|')]
						create_image_grid3([e.strip() for e in images.split(',')], float(scale))
					else:
						create_image_grid3([e.strip() for e in request.split(',')])

				elif request.startswith('shotgrid'):
					'''
					/vidutils)shotgrid|videopath
					/vidutils)shotgrid|videopath|4
					/vidutils)shotgrid|videopath|4,.25
					/vidutils)shotgrid|videopath|4,.25|outputpath
					'''
					code = request.removeprefix('shotgrid').strip().removeprefix('|').strip()
					if '|' in code:
						# videopath, jumlahshots = [e.strip() for e in code.split('|')]
						# videopath = bongkar(videopath)
						# write_shots(videopath, int(jumlahshots))
						video_output = None
						scale = 0.25
						numshots = 8
						if code.count('|')==2: # jk ada numshots/scale + outpath
							video_input, spec, video_output = [e.strip() for e in code.split('|')]
							if ',' in spec:
								for item in [e.strip() for e in spec.split(',')]:
									if '.' in item:
										scale = float(item)
									else:
										numshots = int(item)
						else:
							video_input, spec = [e.strip() for e in code.split('|')]
							if ',' in spec:
								for item in [e.strip() for e in spec.split(',')]:
									if '.' in item:
										scale = float(item)
									else:
										numshots = int(item)
						videopath = bongkar(video_input)
						screenshots_grid(videopath, numshots, scale, video_output)
					else:
						videopath = bongkar(code)
						write_shots(videopath)

				elif request.startswith('rect'):
					'''
					/vidutils)rect|inputpath|specs
					/vidutils)rect|inputpath|specs|outputpath
					specs = x,y,w,h
					specs = x,y,w,h,color
					specs = x,y,w,h,color,thickness
					specs = x,y,w,h,color,thickness,fill
					'''
					# draw_rectangles_on_video(input_file, x_percent=0.25, y_percent=0.25, w_percent=0.5, h_percent=0.5, output_file=None, color=(0,255,0), thickness=1, fill=True)
					request = request.removeprefix('rect').strip().removeprefix('|').strip()
					# voutput = None
					allspecs = {
						'x_percent':0.25, 
						'y_percent':0.25, 
						'w_percent':0.5, 
						'h_percent':0.5, 
						'output_file':None, 
						'color':'red', 
						# 'thickness':2,
						'fill': True,
					}
					if '|' in request:
						if request.count('|')==2: # /vidutils)rect|inputpath|specs|outputpath
							vinput, specs, voutput = [e.strip() for e in request.split('|')]
							allspecs['output_file']=voutput
						else: # /vidutils)rect|inputpath|specs
							vinput, specsstr = [e.strip() for e in request.split('|')]
							specs = [e.strip() for e in specsstr.split(',')]
							if len(specs)==4:
								x,y,w,h=[float(e) for e in specs]
								allspecs['x_percent']=x
								allspecs['y_percent']=y
								allspecs['w_percent']=w
								allspecs['h_percent']=h								
							elif len(specs)==5:
								x,y,w,h,color=specs
								allspecs['x_percent']=float(x)
								allspecs['y_percent']=float(y)
								allspecs['w_percent']=float(w)
								allspecs['h_percent']=float(h)
								allspecs['color']=color
							elif len(specs)==6:
								x,y,w,h,color,fill=specs
								allspecs['x_percent']=float(x)
								allspecs['y_percent']=float(y)
								allspecs['w_percent']=float(w)
								allspecs['h_percent']=float(h)
								allspecs['color']=color
								allspecs['fill']=bool(fill)
							# elif len(specs)==7:
							# 	x,y,w,h,color,thick,fill=specs
							# 	allspecs['x_percent']=float(x)
							# 	allspecs['y_percent']=float(y)
							# 	allspecs['w_percent']=float(w)
							# 	allspecs['h_percent']=float(h)
							# 	allspecs['color']=color
							# 	allspecs['thickness']=int(thick)
							# 	allspecs['fill']=bool(fill)
					else:
						vinput = request
					print(f'draw_rectangles_on_video => allspecs =', allspecs)
					draw_rectangles_on_video(vinput, **allspecs)

				elif request.startswith('play'):
					request = request.removeprefix('play|').strip()
					if request:
						from schnell.app.mediautils import internal_video_viewer
						internal_video_viewer(request)

				elif request.startswith('images|'):
					'''
					video_to_images(video_input, start_frame=1, end_frame=-1, output_dir=None)
					/vidutils)images|c:/fr/pertama.mp4
					/vidutils)images|c:/fr/pertama.mp4|10,30
					/vidutils)images|c:/fr/pertama.mp4|10,30|output_images
					/vidutils)images|*c:/fr/pertama.mp4
					'''
					print_frameno = False
					request = request.removeprefix('images|')
					if request.startswith('*'):
						request = request.removeprefix('*').strip()
						print_frameno = True
					if '|' in request:
						if request.count('|')==2: # /vidutils)images|c:/fr/pertama.mp4|10,30|output_dir
							vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
							start, end = [int(e.strip()) for e in frames.split(',')]
							params = [vidinput, start, end, vidoutput]
							video_to_images(*params, print_frameno=print_frameno)
						else: # /vidutils)images|c:/fr/pertama.mp4|10,30
							vidinput, frames = [e.strip() for e in request.split('|')]
							start, end = [int(e.strip()) for e in frames.split(',')]
							params = [vidinput, start, end]
							video_to_images(*params, print_frameno=print_frameno)
					else: # /vidutils)images|c:/fr/pertama.mp4
						video_to_images(request, print_frameno=print_frameno)

				elif request.startswith('clip|'):
					'''
					video_to_clip(video_input, start_frame=1, end_frame=-1, output_dir=None)
					/vidutils)images|c:/fr/pertama.mp4
					/vidutils)images|c:/fr/pertama.mp4|10,30
					/vidutils)images|c:/fr/pertama.mp4|10,30|output_images
					'''
					request = request.removeprefix('clip|')
					if '|' in request:
						if request.count('|')==2: # /vidutils)clip|c:/fr/pertama.mp4|10,30|output_dir
							vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
							start, end = [int(e.strip()) for e in frames.split(',')]
							params = [vidinput, start, end, vidoutput]
							video_to_clip(*params)
						else: # /vidutils)clip|c:/fr/pertama.mp4|10,30
							vidinput, frames = [e.strip() for e in request.split('|')]
							start, end = [int(e.strip()) for e in frames.split(',')]
							params = [vidinput, start, end]
							video_to_clip(*params)
					else: # /vidutils)clip|c:/fr/pertama.mp4
						video_to_clip(request)

				elif request.startswith('images2'):
					'''
					video_to_images_seconds(video_input, start_second=0, end_second=-1)
					/vidutils)images2|c:/fr/pertama.mp4
					/vidutils)images2|c:/fr/pertama.mp4|10,30
					/vidutils)images2|c:/fr/pertama.mp4|10,30|output_images
					'''
					request = request.removeprefix('images2|')
					print_frameno = False
					if request.startswith('*'):
						request = request.removeprefix('*').strip()
						print_frameno = True
					if '|' in request:
						# if request.count('|')==2: # /vidutils)images2|c:/fr/pertama.mp4|10,30|output_dir
						# 	vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
						# 	start, end = [int(e.strip()) for e in frames.split(',')]
						# 	params = [vidinput, start, end, vidoutput]
						# 	video_to_images_seconds(*params)
						# else: # /vidutils)images|c:/fr/pertama.mp4|10,30
							vidinput, frames = [e.strip() for e in request.split('|')]
							start, end = [int(e.strip()) for e in frames.split(',')]
							params = [vidinput, start, end]
							video_to_images_seconds(*params, print_frameno=print_frameno)
					else: # /vidutils)images|c:/fr/pertama.mp4
						video_to_images_seconds(request, print_frameno=print_frameno)

				elif request.startswith('clip2'):
					'''
					video_to_clip_seconds(video_input, start_second=0, end_second=-1)
					/vidutils)clip2|c:/fr/pertama.mp4
					/vidutils)clip2|c:/fr/pertama.mp4|10,30
					/vidutils)clip2|c:/fr/pertama.mp4|10,30|output_images
					'''
					request = request.removeprefix('clip2|')
					if '|' in request:
						# if request.count('|')==2: # /vidutils)clip2|c:/fr/pertama.mp4|10,30|output_dir
						# 	vidinput, frames, vidoutput = [e.strip() for e in request.split('|')]
						# 	start, end = [int(e.strip()) for e in frames.split(',')]
						# 	params = [vidinput, start, end, vidoutput]
						# 	video_to_clip_seconds(*params)
						# else: # /vidutils)clip|c:/fr/pertama.mp4|10,30
							vidinput, frames = [e.strip() for e in request.split('|')]
							start, end = [int(e.strip()) for e in frames.split(',')]
							params = [vidinput, start, end]
							video_to_clip_seconds(*params)
					else: # /vidutils)clip|c:/fr/pertama.mp4
						video_to_clip_seconds(request)
		return

	elif code .startswith('pesan)'):
		'''
		/pesan)body
		/pesan)title|body
		'''
		from schnell.app.promptutils import message_box_application
		code = code.removeprefix('pesan)')
		if '|' in code:
			title, body = code.split('|')
			# message_box_application(title, body)
			alert(title, body)
		else:
			# message_box_application(body=code)
			alert(code)
		return

	elif code .startswith('wait)'):
		tulisan = code.removeprefix('wait)')
		title = '(UNTITLED)'
		if '=' in tulisan:
			title, body = tulisan.split('=',1)
		else:
			body = tulisan
		body = body.replace('\\n', '\n').replace('\\t', '\t')
		alert(body, title)
		return

	elif code.startswith('edit:') or code.startswith('e:'):
		"""
		/edit:aval)
			/edit:aval)file.mk/fmus=barisentry
				if contains .mk= or .fmus=
			/edit:aval)file.txt
				if isvalid path and isexist
			/edit:aval)string content
				else string
		/edit:jup)
			/edit:jup)file.mk/fmus=barisentry
				if contains .mk= or .fmus=
			/edit:jup)file.txt
				if isvalid path and isexist
			/edit:jup)string content
				else string
		"""
		from schnell.app.windoweditorutils import create_editor, get_window_name
		from schnell.autolang import process_language as process_autolang
		editor = code.removeprefix('edit:' if code.startswith('edit:') else 'e:')
		# CURDIR=os.getcwd() # sementara
		CURDIR=item.workdir

		code = editor
		console_name = None
		window_title = ''
		au_code = ''

		if editor.startswith('aval)'):
			editor = editor.removeprefix('aval)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('avalon',CURDIR,console_name)
		elif editor.startswith('jup)'):
			editor = editor.removeprefix('jup)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('jup',CURDIR,console_name)
		elif editor.startswith('np)'):
			editor = editor.removeprefix('np)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('np',CURDIR,console_name)
		elif editor.startswith('alt)'):
			editor = editor.removeprefix('alt)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('alt',CURDIR,console_name)
		elif editor.startswith('plain)'):
			editor = editor.removeprefix('plain)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('plain',CURDIR,console_name)
		elif editor.startswith('pad)'):
			editor = editor.removeprefix('pad)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('pad',CURDIR,console_name)
		elif editor.startswith('ynote)'):
			editor = editor.removeprefix('ynote)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('ynote',CURDIR,console_name)
		elif editor.startswith('rsed)'):
			editor = editor.removeprefix('rsed)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('rsed',CURDIR,console_name)
		elif editor.startswith('rsnone)'):
			editor = editor.removeprefix('rsnone)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('rsnone',CURDIR,console_name)
		elif editor.startswith('goed)'):
			editor = editor.removeprefix('goed)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('goed',CURDIR,console_name)
		elif editor.startswith('gomd)'):
			editor = editor.removeprefix('gomd)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('gomd',CURDIR,console_name)
		elif editor.startswith('goide)'):
			editor = editor.removeprefix('goide)')
			console_name, au_code = get_window_name(editor)
			items, window_title, index_or_none = create_editor('goide',CURDIR,console_name)
		elif editor in ['ls)', 'list)', 'l)']:

			editor_list = json.dumps(programming_data['j']['editors'], indent=2)
			try:
				handle_publish_to_redis(editor_list)
			except:
				pass		
		if au_code:
			if window_title:
				au_code = f"{au_code}(window_title)"
			process_autolang(au_code)
		return

	elif code.startswith('ngetik)'):
		'''
		/ngetik)hello
		/ngetik)*hello (alert dulu, cocok utk milih window sblm ngetik)
		utk ngetik di current window
		'''
		code = code.removeprefix('ngetik)').strip()
		to_write = code
		if not to_write:
			to_write=sample_pandas_code
		elif '.mk=' in code or '.fmus=' in code:
			filepath, barisentry = code.split('=',1)			
			if filepath.startswith('*'):
				filepath = filepath.removeprefix('*')
				alert(to_write[:100]+'...', 'Press OK if cursor has been put inside the area to write')
			to_write = mkfile_entry(filepath, barisentry)
		elif is_valid_path(code) and isabsolute(code) and not '\\n' in code:
			print(f'/ngetik) => to_write = file_content({code})')
			to_write = file_content(code)
			if to_write.startswith('*'):
				to_write = to_write.removeprefix('*')
				alert(to_write[:100]+'...', 'Press OK if cursor has been put inside the area to write')
		to_write = sanitize_chars(to_write) # jangan lupa
		gugu_type(to_write)
		return
	
	elif code.startswith('css)'):
		# ,<		css				b,d,p/p0,m0/
		# ,<header/p0,x0,m0,bsbb
		from schnell.app.transpiler.css.main import process_language
		code = code.removeprefix('css)').strip()
		process_language(code)
		return
	
	elif code.startswith('flutter)'):
		# #ma(tit:txt("monyet",slv:/icsearch),dbg:scaf(body:row(ch:dtab),fab:csv(txt:txt("hello boyz"))),thm:thmd(pmc:/tsfz,ab:sbui),hm:/mqw)
		from schnell.langs.flutter.main import  process_language
		code = code.removeprefix('flutter)').strip()
		process_language(code)
		return

	elif code.startswith('exe='):
		# /: executor
		from schnell.app.executor import LANGUAGES, ExecFile, FileExecutor
		code = code.removeprefix('exe=').strip()
		if code:
			if code in LANGUAGES:
				indah4(f"executing {code}", warna='green')
				# ExecFile.exec(code)
				FileExecutor().exec(code)
			else:
				indah4(f"{code} not in {LANGUAGES}", warna='red')
		return

	elif code.startswith('eng='):
		'''
		load
		123
		/cari
		/*cari-case-sensitive
		/10/cari				10 before, 10 after
		/10*/cari
		/3,0/cari				3 before, 0 after
		#define-word
		*edit-word
		$1			get one randomly
		$1*			get one randomly + definition
		neo
		vert, tion
		'''
		from schnell.db.writer_service import process_writer
		code = code.removeprefix('eng=').strip()
		result = process_writer(code, print_result=True)
		return

	elif code.startswith('json='):  # /json=url|query
		request = code.removeprefix('json=').strip()
		if not request:  # /json=
			hasil = retrieve_and_print_json()
		elif '|' in request:
			url, query = [item.strip() for item in request.split('|',1)]
			hasil = retrieve_and_print_json(url, query)
		else:
			hasil = retrieve_and_print_json(request)
		indah4(json.dumps(hasil, indent=2))
		return

	elif code.startswith('$'):
		# /$ perintah
		# indah4('>>before perintah', warna='cyan')
		request = code.removeprefix('$').strip()
		process_perintah(request, item=item, root_tree=root_tree)
		# indah4('>>after perintah', warna='cyan')
		return

	elif code .startswith('ketik)'):
		r'''
		app.wcmderutils
		create_cmd_and_type_away(CURDIR=None, ketikan=['wsl'], delay_antar_ketikan=0.2)
		../ketik)ketik1|ketik2|ketik3\\CURDIR

		/ketik)pwd|auto:ctrl,shift,t|pwd|cd __CURDIR__|pwd\\c:\tmp\hapus\hapus2

		upd 6-mei-23
		tambah /ketik)[...]

		upd 27-nov-22
		jk ada berikut ini
			.fmus=
			.mk=
		pada item di ketik_list maka ambil content dari fmus file.

		>>> re.search(r'[^:]\\', 'cd c:\kuda')
		>>> re.search(r'[^:]\\', 'satu\dua')
		<re.Match object; span=(3, 5), match='u\\'>

		>>> re.split(r'([^:])\\', 'cd c:\kuda|pwd\c:\kambing')
		['cd c:\\kuda|pw', 'd', 'c:\\kambing']
		if len==3???

		>>> re.split(r'([^:])\\', 'cd c:\kuda|pwd|c:\kambing')
		['cd c:\\kuda|pwd|c:\\kambing']

		# dari comment lama yg ribut
		# harus better dlm split ini, gunakan regex
		# kita jadi gak bisa cd c:\somewhere, cd __PWD, cd __CURDIR gara2 ini
		# pengennya hanya split jk [A-Za-z0-9PUNCS]\\, tapi jangan jk space\\, bisa \S+\\ dong ya...

		# if '\\' in code:
		# if re.search(r'[^:]\\', code):
		# 	ketik_list_curdir = code.split('\\', 1)  # ingat path bisa punya backslash jd hrs max split 1
		# else:
		# 	ketik_list_curdir = [code]

		# add []
		# schnell.app.appconfig/command_prompt_data

		# cek /ketik)[name=...] dan /ketik)[target=...]

		# ketik_list = []
		# if len(ketik_list_curdir) > 1:
		# 	CURDIR = ketik_list_curdir[1].strip()
		# ketik_list = ketik_list_curdir[0].split('|')

		# utk bentuk cd c:\folder \ perintah \ workdingdir, dimana cd c:\folder ini dibutuhkan utk bikin new tab
		# jk ada pembagi \ => satu\dua\tiga
		# >>> re.split(r'([^:])\\', 'cd c:\kuda|pwd\c:\kambing')
		# ['cd c:\\kuda|pw', 'd', 'c:\\kambing']
		# ketik_list_curdir = [pecah_berdasarkan_double_backslash[0]+pecah_berdasarkan_double_backslash[1], pecah_berdasarkan_double_backslash[2]]
		'''
		code = code.removeprefix('ketik)')

		if root_tree:
			code = replace_root_tree_variables(root_tree, code)
		if '__WORKDIR__' in code or '__WORKDIR' in code: # kita kasih special var
			code = code.replace('__WORKDIR__', item.workdir).replace('__WORKDIR', item.workdir)

		console_name=None
		console_target=None
		
		if code.startswith('[') and ']' in code:
			spec, code = code.split(']')
			spec = spec.removeprefix('[')
			for keyval in [kv.strip() for kv in spec.split(',')]:
				'''
				/ketik)[name=whatever]
				/ketik)[target=whatever]
				'''
				if '=' in keyval:
					k,v = [e.strip() for e in keyval.split('=')]
					if k == 'name':
						console_name=v
					elif k == 'target':
						console_target=v
		
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print(f"""[app/quick/__init__:ketik] 
			code = {code}
			console_name = {console_name}
			console_target = {console_target}
			""")

		CURDIR=os.getcwd()

		# jadi double backslash...krn jk c:\tmp\hapus maka terpisah jadi c:\tmp dan hapus
		pecah_berdasarkan_double_backslash = re.split(r'([^:])\\\\', code)
		
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			# pecah_berdasarkan_double_backslash: ['dir', ' ', ' c:\\hapus\\november17\\ChatGPT']
			print('[app/quick/__init__:ketik] pecah_berdasarkan_double_backslash:', pecah_berdasarkan_double_backslash)

		if len(pecah_berdasarkan_double_backslash)==3:
			ketik_list = (pecah_berdasarkan_double_backslash[0]+pecah_berdasarkan_double_backslash[1]).split('|')
			CURDIR = bongkar(pecah_berdasarkan_double_backslash[2].strip())  # perlu strip() krn folder bisa ada space
		else:
			ketik_list = pecah_berdasarkan_double_backslash[0].split('|')

		for idx, ketikan in enumerate(ketik_list):
			if '.fmus=' in ketikan or '.mk=' in ketikan:
				filepath, baris_entry = ketikan.split('=')
				filepath = bongkar(filepath)
				content = get_definition_by_key_permissive_start(filepath, baris_entry)
				if env_int('ULIBPY_FMUS_DEBUG')>1:
					print(f'[app/quick/__init__:ketik] replacing [{ketikan}] dengan [{content}]')
				ketik_list[idx] = content

		CURDIR = bongkar(CURDIR)

		create_cmd_and_type_away(CURDIR=CURDIR,
			   ketikan=[sanitize_chars(text) for text in ketik_list],
			   console_name=console_name, 
			   console_target=console_target)
		return

	try:
		'''
		//
		/i/
		/ls/

		/wp54/1
		/netlify/1
		'''
		pre_parser = Lark(quick_bahasa, start='program')
		parser = pre_parser.parse

		if env_int('ULIBPY_FMUS_DEBUG')>1:
			indah4('='*20 + ' ' + code + '\n', warna='red')

		parsed_tree = parser(code)
		instructions = TheProcessor().transform(parsed_tree)

		for insn in instructions:
			indah4(insn.pretty(), warna='green', layar='black')
			# if env_int('ULIBPY_FMUS_DEBUG')>1:
			# 	indah4(insn.pretty(), warna='green', layar='black')
				
			hasil = handler(insn)

			# indah4(f'[app.quick] res: [{hasil}], config: {program_config}', warna='yellow')
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				indah4(f'[app.quick] res: [{hasil}], config: {program_config}', warna='yellow')

			if 'operation' in program_config:
				if program_config['operation'] == 'list_statement_config_items':
					'''
					u -e/ls/
					'''
					from schnell.app.special import view_file
					basedir = env_get('ULIBPY_BASEDIR')					
					daftarfile = walk_fullpath(basedir)
					filepath = 'app/quick/bahasa.py'
					if platform() in ['win32', 'windows', 'desktop']:
						filepath = 'app\\quick\\bahasa.py'
					view_file(daftarfile, filepath, '// statement config item start', '// statement config item end')
				elif program_config['operation'] == 'info_quick':
					'''
					u -e/i/
					'''
					disini = ayah(__file__, 1)
					filepath = joiner(disini, 'info.txt')					
					filecontent = file_content(filepath)
					indah4(filecontent, warna='white')
			else:
				if 'filepath' in program_config:
					'''
					index.mk sudah digenerate dari index-input.mk
					'''
					# import os
					# from schnell.app.dirutils import get_cwd
					# indah4(f'''[app.quick]
					# 	informasi cwd utk pwd:
					# 	os.get_cwd	: {os.getcwd()}
					# 	get_cwd		: {get_cwd()}
					# 	''', warna='cyan')
					filepath = program_config['filepath']
					baris_entry = program_config['baris_entry']
					program = get_definition_by_key_permissive_start(filepath, baris_entry)
					fmus.set_file_dir_template(filepath)
					fmus.process(program)
					input('[app.quick] Press any key to continue... ')
					program_config = {}

	except Exception as err:
		print(err)
		trace = traceback.format_exc()
		print(trace)


def myrepl(debug=True):
	code = 1
	while code != 'x':
		try:
			# prompt = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			prompt = datetime.datetime.utcnow().isoformat()
			code = input(f'[app.quick] {prompt} >> ')
			code = code.strip()			
			if code == 'bahasa':
				indah4(bahasa, warna='green')
			elif code.startswith('csv='):
				'''
				csv=json2/{@User=#2}username,s
				'''
				# ternyata perintah dan perintah_shell memakan ; pada "username,s ; password,s"
				csvdir = joiner(schnelldir, 'app/transpiler/csv')
				sys.path.append(csvdir)
				code = code.removeprefix('csv=')
				# print(f'FS mengirimkan [{code}]')
				perintahsp_simple(f'python ../csv/main.py {code}')
			elif code != '' and code != 'x':
				# print(f'code adlh: [{code}]')
				process_language(code, debug=debug)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)


if __name__ == '__main__':
	myrepl()
