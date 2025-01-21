import inspect, importlib
import os, site, sys

# from schnell.gui.system.searcher.filehelper import file_content
# import importlib, sys

if __name__ == 'make_py_help':
	from filehelper import walk_fullpath, file_content
	from make_redis_help import redis_config, try_redis_connect, redis_deletes
else:
	from gui.system.searcher.filehelper import walk_fullpath, file_content
	from gui.system.searcher.make_redis_help import redis_config, try_redis_connect, redis_deletes

def python_package(pkg):
	# https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
	
	package = importlib.import_module(pkg)
	if package:
		lokasi_file = inspect.getfile(package)
		lokasi = os.path.dirname(lokasi_file)
		return lokasi

	return None

def site_packages(packages=['PyQt5']):
	"""
	https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
	(there are more)

	harusnya ambil dari sini...
	C:/Users/usef/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages/PyQt5

	'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.1520.0_x64__qbz5n2kfra8p0', 
	'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.1520.0_x64__qbz5n2kfra8p0\\lib\\site-packages'
	"""
	base = r"C:\Users\usef\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages"
	# return site.getsitepackages()
	return [os.path.join(base, item) for item in packages]


PYWALKER_PREFIX='pywalker:'

def all_python_files():
	# self_paths = []
	# for path in site_packages():
	#     path = os.path.expandvars(path)
	#     if os.path.exists(path):
	#         for filename in os.listdir(path):
	#             _, ext = os.path.splitext(filename)
	#             if ext in ['.exe', '.cmd', '.bat', '.lnk']:
	#                 self_paths.append(os.path.join(path, filename))
	# return self_paths
	pypaths = []
	for basepath in site_packages():
		pypaths.extend(walk_fullpath(basepath, filtered_ends=['.py', '.pyi']))
	# print('all_python_files sepanjang:', len(pypaths))
	return pypaths

"""
cek ada keys
jk kosong load keys
"""

# def all_redis_keys(r, keys=f'{PYWALKER_PREFIX}*'):
# 	return [item.decode('utf8') for item in r.keys(keys)]

def all_python_files_from_redis():
	check_keys = redis_config['r3'].keys(f'{PYWALKER_PREFIX}*')
	check_values = []
	if not check_keys:
		print(f"check_keys empty, nulis filesystem ke redis...START")
		check_values = all_python_files()
		# harusnya berikut ini masuk ke thread/QThread 
		for pyfile in check_values:
			superkey = PYWALKER_PREFIX + pyfile
			redis_config['r3'].set(superkey, pyfile)
			# check_values.append(redis_config['r3'].get(k))
		print(f"check_keys empty, nulis filesystem ke redis...END")
	else:
		for k in check_keys:
			check_values.append(redis_config['r3'].get(k).decode('utf8'))
	return check_values


def pyload():
	# newpath = isdir(code)
	redis_deletes(redis_config['r3'], f'{PYWALKER_PREFIX}*', confirm=False)
	all_python_files_from_redis()
	print(f'pyload selesai...')


# https://stackoverflow.com/questions/19009932/import-arbitrary-python-source-file-python-3-3
# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly

def parentize(innerfunc):
	@functools.wraps(innerfunc)
	def wrapper(filepath, times):
		nilai = filepath
		while times > 0:
			nilai = os.path.join(nilai, os.path.pardir)
			times -= 1
		return nilai
	return wrapper

import functools

def normalize(innerfunc):
	@functools.wraps(innerfunc)
	def wrapper(*args):
		return os.path.normpath(innerfunc(*args))
	return wrapper

@normalize
@parentize
def ayah(filepath, times=1):
	return filepath



def myimport_lib(MODULE_PATH):
	if MODULE_PATH.endswith('.pyi'):
		return file_content(MODULE_PATH)
	_, module_tofind = MODULE_PATH.split('site-packages')
	module_tofind = module_tofind.replace('\\', '.').removeprefix('.').removesuffix('.py')
	supermodule = module_tofind.split('.') [0]
	if module_tofind.endswith('.__init__'):
		module_tofind = module_tofind.removesuffix('.__init__')
	print('modulepath:', MODULE_PATH, 'module_tofind:', module_tofind, 'supermodule:', supermodule)
	# hasil = importlib.import_module(supermodule)
	hasil = importlib.import_module(module_tofind)
	content = [item for item in dir(hasil) if not item.startswith('__')] # hasil berupa list
	return '\n'.join(content)

# def import_module(MODULE_PATH, MODULE_NAME=''):
# 	"""
# 	'generator': '/home/usef/work/ulibs/schnell/app/transpiler/frontend/fslang/z/quick/campur/wp5/wd4/__init__.py', 
# 	'fmusfile': '/home/usef/work/ulibs/schnell/app/transpiler/frontend/fslang/z/quick/campur/wp5/wd4/index-input.mk'

# 	spec_from_file_location(name, 
# 	                        location=None, 
# 							*, <- sering lihat gini, ini artinya positional args kan ya...
# 							loader=None,
#                             submodule_search_locations=_POPULATE)
# 	Return a module spec based on a file location.

#     To indicate that the module is a package, set
#     submodule_search_locations to a list of directory paths.
# 	An empty list is sufficient, though its not otherwise useful to the import system.

#     The loader must take a spec as its only __init__() arg.
# 	"""
# 	# https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
# 	# MODULE_PATH = "/path/to/your/module/__init__.py"
# 	# MODULE_NAME = "mymodule"

# 	if not MODULE_NAME:
# 		# c__users_usef_appdata_local_packages_pythonsoftwarefoundation
# 		MODULE_NAME = MODULE_PATH.replace(os.pathsep, '_').replace(':', '_').replace('\\', '_').lower()
# 		MODULE_NAME = MODULE_NAME[len(MODULE_NAME)-50:]
		
# 		_, module_tofind = MODULE_PATH.split('site-packages')
# 		module_tofind = module_tofind.replace('\\', '.').removeprefix('.').removesuffix('.py')
# 		print('modulepath:', MODULE_PATH, 'module_tofind:', module_tofind)
# 		# harusnya coba
# 		# stlh site-packages
		
	

# 	spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)

# 	if not spec:
# 		# from .dirutils import ayah
# 		print('[app.utils] respeccing...')
# 		submodule_search_locations = ayah(MODULE_PATH,1)
# 		spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH, submodule_search_locations=(submodule_search_locations,))
# 		if not spec:
# 			from importlib._bootstrap_external import _get_supported_file_loaders
# 			a = _get_supported_file_loaders()
# 			print('[app.utils] double respeccing...')
# 			print(a)

# 	# print(f'''[utils/import_module]
# 	# MODULE_NAME	= {MODULE_NAME}
# 	# MODULE_PATH	= {MODULE_PATH}
# 	# spec = {spec}
# 	# ''')

# 	module = importlib.util.module_from_spec(spec)
# 	sys.modules[spec.name] = module
# 	module = spec.loader.exec_module(module)
# 	return module

# def load_module(file_path, module_name=''):
# 	if not module_name:
# 		module_name = file_path.replace(os.pathsep, '_')

# 	print('load_module:', file_path)
# 	spec = importlib.util.spec_from_file_location(module_name, file_path)
# 	module = importlib.util.module_from_spec(spec)
# 	sys.modules[module_name] = module
# 	res = spec.loader.exec_module(module)
# 	return res

