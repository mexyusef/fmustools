import os, sys, traceback, textwrap

from PyQt5.QtCore import (
    Qt, 
    QSize,
)
# from PyQt5.QtCore import *
from PyQt5.QtGui import (
    QColor,
    QIcon,
    QFont,
    QFontMetrics,
    QKeySequence,
)
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    qApp,
    QApplication, 
    QDesktopWidget, 
    QHBoxLayout, 
    QListWidget,
    QListWidgetItem, 
    QLabel,
    QShortcut,
    QStackedWidget,
    QWidget,
)
# from PyQt5.QtWidgets import *
from PyQt5.Qsci import (
    QsciScintilla, 
    QsciLexerJSON, 
    QsciLexerPython, 
    QsciLexerMarkdown,
)


# from dotenv import load_dotenv
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# load_dotenv(envfile)
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir="c:/users/usef/work/sidoarjo"
sys.path.extend([sidoarjodir])

# print(sidoarjodir, schnelldir)

from schnell.app.transpiler.frontend.main import process_language
from schnell.app.printutils import indah4
from schnell.app.dirutils import files_filter
from schnell.app.fileutils import file_write, get_daftar, file_content, get_definition_by_key_permissive_start


stackedwidget_stylesheet = """
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}

QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}

QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}

HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

QStackedWidget {
    background: rgb(30, 30, 30);
}

QLabel {
    color: white;
}
"""


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, wratio=0, delta = 60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

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


class CodeScintilla(QsciScintilla):

    def __init__(self, *args, **kwargs):
        super(CodeScintilla, self).__init__(*args, **kwargs)
        self.margin = 24
        self.init()
        self.linesChanged.connect(self.onLinesChanged)
        

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + self.margin)

    def init(self):
        self.setUtf8(True)

        # lexer = QsciLexerMarkdown(self)
        lexer = QsciLexerPython(self)
        self.setLexer(lexer)

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
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(13)
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

        QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
        # self.foldAll()


def editor_nonmain(filepath=None):
    w = CodeScintilla()
    if filepath:
        w.setText(file_content(filepath))
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=0.8, wratio=1.0)
    # https://stackoverflow.com/questions/12118939/how-to-make-a-pyqt4-window-jump-to-the-front
    w.raise_()
    w.show()

def editor_main(filepath=None):
    app = QApplication(sys.argv)
    app.setStyleSheet(stackedwidget_stylesheet)
    w = CodeScintilla()
    if filepath:
        w.setText(file_content(filepath))
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=0.8, wratio=1.0)
    # https://stackoverflow.com/questions/12118939/how-to-make-a-pyqt4-window-jump-to-the-front
    w.raise_()
    w.show()
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    editor_main()
