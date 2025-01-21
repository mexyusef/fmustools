from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
import logging

import windows
from hotkey import Hotkey
from common import (
    set_app_info,
    set_version,
    write,
    PORT,
)

class Server(QObject):

    def __init__(self, parent=None):
        super(Server, self).__init__(parent)

        self._make_tcp_server()

        self.hotkey_thread = HotkeyThread()
        self.hotkey_thread.fire.connect(self._handle_hotkey)

    def _make_tcp_server(self):
        self.s = QTcpServer(self)
        self.s.newConnection.connect(self._handle_connect)
        self.con = None

    def _handle_connect(self):
        self.con = self.s.nextPendingConnection()
        self.con.readyRead.connect(self._handle_read)
        self.con.disconnected.connect(self._handle_disconnect)
        logging.info('connected')

    def _handle_disconnect(self):
        self.con.deleteLater()
        QCoreApplication.quit()

    def _write(self, callback):
        assert self.con
        write(self.con, callback)

    def _handle_hotkey(self):
        logging.info('toggle')
        self._write(lambda out: out.writeString(b'toggle'))

    def _handle_read(self):
        ins = QDataStream(self.con)
        set_version(ins)
        line = str(ins.readString(), encoding='ascii')
        logging.info(line)
        windows.goto(int(line))

    @pyqtSlot()
    def start(self):
        self.hotkey_thread.start()

        if not self.s.listen(QHostAddress.LocalHost, PORT):
            logging.error(
                "Unable to start the server: %s." %
                self.tcpServer.errorString()
            )
            return


class HotkeyThread(QThread):

    fire = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)    
        # self.hotkey = Hotkey(self.handle_hotkey)

    def handle_hotkey(self):
        self.fire.emit()

    def stop(self):
        # self.hotkey.stop()
        pass

    def run(self):
        # self.hotkey.start()
        pass


if __name__ == '__main__':
    import sys
    import os
    logging.basicConfig(
        filename=os.path.expanduser('.server.log'),
        filemode='w',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    app = QCoreApplication(sys.argv)
    set_app_info(app, 'litserver')
    server = Server()
    QMetaObject.invokeMethod(
        server,
        'start',
        Qt.QueuedConnection
    )
    sys.exit(app.exec_())
