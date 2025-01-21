from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

notification_bottom_stylesheet = """
QMenu {
    /* Translucent effect */
    background-color: rgba(255, 255, 255, 230);
    border: none;
    border-radius: 4px;
}

QMenu::item {
    border-radius: 4px;
    /* This distance is cumbersome and needs to be fine-tuned based on factors such as menu length and icons */
    padding: 8px 48px 8px 36px; /* 36px is the distance from the text to the left*/
    background-color: transparent;
}

/* Mouseover and press effects */
QMenu::item:selected {
    border-radius: 0px;
    /* Translucent effect */
    background-color: rgba(232, 232, 232, 232);
}

/* disable effect */
QMenu::item:disabled {
    background-color: transparent;
}

/* icon distance to the left */
QMenu::icon {
    left: 15px;
}

/* split line effect */
QMenu::separator {
    height: 1px;
    background-color: rgb(232, 236, 243);
}

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

QPushButton#buttonState {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}

QPushButton#buttonState:hover {
    background-color: rgb(64, 239, 212);
}

QPushButton#buttonState:checked {
    background-color: orange;
    border-style: outset;
}

QPushButton#buttonReset {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}

QPushButton#buttonReset:hover {
    background-color: rgb(64, 39, 212);
}

QPushButton#buttonClose {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}

QPushButton#buttonClose:hover {
    background-color: rgb(212, 64, 39);
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

# print(__name__)
# if __name__ in ['__main__']:
#     from clockwidget import ClockWidget
# else:
#     from app.quick.languages.guilang_helper.clockwidget import ClockWidget

class NotificationBottom(QWidget):

    SignalClosed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(NotificationBottom, self).__init__(*args, **kwargs)
        # self.setTitle(title)
        # self._timeout = timeout

        screen_geometry = QDesktopWidget().screenGeometry(-1)
        sw, sh = screen_geometry.width(), screen_geometry.height()
        self.reset_size = QSize(int(sw*__LEBAR__), int(sh*0.2))
        self.resize(self.reset_size) # skrg sudah punya width() dan height(), hanya posisi gak keliatan

        self.screenw, self.screenh = sw, sh

        self._desktop = QApplication.instance().desktop()
        sw2 = self._desktop.screenGeometry().width()
        sh2 = self._desktop.screenGeometry().height()
        # posisi gak keliatan di kanan bawah
        self._startPos = QPoint(
            sw2 - self.width() - 5,
            sh2
        )        
        # posisi muncul di kanan bawah
        self._endPos = QPoint(
            sw2 - self.width() - 5,
            sh2 - self.height() - 5
        )

        self.setStyleSheet(notification_bottom_stylesheet)
        ######################## START setupUi
        self.layout_main = QVBoxLayout(self)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(6)
        self.layout_main.setObjectName("layout_main")

        self.widgetTitle = QWidget(self)
        self.widgetTitle.setMinimumSize(QSize(0, 26))
        self.widgetTitle.setObjectName("widgetTitle")

        self.layout_titlebar = QHBoxLayout(self.widgetTitle)
        self.layout_titlebar.setContentsMargins(10, 0, 0, 0)
        self.layout_titlebar.setSpacing(0)
        self.layout_titlebar.setObjectName("layout_titlebar")

        self.labelTitle = QLabel(self.widgetTitle)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")

        self.layout_titlebar.addWidget(self.labelTitle)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_titlebar.addItem(spacerItem)

        self.buttonClose = QPushButton(self.widgetTitle)
        self.buttonClose.setMinimumSize(QSize(26, 26))
        self.buttonClose.setMaximumSize(QSize(26, 26))
        self.buttonClose.setObjectName("buttonClose")

        self.layout_titlebar.addWidget(self.buttonClose)

        self.layout_main.addWidget(self.widgetTitle)

        # ini adlh bagian content utama
        # self.labelContent = QLabel(self)
        # self.labelContent.setText("Replace me with some widget here")
        # self.labelContent.setWordWrap(True)
        # self.labelContent.setObjectName("labelContent")
__TEMPLATE_CONTENT__
        # self.labelContent = ClockWidget()
        # self.layout_main.addWidget(self.labelContent)

        self.layout_main.addStretch(1)
        self.layout_main.setStretch(1, 1)
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("NotificationBottom", "notification"))
        self.buttonClose.setText(_translate("NotificationBottom", "r"))
        # QMetaObject.connectSlotsByName(self)
        ######################## END setupUi

        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.75)

        self.buttonClose.clicked.connect(self.onClose)

        # awal posisi gak keliatan, agar animasi sblm fixed
        self.move(self._startPos)

        # self.animation = QPropertyAnimation(self, b"pos")
        # self.animation.finished.connect(self.onAnimationEnd)
        # self.animation.setDuration(500)

        # self.close_after_timeout = False # fixed
        # if self.close_after_timeout:
        #     self._timer = QTimer(self, timeout=self.closeAnimation)
        # else:
        #     self._timer = QTimer(self, timeout=self.timeout_notification)

        self.second_animation = QPropertyAnimation(self, b"geometry")
        self.second_animation.setEasingCurve(QEasingCurve.InOutSine)
        self.second_animation.setDuration(1000)

        # x,y=self._endPos.x(), self._endPos.y()
        x,y=self._startPos.x(), self._startPos.y()
        w,h = self.width(), self.height()
        self.small_rect = QRect(x,y,w,h)
        self.dx = 0 # posisi x tidak berubah
        self.dy = int(self.screenh * __TINGGI__)
        self.big_rect = QRect(x-self.dx, y-self.dy, w+self.dx, h+self.dy)
        # self.isBig = False # belum animate, sampai dipanggil eksplisit

    def timeout_notification(self):
        pass

    def onClose(self):
        # self.isShow = False
        # self.isBig = False
        QTimer.singleShot(100, self.closeAnimation)

    def animate(self):
        self.show()
        # self.isShow = True
        # self.isBig = True
        self.second_animation.stop()
        # self.second_animation.setStartValue(self.pos())
        self.second_animation.setStartValue(self.small_rect)
        # https://www.pythonguis.com/tutorials/qpropertyanimation/
        # https://doc.qt.io/qt-5/qeasingcurve.html
        self.second_animation.setEasingCurve(QEasingCurve.OutBounce)
        # self.second_animation.setEndValue(self._endPos)
        self.second_animation.setEndValue(self.big_rect)
        self.second_animation.setDirection(QAbstractAnimation.Forward)
        self.second_animation.start()
        # self._timer.start(self._timeout)

    def animate_reset(self):
        self.second_animation.stop()
        # self.second_animation.setStartValue(self.big_rect)
        # self.second_animation.setEndValue(self.small_rect)
        # self.second_animation.setEasingCurve(QEasingCurve.OutBounce)
        self.second_animation.setDirection(QAbstractAnimation.Backward)
        self.second_animation.start()
        # self.isBig = False

    def closeAnimation(self):
        if self.hasFocus():
            # self._timeouted = True # indicator utk leaveEvent
            return
        self.animate_reset()
        # agar tdk abrupt, keluar dg timer
        QTimer.singleShot(1000, lambda: qApp.quit())

# if __name__ == "__main__":
#     import sys
#     app = QApplication([])
#     # window = QWidget()
#     # window.hide()
#     # NotificationBottom(parent=window, title='kuda').animate()
#     NotificationBottom().animate()
#     sys.exit(app.exec_())
