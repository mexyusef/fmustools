#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import os, sys, traceback
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QStackedWidget, QHBoxLayout, QListWidgetItem, QLabel

from PyQt5.Qsci import QsciScintilla, QsciLexerJSON, QsciLexerPython
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from dotenv import load_dotenv

envfile = "c:/users/usef/work/sidoarjo/schnell/.env"

load_dotenv(envfile)
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
schnelldir = os.environ['ULIBPY_BASEDIR']
sys.path.extend([sidoarjodir, schnelldir])

print(sidoarjodir, schnelldir)

from app.transpiler.frontend.main import process_language
from app.printutils import indah4
from app.fileutils import file_write, get_daftar

helpfile = os.path.join(sidoarjodir, 'database/refcards/pyqt5.mk')
daftar = get_daftar(helpfile)
print('daftar:\n', daftar)

class CodeScintilla(QsciScintilla):

    def __init__(self, *args, **kwargs):
        super(CodeScintilla, self).__init__(*args, **kwargs)
        self.init()
        self.linesChanged.connect(self.onLinesChanged)

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + 6)

    def init(self):
        self.setUtf8(True)

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
        self.setMarginWidth(0, self.fontmetrics.width(str(self.lines())) + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("gainsboro"))
        self.setMarginWidth(1, 0)
        self.setMarginWidth(2, 14)  # folded area

        # Bind autocompletion hotkey Alt+/
        completeKey = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Slash), self)
        completeKey.setContext(Qt.WidgetShortcut)
        completeKey.activated.connect(self.autoCompleteFromAll)

class ListStackedWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(ListStackedWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # Left and right layout(A QListWidget on the left + Right QStackedWidget)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # left list
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # Right Cascading Window
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)
        self.initUi()

    def initUi(self):
        # Initialize the interface
        # Switch the serial number in QStackedWidget through the current item change of QListWidget
        # jk list ganti item, maka stack ganti content
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        # remove border
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # hide scrollbar
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.buatWidgets()

    def buatWidgets(self):
        # Here we use the general text with the icon mode.(You can also use Icon mode directly,setViewMode)
        for i in range(20):
            item = QListWidgetItem(QIcon('Data/0%d.ico' % randint(1, 8)), str('select item %s' % i), self.listWidget)
            # Set the default width and height of the item(Only height is useful here)
            item.setSizeHint(QSize(16777215, 60))
            # center text
            item.setTextAlignment(Qt.AlignCenter)

        # Simulate 20 more pages on the right(It won't be looped together with the above.)
        for i in range(20):
            # label = QLabel('i am page %d' % i, self)
            # label.setAlignment(Qt.AlignCenter)
            # # Set the background color of the label(random here)
            # # A margin is added here(It is convenient to distinguish the color of QStackedWidget and QLabel)
            # label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
            #     randint(0, 255), randint(0, 255), randint(0, 255)))
            label = CodeScintilla()
            label.setText(f"code nomor {i}")
            self.stackedWidget.addWidget(label)


# Beautify the style sheet
stackedwidget_stylesheet = """
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}
/*被选中时的背景颜色和左边框颜色*/
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
/*鼠标悬停颜色*/
HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

/*右侧的层叠窗口的背景颜色*/
QStackedWidget {
    background: rgb(30, 30, 30);
}
/*模拟的页面*/
QLabel {
    color: white;
}
"""

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stackedwidget_stylesheet)
    w = ListStackedWidget()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
