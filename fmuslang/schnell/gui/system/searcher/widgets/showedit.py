# import os, sys
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([sidoarjodir, schnelldir])

# from app.showtext_editor import EditorAll
# from app.utils import env_get
# from app.fileutils import file_content

from PyQt5.Qt import QMainWindow, QShortcut, QKeySequence, QGridLayout
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

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

class EditorAll(QsciScintilla):

	def __init__(self, parent=None, fontsize=14, compact=False):
		super().__init__(parent)

		self.setEolMode(QsciScintilla.EolUnix)
		
		font = QFont()
		font.setFamily('Candara' if compact else 'Consolas')
		font.setFixedPitch(True)
		font.setPointSize(fontsize)
		# font.setBold(True)
		self.setFont(font)

		# Set margin defaults
		fontmetrics = QFontMetrics(font)
		self.setMarginsFont(font)
		self.setMarginWidth(0, fontmetrics.width("000") + 2 if compact else 6)
		self.setMarginLineNumbers(0, True)
		self.setMarginsForegroundColor(QColor(128, 128, 128))
		self.setMarginsBackgroundColor(QColor(39, 40, 34))
		self.setMarginType(1, self.SymbolMargin)
		self.setMarginWidth(1, 5 if compact else 12)

		# Set indentation defaults
		self.setIndentationsUseTabs(False)
		self.setIndentationWidth(2)
		self.setTabWidth(2)
		self.setBackspaceUnindents(True)
		self.setIndentationGuides(True)

		# self.setFolding(QsciScintilla.CircledFoldStyle)

		# Set caret defaults
		self.setCaretForegroundColor(QColor(75, 27, 0xe8))
		self.setCaretWidth(5)

		# Set selection color defaults
		self.setSelectionBackgroundColor(QColor(61, 61, 52))
		self.resetSelectionForegroundColor()

		# Set multiselection defaults
		self.SendScintilla(QsciScintilla.SCI_SETMULTIPLESELECTION, True)
		self.SendScintilla(QsciScintilla.SCI_SETMULTIPASTE, 1)
		self.SendScintilla(QsciScintilla.SCI_SETADDITIONALSELECTIONTYPING, True)

		if not compact:
			# Set the text wrapping mode to word wrap			
			self.setWrapMode(QsciScintilla.WrapWord)
			# Set the text wrapping mode visual indication
			self.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
			# Set the text wrapping to indent the wrapped lines
			self.setWrapIndentMode(QsciScintilla.WrapIndentSame)

		# lexer = LexerJson(self)
		# self.setLexer(lexer)

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


class ShowEditWindow(QMainWindow):

	quit_signal = pyqtSignal(str)  # berikan content file

	def __init__(self, filepath=None, title=None, initial_text='', compact=False):
		super().__init__()
		vbox = QVBoxLayout()
		self.setStyleSheet("background-color: grey;")
		self.setWindowTitle("Show Text Window")
		self.editor = EditorAll(self, fontsize=10 if compact else 14, compact=compact)
		self.editor.setWindowTitle(title)
		self.editor.setText(initial_text)
		vbox = QVBoxLayout()
		self.timer = BerbasisLabel()

		self.file_path = filepath

		if not compact:
			if title:
				labels = QWidget(self)
				grid = QGridLayout()
				judul = QLabel(title)
				# judul.setStyleSheet('color: yellow')
				judul.setStyleSheet('background-color: black; color: yellow')
				# gaya = env_get('ULIBPY_SHOWTEXT_TITLE_STYLE')
				# if gaya:
				# 	judul.setStyleSheet(gaya)
				grid.addWidget(judul, 0, 0)
				grid.addWidget(self.timer, 1, 0)
				labels.setLayout(grid)
				vbox.addWidget(labels, 7)
			else:
				vbox.addWidget(self.timer, 7)

			vbox.addWidget(self.timer, 10)

		vbox.addWidget(self.editor, 90)		
		wid = QWidget(self)
		self.setCentralWidget(wid)  # kunci
		wid.setLayout(vbox)

		# cara keluar: escape, close x, ctrl+w
		QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.keluar_exec_fmus)
		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, activated=self.keluar_exec_fmus)
		# self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
		# self.save_current_file_shortcut.activated.connect(self.keluar_exec_fmus)

		self.resize(1200, 700)

	def set_info(self, filepath=None, content=None):
		if filepath:
			self.file_path = filepath
		if content:
			self.editor.setText(content)

	def closeEvent(self, event):
		self.keluar_exec_fmus()

	@QtCore.pyqtSlot()
	def keluar_exec_fmus(self):
		self.save_current_file()
		content = self.editor.text() + '\n'
		# print('\n', '-'*10)
		# print('showedit:', content)
		# print('good luck!')
		self.quit_signal.emit(content)  # parent tentukan what to do with this widget
		self.hide()

	def save_current_file(self):
		if self.file_path:
			file_contents = self.editor.text()
			with open(self.file_path, "w", encoding='utf8') as f:
				f.write(file_contents)


# def editor(filepath=__file__, title='Fmus Coder', initial_text=''):
# 	app = QApplication(sys.argv)
# 	win = ShowEditWindow(filepath, title=title, initial_text=initial_text)
# 	win.show()
# 	app.exec_()
# 	return file_content(filepath)


# if __name__ == '__main__':
#   editor()
