import sys
import webbrowser
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QDesktopWidget
from PyQt5.QtCore import QEasingCurve, QRect, QAbstractAnimation
from PyQt5 import QtCore, QtGui, QtWidgets

from notrol import NotifyControl


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


class WindowNotify(QWidget, NotifyControl):

    SignalClosed = pyqtSignal()

    def __init__(self, title="", content="", timeout=5000, close_after_timeout=True, *args, **kwargs):
        super(WindowNotify, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTitle(title).setContent(content)
        self._timeout = timeout
        self.close_after_timeout = close_after_timeout
        self.dx = 200
        self.dy = 100
        self.is_closing = False
        self.data = [{'content': 'ini isi pertama'},{'content': 'ini isi kedua'},{'content': 'ini isi ketiga'}]
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
        self.is_closing = True
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
        print('is_closing is now true #1')
        self.is_closing = True
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
        self.animation.setDuration(1000) # 1s
        # Bounce timer, stlh timeout, maka animasi selesai
        if self.close_after_timeout:
            self._timer = QTimer(self, timeout=self.closeAnimation)
        else:
            self._timer = QTimer(self, timeout=self.timeout_notification)
        
        self.second_animation = QPropertyAnimation(self, b"geometry")
        self.second_animation.setEasingCurve(QEasingCurve.InOutSine)
        self.second_animation.setDuration(250)
        # b'geometry'
        # https://stackoverflow.com/questions/66988388/resize-widget-from-center-when-animating-the-size-property
        # b'size'
        # https://stackoverflow.com/questions/66988388/resize-widget-from-center-when-animating-the-size-property
        # self.small_pos = self._endPos # start
        # self.big_pos = QPoint(self._endPos.x()-self.dx, self._endPos.y()-self.dy) # end

        x,y=self._endPos.x(), self._endPos.y()
        w,h = self.width(), self.height()
        self.small_rect = QRect(x,y,w,h)
        # x,y,w,h = self.small_rect.getRect()
        self.big_rect = QRect(x-self.dx, y-self.dy, w+self.dx, h+self.dy)
        print(f"""
        initial = {self.small_rect}
        final = {self.big_rect}
        {self.small_rect.getCoords()}
        {self.small_rect.getRect()}
        """)

    def show(self, title="", content="", timeout=5000):
        self._timer.stop() # Stop the timer to prevent problems with the previous timer when the second popup pops up
        self.hide() # hide first
        self.move(self._startPos)  # Initialize the position to the lower right corner
        super(WindowNotify, self).show()
        self.setTitle(title).setContent(content).setTimeout(timeout)
        return self

    def showAnimation(self):
        print('is_closing is now true #2')
        # show animation
        self.is_closing = True
        self.animation.stop() # Stop the previous animation and start again
        self.animation.setStartValue(self.pos())
        # https://www.pythonguis.com/tutorials/qpropertyanimation/
        # https://doc.qt.io/qt-5/qeasingcurve.html
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.setEndValue(self._endPos)
        self.animation.start()

        # After 5 seconds of popping, if there is no focus, it will pop back
        self._timer.start(self._timeout)
        # QTimer.singleShot(self._timeout, self.closeAnimation)

    def timeout_notification(self):
        print(f'timeout closeAnimation after {self._timeout}')

    def closeAnimation(self):
        print("closeAnimation hasFocus", self.hasFocus())
        # turn off animation
        if self.hasFocus():
            # If there is still focus after the countdown for 5 seconds after the pop-up, you need to actively trigger the shutdown after losing the focus.
            self._timeouted = True
            return # Do not close if it has focus
        # print('is_closing is now false #1')
        # self.is_closing = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    def onAnimationEnd(self):
        # animation ends
        print("onAnimationEnd is_closing", self.is_closing)
        if not self.is_closing:
            # print("onAnimationEnd close()")
            self.close()
            # print("onAnimationEnd stop timer")
            self._timer.stop()
            # print("onAnimationEnd close and emit signal")
            self.SignalClosed.emit()

    def enterEvent(self, event):
        super(WindowNotify, self).enterEvent(event)
        # Set the focus (it seems useless, but after a mouse click, this method is useful)
        print(f"enterEvent, is_closing={self.is_closing}")
        # p = self.pos()
        # x, y = p.x(), p.y()
        # self.move(QPoint(x-self.dx, y-self.dy))
        # self.resize(self.width() + self.dx, self.height() + self.dy)

        # self.second_animation.stop()
        # self.second_animation.setStartValue(self.big_pos)
        # self.animation.setEasingCurve(QEasingCurve.InOutBack)
        # self.second_animation.setEndValue(self.small_pos)
        # self.second_animation.start()
        if not self.is_closing:
            self.second_animation.setStartValue(self.small_rect)
            self.second_animation.setEndValue(self.big_rect)
            self.second_animation.setDirection(QAbstractAnimation.Forward)
            self.second_animation.start()

            self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # remove focus
        # print("leaveEvent clearFocus")
        self.clearFocus()

        # p = self.pos()
        # x, y = p.x(), p.y()
        # self.move(QPoint(x+self.dx, y+self.dy))
        # self.resize(self.width() - self.dx, self.height() - self.dy)

        # self.second_animation.start()
        # self.second_animation.setStartValue(self.small_pos)
        # self.animation.setEasingCurve(QEasingCurve.OutInBack)
        # self.second_animation.setEndValue(self.big_pos)
        # self.second_animation.start()
        self.second_animation.setDirection(QAbstractAnimation.Backward)
        self.second_animation.start()
        
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)

    # def hoverEnterEvent(self, event):
    #     print('enter')
    
    # def hoverLeaveEvent(self, event):
    #     print('leave')


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.hide()
    notify = WindowNotify(parent=window, close_after_timeout=False)

    # screen_geometry = QDesktopWidget().screenGeometry(-1)
    # screenw, screenh = screen_geometry.width(), screen_geometry.height()
    # resize_screen_ratio(notify, screenw, screenh, posx_ratio=0.1, ratio=0.8)
    # notify.resize(300,600)

    notify.show(content='Aku adalah notifikasi untukmu...').showAnimation()
    # main window sembunyikan...    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
