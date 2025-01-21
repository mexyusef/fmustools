
import os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser, threading

browsers = {
    'chrome': "C:/Program Files/Google/Chrome/Application/chrome.exe %s",
    'opera': "C:/Users/usef/AppData/Local/Programs/Opera/opera.exe %s",
    'firefox': "C:/Program Files/Mozilla Firefox/firefox.exe %s",
}

hosts = [
    'http://localhost:3000',
    'http://localhost:4000',
    'http://localhost:5000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:9000',
    'http://localhost',
]

if __name__ == 'gui.system.searcher.widgets.browsing':
    '''
    name: gui.system.searcher.widgets.browsing
    package: gui.system.searcher.widgets
    '''
    from .config import default_websites
else:
    print('name:', __name__)
    print('package:', __package__)
    # print('module:', __module__)
    from config import default_websites


class BrowsingHttpWidget(QWidget):

    def radio_open_handler(self, value):
        pengirim = self.sender()
        # print(pengirim.text())
        radio = self.radio_group.checkedButton()
        # if pengirim == radio:
        #     print('radio terpilih:', radio.text(), 'pengirim:', pengirim.text())


    def radio_browser_handler(self, value):
        pengirim = self.sender()
        # print(pengirim.text())
        radio = self.radio_browser_group.checkedButton()
        # if pengirim == radio:
        #     print('radio terpilih:', radio.text(), 'pengirim:', pengirim.text())

    def __init__(self):
        super().__init__()
        self.initUI()

    def set_input_completer(self):
        model = self.completer.model()
        model.setStringList(self.history)

    def start_browsing(self):
        lokasi = self.alamat.text().strip()
        if lokasi:
            browser_radio = self.radio_browser_group.checkedButton()
            browser = webbrowser.get(browser_radio.property('path'))
            x = threading.Thread(target=browser.open, args=(lokasi,))
            # browser.open(lokasi)
            x.start()
            if lokasi not in self.history:
                self.history.append(lokasi)
            self.set_input_completer()
            self.alamat.setText('')

    def combo_select(self, text):
        self.alamat.setText(text)
        self.start_browsing()

    def initUI(self):

        self.main_layout = QVBoxLayout()

        mylayout = QHBoxLayout()
        self.alamat = QLineEdit("")
        self.alamat.returnPressed.connect(self.start_browsing)
        # self.alamat.setFont(QFont("Consolas", 16))
        self.alamat.setStyleSheet('background-color: oldlace; height: 48px;')
        self.history = [] + default_websites
        self.completer = QCompleter(self.history)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.alamat.setCompleter(self.completer)

        mylayout.addWidget(self.alamat)
        btn1 = QPushButton("go")
        btn1.clicked.connect(self.start_browsing)
        mylayout.addWidget(btn1)
        self.main_layout.addLayout(mylayout)

        groupbox = QGroupBox("Browsing")

        self.radios_opens = []
        self.radios_browsers = []
    
        groupbox_layout = QVBoxLayout()

        layoutbtn = QHBoxLayout()
        self.radio_group = QButtonGroup(self)

        for openstyle in ['open', 'open_new', 'open_new_tab']:
            radio = QRadioButton(openstyle)
            radio.toggled.connect(self.radio_open_handler)
            self.radio_group.addButton(radio)
            layoutbtn.addWidget(radio)
            self.radios_opens.append(radio)


        groupbox_layout.addLayout(layoutbtn)
 
        layoutbrowser = QVBoxLayout()
        self.radio_browser_group = QButtonGroup(self)

        for browser, lokasi in browsers.items():
            radio = QRadioButton(browser)
            radio.toggled.connect(self.radio_browser_handler)
            radio.setProperty('path', lokasi)
            self.radio_browser_group.addButton(radio)
            layoutbrowser.addWidget(radio)
            self.radios_browsers.append(radio)
        
        radio_and_combo = QHBoxLayout()
        self.combo_hosts = QComboBox()
        self.combo_hosts.addItems(hosts)
        self.combo_hosts.currentTextChanged.connect(self.combo_select)
        radio_and_combo.addLayout(layoutbrowser)
        radio_and_combo.addWidget(self.combo_hosts)
        # groupbox_layout.addLayout(layoutbrowser)
        groupbox_layout.addLayout(radio_and_combo)

        # initial choice
        self.radios_opens[0].setChecked(True)
        self.radios_browsers[0].setChecked(True)

        # groupbox_layout.addStretch(1)
        groupbox.setLayout(groupbox_layout)
        self.main_layout.addWidget(groupbox)
        self.setLayout(self.main_layout)

        # self.resize(800, 600)
        # self.setWindowTitle('browsing around')
        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # self.show()


# def get_icon():
#     pixmap = QPixmap(16, 16)
#     pixmap.fill(Qt.transparent)
#     painter = QPainter()
#     painter.begin(pixmap)
#     painter.setFont(QFont('Webdings', 11))
#     painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
#     painter.drawText(0, 0, 16, 16, Qt.AlignCenter, random.choice(string.ascii_letters))
#     painter.end()
#     return QIcon(pixmap)


# def set_theme(app):
#     app.setStyle("Fusion")
#     palette = QPalette()
#     palette.setColor(QPalette.Window, QColor(53, 53, 53))
#     palette.setColor(QPalette.WindowText, Qt.white)
#     palette.setColor(QPalette.Base, QColor(25, 25, 25))
#     palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
#     palette.setColor(QPalette.ToolTipBase, Qt.black)
#     palette.setColor(QPalette.ToolTipText, Qt.white)
#     palette.setColor(QPalette.Text, Qt.white)
#     palette.setColor(QPalette.Button, QColor(53, 53, 53))
#     palette.setColor(QPalette.ButtonText, Qt.white)
#     palette.setColor(QPalette.BrightText, Qt.red)
#     palette.setColor(QPalette.Link, QColor(42, 130, 218))
#     palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
#     palette.setColor(QPalette.HighlightedText, Qt.black)
#     app.setPalette(palette)


# background_image_stylesheet = '''
# BrowsingHttpWidget {
#     border-image: url("bg.jpg");
#     background-repeat: no-repeat; 
#     background-position: center;
# }
# '''


# def main():
#     app = QApplication([])
#     ex = BrowsingHttpWidget()
#     ex.show()
#     ex.setStyleSheet(background_image_stylesheet)
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
