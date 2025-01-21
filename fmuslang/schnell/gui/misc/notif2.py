
import webbrowser
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QGridLayout
from PyQt5.QtCore import QEasingCurve
from PyQt5 import QtCore, QtGui, QtWidgets


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

class Ui_NotifyForm(object):

    def setupUi(self, NotifyForm):

        NotifyForm.setObjectName("NotifyForm")
        NotifyForm.resize(300, 600)
        NotifyForm.setStyleSheet(mystylesheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(NotifyForm)
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

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
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

        self.grid = QGridLayout()

        total = 25

        # for i in range(total):
        #     self.grid.addWidget(QPushButton(f"Baris {i}"), i, 1)
        # self.grid.addWidget(self.labelContent, total, 1)

        # # self.verticalLayout.addWidget(self.labelContent)
        # self.win = QWidget()
        # self.win.setLayout(self.grid)

        # https://stackoverflow.com/questions/41616864/pyqt-expand-grid-in-scroll-area
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

        for i in range(100):
            for j in range(100):
                self.gridLayout.addWidget(QtWidgets.QPushButton(f"{i},{j}"), i, j)
        
        self.gridLayout.addWidget(self.labelContent, 100, 1, -1, 100)

        self.verticalLayout.addWidget(self.scrollArea)
        # self.verticalLayout.addWidget(self.win)

        self.widgetBottom = QtWidgets.QWidget(NotifyForm)
        self.widgetBottom.setObjectName("widgetBottom")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.buttonView = QtWidgets.QPushButton(self.widgetBottom)
        self.buttonView.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonView.setObjectName("buttonView")

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

    def _init(self):
        # Hide Taskbar|Remove Borders|Show Top
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # close button event
        self.buttonClose.clicked.connect(self.onClose)
        # Click the View button
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
        print("onAnimationEnd isShow", self.isShow)
        if not self.isShow:
            print("onAnimationEnd close()")
            self.close()
            print("onAnimationEnd stop timer")
            self._timer.stop()
            print("onAnimationEnd close and emit signal")
            self.SignalClosed.emit()

    def enterEvent(self, event):
        super(WindowNotify, self).enterEvent(event)
        # Set the focus (it seems useless, but after a mouse click, this method is useful)
        print("enterEvent setFocus Qt.MouseFocusReason")
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # remove focus
        print("leaveEvent clearFocus")
        self.clearFocus()
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = QWidget()
    notify = WindowNotify(parent=window)

    layout = QHBoxLayout(window)

    b1 = QPushButton("Open 1", window, clicked=lambda: notify.show(content='Wieke cinta: ' + b1.text()).showAnimation())
    b2 = QPushButton("Open 2", window, clicked=lambda: notify.show(content='Yang disuka gaia adlh: ' + b2.text()).showAnimation())

    layout.addWidget(b1)
    layout.addWidget(b2)

    window.show()

    sys.exit(app.exec_())
