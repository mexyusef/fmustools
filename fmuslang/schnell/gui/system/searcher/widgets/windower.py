import sys, win32api, win32con, win32gui, time
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtWidgets import*


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, wratio=0, delta = 60):
    """
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    if not wratio:
        wratio = ratio
    # print('wratio:', wratio)
    lebar, tinggi = int(screenw*wratio),int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)

def window_rect(hwnd):
    """
    https://stackoverflow.com/questions/7142342/get-window-position-size-with-python
    """
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return x, y, w, h

def move_window(hwnd, x, y, w, h):
    win32gui.MoveWindow(hwnd, x, y, w, h, True)

def resize_window(hwnd, value):
    x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
    w = x1 - x0
    h = y1 - y0
    win32gui.MoveWindow(hwnd, x0-(value/2), y0-(value/2), w+value, h+value, True)

def x_resize_window_keep_center(hwnd, percentage_value, screenw):
    x,y,w,h = window_rect(hwnd)
    new_width = int(percentage_value * screenw / 100)
    half = int((new_width-w)/2)
    new_x = x-half
    print(f"""[x_resize_window_keep_center]
    x awal {x}
    half {half}
    x baru {new_x}
    y {y}
    w lama {w}
    w baru {new_width}
    h {h}
    """)
    win32gui.MoveWindow(hwnd, new_x, y, new_width, h, True)

def y_resize_window_keep_center(hwnd, percentage_value, screenh):
    x,y,w,h = window_rect(hwnd)
    new_height = int(percentage_value * screenh / 100)
    half = int((new_height-h)/2)
    new_y = y-half
    print(f"""[y_resize_window_keep_center]
    x awal {x}
    half {half}
    x baru {new_y}
    y {y}
    w lama {w}
    w baru {new_height}
    h {h}
    """)
    win32gui.MoveWindow(hwnd, x, new_y, w, new_height, True)

def slide_x(hwnd, increment=10):
    x,y,w,h = window_rect(hwnd)
    # new pos, x+=10
    x += increment
    move_window(hwnd, x,y,w,h)

def slide_y(hwnd, increment=5):
    x,y,w,h = window_rect(hwnd)
    # new pos, x+=10
    y += increment
    move_window(hwnd, x,y,w,h)

def calc_x_percentage(hwnd, screenw):
    x,y,w,h = window_rect(hwnd)
    return w/screenw

def calc_y_percentage(hwnd, screenh):
    x,y,w,h = window_rect(hwnd)
    return h/screenh

def calc_xy_percentage(hwnd, screenw, screenh):
    return calc_x_percentage(hwnd, screenw), calc_y_percentage(hwnd, screenh)

def get_child_windows(hwnd):
    child_windows = []
    try:
        win32gui.EnumChildWindows(hwnd, lambda hwnd, container: container.append(hwnd), child_windows)
    except Exception as e:
        # print str(e)
        return []
    return child_windows

def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)

def get_child_windows_with_names(hwnd):
    """
    child_windows = []
    win32gui.EnumChildWindows(hwnd, lambda hwnd, container: container.append('%d - %s' % (hwnd, get_window_title(hwnd))), child_windows)
    return child_windows
    """
    return ['%d - %s' % (window, get_window_title(window)) for window in get_child_windows(hwnd)]

def is_always_on_top(hwnd):
    return win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST

def set_topmost(hwnd, not_topmost=True):
    '''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
    https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
    root = Tk()
    root.wm_attributes("-topmost", 1)

    https://github.com/flashwave/topmostfriend
    https://github.com/Bluegrams/PinWin
    https://github.com/progrium/topframe

    '''
    try:
        if not_topmost:
            win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        else:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    except win32gui.error:
        print ("Error while moving window to top")

def calculate_typing_speed(isi_tulisan, cpm):
    harus_selesai_dlm_berapa_detik = float ( len(isi_tulisan) * 60 / float(cpm) )
    interval_ngetik = float ( 1 / (len(isi_tulisan) / harus_selesai_dlm_berapa_detik) )
    return interval_ngetik

def restore_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

def post_enter(hwnd):
    '''
    kita gunakan post-enter di keyboard module utk ngetik type-interval-chars
    '''
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def post_chars(hwnd, chars, interval=0):
  for c in chars:
    if c == "\n":
      # time.sleep(1.5) # utk enter perlu/penting stop dulu
      # post_char(hwnd, 'a')
      # print('NL')
      post_enter(hwnd)
      # post_char(hwnd, 'b')
    else:
      # print('>',c)
      post_char(hwnd, c)

    if interval > 0:
      time.sleep(interval)

def post_char(hwnd, char):
    win32gui.PostMessage(hwnd, win32con.WM_CHAR, ord(char), 0)

def post_cmd_cpm(hwnd, chars, cpm=4000):
    '''
    '''
    interval = calculate_typing_speed(chars, cpm)
    print('typing interval:', interval)
    post_chars(hwnd, chars, interval)
    # time.sleep(0.5) # entah kenapa hrs gini
    # input('PRE')
    post_enter(hwnd)
    # time.sleep(interval if interval else SLEEP_CREATION_TIME)
    # time.sleep(1.0)
    # input('POST')


class MyHwnd(QWidget):


    def create_child_nodes(self, start_tree_item, parent_hwnd):
        for chwnd in get_child_windows_with_names(parent_hwnd):
        # for chwnd in get_child_windows(self.data['hwnd']):
            item = QTreeWidgetItem(start_tree_item)
            text = str(chwnd)
            item.setText(0, text)
            grandchildren = get_child_windows_with_names(chwnd)
            if grandchildren:
                self.create_child_nodes(item, chwnd)
                # for cchwnd in grandchildren:
                #     cicit = QTreeWidgetItem(item)
                #     text = str(cchwnd)
                #     cicit.setText(0, text)

    def __init__(self, data, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        # self.setMinimumHeight(200)
        self.data = data
        self.current_hwnd = self.data['hwnd']

        # group = QGroupBox(self.data['title'])
        grouplayout = QHBoxLayout()

        treekiri = QTreeWidget(self)
        treekiri.headerItem().setText(0, self.data['title'])
        first_item = QTreeWidgetItem(treekiri)
        first_item.setText(0, str(self.data['hwnd']))

        # item2 = QTreeWidgetItem(item1)
        # item2.setText(0, 'item2')
        # item3 = QTreeWidgetItem(item1)
        # item3.setText(0, 'item3')
        # item4 = QTreeWidgetItem(item1)
        # item2.setText(0, 'item4')
        self.create_child_nodes(first_item, self.data['hwnd'])
        # for chwnd in get_child_windows_with_names(self.data['hwnd']):
        # # for chwnd in get_child_windows(self.data['hwnd']):
        #     item = QTreeWidgetItem(item1)
        #     text = str(chwnd)
        #     item.setText(0, text)
        #     grandchildren = get_child_windows_with_names(chwnd)
        #     if grandchildren:
        #         for cchwnd in grandchildren:
        #             cicit = QTreeWidgetItem(item)
        #             text = str(cchwnd)
        #             cicit.setText(0, text)

        kananlayout = QVBoxLayout()
        # judul = f"[{str(self.data['hwnd'])}] {data['title']}"
        kananlayout.addWidget(QLabel(data['title']))
        judul = str(self.current_hwnd)
        self.hwnd_label = QLabel(judul)
        kananlayout.addWidget(self.hwnd_label)
        # phwnd = QLabel(self.data['phwnd'])
        # kananlayout.addWidget(phwnd)
        # classname = QLabel(self.data['class'])
        # kananlayout.addWidget(classname)
        self.pesanbox = QPlainTextEdit()
        kirim = QPushButton('Send')
        kananlayout.addWidget(self.pesanbox)
        kananlayout.addWidget(kirim)
        kirim.clicked.connect(self.kirim_pesan)

        grouplayout.addWidget(treekiri)
        grouplayout.addLayout(kananlayout)

        # QtCore.QMetaObject.connectSlotsByName(self)
        # treekiri.itemChanged.connect(self.handleChanged)

        # group.setLayout(grouplayout)
        self.setLayout(grouplayout)

        treekiri.itemClicked.connect(self.onItemClicked)
        treekiri.expandAll()

    def kirim_pesan(self):
        pesan = self.pesanbox.toPlainText()
        print(f'harus kirim pesan [{pesan}] ke hwnd [{self.current_hwnd}]')
        post_cmd_cpm(self.current_hwnd, pesan)

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def onItemClicked(self, item, col):
        # tree clicked: <PyQt5.QtWidgets.QTreeWidgetItem object at 0x0000024CFB128C10> 0 1639446 -
        # item kolom 0, bertext "1639446 -"
        # print('tree clicked:', item, col, item.text(col))
        hwndstr = item.text(col) .split()[0]
        if hwndstr.isdigit():
            self.current_hwnd = int(hwndstr)
            self.hwnd_label.setText(hwndstr)

    def handleChanged(self, item, column):
        print(f"""[treekiri.itemChanged]
        item = {item}
        column = {column}
        """)
        # count = item.childCount()
        # if item.checkState(column) == Qt.Checked:
        #     for index in range(count):
        #         item.child(index).setCheckState(0, Qt.Checked)
        # if item.checkState(column) == Qt.Unchecked:
        #     for index in range(count):
        #         item.child(index).setCheckState(0, Qt.Unchecked)


def is_minimized(hwnd):
    """
    https://stackoverflow.com/questions/60471477/using-python-how-can-i-detect-whether-a-program-is-minimized-or-maximized
    """
    minimized = False
    tup = win32gui.GetWindowPlacement(hwnd)
    if tup[1] == win32con.SW_SHOWMAXIMIZED:
        minimized = False
    elif tup[1] == win32con.SW_SHOWMINIMIZED:
        minimized = True
    elif tup[1] == win32con.SW_SHOWNORMAL:
        normal = True
    print(f'is {hwnd} minimized?', minimized)
    return minimized


class MyListItem(QWidget):

    def bring_to_top(self, data):
        hwnd = data['hwnd']
        # first restore (mending cek dulu jk minimized)
        try:
            if is_minimized(hwnd):
                print(f'restoring miinimized {hwnd}')
                restore_window(hwnd)
            win32gui.BringWindowToTop(hwnd)
        except Exception as err:
            print(f"""[{err}]
            tidak berhasil bring to top {data}
            """)
            return
        if self.topmost.isChecked():
            set_topmost(hwnd)
            print(f'{hwnd} now topmost')
        else:
            if is_always_on_top(hwnd):
                print(f'not top mosting {hwnd}.')
                set_topmost(hwnd, not_topmost=True)

    def geser_x(self, data, value):
        hwnd = data['hwnd']
        print(f'pindah x sebanyak: {value} berjenis {type(value)}')
        slide_x(hwnd, value)

    def geser_y(self, data, value):
        hwnd = data['hwnd']
        print(f'pindah y sebanyak: {value} berjenis {type(value)}')
        slide_y(hwnd, value)

    def change_width(self, data, screenw, value):
        hwnd = data['hwnd']
        # print(f'pindah sebanyak {value}')
        x_resize_window_keep_center(hwnd, value, screenw)

    def change_height(self, data, screenh, value):
        hwnd = data['hwnd']
        # print(f'pindah sebanyak {value}')
        y_resize_window_keep_center(hwnd, value, screenh)

    def toggle_topmost(self, state):
        if state == Qt.Checked:
            print('topmost')
        else:
            print('not topmost')

    def __init__(self, data_item, listwidgetitem, *args, **kwargs):
        """
        terima: text, listwidgetitem (li), listwidget (ul/ol) = parent
        """
        super(MyListItem, self).__init__(*args, **kwargs)

        screen_geometry = QDesktopWidget().screenGeometry(-1)
        screenw, screenh = screen_geometry.width(), screen_geometry.height()

        self.data = data_item
        text = f"""[{self.data['hwnd']}] [{self.data['phwnd']}] [{self.data['class']}] {self.data['title']}"""

        self._item = listwidgetitem

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        # layout.addWidget(QLineEdit(text, self))
        # layout.addWidget(QPushButton('x', self, clicked=self.doDeleteItem))

        # self.cb = QCheckBox('', self)
        # self.cb.stateChanged.connect(self.checkedItem)
        # layout.addWidget(self.cb)

        # line edit read only?
        # self.le = QLineEdit(text, self)
        # layout.addWidget(self.le)

        self.info = MyHwnd(self.data, self)
        layout.addWidget(self.info)

        topicon = QApplication.style().standardIcon(QStyle.SP_TitleBarNormalButton)
        top = QPushButton('top', icon=topicon, parent=self)
        top.clicked.connect(lambda x:self.bring_to_top(self.data))
        layout.addWidget(top)

        self.topmost = QCheckBox('Topmost')
        self.topmost.stateChanged.connect(self.toggle_topmost)
        layout.addWidget(self.topmost)
        # geser x
        # group = QButtonGroup(self)
        # https://www.pythonguis.com/faq/built-in-qicons-pyqt/icons-builtin.png
        back = QApplication.style().standardIcon(QStyle.SP_ArrowBack)
        front = QApplication.style().standardIcon(QStyle.SP_ArrowForward)
        geserx = QPushButton('left', icon=back, parent=self)
        geserx2 = QPushButton('right', icon=front, parent=self)
        geserx.clicked.connect(lambda x:self.geser_x(self.data, -10))
        geserx2.clicked.connect(lambda x:self.geser_x(self.data, 10))
        # sldx = QSlider(Qt.Horizontal, self)
        # sldx.setRange(-screenw//4, screenw//4)
        # sldx.setMaximumWidth(100)
        # sldx.setValue(0)
        # # sldx.setFocusPolicy(Qt.NoFocus)
        # # sldx.setPageStep(5)
        # sldx.valueChanged.connect(lambda value:self.geser_x(self.data, value))
        layout.addWidget(geserx)
        layout.addWidget(geserx2)

        # geser y
        # group2 = QButtonGroup(self)
        down = QApplication.style().standardIcon(QStyle.SP_ArrowDown)
        up = QApplication.style().standardIcon(QStyle.SP_ArrowUp)
        # gesery = QPushButton('geser-y', self)
        gesery = QPushButton('up', icon=up, parent=self)
        gesery2 = QPushButton('down', icon=down, parent=self)
        gesery.clicked.connect(lambda x:self.geser_y(self.data, -5))
        gesery2.clicked.connect(lambda x:self.geser_y(self.data, 5))
        # sldy = QSlider(Qt.Horizontal, self)
        # sldy.setRange(-screenw//4, screenw//4)
        # sldy.setMaximumWidth(100)
        # sldy.setValue(0)
        # # sldx.setFocusPolicy(Qt.NoFocus)
        # # sldx.setPageStep(5)
        # # sldx.valueChanged.connect(self.updateLabel)
        layout.addWidget(gesery)
        layout.addWidget(gesery2)
        # layout.addWidget(sldy)
        # resize x
        # group3 = QButtonGroup(self)
        # szx = QPushButton('resize-x', self)
        percent_x, percent_y = calc_xy_percentage(self.data['hwnd'], screenw, screenh)
        xsizeicon = QApplication.style().standardIcon(QStyle.SP_ToolBarHorizontalExtensionButton)
        szx = QLabel()
        szx.setPixmap(xsizeicon.pixmap(QSize(16,16)))
        sldszx = QSlider(Qt.Horizontal, self)        
        # sldszx.setRange(-screenw//4, screenw//4)
        sldszx.setRange(10,100) # mininum 1/10 of screen width
        sldszx.setMaximumWidth(100)
        sldszx.setValue(int(percent_x * 100))
        # sldx.setFocusPolicy(Qt.NoFocus)
        # sldx.setPageStep(5)
        sldszx.valueChanged.connect(lambda value:self.change_width(self.data, screenw, value))
        layout.addWidget(szx)
        layout.addWidget(sldszx)
        # resize y
        # group4 = QButtonGroup(self)
        # szy = QPushButton('resize-y', self)
        ysizeicon = QApplication.style().standardIcon(QStyle.SP_ToolBarVerticalExtensionButton)
        szy = QLabel()
        szy.setPixmap(ysizeicon.pixmap(QSize(16,16)))
        sldszy = QSlider(Qt.Horizontal, self)
        # sldszy.setRange(-screenw//4, screenw//4)
        sldszy.setRange(10,100)
        sldszy.setMaximumWidth(100)
        # sldszy.setValue(0)
        sldszy.setValue(int(percent_y * 100))
        sldszy.valueChanged.connect(lambda value:self.change_height(self.data, screenh, value))
        # sldx.setFocusPolicy(Qt.NoFocus)
        # sldx.setPageStep(5)
        # sldx.valueChanged.connect(self.updateLabel)
        layout.addWidget(szy)
        layout.addWidget(sldszy)

    def checkedItem(self, state):
        # state Qt.Checked
        pass


app_stylesheet = """
* {
    font-family: Consolas;
    font-size: 15px;
}

WindowerWidget {
    background-position: center;
    background-color: #aaff7f;
}
"""


class WindowEmbedder(QWidget):

    def __init__(self, *args, **kwargs):
        super(WindowEmbedder, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self)

        self.myhwnd = int(self.winId())  # 自己的句柄

        self.list_windows = QPushButton('List windows', self, clicked=self._getWindowList, maximumHeight=30)
        self.release_window = QPushButton('Release', clicked=self.releaseWidget, maximumHeight=30)
        # layout.addWidget(QLabel('Double-click an item in the list to embed the target window to the bottom\n format is: handle|parent handle|title|class name', self, maximumHeight=30))
        self.windowList = QListWidget(self, itemDoubleClicked=self.onItemDoubleClicked, maximumHeight=200)
        toolbar_layout = QHBoxLayout()
        toolbar_layout.addWidget(self.list_windows)
        toolbar_layout.addWidget(self.release_window)
        toolbar_layout.addWidget(self.windowList)
        # layout.addWidget(self.list_windows)
        # layout.addWidget(self.release_window)
        # layout.addWidget(self.windowList)
        layout.addLayout(toolbar_layout)

    def releaseWidget(self):
        """release window"""
        if self.layout().count() == 5:
            self.restore()
            self._getWindowList()

    def closeEvent(self, event):
        """window close"""
        self.releaseWidget()
        super(WindowEmbedder, self).closeEvent(event)

    def _getWindowList(self):
        """Clear the original list"""
        self.windowList.clear()
        win32gui.EnumWindows(self._enumWindows, None)

    def onItemDoubleClicked(self, item):
        """list double click event"""
        # Remove the item first
        self.windowList.takeItem(self.windowList.indexFromItem(item).row())
        hwnd, phwnd, _, _ = item.text().split('|')
        # start embedding
        self.releaseWidget()
        hwnd, phwnd = int(hwnd), int(phwnd)
        # Attributes before embedding
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        wrect = win32gui.GetWindowRect(hwnd)[:2] + win32gui.GetClientRect(hwnd)[2:]
        print('save', hwnd, style, exstyle, wrect)

        widget = QWidget.createWindowContainer(QWindow.fromWinId(hwnd))
        widget.hwnd = hwnd  # 窗口句柄
        widget.phwnd = phwnd  # 父窗口句柄
        widget.style = style  # 窗口样式
        widget.exstyle = exstyle  # 窗口额外样式
        widget.wrect = wrect  # 窗口位置
        self.layout().addWidget(widget)

        widget.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        win32gui.SetParent(hwnd, int(self.winId()))

    def restore(self):
        """return window"""
        # 有bug，归还后窗口没有了WS_VISIBLE样式，不可见
        widget = self.layout().itemAt(4).widget()
        hwnd, phwnd, style, exstyle, wrect = widget.hwnd, widget.phwnd, widget.style, widget.exstyle, widget.wrect
        print('restore', hwnd, phwnd, style, exstyle, wrect)
        widget.close()
        self.layout().removeWidget(widget)  # 从布局中移出
        widget.deleteLater()

        win32gui.SetParent(hwnd, phwnd)  # 让它返回它的父窗口
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style | win32con.WS_VISIBLE)  # 恢复样式
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, exstyle)  # 恢复样式
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)  # 显示窗口
        win32gui.SetWindowPos(hwnd, 0, wrect[0], wrect[1], wrect[2], wrect[3], win32con.SWP_NOACTIVATE)

    def _enumWindows(self, hwnd, _):
        """traversal callback function"""
        if hwnd == self.myhwnd:
            return  # 防止自己嵌入自己
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            phwnd = win32gui.GetParent(hwnd)
            title = win32gui.GetWindowText(hwnd)
            name = win32gui.GetClassName(hwnd)
            self.windowList.addItem('{0}|{1}|\ttitle:{2}\t|\tclass name:{3}'.format(hwnd, phwnd, title, name))


class WindowerWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(WindowerWidget, self).__init__(*args, **kwargs)
        self.init()
        self.setWindowTitle('Single atau double click untuk bring window to front')
        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        self.setStyleSheet(app_stylesheet)

    def _getWindowList(self):
        self.windowList.clear()
        win32gui.EnumWindows(self._enumWindows, None)

    def onItemDoubleClicked(self, item):
        pecah = item.text().split(maxsplit=4)
        pecah = [i.strip() for i in pecah]
        print(pecah)
        hwnd, _, _, title = pecah[0], pecah[1], pecah[2], ' '.join(pecah[3:]) # [i.strip() for i in pecah]
        # print(f"hwnd {hwnd} berjudul '{title}'")
        win32gui.BringWindowToTop(hwnd)

    def move_window(self, item):
        pecah = item.text().split(maxsplit=4)
        pecah = [i.strip() for i in pecah]
        print(pecah)
        hwnd, _, _, title = pecah[0], pecah[1], pecah[2], ' '.join(pecah[3:]) # [i.strip() for i in pecah]
        slide_x(hwnd, self.increment)

    def _enumWindows(self, hwnd, _):
        if hwnd == self.myhwnd:
            return  # Prevent yourself from embedding yourself
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            phwnd = win32gui.GetParent(hwnd)
            title = win32gui.GetWindowText(hwnd)
            name = win32gui.GetClassName(hwnd)
            if title and name and phwnd==0:
                # self.windowList.addItem('{0}|{1}|\ttitle:{2}\t|\tclass name:{3}'.format(hwnd, phwnd, title, name))
                item = {
                    'hwnd': hwnd,
                    'phwnd': phwnd,
                    'title': title,
                    'class': name,
                }
                self.window_list.append(item)

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def init(self):
        self.myhwnd = int(self.winId())
        self.window_list = []
        self.increment = 10  # geser ke kanan

        self.context_menu = QMenu(self)

        layout = QVBoxLayout(self)
        self.embedder = WindowEmbedder()
        self.embedder.setStyleSheet('background-color: red;')
        # self.windowList = QListWidget(self, itemDoubleClicked=self.move_window, itemClicked=self.onItemDoubleClicked)
        self.windowList = QListWidget(self)
        # layout.addWidget(self.windowList)
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.windowList)
        self.stack.addWidget(self.embedder)
        layout.addWidget(self.stack)
        self.context_menu.addAction('window list', lambda: self.stack.setCurrentIndex(0))
        self.context_menu.addAction('window embedder', lambda: self.stack.setCurrentIndex(1))

        self._getWindowList()
        # sort list
        self.window_list.sort(key=lambda item: item['hwnd'])
        for entry in self.window_list:
            listwidgetitem = QListWidgetItem(self.windowList)

            w,h = self.sizeHint().width(), 200
            listwidgetitem.setSizeHint(QSize(w,h))

            # item = f"{entry['hwnd']:<20}{entry['phwnd']:<20}{entry['class']:<50}{entry['title']}"
            list_item = MyListItem(entry, listwidgetitem, self.windowList)
            # self.windowList.addItem(list_item)
            self.windowList.setItemWidget(listwidgetitem, list_item)


def main():
    app = QApplication(sys.argv)
    # app.setStyleSheet(app_stylesheet)
    w = WindowerWidget()
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=0.8, wratio=1.0)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

"""
TODO:
itemwidget

table                       to top      geser-x         geser-y         resize-xy           resize-x       resize-y
title, hwnd, pwnd, class                neg-pos         neg-pos         neg-pos             neg-pos         neg-pos
"""
