import os, sys, functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# # schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([sidoarjodir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
sys.path.append(sidoarjodir)
if __name__ == '__main__':
    from startup import initialize_programming_data, programming_data
    initialize_programming_data()
from startup import programming_data
from schnell.app.datetimeutils import doy
from schnell.app.dirutils import joiner, joinhere, isfile
from schnell.app.fileutils import file_content, file_write, file_lines
from schnell.app.utils import env_get
from schnell.app.writers.file_handler import number_to_zau, date_to_zau
from schnell.db.writer_service import edit_zau_digit_word, get_words_from_number
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget


env_ok = False
if 'j' in programming_data:
    if 'env' in programming_data['j']:
        if 'ULIBPY_ACTORFILE' in programming_data['j']['env']:
            ACTOR_FILE = programming_data['j']['env']['ULIBPY_ACTORFILE']
            env_ok = True
if not env_ok:
    from startup import initialize_programming_data
    initialize_programming_data()
    ACTOR_FILE = programming_data['j']['env']['ULIBPY_ACTORFILE']


actor_lines = [] if not isfile(ACTOR_FILE) else file_lines(ACTOR_FILE)


class ActorWindow(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()


    def button_with_data(self, label, number, value='', key='custom_data'):

        button_menu = QMenu(self)
        button_menu.addAction(
            # QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
            # folder,
            f"Edit {number}",
            functools.partial(edit_zau_digit_word, number)
        )
        button_menu.addAction(
            # QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
            # folder,
            f"Words of {number}",
            functools.partial(get_words_from_number, number)
        )

        b = QPushButton(label)
        b.setProperty('number', number)
        b.setProperty(key, value)

        b.setMenu(button_menu)

        return b

    def setData(self):

        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 150)
        self.table.setRowHeight(0, 300)

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Col 0", "Col 1"])
        self.table.setVerticalHeaderLabels(["Row 0", "Row 1", "Row 2", "Row 3", "Row 4"])

        records = [item for item in file_lines(ACTOR_FILE) if item.strip()]
        self.table.setRowCount(len(records))

        today = int(doy())
        for idx, line in enumerate(records):
            self.table.setItem(idx, 0, QTableWidgetItem(line))
            self.table.setItem(idx, 1, QTableWidgetItem('*'))
            zau = number_to_zau(idx, asstring=True)
            b = self.button_with_data(f'{zau} {idx}', idx)
            if today == idx:
                b.setStyleSheet('background-color: gold')
            self.table.setCellWidget(idx, 1, b)

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.table = QTableWidget(self)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setData()

        self.main_layout.addWidget(self.table)
        self.setLayout(self.main_layout)


class ActorWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()

        # self.tab = QTabWidget(self, tabPosition=QTabWidget.West)
        self.tab = TabWidget(letak='north', parent=self)
        self.tab.setAutoFillBackground(True)

        tab = MKHelpWidget(parent=self, rootpath=joiner(sidoarjodir, 'database/geura/memorizer'))
        self.tab.addTab(tab, 'Memo')

        box_tddlang = QGroupBox("The Actor")
        layout_boxtddlang = QVBoxLayout()
        lbl0 = ActorWindow()
        layout_boxtddlang.addWidget(lbl0)
        # layout_boxtddlang.addStretch(1)
        box_tddlang.setLayout(layout_boxtddlang)
        self.tab.addTab(box_tddlang, 'The Actor')
        # self.main_layout.addWidget(box_tddlang)

        box_replang = QGroupBox("REPL lang")
        layout_replang = QVBoxLayout()
        lbl0 = QLabel("replang spt ff, f@c, f@e, f@m, fv, fy, dst.")
        layout_replang.addWidget(lbl0)
        # layout_replang.addStretch(1)
        box_replang.setLayout(layout_replang)
        self.tab.addTab(box_replang, 'Replang')

        self.main_layout.addWidget(self.tab)
        self.setLayout(self.main_layout)


def main():
    app = QApplication([])
    # app.setStyleSheet(background_image_stylesheet)
    wnd = ActorWidget()
    wnd.show()
    wnd.resize(1200, 800)
    wnd.setWindowTitle(ACTOR_FILE)
    QShortcut(QKeySequence("Ctrl+Q"), wnd, activated=lambda: qApp.quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
