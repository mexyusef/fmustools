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

from schnell.app.dirutils import normy, explore, joiner, files_filter, joinhere, basename
from schnell.gui.system.searcher.widgets.common import (
    mkhelp_initial_path,
)
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget
from schnell.app.jsonutils import json_loads, json_dumps, json_file_content
from schnell.gui.system.searcher.widgets.quickconfigurable import QuickConfigurableWidget


class QuickBundleWidget(QWidget):

    def __init__(self, configs=[]):
        super().__init__()
        self.configs = configs
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_tab = TabWidget(self)

        for config in self.configs:
            starter = ('quick-' if config.startswith('quick-') 
                else ('epmus-' if config.startswith('epmus-') else 'others-')
                )
            prefix = ('Q ' if starter == 'quick-'
                else ('E ' if starter == 'epmus-' else 'O ')
                )
            quick_config = QuickConfigurableWidget(config)
            judul = prefix + basename(config.removesuffix('.json').removeprefix(starter))
            self.main_tab.addTab(quick_config, judul)

        self.main_layout.addWidget(self.main_tab)
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = TabWidget()
    w.addTab(QWidget(), "tab1 bisa nama panjang kah")
    w.addTab(QWidget(), "tab2")
    w.addTab(QWidget(), "tab3 coba panjang juga")
    w.show()

    sys.exit(app.exec_())
