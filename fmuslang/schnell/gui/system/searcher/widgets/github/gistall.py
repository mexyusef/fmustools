from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os, sys

if __name__ == '__main__':
    from gist import GistWindow as GistWindowOriginal
    from gistlist import GistListWindow
else:
    from .gist import GistWindow as GistWindowOriginal
    from .gistlist import GistListWindow

# class GistWindow(QWidget):
class GistWindow(QDialog):
    def __init__(self, parent=None):
        super(GistWindow, self).__init__(parent=parent)
        layout = QVBoxLayout()

        second_splitter = QSplitter(self)
        second_splitter.setHandleWidth(8)
        second_splitter.setOrientation(Qt.Horizontal)
        self.left = GistWindowOriginal(will_close=False)
        self.right = GistListWindow(will_close=False)
        second_splitter.addWidget(self.left)
        second_splitter.addWidget(self.right)
        layout.addWidget(second_splitter)

        self.setLayout(layout)


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

def main():
    app = QApplication([])
    set_theme(app)
    window = GistWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()