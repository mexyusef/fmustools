import pyperclip, sys, textwrap, time
import PyQt5
from PyQt5.Qt import * # noqa
from PyQt5.Qsci import QsciScintilla, QsciLexerCustom
from PyQt5.Qsci import (
	QsciLexerHTML, 
	QsciLexerCPP, 
	QsciLexerPerl,
	QsciLexerRuby, 
	# QsciLexerCoffeeScript, 
	# QsciLexerD, 
	QsciLexerPython, 
	# QsciLexerVerilog, 
	QsciLexerCSS,
	QsciLexerLua, 
	QsciLexerSQL, 
	# QsciLexerTCL, 
	# QsciLexerPascal, 
	# QsciLexerMarkdown,
	# QsciLexerPOV, 
	# QsciLexerVHDL, 
	# QsciLexerPostScript, 
	# QsciLexerFortran77, 
	QsciLexerBash,
	# QsciLexerAVS, 
	QsciLexerCMake,
	QsciLexerJSON,
	# QsciLexerPO, 
	# QsciLexerBatch, 
	# QsciLexerYAML,
	# QsciLexerXML,
	# QsciLexerSpice, 
	# QsciLexerMakefile, 
	# QsciLexerMatlab, 
	# QsciLexerProperties, 
	# QsciLexerDiff,
	# QsciLexerTeX, 
	QsciLexerCSharp,
	QsciLexerJavaScript,
	QsciLexerJava,
	# QsciLexerIDL
)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
	QApplication,
	QWidget,
	QTextEdit,
	QVBoxLayout,
	QPushButton,
	QLabel,
)
from PyQt5.QtCore import (
	Qt, 
	QTime, 
	QTimer
)
from .dirutils import bongkar, isfile
from .fileutils import file_content, file_write
from .utils import (
	env_get
)
from .showtext_editor import EditorAll

EXAMPLE_TEXT = textwrap.dedent("""\
class Solution
\
 """)

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

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.showTime)
		self.timer.start(100)

		self.showTime()

		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet(gaya)

		self.setWindowTitle("Digital Clock")
		self.resize(500, 60)

	def stop(self):
		self.timer.stop()

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


class ShowText(QWidget):
	def __init__(self, mode='text', parent=None):
		super().__init__(parent)

		self.tab = '&nbsp;'*4

		self.setWindowTitle("QTextEdit")
		# self.resize(1300, 800)
		self.resize(1200, 700)

		self.textEdit = QTextEdit()
		self.btnClose = QPushButton("OK")

		layout = QVBoxLayout()
		layout.addWidget(self.textEdit)
		layout.addWidget(self.btnClose)
		self.setLayout(layout)

		QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.on_Escape)

		if mode == 'html':
			kalimat = pyperclip.paste() \
				.replace('\n', '<br/>') \
				.replace(' ', '&nbsp;').replace('\t', self.tab)
			kalimat = '<pre>' + kalimat + '</pre>'
			self.textEdit.setHtml(f"<font color='red' size='6'><red>{kalimat}</font>")
		else:
			kalimat = pyperclip.paste()
			self.textEdit.setText(kalimat)

		self.btnClose.clicked.connect(QtWidgets.qApp.quit)
		# self.btnClose.clicked.connect(QtWidgets.qApp.closeAllWindows)

	@QtCore.pyqtSlot()
	def on_Escape(self):
		QtWidgets.qApp.quit()

	def event(self, event):
		"""
		https://stackoverflow.com/questions/62422643/moving-focus-to-next-qlineedit-using-enter
		"""
		if event.type() == QtCore.QEvent.KeyPress:
			if event.key() == QtCore.Qt.Key_Tab:
				self.focusNextPrevChild(True)
		return super().event(event)


class ExamWindow(QMainWindow): 
	def __init__(self, initial_text, filepath):
		super().__init__()
		self.file_path = filepath
		self.lexering = False
		self.setStyleSheet("background-color: grey;")
		self.setWindowTitle("Color") 

		self.editor = EditorAll(self)		
		self.editor.setWindowTitle(self.file_path)
		self.editor.setText(initial_text)
		# self.setCentralWidget(self.editor)
		vbox = QVBoxLayout()
		self.timer = BerbasisLabel()
		vbox.addWidget(self.timer, 10)
		vbox.addWidget(self.editor, 90)
		
		wid = QWidget(self)
		self.setCentralWidget(wid)
		wid.setLayout(vbox)

		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+P"), self, activated=self.onSetLexer)
		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, activated=self.onQuitApp)
		self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
		self.save_current_file_shortcut.activated.connect(self.save_current_file)

		# self.resize(1300, 800)
		self.resize(1200, 700)
		self.show()

	@QtCore.pyqtSlot()
	def onSetLexer(self):
		self.lexering = not self.lexering
		# print('lexer:', self.lexering)
		if self.lexering:
			font = QFont()
			font.setFamily('Courier')
			font.setFixedPitch(True)
			font.setPointSize(14)
			lexer = QsciLexerPython()
			lexer.setDefaultFont(font)
			self.editor.setLexer(lexer)
			# self.editor.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Courier')
		else:
			font = QFont()
			font.setFamily('Consolas')
			font.setFixedPitch(True)
			font.setPointSize(16)
			# font.setBold(True)
			self.editor.setFont(font)
			self.editor.setLexer(None)

	@QtCore.pyqtSlot()
	def onQuitApp(self):
		self.save_current_file()
		QtWidgets.qApp.quit()

	def save_current_file(self):
		if not self.file_path:
			new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Save this file as...", "", "All files (*)")
			if new_file_path:
				self.file_path = new_file_path
			else:
				# self.invalid_path_alert_message()
				return False

		# https://raw.githubusercontent.com/pycom/Pymakr/master/QScintilla/MiniEditor.py
		# file_contents = self.editor.toPlainText()
		file_contents = self.editor.text()
		file_write(self.file_path, file_contents)
		# with open(self.file_path, "w") as f:
		# 	f.write(file_contents)
		
		# self.title.setText(self.file_path)


class ImageEditor(QMainWindow):
	def get_image(self):
		import io, requests
		from PIL import Image
		from PyQt5.QtGui import QIcon, QPixmap
		alamat = 'https://source.unsplash.com/random'
		filename = '/tmp/download.jpg'
		gambar = io.BytesIO(requests.get(alamat).content)
		img = Image.open(gambar)
		img.save(filename)
		return filename

	def __init__(self, initial_text, file_path, image_path=None):
		super().__init__()
		self.file_path = file_path
		vbox = QVBoxLayout()

		self.setStyleSheet("background-color: grey;")
		self.setWindowTitle("ImageEditor")

		self.editor = EditorAll(self)
		self.editor.setWindowTitle(self.file_path)
		self.editor.setText(initial_text)

		if image_path:
			self.gambar = QPixmap(image_path)
		else:
			self.gambar = QPixmap(self.get_image())
		
		self.label = QLabel(self)
		self.label.setPixmap(self.gambar)
		self.scroll = QScrollArea()
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		# self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(True)
		self.scroll.setWidget(self.label)

		self.timer = BerbasisLabel()

		vbox.addWidget(self.scroll, 40)
		vbox.addWidget(self.timer, 7)
		vbox.addWidget(self.editor, 53)

		# self.setCentralWidget(self.editor)
		# self.setLayout(vbox)
		# https://stackoverflow.com/questions/37304684/qwidgetsetlayout-attempting-to-set-qlayout-on-mainwindow-which-already
		wid = QWidget(self)
		self.setCentralWidget(wid)
		wid.setLayout(vbox)

		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, activated=self.onQuitApp)
		self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
		self.save_current_file_shortcut.activated.connect(self.save_current_file)

		# self.resize(1300, 800)
		self.resize(1200, 700)
		# self.showMaximized()

	@QtCore.pyqtSlot()
	def onQuitApp(self):
		self.save_current_file()
		QtWidgets.qApp.quit()

	def save_current_file(self):
		if not self.file_path:
			new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Save this file as...", "", "All files (*)")
			if new_file_path:
				self.file_path = new_file_path
			else:
				# self.invalid_path_alert_message()
				return False

		# https://raw.githubusercontent.com/pycom/Pymakr/master/QScintilla/MiniEditor.py
		# file_contents = self.editor.toPlainText()
		file_contents = self.editor.text()
		file_write(self.file_path, file_contents)
		# with open(self.file_path, "w") as f:
		# 	f.write(file_contents)


class ShowTextWindow(QMainWindow):
	def __init__(self, title=None, filepath=None, images=[], content_from_clipboard=True, content_text=None):
		super().__init__()
		vbox = QVBoxLayout()
		self.setStyleSheet("background-color: grey;")
		self.setWindowTitle("Show Text Window")
		# vbox.addWidget(self.scroll, 40)
		self.editor = EditorAll(self)
		self.lexering = False
		if content_from_clipboard:
			initial_text = pyperclip.paste()
		elif filepath:
			# if not isfile(filepath):
			# 	filepath = bongkar(filepath)
			filepath = bongkar(filepath)
			initial_text = file_content(filepath)
		elif content_text is not None:
			initial_text = content_text
		self.editor.setWindowTitle("Show Text Window: Editor")
		self.editor.setText(initial_text)
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
		
		if images:
			jumlah = len(images)
			if jumlah == 1:
				image_path = images[0]
				self.gambar = QPixmap(image_path)
				self.label = QLabel(self)
				self.label.setPixmap(self.gambar)
			else:
				self.label = QWidget(self)
				vlayout = QVBoxLayout()
				for picture in images:
					gambar = QPixmap(picture)
					label_gambar = QLabel(self)
					label_gambar.setPixmap(gambar)
					vlayout.addWidget(label_gambar)
				self.label.setLayout(vlayout)

			self.scroll = QScrollArea()
			self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
			self.scroll.setWidgetResizable(True)
			self.scroll.setWidget(self.label)
			# vbox.addWidget(self.scroll, 10)
			# vbox.addWidget(self.editor, 83)
			geser_gambar_editor = QSplitter(Qt.Vertical)
			geser_gambar_editor.addWidget(self.scroll)
			geser_gambar_editor.addWidget(self.editor)
			# https://stackoverflow.com/questions/43831474/how-to-equally-distribute-the-width-of-qsplitter/43835396
			# https://stackoverflow.com/questions/29537762/pyqt-qsplitter-setsizes-usage
			# scroll 1 unit, editor 5 unit
			geser_gambar_editor.setStretchFactor(0, 1)
			geser_gambar_editor.setStretchFactor(1, 5)
			vbox.addWidget(geser_gambar_editor, 93)
		else:
			vbox.addWidget(self.editor, 93)

		wid = QWidget(self)
		self.setCentralWidget(wid)
		wid.setLayout(vbox)
		# ini dimakan editor
		# esc keluar tanpa save
		# q keluar dg save
		QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self, activated=QtWidgets.qApp.quit)
		# QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, activated=QtWidgets.qApp.quit)
		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+P"), self, activated=self.onSetLexer)
		QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, activated=self.onQuitApp)
		self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
		self.save_current_file_shortcut.activated.connect(self.save_current_file)
		self.resize(1200, 700)
		# self.showMaximized()

	@QtCore.pyqtSlot()
	def onSetLexer(self):
		self.lexering = not self.lexering
		print('lexer:', self.lexering)
		if self.lexering:
			font = QFont()
			font.setFamily('Courier')
			font.setFixedPitch(True)
			font.setPointSize(14)
			lexer = QsciLexerPython()
			lexer.setDefaultFont(font)
			self.editor.setLexer(lexer)
			# self.editor.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Courier')
		else:
			font = QFont()
			font.setFamily('Consolas')
			font.setFixedPitch(True)
			font.setPointSize(16)
			# font.setBold(True)
			self.editor.setFont(font)
			self.editor.setLexer(None)

	@QtCore.pyqtSlot()
	def onQuitApp(self):
		self.timer.timer.stop()
		self.save_current_file()
		QtWidgets.qApp.quit()

	def save_current_file(self):
		# if not self.file_path:
		# 	new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Save this file as...", "", "All files (*)")
		# 	if new_file_path:
		# 		self.file_path = new_file_path
		# 	else:
		# 		# self.invalid_path_alert_message()
		# 		return False

		# https://raw.githubusercontent.com/pycom/Pymakr/master/QScintilla/MiniEditor.py
		# file_contents = self.editor.toPlainText()
		if self.file_path:
			file_contents = self.editor.text()
			file_write(self.file_path, file_contents)
			# with open(self.file_path, "w") as f:
			# 	f.write(file_contents)


def image_editor(initial_text=EXAMPLE_TEXT, file_path=__file__):
	app = QApplication(sys.argv)
	window = ImageEditor(initial_text, file_path)
	sys.exit(app.exec_())
	# app.exec_()


def code_editor(initial_text=EXAMPLE_TEXT, filepath=__file__):
	app = QApplication(sys.argv)
	window = ExamWindow(initial_text, filepath)
	# sys.exit(app.exec_())
	app.exec_()


def main_process(filepath=None, title=None, images=[]):
	"""
	tampilkan isi filepath dan images di window (blocking view)
	belum berhasil set focus utk bbrp platform
	tapi sudah berhasil tampilkan on top
	"""
	app = QApplication(sys.argv)
	win = ShowTextWindow(title=title, filepath=filepath, images=images)

	############################
	# win.setFocus(True)
	win.raise_()
	win.setWindowFlags(win.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  # set always on top flag, makes window disappear
	win.show() # makes window reappear, but it's ALWAYS on top	
	# win.setWindowFlags(win.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
	# print('[showtext] activate main_process')
	win.activateWindow()
	# ini jadi error...di desktop
	# win.setWindowFlags(win.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
	############################


	app.exec_()


def show_content_window(title=None, content_text=None, filepath=None, images=[]):
	"""
	spt main_process di atas tetapi menerima text content alih2 filepath
	"""
	app = QApplication(sys.argv)
	win = ShowTextWindow(title=title, content_text=content_text, content_from_clipboard=False, filepath=filepath, images=images)
	############################
	# win.setFocus(True)
	win.raise_()
	win.setWindowFlags(win.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  # set always on top flag, makes window disappear
	win.show() # makes window reappear, but it's ALWAYS on top	
	# win.setWindowFlags(win.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
	# print('[showtext] activate main_process')
	win.activateWindow()
	############################
	app.exec_()


def show_file_window(filepath, title=None, images=[]):
	app = QApplication(sys.argv)
	win = ShowTextWindow(title=title, filepath=filepath, images=images, content_from_clipboard=False)
	############################
	# win.setFocus(True)
	win.raise_()
	win.setWindowFlags(win.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  # set always on top flag, makes window disappear
	win.show() # makes window reappear, but it's ALWAYS on top
	# win.setWindowFlags(win.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
	# print('[showtext] activate main_process')
	win.activateWindow()
	############################
	app.exec_()


if __name__ == '__main__':
	image_editor()
