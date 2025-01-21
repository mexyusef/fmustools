# -*- coding: utf-8 -*-
import sys
import math, random, string




from PyQt5.QtWidgets import QProxyStyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtWidgets import *

from PyQt5.QtCore import Qt
from PyQt5.QtCore import *

from PyQt5.QtGui import QFont, QFontMetrics, QFontInfo, QFontMetricsF, QFontDatabase
from PyQt5.QtGui import *


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.Qsci import QsciScintilla, QsciLexerJSON, QsciLexerPython
# import ctypes
# myappid = 'fulgent.krepl.gui.1.0.0' # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



class CodeScintilla(QsciScintilla):

    def __init__(self, *args, **kwargs):
        super(CodeScintilla, self).__init__(*args, **kwargs)
        self.init()
        self.linesChanged.connect(self.onLinesChanged)

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + 6)

    def init(self):
        self.setUtf8(True)
        lexer = QsciLexerPython(self)
        self.setLexer(lexer)
        self.setAutoCompletionCaseSensitivity(False)  # ignore case
        self.setAutoCompletionSource(self.AcsAll)
        self.setAutoCompletionThreshold(1)  # One character pops up completion
        self.setAutoIndent(True)  # auto indent
        self.setBackspaceUnindents(True)
        self.setBraceMatching(self.StrictBraceMatch)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setTabWidth(4)
        self.setWhitespaceSize(1)
        self.setWhitespaceVisibility(self.WsVisible)
        self.setWhitespaceForegroundColor(Qt.gray)
        self.setWrapIndentMode(self.WrapIndentFixed)
        self.setWrapMode(self.WrapWord)
        # fold
        self.setFolding(self.BoxedTreeFoldStyle, 2)
        self.setFoldMarginColors(QColor("#676A6C"), QColor("#676A6D"))
        font = self.font() or QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(13)
        self.setFont(font)
        self.setMarginsFont(font)
        self.fontmetrics = QFontMetrics(font)
        lexer.setFont(font)
        self.setMarginWidth(0, self.fontmetrics.width(str(self.lines())) + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("gainsboro"))
        self.setMarginWidth(1, 0)
        self.setMarginWidth(2, 14)  # folded area
        # Bind autocompletion hotkey Alt+/
        completeKey = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Slash), self)
        completeKey.setContext(Qt.WidgetShortcut)
        completeKey.activated.connect(self.autoCompleteFromAll)


class TabBarStyle(QProxyStyle):

    def sizeFromContents(self, types, option, size, widget):
        size = super(TabBarStyle, self).sizeFromContents(types, option, size, widget)
        if types == self.CT_TabBarTab:
            size.transpose()
        return size

    def drawControl(self, element, option, painter, widget):
        if element == self.CE_TabBarTabLabel:
            painter.drawText(option.rect, Qt.AlignCenter, option.text)
            return
        super(TabBarStyle, self).drawControl(element, option, painter, widget)


# https://gist.github.com/espdev/4f1565b18497a42d317cdf2531b7ef05
tab_style = """
QTabWidget::pane {
    border: 1px solid black;
    background: white;
}

QTabWidget::tab-bar:top {
    top: 1px;
}

QTabWidget::tab-bar:bottom {
    bottom: 1px;
}

QTabWidget::tab-bar:left {
    right: 1px;
}

QTabWidget::tab-bar:right {
    left: 1px;
}

QTabBar::tab {
    border: 1px solid black;
}

QTabBar::tab:selected {
    background: white;
}

QTabBar::tab:!selected {
    background: silver;
}

QTabBar::tab:!selected:hover {
    background: #999;
}

QTabBar::tab:top:!selected {
    margin-top: 3px;
}

QTabBar::tab:bottom:!selected {
    margin-bottom: 3px;
}

QTabBar::tab:top, QTabBar::tab:bottom {
    min-width: 8ex;
    margin-right: -1px;
    padding: 5px 10px 5px 10px;
}

QTabBar::tab:top:selected {
    border-bottom-color: none;
}

QTabBar::tab:bottom:selected {
    border-top-color: none;
}

QTabBar::tab:top:last, QTabBar::tab:bottom:last,
QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {
    margin-right: 0;
}

QTabBar::tab:left:!selected {
    margin-right: 3px;
}

QTabBar::tab:right:!selected {
    margin-left: 3px;
}

QTabBar::tab:left, QTabBar::tab:right {
    min-height: 8ex;
    margin-bottom: -1px;
    padding: 10px 5px 10px 5px;
}

QTabBar::tab:left:selected {
    border-left-color: none;
}

QTabBar::tab:right:selected {
    border-right-color: none;
}

QTabBar::tab:left:last, QTabBar::tab:right:last,
QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {
    margin-bottom: 0;
}

"""
class TabWidget(QTabWidget):

    def __init__(self, *args, **kwargs):
        """
        TabWidget(self, tabPosition=TabWidget.North)
        TabWidget(self, tabPosition=TabWidget.South)
        TabWidget(self, tabPosition=TabWidget.West)
        TabWidget(self, tabPosition=TabWidget.East)
        """
        super(TabWidget, self).__init__(*args, **kwargs)
        # self.setStyle(TabBarStyle())
        # self.setStyleSheet(tab_style)
        # self.tabBar().setStyleSheet('border: 1px solid red;')
        # ukuran = self.window().size()
        # print(f"""
        # w = {ukuran.width()}
        # h = {ukuran.height()}
        # """)
        
    #     self.w, self.h = self.frameGeometry().width(), self.frameGeometry().height()
    #     print(f"""[tabwidget]
    #     w = {self.w}
    #     h = {self.h}
    #     """)


    def minimumSizeHint(self):
        return self.sizeHint()
    #     return QSize(100, 80)

    def sizeHint(self):
        return QSize(100, 80)
    # def sizeHint(self):
    #     # current = self.currentWidget()
    #     # if not current:
    #     #     return super().sizeHint()
    #     # return current.sizeHint()
    #     # cursize = self.frameSize()
    #     # cursize = QSize(self.frameGeometry().width, self.frameGeometry().height)
    #     # return QSize(cursize.width(), cursize.height()+30)
    #     # w,h = self.frameGeometry().width(), self.frameGeometry().height()
    #     return QSize(self.w, self.h+30)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(335, 50)
        # Form.resize(150, 25)

        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        # self.lcdNumber.setStyleSheet('border: 1px solid blue; color: yellow;')
        self.lcdNumber.setStyleSheet('color: blue;')
        # self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 250, 50))
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 100, 40))
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 2021.0)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class DigitalClock(QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(DigitalClock, self).__init__(parent)
        self.setupUi(self)
        # self.setStyleSheet('background-color')
        self.setWindowFlags(Qt.FramelessWindowHint)#无边框
        self.setAcceptDrops(True)
        self.lcdNumber.display('00:00:00')
        time_slot =QTimer(self)
        time_slot.timeout.connect(self.event_1)
        time_slot.start(1000)

    def event_1(self):
        time_format = QTime.currentTime()
        time_format = time_format.toString("hh:mm:ss")
        self.lcdNumber.display(time_format)
        QApplication.processEvents()



class AnalogClock(QLabel):
    # vintage clock
    def __init__(self,parent  =None):
        super(AnalogClock,self).__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def textRectF(self,radius,pointsize,angle):

        recf = QRectF()
        recf.setX(radius*math.cos(angle*math.pi/180.0)-pointsize*2)
        recf.setY(radius*math.sin(angle*math.pi/180.0)-pointsize/2.0)
        recf.setWidth(pointsize*4)#Width Height
        recf.setHeight(pointsize)
        return recf

    def paintEvent(self, event):
        panjang_jam = -50
        panjang_menit = -65
        panjang_detik = -80
        hour_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_jam)]
        minute_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_menit)]
        second_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_detik)]

        hour_color = QColor(200,100,0,200)
        minute_color = QColor(0,127,127,150)
        second_color = QColor(160,200,230,150) # QColor(0,160,230,150)

        min_len = min(self.width(),self.height())
        time = QTime.currentTime() #get current time
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2,self.height()/2)#Pan to center of window
        painter.scale(min_len/200.0,min_len/200.0) #scaling

        #----------绘制时针------------
        painter.setPen(Qt.NoPen)
        painter.setBrush(hour_color)#color
        painter.save()
        # according to 1 hour = 30°, rotate counterclockwise in the direction of water quality
        painter.rotate(30.0*((time.hour()+time.minute()/60.0)))
        painter.drawConvexPolygon(QPolygon(hour_points))
        painter.restore() # save Exit to reset the brush

        painter.setPen(hour_color)
        #draw hour line(360/12 = 30 degrees)
        for i in range(12):
            painter.drawLine(88,0,96,0)#draw horizontal lines
            painter.rotate(30.0)# Rotate at the original rotation angle;

        radius = 100 # 半径
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
        pointSize = font.pointSize()#字体大小
        # print(pointSize)

        #draw hour text
        for i in range(12):
            nhour = i + 3 # from level 3 point to draw
            if(nhour>12):
                nhour -= 12
            painter.drawText(self.textRectF(radius*0.8,pointSize,i*30),Qt.AlignCenter,str(nhour))

        #draw the minute hand;
        painter.setPen(Qt.NoPen)
        painter.setBrush(minute_color)
        painter.save()

        # 1分钟为6°，
        painter.rotate(6.0*(time.minute()+time.second()/60.0))
        painter.drawConvexPolygon(QPolygon(minute_points))
        painter.restore()

        #绘制分针线
        painter.setPen(minute_color)
        for i in range(60):
            if(i%5 !=0):
                painter.drawLine(92,0,96,0)
            painter.rotate(6.0)

        #绘制秒针
        painter.setPen(Qt.NoPen)
        painter.setBrush(second_color)
        painter.save()
        #绘制秒线
        painter.rotate(6.0*time.second())
        painter.drawConvexPolygon(QPolygon(second_points))
        painter.restore()

        painter.setPen(second_color)
        for i in range(360):
            if(i%5!=0 or i%30!=0):#绘制
                painter.drawLine(94,0,96,0)
            painter.rotate(1.0)#旋转



context_menu_stylesheet = """
QMenu {
    /* 半透明效果 */
    background-color: rgba(255, 255, 255, 230);
    border: none;
    border-radius: 4px;
}

QMenu::item {
    border-radius: 4px;
    /* 这个距离很麻烦需要根据菜单的长度和图标等因素微调 */
    padding: 8px 48px 8px 36px; /* 36px是文字距离左侧距离*/
    background-color: transparent;
}

/* 鼠标悬停和按下效果 */
QMenu::item:selected {
    border-radius: 0px;
    /* 半透明效果 */
    background-color: rgba(232, 232, 232, 232);
}

/* 禁用效果 */
QMenu::item:disabled {
    background-color: transparent;
}

/* 图标距离左侧距离 */
QMenu::icon {
    left: 15px;
}

/* 分割线效果 */
QMenu::separator {
    height: 1px;
    background-color: rgb(232, 236, 243);
}
"""

def get_icon():
    pixmap = QPixmap(16, 16)
    pixmap.fill(Qt.transparent)
    painter = QPainter()
    painter.begin(pixmap)
    painter.setFont(QFont('Webdings', 11))
    painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
    painter.drawText(0, 0, 16, 16, Qt.AlignCenter, random.choice(string.ascii_letters))
    painter.end()
    return QIcon(pixmap)

def about_qt():
    QApplication.instance().aboutQt()

class My_Widget(QWidget):

    def init_menu(self):
        # transparent background
        self.context_menu.setAttribute(Qt.WA_TranslucentBackground)
        # No border, remove built-in shadow
        self.context_menu.setWindowFlags(self.context_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        # Simulate menu items
        about = self.context_menu.addAction(get_icon(), 'About Qt', about_qt)
        quarter = self.context_menu.addAction(get_icon(), '1/4 screen', lambda: self.resize_screen_ratio(1/4))
        half = self.context_menu.addAction(get_icon(), '1/2 screen', lambda: self.resize_screen_ratio(1/2))        
        threequarter = self.context_menu.addAction(get_icon(), '3/4 screen', lambda: self.resize_screen_ratio(3/4))
        defaultsize = self.context_menu.addAction(get_icon(), 'default size', lambda: self.resize_screen_ratio(1/6))

        self.context_menu.addAction(get_icon(), 'bottom left', lambda: self.to_bottomleft())
        self.context_menu.addAction(get_icon(), 'bottom right', lambda: self.to_bottomright())

        self.context_menu.addSeparator()
        # activate tab
        menu = QMenu('Activate tab', self.context_menu)
        menu.setAttribute(Qt.WA_TranslucentBackground)
        menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        menu.addAction(get_icon(), 'Waktu', lambda: self.main_control.setCurrentIndex(0))
        menu.addAction(get_icon(), 'form', lambda: self.main_control.setCurrentIndex(1))
        menu.addAction(get_icon(), 'code', lambda: self.main_control.setCurrentIndex(2))
        menu.addAction(get_icon(), 'repl', lambda: self.main_control.setCurrentIndex(3))
        menu.addAction(get_icon(), 'mmm', lambda: self.main_control.setCurrentIndex(4))
        self.context_menu.addMenu(menu)
        # No border, remove built-in shadow
        self.context_menu.addSeparator()
        self.context_menu.addAction(get_icon(), 'Tray', self.systemtrayicon)
        self.context_menu.addAction(get_icon(), 'Quit', lambda: qApp.quit())

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def systemtrayicon(self):
        self.hide()
        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

    def __init__(self, parent = None):
        super(My_Widget, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # self.setStyleSheet('background: black;' + '\n\n' +context_menu_stylesheet)
        self.setStyleSheet(context_menu_stylesheet)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
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
        self.tray_icon.show()

        self.horizon_layout = QHBoxLayout() # main layout

        self.analog_clock = AnalogClock()
        self.digital_clock = DigitalClock() # lcd

        self.kanancontainer = QWidget()
        self.kananlayout = QVBoxLayout()

        # self.dummywidget = QWidget()
        # self.dummywidget.setStyleSheet('border: 1px solid red;')

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        rows = 50
        cols = 10
        for i in range(rows):
            for j in range(cols):
                btn = QtWidgets.QPushButton(f"{i},{j}")
                btn.setStyleSheet("background-color:skyblue;")
                # btn.resize(20,10) # gak pengaruh
                # btn.clicked.connect(self.button_clicked)
                self.gridLayout.addWidget(btn, i, j)
        
        # self.scrollArea.verticalScrollBar().setMaximumSize(10,10)
        
        self.scrollArea.verticalScrollBar().setMaximumWidth(10)
        self.scrollArea.horizontalScrollBar().setMaximumHeight(10)
        # self.scrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.scrollArea.resize()
        # sw = self.scrollArea.frameGeometry().width()
        # sh = self.scrollArea.frameGeometry().height()
        # ww = self.scrollArea.widget().frameGeometry().width()
        # wh = self.scrollArea.widget().frameGeometry().height()
        # print(f'''
        # sw = {sw}
        # sh = {sh}
        # ww = {ww}
        # wh = {wh}
        # ''')

        # self.scrollArea.frameGeometry().setWidth(sw + 50)
        # self.scrollArea.resize(sw+50, sh+50)
        # self.scrollArea.widget().resize(QSize(ww+5,wh+5))

        # self.dummywidget.setSizePolicy(-1, QSizePolicy.Expanding)
        # self.dummywidget.setSizePolicy(QSizePolicy.Expanding, -1)
        self.kananlayout.addWidget(self.digital_clock, 2)
        # self.kananlayout.addWidget(self.dummywidget, 8)
        self.kananlayout.addWidget(self.scrollArea, 8)

        self.kanancontainer.setLayout(self.kananlayout)
        # https://stackoverflow.com/questions/54276638/setsizepolicy-with-qsizepolicy-expanding-does-not-work-the-child-does-not-exp
        self.kananlayout.setContentsMargins(0,0,0,0)
        # self.kanancontainer.setStyleSheet('border: 1px solid green;')

        # self.analog_clock.setStyleSheet('border: 2px solid green;')
        # self.digital_clock.setStyleSheet('border: 2px solid red;')
        self.horizon_layout.addWidget(self.analog_clock, 65)
        # self.horizon_layout.addWidget(self.digital_clock, 35)
        
        # self.tabkanan = TabWidget(self, tabPosition=TabWidget.East)
        self.tabkanan = TabWidget(self, tabPosition=TabWidget.South)
        # lebar = self.tabkanan.frameGeometry().width()
        # tinggi = self.tabkanan.frameGeometry().height()
        self.tabkanan.addTab(QWidget(), "0")
        self.tabkanan.addTab(self.kanancontainer, "1")
        self.tabkanan.addTab(QWidget(), "2")
        self.tabkanan.addTab(QWidget(), "3")
        self.tabkanan.addTab(QWidget(), "4")
        self.tabkanan.addTab(QWidget(), "5")

        # self.tabkanan.tabBar().setMaximumWidth(25)
        self.tabkanan.tabBar().setMaximumHeight(25)
        # self.tabkanan.tabBar().setStyleSheet('background: black; color: green;')
        # self.tabkanan.setStyleSheet('background: black; color: green;')
        # self.horizon_layout.addWidget(self.kanancontainer, 35)

        # self.tabkanan.resize(lebar, tinggi+30)
        # self.tabkanan.resize(100, 60)

        self.horizon_layout.addWidget(self.tabkanan, 35)


        # kita pengen gini
        # ada main tab widget...
        self.main_layout = QVBoxLayout()
        self.main_control = QTabWidget()
        self.main_layout.addWidget(self.main_control)
        self.holder_previous_main = QWidget()
        self.holder_previous_main.setLayout(self.horizon_layout)
        # tab 1
        self.main_control.addTab(self.holder_previous_main, '0')
        # tab 2
        # self.main_control.addTab(QWidget(), '1')
        from fold1 import FoldedListWidget
        self.main_control.addTab(FoldedListWidget(), '1')
        # tab 3 scintilla
        self.main_control.addTab(CodeScintilla(), '2')
        # tab 4
        from embed import WindowEmbedder
        repl = WindowEmbedder()
        self.main_control.addTab(repl, '3')
        # tab 5
        from mmm import MmmWidget
        mmmw = MmmWidget()
        self.main_control.addTab(mmmw, '4')
        # hide tabbar
        self.main_control.tabBar().hide()


        # self.setLayout(self.horizon_layout)
        self.setLayout(self.main_layout)

        self.setWindowTitle("Waktuku")
        self.setWindowIcon(QIcon('fmus-fm.png'))
        self.setWindowOpacity(0.8)

        self.context_menu = QMenu(self)
        self.init_menu()

        screen_geometry = QDesktopWidget().screenGeometry(-1)
        self.w,self.h = screen_geometry.width(), screen_geometry.height()

        # posx, posy = self.reset_size()
        # self.move(posx, posy)
        self.resize_screen_ratio()

    def to_bottomright(self):
        lebar = self.width()
        posx = self.w - lebar
        delta = 60
        tinggi = self.height()
        posy = self.h - tinggi - delta
        self.move(posx, posy)

    def to_bottomleft(self):
        posx = 0
        delta = 60
        tinggi = self.height()
        posy = self.h - tinggi - delta
        self.move(posx, posy)

    def resize_screen_ratio(self, ratio=1/6):
        lebar, tinggi = int(self.w*ratio),int(self.h*ratio)
        self.resize(lebar, tinggi)
        posx = self.w - lebar
        delta = 60
        posy = self.h - tinggi - delta
        self.move(posx, posy)

    # def halfscreen_size(self):
    #     lebar, tinggi = int(self.w*1/2),int(self.h*1/2)
    #     self.resize(lebar, tinggi)
    #     posx = self.w - lebar
    #     delta = 60
    #     posy = self.h - tinggi - delta
    #     return posx, posy

    # def reset_size(self):
    #     lebar, tinggi = int(self.w*1/6),int(self.h*1/6)
    #     self.resize(lebar, tinggi)
    #     posx = self.w - lebar
    #     delta = 60
    #     posy = self.h - tinggi - delta
    #     return posx, posy

def main():
    app = QApplication(sys.argv)
    my_widget = My_Widget()
    # https://www.geeksforgeeks.org/pyqt5-how-to-hide-app-from-taskbar/
    my_widget.setWindowFlag(QtCore.Qt.Tool)
    # my_widget.setWindowIcon(QtGui.QIcon('fmus-fm.png'))
    # app.setWindowIcon(QtGui.QIcon('fmus-fm.png'))
    my_widget.show()
    sys.exit(app.exec())

if __name__ =='__main__':
    main()
    # app = QApplication(sys.argv)
    # my_widget = My_Widget()
    # # https://www.geeksforgeeks.org/pyqt5-how-to-hide-app-from-taskbar/
    # my_widget.setWindowFlag(QtCore.Qt.Tool)
    # # my_widget.setWindowIcon(QtGui.QIcon('fmus-fm.png'))
    # # app.setWindowIcon(QtGui.QIcon('fmus-fm.png'))
    # my_widget.show()
    # sys.exit(app.exec())


