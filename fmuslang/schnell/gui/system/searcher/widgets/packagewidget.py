
"""
konsep spt apa?
flow widget tentunya
ada checkbox dan ada button...dg property 'versi'
"""

import functools, os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .flowwidget import FlowWidget


class PackageItem(QWidget):

    def __init__(self, name):
        super().__init__()
        self.name = name # package name
        self.version = None
        self.menu = None
        self.checkbox = QCheckBox()
        if ',' in name:
            self.name, self.version = name.split(',',1)
            if ',' in self.version:
                pecah = self.version.split(',')
                self.version = None  # default
                self.menu = QMenu(self.name, self)
                self.menu.addAction('None', functools.partial(self.set_version, self.version))  # default

                for i,versi in enumerate(pecah):
                    self.menu.addAction(versi, functools.partial(self.set_version, versi))

        self.initUI()
    
    def set_version(self, versi):
        self.version = versi
        self.checkbox.setChecked(True)

    def initUI(self):
        self.main_layout = QHBoxLayout()
        # self.checkbox.stateChanged.connect(lambda state: print('a says yes' if state==Qt.Checked else 'a says no'))
        self.main_layout.addWidget(self.checkbox)
        self.button = QPushButton(self.name)
        self.button.clicked.connect(lambda: print(self.name))
        if self.menu:
            self.button.setMenu(self.menu)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

    def isChecked(self):
        return self.checkbox.isChecked()


class PackageWidget(QWidget):

    def __init__(self,
        items=['satu', 'dua', 'tiga', 'empat', 'lima', 'enam,1.0.0,^2.1.1,3', 'tujuh', 'delapan', 'sembilan', 'sepuluh'],
        callback=None, button_mode=False):
        """
        button_mode
            True = QPushButton
            False = PackageItem
        """
        super().__init__()
        self.items = items
        self.callback = callback
        self.button_mode = button_mode
        self.initUI()
        self.setStyleSheet("""
QPushButton {
    background-color: wheat;
    border-radius: 5px;
    border: 1px solid darkblue;
    font-size: 14pt;
    margin: 2px;
    padding: 5px;
}
QPushButton:hover{ 
    background-color: papayawhip;
    color:lightsalmon; 
}
""")

    def initUI(self):

        self.main_layout = QVBoxLayout()
        dummy_text = QLabel('__________________________________________________________________________________________________________________________________________________________________________')        
        dummy_text.setStyleSheet('font-family: Verdana, Arial, Consolas;')
        self.main_layout.addWidget(dummy_text)
        flow0 = FlowWidget()
        self.widgets = []
        for item in self.items:
            if self.button_mode:
                b = QPushButton(item)
                b.setProperty('command', item)
                b.clicked.connect(functools.partial(self.process_click, item))
            else:
                b = PackageItem(item)
            self.widgets.append(b)
        flow0.add_items(self.widgets)
        self.main_layout.addWidget(flow0)
        self.setLayout(self.main_layout)

        if not self.button_mode:
            self.process = QPushButton('Process')
            self.process.setStyleSheet("""
QPushButton {
    background-color: ivory;
    border-radius: 3px;
}
QPushButton:hover {
    background-color: gold;
}
""")
            self.main_layout.addWidget(self.process)
            if self.button_mode:
                self.process.clicked.connect(self.process_packages)

    def process_click(self, cmd):
        if self.callback:
            self.callback(cmd)
            # b = self.sender()
            # cmd = b.property('command')
            # if cmd:
            #     self.callback(cmd)

    def process_packages(self):
        # from rich.pretty import pprint
        selection = []
        for item in self.widgets:
            if item.isChecked():
                # selection.append({'name':item.name, 'version':item.version})
                if item.version:
                    hasil = f"{item.name}@{item.version}"
                else:
                    hasil = item.name
                selection.append(hasil)
        # pprint(selection)
        selection = ' '.join(selection)
        if self.callback:
            self.callback(selection)
        # stlh install, clear selection
        for item in self.widgets:
            item.checkbox.setChecked(False)


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


background_image_stylesheet = '''
PackageItem {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    ex = PackageWidget()
    ex.show()
    ex.setStyleSheet(background_image_stylesheet)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
