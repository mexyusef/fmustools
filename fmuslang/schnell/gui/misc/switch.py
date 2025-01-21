import os, sys

from PyQt5.QtCore import Qt, pyqtProperty, QEasingCurve, QPoint, QPropertyAnimation, QParallelAnimationGroup, QTimer
from PyQt5.QtWidgets import QStackedWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QEasingCurve, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

IMAGEDIR = '../acdsee/images'

class SlidingStackedWidget(QStackedWidget):

    LEFT2RIGHT, RIGHT2LEFT, TOP2BOTTOM, BOTTOM2TOP, AUTOMATIC = range(5)

    def __init__(self, *args, **kwargs):
        super(SlidingStackedWidget, self).__init__(*args, **kwargs)
        self._pnow = QPoint(0, 0)
        # 动画速度
        self._speed = 500
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

    def setSpeed(self, speed=500):
        """Set animation speed
        :param speed:       speed value,Default is 500
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

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 612)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.stackedWidget = SlidingStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")

        self.verticalLayout.addWidget(self.stackedWidget)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.spinBoxSpeed = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxSpeed.setMinimum(100)
        self.spinBoxSpeed.setMaximum(5000)
        self.spinBoxSpeed.setProperty("value", 500)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")

        self.horizontalLayout.addWidget(self.spinBoxSpeed)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.radioButtonHor = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonHor.setChecked(True)
        self.radioButtonHor.setObjectName("radioButtonHor")

        self.horizontalLayout_2.addWidget(self.radioButtonHor)

        self.radioButtonVer = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonVer.setObjectName("radioButtonVer")

        self.horizontalLayout_2.addWidget(self.radioButtonVer)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.comboBoxEasing = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBoxEasing.setObjectName("comboBoxEasing")

        self.horizontalLayout_3.addWidget(self.comboBoxEasing)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.pushButtonPrev = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonPrev.setObjectName("pushButtonPrev")

        self.horizontalLayout_4.addWidget(self.pushButtonPrev)

        self.pushButtonNext = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonNext.setObjectName("pushButtonNext")

        self.horizontalLayout_4.addWidget(self.pushButtonNext)

        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.pushButtonStart = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.horizontalLayout_5.addWidget(self.pushButtonStart)

        self.pushButtonStop = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonStop.setObjectName("pushButtonStop")

        self.horizontalLayout_5.addWidget(self.pushButtonStop)
        self.verticalLayout.addWidget(self.groupBox_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Image carousel animation"))
        self.groupBox.setTitle(_translate("Form", "animation speed"))
        self.groupBox_2.setTitle(_translate("Form", "animation direction(The default is landscape)"))
        self.radioButtonHor.setText(_translate("Form", "horizontal"))
        self.radioButtonVer.setText(_translate("Form", "portrait"))
        self.groupBox_3.setTitle(_translate("Form", "Animation Curve Type"))
        self.groupBox_4.setTitle(_translate("Form", "turn pages"))
        self.pushButtonPrev.setText(_translate("Form", "previous page"))
        self.pushButtonNext.setText(_translate("Form", "next page"))
        self.groupBox_5.setTitle(_translate("Form", "carousel"))
        self.pushButtonStart.setText(_translate("Form", "Carousel starts"))
        self.pushButtonStop.setText(_translate("Form", "carousel stopped"))


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())


class ImageSliderWidget(QWidget, Ui_Form):

    """
    self.spinBoxSpeed.valueChanged.connect(self.stackedWidget.setSpeed)
    self.pushButtonPrev.clicked.connect(self.stackedWidget.slideInPrev)
    self.pushButtonNext.clicked.connect(self.stackedWidget.slideInNext)
    self.stackedWidget.addWidget(label)
    self.stackedWidget.autoStart()
    self.stackedWidget.autoStop()
    self.stackedWidget.setEasing(getattr(QEasingCurve, name))
    self.stackedWidget.setOrientation(Qt.Horizontal if hor else Qt.Vertical)
    """

    def __init__(self, *args, **kwargs):
        super(ImageSliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Initialize the animation curve type
        curve_types = [(n, c) for n, c in QEasingCurve.__dict__.items()
                       if isinstance(c, QEasingCurve.Type)]
        curve_types.sort(key=lambda ct: ct[1])
        curve_types = [c[0] for c in curve_types]
        self.comboBoxEasing.addItems(curve_types)

        # bind signal slot
        self.spinBoxSpeed.valueChanged.connect(self.stackedWidget.setSpeed)
        self.pushButtonPrev.clicked.connect(self.stackedWidget.slideInPrev)
        self.pushButtonNext.clicked.connect(self.stackedWidget.slideInNext)

        self.comboBoxEasing.currentTextChanged.connect(self.setEasing)
        self.radioButtonHor.toggled.connect(self.setOrientation)
        self.radioButtonVer.toggled.connect(self.setOrientation)

        self.pushButtonStart.clicked.connect(self.autoStart)
        self.pushButtonStop.clicked.connect(self.autoStop)

        # add image page
        for name in os.listdir(IMAGEDIR):
            label = QLabel(self.stackedWidget)
            label.setScaledContents(True)
            # label.setPixmap(QPixmap(f'{IMAGEDIR}/' + name))
            label.setText(name)
            self.stackedWidget.addWidget(label)

    def autoStart(self):
        self.pushButtonNext.setEnabled(False)
        self.pushButtonPrev.setEnabled(False)
        self.stackedWidget.autoStart()

    def autoStop(self):
        self.pushButtonNext.setEnabled(True)
        self.pushButtonPrev.setEnabled(True)
        self.stackedWidget.autoStop()

    def setEasing(self, name):
        self.stackedWidget.setEasing(getattr(QEasingCurve, name))

    def setOrientation(self, checked):
        hor = self.sender() == self.radioButtonHor
        if checked:
            self.stackedWidget.setOrientation(Qt.Horizontal if hor else Qt.Vertical)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ImageSliderWidget()
    w.show()
    sys.exit(app.exec_())
