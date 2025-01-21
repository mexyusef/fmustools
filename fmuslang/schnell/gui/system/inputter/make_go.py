import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from datetime import datetime
import itertools

import windows as winutils
from utils import Query

NAME_LIMIT = 42


def lcs(x, y):
    n = len(x)
    m = len(y)
    table = dict()  # a hashtable, but we'll use it as a 2D array here

    for i in range(n+1):     # i=0,1,...,n
        for j in range(m+1):  # j=0,1,...,m
            if i == 0 or j == 0:
                table[i, j] = 0
            elif x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i-1, j], table[i, j-1])

    # Now, table[n, m] is the length of LCS of x and y.

    # Let's go one step further and reconstruct
    # the actual sequence from DP table:

    def recon(i, j):
        if i == 0 or j == 0:
            return []
        elif x[i-1] == y[j-1]:
            return recon(i-1, j-1) + [x[i-1]]
        elif table[i-1, j] > table[i, j-1]:
            return recon(i-1, j)
        else:
            return recon(i, j-1)

    return recon(n, m)


class Task(object):

    def __init__(self, hwnd, query, usetime):
        self.hwnd = hwnd
        self.query = query
        self.usetime = usetime

    def use(self):
        self.usetime = datetime.now()

    @property
    def digest(self):
        if len(self.name) > NAME_LIMIT:
            shortname = self.name[:NAME_LIMIT - 3] + '...'
        else:
            shortname = self.name
        if self.filename:
            return '%s (%s)' % (shortname, self.filename)
        else:
            return shortname

    @property
    def title(self):
        return self.name

    @property
    def fullname(self):
        if self.filename:
            return self.title + self.filename
        else:
            return self.title

    @property
    def filename(self):
        if not hasattr(self, '_filename'):
            self._filename = winutils.get_app_name(self.hwnd)
        return self._filename

    @property
    def name(self):
        return winutils.window_title(self.hwnd)

    @property
    def icon(self):
        if not hasattr(self, '_icon'):
            self._icon = winutils.get_window_icon(self.hwnd)
        return self._icon


class WindowModel(QAbstractListModel):

    NAME_ROLE = Qt.DisplayRole
    HWND_ROLE = Qt.UserRole

    def __init__(self, items):
        self.super.__init__()
        self.items = items

    @property
    def super(self):
        return super(WindowModel, self)

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        return 1

    def data(self, index, role=Qt.UserRole):
        if not index.isValid():
            return None
        if role == Qt.TextAlignmentRole:
            return int(Qt.AlignLeft | Qt.AlignVCenter)
        elif role == Qt.DisplayRole:
            data = self.items[index.row()].digest
            # print('return digest:', data)
            return data
        elif role == Qt.DecorationRole:
            return self.items[index.row()].icon
        elif role == Qt.UserRole:
            return self.items[index.row()].hwnd
        else:
            return None


class Go(object):

    def __init__(self, worker, client):
        self.tasks = {}
        self.mutex = QMutex()
        self.worker = worker
        self.client = client

    @property
    def name(self):
        return 'g'

    def lit(self, query, upper_bound, finished, *args, **kargs):
        self.worker.do(
            # make adlh self.impl nantinya self.impl(), hasilnya??? WindowModel yg punya items dan data
            make=lambda: WindowModel(
                self.sorted_active_runnable(
                    query,
                    winutils.top_level_windows()
                )[:upper_bound]
            ),
            catch=finished,
            main=True
        )

    def sorted_active_runnable(self, query, hwnds):
        with QMutexLocker(self.mutex):
            # update query and collect active ones
            self._refresh_tasks(hwnds, query)
            active_tasks = [self.tasks[h] for h in hwnds]

            # sort by last use
            if not query:
                return sorted(active_tasks, key=lambda t: t.usetime, reverse=True)

            titles = [task.fullname.lower() for task in active_tasks]

            def f(task, title):
                return task.query.distance_to(title)

            ds = [f(task, title) * (10 ** len(query)) for task, title in zip(active_tasks, titles)]
            best = ds[0]

            for i in itertools.takewhile(lambda i: ds[i] == best, range(len(ds))):
                ds[i] -= len(lcs(query, titles[i]))

            #return sorted(active_tasks, key=f)
            return [task for i, task in sorted(enumerate(active_tasks), key=lambda i: ds[i[0]])]

    def _refresh_tasks(self, hwnds, query=None):
        for hwnd in hwnds:
            if not hwnd in self.tasks:
                """
                daftarkan entry dulu jk belum, stlh jd Task, baru bisa hitung jauhnya ke user query
                """
                self.tasks[hwnd] = Task(
                    hwnd=hwnd,
                    usetime=datetime.now(),
                    query=Query(
                        text='' if query is None else query,
                        insertion_cost=1,
                        first_insertion_cost=50,
                        prepend_first_insertion_cost=5,
                        append_first_insertion_cost=10,
                        deletion_cost=100,
                        substitution_cost=100,
                        transposition_cost=10
                    )
                )
            elif not (query is None):
                """
                utk tiap entry yg ada, hitung kedekatannya ke user query
                """
                self.tasks[hwnd].query.update(query.lower())

    def update_usetime(self, hwnd):
        """Update with one time delay."""
        if hasattr(self, 'after_select') and self.after_select:
            self.after_select()
        self.after_select = self.tasks[hwnd].use

    def select(self, content, index):
        # check content type
        if not isinstance(content, WindowModel):
            print('wrong content type {}'.format(type(content)))
            return

        for hwnd in winutils.top_level_windows():
            if content.data(index, WindowModel.HWND_ROLE) == hwnd:
                self._refresh_tasks([hwnd])
                self.client.goto(hwnd=hwnd)
                self.update_usetime(hwnd)
                return

        # remove invalid tasks
        del self.tasks[content.data(index, WindowModel.HWND_ROLE)]

    def act(self):
        print('im acting as make_go now...')
        # QApplication.quit()

