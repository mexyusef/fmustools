
import string, webbrowser
import os, random

from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal, pyqtSlot, pyqtProperty, QRandomGenerator
from PyQt5.QtCore import QPointF, QRectF, QSizeF, QParallelAnimationGroup, QIODevice, QByteArray
from PyQt5.QtCore import QEasingCurve

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox, QToolBar, QLineEdit, QAction

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QColor, QGradient, QLinearGradient, QPainter, QPen, QStandardItemModel, QStandardItem
# pip install PyQtChart
from PyQt5.QtChart import QChartView, QChart, QBarSet, QBarSeries, QBarCategoryAxis, QCategoryAxis
from PyQt5.QtChart import QPieSeries
from PyQt5.QtChart import QScatterSeries
from PyQt5.QtChart import QSplineSeries
from PyQt5.QtChart import QLineSeries, QAreaSeries
from PyQt5.QtChart import QValueAxis, QDateTimeAxis
from PyQt5.QtChart import QStackedBarSeries
from PyQt5.QtChart import QPercentBarSeries, QHorizontalPercentBarSeries, QHorizontalBarSeries, QLegend

from PyQt5.QtCore import QDateTime, QDate, QUrl
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QImage
from PyQt5.QtWidgets import QTableView, QTableWidget, QTableWidgetItem, QLabel, QComboBox, QDateEdit, QDateTimeEdit, QSpinBox, QCheckBox, QSizePolicy, QGraphicsProxyWidget, QGraphicsLineItem, QMainWindow, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene, QMenu, QStackedWidget




class MyTableView(QTableView):

    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)
        self.resize(800, 600)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)  # 右键菜单
        self.setEditTriggers(self.NoEditTriggers)  # 禁止编辑
        self.doubleClicked.connect(self.onDoubleClick)
        self.addAction(QAction("copy", self, triggered=self.copyData))
        self.myModel = QStandardItemModel()  # model
        self.initHeader()  # 初始化表头
        self.setModel(self.myModel)
        self.initData()  # 初始化模拟数据

    def onDoubleClick(self, index):
        print(index.row(), index.column(), index.data())

    def keyPressEvent(self, event):
        super(MyTableView, self).keyPressEvent(event)
        # Ctrl + C
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.copyData()

    def copyData(self):
        count = len(self.selectedIndexes())
        if count == 0:
            return
        if count == 1:  # 只复制了一个
            QApplication.clipboard().setText(
                self.selectedIndexes()[0].data())  # 复制到剪贴板中
            QMessageBox.information(self, "hint", "A data has been copied")
            return
        rows = set()
        cols = set()
        for index in self.selectedIndexes():  # 得到所有选择的
            rows.add(index.row())
            cols.add(index.column())
            # print(index.row(),index.column(),index.data())
        if len(rows) == 1:  # 一行
            QApplication.clipboard().setText("\t".join(
                [index.data() for index in self.selectedIndexes()]))  # 复制
            QMessageBox.information(self, "hint", "A row of data has been copied")
            return
        if len(cols) == 1:  # 一列
            QApplication.clipboard().setText("\r\n".join(
                [index.data() for index in self.selectedIndexes()]))  # 复制
            QMessageBox.information(self, "hint", "A column of data has been copied")
            return
        mirow, marow = min(rows), max(rows)  # 最(少/多)行
        micol, macol = min(cols), max(cols)  # 最(少/多)列
        print(mirow, marow, micol, macol)
        arrays = [
            [
                "" for _ in range(macol - micol + 1)
            ] for _ in range(marow - mirow + 1)
        ]  # 创建二维数组(并排除前面的空行和空列)
        print(arrays)
        # 填充数据
        for index in self.selectedIndexes():  # 遍历所有选择的
            arrays[index.row() - mirow][index.column() - micol] = index.data()
        print(arrays)
        data = ""  # 最后的结果
        for row in arrays:
            data += "\t".join(row) + "\r\n"
        print(data)
        QApplication.clipboard().setText(data)  # 复制到剪贴板中
        QMessageBox.information(self, "hint", "copied")

    def initHeader(self):
        for i in range(5):
            self.myModel.setHorizontalHeaderItem(
                i, QStandardItem("header" + str(i + 1)))

    def initData(self):
        for row in range(100):
            for col in range(5):
                self.myModel.setItem(
                    row, col, QStandardItem("row: {row},col: {col}".format(row=row + 1, col=col + 1)))


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
        """设置动画速度
        :param speed:       速度值,默认值为500
        :type speed:        int
        """
        self._speed = speed

    @pyqtProperty(int, fset=setSpeed)
    def speed(self):
        return self._speed

    def setOrientation(self, orientation=Qt.Horizontal):
        """设置动画的方向(横向和纵向)
        :param orientation:    方向(Qt.Horizontal或Qt.Vertical)
        :type orientation:     http://doc.qt.io/qt-5/qt.html#Orientation-enum
        """
        self._orientation = orientation

    @pyqtProperty(int, fset=setOrientation)
    def orientation(self):
        return self._orientation

    def setEasing(self, easing=QEasingCurve.OutBack):
        """设置动画的曲线类型
        :param easing:    默认为QEasingCurve.OutBack
        :type easing:     http://doc.qt.io/qt-5/qeasingcurve.html#Type-enum
        """
        self._easing = easing

    @pyqtProperty(int, fset=setEasing)
    def easing(self):
        return self._easing

    def slideInNext(self):
        """滑动到下一页"""
        now = self.currentIndex()
        if now < self.count() - 1:
            self.slideInIdx(now + 1)
            self._current = now + 1

    def slideInPrev(self):
        """滑动到上一页"""
        now = self.currentIndex()
        if now > 0:
            self.slideInIdx(now - 1)
            self._current = now - 1

    def slideInIdx(self, idx, direction=4):
        """滑动到指定序号
        :param idx:               序号
        :type idx:                int
        :param direction:         方向,默认是自动AUTOMATIC=4
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
        """滑动到指定的widget
        :param widget:        QWidget, QLabel, etc...
        :type widget:         QWidget Base Class
        :param direction:     方向
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
        """初始化当前页和下一页的动画变量"""
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
        """动画结束处理函数"""
        # 由于重写了setCurrentIndex方法所以这里要用父类本身的方法
        #         self.setCurrentIndex(self._next)
        QStackedWidget.setCurrentIndex(self, self._next)
        w = self.widget(self._now)
        w.hide()
        w.move(self._pnow)
        self._active = 0

    def autoStop(self):
        """停止自动播放"""
        if hasattr(self, '_autoTimer'):
            self._autoTimer.stop()

    def autoStart(self, msec=3000):
        """自动轮播
        :param time: 时间, 默认3000, 3秒
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


class PageSwitching_Ui_Form(object):
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


imagedir = 'images'


class ImageSliderWidget(QWidget, PageSwitching_Ui_Form):

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
        self.comboBoxEasing.currentTextChanged.connect(self.setEasing)
        self.radioButtonHor.toggled.connect(self.setOrientation)
        self.radioButtonVer.toggled.connect(self.setOrientation)
        self.pushButtonPrev.clicked.connect(self.stackedWidget.slideInPrev)
        self.pushButtonNext.clicked.connect(self.stackedWidget.slideInNext)
        self.pushButtonStart.clicked.connect(self.autoStart)
        self.pushButtonStop.clicked.connect(self.autoStop)

        # add image page
        for name in os.listdir(imagedir):
            label = QLabel(self.stackedWidget)
            label.setScaledContents(True)
            label.setPixmap(QPixmap(f'{imagedir}/' + name))
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
            self.stackedWidget.setOrientation(
                Qt.Horizontal if hor else Qt.Vertical)


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
    # test mock icon
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
    # About Qt
    QApplication.instance().aboutQt()

class ImageView(QGraphicsView):
    """Image viewing controls"""

    def doShow(self):
        try:
            # Attempt to cancel the signal that closes the window after the animation is complete
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # The transparency range gradually increases from 0 to 1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # Close the window when the animation is complete
        # Transparency range gradually decreases from 1 to 0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def init_menu(self):
        # transparent background
        self.context_menu.setAttribute(Qt.WA_TranslucentBackground)
        # No border, remove built-in shadow
        self.context_menu.setWindowFlags(
            self.context_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        # Simulate menu items
        for i in range(10):
            if i % 2 == 0:
                action = self.context_menu.addAction('menu %d' % i, about_qt)
                action.setEnabled(i % 4)
            elif i % 3 == 0:
                self.context_menu.addAction(get_icon(), 'menu %d' % i, about_qt)
            if i % 4 == 0:
                self.context_menu.addSeparator()
            if i % 5 == 0:
                # 二级菜单
                # 二级菜单
                menu = QMenu('Secondary menu %d' % i, self.context_menu)
                # 背景透明
                menu.setAttribute(Qt.WA_TranslucentBackground)
                # No border, remove built-in shadow
                menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
                for j in range(3):
                    menu.addAction(get_icon(), 'Submenu %d' % j)
                self.context_menu.addMenu(menu)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QPixmap(file_path))
            event.accept()
        else:
            event.ignore()

    def __init__(self, *args, **kwargs):
        image = kwargs.pop('image', 'bg.jpg')
        background = kwargs.pop('background', Qt.black)
        super(ImageView, self).__init__(*args, **kwargs)

        self.setAcceptDrops(True)

        self.setStyleSheet(context_menu_stylesheet)

        self.setCursor(Qt.OpenHandCursor)
        self.setBackground(background)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                            QPainter.SmoothPixmapTransform)
        self.setCacheMode(self.CacheBackground)
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        self._item = QGraphicsPixmapItem()  # place image
        self._item.setFlags(QGraphicsPixmapItem.ItemIsFocusable |
                            QGraphicsPixmapItem.ItemIsMovable)
        self._scene = QGraphicsScene(self)  # Scenes
        self.setScene(self._scene)
        self._scene.addItem(self._item)

        rect = QApplication.instance().desktop().availableGeometry(self)
        self.resize(int(rect.width() * 2 / 3), int(rect.height() * 2 / 3))

        self.pixmap = None
        self._delta = 0.1  # zoom
        self.setPixmap(image)

        # tambah context menu
        self.context_menu = QMenu(self)
        self.init_menu()

        # sblm show, tapi gak berhasil, hrsnya wkt panggil di button click: imagebutton
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(1000)  # Duration 1 second

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def setBackground(self, color):
        """设置背景颜色
        :param color: 背景颜色
        :type color: QColor or str or GlobalColor
        """
        if isinstance(color, QColor):
            self.setBackgroundBrush(color)
        elif isinstance(color, (str, Qt.GlobalColor)):
            color = QColor(color)
            if color.isValid():
                self.setBackgroundBrush(color)

    def setPixmap(self, pixmap, fitIn=True):
        """加载图片
        :param pixmap: 图片或者图片路径
        :param fitIn: 是否适应
        :type pixmap: QPixmap or QImage or str
        :type fitIn: bool
        """
        if isinstance(pixmap, QPixmap):
            self.pixmap = pixmap
        elif isinstance(pixmap, QImage):
            self.pixmap = QPixmap.fromImage(pixmap)
        elif isinstance(pixmap, str) and os.path.isfile(pixmap):
            self.pixmap = QPixmap(pixmap)
        else:
            return
        self._item.setPixmap(self.pixmap)
        self._item.update()
        self.setSceneDims()
        if fitIn:
            self.fitInView(QRectF(self._item.pos(), QSizeF(
                self.pixmap.size())), Qt.KeepAspectRatio)
        self.update()

    def setSceneDims(self):
        if not self.pixmap:
            return
        self.setSceneRect(QRectF(QPointF(0, 0), QPointF(self.pixmap.width(), self.pixmap.height())))

    def fitInView(self, rect, flags=Qt.IgnoreAspectRatio):
        """剧中适应
        :param rect: 矩形范围
        :param flags:
        :return:
        """
        if not self.scene() or rect.isNull():
            return
        unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        viewRect = self.viewport().rect()
        sceneRect = self.transform().mapRect(rect)
        x_ratio = viewRect.width() / sceneRect.width()
        y_ratio = viewRect.height() / sceneRect.height()
        if flags == Qt.KeepAspectRatio:
            x_ratio = y_ratio = min(x_ratio, y_ratio)
        elif flags == Qt.KeepAspectRatioByExpanding:
            x_ratio = y_ratio = max(x_ratio, y_ratio)
        self.scale(x_ratio, y_ratio)
        self.centerOn(rect.center())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def zoomIn(self):
        """放大"""
        self.zoom(1 + self._delta)

    def zoomOut(self):
        """缩小"""
        self.zoom(1 - self._delta)

    def zoom(self, factor):
        """缩放
        :param factor: 缩放的比例因子
        """
        _factor = self.transform().scale(
            factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            # 防止过大过小
            return
        self.scale(factor, factor)


m_listCount = 3
m_valueMax = 10
m_valueCount = 7


def generateRandomData(listCount, valueMax, valueCount):
    random.seed()
    dataTable = []
    for i in range(listCount):
        dataList = []
        yValue = 0.0
        f_valueCount = float(valueCount)
        for j in range(valueCount):
            yValue += random.uniform(0, valueMax) / f_valueCount
            value = j + random.random() * m_valueMax / f_valueCount, yValue
            label = "Slice " + str(i) + ":" + str(j)
            dataList.append((value, label))
        dataTable.append(dataList)
    return dataTable


m_dataTable = generateRandomData(m_listCount, m_valueMax, m_valueCount)


def getChart(title):
    chart = QChart(title=title)
    for i, data_list in enumerate(m_dataTable):
        series = QLineSeries(chart)
        for value, _ in data_list:
            series.append(*value)
        series.setName("Series " + str(i))
        chart.addSeries(series)
    chart.createDefaultAxes()  # 创建默认的轴
    return chart


def customAxisX(chart):
    # 自定义x轴(均分)
    series = chart.series()
    if not series:
        return
    axisx = QCategoryAxis(
        chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
    minx = chart.axisX().min()
    maxx = chart.axisX().max()
    tickc = chart.axisX().tickCount()
    if tickc < 2:
        axisx.append("lable0", minx)
    else:
        step = (maxx - minx) / (tickc - 1)  # tickc>=2
        for i in range(0, tickc):
            axisx.append("lable%s" % i, minx + i * step)
    chart.setAxisX(axisx, series[-1])


def customTopAxisX(chart):
    # 自定义top x轴
    series = chart.series()
    if not series:
        return
    category = ["%d月" % i for i in range(1, 9)]  # 1-8月
    axisx = QCategoryAxis(
        chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
    axisx.setGridLineVisible(False)  # 隐藏网格线条
    axisx.setTickCount(len(category))  # 设置刻度个数
    chart.axisX().setTickCount(len(category))  # 强制修改x轴的刻度个数一致
    minx = chart.axisX().min()
    maxx = chart.axisX().max()
    tickc = chart.axisX().tickCount()
    step = (maxx - minx) / (tickc - 1)  # tickc>=2
    for i in range(0, tickc):
        axisx.append(category[i], minx + i * step)
    chart.addAxis(axisx, Qt.AlignTop)  # 添加到右侧
    series[-1].attachAxis(axisx)  # 附加到series上


def customAxisY(chart):
    # 自定义y轴(不等分)
    series = chart.series()
    if not series:
        return
    category = ["周一", "周二", "周三", "周四",
                "周五", "周六", "周日"]
    axisy = QCategoryAxis(
        chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
    axisy.setGridLineVisible(False)  # 隐藏网格线条
    axisy.setTickCount(len(category))  # 设置刻度个数
    miny = chart.axisY().min()
    maxy = chart.axisY().max()
    tickc = axisy.tickCount()
    if tickc < 2:
        axisy.append(category[0])
    else:
        step = (maxy - miny) / (tickc - 1)  # tickc>=2
        for i in range(0, tickc):
            axisy.append(category[i], miny + i * step)
    chart.addAxis(axisy, Qt.AlignRight)  # 添加到右侧
    series[-1].attachAxis(axisy)  # 附加到series上


class MyCustomxyAxis(QWidget):

    def __init__(self, *args, **kwargs):
        super(MyCustomxyAxis, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)

        # 自定义x轴(和原来的x轴值对应等分)
        chart = getChart("自定义x轴(和原来的x轴值对应等分)")
        customAxisX(chart)
        layout.addWidget(QChartView(chart, self))
        # 自定义添加右侧y轴(等分,与左侧不对应)
        chart = getChart("自定义添加右侧y轴(等分,与左侧不对应)")
        customAxisY(chart)
        layout.addWidget(QChartView(chart, self))
        # 自定义top x轴(按现有新的x轴划分)
        chart = getChart("自定义top x轴(按现有新的x轴划分)")
        customTopAxisX(chart)
        layout.addWidget(QChartView(chart, self))


class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, points):
        self.titleLabel.setText(title)
        for serie, point in points:
            if serie not in self.Cache:
                item = ToolTipItem(
                    serie.color(),
                    (serie.name() or "-") + ":" + str(point.y()), self)
                self.layout().addWidget(item)
                self.Cache[serie] = item
            else:
                self.Cache[serie].setText(
                    (serie.name() or "-") + ":" + str(point.y()))
            self.Cache[serie].setVisible(serie.isVisible())  # 隐藏那些不可用的项
        self.adjustSize()  # 调整大小


class ToolTipWidgetForBar(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidgetForBar, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidgetForBar{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, bars):
        self.titleLabel.setText(title)
        for bar, value in bars:
            if bar not in self.Cache:
                item = ToolTipItem(
                    bar.color(),
                    (bar.label() or "-") + ":" + str(value), self)
                self.layout().addWidget(item)
                self.Cache[bar] = item
            else:
                self.Cache[bar].setText(
                    (bar.label() or "-") + ":" + str(value))
            brush = bar.brush()
            color = brush.color()
            self.Cache[bar].setVisible(color.alphaF() == 1.0)  # 隐藏那些不可用的项
        self.adjustSize()  # 调整大小


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, mode='line', *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        if mode == 'bar':
            self.tipWidget = ToolTipWidgetForBar()

        self.setWidget(self.tipWidget)
        self.hide()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def show(self, title, points, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, points)
        super(GraphicsProxyWidget, self).show()


class MyLineStackchart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyLineStackchart, self).__init__(*args, **kwargs)
        # self.resize(800, 600)
        self.setMinimumSize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # 自定义x轴label
        self.category = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        self.initChart()

        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget('line', self._chart)

        # line
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        pen.setWidth(1)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.min_x, self.max_x = axisX.min(), axisX.max()
        self.min_y, self.max_y = axisY.min(), axisY.max()

    def resizeEvent(self, event):
        super(MyLineStackchart, self).resizeEvent(event)
        # 当窗口大小改变时需要重新计算
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))
        # 坐标原点坐标
        self.point_bottom = self._chart.mapToPosition(
            QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / \
                      (self._chart.axisX().tickCount() - 1)

    def mouseMoveEvent(self, event):
        super(MyLineStackchart, self).mouseMoveEvent(event)
        pos = event.pos()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round((x - self.min_x) / self.step_x)
        # 得到在坐标系中的所有正常显示的series的类型和点
        points = [(serie, serie.at(index))
                  for serie in self._chart.series()
                  if self.min_x <= x <= self.max_x and
                  self.min_y <= y <= self.max_y]
        if points:
            pos_x = self._chart.mapToPosition(
                QPointF(index * self.step_x + self.min_x, self.min_y))
            self.lineItem.setLine(pos_x.x(), self.point_top.y(),
                                  pos_x.x(), self.point_bottom.y())
            self.lineItem.show()
            try:
                title = self.category[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            """
            File "C:\work\hapus\kerja\hapus\notif6.py", line 166, in mouseMoveEvent
                title, points, QPoint(x, y))
            TypeError: arguments did not match any overloaded call:
            QPoint(): too many arguments
            QPoint(int, int): argument 2 has unexpected type 'float'
            QPoint(QPoint): argument 1 has unexpected type 'int'
            """
            self.toolTipWidget.show(
                title, points, QPoint(int(x), int(y)))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        visible = not marker.series().isVisible()
        #         # 隐藏或显示series
        marker.series().setVisible(visible)
        marker.setVisible(True)  # 要保证marker一直显示
        # 透明度
        alpha = 1.0 if visible else 0.4
        # 设置label的透明度
        brush = marker.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker的透明度
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)
        # 设置画笔透明度
        pen = marker.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)

    def handleMarkerHovered(self, status):
        # 设置series的画笔宽度
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        series = marker.series()
        if not series:
            return
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        series.setPen(pen)

    def handleSeriesHoverd(self, point, state):
        # 设置series的画笔宽度
        series = self.sender()  # 信号发送者
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if state else -1))
        series.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="折线图堆叠")
        self._chart.setAcceptHoverEvents(True)
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        dataTable = [
            ["邮件营销", [120, 132, 101, 134, 90, 230, 210]],
            ["联盟广告", [220, 182, 191, 234, 290, 330, 310]],
            ["视频广告", [150, 232, 201, 154, 190, 330, 410]],
            ["直接访问", [320, 332, 301, 334, 390, 330, 320]],
            ["搜索引擎", [820, 932, 901, 934, 1290, 1330, 1320]]
        ]
        for series_name, data_list in dataTable:
            series = QLineSeries(self._chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName(series_name)
            series.setPointsVisible(True)  # 显示圆点
            series.hovered.connect(self.handleSeriesHoverd)  # 鼠标悬停
            self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        axisX = self._chart.axisX()  # x轴
        axisX.setTickCount(7)  # x轴设置7个刻度
        axisX.setGridLineVisible(False)  # 隐藏从x轴往上的线条
        axisY = self._chart.axisY()
        axisY.setTickCount(7)  # y轴设置7个刻度
        axisY.setRange(0, 1500)  # 设置y轴范围
        # 自定义x轴
        axis_x = QCategoryAxis(
            self._chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
        axis_x.setTickCount(7)
        axis_x.setGridLineVisible(False)
        min_x = axisX.min()
        max_x = axisX.max()
        step = (max_x - min_x) / (7 - 1)  # 7个tick
        for i in range(0, 7):
            axis_x.append(self.category[i], min_x + i * step)
        self._chart.setAxisX(axis_x, self._chart.series()[-1])
        # chart的图例
        legend = self._chart.legend()
        # 设置图例由Series来决定样式
        legend.setMarkerShape(QLegend.MarkerShapeFromSeries)
        # 遍历图例上的标记并绑定信号
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.handleMarkerClicked)
            # 鼠标悬停事件
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)


class MyBarStackchart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyBarStackchart, self).__init__(*args, **kwargs)
        # self.resize(800, 600)
        self.setMinimumSize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.initChart()

        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget('bar', self._chart)

        # line 宽度需要调整
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.category_len = len(axisX.categories())
        self.min_x, self.max_x = -0.5, self.category_len - 0.5
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))

    def mouseMoveEvent(self, event):
        super(MyBarStackchart, self).mouseMoveEvent(event)
        pos = event.pos()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round(x)
        # 得到在坐标系中的所有bar的类型和点
        serie = self._chart.series()[0]
        bars = [(bar, bar.at(index))
                for bar in serie.barSets() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        #         print(bars)
        if bars:
            right_top = self._chart.mapToPosition(
                QPointF(self.max_x, self.max_y))
            # 等分距离比例
            step_x = round(
                (right_top.x() - self.point_top.x()) / self.category_len)
            posx = self._chart.mapToPosition(QPointF(x, self.min_y))
            self.lineItem.setLine(posx.x(), self.point_top.y(),
                                  posx.x(), posx.y())
            self.lineItem.show()
            try:
                title = self.categories[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, bars, QPoint(int(x), int(y)))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        # bar透明度
        brush = bar.brush()
        color = brush.color()
        alpha = 0.0 if color.alphaF() == 1.0 else 1.0
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar.setBrush(brush)
        # marker
        brush = marker.labelBrush()
        color = brush.color()
        alpha = 0.4 if color.alphaF() == 1.0 else 1.0
        # 设置label的透明度
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker的透明度
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

    def handleMarkerHovered(self, status):
        # 设置bar的画笔宽度
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def handleBarHoverd(self, status, index):
        # 设置bar的画笔宽度
        bar = self.sender()  # 信号发送者
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="柱状图堆叠")
        self._chart.setAcceptHoverEvents(True)
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        names = ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]
        series = QBarSeries(self._chart)
        for name in names:
            bar = QBarSet(name)
            # 随机数据
            for _ in range(7):
                bar.append(random.randint(0, 10))
            series.append(bar)
            bar.hovered.connect(self.handleBarHoverd)  # 鼠标悬停
        self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        # x轴
        axis_x = QBarCategoryAxis(self._chart)
        axis_x.append(self.categories)
        self._chart.setAxisX(axis_x, series)
        # chart的图例
        legend = self._chart.legend()
        legend.setVisible(True)
        # 遍历图例上的标记并绑定信号
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.handleMarkerClicked)
            # 鼠标悬停事件
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)


class HorizontalPercentBarchart(QChartView):

    def __init__(self, *args, **kwargs):
        super(HorizontalPercentBarchart, self).__init__(*args, **kwargs)
        # self.resize(400, 300)
        self.setMinimumSize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple horizontal percent barchart example')
        # 开启动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 添加Series
        series = self.getSeries()
        chart.addSeries(series)
        # 分类
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # 分类x轴
        axis = QBarCategoryAxis()
        axis.append(categories)
        # 创建默认轴线
        chart.createDefaultAxes()
        # 替换默认y轴
        chart.setAxisY(axis, series)
        # 显示图例
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self):
        # 创建5个柱子
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        set2 = QBarSet('Axel')
        set3 = QBarSet('Mary')
        set4 = QBarSet('Samantha')

        # 添加数据
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        # 创建柱状条
        series = QHorizontalPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series


class MyPercentBarchart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyPercentBarchart, self).__init__(*args, **kwargs)
        # self.resize(400, 300)
        self.setMinimumSize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple percentbarchart example')
        # 开启动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 添加Series
        series = self.getSeries()
        chart.addSeries(series)
        # 分类
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # 分类x轴
        axis = QBarCategoryAxis()
        axis.append(categories)
        # 创建默认轴线
        chart.createDefaultAxes()
        # 替换默认x轴
        chart.setAxisX(axis, series)
        # 显示图例
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self):
        # 创建5个柱子
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        set2 = QBarSet('Axel')
        set3 = QBarSet('Mary')
        set4 = QBarSet('Samantha')

        # 添加数据
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        # 创建柱状条
        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series


class HorizontalBarchart(QChartView):

    def __init__(self, *args, **kwargs):
        super(HorizontalBarchart, self).__init__(*args, **kwargs)
        # self.resize(400, 300)
        self.setMinimumSize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple horizontal barchart example')
        # 开启动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 添加Series
        series = self.getSeries()
        chart.addSeries(series)
        # 分类
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # 分类x轴
        axis = QBarCategoryAxis()
        axis.append(categories)
        # 创建默认轴线
        chart.createDefaultAxes()
        # 替换默认y轴
        chart.setAxisY(axis, series)
        # 显示图例
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self):
        # 创建5个柱子
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        set2 = QBarSet('Axel')
        set3 = QBarSet('Mary')
        set4 = QBarSet('Samantha')

        # 添加数据
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        # 创建柱状条
        series = QHorizontalBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series


from psutil import cpu_percent

class CpuLineChart(QChart):

    def __init__(self, *args, **kwargs):
        super(CpuLineChart, self).__init__(*args, **kwargs)
        self.m_count = 10
        # 隐藏图例
        self.legend().hide()
        self.m_series = QSplineSeries(self)
        # 设置画笔
        self.m_series.setPen(QPen(QColor('#3B8CFF'), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.addSeries(self.m_series)
        # x轴
        self.m_axisX = QDateTimeAxis(self)
        self.m_axisX.setTickCount(self.m_count + 1)  # 设置刻度数量
        self.m_axisX.setFormat('hh:mm:ss')  # 设置时间显示格式
        now = QDateTime.currentDateTime()  # 前10秒到现在
        self.m_axisX.setRange(now.addSecs(-self.m_count), now)
        self.addAxis(self.m_axisX, Qt.AlignBottom)
        self.m_series.attachAxis(self.m_axisX)
        # y轴
        self.m_axisY = QValueAxis(self)
        self.m_axisY.setLabelFormat('%d')  # 设置文本格式
        self.m_axisY.setMinorTickCount(4)  # 设置小刻度线的数目
        self.m_axisY.setTickCount(self.m_count + 1)
        self.m_axisY.setRange(0, 100)
        self.addAxis(self.m_axisY, Qt.AlignLeft)
        self.m_series.attachAxis(self.m_axisY)

        # 填充11个初始点，注意x轴 需要转为秒的时间戳
        self.m_series.append(
            [QPointF(now.addSecs(-i).toMSecsSinceEpoch(), 0) for i in range(self.m_count, -1, -1)])

        # 定时器获取数据
        self.m_timer = QTimer()
        self.m_timer.timeout.connect(self.update_data)
        self.m_timer.start(1000)

    def update_data(self):
        value = cpu_percent()
        now = QDateTime.currentDateTime()
        self.m_axisX.setRange(now.addSecs(-self.m_count), now)  # 重新调整x轴的时间范围
        # 获取原来的所有点,去掉第一个并追加新的一个
        points = self.m_series.pointsVector()
        points.pop(0)
        points.append(QPointF(now.toMSecsSinceEpoch(), value))
        # 替换法速度更快
        self.m_series.replace(points)

class MyCpuChart(QChartView):
    def __init__(self, *args, **kwargs):
        super(MyCpuChart, self).__init__(*args, **kwargs)
        # self.resize(400, 300)
        self.setMinimumSize(400, 500)
        chart = CpuLineChart()
        chart.setTitle('cpu')
        self.setRenderHint(QPainter.Antialiasing)
        self.setChart(chart)

class MyGalore(QWidget):

    def __init__(self, parent=None):
        super(MyGalore, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(400, 1400)

        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color:red;")

        vbox = QVBoxLayout(self)
        self.setLayout(vbox)

        obj1 = MyPercentBarchart()
        obj2 = HorizontalPercentBarchart()
        obj3 = HorizontalBarchart()
        obj4 = MyCpuChart()
        # vbox.addWidget(obj1)
        # vbox.addWidget(obj2)
        # vbox.addWidget(obj3)
        # vbox.addWidget(obj4)

        # https://stackoverflow.com/questions/51220553/pyqt-automatically-resize-widget-in-scroll-area
        intermediate_layout = QtWidgets.QVBoxLayout()
        vbox.addLayout(intermediate_layout)
        vbox.addStretch() 

        intermediate_layout.addWidget(obj1)
        intermediate_layout.addWidget(obj2)
        intermediate_layout.addWidget(obj3)
        intermediate_layout.addWidget(obj4)

        # container = QWidget(self)
        # container.setLayout(vbox)

        # self.scroller = QtWidgets.QScrollArea()
        # self.scroller.setWidgetResizable(True)
        # self.scroller.setWidget(container)

        # ownlayout = QVBoxLayout()
        # ownlayout.addWidget(self.scroller)
        # self.setLayout(ownlayout)

        # QScrollArea

        # self.setGeometry(300, 300, 350, 250)
        # self.setWindowTitle('QWebEngineView')
        # self.show()

class MyThemeWidget(QWidget):

    def __init__(self, parent=None):
        super(MyThemeWidget, self).__init__(parent)
        # super(MyThemeWidget, self).__init__(parent, QtCore.Qt.Window)

        self.m_charts = []
        self.m_listCount = 3
        self.m_valueMax = 10
        self.m_valueCount = 7
        self.m_dataTable = self.generateRandomData(self.m_listCount,
                                                   self.m_valueMax, self.m_valueCount)
        self.m_themeComboBox = self.createThemeBox()
        self.m_antialiasCheckBox = QCheckBox("Anti-aliasing")
        self.m_animatedComboBox = self.createAnimationBox()
        self.m_legendComboBox = self.createLegendBox()

        self.connectSignals()

        # Create the layout.
        baseLayout = QGridLayout()
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)
        settingsLayout.addWidget(self.m_antialiasCheckBox)
        settingsLayout.addStretch()
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        # Create the charts.
        chartView = QChartView(self.createAreaChart())
        baseLayout.addWidget(chartView, 1, 0)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createBarChart(self.m_valueCount))
        baseLayout.addWidget(chartView, 1, 1)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createLineChart())
        baseLayout.addWidget(chartView, 1, 2)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createPieChart())
        # Funny things happen if the pie slice labels no not fit the screen...
        chartView.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        baseLayout.addWidget(chartView, 2, 0)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createSplineChart())
        baseLayout.addWidget(chartView, 2, 1)
        self.m_charts.append(chartView)

        chartView = QChartView(self.createScatterChart())
        baseLayout.addWidget(chartView, 2, 2)
        self.m_charts.append(chartView)

        self.setLayout(baseLayout)

        # Set the defaults.
        self.m_antialiasCheckBox.setChecked(True)
        self.updateUI()

    def connectSignals(self):
        self.m_themeComboBox.currentIndexChanged.connect(self.updateUI)
        self.m_antialiasCheckBox.toggled.connect(self.updateUI)
        self.m_animatedComboBox.currentIndexChanged.connect(self.updateUI)
        self.m_legendComboBox.currentIndexChanged.connect(self.updateUI)

    def generateRandomData(self, listCount, valueMax, valueCount):
        random.seed()

        dataTable = []

        for i in range(listCount):
            dataList = []
            yValue = 0.0
            f_valueCount = float(valueCount)

            for j in range(valueCount):
                yValue += random.uniform(0, valueMax) / f_valueCount
                value = QPointF(
                    j + random.random() * self.m_valueMax / f_valueCount,
                    yValue)
                label = "Slice " + str(i) + ":" + str(j)
                dataList.append((value, label))

            dataTable.append(dataList)

        return dataTable

    def createThemeBox(self):
        themeComboBox = QComboBox()

        themeComboBox.addItem("Light", QChart.ChartThemeLight)
        themeComboBox.addItem("Blue Cerulean", QChart.ChartThemeBlueCerulean)
        themeComboBox.addItem("Dark", QChart.ChartThemeDark)
        themeComboBox.addItem("Brown Sand", QChart.ChartThemeBrownSand)
        themeComboBox.addItem("Blue NCS", QChart.ChartThemeBlueNcs)
        themeComboBox.addItem("High Contrast", QChart.ChartThemeHighContrast)
        themeComboBox.addItem("Blue Icy", QChart.ChartThemeBlueIcy)

        return themeComboBox

    def createAnimationBox(self):
        animationComboBox = QComboBox()

        animationComboBox.addItem("No Animations", QChart.NoAnimation)
        animationComboBox.addItem("GridAxis Animations", QChart.GridAxisAnimations)
        animationComboBox.addItem("Series Animations", QChart.SeriesAnimations)
        animationComboBox.addItem("All Animations", QChart.AllAnimations)

        return animationComboBox

    def createLegendBox(self):
        legendComboBox = QComboBox()

        legendComboBox.addItem("No Legend ", 0)
        legendComboBox.addItem("Legend Top", Qt.AlignTop)
        legendComboBox.addItem("Legend Bottom", Qt.AlignBottom)
        legendComboBox.addItem("Legend Left", Qt.AlignLeft)
        legendComboBox.addItem("Legend Right", Qt.AlignRight)

        return legendComboBox

    def createAreaChart(self):
        chart = QChart()
        chart.setTitle("Area chart")

        # The lower series is initialized to zero values.
        lowerSeries = None
        y_points = []

        for i, data_list in enumerate(self.m_dataTable):
            upperSeries = QLineSeries(chart)
            for j, (value, _) in enumerate(data_list):
                y = value.y()

                if lowerSeries is None:
                    upperSeries.append(QPointF(j, y))
                    y_points.append(y)
                else:
                    new_y = y_points[i] + y
                    upperSeries.append(QPointF(j, new_y))
                    y_points[j] += new_y

            area = QAreaSeries(upperSeries, lowerSeries)
            area.setName("Series " + str(i))
            chart.addSeries(area)
            lowerSeries = upperSeries

        chart.createDefaultAxes()

        return chart

    def createBarChart(self, valueCount):
        chart = QChart()
        chart.setTitle("Bar chart")

        series = QStackedBarSeries(chart)

        for i, data_list in enumerate(self.m_dataTable):
            set = QBarSet("Bar set " + str(i))
            for value, _ in data_list:
                set << value.y()

            series.append(set)

        chart.addSeries(series)
        chart.createDefaultAxes()

        return chart

    def createLineChart(self):
        chart = QChart()
        chart.setTitle("Line chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QLineSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    def createPieChart(self):
        chart = QChart()
        chart.setTitle("Pie chart")

        pieSize = 1.0 / len(self.m_dataTable)

        for i, data_list in enumerate(self.m_dataTable):
            series = QPieSeries(chart)
            for value, label in data_list:
                slice = series.append(label, value.y())
                if series.count() == 1:
                    slice.setLabelVisible()
                    slice.setExploded()

            hPos = (pieSize / 2) + (i / float(len(self.m_dataTable)))
            series.setPieSize(pieSize)
            series.setHorizontalPosition(hPos)
            series.setVerticalPosition(0.5)

            chart.addSeries(series)

        return chart

    def createSplineChart(self):
        chart = QChart()
        chart.setTitle("Spline chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QSplineSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    def createScatterChart(self):
        chart = QChart()
        chart.setTitle("Scatter chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    @pyqtSlot()
    def updateUI(self):
        theme = self.m_themeComboBox.itemData(
            self.m_themeComboBox.currentIndex())

        if self.m_charts[0].chart().theme() != theme:
            for chartView in self.m_charts:
                chartView.chart().setTheme(QChart.ChartTheme(theme))

            pal = self.window().palette()

            if theme == QChart.ChartThemeLight:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeDark:
                pal.setColor(QPalette.Window, QColor(0x121218))
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBlueCerulean:
                pal.setColor(QPalette.Window, QColor(0x40434a))
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBrownSand:
                pal.setColor(QPalette.Window, QColor(0x9e8965))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeBlueNcs:
                pal.setColor(QPalette.Window, QColor(0x018bba))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeHighContrast:
                pal.setColor(QPalette.Window, QColor(0xffab03))
                pal.setColor(QPalette.WindowText, QColor(0x181818))
            elif theme == QChart.ChartThemeBlueIcy:
                pal.setColor(QPalette.Window, QColor(0xcee7f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            else:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))

            self.window().setPalette(pal)

        checked = self.m_antialiasCheckBox.isChecked()
        for chartView in self.m_charts:
            chartView.setRenderHint(QPainter.Antialiasing, checked)

        options = QChart.AnimationOptions(
            self.m_animatedComboBox.itemData(
                self.m_animatedComboBox.currentIndex()))

        if self.m_charts[0].chart().animationOptions() != options:
            for chartView in self.m_charts:
                chartView.chart().setAnimationOptions(options)

        alignment = self.m_legendComboBox.itemData(
            self.m_legendComboBox.currentIndex())

        for chartView in self.m_charts:
            legend = chartView.chart().legend()

            if alignment == 0:
                legend.hide()
            else:
                legend.setAlignment(Qt.Alignment(alignment))
                legend.show()

class MyThemeWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyThemeWindow, self).__init__(parent)
        self.setCentralWidget(MyThemeWidget(self))
        self.resize(900, 600)
        # self.show()
        print('\n\n\n\nAKU DIPANGGIL\n\n\n')

class MessageBox(QMessageBox):

    def __init__(self, *args, count=5, time=1000, auto=False, **kwargs):
        super(MessageBox, self).__init__(*args, **kwargs)
        self._count = count
        self._time = time
        self._auto = auto  # 是否自动关闭
        assert count > 0  # 必须大于0
        assert time >= 500  # 必须>=500毫秒
        self.setStandardButtons(self.Close)  # 关闭按钮
        self.closeBtn = self.button(self.Close)  # 获取关闭按钮
        self.closeBtn.setText('close(%s)' % count)
        self.closeBtn.setEnabled(False)
        self._timer = QTimer(self, timeout=self.doCountDown)
        self._timer.start(self._time)
        print('Whether to close automatically', auto)

    def doCountDown(self):
        self.closeBtn.setText('close(%s)' % self._count)
        self._count -= 1
        if self._count <= 0:
            self.closeBtn.setText('close')
            self.closeBtn.setEnabled(True)
            self._timer.stop()
            if self._auto: # auto close
                self.accept()
                self.close()


class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("i am a form")
        self.setWindowIcon(QIcon("male.png"))
        self.resize(920, 240)
        self.setColumnCount(6)
        self.setRowCount(2)
        # 设置表格有两行五列。
        self.setColumnWidth(0, 200)
        self.setColumnWidth(4, 200)
        self.setRowHeight(0, 100)
        # 设置第一行高度为100px，第一列宽度为200px。

        self.table()

    def table(self):
        self.setItem(0, 0, QTableWidgetItem("your name"))
        self.setItem(0, 1, QTableWidgetItem("gender"))
        self.setItem(0, 2, QTableWidgetItem("date of birth"))
        self.setItem(0, 3, QTableWidgetItem("Profession"))
        self.setItem(0, 4, QTableWidgetItem("income"))
        self.setItem(0, 5, QTableWidgetItem("progress bar"))
        # 添加表格的文字内容.
        self.setHorizontalHeaderLabels(["first column", "second column", "The third column", "fourth column", "The fifth column", "sixth column"])
        self.setVerticalHeaderLabels(["first row", "the second row"])
        # 设置表头
        lbp = QLabel()
        lbp.setPixmap(QPixmap("youPicture.png"))
        self.setCellWidget(1, 1, lbp)
        # 在表中添加一张图片
        twi = QTableWidgetItem("Graph")
        twi.setFont(QFont("Times", 10, ))
        self.setItem(1, 0, twi)

        # 添加一个自己设置了大小和类型的文字。
        dte = QDateTimeEdit()
        dte.setDateTime(QDateTime.currentDateTime())
        dte.setDisplayFormat("yyyy/MM/dd")
        dte.setCalendarPopup(True)
        self.setCellWidget(1, 2, dte)
        # 添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
        cbw = QComboBox()
        cbw.addItem("doctor")
        cbw.addItem("teacher")
        cbw.addItem("lawyer")
        self.setCellWidget(1, 3, cbw)
        # 添加了一个下拉选择框
        sb = QSpinBox()
        sb.setRange(1000, 10000)
        sb.setValue(5000)  # 设置最开始显示的数字
        sb.setDisplayIntegerBase(10)  # 这个是显示数字的进制，默认是十进制。
        sb.setSuffix("Rupiah")  # 设置后辍
        sb.setPrefix("IDR: ")  # 设置前辍
        sb.setSingleStep(100)
        self.setCellWidget(1, 4, sb)
        # 添加一个进度条

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.setCellWidget(1, 5, self.progressBar)
        self.step = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        # 信号连接到槽
        self.timer.timeout.connect(self.onTimerOut)
        self.count = 0

    def onTimerOut(self):  # 重写timerEvent
        self.count += 1
        if self.count >= 100:  # value >= 100时，停止计时器
            self.timer.stop()
            print("Finish")
            # self.progressBar.setValue(self.step)
        else:
            print(self.count)
            self.progressBar.setValue(self.count)
            # return
            # self.step += 1

class DynamicSpline(QChart):
    def __init__(self):
        super().__init__()
        self.m_step = 0
        self.m_x = 5
        self.m_y = 1
        # 初始化图像
        self.series = QSplineSeries(self)
        green_pen = QPen(Qt.red)
        green_pen.setWidth(3)
        self.series.setPen(green_pen)
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()
        self.series.append(self.m_x, self.m_y)

        self.addSeries(self.series)
        self.addAxis(self.axisX, Qt.AlignBottom)
        self.addAxis(self.axisY, Qt.AlignLeft)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
        self.axisX.setTickCount(5)
        self.axisX.setRange(0, 10)
        self.axisY.setRange(-5, 10)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handleTimeout)
        self.timer.start()

    def handleTimeout(self):
        x = self.plotArea().width() / self.axisX.tickCount()
        y = (self.axisX.max() - self.axisX.min()) / self.axisX.tickCount()
        self.m_x += y
        # 在PyQt5.11.3及以上版本中，QRandomGenerator.global()被重命名为global_()
        self.m_y = QRandomGenerator.global_().bounded(5) - 2.5
        self.series.append(self.m_x, self.m_y)
        self.scroll(x, 0)
        if self.m_x >= 100:
            self.timer.stop()

class MyDynamicSplineChart(QChartView):
    def __init__(self, *args, **kwargs):
        super(MyDynamicSplineChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        self.setRenderHint(QPainter.Antialiasing)

        chart = DynamicSpline()
        chart.setTitle("Dynamic spline chart")
        chart.legend().hide()
        chart.setAnimationOptions(QChart.AllAnimations)
        self.setChart(chart)

class MySplineChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MySplineChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple splinechart example')
        # 添加Series
        self.getSeries(chart)
        # 创建默认xy轴
        chart.createDefaultAxes()
        chart.legend().setVisible(False)

    def getSeries(self, chart):
        # 第一组
        series = QSplineSeries(chart)
        series << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) \
        << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        chart.addSeries(series)

        # 第二组
        series = QSplineSeries(chart)
        series << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) \
        << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)
        chart.addSeries(series)

class MyScatterChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyScatterChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)
        # 生成模拟数据
        self.m_dataTable = self.generateRandomData(3, 10, 7)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Scatter chart')
        # 添加Series
        self.getSeries(chart)
        # 创建默认xy轴
        chart.createDefaultAxes()
        chart.legend().setVisible(False)

    def getSeries(self, chart):
        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName('Series ' + str(i))
            chart.addSeries(series)

    def generateRandomData(self, listCount, valueMax, valueCount):
        # 生成模拟随机数据
        random.seed()

        dataTable = []

        for i in range(listCount):
            dataList = []
            yValue = 0.0
            f_valueCount = float(valueCount)

            for j in range(valueCount):
                yValue += random.uniform(0, valueMax) / f_valueCount
                value = QPointF(j + random.random() * valueMax / f_valueCount, yValue)
                label = 'Slice ' + str(i) + ':' + str(j)
                dataList.append((value, label))

            dataTable.append(dataList)

        return dataTable

class MyPieChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyPieChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple piechart example')
        # 添加Series
        chart.addSeries(self.getSeries())

    def getSeries(self):
        series = QPieSeries()
        slice0 = series.append('10%', 1)
        series.append('20%', 2)
        series.append('70%', 7)
        # 显示label文字
        series.setLabelsVisible()
        series.setPieSize(0.5)
        # 使第一块突出显示
        slice0.setLabelVisible()
        slice0.setExploded()
        # 设置第一块颜色
        slice0.setColor(QColor(255, 0, 0, 100))
        return series

class MyLineChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyLineChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # Antialiasing
        self.setRenderHint(QPainter.Antialiasing)

        # chart
        chart = QChart()
        self.setChart(chart)
        # set title
        chart.setTitle('Simple linechart example')
        # Turn on animation effects
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # Add to/increase Series
        series = self.getSeries(chart)
        chart.addSeries(series)
        # Classification
        # categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # Category x-axis
        # axis = QBarCategoryAxis()
        # axis.append(categories)
        # Create default grid
        chart.createDefaultAxes()
        # replace the default x-axis
        # chart.setAxisX(axis, series)
        # show legend
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self, chart):
        series = QLineSeries(chart)
        series.append(0, 6)
        series.append(1, 32)
        series.append(2, 4)
        series.append(3, 18)
        series.append(4, 10)
        return series

class MyAreaChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyAreaChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple areachart example')
        # 添加Series
        chart.addSeries(self.getSeries())
        # 创建默认轴线
        chart.createDefaultAxes()
        # 设置xy轴的范围
        chart.axisX().setRange(0, 20)
        chart.axisY().setRange(0, 10)

    def getSeries(self):
        # 创建Series
        series0 = QLineSeries(self)
        series1 = QLineSeries(self)

        # 添加数据
        series0 << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) \
        << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        series1 << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) \
        << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)

        # 创建区域图
        series = QAreaSeries(series0, series1)
        series.setName('Batman')

        # 画笔
        pen = QPen(0x059605)
        pen.setWidth(3)
        series.setPen(pen)

        # 设置画刷
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, QColor(0x3cc63c))
        gradient.setColorAt(1.0, QColor(0x26f626))
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        series.setBrush(gradient)

        return series

class MyBarChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyBarChart, self).__init__(*args, **kwargs)
        # self.resize(400, 300)
        self.setMinimumSize(400, 300)
        # Antialiasing
        self.setRenderHint(QPainter.Antialiasing)

        # chart
        chart = QChart()
        self.setChart(chart)
        # set title
        chart.setTitle('Simple barchart example')
        # Turn on animation effects
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # Add to/increase Series
        series = self.getSeries()
        chart.addSeries(series)
        # Classification
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # Category x-axis
        axis = QBarCategoryAxis()
        axis.append(categories)
        # Create default grid
        chart.createDefaultAxes()
        # replace the default x-axis
        chart.setAxisX(axis, series)
        # show legend
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self):
        # Create 5 pillars
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        set2 = QBarSet('Axel')
        set3 = QBarSet('Mary')
        set4 = QBarSet('Samantha')

        # adding data
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        # Create column bars
        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series

mystylesheet = """
QWidget#widgetTitle {
    background-color: rgb(76, 169, 106);
}
QWidget#widgetBottom {
    border-top-style: solid;
    border-top-width: 2px;
    border-top-color: rgb(185, 218, 201);
}
QLabel#labelTitle {
    color: rgb(255, 255, 255);
}
QLabel#labelContent {
    padding: 5px;
}
QPushButton {
    border: none;
    background: transparent;
}
QPushButton#buttonClose {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}
QPushButton#buttonClose:hover {
    background-color: rgb(212, 64, 39);
}
QPushButton#otherbutton {
    color: rgb(255, 255, 255);
    border-radius: 5px;
    border: solid 1px rgb(76, 169, 106);
    background-color: rgb(169, 76, 106);
}
QPushButton#imagebutton {
    color: rgb(255, 255, 255);
    border-radius: 5px;
    border: solid 1px rgb(76, 169, 106);
    background-color: rgb(106, 169, 76);
}
QPushButton#buttonView {
    color: rgb(255, 255, 255);
    border-radius: 5px;
    border: solid 1px rgb(76, 169, 106);
    background-color: rgb(76, 169, 106);
}
QPushButton#buttonView:hover {
    color: rgb(0, 0, 0);
}
"""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
</head>
<body>
    <p>
        This is a simple HTML page.
    </p>
</body>
</html>
"""
# pip install pyqtwebengine
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class MyWebview(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.loadPage()

        self.toolBar = QToolBar()

        self.backBtn = QPushButton(self)
        self.backBtn.setEnabled(False)
        self.backBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/left-32.png'))
        self.backBtn.clicked.connect(self.back)
        self.toolBar.addWidget(self.backBtn)

        self.forBtn = QPushButton(self)
        self.forBtn.setEnabled(False)
        self.forBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forBtn.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forBtn)

        self.address = QLineEdit(self)
        self.address.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.address)

        vbox.addWidget(self.toolBar, 10)
        vbox.addWidget(self.webEngineView, 90)

        self.webEngineView.page().urlChanged.connect(self.onLoadFinished)
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QWebEngineView')
        self.show()

    def loadPage(self):

        self.webEngineView.setHtml(html_content)

    def load(self):

        url = QUrl.fromUserInput(self.address.text())

        if url.isValid():
            self.webEngineView.load(url)


    def onLoadFinished(self):

        if self.webEngineView.history().canGoBack():
            self.backBtn.setEnabled(True)
        else:
            self.backBtn.setEnabled(False)

        if self.webEngineView.history().canGoForward():
            self.forBtn.setEnabled(True)
        else:
            self.forBtn.setEnabled(False)

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def urlChanged(self, url):
        self.address.setText(url.toString())

class Ui_NotifyForm(object):

    def button_clicked(self):
        # lambda: MessageBox(self, text='Countdown to close dialog', auto=random.randrange(0, 2)).exec_()
        # self.doShake()
        MessageBox(self, text='Countdown to close dialog', auto=random.randrange(0, 2)).exec_()

    def setupUi(self, NotifyForm):

        NotifyForm.setObjectName("NotifyForm")
        # NotifyForm.resize(300, 600)
        NotifyForm.resize(500, 900)
        NotifyForm.setStyleSheet(mystylesheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(NotifyForm) # ini jadi layout of choice dong ya...setara NotifyForm.setLayout(self.verticalLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widgetTitle = QtWidgets.QWidget(NotifyForm)
        self.widgetTitle.setMinimumSize(QtCore.QSize(0, 26))
        self.widgetTitle.setObjectName("widgetTitle")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetTitle)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.labelTitle = QtWidgets.QLabel(self.widgetTitle)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")

        self.horizontalLayout_3.addWidget(self.labelTitle)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.buttonClose = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonClose.setMinimumSize(QtCore.QSize(26, 26))
        self.buttonClose.setMaximumSize(QtCore.QSize(26, 26))
        self.buttonClose.setObjectName("buttonClose")

        self.horizontalLayout_3.addWidget(self.buttonClose)

        self.verticalLayout.addWidget(self.widgetTitle)

        self.labelContent = QtWidgets.QLabel(NotifyForm)
        self.labelContent.setText("")
        self.labelContent.setWordWrap(True)
        self.labelContent.setObjectName("labelContent")

        # self.grid = QGridLayout()
        # total = 25

        # for i in range(total):
        #     self.grid.addWidget(QPushButton(f"Baris {i}"), i, 1)
        # self.grid.addWidget(self.labelContent, total, 1)

        # # self.verticalLayout.addWidget(self.labelContent)
        # self.win = QWidget()
        # self.win.setLayout(self.grid)

        # https://stackoverflow.com/questions/41616864/pyqt-expand-grid-in-scroll-area
        # buat scrollarea, setwidget ke container widget, buat control widget dg parent = container widget
        # container widget hanya QWidget biasa, spt dummy widget saja
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

        for i in range(100):
            if i==50:
                chart = MyBarChart()
                self.gridLayout.addWidget(chart, i, 1, 1+4, 100) # span row 5 
            else:
                for j in range(100):
                    btn = QtWidgets.QPushButton(f"{i},{j}")
                    btn.setStyleSheet("background-color:cyan;")
                    btn.clicked.connect(self.button_clicked)
                    self.gridLayout.addWidget(btn, i+4 if i>50 else i, j)
        
        self.gridLayout.addWidget(self.labelContent, 100, 1, -1, 100)


        # verticallayout addwidget = tab, tab berisi 2: 1 scrollarea, 2 barchart, dst...

        self.tabWidget = QtWidgets.QTabWidget(NotifyForm)
        self.tabWidget.setObjectName("tabWidget")

        self.tabWidget.addTab(self.scrollArea, "Maintab")

        # MyThemeWidget

        self.tab0 = MyTable()
        self.tab0.setObjectName("table")
        self.tabWidget.addTab(self.tab0, "Tabel")

        self.tableview = MyTableView()
        self.tableview.setObjectName("tableview")
        self.tabWidget.addTab(self.tableview, "tableview")

        # self.imageslider = ImageSliderWidget()
        # self.imageslider.setObjectName("imageslider")
        # self.tabWidget.addTab(self.imageslider, "imageslider")


        self.tab = MyLineChart() # QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "Line chart")

        self.tab_galore = MyGalore()
        # self.tab_galore.setObjectName("tab_galore")
        # self.tabWidget.addTab(self.tab_galore, "Various chart")


        # https://stackoverflow.com/questions/51220553/pyqt-automatically-resize-widget-in-scroll-area
        # harusnya: dari scoll area, ke scroll content widget ke scroll content layout
        # tapi jangan langsung masukkan item ke scroll content layout
        # tapi via intermediate layout dulu
        self.scrollArea2 = QtWidgets.QScrollArea(self)
        self.scrollArea2.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        # self.scrollArea2.setWidget(self.tab_galore)
        self.scrollArea2.setWidget(container_widget)
        self.tabWidget.addTab(self.scrollArea2, "Galorechart")
        container_layout.addWidget(MyCpuChart())
        container_layout.addWidget(HorizontalBarchart())
        container_layout.addWidget(MyPercentBarchart())
        # container_layout.addWidget(MyPercentBarchart())
        container_layout.addWidget(MyLineStackchart())
        container_layout.addWidget(MyBarStackchart())
        container_layout.addWidget(MyCustomxyAxis())

        from settings import SettingsWindow
        self.settingswindow = SettingsWindow()
        self.settingswindow.setObjectName("settingswindow")
        self.tabWidget.addTab(self.settingswindow, "settingswindow")

        from parsejson import JsonTreeWidget
        self.parsejson = JsonTreeWidget()
        self.parsejson.setObjectName("parsejson")
        self.tabWidget.addTab(self.parsejson, "parsejson")

        from leftstack import LeftTabWidget
        self.leftstack = LeftTabWidget()
        self.leftstack.setObjectName("leftstack")
        self.tabWidget.addTab(self.leftstack, "leftstack")

        self.tab_2 = MyAreaChart() # QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Areachart")

        self.tab_3 = MyBarChart()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "Barchart")

        self.tab4 = MyPieChart()
        self.tab4.setObjectName("tab4")
        self.tabWidget.addTab(self.tab4, "Pie chart")

        self.tab5 = MyScatterChart()
        self.tab5.setObjectName("tab5")
        self.tabWidget.addTab(self.tab5, "Scatter chart")

        self.tab6 = MySplineChart()
        self.tab6.setObjectName("tab6")
        self.tabWidget.addTab(self.tab6, "Spline chart")

        self.tab7 = MyDynamicSplineChart()
        self.tab7.setObjectName("tab7")
        self.tabWidget.addTab(self.tab7, "Dynamic Spline")

        self.tab8 = MyWebview()
        self.tab8.setObjectName("tab8")
        self.tabWidget.addTab(self.tab8, "Webview")


        # terlalu luas utk notif window
        # self.tab1 = MyThemeWidget()
        # self.tab1.setObjectName("themechart")
        # self.tabWidget.addTab(self.tab1, "Themed Chart")


        self.tabWidget.setCurrentIndex(0)
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "折线图"))

        self.verticalLayout.addWidget(self.tabWidget)
        # self.verticalLayout.addWidget(self.scrollArea)
        # self.verticalLayout.addWidget(self.win)

        self.widgetBottom = QtWidgets.QWidget(NotifyForm)
        self.widgetBottom.setObjectName("widgetBottom")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)


        self.sliderbutton = QtWidgets.QPushButton('Slider', self.widgetBottom)
        self.sliderbutton.setMinimumSize(QtCore.QSize(60, 25))
        self.sliderbutton.setObjectName("sliderbutton")

        self.imagebutton = QtWidgets.QPushButton('Image', self.widgetBottom)
        self.imagebutton.setMinimumSize(QtCore.QSize(60, 25))
        self.imagebutton.setObjectName("imagebutton")

        self.otherbutton = QtWidgets.QPushButton('Theme', self.widgetBottom)
        self.otherbutton.setMinimumSize(QtCore.QSize(60, 25))
        # self.otherbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.otherbutton.setObjectName("otherbutton")

        self.buttonView = QtWidgets.QPushButton(self.widgetBottom)
        self.buttonView.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonView.setObjectName("buttonView")

        self.horizontalLayout.addWidget(self.sliderbutton)
        self.horizontalLayout.addWidget(self.imagebutton)
        self.horizontalLayout.addWidget(self.otherbutton)
        self.horizontalLayout.addWidget(self.buttonView)

        self.verticalLayout.addWidget(self.widgetBottom)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(NotifyForm)
        QtCore.QMetaObject.connectSlotsByName(NotifyForm)

    def retranslateUi(self, NotifyForm):
        _translate = QtCore.QCoreApplication.translate
        NotifyForm.setWindowTitle(_translate("NotifyForm", "notification"))
        self.buttonClose.setText(_translate("NotifyForm", "r"))
        self.buttonView.setText(_translate("NotifyForm", "Go"))


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     NotifyForm = QtWidgets.QWidget()
#     ui = Ui_NotifyForm()
#     ui.setupUi(NotifyForm)
#     NotifyForm.show()
#     sys.exit(app.exec_())

class WindowNotify(QWidget, Ui_NotifyForm):

    SignalClosed = pyqtSignal()  # Popup close signal


    def doShake(self):
        self.doShakeWindow(self)

    # 下面这个方法可以做成这样的封装给任何控件
    def doShakeWindow(self, target):
        """窗口抖动动画
        :param target:        目标控件
        """
        if hasattr(target, '_shake_animation'):
            # 如果已经有该对象则跳过
            return

        animation = QPropertyAnimation(target, b'pos', target)
        target._shake_animation = animation
        animation.finished.connect(lambda: delattr(target, '_shake_animation'))

        pos = target.pos()
        x, y = pos.x(), pos.y()

        animation.setDuration(200)
        animation.setLoopCount(2)
        animation.setKeyValueAt(0, QPoint(x, y))
        animation.setKeyValueAt(0.09, QPoint(x + 2, y - 2))
        animation.setKeyValueAt(0.18, QPoint(x + 4, y - 4))
        animation.setKeyValueAt(0.27, QPoint(x + 2, y - 6))
        animation.setKeyValueAt(0.36, QPoint(x + 0, y - 8))
        animation.setKeyValueAt(0.45, QPoint(x - 2, y - 10))
        animation.setKeyValueAt(0.54, QPoint(x - 4, y - 8))
        animation.setKeyValueAt(0.63, QPoint(x - 6, y - 6))
        animation.setKeyValueAt(0.72, QPoint(x - 8, y - 4))
        animation.setKeyValueAt(0.81, QPoint(x - 6, y - 2))
        animation.setKeyValueAt(0.90, QPoint(x - 4, y - 0))
        animation.setKeyValueAt(0.99, QPoint(x - 2, y + 2))
        animation.setEndValue(QPoint(x, y))

        animation.start(animation.DeleteWhenStopped)


    def __init__(self, title="", content="", timeout=5000, *args, **kwargs):
        super(WindowNotify, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTitle(title).setContent(content)
        self._timeout = timeout
        self._init()

    def setTitle(self, title):
        if title:
            self.labelTitle.setText(title)
        return self

    def title(self):
        return self.labelTitle.text()

    def setContent(self, content):
        if content:
            self.labelContent.setText(content)
        return self

    def content(self):
        return self.labelContent.text()

    def setTimeout(self, timeout):
        if isinstance(timeout, int):
            self._timeout = timeout
        return self

    def timeout(self):
        return self._timeout

    def onView(self):
        print("onView")
        webbrowser.open_new_tab("https://google.com")

    def onClose(self):
        # When the close button is clicked
        print("onClose")
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)  # Start the bounce animation


    def new_window(self):
        if self.w is None:
            self.w = MyThemeWindow()
        self.w.show()

    def image_view_window(self):
        if self.w2 is None:
            self.w2 = ImageView()
        self.w2.show()

    def image_slider_window(self):
        if self.w3 is None:
            self.w3 = ImageSliderWidget()
        self.w3.show()

    def _init(self):
        # Hide Taskbar|Remove Borders|Show Top
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # close button event
        self.buttonClose.clicked.connect(self.onClose)
        self.w = None
        self.w2 = None
        self.w3 = None
        # ternyata jangan di dalam lambda karena dia jd transient!!
        # self.otherbutton.clicked.connect(lambda: MyThemeWindow().show())
        self.otherbutton.clicked.connect(self.new_window)
        # self.otherbutton.clicked.connect(lambda: MyThemeWidget(self).show())
        self.imagebutton.clicked.connect(self.image_view_window)
        self.sliderbutton.clicked.connect(self.image_slider_window)
        self.buttonView.clicked.connect(self.onView)
        # whether the logo is being displayed
        self.isShow = True
        # time out
        self._timeouted = False
        # desktop
        self._desktop = QApplication.instance().desktop()
        # window initial start position
        self._startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.screenGeometry().height()
        )
        # window popup end position
        self._endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.availableGeometry().height() - self.height() - 5
        )
        # Initialize the position to the lower right corner
        self.move(self._startPos)

        # animation
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(1000)  # 1s

        # Bounce timer
        self._timer = QTimer(self, timeout=self.closeAnimation)

    def show(self, title="", content="", timeout=5000):
        self._timer.stop()  # Stop the timer to prevent problems with the previous timer when the second popup pops up
        self.hide()  # hide first
        self.move(self._startPos)  # Initialize the position to the lower right corner
        super(WindowNotify, self).show()
        self.setTitle(title).setContent(content).setTimeout(timeout)
        return self

    def showAnimation(self):
        print("showAnimation isShow = True")
        # show animation
        self.isShow = True
        self.animation.stop()  # Stop the previous animation and start again
        self.animation.setStartValue(self.pos())

        # https://www.pythonguis.com/tutorials/qpropertyanimation/
        # https://doc.qt.io/qt-5/qeasingcurve.html
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        self.animation.setEndValue(self._endPos)
        self.animation.start()
        # After 5 seconds of popping, if there is no focus, it will pop back
        self._timer.start(self._timeout)

        # QTimer.singleShot(self._timeout, self.closeAnimation)

    def closeAnimation(self):
        print("closeAnimation hasFocus", self.hasFocus())
        # turn off animation
        if self.hasFocus():
            # If there is still focus after the countdown for 5 seconds after the pop-up, you need to actively trigger the shutdown after losing the focus.
            self._timeouted = True
            return  # Do not close if it has focus
        self.isShow = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    def onAnimationEnd(self):
        # animation ends
        # print("onAnimationEnd isShow", self.isShow)
        if not self.isShow:
            # print("onAnimationEnd close()")
            self.close()
            # print("onAnimationEnd stop timer")
            self._timer.stop()
            # print("onAnimationEnd close and emit signal")
            self.SignalClosed.emit()

    def enterEvent(self, event):
        super(WindowNotify, self).enterEvent(event)
        # Set the focus (it seems useless, but after a mouse click, this method is useful)
        # print("enterEvent setFocus Qt.MouseFocusReason")
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # remove focus
        # print("leaveEvent clearFocus")
        self.clearFocus()
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = QWidget()
    notify = WindowNotify(parent=window)

    layout = QHBoxLayout(window)

    b1 = QPushButton("Open 1", window, clicked=lambda: notify.show(timeout=10000,content='Wieke cinta: ' + b1.text()).showAnimation())
    b2 = QPushButton("Open 2", window, clicked=lambda: notify.show(content='Yang disuka gaia adlh: ' + b2.text()).showAnimation())

    layout.addWidget(b1)
    layout.addWidget(b2)

    window.show()

    sys.exit(app.exec_())
