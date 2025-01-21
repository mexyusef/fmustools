import os, sys
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

# https://stackoverflow.com/questions/46607298/pyqt-qtabwidget-horizontal-tab-and-horizontal-text-in-qtdesigner
# https://stackoverflow.com/questions/51230544/pyqt5-how-to-set-tabwidget-west-but-keep-the-text-horizontal

from schnell.app.dirutils import normy, explore, joiner, files_filter
# from schnell.gui.system.searcher.widgets.common import mkhelp_initial_path
# from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget


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


class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, letak=4, *args, **kwargs):
        """
                1
            4       2
                3
        """
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        
        if letak in [1, 'north', 'North', 'N', 'utara']:
            self.setTabPosition(QtWidgets.QTabWidget.North)
        elif letak in [2, 'east', 'East', 'E', 'timur']:
            self.setTabBar(TabBar(self))
            self.setTabPosition(QtWidgets.QTabWidget.East)
        elif letak in [3, 'south', 'South', 'S', 'selatan']:
            self.setTabPosition(QtWidgets.QTabWidget.South)
        elif letak in [4, 'west', 'West', 'W', 'barat']:
            self.setTabBar(TabBar(self))
            self.setTabPosition(QtWidgets.QTabWidget.West)


class SampleWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_tab = TabWidget(self)

        self.main_layout.addWidget(self.main_tab)
        self.setLayout(self.main_layout)
