
import re, requests, sys, webbrowser
from bs4 import BeautifulSoup
import bs4

from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QDesktopWidget, QSystemTrayIcon
from PyQt5.QtCore import QEasingCurve, QRect, QAbstractAnimation, QSize
from PyQt5 import QtCore, QtGui, QtWidgets

# from notrol import NotifyControl
if __name__ == '__main__':
    from noticontrol import NotifyControl
else:
    from .noticontrol import NotifyControl

default_parser = 'html.parser'


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

    def __init__(self, title="", data=[], timeout=5000, close_after_timeout=True, *args, **kwargs):

        super(WindowNotify, self).__init__(*args, **kwargs)

        # self.setWindowOpacity(0.5) # di sini gak jalan, baru jalan stlh setWindowFlags

        screen_geometry = QDesktopWidget().screenGeometry(-1)
        sw, sh = screen_geometry.width(), screen_geometry.height()
        self.reset_size = QSize(int(sw*0.1), int(sh*0.2))
        self.resize(self.reset_size)

        self.data = data
        self.setupUi(self)

        self.setTitle(title) # .setContent(content)
        self._timeout = timeout
        self.close_after_timeout = close_after_timeout
        self.dx = 1000
        self.dy = 500

        self._init()


    def setTitle(self, title):
        if title:
            self.labelTitle.setText(title)
        return self

    def title(self):
        return self.labelTitle.text()

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
        # print("onClose")
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)  # Start the bounce animation

    def onReset(self):
        # print('onReset called...')
        # self.resize(self.reset_size)
        self.second_animation.setDirection(QAbstractAnimation.Backward)
        self.second_animation.start()
        self.isBig = False

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    # def systemtrayicon(self):
    #     self.hide()
    #     self.tray_icon.showMessage(
    #         "Tray Program",
    #         "Application was minimized to Tray",
    #         QSystemTrayIcon.Information,
    #         2000
    #     )

    def _init(self):
        # Hide Taskbar|Remove Borders|Show Top
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.75)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.buttonClose.clicked.connect(self.onClose)
        self.buttonReset.clicked.connect(self.onReset)
        self.buttonView.clicked.connect(self.onView)

        self.isShow = True
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
        # print(f"""
        # endpos dg geometry
        # self._desktop.screenGeometry().width() - self.width() - 5
        # {self._desktop.screenGeometry().width()} - {self.width()} - 5
        # self._desktop.availableGeometry().height() - self.height() - 5
        # {self._desktop.availableGeometry().height()} - {self.height()} - 5
        # awal dg endpos = {self._endPos}
        # initial = {self.small_rect}
        # final = {self.big_rect}
        # {self.small_rect.getCoords()}
        # {self.small_rect.getRect()}
        # """)
        self.isBig = False

    def show(self, title="", timeout=5000):
        self._timer.stop() # Stop the timer to prevent problems with the previous timer when the second popup pops up
        self.hide() # hide first
        self.move(self._startPos)  # Initialize the position to the lower right corner
        super(WindowNotify, self).show()
        self.setTitle(title) # .setContent(content)
        self.setTimeout(timeout)
        return self

    def showAnimation(self):
        # print("showAnimation isShow = True")
        # show animation
        self.isShow = True
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
        pass
        # print(f'timeout closeAnimation after {self._timeout}')

    def closeAnimation(self):
        # print("closeAnimation hasFocus", self.hasFocus())
        # turn off animation
        if self.hasFocus():
            # If there is still focus after the countdown for 5 seconds after the pop-up, you need to actively trigger the shutdown after losing the focus.
            self._timeouted = True
            return # Do not close if it has focus
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
        # p = self.pos()
        # x, y = p.x(), p.y()
        # self.move(QPoint(x-self.dx, y-self.dy))
        # self.resize(self.width() + self.dx, self.height() + self.dy)

        # self.second_animation.stop()
        # self.second_animation.setStartValue(self.big_pos)
        # self.animation.setEasingCurve(QEasingCurve.InOutBack)
        # self.second_animation.setEndValue(self.small_pos)
        # self.second_animation.start()

        # animasi jadi big hanya jk tidak buttonstate=checked dan tidak sudah big/resize
        if not self.isBig and not self.buttonState.isChecked():
            self.second_animation.setStartValue(self.small_rect)
            self.second_animation.setEndValue(self.big_rect)
            self.second_animation.setDirection(QAbstractAnimation.Forward)
            self.second_animation.start()
            self.isBig = True

        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # remove focus
        # print("leaveEvent clearFocus")
        self.clearFocus()

        # stlh press x, jangan aktifkan animasi...
        # agar gak rebutan animasi oleh 2 anim
        # if self.isShow:
        #     self.second_animation.setDirection(QAbstractAnimation.Backward)
        #     self.second_animation.start()
        
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)

prefix = 'https://stackoverflow.com'

def get_data(so_url):
    # so_url = 'https://stackoverflow.com/questions?tab=newest&pagesize=50'
    # # https://stackoverflow.com/questions?tab=newest&page=5
    # if page and page.isdigit():
    #     so_url += f'&page={page}'
    isi = requests.get(so_url).content
    soup = BeautifulSoup(isi, default_parser)
    doctype, html = [item for item in list(soup.children) if type(item) is not bs4.element.NavigableString]
    head, body = [item for item in list(html.children) if type(item) is not bs4.element.NavigableString]

    # question_links = body.findAll('a', class_='s-link')
    # question_links = [item for item in question_links if item.attrs['href'].startswith('/questions/')]
    # satu = [item.text for item in question_links]
    # dua = [prefix+item.attrs['href'] for item in question_links]
    # return [{'title': a, 'url': b} for (a,b) in zip(satu,dua)]

    results = []
    blocks = body.findAll('div', class_='s-post-summary')
    for block in blocks:
        stat_links = block.findAll('div', class_='s-post-summary--stats')[0]
        question_links = block.findAll('div', class_='s-post-summary--content')[0]
        stat = stat_links.findAll('div', class_='s-post-summary--stats-item')[1]
        stat = stat.find('span')
        answers = stat.text
        q_link = question_links.find('a')
        text = q_link.text
        url = prefix+q_link.attrs['href']
        d_sum = question_links.findAll('div', class_='s-post-summary--content-excerpt')[0]
        summary = d_sum.text.strip()
        tags = question_links.findAll('div', class_='s-post-summary--meta-tags')[0]
        tags_ref = tags.findAll('a')
        tags = ', '.join([a.text for a in tags_ref])

        item = {
            'title': text,
            'url': url,
            'summary': summary,
            'answers': answers,
            'tags': tags,
        }
        results.append(item)
    return results

def main(code=''):
    """    
    """
    app = QApplication(sys.argv)
    window = QWidget()
    window.hide()
    # window.setWindowOpacity(0.8)

    # so_url = 'https://stackoverflow.com/questions__TAG__?tab=newest&pagesize=50__PAGE__'
    # tag_tpl = '/tagged/python'
    # page_tpl = '&page=5'
    # m = re.match(r'([A-Za-z]+)?\s*(\d+)?', code).groups()
    # # (None, '9')
    # # ('rust ', '9')
    # # ('rust', None)
    # if m[0] or m[1]:
    #     if m[0]:
    #         so_url = so_url.replace('__TAG__', '/tagged/'+m[0])
    #     else:
    #         so_url = so_url.replace('__TAG__', '')
    #     if m[1]:
    #         so_url = so_url.replace('__PAGE__', '&page='+m[1])
    #     else:
    #         so_url = so_url.replace('__PAGE__', '')
    
    # https://stackoverflow.com/questions?tab=newest&page=5
    # https://stackoverflow.com/questions/tagged/python?tab=newest&pagesize=50
    # https://stackoverflow.com/questions/tagged/python?tab=newest&page=4&pagesize=50
    # https://stackoverflow.com/questions/tagged/python?tab=newest&pagesize=50&page=5
    # if page and page.isdigit():
    #     so_url += f'&page={page}'
    # data = [{'content': 'ini isi pertama'},{'content': 'ini isi kedua'},{'content': 'ini isi ketiga'}]
    # data = get_data(so_url)
    data = 'dummy'

    notify = WindowNotify(title='clock', data=data, parent=window, close_after_timeout=False)
    # title jangan terlalu panjang, nanti widget kepotong...
    notify.show(title='Clock').showAnimation()

    # main window sembunyikan...    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

