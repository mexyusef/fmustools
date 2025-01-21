import os, re, sys
import win32api

from functools import partial

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
# from PyQt5.Qsci import (
#     QsciScintilla,
# 	QsciLexerCustom,
# 	QsciLexerJSON,
# 	QsciLexerPython,
# )

import heapq
import itertools

from utils import Query
import windows

PORT = 50007

MAX_ITEM = 7
MAX_LIST_LENGTH = 20
MAX_VISIBLE_ITEMS = 12

""" ada go dan ada run, kita oprek run yg bermain dg file, bukan hwnd """


icon_provider = QFileIconProvider()


def _file_icon(path):
    return icon_provider.icon(QFileInfo(path))


class Runnable(QObject):

    icon_loaded = pyqtSignal()

    def __init__(self, name, path, query, worker, order):
        super(Runnable, self).__init__()
        self.name = name
        self.path = path
        self.query = query
        self.worker = worker
        self.order = order
        self._icon = None

    @property
    def icon(self):
        if self._icon is None:
            #QThreadPool.globalInstance().start(AsyncJob(self._fill_icon))
            #QTimer.singleShot(0, self._fill_icon)
            #self._icon = windows.get_file_icon(self.path)
            self.worker.do(
                action=self._fill_icon,
                react=self._fill_icon_finished,
                main=True,
                priority=-42
            )
            return self._default_icon()
        else:
            return self._icon

    def _default_icon(self):
        return QIcon(':/unknown.png')

    def _fill_icon_finished(self):
        self.icon_loaded.emit()

    def _fill_icon(self):
        self._icon = windows.get_file_icon(self.path)
        if self._icon is None:
            self._icon = self._default_icon()


class UpdateIcon(QObject):

    def __init__(self, model, index):
        super(UpdateIcon, self).__init__(model)
        self.index = index

    @pyqtSlot()
    def fire(self):
        self.parent().dataChanged.emit(self.index, self.index)


class RunnableModel(QAbstractListModel):

    NAME_ROLE = Qt.DisplayRole
    ICON_ROLE = Qt.DecorationRole

    def __init__(self, items):
        super(RunnableModel, self).__init__()
        self.items = items
        for i, item in enumerate(self.items):
            # must use Qt.DirectConnection here, but why?
            update = UpdateIcon(self, self.index(i, 0))
            update.setParent(self)
            item.icon_loaded.connect(update.fire)
            self.destroyed.connect(partial(item.icon_loaded.disconnect, update.fire))

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return None
        if role == Qt.TextAlignmentRole:
            return int(Qt.AlignLeft | Qt.AlignVCenter)
        elif role == Qt.DisplayRole:
            return self.items[index.row()].name
        elif role == Qt.DecorationRole:
            return self.items[index.row()].icon
        else:
            return None


class Job(QObject):

    mutex = QMutex()

    def __init__(self, p, query, upper_bound, finished):
        super(Job, self).__init__()
        self.p = p
        self.query = query
        self.upper_bound = upper_bound
        self.finished = finished
        self.canceled = False

    @pyqtSlot(object)
    def _make_model(self, args):
        if not self.canceled:
            with QMutexLocker(self.mutex):
                self.finished(RunnableModel(args))
        self.deleteLater()

    def cancel(self):
        self.canceled = True

    def run(self):
        """Use mutex to protect self.d."""
        with QMutexLocker(self.p.mutex):
            for runnable in self.p.d.values():
                runnable.query.update(self.query.lower())

            def f(runnable):
                """Don't calculate editing distance if job stopped."""
                if self.canceled:
                    return 0
                elif not self.query:
                    return runnable.order
                else:
                    return runnable.query.distance_to(runnable.name.lower())

            QMetaObject.invokeMethod(
                self,
                '_make_model',
                Qt.QueuedConnection,
                Q_ARG(object, sorted(self.p.d.values(), key=f)[:self.upper_bound])
            )


class Files(object):

    def __init__(self, worker, **kargs):
        super(Files, self).__init__()
        self.d = dict()
        self.mutex = QMutex()
        self.worker = worker

    def path_list_changed(self):
        """Update runnable list."""
        with QMutexLocker(self.mutex):
            runnables = []
            for order, path in enumerate(self.paths):
                name, _ = os.path.splitext(os.path.basename(path))
                if name in self.d:
                    runnables.append((name, Runnable(
                        name=name,
                        path=path,
                        query=self.d[name].query,
                        worker=self.worker,
                        order=order
                    )))
                else:
                    runnables.append((name, Runnable(
                        name=name,
                        path=path,
                        query=Query(
                            text='',
                            insertion_cost=1,
                            first_insertion_cost=50,
                            prepend_first_insertion_cost=5,
                            append_first_insertion_cost=10,
                            deletion_cost=100,
                            substitution_cost=100,
                            transposition_cost=10
                        ),
                        worker=self.worker,
                        order=order
                    )))
            self.d = dict(runnables)

    @property
    def paths(self):
        assert False, 'Not implemented.'

    def select(self, content, index):
        # check content type
        if not isinstance(content, RunnableModel):
            print('wrong content type {}'.format(type(content)))
            return

        name = content.data(index, RunnableModel.NAME_ROLE)
        if name in self.d:
            try:
                win32api.ShellExecute(0, 'open', self.d[name].path, '', '', 1)
            except Exception as e:
                print(e)

    def lit(self, query, upper_bound, finished, *args, **kargs):
        self.worker.do(job=Job(self, query, upper_bound, finished))


class Run(Files):

    def __init__(self, worker, **kargs):
        super(Run, self).__init__(worker, **kargs)
        self._paths = []
        for path in os.environ['PATH'].split(os.pathsep):
            path = os.path.expandvars(path)
            if os.path.exists(path):
                for filename in os.listdir(path):
                    _, ext = os.path.splitext(filename)
                    if ext in ['.exe', '.cmd', '.bat', '.lnk']:
                        self._paths.append(os.path.join(path, filename))
        self.path_list_changed()

    @property
    def paths(self):
        return self._paths

    @property
    def name(self):
        return 'r'


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


def set_version(s):
    s.setVersion(QDataStream.Qt_4_0)


def write(con, callback):
    block = QByteArray()
    out = QDataStream(block, QIODevice.WriteOnly)
    set_version(out)
    callback(out)
    con.write(block)


class Client(QObject):

    toggle = pyqtSignal()

    def __init__(self, parent=None):
        super(Client, self).__init__(parent)

        self._make_socket()

    def _make_socket(self):
        self.con = QTcpSocket(self)
        self.con.readyRead.connect(self._handle_read)

    def _handle_read(self):
        ins = QDataStream(self.con)
        set_version(ins)
        line = str(ins.readString(), encoding='ascii')
        if line == 'toggle':
            self.toggle.emit()

    @pyqtSlot()
    def start(self):
        self.con.connectToHost(QHostAddress.LocalHost, PORT)

    def stop(self):
        self.con.disconnectFromHost()

    def _write(self, callback):
        assert self.con
        write(self.con, callback)

    def goto(self, hwnd):
        self._write(lambda out: out.writeString(str(int(hwnd)).encode('ascii')))



class Action(QObject):

    def __init__(self, impl, finished=None, failed=None, main=False, priority=0):
        super(Action, self).__init__()
        self.impl = impl
        self._finished = finished
        self._failed = failed
        self.main = main
        self.priority = priority

    @pyqtSlot()
    def finished(self):
        if self._finished:
            self._finished()
        self.deleteLater()

    @pyqtSlot(object)
    def failed(self, e):
        if self._failed:
            self._failed(e)
        self.deleteLater()

    @pyqtSlot()
    def run(self):
        try:
            self.impl()
            if self.main:
                self.finished()
            else:
                QMetaObject.invokeMethod(
                    self,
                    'finished',
                    Qt.QueuedConnection
                )
        except Exception as e:
            if self.main:
                self.failed(e)
            else:
                QMetaObject.invokeMethod(
                    self,
                    'failed',
                    Qt.QueuedConnection,
                    Q_ARG(object, e)
                )


class Make(QObject):

    def __init__(self, impl, finished=None, failed=None, main=False, priority=0):
        """
        kita pengen cari finished adlh popup yg menerima content utk ngisi list/table/dsb
        content diperoleh stlh impl selesai wkt run.
        jadi content utk daftar completer berasal dari fungsi impl:
        make=lambda: WindowModel(
                self.sorted_active_runnable(
                    query,
                    winutils.top_level_windows()
                )[:upper_bound]
            ),
        result ini dari WindowModel/self.items yg berasal dari kembalian self.sorted_active_runnable()
        ternyata ini daftar hwnd...
        """
        super(Make, self).__init__()
        self.impl = impl
        self._finished = finished
        self._failed = failed
        self.main = main
        self.priority = priority

    @pyqtSlot(object)
    def finished(self, result):
        if self._finished:
            self._finished(result)
        self.deleteLater()

    @pyqtSlot(object)
    def failed(self, e):
        if self._failed:
            self._failed(e)
        self.deleteLater()

    @pyqtSlot()
    def run(self):
        try:
            result = self.impl()
            if self.main:
                self.finished(result)
            else:
                QMetaObject.invokeMethod(
                    self,
                    'finished',
                    Qt.QueuedConnection,
                    Q_ARG(object, result)
                )
        except Exception as e:
            if self.main:
                self.failed(e)
            else:
                QMetaObject.invokeMethod(
                    self,
                    'failed',
                    Qt.QueuedConnection,
                    Q_ARG(object, e)
                )


class Job2(QObject):

    def __init__(self, impl):
        super(Job2, self).__init__()
        self.impl = impl

    @pyqtSlot()
    def run(self):
        self.impl.run()
        self.deleteLater()


class Pool(object):

    def __init__(self):
        self.thread = QThread()
        self.thread.start()
        self.local = QObject()
        self.remote = QObject()
        self.remote.moveToThread(self.thread)

    def start(self, job):
        job.setParent(self.local)
        # job = Job(job)
        job = Job2(job)
        job.moveToThread(self.thread)
        job.setParent(self.remote)
        QMetaObject.invokeMethod(
            job,
            'run',
            Qt.QueuedConnection
        )

    def clear(self):
        for job in self.local.children():
            if hasattr(job, 'cancel'):
                job.cancel()


class Heap(object):

    REMOVED = '<removed-task>'      # placeholder for a removed task

    def __init__(self):
        self.mutex = QMutex()
        self.clear()

    def push(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        with QMutexLocker(self.mutex):
            if task in self.entry_finder:
                self.remove(task)
            count = next(self.counter)
            entry = [priority, count, task]
            self.entry_finder[task] = entry
            heapq.heappush(self.pq, entry)

    def remove(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        with QMutexLocker(self.mutex):
            entry = self.entry_finder.pop(task)
            entry[-1] = self.REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        with QMutexLocker(self.mutex):
            while self.pq:
                priority, count, task = heapq.heappop(self.pq)
                if task is not self.REMOVED:
                    del self.entry_finder[task]
                    return task
            raise KeyError('pop from an empty priority queue')

    def clear(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count

    def __bool__(self):
        return bool(self.pq)


def _getattr(target, name, default):
    return getattr(target, name) if hasattr(target, name) else default


def _check_job(job):
    assert isinstance(job, QObject)
    assert hasattr(job, 'run')


class Worker(QObject):

    def __init__(self):
        super(Worker, self).__init__()
        #self.q = deque()
        self.q = Heap()
        self.pool = Pool()

    @pyqtSlot()
    def deal(self):
        try:
            job = self.q.pop()
        except:
            pass
        else:
            if _getattr(job, 'main', False):
                job.run()
            else:
                self.pool.start(job)
            if self.q:
                self.delay_deal()

    def clear(self):
        self.q.clear()
        self.pool.clear()

    def delay_deal(self):
        QMetaObject.invokeMethod(
            self,
            'deal',
            Qt.QueuedConnection
        )

    def do(self, **kargs):
        """Do some async job, maybe in main thread."""
        if 'make' in kargs:
            make = kargs['make']
            catch = kargs.get('catch', lambda x: x)
            job = Make(
                make,
                catch,
                main=kargs.get('main', False),
                priority=kargs.get('priority', 0)
            )
        elif 'action' in kargs:
            action = kargs['action']
            react = kargs.get('react', lambda: None)
            job = Action(
                action,
                react,
                main=kargs.get('main', False),
                priority=kargs.get('priority', 0)
            )
        elif 'job' in kargs:
            job = kargs['job']
            _check_job(job)
        else:
            assert False, 'Wrong arguments.'

        self.q.push(job, -_getattr(job, 'priority', 0))
        self.delay_deal()


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
            # self.client.stop()
            QApplication.quit()
        # if self.cmd in self.plugins:
        #     self.plugins[self.cmd].act()

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
        self.hide()

    def select(self, index):
        cmd = self.cmd
        #text = self.completer.completionModel().data(index, Qt.DisplayRole)
        self.hide_window()
        assert self.completer.content
        if cmd in self.plugins:
            self.plugins[cmd].select(content=self.completer.content, index=index)

    def _reset_popup(self):
        self.completer.reset()

    def _try_popup(self, content):
        # don't show popup if search box is hidden
        if self.isVisible():
            QTimer.singleShot(0, lambda: self.popup(content))

    def popup(self, content):
        with QMutexLocker(self.mutex):
            self.completer.complete(content)

    def query(self, text):
        cmd, arg = parse_query(text)
        print(f'query, cmd = {cmd}, arg = {arg}, self.plugins: {self.plugins}')
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
            # Go(worker=worker, client=client),
            Run(worker=worker, client=client)
        ]
        self._install_plugins(plugins)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup | Qt.WindowStaysOnTopHint)
        self.setWindowTitle('inputter')
        self.mutex = QMutex()
        self.jobs = []


STYLESHEET = 'style.css'


def main():
    app = QApplication(sys.argv)
    # app.setStyleSheet(app_stylesheet)
    with open(STYLESHEET, 'r') as f:
        app.setStyleSheet(f.read())
    w = TheWIndow()
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=1/2, h_ratio=1/8)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    r"""
    IDE:
    bisa search repl, dia juga terima global hotkey yg bisa focus/aktifkan.
    abis itu muncul editor yg tuliskan hasilnya

    C:\Users\usef\work\sidoarjo\schnell\gui\system\inputter\cara-kerja.md
    """
    main()
