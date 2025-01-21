from PyQt5.QtWidgets import QApplication
from pyqt_transparent_timer import TransparentTimer


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    tm = TransparentTimer()
    tm.show()
    app.exec_()