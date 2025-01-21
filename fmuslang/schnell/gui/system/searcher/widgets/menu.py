from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# rootdir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([rootdir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.insert(0, sidoarjodir)
ULIBPY_BASEDIR = schnelldir
SIDOARJODIR = sidoarjodir

def sidoarjo_menu(self, get_icon):
    self.sidomuncul = QMenu('Sidoarjo', self)
    self.sidomuncul.setIcon(get_icon())
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo', lambda: os.system(
        f'code {SIDOARJODIR}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/codes', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "codes")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/coords', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit various frameworks => coords/draft/readme.txt⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords/draft/readme.txt")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/coords/fullstack', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords/fullstack")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/coords/fullstack/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "coords/fullstack/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/data', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/data/github', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/github")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/data/gui', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/gui")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/gui/README.md⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/gui/README.md")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/gui/PyQt/README.md⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/gui/PyQt/README.md")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open data/kenza', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/kenza")}/'))
    self.sidomuncul.addAction(get_icon(), '🤖Edit sidoarjo/data/kenza/readme.txt⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/kenza/readme.txt")}/'))
    self.sidomuncul.addAction(get_icon(), '🤖Edit sidoarjo/data/kenza-us/dummy.us⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/kenza-us/dummy.us")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/ocr-data/ocr.txt⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/ocr-data/ocr.txt")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/snippets/readme.txt⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/snippets/readme.txt")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/ageh', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/ageh")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/geura', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/geura")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/refcards', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/refcards")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/database/refcards/pyqt5.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/refcards/pyqt5.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/database/refcards/pyqt5_methods.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/refcards/pyqt5_methods.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/database/zhelps', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "database/zhelps")}/'))

    self.sidomuncul.addAction(get_icon(), '😀Edit mkhelp/next.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "mkhelp/next.mk")}/'))

    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/app', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/wmc.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/wmc.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/fmus/fmus.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/fmus/fmus.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/fmus/generator.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/fmus/generator.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/fmus/processor.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/fmus/processor.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/quick/blitz/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/quick/blitz/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/quick/dahsyater.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/quick/dahsyater.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/quick/languages/guilang.py⚡🏞️', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/quick/languages/guilang.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/app/transpiler', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fullstack.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fullstack.py")}/'))

    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fslang/django/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fslang/django/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fslang/django/index-input.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fslang/django/index-input.mk")}/'))

    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/frontend/fslang/node_antd/__init__.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/frontend/fslang/node_antd/__init__.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/app/transpiler/mycsv/main.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/mycsv/main.py")}/'))

    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit (old) gui/clock/clock.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/clock/clock.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui/system', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui/system/help', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/help")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/gui/system/help/helper.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/help/helper.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/schnell/gui/system/launcher/mmm.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/launcher/mmm.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Open sidoarjo/schnell/gui/system/searcher', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/searcher.py⚡🔎', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/searcher.py")}/'))

    self.sidomuncul.addAction(get_icon(), 'Edit (new) gui/system/searcher/widgets/clock.py⚡⏰', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/clock.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/widgets/config.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/config.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/widgets/creator.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/creator.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/widgets/filetreewidget.py⚡📁', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/filetreewidget.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/widgets/fm.py⚡📁', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/fm.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/widgets/menu.py⚡🌶️', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/menu.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit gui/system/searcher/widgets/newcmder.py⚡🎮', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/gui/system/searcher/widgets/newcmder.py")}/'))

    self.sidomuncul.addAction(get_icon(), 'Edit csv-rootnode schnell.langs.ucsv.grammar.grammar.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/langs/ucsv/grammar/grammar.py")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit csv-string/list schnell.app.transpiler.mycsv.csv_operation.py⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "schnell/app/transpiler/mycsv/csv_operation.py")}/'))

    self.sidomuncul.addAction(get_icon(), '💪💪💪providers/readme.txt⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/readme.txt")}/'))
    self.sidomuncul.addAction(get_icon(), 'providers/directories/batchers.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/directories/batchers.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'providers/directories/snippets.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/directories/snippets.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'Edit sidoarjo/data/snippets/readme.txt⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "data/snippets/readme.txt")}/'))
    self.sidomuncul.addAction(get_icon(), 'providers/files/capcay.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/files/capcay.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'providers/languages/ts.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/languages/ts.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'providers/models/predefined_commands.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/models/predefined_commands.mk")}/'))
    self.sidomuncul.addAction(get_icon(), 'providers/models/tables.mk⚡', lambda: os.system(
        f'code {os.path.join(SIDOARJODIR, "providers/models/tables.mk")}/'))

    self.sidomuncul.addAction(get_icon(), 'Open C:/src/', lambda: os.system(
        f'code C:/src/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/src/flet-flutter/', lambda: os.system(
        f'code C:/src/flet-flutter/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/oprek/', lambda: os.system(
        f'code C:/src/oprek/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/verwijderen/', lambda: os.system(
        f'code C:/verwijderen/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/work/fmusify/', lambda: os.system(
        f'code C:/work/fmusify/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/work/github/', lambda: os.system(
        f'code C:/work/github/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/work/github/go/', lambda: os.system(
        f'code C:/work/github/go/'))
    self.sidomuncul.addAction(get_icon(), 'Open C:/work/upw/', lambda: os.system(
        f'code C:/work/upw/'))
    return self.sidomuncul

# try:
#     from schnell.gui.system.searcher.menu_runner import running
# except Exception as err:
#     sys.path.append('..')
#     # print('exception:', err)
#     # print('name:', __name__)
#     # print('package:', __package__)
#     # import menu_runner
#     __package__ = 'menu_runner'
#     print('start to import relatively')
#     from menu_runner import running
#     print('end to import relatively')

from schnell.gui.system.searcher.menu_runner import running

def runner_menu(self, get_icon):
    """    
    self = CornerWidget
    """
    self._runnermenu = QMenu('Run commands', self)
    self._runnermenu.setIcon(get_icon())
    self._runnermenu.addAction(get_icon(), 'l ff', lambda: running('l ff'))
    self._runnermenu.addSeparator()
    self._runnermenu.addAction(get_icon(), 'MMM', lambda: running('m'))
    self._runnermenu.addAction(get_icon(), 'Helper', lambda: running('h'))
    # if hasattr(self, 'parent') and hasattr(self.parent, 'toggle_cmder_action_visibility'):
    #     self._runnermenu.addAction(get_icon(), 'Cmder', self.parent.toggle_cmder_action_visibility)
    return self._runnermenu
