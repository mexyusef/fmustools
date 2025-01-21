kode_output = """
import os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__ADDITIONAL_CLASSES__

__FUNCTIONS__

class MainWindow(__PARENT_WINDOW__):

__METHODS__

    def __init__(self):
        super().__init__()
__WINDOWS_ATTRIBUTES__
        self.initUI()

    def initUI(self):

        self.main_layout = __LAYOUT__
__LAYOUT_CONTENT__
__SET_MAIN_LAYOUT_CODE__



def get_icon():
    pixmap = QPixmap(16, 16)
    pixmap.fill(Qt.transparent)
    painter = QPainter()
    painter.begin(pixmap)
    painter.setFont(QFont('Webdings', 11))
    painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
    painter.drawText(0, 0, 16, 16, Qt.AlignCenter, random.choice(string.ascii_letters))
    painter.end()
    return QIcon(pixmap)


def set_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)


background_image_stylesheet = '''
MainWindow {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
__INVOKE_APPLICATION__
    wnd = MainWindow()
    wnd.setStyleSheet(background_image_stylesheet)
    wnd.show()
    wnd.resize(__LEBAR__, __TINGGI__)
    wnd.setWindowTitle('__JUDUL__')
    QShortcut(QKeySequence("Ctrl+Q"), wnd, activated=lambda: qApp.quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""
