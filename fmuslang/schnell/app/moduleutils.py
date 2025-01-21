# https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-module
from importlib import import_module as std_import_module
from importlib import metadata
from inspect import getmembers, isfunction
import os, site, sys


def print_functions(moduleobj, warna=True):
    from .printutils import print_list_warna
    funcs = get_functions(moduleobj)
    nama_fungsi = [item[0] for item in funcs]
    if warna:
        print_list_warna(nama_fungsi)
    else:
        print('\n'.join(nama_fungsi))


def get_functions(moduleobj):
    """
    contoh pake di upy:
    >>> from schnell.app.moduleutils import get_functions
    >>> from schnell.app.moduleutils import get_functions as gf
    >>> import app.redisutils as aru
    >>> gf(aru)

    >>> import os
    >>> import sys
    >>> from importlib import import_module as im
    >>> from inspect import getmembers, isfunction

    >>> basedir = 'c:/users/usef/work/sidoarjo/data/scheduler'
    >>> os.listdir(basedir)
    ['ticker.py', '__init__.py']        
    >>> sys.path.append(basedir)

    >>> im('ticker')
    <module 'ticker' from 'c:\\users/usef/work/sidoarjo/data/scheduler\\ticker.py'>
    >>> m = im('ticker')
    
    >>> getmembers(m, isfunction)
    [('tick', <function tick at 0x00000202B9B14DC0>)]
    >>> getmembers(m, isfunction)[0][1]()
    Tick! The time is: 2022-06-15 11:46:49.713904

    kembalikan list of tuples, dg masing2 tuple adlh (namafungsi, callable-fungsi)
    """
    return getmembers(moduleobj, isfunction)


def get_functions_from_basedir(basedir, filename_without_py, switch_item_in_tuples=True):
    """
    [('tick', <function tick at 0x00000202B9B14DC0>)]

    >>> basedir = 'c:/users/usef/work/sidoarjo/data/scheduler'
    >>> os.listdir(basedir)
    ['ticker.py', '__init__.py']        
    >>> sys.path.append(basedir)
    >>> m = im('ticker')
    """
    if basedir not in sys.path:
        sys.path.append(basedir)
    moduleobj = std_import_module(filename_without_py)
    list_of_tuples = getmembers(moduleobj, isfunction)
    if switch_item_in_tuples:
        from .collutils import balik_list_of_pairs
        list_of_tuples = balik_list_of_pairs(list_of_tuples)
    return list_of_tuples


def get_functions_from_filename(filename_without_py, switch_item_in_tuples=True):
    """
    [('tick', <function tick at 0x00000202B9B14DC0>)]
    """
    # sys.path.append(basedir)
    moduleobj = std_import_module(filename_without_py)
    list_of_tuples = getmembers(moduleobj, isfunction)
    if switch_item_in_tuples:
        from .collutils import balik_list_of_pairs
        list_of_tuples = balik_list_of_pairs(list_of_tuples)
    return list_of_tuples


def get_function_from_name(function_name, filename='scheduler', basedir=None):
    from .dirutils import joiner
    from .utils import env_get
    if basedir is None:
        basedir = joiner(env_get('ULIBPY_DATA_FOLDER_ABS'), 'scheduler')
    print(f"""[app.moduleutils][get_function_from_name]
    basedir = {basedir}
    filename = {filename}
    function_name = {function_name}
    """)
    tuple_fungsi = get_functions_from_basedir(basedir, filename, switch_item_in_tuples=False)
    peroleh = [item[1] for item in tuple_fungsi if function_name==item[0]]
    if peroleh:
        return peroleh[0]
    return None


def import_from_string(fq_classname):
	"""
	fq_classname = app.transpiler.frontend.fslang.flask.Coordinator

	module:
		app.transpiler.frontend.fslang.flask
	class_name:
		Coordinator
	krn teknik berikut
		module_path, class_name = fq_classname.rsplit('.', 1)
	kita juga bisa:
		app.notfutils.pynotif
		dimana pynotif adlh fungsi
		import_from_string('app.notfutils.pynotif')(judul, badan)
	class_str: str = 'A.B.YourClass'
	"""	
	try:
		module_path, class_name = fq_classname.rsplit('.', 1)
		module = std_import_module(module_path)
		return getattr(module, class_name)
	except (ImportError, AttributeError) as e:
		raise ImportError(fq_classname)


def import_module_original(dotted_filepath, redot=False):
	"""
	import_module_original('a/b/c/d', redot=True)
	import_module_original('a.b.c.d')
	"""

	if redot:
		dotted_filepath = dotted_filepath.replace('/', '.')
	module = std_import_module(dotted_filepath)
	return module


def import_module(MODULE_NAME, MODULE_PATH):
	"""
	'generator': '/home/usef/work/ulibs/schnell/app/transpiler/frontend/fslang/z/quick/campur/wp5/wd4/__init__.py', 
	'fmusfile': '/home/usef/work/ulibs/schnell/app/transpiler/frontend/fslang/z/quick/campur/wp5/wd4/index-input.mk'

	spec_from_file_location(name, 
	                        location=None, 
							*, <- sering lihat gini, ini artinya positional args kan ya...
							loader=None,
                            submodule_search_locations=_POPULATE)
	Return a module spec based on a file location.

    To indicate that the module is a package, set
    submodule_search_locations to a list of directory paths.
	An empty list is sufficient, though its not otherwise useful to the import system.

    The loader must take a spec as its only __init__() arg.
	"""
	# https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
	# MODULE_PATH = "/path/to/your/module/__init__.py"
	# MODULE_NAME = "mymodule"
	import importlib, sys

	spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)

	if not spec:
		from .dirutils import ayah
		print('[app.utils] respeccing...')
		submodule_search_locations = ayah(MODULE_PATH,1)
		spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH, submodule_search_locations=(submodule_search_locations,))
		if not spec:
			from importlib._bootstrap_external import _get_supported_file_loaders
			a = _get_supported_file_loaders()
			print('[app.utils] double respeccing...')
			print(a)

	# print(f'''[utils/import_module]
	# MODULE_NAME	= {MODULE_NAME}
	# MODULE_PATH	= {MODULE_PATH}
	# spec = {spec}
	# ''')

	module = importlib.util.module_from_spec(spec)
	sys.modules[spec.name] = module
	spec.loader.exec_module(module)
	return module


def python_package(pkg):
	# https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
	import inspect, importlib
	package = importlib.import_module(pkg)
	if package:
		lokasi_file = inspect.getfile(package)
		lokasi = os.path.dirname(lokasi_file)
		return lokasi

	return None

def site_packages():
    """
    https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
    (there are more)
    """
    return site.getsitepackages()


def package_version(package_name):
    return metadata.version(package_name)

