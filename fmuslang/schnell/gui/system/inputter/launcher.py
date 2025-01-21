import os, re, sys


import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import (
    QsciScintilla,
	QsciLexerCustom,
	QsciLexerJSON,
	QsciLexerPython,
)

from client import Client
from worker import Worker
from job_run import Run
from make_go import Go
from make_redis import RedisWorker

MAX_ITEM = 7
MAX_LIST_LENGTH = 20
MAX_VISIBLE_ITEMS = 12

""" ada go dan ada run, kita oprek run yg bermain dg file, bukan hwnd """


icon_provider = QFileIconProvider()


def _file_icon(path):
    return icon_provider.icon(QFileInfo(path))


def parse_query(text):
    """
    cmd, arg = parse_query(text)
    """
    if not text.startswith('\\'):
        return None, text
    m = re.search(r'\\(\S*)( (.*)){0,1}', text)
    return m.group(1), m.group(2)[1:] if not m.group(2) is None else None


class Bar(QScrollBar):

    def setRange(self, min, max):
        print(max)
        super(Bar, self).setRange(min, max)


class CenterListView(QListView):
    """Always scroll to center."""

    def __init__(self, parent=None):
        super(CenterListView, self).__init__(parent)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.setRootIsDecorated(False)
        #self.setHeaderHidden(True)
        #self.setVerticalScrollBar(Bar())

    def scrollTo(self, index, _):
        """Always scroll to center."""
        super(CenterListView, self).scrollTo(index, QAbstractItemView.PositionAtCenter)

    #def resizeEvent(self, e):
        #QTimer.singleShot(0, self._adjust_popup_height)
        ##self.setAttribute(Qt.WA_WState_ExplicitShowHide, True)
        ##st = self.testAttribute(Qt.WA_WState_Hidden)
        ##self.setAttribute(Qt.WA_WState_Hidden, False)
        ##self._adjust_popup_height()
        ##self.setAttribute(Qt.WA_WState_Hidden, st)
        #super(CenterListView, self).resizeEvent(e)

    #def _adjust_popup_height(self):
        ##self.ensurePolished()
        ##self.updateGeometries()
        #if self.model().rowCount(QModelIndex()) <= MAX_ITEM:
            #vsb = self.verticalScrollBar()
            ##if vsb and vsb.isVisible():
            #if vsb:
                ##print(self.height())
                ##print("m: {}".format(self.maximumViewportSize().height()))
                ##print("v: {}".format(self.viewport().height()))
                #if vsb.maximum() > 0:
                    #self.resize(self.width(), self.height() + 1)
                    #QTimer.singleShot(0, self._adjust_popup_height)
                #elif vsb.maximum() < 0:
                    #self.resize(self.width(), self.height() - 1)
                    #QTimer.singleShot(0, self._adjust_popup_height)
                ##self._adjust_popup_height()


class Suggest(QWidget):

    activated = pyqtSignal(QModelIndex)

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self.editor = parent
        self.popup = None
        self.set_popup(CenterListView())
        self.content = None

    def set_popup(self, popup):
        if self.popup:
            self.popup.removeEventFilter(self)

        self.popup = popup
        popup.setWindowFlags(Qt.Popup)
        popup.setFocusPolicy(Qt.NoFocus)
        #popup.setFocusProxy(self.editor)
        popup.setMouseTracking(True)

        popup.installEventFilter(self)

        popup.clicked.connect(self.activated)
        self.activated.connect(popup.hide)

    def completionModel(self):
        return self.model

    def done(self, index):
        if index.isValid():
            self.activated.emit(index)

    def eventFilter(self, o, e):
        #if e.type() == QEvent.MouseButtonPress:
            ##self.popup.hide()
            #self.editor.setFocus()
            #return True

        if o == self.popup:
            if not self.popup.underMouse() and e.type() in (
                QEvent.MouseButtonPress,
                #QEvent.MouseButtonRelease,
                #QEvent.MouseButtonDblClick,
                #QEvent.MouseMove
            ):
                self.popup.hide()
                #self.editor.setFocus()
                #QApplication.sendEvent(self.editor, e)
                return False
            elif e.type() == QEvent.KeyPress:
                key = e.key()
                if e.key() == Qt.Key_Tab or e.key() == Qt.Key_J and e.modifiers() & Qt.ControlModifier:
                    ne = QKeyEvent(
                        QEvent.KeyPress,
                        Qt.Key_Down,
                        e.modifiers(),
                        ''
                    )
                    QApplication.sendEvent(o, ne)
                    return True
                elif e.key() == Qt.Key_Tab or e.key() == Qt.Key_K and e.modifiers() & Qt.ControlModifier:
                    ne = QKeyEvent(
                        QEvent.KeyPress,
                        Qt.Key_Up,
                        e.modifiers(),
                        e.text(),
                        e.isAutoRepeat(),
                        e.count()
                    )
                    QApplication.sendEvent(o, ne)
                    return True
                elif e.key() == Qt.Key_Up and self.attop:
                    ne = QKeyEvent(
                        QEvent.KeyPress,
                        Qt.Key_End,
                        Qt.ControlModifier
                    )
                    QApplication.sendEvent(o, ne)
                    return True
                elif e.key() == Qt.Key_Down and self.atbottom:
                    ne = QKeyEvent(
                        QEvent.KeyPress,
                        Qt.Key_Home,
                        Qt.ControlModifier
                    )
                    QApplication.sendEvent(o, ne)
                    return True
                elif key in (Qt.Key_Enter, Qt.Key_Return):
                    self.done(self.popup.currentIndex())
                    return True
                #elif key in (Qt.Key_Escape, ):
                    #self.editor.setFocus()
                    #self.popup.hide()
                    #return True
                #elif key in (
                    #Qt.Key_Home,
                    #Qt.Key_End,
                #):
                    #QApplication.sendEvent(self.editor, e)
                    #return True
                #elif key in (
                        #Qt.Key_Up,
                        #Qt.Key_Down,
                        #Qt.Key_Home,
                        #Qt.Key_End,
                        #Qt.Key_PageUp,
                        #Qt.Key_PageDown
                        #):
                    #pass
                else:
                    #self.editor.setFocus()
                    #self.editor.event(e)
                    #TODO: why HOME and END not processed by editor?
                    QApplication.sendEvent(self.editor, e)
                    #self.popup.hide()

        return self.super.eventFilter(o, e)

    @property
    def atbottom(self):
        p = self.popup
        return p.currentIndex().row() + 1 == p.model().rowCount(QModelIndex())

    @property
    def attop(self):
        return self.popup.currentIndex().row() == 0

    @property
    def popuped(self):
        return self.popup.isVisible()

    @property
    def super(self):
        return super(QWidget, self)

    @property
    def model(self):
        return self.popup.model() if self.popup else None

    @model.setter
    def model(self, value):
        self.popup.setModel(value)

    def hide_popup(self):
        self.popup.hide()

    def reset(self):
        """Reset model and hide popup."""
        self.model = QStringListModel()
        self.hide_popup()

    def select_first_item(self):
        first_index = self.popup.model().index(0, 0)
        self.popup.selectionModel().setCurrentIndex(
            first_index,
            QItemSelectionModel.Select | QItemSelectionModel.Rows
        )
        self.popup.scrollTo(first_index, QAbstractItemView.PositionAtCenter)

    def _resize_popup(self):
        h = sum([
            self.popup.sizeHintForRow(0) * min(MAX_ITEM, self.row_count),
            self.popup.contentsMargins().top(),
            self.popup.contentsMargins().bottom()
        ])
        self.popup.resize(self.editor.width(), h)
        #self.popup._adjust_popup_height()
        #hsb = self.popup.horizontalScrollBar()
        #if hsb and hsb.isVisible():
            #h += hsb.sizeHint().height()
        self.popup.move(self.editor.mapToGlobal(QPoint(0, self.editor.height())))

    @property
    def row_count(self):
        return self.model.rowCount(QModelIndex())

    @property
    def empty(self):
        return self.row_count == 0

    def complete(self, content):
        if content is None:
            # logging.debug('Content should not be None...')
            content = []

        # cache content
        self.content = content

        # make model
        if isinstance(content, QAbstractItemModel):
            model = content
        else:
            model = QStringListModel()
            model.setStringList([str(c) for c in content])

        self.model = model

        if self.empty:
            # no suggestion, hide
            self.hide_popup()
        else:
            #self.popup.setFocus()
            self._resize_popup()
            self.select_first_item()
            self.popup.show()
            #self._continues_update()

    def _update_popup(self):
        model = self.model
        self.model = None
        self.model = model

    def _continues_update(self):
        if self.popuped:
            self._update_popup()
            QTimer.singleShot(1000, self._continues_update)



class Input(QLineEdit):

    def __init__(self, enter=lambda: None, parent=None):
        super(Input, self).__init__(parent)
        self.enter = enter

    @property
    def super(self):
        return super(Input, self)

    def keyPressEvent(self, e):
        #{
            #Qt.Key_Escape: lambda: self.setText(''),
            #Qt.Key_Return: self.enter
        #}.get(e.key(), lambda: None)()
        #super(Input, self).keyPressEvent(e)

        if e.key() == Qt.Key_Escape:
            if self.text():
                self.setText('')
                e.accept()
            else:
                e.ignore()
        elif e.key() == Qt.Key_Return:
            self.enter()
        else:
            super(Input, self).keyPressEvent(e)

    #def setCompleter(self, completer):
        #completer.setWidget(self)


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, h_ratio=0, delta = 60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    if h_ratio<=0:
        h_ratio = ratio
    lebar, tinggi = int(screenw*ratio),int(screenh*h_ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)


class TheWIndow(QDialog):

    def _teardown_plugins(self):
        for p in self.plugins.values():
            if hasattr(p, 'teardown'):
                p.teardown()

    def _setup_plugins(self):
        for p in self.plugins.values():
            if hasattr(p, 'setup'):
                p.setup()

    def act(self):
        if self.cmd == 'exit':
            self._teardown_plugins()
            self.client.stop()
            QApplication.quit()
        if self.cmd in self.plugins:
            self.plugins[self.cmd].act()

    def _install_plugins(self, plugins):
        self.plugins = {p.name: p for p in plugins}
        self.default_plugin = plugins[0] if self.plugins else None
        self._setup_plugins()

    def _try_query(self, text):
        """Avoid line editor frozen when key continues pressed."""
        QTimer.singleShot(0, lambda: self.query(text))

    def hide_window(self):
        #self.inp.setText('')
        #self.completer.popup().hide()
        #self.setWindowState(self.windowState() | Qt.WindowMinimized)
        # print('[launcher][hide_window] hiding windows')
        self.hide()

    def select(self, index):
        cmd = self.cmd
        #text = self.completer.completionModel().data(index, Qt.DisplayRole)

        # self.hide_window() # ternyata ini sebabnya hide...susah mau diakses setelah itu
        assert self.completer.content
        if cmd in self.plugins:
            self.plugins[cmd].select(content=self.completer.content, index=index)

    def _reset_popup(self):
        self.completer.reset()

    def _try_popup(self, content):
        # don't show popup if search box is hidden
        # print(f"_try_popup v=[{self.isVisible()}] dg content.data [{content}]")
        if self.isVisible():
            QTimer.singleShot(0, lambda: self.popup(content))

    def popup(self, content):
        with QMutexLocker(self.mutex):
            self.completer.complete(content)

    def query(self, text):
        cmd, arg = parse_query(text)
        # print(f'query, cmd = {cmd}, arg = {arg}, self.plugins: {self.plugins}')
        self.cmd = self.default_plugin.name if ((cmd is None) and (self.default_plugin)) else cmd
        if arg is None:
            self._reset_popup()
        else:
            plugin = None
            if cmd is None:
                if not self.default_plugin is None:
                    plugin = self.default_plugin
            else:
                if cmd in self.plugins:
                    plugin = self.plugins[cmd]
            if plugin:
                plugin.worker.clear()
                plugin.lit(
                    arg,
                    upper_bound=MAX_LIST_LENGTH,
                    finished=self._try_popup
                )

    def __init__(self, *args, **kwargs):
        super(TheWIndow, self).__init__(*args, **kwargs)
        self.init()

    def init(self):

        lay = QVBoxLayout()
        # spacing of search box
        lay.setSpacing(0)
        # lay.setMargin(0)
        self.inp = Input(self.act, self)
        self.inp.textChanged.connect(self._try_query)
        self.completer = Suggest(self.inp)
        #self.inp.setCompleter(self.completer)
        self.completer.activated[QModelIndex].connect(self.select)
        lay.addWidget(self.inp)
        self.setLayout(lay)
        # plugins = []
        worker = Worker()
        client = Client()
        QMetaObject.invokeMethod(
            client,
            'start',
            Qt.QueuedConnection
        )
        plugins = [
            Go(worker=worker, client=client),
            Run(worker=worker, client=client),
            RedisWorker(worker)
        ]
        self._install_plugins(plugins)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup | Qt.WindowStaysOnTopHint)
        self.setWindowTitle('launcher')
        self.mutex = QMutex()
        self.jobs = []


def main():
    app = QApplication(sys.argv)
    # app.setStyleSheet(app_stylesheet)
    w = TheWIndow()
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=1/2, h_ratio=1/8)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


"""
**Task switching** using `\g` command or query directly (default mode is `\g`):
**Launcher** using `\r` command:

Use `;;` to toggle search box (I'm a vimer, and accustomed to `jj`). 
Search text are make of two parts: command and query (optional, 
some command may haven't query part, like `\exit`), seperated by a space.

Command can be:

* `\r` (i.e. `\run`): run executable under your `PATH`
* `\g` (i.e. `\go`): task switch
* `\exit`: as it says

Default mode is `\g`, you can do task switch just without command part.

Use:

* arrow keys or `CTRL+J`/`CTRL+K` to navigate;
* `ESC` to clear search box (when popup shown) or hide it.

"""

"""
IDE:
bisa search repl, dia juga terima global hotkey yg bisa focus/aktifkan.
abis itu muncul editor yg tuliskan hasilnya
"""
