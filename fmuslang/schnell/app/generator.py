import os, sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

from PyQt5.QtWidgets import (qApp, QMainWindow, QTextEdit, QAction)
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

from .dirutils import (
	ayah, abs_dir, joiner, here
)
from .definitor import BaseDefinitor
from .utils import trycopy


GENERATED_DIR = joiner(abs_dir(__file__), 'codes', 'additional', 'misc', 'generated')
if 'ULIBPY_WMC_GENDIR' in os.environ:
	GENERATED_DIR = os.environ.get('ULIBPY_WMC_GENDIR')

class FileDirChooser(QWidget):

	def __init__(self, basedir=None):
		super().__init__()
		self.initUI()
		self.basedir = GENERATED_DIR # str(Path.home())
		if basedir:
			self.basedir = basedir

		# QCoreApplication.quit()
		# QCoreApplication.exit(0)
		# qApp.quit()
		# app.quit()

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
		basedir = self.basedir if not basedir else basedir
		fname = QFileDialog.getOpenFileName(self, 'Open file', basedir)
		if fname[0]:
			return fname[0]

		return None

	def chooseSaveDialog(self, basedir=None):
		"""
		jk specify basedir maka save ke basedir
		else gunakan ULIBPY GENERATED DIR
		"""
		basedir = self.basedir if not basedir else basedir
		fname = QFileDialog.getSaveFileName(self, 'Save file', basedir)
		if fname[0]:
			return fname[0]
			
		return None


# The following keyword arguments are applicable to the classes and functions listed below:
#   parent - the window to place the dialog on top of
#   title - the title of the window
#   initialdir - the directory that the dialog starts in
#   initialfile - the file selected upon opening of the dialog
#   filetypes - a sequence of (label, pattern) tuples, ‘*’ wildcard is allowed
#   defaultextension - default extension to append to file (save dialogs)
#   multiple - when true, selection of multiple items is allowed

# tkinter.filedialog.asksaveasfilename()
# tkinter.filedialog.asksaveasfile()
# tkinter.filedialog.askopenfilename()
# tkinter.filedialog.askopenfile()
# tkinter.filedialog.askdirectory()
# tkinter.filedialog.askopenfilenames()
# tkinter.filedialog.askopenfiles()

# def callback():
#   name = filedialog.askopenfilename()
#   print(name)
		
# errmsg = 'Error!'
# tk.Button(text='Click to Open File', command=callback).pack(fill=tk.X)
# tk.mainloop()


class ChooserDialog(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 file dialogs - pythonspot.com'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.openFileNameDialog()
		self.openFileNamesDialog()
		# self.saveFileDialog()
		
		self.show()
	
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			print(fileName)
	
	def openFileNamesDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
		if files:
			print(files)
	
	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
		if fileName:
			print(fileName)

	def result(self):
		return self.result


class Generator:
	def __init__(self):
		# self.basedir = os.getcwd()
		self.basedir = '/tmp'
		# self.gendir = '/home/usef/danger/ulib/upy/ulibpy/xcurse/codes/additional/misc/generated/'
		self.gendir = GENERATED_DIR
		self.choosedir = None
		self.savefile = None

	def callback(self):
		self.choosedir = filedialog.askdirectory()
		# print(self.choosedir)

	def dialog_directory(self, basedir=None):
		app = QApplication(sys.argv)
		ex = FileDirChooser()
		pilih = ex.chooseDirDialog(basedir)
		print(pilih)
		ex.close()
		app.quit()
		# return pilih

	def dialog_open_file(self, basedir=None):
		app = QApplication(sys.argv)
		ex = FileDirChooser()
		pilih = ex.chooseOpenDialog(basedir)
		# print(pilih)
		for_use = f"filepath = '{pilih}'"
		print(for_use)
		trycopy(for_use)
		ex.close()
		app.quit()
		# return pilih
		
	def dialog_save_file(self, basedir=None):
		app = QApplication(sys.argv)
		ex = FileDirChooser()
		pilih = ex.chooseSaveDialog(basedir)
		print(pilih)
		ex.close()
		app.quit()
		# return pilih

	def ask_with_qt(self, basedir=None, use_same_folder_for_generated=False):
		app = QApplication(sys.argv)
		ex = FileDirChooser()

		self.choosedir = ex.chooseDirDialog(basedir)
		print('opendir:', self.choosedir)

		if use_same_folder_for_generated:
			self.savefile = ex.chooseSaveDialog(basedir)
		else:
			self.savefile = ex.chooseSaveDialog()

		print('savedir', self.savefile)

		# self.savefile = ex.chooseOpenDialog(basedir)
		# print(self.savefile)

		app.exec()
		ex.close()
		app.quit()

		print('Got:', self.choosedir, 'into:', self.savefile)
		self.reverse_fm()

	@staticmethod
	def opendir(basedir=None):
		if not basedir:
			basedir = os.getcwd()
		app = QApplication(sys.argv)
		ex = FileDirChooser()
		choosedir = ex.chooseDirDialog(basedir)
		print(choosedir)
		app.exec()
		ex.close()
		app.quit()
		print('Got:', choosedir)

	@staticmethod
	def openfile(basedir=None):
		if not basedir:
			basedir = os.getcwd()
		app = QApplication(sys.argv)
		ex = FileDirChooser()
		choosefile = ex.chooseOpenDialog(basedir)
		print(choosefile)
		app.exec()
		ex.close()
		app.quit()
		print('Got:', choosefile)
		return choosefile


	def reverse_fm(self):
		if self.choosedir and self.savefile:
			from .reversefm import ReverseFM
			revver = ReverseFM()
			revver.walkgen(self.choosedir, self.savefile)

	def ask(self):
		# os.chdir(self.basedir)
		# tk.Button(text='Choose directory', command=self.callback).pack(fill=tk.X)
		self.choosedir = filedialog.askdirectory(initialdir=self.basedir)
		# os.chdir(self.gendir)
		self.savefile = filedialog.asksaveasfilename(initialdir=self.gendir)
		tk.mainloop()
		print('Got:', self.choosedir, 'into:', self.savefile)
		self.reverse_fm()
		# if self.choosedir and self.savefile:
		# 	revver = ReverseFM()
		# 	revver.walkgen(self.choosedir, self.savefile)

if __name__ == '__main__':
	# Generator().ask()
	# Generator().ask_with_qt()
	Generator().dialog_open_file('/home/usef/tc/resources')
	input('Press any key to protect clipboard...')
