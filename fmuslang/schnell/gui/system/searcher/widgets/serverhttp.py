"""
terima location...rootpath
abis itu python httpserver...
sekaligus dg ngrokker...
"""
import os, random, string, sys
# import shutil
# import functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *


if __name__ == '__main__':
    # envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
    # from dotenv import load_dotenv
    # load_dotenv(envfile)
    # schnelldir = os.environ['ULIBPY_BASEDIR']
    # rootdir = os.environ['ULIBPY_ROOTDIR']
    # sys.path.extend([rootdir, schnelldir])
    from pathlib import Path
    sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
    # schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
    #                              file        wid    sea    sys    gui    sch    sido
    sys.path.append(sidoarjodir)
    from startup import initialize_programming_data
    initialize_programming_data()
    from mkhelp import MKHelpWidget
else:
    from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget
    
from gui.system.searcher.widgets.browsing import BrowsingHttpWidget
from schnell.app.threadutils import mulai
from schnell.app.serverutils import (
    run_server, close_server,
    run_quick, stop_quick,
    start_thread_server1, stop_thread_server1,
    ngonek, nutup, aktif, monitor,
)
from schnell.app.utils import GOOGLESEARCH, buka


server_stylesheet = """
#button_start_http {
    background-color: greenyellow;
}

#button_start_http:checked {
    background-color: darksalmon;
}

#button_start_http:hover {
    background-color: cornsilk;
}

#button_start_ngrok {
    background-color: greenyellow;
}

#button_start_ngrok:checked {
    background-color: darksalmon;
}

#button_start_ngrok:hover {
    background-color: cornsilk;
}
"""


class HttpServerStarterThread(QThread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
    def run(self):
        start_thread_server1(self.host, self.port)


class HttpServerStopperThread(QThread):

    """
    stopper untuk ThreadingSimpleServer
    callback adlh utk ganti icon dari stop-icon ke start-icon
    """
    def __init__(self, host, port, stop_callback):
        super().__init__()
        self.host = host
        self.port = port
        self.stop_callback = stop_callback
    def run(self):
        print('HttpServerStopperThread stopping start')
        stop_thread_server1(self.host, self.port)
        print('HttpServerStopperThread stopping end')
        self.stop_callback()


class ServerHttpWidget(QWidget):

    def __init__(self, publisher=None):
        super().__init__()
        self.publisher=publisher
        self.initUI()

    def toggle_start_stop_ngrok(self, checked):
        if checked:
            # masuk start
            self.start_ngrok.setIcon(self.stop_icon)
            self.start_ngrok.setText('Stop')
            port = self.ngrok_spinbox.value()
            self.ngrok_status.append(f'starting ngrok at {port}...')
            ngonek(port)
        else:
            port = self.ngrok_spinbox.value()
            self.start_ngrok.setIcon(self.start_icon)
            self.start_ngrok.setText('Start')
            self.ngrok_status.append(f'stopping ngrok at {port}...')
            nutup(port)

    def toggle_start_stop(self, checked):
        if checked:
            # masuk start
            self.start_http.setIcon(self.stop_icon)
            self.start_http.setText('Stop')
            port = self.http_spinbox.value()
            # res = run_server('localhost', port)
            # res = run_quick('localhost', port)
            # res = start_thread_server1('localhost', port)
            # start_thread_server1('localhost', port)
            self.t = HttpServerStarterThread('localhost', port)
            self.t.start()
            print('jika anda baca ini maka tidak terblock')
        else:

            port = self.http_spinbox.value()
            def callback():
                # terpanggil jk berhasil stop
                self.start_http.setIcon(self.start_icon)
                self.start_http.setText('Start')
            self.t2 = HttpServerStopperThread('localhost', port, callback)
            self.t2.start()
            self.t.quit()
            self.t2.quit()

    def change_rootpath(self, rootpath):
        self.rootpath = rootpath
        self.rootpath_control.setText(self.rootpath)
        self.mkhelp_widget.change_rootpath(self.rootpath)

    def initUI(self):

        self.setStyleSheet(server_stylesheet)

        self.start_icon = QApplication.style().standardIcon(QStyle.SP_MediaPlay)
        self.stop_icon = QApplication.style().standardIcon(QStyle.SP_MediaStop)

        self.main_layout = QVBoxLayout()

        self.box_repl_google = QGroupBox("Repl or Googl")
        self.box_repl_google_layout = QVBoxLayout()
        self.box_repl_google.setLayout(self.box_repl_google_layout)
        self.entry_input = QLineEdit()
        self.entry_input.setFont(QFont("Consolas", 16))
        self.entry_input.setStyleSheet('background-color: oldlace; height: 48px;')
        self.entry_input.returnPressed.connect(self.query_searching)
        # self.publisher = None
        self.history = []
        self.completer = QCompleter(self.history)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.entry_input.setCompleter(self.completer)
        # toolbar di bawah qlineedit
        self.code_sidoarjo = QPushButton('Code Sidoarjo')
        self.ssh_server = QPushButton('SSH')
        self.notepad_win = QPushButton('Notepad')
        self.notepad_pp = QPushButton('Notepad++')
        self.google_mode = QCheckBox()
        self.google_mode.setChecked(True)
        google_mode_label = QLabel('Google mode')
        self.search_site = QCheckBox()        
        search_site_label = QLabel('Search site')
        self.site_list = QComboBox()
        self.site_list.addItems(['site:stackoverflow.com'])
        toolbarlayout = QHBoxLayout()
        toolbarlayout.addStretch(1)
        toolbarlayout.addWidget(self.code_sidoarjo)
        toolbarlayout.addWidget(self.ssh_server)
        toolbarlayout.addWidget(self.notepad_win)
        toolbarlayout.addWidget(self.notepad_pp)
        toolbarlayout.addWidget(self.google_mode)
        toolbarlayout.addWidget(google_mode_label)
        toolbarlayout.addWidget(self.search_site)
        toolbarlayout.addWidget(search_site_label)
        toolbarlayout.addWidget(self.site_list)
        self.box_repl_google_layout.addWidget(self.entry_input)
        self.box_repl_google_layout.addLayout(toolbarlayout)

        # http part
        box_httpserver = QGroupBox("HTTP Server")
        layout_boxhttpserver = QVBoxLayout()

        formlayout_http = QFormLayout()
        self.http_spinbox = QSpinBox()
        self.serverport = 8080 # dipake juga di ngrokker...
        self.rootpath = r'C:/tmp'
        self.http_spinbox.setRange(8000,8999)
        self.http_spinbox.stepBy(1)
        self.http_spinbox.setValue(self.serverport)
        formlayout_http.addRow('port', self.http_spinbox)
        self.rootpath_control = QLineEdit(self.rootpath)
        self.rootpath_control.setStyleSheet('background-color: linen; width: 150px;')
        formlayout_http.addRow('rootpath', self.rootpath_control)

        http_hbox = QHBoxLayout()
        http_hbox.addLayout(formlayout_http)
        self.start_http = QPushButton('Start')
        self.start_http.setCheckable(True)
        self.start_http.setChecked(False)
        self.start_http.setIcon(self.start_icon)
        self.start_http.setObjectName("button_start_http")
        self.start_http.toggled.connect(self.toggle_start_stop)
        http_hbox.addStretch(1)
        http_hbox.addWidget(self.start_http)

        layout_boxhttpserver.addLayout(http_hbox)

        # layout_boxhttpserver.addStretch(1)
        box_httpserver.setLayout(layout_boxhttpserver)
        

        # ngrok part
        box_ngrok = QGroupBox("Ngrok")
        layout_boxngrok = QVBoxLayout()
        formlayout_ngrok = QFormLayout()
        self.ngrok_spinbox = QSpinBox()
        self.ngrok_spinbox.setRange(8000,8999)
        self.ngrok_spinbox.stepBy(1)
        self.ngrok_spinbox.setValue(self.serverport)
        formlayout_ngrok.addRow('port', self.ngrok_spinbox)

        ngrok_hbox = QHBoxLayout()
        ngrok_hbox.addLayout(formlayout_ngrok)
        self.start_ngrok = QPushButton('Start')
        self.start_ngrok.setObjectName('button_start_ngrok')
        self.start_ngrok.setCheckable(True)
        self.start_ngrok.setChecked(False)
        self.start_ngrok.setIcon(self.start_icon)
        self.start_ngrok.toggled.connect(self.toggle_start_stop_ngrok)

        # tambah textbrowser
        self.ngrok_status = QTextBrowser()

        self.close_ngrok = QPushButton('Close')
        self.close_ngrok.clicked.connect(self.close_tunnel)
        self.status_ngrok = QPushButton('Status')
        self.status_ngrok.clicked.connect(self.see_status)
        ngrok_hbox.addStretch(1)
        ngrok_hbox.addWidget(self.close_ngrok)
        ngrok_hbox.addWidget(self.status_ngrok)
        ngrok_hbox.addWidget(self.start_ngrok)

        ngrok_wrap_old_and_browser = QVBoxLayout()
        ngrok_wrap_old_and_browser.addLayout(ngrok_hbox)
        ngrok_wrap_old_and_browser.addWidget(self.ngrok_status)
        layout_boxngrok.addLayout(ngrok_wrap_old_and_browser)
        box_ngrok.setLayout(layout_boxngrok)

        self.http_spinbox.valueChanged.connect(self.ngrok_spinbox.setValue)
        self.ngrok_spinbox.valueChanged.connect(self.http_spinbox.setValue)

        # MKHelpWidget
        # self.mkhelpbox = QGroupBox("MK Help")
        self.mkhelpbox = QWidget() # terlalu makan tempat
        mkhelpbox_layout = QVBoxLayout()
        self.mkhelpbox.setLayout(mkhelpbox_layout)
        self.mkhelp_widget = MKHelpWidget()
        mkhelpbox_layout.addWidget(self.mkhelp_widget)

        self.main_layout.addWidget(self.box_repl_google)
        self.main_layout.addWidget(self.mkhelpbox)

        # self.box_http_server = QGroupBox('Server')
        self.box_http_server = QWidget()
        server_group_layout = QVBoxLayout()
        self.box_http_server.setLayout(server_group_layout)
        # self.box_http_client = QGroupBox('Client')
        self.box_http_client = QWidget()
        client_group_layout = QVBoxLayout()
        self.box_http_client.setLayout(client_group_layout)
        server_client = QHBoxLayout()
        server_client.addWidget(self.box_http_server)
        server_client.addWidget(self.box_http_client)

        self.browsing_http = BrowsingHttpWidget()
        # self.main_layout.addWidget(box_httpserver)
        # self.main_layout.addWidget(box_ngrok)
        server_group_layout.addWidget(box_httpserver)
        server_group_layout.addWidget(box_ngrok)
        client_group_layout.addWidget(self.browsing_http)
        self.main_layout.addLayout(server_client)
        # bisa toggle box repl/google dan box server+client
        self.mkhelp_widget.toggle_top_signal.connect(self.box_repl_google.setHidden)
        self.mkhelp_widget.toggle_bot_signal.connect(self.box_http_server.setHidden)
        self.mkhelp_widget.toggle_bot_signal.connect(self.box_http_client.setHidden)

        self.notepad_win.clicked.connect(lambda: mulai(self.notepad, ()))
        self.notepad_pp.clicked.connect(lambda: mulai(self.notepad, (True,)))
        self.ssh_server.clicked.connect(lambda: mulai(self.ssh_server_handler))
        self.code_sidoarjo.clicked.connect(lambda: mulai(self.exec_code_sidoarjo))

        self.setLayout(self.main_layout)

    def exec_code_sidoarjo(self):
        import subprocess
        from schnell.app.utils import env_get
        subprocess.run(f'code {env_get("ULIBPY_ROOTDIR")}'.split(), shell=True)

    def ssh_server_handler(self):
        from schnell.app.fmusutils import run_fmus_for_content_in_thread
        # run_fmus_for_content_in_thread('/ketik)ssh -l root fulgent.hopto.org')
        run_fmus_for_content_in_thread('/ketik)ssh -l root 143.198.203.74')

    def notepad(self, plusplus=False):
        import subprocess
        if plusplus:
            subprocess.run([r'C:\Program Files"\Notepad++\notepad++.exe'], shell=True)
        else:
            subprocess.run(r'C:\Windows\system32\notepad.exe'.split(), shell=True)

    def see_status(self):
        data = aktif()
        for item in data:
            self.ngrok_status.append(str(item))
        # self.ngrok_status.append('http://8.tcp.ngrok.io:15921/')

    def close_tunnel(self):
        # port = self.ngrok_spinbox.value()
        # nutup(port, forced=True)
        pass

    def set_input_completer(self):
        model = self.completer.model()
        model.setStringList(self.history)

    def setRedisPublisher(self, publisher):
        """
        from make_redis_help import redis_publish
        self.internal_clocker.setRedisPublisher(redis_publish)
        """
        self.publisher = publisher

    def query_searching(self):
        query = self.entry_input.text()
        if self.google_mode.checkState() == Qt.Checked:
            # https://www.google.com/search?client=firefox-b-d&q=qtextbrowse+site%3Astackoverflow.com
            if self.search_site.checkState() == Qt.Checked:
                query += self.site_list.currentText()
            __TEXTPLACEHOLDER__ = query.replace(' ', '+').replace(':', '%3A')
            alamat = GOOGLESEARCH.replace('__TEXTPLACEHOLDER__', __TEXTPLACEHOLDER__)
            buka(alamat)
        elif self.publisher:
            self.publisher(query)
            # self.entry_input.setText('') # kadang masih pengen gunakan last query
            if query not in self.history:
                self.history.append(query)
            self.set_input_completer()


# background_image_stylesheet = '''
# FileManager {
#     border-image: url("bg.jpg");
#     background-repeat: no-repeat; 
#     background-position: center;
# }
# '''


def main():
    app = QApplication([])
    w = ServerHttpWidget()
    # ex.setStyleSheet(background_image_stylesheet)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
