import os, sys
from functools import partial
from turtle import pos

from PyQt5.QtCore import (
    Qt, 
    pyqtProperty, 
    QEasingCurve, 
    QPoint, 
    QPropertyAnimation, 
    QParallelAnimationGroup, 
    QTimer,
)
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QStackedWidget,
    QApplication,
)
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtWidgets import (
	QApplication,
	QCheckBox,
	QDesktopWidget,
	QDialog,
	QFormLayout,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMessageBox,
	QMenu,
	QPushButton,
	QScrollArea,
	QShortcut,
	QTextEdit,
	QToolTip,
	QVBoxLayout,
	QWidget,
	qApp,
)

miscdir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
guidir = os.path.normpath(os.path.join(miscdir, os.pardir))
schnelldir = os.path.normpath(os.path.join(guidir, os.pardir))
envfile = os.path.join(schnelldir, '.env')
from dotenv import load_dotenv
load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
sys.path.extend([schnelldir, '..'])
from app.utils import env_get
from app.dirutils import isfile
from app.fileutils import file_content


if __name__ == '__main__':
    # guidir = os.path.normpath(os.path.join(systemdir, os.pardir))
    print(f"""
    miscdir = {miscdir}
    guidir = {guidir}
    """)
    sys.path.append(guidir)
    from system.editor.editor import CodeScintilla
    from primitives.flowwidget import FlowWidget
else:
    from ..system.editor.editor import CodeScintilla
    from ..primitives.flowwidget import FlowWidget

def handle_186_1():
    QMessageBox.critical(
        None,
        "Critical",
        "Critical body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )
def handle_186_2():
    QMessageBox.information(
        None,
        "Information",
        "Information body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )
def handle_186_3():
    QMessageBox.warning(
        None,
        "Warning",
        "Warning body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )
def handle_186_4():
    QMessageBox.question(
        None,
        "Question",
        "Question body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )
button_groups_by_number = {
    '186': {
        'critical': handle_186_1,
        'information': handle_186_2,
        'warning': handle_186_3,
        'question': handle_186_4,
    },
    '187': {
        'kritis': handle_186_1,
        'info': handle_186_2,
        'tanya': handle_186_4,
    },
}


default_stylesheet = """
background-color:skyblue;
"""

def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, h_ratio=0, delta = 60):
    """
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    if not h_ratio:
        h_ratio = ratio
    lebar, tinggi = int(screenw*ratio),int(screenh*h_ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)


DEFAULT_SPEED = 250

class SlidingStackedWidget(QStackedWidget):

    LEFT2RIGHT, RIGHT2LEFT, TOP2BOTTOM, BOTTOM2TOP, AUTOMATIC = range(5)

    def __init__(self, *args, **kwargs):
        super(SlidingStackedWidget, self).__init__(*args, **kwargs)
        self._pnow = QPoint(0, 0)
        # 动画速度
        self._speed = DEFAULT_SPEED
        # 当前索引
        self._now = 0
        # 自动模式的当前索引
        self._current = 0
        # 下一个索引
        self._next = 0
        # 是否激活
        self._active = 0
        # 动画方向(默认是横向)
        self._orientation = Qt.Horizontal
        # 动画曲线类型
        self._easing = QEasingCurve.Linear
        # 初始化动画
        self._initAnimation()

    def setSpeed(self, speed=DEFAULT_SPEED):
        """Set animation speed
        :param speed:       speed value, Default is DEFAULT_SPEED
        :type speed:        int
        """
        self._speed = speed

    @pyqtProperty(int, fset=setSpeed)
    def speed(self):
        return self._speed

    def setOrientation(self, orientation=Qt.Horizontal):
        """Set the direction of the animation(landscape and portrait)
        :param orientation:    direction(Qt.Horizontal or Qt.Vertical)
        :type orientation:     http://doc.qt.io/qt-5/qt.html#Orientation-enum
        """
        self._orientation = orientation

    @pyqtProperty(int, fset=setOrientation)
    def orientation(self):
        return self._orientation

    def setEasing(self, easing=QEasingCurve.OutBack):
        """Set the curve type for animation
        :param easing:    默认为QEasingCurve.OutBack
        :type easing:     http://doc.qt.io/qt-5/qeasingcurve.html#Type-enum
        """
        self._easing = easing

    @pyqtProperty(int, fset=setEasing)
    def easing(self):
        return self._easing

    def slideInNext(self):
        """Swipe to next page"""
        now = self.currentIndex()
        if now < self.count() - 1:
            self.slideInIdx(now + 1)
            self._current = now + 1

    def slideInPrev(self):
        """Swipe to previous page"""
        now = self.currentIndex()
        if now > 0:
            self.slideInIdx(now - 1)
            self._current = now - 1

    def slideInLast(self):
        """Swipe to last page"""
        # now = self.currentIndex()
        # if now < self.count() - 1:
        #     self.slideInIdx(now + 1)
        #     self._current = now + 1
        pos = self.count() - 1
        self.slideInIdx(pos)
        self._current = pos

    def slideInFirst(self):
        """Swipe to first page"""
        pos = 0
        self.slideInIdx(pos)
        self._current = pos

    def slideInIdx(self, idx, direction=4):
        """Slide to the specified serial number
        :param idx:               serial number
        :type idx:                int
        :param direction:         direction,The default is AUTOMATIC=4
        :type direction:          int
        """
        if idx > self.count() - 1:
            direction = self.TOP2BOTTOM if self._orientation == Qt.Vertical else self.RIGHT2LEFT
            idx = idx % self.count()
        elif idx < 0:
            direction = self.BOTTOM2TOP if self._orientation == Qt.Vertical else self.LEFT2RIGHT
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx), direction)

    def slideInWgt(self, widget, direction):
        """Swipe to the specified widget
        :param widget:        QWidget, QLabel, etc...
        :type widget:         QWidget Base Class
        :param direction:     direction
        :type direction:      int
        """
        if self._active:
            return
        self._active = 1
        _now = self.currentIndex()
        _next = self.indexOf(widget)
        if _now == _next:
            self._active = 0
            return

        w_now = self.widget(_now)
        w_next = self.widget(_next)

        # 自动判断方向
        if _now < _next:
            directionhint = self.TOP2BOTTOM if self._orientation == Qt.Vertical else self.RIGHT2LEFT
        else:
            directionhint = self.BOTTOM2TOP if self._orientation == Qt.Vertical else self.LEFT2RIGHT
        if direction == self.AUTOMATIC:
            direction = directionhint

        # 计算偏移量
        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()
        w_next.setGeometry(0, 0, offsetX, offsetY)

        if direction == self.BOTTOM2TOP:
            offsetX = 0
            offsetY = -offsetY
        elif direction == self.TOP2BOTTOM:
            offsetX = 0
        elif direction == self.RIGHT2LEFT:
            offsetX = -offsetX
            offsetY = 0
        elif direction == self.LEFT2RIGHT:
            offsetY = 0

        # 重新定位显示区域外部/旁边的下一个窗口小部件
        pnext = w_next.pos()
        pnow = w_now.pos()
        self._pnow = pnow

        # 移动到指定位置并显示
        w_next.move(pnext.x() - offsetX, pnext.y() - offsetY)
        w_next.show()
        w_next.raise_()

        self._animnow.setTargetObject(w_now)
        self._animnow.setDuration(self._speed)
        self._animnow.setEasingCurve(self._easing)
        self._animnow.setStartValue(QPoint(pnow.x(), pnow.y()))
        self._animnow.setEndValue(
            QPoint(offsetX + pnow.x(), offsetY + pnow.y()))

        self._animnext.setTargetObject(w_next)
        self._animnext.setDuration(self._speed)
        self._animnext.setEasingCurve(self._easing)
        self._animnext.setStartValue(
            QPoint(-offsetX + pnext.x(), offsetY + pnext.y()))
        self._animnext.setEndValue(QPoint(pnext.x(), pnext.y()))

        self._next = _next
        self._now = _now
        self._active = 1
        self._animgroup.start()

    def _initAnimation(self):
        """Initialize animation variables for current page and next page"""
        # 当前页的动画
        self._animnow = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # 下一页的动画
        self._animnext = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # 并行动画组
        self._animgroup = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot)
        self._animgroup.addAnimation(self._animnow)
        self._animgroup.addAnimation(self._animnext)

    def setCurrentIndex(self, index):
        # 覆盖该方法实现的动画切换
        # super(SlidingStackedWidget, self).setCurrentIndex(index)
        # 坚决不能调用上面的函数,否则动画失效
        self.slideInIdx(index)

    def setCurrentWidget(self, widget):
        # 覆盖该方法实现的动画切换
        super(SlidingStackedWidget, self).setCurrentWidget(widget)
        # 坚决不能调用上面的函数,否则动画失效
        self.setCurrentIndex(self.indexOf(widget))

    def animationDoneSlot(self):
        """animation end handler"""
        # 由于重写了setCurrentIndex方法所以这里要用父类本身的方法
        #         self.setCurrentIndex(self._next)
        QStackedWidget.setCurrentIndex(self, self._next)
        w = self.widget(self._now)
        w.hide()
        w.move(self._pnow)
        self._active = 0

    def autoStop(self):
        """stop autoplay"""
        if hasattr(self, '_autoTimer'):
            self._autoTimer.stop()

    def autoStart(self, msec=3000):
        """Automatic carousel
        :param time: time, Default 3000, 3 seconds
        """
        if not hasattr(self, '_autoTimer'):
            self._autoTimer = QTimer(self, timeout=self._autoStart)
        self._autoTimer.stop()
        self._autoTimer.start(msec)

    def _autoStart(self):
        if self._current == self.count():
            self._current = 0
        self._current += 1
        self.setCurrentIndex(self._current)


class AnimationShadowEffect(QGraphicsDropShadowEffect):

    def __init__(self, color, *args, **kwargs):
        super(AnimationShadowEffect, self).__init__(*args, **kwargs)
        self.setColor(color)
        self.setOffset(0, 0)
        self.setBlurRadius(0)
        self._radius = 0
        self.animation = QPropertyAnimation(self)
        self.animation.setTargetObject(self)
        self.animation.setDuration(2000)
        self.animation.setLoopCount(-1)
        self.animation.setPropertyName(b'radius')
        self.animation.setKeyValueAt(0, 1)
        self.animation.setKeyValueAt(0.5, 30)
        self.animation.setKeyValueAt(1, 1)

    def start(self):
        self.animation.start()

    def stop(self, r=0):
        self.animation.stop()
        self.radius = r

    @pyqtProperty(int)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.setBlurRadius(r)

class BlockWidget(QWidget):

    def __init__(self, parent=None, angka_mulai=0, style_sheet=default_stylesheet, effect=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.angka_mulai = angka_mulai
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        if effect:
            self.setGraphicsEffect(effect)

        rows = 20
        cols = 5
        self.buttons = []
        button_label = self.angka_mulai
        # counter = 0
        for i in range(rows):
            for j in range(cols):
                # btn = QPushButton(f"{button_label}")
                btn = QPushButton(str(button_label))
                
                if button_label < self.angka_mulai+25:
                    btn.setStyleSheet(style_sheet)
                elif button_label < self.angka_mulai+50:
                    btn.setStyleSheet('background-color: #55aaff;')
                elif button_label < self.angka_mulai+75:
                    btn.setStyleSheet('background-color: #008ed5;')
                else:
                    btn.setStyleSheet('background-color: #0055ff;')
                btn.setToolTip(f'This is <i>button</i> number <b>{i}, {j}</b> or <u>{button_label}</u>.')
                # btn.clicked.connect(lambda: click_handler(button_label))
                # btn.clicked.connect(click_handler)
                # btn.clicked.connect(lambda: self.click_me(self.angka_mulai + counter))
                # btn.clicked.connect(lambda state: self.click_me(counter))
                # btn.clicked.connect(partial(self.click_me, self.angka_mulai))
                # btn.clicked.connect(partial(self.click_me, button_label))
                # btn.clicked.connect(partial(self.click_me, btn.text()))

                aniButton = AnimationShadowEffect(Qt.blue, btn)
                btn.setGraphicsEffect(aniButton)
                aniButton.start()
                # btn.clicked.connect(self.button_clicked)
                self.gridLayout.addWidget(btn, i, j)
                # counter += 1
                button_label += 1
                # self.angka_mulai += 1
                self.buttons.append(btn)

        lay = QVBoxLayout()
        lay.addWidget(self.scrollArea)
        self.setLayout(lay)
    
    def click_me(self, nilai):
        print('click me:', nilai)


class MMM(QWidget):

    def __init__(self, editor, flow_widget, *args, **kwargs):
        super(MMM, self).__init__(*args, **kwargs)
        self.editor = editor
        self.flow_widget = flow_widget
        self.setWindowTitle('MMM')

        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        self.button_box = QtWidgets.QGroupBox(self)
        self.button_box.setObjectName("button_box")
        self.button_layout = QtWidgets.QHBoxLayout(self.button_box)
        self.button_layout.setObjectName("button_layout")

        self.pushButtonPrev = QtWidgets.QPushButton(self.button_box)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.pushButtonPrev.setText('<<')
        
        self.pushButtonFirst = QtWidgets.QPushButton(self.button_box)
        self.pushButtonFirst.setObjectName("pushButtonFirst")
        self.pushButtonFirst.setText('|<')

        self.buttonQUit = QtWidgets.QPushButton(self.button_box)
        self.buttonQUit.setObjectName("buttonQUit")
        self.buttonQUit.setText('x')

        self.pushButtonLast = QtWidgets.QPushButton(self.button_box)
        self.pushButtonLast.setObjectName("pushButtonLast")
        self.pushButtonLast.setText('>|')

        self.pushButtonNext = QtWidgets.QPushButton(self.button_box)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonNext.setText('>>')

        self.button_layout.addWidget(self.pushButtonPrev)
        self.button_layout.addWidget(self.pushButtonFirst)
        self.button_layout.addWidget(self.buttonQUit)
        self.button_layout.addWidget(self.pushButtonLast)
        self.button_layout.addWidget(self.pushButtonNext)
        self.verticalLayout.addWidget(self.button_box)
        
        # self.tab_bar = QtGui.QTabBar(self)
        # self.add_button = QtGui.QToolButton()
        # self.add_button.setIcon(QtGui.QIcon('add.png'))
        # self.add_button.clicked.connect(self.set_menu)
        # self.tab_bar.setTabButton(
        #     0,
        #     QtGui.QTabBar.ButtonPosition.RightSide,
        #     self.add_button,
        # )

        self.stackedWidget = SlidingStackedWidget(self)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.setLayout(self.verticalLayout)

        self.pushButtonPrev.clicked.connect(self.stackedWidget.slideInPrev)
        self.pushButtonNext.clicked.connect(self.stackedWidget.slideInNext)
        self.pushButtonFirst.clicked.connect(self.stackedWidget.slideInFirst)
        self.pushButtonLast.clicked.connect(self.stackedWidget.slideInLast)
        self.buttonQUit.clicked.connect(lambda: qApp.quit())

        for num in range(10):
            # label = QLabel(self.stackedWidget)
            # label.setScaledContents(True)
            # # label.setPixmap(QPixmap(f'{IMAGEDIR}/' + name))
            # label.setText(str(num))
            angka_mulai = num*100
            label = BlockWidget(self, angka_mulai)
            self.stackedWidget.addWidget(label)
            # connect
            for i in range(100):
                # print(f'mulai: {angka_mulai}, index: {i}')
                label.buttons[i].clicked.connect(partial(self.show_button_content_in_editor, label.buttons[i].text()))

    def show_button_content_in_editor(self, angka):
        mmm_zau_folder    = env_get('ULIBPY_ZAUDIR')
        filename = angka.zfill(3) + '.txt'
        filepath = os.path.join(mmm_zau_folder, filename)
        if isfile(filepath):
            content = file_content(filepath)
            self.editor.setText(content)
            self.editor.setWindowTitle(filename)
            self.editor.foldAll()
        if angka in button_groups_by_number:
            # print(f"FOUND {angka} => {button_groups_by_number[angka].keys()}")
            widgets = []
            for k,v in button_groups_by_number[angka].items():
                # btn = QPushButton(f"{angka}/{k}")
                btn = QPushButton(f"{k}")
                widgets.append(btn)
                btn.clicked.connect(v)
            self.flow_widget.clear_add_items(widgets)
            self.flow_widget.setWindowTitle(angka)

def main():
    app = QApplication(sys.argv)

    editor = CodeScintilla()
    # rw = w.rect().topRight()
    # print(f"""
    # w rect = {w.rect()}
    # pindah ke {rw}
    # """)
    editor.resize(1000, 600)
    # editor.move(1000, 100)
    # editor.move(rw) # ke x1, y0
    editor.show()

    flow = FlowWidget()
    # flow.resize(300, 600)
    # flow.move(100, 100)
    flow.show()

    w = MMM(editor, flow)
    # w.resize(800, 600)
    w.show()

    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(flow, screenw, screenh, posx_ratio=0.01, ratio=1/8, h_ratio=0.5)
    resize_screen_ratio(w, screenw, screenh, posx_ratio=0.21, ratio=1/2, h_ratio=0.8)
    resize_screen_ratio(editor, screenw, screenh, posx_ratio=0.99, ratio=2/5, h_ratio=0.8)


    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
