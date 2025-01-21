import os, sys                                                                                                            

# schnelldir = '/home/usef/danger/ulib/schnell'
curdir = os.path.dirname(__file__)
schnelldir = os.path.join(curdir, '../../..')
sys.path.extend([schnelldir, '..'])

from app.showtext_editor import EditorAll
from app.utils import env_get
from app.fileutils import file_content

from PyQt5.Qt import QMainWindow, QShortcut, QKeySequence, QGridLayout
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

unit = 10 # 1/10 detik
sedetik = 1*unit
semenit = 60*sedetik
sejam = 60*semenit

gaya = """
font-family: sans-serif;
color: #ffffff;
font-size: 32px;
background-color: #000000;
"""


class BerbasisLabel(QLabel):
	def __init__(self, parent=None):
		super(BerbasisLabel, self).__init__(parent)

		self.counter = 0

		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(100)

		self.showTime()

		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet(gaya)

		self.setWindowTitle("Digital Clock")
		self.resize(500, 60)

	def showTime(self):
		self.counter += 1
		text = str(self.counter)
		jam = "00"
		menit = "00"
		detik = "00"
		if self.counter >= sejam:
			jam = self.counter // sejam
			jam = str(jam).zfill(2)
			menit = (self.counter % sejam) // semenit
			menit = str(menit).zfill(2)
			detik = ((self.counter % sejam) % semenit) // sedetik
			detik = str(detik).zfill(2)
			desi = ((self.counter % sejam) % semenit) % sedetik
			desi = str(desi) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		elif self.counter >= semenit:
			# jam = "00"
			menit = self.counter // semenit
			menit = str(menit).zfill(2)
			detik = (self.counter % semenit) // sedetik
			detik = str(detik).zfill(2)
			desi = (self.counter % semenit) % sedetik
			desi = str(desi) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		elif self.counter >= sedetik:
			# jam = "00"
			# menit = "00"
			detik = self.counter // sedetik
			detik = str(detik).zfill(2)
			desi = self.counter % sedetik
			desi = str(desi) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		else:
			# jam = "00"
			# menit = "00"
			# detik = "00"
			desi = str(self.counter) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"

		self.setText(text)


class ShowTextWindow(QMainWindow):
	def __init__(self, filepath=None, title=None, initial_text=''):
		super().__init__()
		vbox = QVBoxLayout()
		self.setStyleSheet("background-color: grey;")
		self.setWindowTitle("Show Text Window")
		self.editor = EditorAll(self)		
		self.editor.setWindowTitle(title)
		self.editor.setText(initial_text)
		vbox = QVBoxLayout()
		self.timer = BerbasisLabel()

		self.file_path = filepath
		if title:
			labels = QWidget(self)
			grid = QGridLayout()
			judul = QLabel(title)
			# judul.setStyleSheet('color: yellow')
			judul.setStyleSheet('background-color: black; color: yellow')
			gaya = env_get('ULIBPY_SHOWTEXT_TITLE_STYLE')
			if gaya:
				judul.setStyleSheet(gaya)
			grid.addWidget(judul, 0, 0)
			grid.addWidget(self.timer, 1, 0)
			labels.setLayout(grid)
			vbox.addWidget(labels, 7)
		else:
			vbox.addWidget(self.timer, 7)

		vbox.addWidget(self.timer, 10)
		vbox.addWidget(self.editor, 90)
		
		wid = QWidget(self)
		self.setCentralWidget(wid) # kunci
		wid.setLayout(vbox)

		# QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self, activated=QtWidgets.qApp.quit)
		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, activated=self.onQuitApp)
		self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
		self.save_current_file_shortcut.activated.connect(self.save_current_file)

		self.resize(1200, 700)
		self.show()

	@QtCore.pyqtSlot()
	def onQuitApp(self):
		self.save_current_file()
		QtWidgets.qApp.quit()

	def save_current_file(self):
		if self.file_path:
			file_contents = self.editor.text()
			with open(self.file_path, "w") as f:
				f.write(file_contents)


def editor(filepath=__file__, title='Fmus Coder', initial_text=''):
	app = QApplication(sys.argv)
	win = ShowTextWindow(filepath, title=title, initial_text=initial_text)
	win.show()
	app.exec_()
	return file_content(filepath)


if __name__ == '__main__':
  editor()
