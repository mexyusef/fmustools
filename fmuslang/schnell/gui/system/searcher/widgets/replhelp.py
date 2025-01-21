import os, sys
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# rootdir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([rootdir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
# schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)
# from schnell.db.myredis import redis_repl
from schnell.app.fmusutils import fmus
from schnell.app.dirutils import tempdir
from schnell.app.stringutils import newlinify

# /%$*filename.py

# elif text.startswith('/'):
#     from db import redis_repl
#     code = text.replace('/', '', 1).strip()
#     redis_repl(code, self)

# elif text .startswith('..'):
#     program = text.removeprefix('..').lstrip()
#     # indah4(f'[repl] fm/ => [{program}]', warna='yellow')
#     fmus.set_dir_template(tempdir())
#     fmus.process(newlinify(program))


def search_edit(program, prefix='/%$*'):
    """
    /%$*redisutils.py
    tinggal masukkan "redisutils.py"
    """
    program = prefix + program
    fmus.set_dir_template(tempdir())
    fmus.process(newlinify(program))
