import os, sys, functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui, QtWidgets

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

from schnell.app.dirutils import normy, explore, joiner, files_filter, joinhere, is_absolute, bongkar, is_relative, basename
from schnell.gui.system.searcher.widgets.common import (
    mkhelp_initial_path,
)
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget
from schnell.gui.system.searcher.widgets.common import MkfileButton
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget
from schnell.app.jsonutils import json_loads, json_dumps, json_file_content


class QuickConfigurableWidget(QWidget):

    def __init__(self, config='quick1.json'):
        super().__init__()
        self.config = config
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_tab = TabWidget(self)
        # configfile = joinhere(__file__, self.config)
        # configfile = self.config if is_absolute(bongkar(self.config)) else joinhere(__file__, self.config)
        if self.config.startswith('ULIBPY'):
            self.config = bongkar(self.config)
        configfile = joinhere(__file__, self.config) if is_relative(self.config) else self.config
        # print(f'QuickConfigurableWidget => configfile = {configfile}')
        configuration = json_file_content(configfile)
        # self.tabs = []
        # tiap entry misalnya
        # {
        #     "name": "Android",
        #     "path": "database/quicks/mobile/androidkotlin",
        #     "extras": []
        # }
        for entry in configuration:
            provider_list = [MkfileButton(f'ULIBPY_ROOTDIR/{item}') for item in entry['extras']]
            extra_buttons = [item.get_button() for item in provider_list]
            tab = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, entry['path']), extra_buttons=extra_buttons)
            # tab = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, entry['path']), extra_buttons_to_connect_to_editor=provider_list)
            self.main_tab.addTab(tab, entry['name'])

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
