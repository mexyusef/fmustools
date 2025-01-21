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
# schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

from schnell.app.dirutils import normy, explore, joiner, files_filter, joinhere, is_absolute, bongkar, is_relative, basename
if __name__ == '__main__':
    from startup import initialize_programming_data
    initialize_programming_data()
from schnell.gui.system.searcher.widgets.dahsyatwidget import DahsyaterWidget
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget
# from schnell.app.jsonutils import json_loads, json_dumps, json_file_content
from schnell.gui.system.searcher.widgets.github.repoall import RepoAllWindow
# from schnell.gui.system.searcher.widgets.fmdata import guilang_items, fmdata
from schnell.gui.system.searcher.widgets.fakerlang import FakerlangWidget
from schnell.gui.system.searcher.widgets.csvlang import CsvlangWidget
from schnell.gui.system.searcher.widgets.replang import ReplangWidget
from schnell.gui.system.searcher.widgets.framelang import FramelangWidget
from schnell.gui.system.searcher.widgets.colorwidget import ColorWidget
from schnell.gui.system.searcher.widgets.buttonwidget import ButtonWidget
from schnell.gui.system.searcher.widgets.cmderwidget import CmderWidget
from schnell.gui.system.searcher.widgets.windower import WindowerWidget
from schnell.gui.system.searcher.widgets.lalangwidget import LalangWidget


class QuickLangsWidget(QWidget):

    def __init__(self):
        super().__init__()
        # self.config = config
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_tab = TabWidget(self)

        self.tab_dahsyater = DahsyaterWidget()
        self.tab_dahsyater.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.tab_dahsyater, 'Dahsyater')
        self.csvlanger = CsvlangWidget()
        # self.csvlanger.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.csvlanger, 'Csvlang')
        self.replanger = ReplangWidget()
        self.replanger.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.replanger, 'Replang')
        self.framelanger = FramelangWidget()
        self.framelanger.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.framelanger, 'Framework lang')
        self.tab_lalangwidget = LalangWidget()
        self.tab_lalangwidget.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.tab_lalangwidget, 'Lalang')
        self.tab_fakerlang = FakerlangWidget()
        self.tab_fakerlang.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.tab_fakerlang, 'Fakerlang')

        # self.tab_cmder = QWidget(self)
        # self.tab_cmder.setStyleSheet('background-color: tan;')
        # layout_for_tab_cmder = QVBoxLayout(self.tab_cmder) # utk content tab 2
        # layout_for_tab_cmder.addWidget(self.cmder)
        self.color_widget = ColorWidget()
        self.button_widget = ButtonWidget()
        self.cmder = CmderWidget()
        cmder_color = QSplitter(Qt.Horizontal)
        cmder_color.addWidget(self.cmder)
        cmder_color.addWidget(self.color_widget)
        cmder_color_button = QSplitter(Qt.Vertical)
        cmder_color_button.addWidget(cmder_color)
        cmder_color_button.addWidget(self.button_widget)
        self.main_tab.addTab(cmder_color_button, 'Cmder')

        self.windower = WindowerWidget()
        self.windower.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.windower, 'Windower')

        self.repoallwidget = RepoAllWindow()
        self.repoallwidget.setStyleSheet('background-color: tan;')
        self.main_tab.addTab(self.repoallwidget, 'Github Repo')


        self.main_layout.addWidget(self.main_tab)
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # w = TabWidget()
    # w.addTab(QWidget(), "tab1 bisa nama panjang kah")
    # w.addTab(QWidget(), "tab2")
    # w.addTab(QWidget(), "tab3 coba panjang juga")
    # dari C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\fm.py
    w = QuickLangsWidget()
    w.setStyleSheet('background-color: tan;')

    w.show()

    sys.exit(app.exec_())
