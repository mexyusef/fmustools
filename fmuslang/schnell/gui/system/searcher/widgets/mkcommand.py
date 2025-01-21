import functools, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


if __name__ == 'mkcommand':
	import pathlib, sys
	__curfile__ = pathlib.Path(__file__).resolve()
	sidoarjodir_ = __curfile__.parent.parent.parent.parent.parent.parent
	sidoarjodir = str(sidoarjodir_)
	sys.path.append(sidoarjodir)

from schnell.app.appconfig import programming_data
from schnell.app.fmusutils import run_fmus_for_file_in_folder_in_thread
from schnell.gui.system.searcher.widgets.common import get_icon

# create mkcommand_menu
def create_menu_mkcommand(parent):
	menu_cmds = QMenu(parent)
	for label, exepath in sorted(programming_data['perintah'].items()):
		if exepath:
			filepath = exepath['file']
			barisentry = exepath['entry']
			menu_cmds.addAction(
				# QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
				get_icon(),
				label,
				functools.partial(run_fmus_for_file_in_folder_in_thread, os.getcwd(), filepath, barisentry)
			)
	return menu_cmds
