# https://gist.github.com/DataSolveProblems/85b89d888921a3f423a931448b283d5d

import sys
# from PyQt5.QtCore import (
# 	QAction
# )
from PyQt5.QtGui import (
	QIcon
)
from PyQt5.QtWidgets import (
	qApp,

	QAction,
	
	QAbstractItemView,
	QApplication,
	QCheckBox,
	QCalendarWidget,
	QComboBox,
	QCompleter,
	QDesktopWidget,
	QDialog,
	QFileDialog,
	QFileSystemModel,
	QFormLayout,
	QGraphicsDropShadowEffect,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QListView,
	QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMdiArea,
	QMessageBox,
	QMenu,
	QPlainTextEdit,
	QPushButton,
	QScrollArea,	
	QShortcut,
	QSizePolicy,
	QSlider,
	QSpacerItem,
	QSpinBox,
	QStatusBar,
	QStyle,
	QTextBrowser,
	QTextEdit,
	QToolBar,
	QToolTip,
	QVBoxLayout,
	QWidget,
	QRadioButton,
	QRubberBand,
)

def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, wratio=0, delta = 60):
	"""
	screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
	screenw, screenh = screen_geometry.width(), screen_geometry.height()
	resize_screen_ratio(w1, screenw, screenh, ratio=1/5)
	resize_screen_ratio(w2, screenw, screenh, ratio=1/5, wratio=1.0) # lebar sama dg screenw

	object hrs punya method resize dan move.
	"""
	if not wratio:
		wratio = ratio
	# print('wratio:', wratio)
	lebar, tinggi = int(screenw*wratio),int(screenh*ratio)
	object.resize(lebar, tinggi)
	posx = int((screenw-lebar)*posx_ratio)    
	posy = int((screenh - tinggi)/2) - delta
	object.move(posx, posy)

class AppDemo(QMainWindow):


	def onMyToolBarButtonClick(self, s):
		print("click", s)
		
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)

		toolbar = QToolBar("My main toolbar")
		self.addToolBar(toolbar)
		# new_action = QAction(QIcon("new.bmp"), "new", self)
		# new_action = QAction("new", self)
		# toolbar.addAction(new_action)
		button_action = QAction("Your button", self)
		button_action.setStatusTip("This is your button")
		button_action.triggered.connect(self.onMyToolBarButtonClick)
		toolbar.addAction(button_action)

		# self.setStatusBar(QStatusBar(self))
		self.statusBar().showMessage('Ready')

		exitAct = QAction(QIcon('exit.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit application')
		exitAct.triggered.connect(qApp.quit)
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAct)

		self.setWindowTitle("MDI Lengkap")
		
		screen_geometry = QDesktopWidget().screenGeometry(-1)
		self.sw, self.sh = screen_geometry.width(), screen_geometry.height()
		resize_screen_ratio(self, self.sw, self.sh, ratio=0.8)

		workspace = QMdiArea(self)
		workspace.resize(self.rect().width(), self.rect().height())

		self.calendar = QCalendarWidget()
		self.calendar.clicked.connect(lambda date: print(date.getDate()))
		workspace.addSubWindow(self.calendar)

		self.button = QPushButton('My Button')
		self.button.clicked.connect(lambda: print('button is clicked'))
		workspace.addSubWindow(self.button)

		textEditor = QTextEdit('text edit')
		workspace.addSubWindow(textEditor)

		workspace.addSubWindow(QLabel('label'))
		list_data = ['satu', 'dua', 'tiga', 'empat', 'lima']
		le = QLineEdit('lineedit')
		le.setCompleter(QCompleter(list_data))
		workspace.addSubWindow(le)
		workspace.addSubWindow(QPlainTextEdit('plain text edit'))
		workspace.addSubWindow(QGroupBox('group box'))
		cb = QComboBox()
		cb.addItems(list_data)
		workspace.addSubWindow(cb)
		workspace.addSubWindow(QSpinBox())
		workspace.addSubWindow(QCheckBox('check box'))
		workspace.addSubWindow(QRadioButton('radio button'))
		# https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QRubberBand.html
		workspace.addSubWindow(QRubberBand(QRubberBand.Rectangle))

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

	sys.exit(app.exec_())
#
