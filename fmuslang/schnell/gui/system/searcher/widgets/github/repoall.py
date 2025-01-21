from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QColor
import os, sys

if __name__ == '__main__':
    from repo import RepoWindow
    from repolist import RepoListWindow
    from repouser import RepoUserWindow
else:
    # print('repo all START')
    # launchdir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir))
    # systemdir = os.path.normpath(os.path.join(launchdir, os.pardir))
    # guidir = os.path.normpath(os.path.join(systemdir, os.pardir))
    # schnelldir = os.path.normpath(os.path.join(guidir, os.pardir))
    # # envfile = os.path.join(schnelldir, '.env')
    # # from dotenv import load_dotenv
    # # load_dotenv(envfile)
    # # schnelldir = os.environ['ULIBPY_BASEDIR']
    # sys.path.extend([schnelldir, '..'])
    # from gui.system.launcher.helper.repo import RepoWindow
    # from gui.system.launcher.helper.repolist import RepoListWindow
    from .repo import RepoWindow
    from .repolist import RepoListWindow
    from .repouser import RepoUserWindow

# class RepoAllWindow(QWidget):
class RepoAllWindow(QDialog):
    def __init__(self, parent=None):
        super(RepoAllWindow, self).__init__(parent=parent)
        layout = QVBoxLayout()

        second_splitter = QSplitter(self)
        second_splitter.setHandleWidth(8)
        second_splitter.setOrientation(Qt.Horizontal)
        self.left = RepoWindow(will_close=False)
        self.right = RepoListWindow(will_close=False)
        self.rightmost = RepoUserWindow(will_close=False)
        second_splitter.addWidget(self.left)
        second_splitter.addWidget(self.right)
        second_splitter.addWidget(self.rightmost)
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
    window = RepoAllWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
