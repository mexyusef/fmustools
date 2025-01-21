import os, sys, functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([sidoarjodir, schnelldir])

# https://stackoverflow.com/questions/46607298/pyqt-qtabwidget-horizontal-tab-and-horizontal-text-in-qtdesigner
# https://stackoverflow.com/questions/51230544/pyqt5-how-to-set-tabwidget-west-but-keep-the-text-horizontal

from schnell.app.dirutils import normy, explore, joiner, files_filter
from schnell.gui.system.searcher.widgets.common import (
    mkhelp_initial_path,
)
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget


# C:\Users\usef\work\sidoarjo\database\quicks
QUICKS_DIR = joiner(sidoarjodir, 'database/quicks')
# C:\Users\usef\work\sidoarjo\database\quicks\reactjs\boot.mk
# C:\Users\usef\work\sidoarjo\database\quicks\nodejs\boot.mk
# C:\Users\usef\work\sidoarjo\database\quicks\nextjs\boot.mk
# C:\Users\usef\work\sidoarjo\database\quicks\nestjs\boot.mk
REACT_DIR = joiner(QUICKS_DIR, 'reactjs')
NODE_DIR = joiner(QUICKS_DIR, 'nodejs')
NEXT_DIR = joiner(QUICKS_DIR, 'nextjs')
NEST_DIR = joiner(QUICKS_DIR, 'nestjs')
QUARKUS_DIR = joiner(QUICKS_DIR, 'quarkus')
SPRINGBOOT_DIR = joiner(QUICKS_DIR, 'springboot')
GINGONIC_DIR = joiner(QUICKS_DIR, 'gingonic')
PLAY_DIR = joiner(QUICKS_DIR, 'playframework')
JAKARTA_DIR = joiner(QUICKS_DIR, 'jakartaee')
WARP_DIR = joiner(QUICKS_DIR, 'rswarp')


class DailyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_tab = TabWidget(letak=1, parent=self)

        self.tab_daily = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'database/daily'), extra_buttons=[])
        self.main_tab.addTab(self.tab_daily, 'Daily practice')

        self.tab_perjalanan = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'data/karya/perjalanan'), extra_buttons=[], lexer='md')
        self.main_tab.addTab(self.tab_perjalanan, 'Perjalanan/Menulis')

        # kenza_folder_button = QPushButton('Code kenza')
        # kenza_folder_button.clicked.connect(lambda: os.system(f"code {sidoarjodir}/data/kenza"))
        # explore_kenza_folder_button = QPushButton('Explorer kenza')
        # explore_kenza_folder_button.clicked.connect(lambda: os.system(f"explorer {sidoarjodir}/data/kenza".replace('/', '\\')))
        # self.tab_karya = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'data/karya'), copy_after_insert=True, extra_buttons=[kenza_folder_button, explore_kenza_folder_button])
        # self.main_tab.addTab(self.tab_karya, 'Karya')

        # # C:\Users\usef\work\sidoarjo\database\streaming
        # self.tab_streaming = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'database/streaming'), copy_after_insert=True, extra_buttons=[])
        # self.main_tab.addTab(self.tab_streaming, 'Streaming')

        # self.tab_karya = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'database/geura/memorizer'), copy_after_insert=True, extra_buttons=[])
        # self.main_tab.addTab(self.tab_karya, 'Memo')

        # self.tab_mkhelp = MKHelpWidget(parent=self, rootpath=mkhelp_initial_path)
        # self.main_tab.addTab(self.tab_mkhelp, 'Help MK2')

        # # system mkhelp
        # # system = database, data model = table
        # self.tab_system = MKHelpWidget(parent=self, rootpath=f'{sidoarjodir}/data/system')
        # self.main_tab.addTab(self.tab_system, 'System')

        # self.tab_datamodel = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'data/model-data'), extra_buttons=[])
        # self.main_tab.addTab(self.tab_datamodel, 'Data models')

        # vampire_button = QPushButton('Open /src/vamp')
        # vampire_button.clicked.connect(lambda: os.system(f"code \\src\\vamp"))
        # self.tab_vampire = MKHelpWidget(parent=self,
        #     rootpath=joiner(sidoarjodir, 'data/vamp'),
        #     extra_buttons=[vampire_button]
        # )
        # self.main_tab.addTab(self.tab_vampire, 'Vamp')

        self.main_layout.addWidget(self.main_tab)
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = DailyWidget()
    w.show()

    sys.exit(app.exec_())
