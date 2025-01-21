from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

stylesheet_notification_kanan_bawah = """
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

class Ui_NotificationKananBawah(object):

    def setupUi(self, NotifyForm):
        NotifyForm.setObjectName("NotifyForm")
        NotifyForm.resize(300, 600)
        NotifyForm.setStyleSheet(stylesheet_notification_kanan_bawah)

        self.layout_main = QVBoxLayout(NotifyForm)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(6)
        self.layout_main.setObjectName("layout_main")

        self.widgetTitle = QWidget(NotifyForm)
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

        self.labelContent = QLabel(NotifyForm)
        self.labelContent.setText("")
        self.labelContent.setWordWrap(True)
        self.labelContent.setObjectName("labelContent")

        self.layout_main.addWidget(self.labelContent)


        # hapus bottom
        # self.widgetBottom = QWidget(NotifyForm)
        # self.widgetBottom.setObjectName("widgetBottom")
        # self.horizontalLayout = QHBoxLayout(self.widgetBottom)
        # self.horizontalLayout.setContentsMargins(0, 5, 5, 5)
        # self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # spacerItem1 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem1)
        # self.buttonView = QPushButton(self.widgetBottom)
        # self.buttonView.setMinimumSize(QSize(75, 25))
        # self.buttonView.setCursor(QCursor(Qt.PointingHandCursor))
        # self.buttonView.setObjectName("buttonView")
        # self.horizontalLayout.addWidget(self.buttonView)
        # self.layout_main.addWidget(self.widgetBottom)

        self.layout_main.setStretch(1, 1)

        # self.retranslateUi(NotifyForm)
        _translate = QCoreApplication.translate
        NotifyForm.setWindowTitle(_translate("NotifyForm", "notification"))
        self.buttonClose.setText(_translate("NotifyForm", "r"))
        # self.buttonView.setText(_translate("NotifyForm", "Go"))
    
        QMetaObject.connectSlotsByName(NotifyForm)




class NotificationKananBawah(QWidget, Ui_NotificationKananBawah):


    SignalClosed = pyqtSignal()

    def __init__(self, title="", content="", timeout=5000, close_after_timeout=True, *args, **kwargs):
        super(NotificationKananBawah, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTitle(title).setContent(content)
        self._timeout = timeout
        self.close_after_timeout = close_after_timeout
        self._init()

    def _init(self):
        # Hide Taskbar|Remove Borders|Show Top
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.buttonClose.clicked.connect(self.onClose)
        # self.buttonView.clicked.connect(self.onView)
        self.isShow = True
        self._timeouted = False
        self._desktop = QApplication.instance().desktop()
        self._startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.screenGeometry().height()
        )
        self._endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.availableGeometry().height() - self.height() - 5
        )
        self.move(self._startPos)
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(1000)
        if self.close_after_timeout:
            self._timer = QTimer(self, timeout=self.closeAnimation)
        else:
            self._timer = QTimer(self, timeout=self.timeout_notification)

    def content(self):
        return self.labelContent.text()

    def timeout(self):
        return self._timeout

    def title(self):
        return self.labelTitle.text()

    def setContent(self, content):
        if content:
            self.labelContent.setText(content)
        return self

    def setTimeout(self, timeout):
        if isinstance(timeout, int):
            self._timeout = timeout
        return self

    def setTitle(self, title):
        if title:
            self.labelTitle.setText(title)
        return self

    def onAnimationEnd(self):
        if not self.isShow:
            self.close()
            self._timer.stop()
            self.SignalClosed.emit()

    def onClose(self):
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)

    def enterEvent(self, event):
        super(NotificationKananBawah, self).enterEvent(event)
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(NotificationKananBawah, self).leaveEvent(event)
        self.clearFocus()
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)

    def show(self, title="", content="", timeout=5000):
        self._timer.stop()
        self.hide()
        self.move(self._startPos)
        super(NotificationKananBawah, self).show()
        self.setTitle(title).setContent(content).setTimeout(timeout)
        return self

    def showAnimation(self):
        self.isShow = True
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        # https://www.pythonguis.com/tutorials/qpropertyanimation/
        # https://doc.qt.io/qt-5/qeasingcurve.html
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.setEndValue(self._endPos)
        self.animation.start()
        self._timer.start(self._timeout)

    def timeout_notification(self):
        pass

    def closeAnimation(self):
        if self.hasFocus():
            self._timeouted = True
            return
        self.isShow = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()




# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)

#     # # window = QWidget()
#     # # notify = NotificationKananBawah(parent=window, close_after_timeout=True)
#     # notify = NotificationKananBawah(close_after_timeout=True)
#     # notify.show(content='Aku adalah notifikasi untukmu...').showAnimation()
#     # # main window sembunyikan...
#     # # window.hide()

#     NotificationKananBawah().show(content='Aku adalah notifikasi untukmu...').showAnimation()

#     sys.exit(app.exec_())

