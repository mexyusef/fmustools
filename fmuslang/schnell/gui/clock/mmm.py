import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import (
	QsciScintilla,
	QsciLexerCustom,
	QsciLexerJSON,
	QsciLexerPython,
)
from PyQt5.QtCore import (
	pyqtSlot as qslot,
	pyqtSignal as qsignal,
	Qt as K,
	QCoreApplication,
	QEvent,
	QMimeData,
	QPoint,
	QSize,
	QTime,
	QTimer,
)
from PyQt5.QtGui import (
	QBrush,
	QDrag,
	QIcon,
	QPalette,
	QPainter,
	QPen,
	QPixmap,
	QPolygon,
	QKeySequence as kunci,
)
from PyQt5.QtWidgets import (
	QApplication,
	QCheckBox,
	QDesktopWidget,
	QDialog,
	QFormLayout,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMessageBox,
	QMenu,
	QPushButton,
	QScrollArea,
	QShortcut,
	QTextEdit,
	QToolTip,
	QVBoxLayout,
	QWidget,
	qApp,
)
# import typing


class BlockWidget(QWidget):
    def __init__(self, parent=None, angka_mulai=1, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.angka_mulai = angka_mulai
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        rows = 20
        cols = 5
        for i in range(rows):
            for j in range(cols):
                btn = QPushButton(f"{self.angka_mulai}")
                self.angka_mulai += 1
                btn.setStyleSheet("background-color:skyblue;")
                # btn.resize(20,10) # gak pengaruh
                # btn.clicked.connect(self.button_clicked)
                self.gridLayout.addWidget(btn, i, j)

        lay = QVBoxLayout()
        lay.addWidget(self.scrollArea)
        self.setLayout(lay)
        self.setMinimumWidth(500)


class MmmWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)


        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        jumlah = 10
        for i in range(jumlah):
            bw = BlockWidget(self, 100*i)
            self.gridLayout.addWidget(bw, 1, i)
        lay = QVBoxLayout()
        lay.addWidget(self.scrollArea)
        self.setLayout(lay)


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	# app.setStyleSheet('#testBtn{min-height:40px; background:green;}')
	wnd = MmmWidget()
	screen_geometry = QDesktopWidget().screenGeometry(-1)
	w,h = screen_geometry.width(), screen_geometry.height()
	wnd.resize(int(w*3/4), int(h*3/4))
	wnd.show()
	sys.exit(app.exec_())
