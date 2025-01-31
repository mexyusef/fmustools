# import os, re, sys
# import win32api
# from functools import partial

import heapq
import itertools
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

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
            # print('worker Make, memanggil finish dg result:', result)
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


class Job(QObject):

    def __init__(self, impl):
        super(Job, self).__init__()
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
        job = Job(job)
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
        """Do some asyne job, maybe in main thread."""
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

