import os
from .dirutils import joiner
# from .printutils import indah4
from .utils import env_get

envvalues_dir = os.path.abspath(os.path.dirname(__file__))
sidoarjo_relative = os.path.join(envvalues_dir, '../..')
sidoarjo_relative_normalized = os.path.normpath(sidoarjo_relative)
sidoarjo_absolute = os.path.abspath(sidoarjo_relative_normalized)
schnell_relative = os.path.join(envvalues_dir, '../..')
database_relative = os.path.join(sidoarjo_relative, 'database')
datadir_relative = os.path.join(sidoarjo_relative, 'data')
bylangs_relative = os.path.join(database_relative, 'by-langs')

# datadir = env_get('ULIBPY_DATA_FOLDER_ABS')
# if not datadir:
#     if 0:
#         indah4(f'''[envvalues]
#         datadir env_get('ULIBPY_DATA_FOLDER_ABS') = [{datadir}]
#         ''', warna='red')
datadir = datadir_relative

def datadir_():
    return env_get('ULIBPY_DATA_FOLDER_ABS')

def datadir0():
    return joiner(sidoarjo(), 'data')

def github_token():
    return env_get('ULIBPY_GITHUB_TOKEN')

def schnelldir():
    return env_get('ULIBPY_BASEDIR')

def sidoarjo():
    return env_get('ULIBPY_ROOTDIR')

def bylangsdir():
    return env_get('ULIBPY_BYLANGSDIR')

def databasedir():    
    return joiner(sidoarjo(), 'database')

def debuglevel():
    return env_get('ULIBPY_FMUS_DEBUG')

def default_entry():
    # utk repl:1055
    return env_get('ULIBPY_MKFILE_KEY')

def dirjoiner(*daftar):
    """
    filepath = dirjoiner(schnelldir(), 'gui/system/help/README.md')
    perintah_shell(f'code {filepath}')
    """
    return joiner(*daftar)
