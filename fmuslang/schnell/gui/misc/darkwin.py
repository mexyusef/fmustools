# https://gist.githubusercontent.com/Axel-Erfurt/cd2406301dd22b5383e12e89ef1385a4/raw/d6f652d52000a5436797f4be2f2ccd60d8049c46/PyQt5BlackWindow.py
# https://gist.github.com/Axel-Erfurt/cd2406301dd22b5383e12e89ef1385a4
import sys

from PyQt5.QtCore import (
    QPoint, 
    Qt,
)
from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
)

btn_size = 14

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

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("QMainWindow {background: #2e3436;}")
        #self.setMinimumSize(600,300)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        
        self.title = QLabel("Dark Window", self)
        self.title.setGeometry(0, 0, self.width(), 24)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("background-color: #2e3436; color: #eeeeec; font-weight: bold;")
        
        self.btn_close = QPushButton("x", self)
        self.btn_close.setGeometry(5, 5, btn_size, btn_size)
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("background: #cc0000; padding-bottom: 2px;")
        
        self.btn_min = QPushButton("-", self)
        self.btn_min.setGeometry(22, 5, btn_size, btn_size)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setStyleSheet("background: #edd400;; padding-bottom: 2px;")
        
        self.btn_max = QPushButton("+", self)
        self.btn_max.setGeometry(39, 5, btn_size, btn_size)
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet("background: #73d216;; padding-bottom: 2px;")
        
        self.findfield = QLineEdit(self)
        self.findfield.setPlaceholderText("find ...")
        
        self.lebar_widget = 225
        margin_kanan = 5
        self.x_awal_pengurang = self.lebar_widget + margin_kanan
        self.findfield.setGeometry(self.width() - self.x_awal_pengurang, 5, self.lebar_widget, 22)
        # self.findfield.setStyleSheet("background: #2e3436; color: #eeeeec; border: 1px solid #555753")
        self.findfield.setStyleSheet(search_stylesheet)

        self.start = QPoint(0, 0)
        self.pressing = False
        
        self.myeditor = QPlainTextEdit(self)
        self.myeditor.setGeometry(5, 20, self.width() - 10, self.height() - 32)
        self.myeditor.setStyleSheet("background: #2e3436; color: #eeeeec; border: 1px solid #555753")
        
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
        self.myeditor.setGeometry(5, 28, self.width() - 10, self.height() - 32)
        self.findfield.setGeometry(self.width() - self.x_awal_pengurang, 5, self.lebar_widget, 22)

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
    win.show()
    sys.exit(app.exec_())
