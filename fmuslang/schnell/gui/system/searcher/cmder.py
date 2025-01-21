import os, sys, time
from pprint import pprint
from uuid import uuid4 as u4

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([schnelldir, '..'])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(sidoarjodir)

from schnell.app.appconfig import command_prompt_data
from schnell.app.windowsutils import (
    cmd_register_list as l,
    create_register_commandprompt as c,
    ketik as k,
    ketik_by_index as ki,
    fill_in_hwnds as fill,
    hapus_by_id as hadi,
    get_command_prompt_data_index_from_uuidtitle,

    get_hwnd_from_uuidtitle,
    minimize_window, maximize_window,
    show_window, hide_window,
    restore_window, normal_window,
    close_window,
    bring_to_top, set_top, set_topmost, set_not_topmost,

    hapus_empty, hapus_by_id,
    hapus_iterate_by_title,
)
# c()
# l()
# fill()
# l()
# ki(1, 'hello')

class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


class FlowWidget(QWidget):

    def __init__(self, parent=None, widgets=[], *args, **kwargs):
        
        super(FlowWidget, self).__init__(parent, *args, **kwargs)
        self.main_layout = QVBoxLayout()
        self.flow_widget = QWidget(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        # scrollarea gunakan widget yg akan dilayout dg flowLayout
        self.scrollArea.setWidget(self.flow_widget)
        self.flowLayout = FlowLayout(self.flow_widget)

        for widget in widgets:
            self.flowLayout.addWidget(widget)

        self.main_layout.addWidget(self.scrollArea)
        self.setLayout(self.main_layout)

    def clearLayout(self):
        while self.flowLayout.count():
            child = self.flowLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def add_items(self, widgets):
        for widget in widgets:
            self.flowLayout.addWidget(widget)

    def clear_add_items(self, widgets):
        self.clearLayout()
        self.add_items(widgets)


class Cmder(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        combo0 = QComboBox(self)
        combo0.addItems(['hwnd1', 'hwnd2', 'hwnd3', 'hwnd4', 'hwnd5'])
        combo0.currentTextChanged.connect(lambda value: print(value))
        combo0.currentIndexChanged.connect(lambda index: print(index))
        # combo0.textChanged.connect(lambda value: print(value))
        self.main_layout.addWidget(combo0)

        def set_combo_items():
            items = [v['id'] for v in command_prompt_data.values()]
            combo0.clear()
            combo0.addItems(items)

        flow1 = FlowWidget()
        widgets = []
        btn1_0 = QPushButton('create+fill+set cmd')
        widgets.append(btn1_0)
        def fill_set():
            fill()
            set_combo_items()
        def create_fill_set():
            id = c()
            fill_set()

            l() # print

            # cek id ada
            index_or_none = get_command_prompt_data_index_from_uuidtitle(id)
            if not index_or_none:
                # TODO: loop + sleep utk fill automatic
                print('ERR...please fill secara manual! karena masih kosong...')
            else:
                # cek hwnd sudah ada
                hwnd = get_hwnd_from_uuidtitle(id)
                while not hwnd:
                    fill_set()
                    time.sleep(0.5)
                    hwnd = get_hwnd_from_uuidtitle(id)
            
        btn1_0.clicked.connect(lambda: create_fill_set())

        btn1_2 = QPushButton('fill+set info')
        widgets.append(btn1_2)
        btn1_2.clicked.connect(lambda: fill_set())

        btn1_1 = QPushButton('list cmds')
        widgets.append(btn1_1)
        btn1_1.clicked.connect(lambda: l())

        btn1_3 = QPushButton('set items')
        widgets.append(btn1_3)
        btn1_3.clicked.connect(lambda: set_combo_items())

        btn1_4 = QPushButton('hapus window kosong')
        widgets.append(btn1_4)
        def hapus_set_combo_items():
            hapus_iterate_by_title()
            set_combo_items()
        btn1_4.clicked.connect(lambda: hapus_set_combo_items())

        def to_top(mode='topmost'):
            id_now = combo0.currentText()
            hwnd = get_hwnd_from_uuidtitle(id_now)
            if mode == 'topmost':
                set_topmost(hwnd)
            elif mode == 'nottopmost':
                set_not_topmost(hwnd)
            elif mode == 'top':
                set_top(hwnd)
            elif mode == 'bringtop':
                bring_to_top(hwnd)

        btn_topmost = QPushButton('set topmost')
        widgets.append(btn_topmost)
        btn_topmost.clicked.connect(lambda: to_top('topmost'))
        btn_nottopmost = QPushButton('set NOT topmost')
        widgets.append(btn_nottopmost)
        btn_nottopmost.clicked.connect(lambda: to_top('nottopmost'))
        btn_top = QPushButton('set top')
        widgets.append(btn_top)
        btn_top.clicked.connect(lambda: to_top('top'))
        btn_bringtop = QPushButton('bring to top')
        widgets.append(btn_bringtop)
        btn_bringtop.clicked.connect(lambda: to_top('bringtop'))

        def operate_on_windows(mode='hide'):
            id_now = combo0.currentText()
            hwnd = get_hwnd_from_uuidtitle(id_now)
            if mode == 'hide':
                hide_window(hwnd)
            elif mode == 'show':
                show_window(hwnd)
            elif mode == 'normal':
                normal_window(hwnd)
            elif mode == 'restore':
                restore_window(hwnd)
            elif mode == 'min':
                minimize_window(hwnd)
            elif mode == 'max':
                maximize_window(hwnd)
            elif mode == 'close':
                close_window(hwnd)
        btn_minimize = QPushButton('minimize')
        widgets.append(btn_minimize)
        btn_minimize.clicked.connect(lambda: operate_on_windows('min'))
        btn_maximize = QPushButton('maximize')
        widgets.append(btn_maximize)
        btn_maximize.clicked.connect(lambda: operate_on_windows('max'))
        btn_restore = QPushButton('restore')
        widgets.append(btn_restore)
        btn_restore.clicked.connect(lambda: operate_on_windows('restore'))
        btn_normal = QPushButton('normal')
        widgets.append(btn_normal)
        btn_normal.clicked.connect(lambda: operate_on_windows('normal'))
        btn_hide = QPushButton('hide')
        widgets.append(btn_hide)
        btn_hide.clicked.connect(lambda: operate_on_windows('hide'))
        btn_show = QPushButton('show')
        widgets.append(btn_show)
        btn_show.clicked.connect(lambda: operate_on_windows('show'))
        btn_close = QPushButton('close')
        widgets.append(btn_close)
        btn_close.clicked.connect(lambda: operate_on_windows('close'))

        line_ketik = QLineEdit()
        # line_ketik.setMinimumWidth(200)
        line_ketik.setStyleSheet('height: 60px; width: 350px; font-family: Consolas; font-size: 14px; background-color: oldlace;')
        button_ketik = QPushButton('ketik')
        widgets.append(line_ketik)
        widgets.append(button_ketik)
        def button_ketik_handler(text=None):
            if not text:
                text = line_ketik.text()
            id_now = combo0.currentText()
            index = get_command_prompt_data_index_from_uuidtitle(id_now)
            print(f"send [{text}] to {id_now}, index={index}")
            ki(index, text)
        button_ketik.clicked.connect(lambda: button_ketik_handler())
        line_ketik.returnPressed.connect(lambda: button_ketik_handler())

        
        btn_gitstatus = QPushButton('git status')
        widgets.append(btn_gitstatus)
        btn_gitstatus.clicked.connect(lambda: button_ketik_handler('gs'))

        flow1.add_items(widgets)
        self.main_layout.addWidget(flow1)
        self.setLayout(self.main_layout)

        #self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Cmder')
        # self.setMinimumWidth(600)
        # self.show()
        
# def main():
#     app = QApplication([])
#     ex = Cmder()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
