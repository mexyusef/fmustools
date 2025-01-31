import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *


from common import (
    set_app_info,
    set_version,
    write,
    PORT,
)
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

