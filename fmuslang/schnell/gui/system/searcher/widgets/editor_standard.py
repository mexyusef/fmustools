from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *



class EditorStandard(QsciScintilla):

    save_file = pyqtSignal(bool)

    def __init__(self, parent=None, lexer='py', *args, **kwargs):
        super(EditorStandard, self).__init__(parent, *args, **kwargs)
        self.margin = 24
        self.lexer = lexer
        self.init()
        self.linesChanged.connect(self.onLinesChanged)

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + self.margin)

    def init(self):
        self.setUtf8(True)

        lexer = QsciLexerPython(self)
        if self.lexer=='md':
            lexer = QsciLexerMarkdown(self)
        self.setLexer(lexer)
        self.setEolMode(QsciScintilla.EolUnix)
        self.setAutoCompletionCaseSensitivity(False)  # ignore case
        self.setAutoCompletionSource(self.AcsAll)
        self.setAutoCompletionThreshold(1)  # One character pops up completion
        self.setAutoIndent(True)  # auto indent
        self.setBackspaceUnindents(True)
        self.setBraceMatching(self.StrictBraceMatch)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setTabWidth(4)
        self.setWhitespaceSize(1)
        self.setWhitespaceVisibility(self.WsVisible)
        self.setWhitespaceForegroundColor(Qt.gray)
        self.setWrapIndentMode(self.WrapIndentFixed)
        self.setWrapMode(self.WrapWord)

        # fold
        # https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
        self.setFolding(self.BoxedTreeFoldStyle, 2)
        self.setFoldMarginColors(QColor("#676A6C"), QColor("#676A6D"))
        font = self.font() or QFont()
        font.setFamily("Hack")
        font.setFixedPitch(True)
        font.setPointSize(12)
        self.setFont(font)
        self.setMarginsFont(font)
        self.fontmetrics = QFontMetrics(font)
        lexer.setFont(font)

        self.setMarginWidth(0, self.fontmetrics.width(str(self.lines())) + self.margin)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("gainsboro"))
        self.setMarginWidth(1, 0)
        self.setMarginWidth(2, 14) # folded area

        # Bind autocompletion hotkey Alt+/
        completeKey = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Slash), self)
        completeKey.setContext(Qt.WidgetShortcut)
        completeKey.activated.connect(self.autoCompleteFromAll)

        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
        # self.foldAll()
        QShortcut(QKeySequence("Ctrl+L"), self, activated=lambda: self.foldAll)
        QShortcut(QKeySequence("Ctrl+S"), self, activated=lambda: self.save_file.emit(True))
