import ctypes
import json
from .utils import is_windows, env_get
library = None
datadir = env_get('ULIBPY_DATA_FOLDER_ABS', '.')

def set_library(libraryname = 'library.so'):
    from .dirutils import joiner
    librarypath = joiner(datadir, libraryname)
    global library
    library = ctypes.cdll.LoadLibrary(librarypath)

if is_windows():
    set_library()

# 00, 0 args, 0 returns
def func00(funcname):
    """
    gofunc tdk terima args dan tdk kembalikan vals
    """
    the_function = getattr(library, funcname) # library.helloWorld
    the_function()


def func0s(funcname):
    """
    gofunc kembalikan 1 retval string
    """
    the_function = getattr(library, funcname) # library.helloWorld
    # .argtypes = [ctypes.c_char_p]
    setattr(library, 'restype', ctypes.c_void_p)
    # args = args.encode('utf8')
    out_original = the_function()
    out_byte_array = ctypes.string_at(out_original)
    result = out_byte_array.decode('utf-8')
    return result


def funcs0(funcname, args):
    """
    gofunc terima 1 arg *C.char berisi string
    """
    the_function = getattr(library, funcname) # library.helloWorld
    # .argtypes = [ctypes.c_char_p]
    setattr(library, 'argtypes', [ctypes.c_char_p])
    args = args.encode('utf-8')
    the_function(args)


def funcj0(funcname, args):
    """
    gofunc terima 1 arg *C.char berisi loadable json document
    """
    the_function = getattr(library, funcname) # library.helloWorld
    # .argtypes = [ctypes.c_char_p]
    setattr(library, 'argtypes', [ctypes.c_char_p])
    args = json.dumps(args).encode('utf-8')
    the_function(args)

# from_json = library.fromJSON
# from_json.argtypes = [ctypes.c_char_p]
# document = {
#     "name": "john",
#     "last_name": "smith"
# }
# from_json(json.dumps(document).encode('utf-8'))
