import os, sys, functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([sidoarjodir, schnelldir])

from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

# https://stackoverflow.com/questions/46607298/pyqt-qtabwidget-horizontal-tab-and-horizontal-text-in-qtdesigner
# https://stackoverflow.com/questions/51230544/pyqt5-how-to-set-tabwidget-west-but-keep-the-text-horizontal

from schnell.app.dirutils import normy, explore, joiner, files_filter
from schnell.gui.system.searcher.widgets.common import (
    mkhelp_initial_path,
)
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget


QUICKS_DIR = joiner(sidoarjodir, 'database/quicks')
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


class QuickWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_tab = TabWidget(self)

        # REACT_DIR = joiner(QUICKS_DIR, 'reactjs')
        self.tab1 = MKHelpWidget(parent=self, rootpath=REACT_DIR)
        self.main_tab.addTab(self.tab1, 'react')
        # NODE_DIR = joiner(QUICKS_DIR, 'nodejs')
        self.tab2 = MKHelpWidget(parent=self, rootpath=NODE_DIR)
        self.main_tab.addTab(self.tab2, 'node')
        # NEXT_DIR = joiner(QUICKS_DIR, 'nextjs')
        self.tab3 = MKHelpWidget(parent=self, rootpath=NEXT_DIR)
        self.main_tab.addTab(self.tab3, 'next')
        # NEST_DIR = joiner(QUICKS_DIR, 'nestjs')
        self.tab4 = MKHelpWidget(parent=self, rootpath=NEST_DIR)
        self.main_tab.addTab(self.tab4, 'nest')
        self.tablang3 = MKHelpWidget(parent=self, rootpath=joiner(QUICKS_DIR, 'languages/typescript'))
        self.main_tab.addTab(self.tablang3, 'TS')

        self.tablang7 = MKHelpWidget(parent=self, rootpath=joiner(QUICKS_DIR, 'languages/c++'))
        self.main_tab.addTab(self.tablang7, 'C++')
        self.tablang4 = MKHelpWidget(parent=self, rootpath=joiner(QUICKS_DIR, 'languages/golang'))
        self.main_tab.addTab(self.tablang4, 'GO')
        self.tablang5 = MKHelpWidget(parent=self, rootpath=joiner(QUICKS_DIR, 'languages/rust'))
        self.main_tab.addTab(self.tablang5, 'RS')
        self.tablang6 = MKHelpWidget(parent=self, rootpath=joiner(QUICKS_DIR, 'languages/scala'))
        self.main_tab.addTab(self.tablang6, 'scala')
        self.tab8 = MKHelpWidget(parent=self, rootpath=PLAY_DIR)
        self.main_tab.addTab(self.tab8, 'play')
        self.tablang6b = MKHelpWidget(parent=self, rootpath=joiner(QUICKS_DIR, 'languages/haskell'))
        self.main_tab.addTab(self.tablang6b, 'haskell')

        self.main_layout.addWidget(self.main_tab)
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = TabWidget()
    w.addTab(QtWidgets.QWidget(), "tab1 bisa nama panjang kah")
    w.addTab(QtWidgets.QWidget(), "tab2")
    w.addTab(QtWidgets.QWidget(), "tab3 coba panjang juga")
    w.show()

    sys.exit(app.exec_())
