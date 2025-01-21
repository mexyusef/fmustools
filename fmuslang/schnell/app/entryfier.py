import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from .fileutils import (
	entrify_blocks,
	write_list
)
from .utils import (
	env_get
)

class FileDirChooser(QWidget):

	def __init__(self, basedir=None):
		super().__init__()
		self.initUI()
		self.basedir = os.getcwd() # GENERATED_DIR # str(Path.home())
		if basedir:
			self.basedir = basedir

	def initUI(self):
		# self.statusBar()
		# self.setGeometry(300, 300, 550, 450)
		# self.setWindowTitle('File dialog')
		self.show()

	def chooseDirDialog(self, basedir=None):
		basedir = self.basedir if not basedir else basedir
		file = str(QFileDialog.getExistingDirectory(self, "Select Directory", basedir))
		return file

	def chooseOpenDialog(self, basedir=None):
		if basedir:
			self.basedir = basedir
		else:
			basedir = self.basedir
		
		fname = QFileDialog.getOpenFileName(self, 'Open file', basedir)
		if fname[0]:
			return fname[0]

		return None

	def chooseSaveDialog(self, basedir=None):
		basedir = self.basedir if not basedir else basedir
		fname = QFileDialog.getSaveFileName(self, 'Save file', basedir)
		if fname[0]:
			return fname[0]
			
		return None

class Generator:
	def __init__(self):
		self.basedir = '/tmp'

	def ask_with_qt(self, basedir=None):
		app = QApplication(sys.argv)
		ex = FileDirChooser()

		self.openfile = ex.chooseOpenDialog(basedir)
		print(self.openfile)
		self.savefile = ex.chooseSaveDialog()
		print(self.savefile)

		app.exec()
		ex.close()
		app.quit()

		print('Got:', self.openfile, 'into:', self.savefile)
		self.reverse_fm()

	def reverse_fm(self):
		if self.openfile and self.savefile:
			entries = entrify_blocks(self.openfile)
			if entries:
				write_list(self.savefile, entries, '\n'*2)
