import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from functools import partial
import os, windows
import win32api

from utils import Query

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


class RunJob(QObject):

    mutex = QMutex()

    def __init__(self, p, query, upper_bound, finished):
        super(RunJob, self).__init__()
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
        self.worker.do(job=RunJob(self, query, upper_bound, finished))


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


