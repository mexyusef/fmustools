import pyperclip, sys, textwrap, time
import PyQt5
from PyQt5.Qsci import QsciScintilla, QsciLexerCustom
from PyQt5.Qsci import (
	# QsciLexerHTML,
	# QsciLexerCPP,
	# QsciLexerPerl,
	# QsciLexerRuby,
	# QsciLexerCoffeeScript,
	# QsciLexerD,
	QsciLexerPython,
	# QsciLexerVerilog,
	# QsciLexerCSS,
	# QsciLexerLua,
	# QsciLexerSQL,
	# QsciLexerTCL,
	# QsciLexerPascal,
	# QsciLexerMarkdown,
	# QsciLexerPOV,
	# QsciLexerVHDL,
	# QsciLexerPostScript,
	# QsciLexerFortran77,
	# QsciLexerBash,
	# QsciLexerAVS,
	# QsciLexerCMake,
	# QsciLexerJSON,
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
	# QsciLexerCSharp,
	# QsciLexerJavaScript,
	# QsciLexerJava,
	# QsciLexerIDL
)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
	QApplication,
    QLabel,
	QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import (
	Qt,
	QTime,
	QTimer,
)
# from PyQt5.Qt import * # noqa
from PyQt5.Qt import (
    QFont,
    QGridLayout,
    QMainWindow,
    QPixmap,
    QScrollArea,
    QKeySequence,
    QShortcut,
    QSplitter,
)

from .dirutils import isfile
from .fileutils import file_content, file_write
from .printutils import indah4
from .showtext_editor import EditorAll
from .utils import env_get


unit = 10 # 1/10 detik
sedetik = 1*unit
semenit = 60*sedetik
sejam = 60*semenit
LEBAR = 1980
TINGGI = 800
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
		self.history = []

		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(100)

		self.showTime()

		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet(gaya)

		self.setWindowTitle("Digital Clock")
		# self.resize(500, 60)

	def resetCounter(self):
		self.counter = 0

	def saveCounter(self):
		text = self.counterToText(self.counter)
		self.history.append(text)

	def counterToText(self, counter):
		text = str(counter)
		jam = "00"
		menit = "00"
		detik = "00"
		if counter >= sejam:
			jam = counter // sejam
			jam = str(jam).zfill(2)
			menit = (counter % sejam) // semenit
			menit = str(menit).zfill(2)
			detik = ((counter % sejam) % semenit) // sedetik
			detik = str(detik).zfill(2)
			desi = ((counter % sejam) % semenit) % sedetik
			desi = str(desi) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		elif counter >= semenit:
			# jam = "00"
			menit = counter // semenit
			menit = str(menit).zfill(2)
			detik = (counter % semenit) // sedetik
			detik = str(detik).zfill(2)
			desi = (counter % semenit) % sedetik
			desi = str(desi) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		elif counter >= sedetik:
			# jam = "00"
			# menit = "00"
			detik = counter // sedetik
			detik = str(detik).zfill(2)
			desi = counter % sedetik
			desi = str(desi) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		else:
			# jam = "00"
			# menit = "00"
			# detik = "00"
			desi = str(counter) # .zfill(2)
			text = f"{jam}:{menit}:{detik}:{desi}"
		return text

	def showTime(self):
		self.counter += 1
		text = self.counterToText(self.counter)
		self.setText(text)


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
		elif content_text is not None:
			initial_text = content_text
		elif filepath and isfile(filepath):
			initial_text = file_content(filepath)
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
		self.resize(LEBAR, TINGGI)
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
			# indah4(f'''[showtextwindow]
			# menyimpan content [{file_contents[:100]}...] ke file {self.file_path}
			# ''', warna='white')


def showtextwindow(filepath=None, title=None, images=[], content_from_clipboard=True, content_text=None):
	"""
    asumsikan images adlh daftar filename yg bisa ditemukan di "curdir"
        func = show_file_window if show_file else main_process
        args = {
            'title': title,
        }
        if images:
            args.update({
                'images': images,
            })
        if show_file:
            args.update({
                'filepath': filepath,
            })
        func(**args)

	tampilkan isi filepath dan images di window (blocking view)
	belum berhasil set focus utk bbrp platform
	tapi sudah berhasil tampilkan on top
	"""
	app = QApplication(sys.argv)
	win = ShowTextWindow(title=title, filepath=filepath, images=images, content_from_clipboard=content_from_clipboard, content_text=content_text)

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
