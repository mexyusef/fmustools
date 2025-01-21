from PyQt5 import QtWidgets, QtCore, QtGui
import PyQt5
from PyQt5.Qt import *  # noqa
from PyQt5.Qsci import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import pyperclip, sys, textwrap


# https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html#a8010e1671a15976254fd11b59ca3e03d
class EditorAll(QsciScintilla):

	def __init__(self, parent=None):
		super().__init__(parent)

		self.setEolMode(QsciScintilla.EolUnix)

		# Set font defaults
		font = QFont()
		font.setFamily('Consolas')
		font.setFixedPitch(True)
		font.setPointSize(16)
		# font.setBold(True)
		self.setFont(font)

		# Set margin defaults
		fontmetrics = QFontMetrics(font)
		self.setMarginsFont(font)
		self.setMarginWidth(0, fontmetrics.width("000") + 6)
		self.setMarginLineNumbers(0, True)
		self.setMarginsForegroundColor(QColor(128, 128, 128))
		self.setMarginsBackgroundColor(QColor(39, 40, 34))
		self.setMarginType(1, self.SymbolMargin)
		self.setMarginWidth(1, 12)

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

		# https://stackoverflow.com/questions/42329818/how-to-use-autocomplete-using-qscintilla-and-c
		"""
		Customization - LINE WRAPPING
		https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
		enum WrapMode {
			WrapNone = SC_WRAP_NONE, 
			WrapWord = SC_WRAP_WORD, 
			WrapCharacter = SC_WRAP_CHAR,
			WrapWhitespace = SC_WRAP_WHITESPACE
		}

		enum WrapVisualFlag {
			WrapFlagNone, 
			WrapFlagByText, 
			WrapFlagByBorder,
			WrapFlagInMargin
		}

		enum WrapIndentMode { 
			WrapIndentFixed = SC_WRAPINDENT_FIXED, 
			WrapIndentSame = SC_WRAPINDENT_SAME, 
			WrapIndentIndented = SC_WRAPINDENT_INDENT 
		}
		"""
		# Set the text wrapping mode to word wrap
		self.setWrapMode(QsciScintilla.WrapWord)
		# Set the text wrapping mode visual indication
		self.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
		# Set the text wrapping to indent the wrapped lines
		self.setWrapIndentMode(QsciScintilla.WrapIndentSame)

		# lexer = LexerJson(self)
		# self.setLexer(lexer)
