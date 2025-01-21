import os, sys, traceback, textwrap
# from PyQt5.QtCore import (
#     Qt, 
#     QSize,
# )
from PyQt5.QtCore import *
# from PyQt5.QtGui import (
#     QColor,
#     QIcon,
#     QFont,
#     QFontMetrics,
#     QKeySequence,
# )
from PyQt5.QtGui import *
# from PyQt5.QtWidgets import (
#     qApp,
#     QApplication, 
#     QDesktopWidget, 
#     QHBoxLayout, 
#     QListWidget,
#     QListWidgetItem, 
#     QLabel,
#     QShortcut,
#     QStackedWidget,
#     QWidget,
# )
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *
# from PyQt5.Qsci import (
#     QsciScintilla, 
#     QsciLexerJSON, 
#     QsciLexerPython, 
#     QsciLexerMarkdown,
# )


sidoarjodir="c:/users/usef/work/sidoarjo"
sys.path.extend([sidoarjodir])

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
BACKGROUND_COLOR = '#f3f3e0'
UKURAN_FONT = 8

class FmusEditor(QsciScintilla):

    def __init__(self, *args, **kwargs):
        super(FmusEditor, self).__init__(*args, **kwargs)
        self.margin = 10

        # self.setStyleSheet('background-color:'+ BACKGROUND_COLOR +';')
        self.setPaper(QColor(BACKGROUND_COLOR))

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
        font.setPointSize(UKURAN_FONT)
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

# from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
# from PyQt5.QtCore import Qt, QMimeData, pyqtRemoveInputHook
def message_handler(type, context, message):
    # # Suppress the specified warning message
    if "Retrying to obtain clipboard" not in message:
        sys.__stdout__.write(message)
    # pass

class FmusEditorWrapper(QWidget):
    def __init__(self, parent=None):
        # super().__init__()
        super().__init__(parent)

        # # Redirect warning messages to the custom message handler
        # sys.stdout.write = sys.__stdout__.write
        # sys.stderr.write = sys.__stderr__.write
        # sys.__stdout__.write = message_handler

        # Install the custom message handler
        qInstallMessageHandler(message_handler)

        self.initUI()

    def initUI(self):
        self.editor = FmusEditor(self)

        self.monitorButton = QPushButton('Start Monitoring', self)
        self.monitorButton.setStyleSheet("background-color: green;")
        self.monitorButton.clicked.connect(self.toggleMonitoring)

        # Create a layout to arrange the text edit, button, and optional spacer
        layout = QVBoxLayout()
        layout.addWidget(self.monitorButton)
        layout.addWidget(self.editor, stretch=1)
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        self.setLayout(layout)

        self.clipboard_monitoring_enabled = False
        self.clipboard = QApplication.clipboard()

    def toggleMonitoring(self):
        if self.clipboard_monitoring_enabled:
            # If monitoring is enabled, disable it
            self.clipboard_monitoring_enabled = False
            self.monitorButton.setText('Start Monitoring')
            self.monitorButton.setStyleSheet("background-color: green;")
            self.clipboard.dataChanged.disconnect(self.updateClipboard)
        else:
            # If monitoring is disabled, enable it
            self.clipboard_monitoring_enabled = True
            self.monitorButton.setText('Stop Monitoring')
            self.monitorButton.setStyleSheet("background-color: red;")
            self.clipboard.dataChanged.connect(self.updateClipboard)

    def updateClipboard(self):
        try:
            mime_data = self.clipboard.mimeData()
            if mime_data.hasText():
                text = mime_data.text()
                self.editor.setText(text)
        except:
            # qt.qpa.mime: Retrying to obtain clipboard.
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Example of using the ClipboardMonitorWidget in another widget
    main_widget = QWidget()
    clipboard_monitor_widget = FmusEditorWrapper()
    
    # Add the clipboard monitor widget to the layout of the main widget
    layout = QVBoxLayout()
    layout.addWidget(clipboard_monitor_widget)
    
    main_widget.setLayout(layout)
    main_widget.setGeometry(100, 100, 800, 600)
    main_widget.setWindowTitle('Clipboard Monitor Example')
    main_widget.show()

    sys.exit(app.exec_())
