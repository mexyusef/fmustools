from schnell.app.dirutils import (
	joiner, 
	ayah,
)
from schnell.app.utils import env_get, env_exist, platform, isdesktop

from constants import vscode
# CODE = 'code'
CODE = vscode
TERM = 'qterminal'
if platform() == 'termux':
	# CODE = 'vim'
	CODE = 'nano'
elif isdesktop():
	CODE = '"C:/Program Files/Sublime Text 3/sublime_text.exe"'

# help_basedir = joiner(ayah(__file__, 1), 'zhelps')

# loading env lebih lambat dari lines berikut
# help_basedir = env_get('ULIBPY_HELPDIR')
# if not help_basedir:
# 	help_basedir = '/home/usef/danger/ulib/database/zhelps/'
# help_basedir = '/home/usef/danger/ulib/database/zhelps/'
if not env_exist('ULIBPY_ROOTDIR'):
	root_dir = '/home/usef/work/ulibs/database/zhelps'
	# os.path.realpath ( os.path.join(a, os.pardir, os.pardir, os.pardir) )
	# 'C:\\Users\\usef\\work\\sidoarjo
	import os
	disini = os.path.dirname(os.path.abspath(__file__)) # creator
	root_dir = os.path.join(disini, os.pardir, os.pardir) # sido
	# databasedir = os.path.join(disini, 'database')
else:	
	root_dir = env_get('ULIBPY_ROOTDIR')
help_basedir = joiner(root_dir, 'database/zhelps')

template_default_entry = """--% default
--#
"""

template_use_entry = """--% gunakan
--#
"""

template_reverse_entry = """--#

--% """

template_entrify = f"""--% __TITLE__
__TITLE__
--#
"""

template_python_utf8 = f"""# -*- coding: utf-8 -*-
"""

template_index_mk = """--% index/fmus
.,d(/mk)
	$*code __FILE__
	&*showtext=welcome	
--#

--% welcome
Pengenalan proyek.
--#
"""

template_link = """$$link=ULIBPY_SNIPPETS/"""

template_unless = """--% index/fmus
__PWD,d
	~unless[q]
		.,d(/load=__FILE__=index/loop*)
--#

--% index/loop
__PWD,d
	?pick
		@satu
		@dua
		@tiga
--#
"""

template_pick = """--% index/fmus
__PWD,d
	?pick
		@satu
		@dua
		@tiga
--#
"""
