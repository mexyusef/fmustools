# https://gist.githubusercontent.com/Axel-Erfurt/cd2406301dd22b5383e12e89ef1385a4/raw/d6f652d52000a5436797f4be2f2ccd60d8049c46/PyQt5BlackWindow.py
# https://gist.github.com/Axel-Erfurt/cd2406301dd22b5383e12e89ef1385a4
import sys

from PyQt5.QtCore import (
    QPoint, 
    QRect,
    Qt,
)
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QDesktopWidget,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QPlainTextEdit,
    QPushButton,
    QSystemTrayIcon,
    QStyle,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


if __name__ == '__main__' or __name__ == 'winless1': # jk sama dg nama file = standalone
    from wembed import WindowEmbedder
else:
    from .wembed import WindowEmbedder

btn_size = 14
margin_kanan = 5
lebar_widget = 225
x_awal_pengurang = lebar_widget + margin_kanan
# https://www.w3schools.com/css/css3_borders.asp
search_stylesheet = """
border-radius: 5px;
padding: 5px 0 0 5px;
background: #2e3436; 
color: #eeeeec; 
border: 1px solid #555753
"""

def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, delta = 60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    lebar, tinggi = int(screenw*ratio),int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)

class WindowTitle(QLabel):
    def __init__(self, lebar, parent):
        super(WindowTitle, self).__init__(parent)
        self.title = QLabel("Dark Window", parent)
        self.title.setGeometry(0, 0, lebar, 24)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("background-color: #2e3436; color: #eeeeec; font-weight: bold;")

class CloseButton(QPushButton):
    def __init__(self, handler, parent):
        super(CloseButton, self).__init__(parent)
        # self.btn_close = QPushButton("x", self)
        self.setText('x')
        self.setGeometry(5, 5, btn_size, btn_size)
        self.clicked.connect(handler)
        self.setFixedSize(btn_size, btn_size)
        self.setStyleSheet("background: #cc0000; padding-bottom: 2px;")

class MinimizeButton(QPushButton):
    def __init__(self, handler, parent):
        super(MinimizeButton, self).__init__(parent)
        # self.btn_close = QPushButton("x", self)
        self.setText('-')
        # self.setGeometry(5, 5, btn_size, btn_size)
        self.setGeometry(22, 5, btn_size, btn_size)
        self.clicked.connect(handler)
        # self.setFixedSize(btn_size, btn_size)
        # self.setStyleSheet("background: #cc0000; padding-bottom: 2px;")
        self.setStyleSheet("background: #edd400; padding-bottom: 2px;")

class RestoreButton(QPushButton):
    def __init__(self, handler, parent):
        super(RestoreButton, self).__init__(parent)
        # self.btn_close = QPushButton("x", self)
        self.setText('+')
        self.setGeometry(39, 5, btn_size, btn_size)
        self.clicked.connect(handler)
        self.setFixedSize(btn_size, btn_size)
        self.setStyleSheet("background: #73d216; padding-bottom: 2px;")

class FindButton(QLineEdit):
    def __init__(self, parent):
        super(FindButton, self).__init__(parent)
        self.setPlaceholderText("find ...")

        self.setGeometry(self.width() - x_awal_pengurang, 5, lebar_widget, 22)
        # self.findfield.setStyleSheet("background: #2e3436; color: #eeeeec; border: 1px solid #555753")
        self.setStyleSheet(search_stylesheet)

class MainContent(QWidget):
    def __init__(self, geometry, parent):
        super(MainContent, self).__init__(parent)
        self.setGeometry(geometry)
        self.setStyleSheet("background: #2e3436; color: #eeeeec; border: 1px solid #555753")
        self.tab = QTabWidget()

        # self.widget_cmd = QWidget()
        # self.widget_wsl = QWidget()
        # self.widget_listener = QWidget()

        self.widget_cmd = WindowEmbedder(perintah=['pwd', 'sido', 'gs'])
        self.widget_wsl = WindowEmbedder(perintah=['wsl', 'pwd', 'sido', 'gs'])
        self.widget_listener = WindowEmbedder(perintah=['wsl', 'pwd', 'sido', 'W'])

        self.tab.addTab(self.widget_cmd, '1')
        self.tab.addTab(self.widget_wsl, '2')
        self.tab.addTab(self.widget_listener, '3')

        layout = QVBoxLayout(self)
        layout.addWidget(self.tab)

class MainWindow(QMainWindow):

    def setTrayMenu(self):
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(QApplication.instance().quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)

    def trayMessage(self, judul, isi, lama=3000):
        self.tray_icon.showMessage(judul, isi, QSystemTrayIcon.Information, lama)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("QMainWindow {background: #2e3436;}")
        #self.setMinimumSize(600,300)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        
        self.title = WindowTitle(lebar=self.width(), parent=self)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.setTrayMenu()


        self.btn_close = CloseButton(handler=self.btn_close_clicked, parent=self)

        # self.btn_min = QPushButton("-", self)
        # self.btn_min.setGeometry(22, 5, btn_size, btn_size)
        # self.btn_min.clicked.connect(self.btn_min_clicked)
        # self.btn_min.setStyleSheet("background: #edd400;; padding-bottom: 2px;")
        self.btn_min = MinimizeButton(handler=self.btn_min_clicked, parent=self)
        
        # self.btn_max = QPushButton("+", self)
        # self.btn_max.setGeometry(39, 5, btn_size, btn_size)
        # self.btn_max.clicked.connect(self.btn_max_clicked)
        # self.btn_max.setFixedSize(btn_size, btn_size)
        # self.btn_max.setStyleSheet("background: #73d216;; padding-bottom: 2px;")
        self.btn_max = RestoreButton(handler=self.btn_max_clicked, parent=self)
        
        # self.findfield = QLineEdit(self)
        # self.findfield.setPlaceholderText("find ...")
        # self.lebar_widget = 225
        # margin_kanan = 5
        # self.x_awal_pengurang = self.lebar_widget + margin_kanan
        # self.findfield.setGeometry(self.width() - self.x_awal_pengurang, 5, self.lebar_widget, 22)
        # # self.findfield.setStyleSheet("background: #2e3436; color: #eeeeec; border: 1px solid #555753")
        # self.findfield.setStyleSheet(search_stylesheet)
        self.findfield = FindButton(self)

        self.start = QPoint(0, 0)
        self.pressing = False
        
        # self.main_content = QPlainTextEdit(self)
        # self.main_content.setGeometry(5, 20, self.width() - 10, self.height() - 32)
        # self.main_content.setStyleSheet("background: #2e3436; color: #eeeeec; border: 1px solid #555753")
        maingeo = QRect(5, 20, self.width() - 10, self.height() - 32)
        self.main_content = MainContent(maingeo, self)
        
        self.tray_icon.show()
        self.trayMessage('App is running', 'App is running here in the tray')

    def closeEvent(self, event):
        # if self.check_box.isChecked():
        event.ignore()
        self.hide()
        self.trayMessage('App is running', 'App is running here in the tray')

    def btn_close_clicked(self):
        self.close()
        
    def btn_min_clicked(self):
        self.showMinimized()
        
    def btn_max_clicked(self):
        if self.windowState() == Qt.WindowMaximized:
            self.showNormal()
        else:
            self.showMaximized()

    def resizeEvent(self, QResizeEvent):
        super(MainWindow, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.width())
        self.main_content.setGeometry(5, 28, self.width() - 10, self.height() - 32)
        self.findfield.setGeometry(self.width() - x_awal_pengurang, 5, lebar_widget, 22)

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                            self.mapToGlobal(self.movement).y(),
                            self.width(),
                            self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(win, screenw, screenh, ratio=1/2)
    # win.show()
    win.hide()
    sys.exit(app.exec_())
