
from datetime import datetime
import os, random, string, sys, functools, subprocess, shutil
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *
from PyQt5.QtWebEngineWidgets import *


# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# bylangsdir = os.environ['ULIBPY_BYLANGSDIR']
# sys.path.extend([sidoarjodir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

from schnell.app.dirutils import (
    tempdir,
    timestamp,
)
from schnell.app.fileutils import (
    file_write,
    file_content,
)
from schnell.gui.system.searcher.widgets.acdsee import AcdseeWidget
from schnell.creator.context import context as creator_context


class PdfViewer(QWebEngineView):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._delta = 0.1  # zoom
        self.setZoomFactor(1.8)
        self.urlChanged.connect(self.url_changed)
        self.settings().setAttribute(self.settings().WebAttribute.PluginsEnabled, True)
        self.settings().setAttribute(self.settings().WebAttribute.PdfViewerEnabled, True)

    def url_changed(self):
        self.setWindowTitle(self.title())

    def go_back(self):
        self.back()

    def go_load(self, filepath):
        alamat = QUrl.fromLocalFile(filepath)
        self.load(alamat)

    # def wheelEvent(self, event):
    #     if event.angleDelta().y() > 0:
    #         self.zoomIn()
    #     else:
    #         self.zoomOut()

    # def zoomIn(self):
    #     """enlarge"""
    #     self.zoom(1 + self._delta)

    # def zoomOut(self):
    #     """zoom out"""
    #     self.zoom(1 - self._delta)

    # def zoom(self, factor):
    #     """zoom
    #     :param factor: scaling factor
    #     """
    #     # _factor = self.transform().scale(factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
    #     # if _factor < 0.07 or _factor > 100:
    #     #     # Prevent too big and too small
    #     #     return
    #     # self.scale(factor, factor)
    #     self.setZoomFactor(factor)



class SepiaPythonLexer(QsciLexerPython):
    def __init__(self, parent=None):
        super().__init__(parent)

    def defaultPaper(self, style):
        # return QColor("#F5DEB3")
        # return QColor("#424242")
        return QColor("#555555")

class QuickViewerEditor(QsciScintilla):

    save_file = pyqtSignal(bool)

    def __init__(self, parent=None, *args, **kwargs):
        super(QuickViewerEditor, self).__init__(parent, *args, **kwargs)
        self.margin = 24
        self.init()
        self.linesChanged.connect(self.onLinesChanged)

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + self.margin)

    def set_lexer(self, lex):
        self.setLexer(lex)

    def init(self):
        self.setUtf8(True)

        # lexer = QsciLexerMarkdown(self)
        # lexer = QsciLexerPython(self)
        lexer = SepiaPythonLexer(self)
        self.setLexer(lexer)

        # self.setEolMode(QsciScintilla.EolWindows)
        self.setEolMode(QsciScintilla.EolUnix)
        # self.setEolVisibility(True)

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

        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
        self.foldAll()

        QShortcut(QKeySequence("Ctrl+S"), self, activated=lambda: self.save_file.emit(True))


class DiskInfoLabel(QLabel):

    clicked=pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()


class QuickViewerWidget(QWidget):

    def set_info(self):
        tanggal = datetime.now().strftime('%d %b %Y, %H:%M:%S')
        total, used, free = shutil.disk_usage('C:')
        pembagi = 2**30
        self.information = f"{tanggal}, total {total//pembagi} GB, used {used//pembagi} GB, free {free//pembagi} GB"
        self.disk_info.setText(self.information)

    def __init__(self):
        super().__init__()

        self.disk_info = DiskInfoLabel()
        self.set_info()
        self.disk_info.clicked.connect(self.set_info)

        self.initUI()

    def set_filepath(self, filePath):
        """
        dipanggil dari filemanager
        """
        self.filepath = filePath
        self.status.setText(filePath)
        self.filepath_label.setText(filePath)

        self.first_load = True
        self.editor.setText(file_content(filePath))
        if creator_context['quick_viewer_folding']:
            self.editor.foldAll()
        self.stack.setCurrentWidget(self.editor)

    def set_imagepath(self, filePath):
        self.filepath = filePath
        self.status.setText(filePath)
        self.filepath_label.setText(filePath)

        self.acdsee.setPixmap(self.filepath)
        self.stack.setCurrentWidget(self.acdsee)

    def set_pdfpath(self, filePath):
        self.filepath = filePath
        self.status.setText(filePath)
        self.filepath_label.setText(filePath)

        self.pdf.go_load(self.filepath)
        self.stack.setCurrentWidget(self.pdf)

    def run_python(self):
        unset_filepath = False
        if not self.filepath:
            self.filepath = os.path.join(tempdir(), 'hapus_' + timestamp())
            file_write(self.filepath, self.editor.text())
            unset_filepath = True
        result = subprocess.run(['python', self.filepath], capture_output=True, text=True)
        self.stdout.append(result.stdout)
        self.stderr.append(result.stderr)
        self.stdout_stderr_widget.setVisible(True)
        if unset_filepath:
            self.filepath = '' # spy bisa ganti content

    def save_file(self, _):
        if self.filepath:
            file_contents = self.editor.text()
            # with open(self.filepath, "w", encoding='utf8') as f:
            #     f.write(file_contents)
            file_write(self.filepath, file_contents)

    def initUI(self):
        self.filepath = ''
        self.first_load = True

        self.editor = QuickViewerEditor(self)
        self.editor.save_file.connect(self.save_file)
        self.acdsee = AcdseeWidget(self)
        self.pdf = PdfViewer(self)
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.editor)
        self.stack.addWidget(self.acdsee)
        self.stack.addWidget(self.pdf)

        self.main_layout = QVBoxLayout()
        headerlayout = QHBoxLayout()
        self.mainbutton = QPushButton('exec')
        self.execmenu = QMenu(self.mainbutton)
        # utk kasih shortcut, dari 2 baris jadi 4 baris
        action_run_python = QAction('Run Python', self.execmenu)
        action_run_python.triggered.connect(self.run_python)
        action_run_python.setShortcut(QKeySequence("Ctrl+R"))
        self.execmenu.addAction(action_run_python)
        # self.execmenu.addAction('Run Python', self.run_python)
        
        self.execmenu.addAction('Fold', lambda: self.editor.foldAll())
        self.execmenu.addAction('Unfold', lambda: self.editor.clearFolds())
        self.execmenu.addAction('Status', lambda: self.stdout_stderr_widget.setVisible(self.stdout_stderr_widget.isHidden()))
        self.mainbutton.setMenu(self.execmenu)
        # self.mainbutton.clicked.connect(lambda: print('header1'))
        headerlayout.addWidget(self.mainbutton)
        # self.lexbutton = QPushButton('lex')
        # headerlayout.addWidget(self.lexbutton)
        # lexmenu = QMenu(self.lexbutton)
        # lexers = {
        #     # https://github.com/josephwilk/qscintilla/tree/master/Qt4Qt5
        #     # https://docs.huihoo.com/pyqt/QScintilla2/classQsciLexer.html
        #     # QsciLexerHTML,
        #     ...
        #     # QsciLexerXML.
        #     'Python': QsciLexerPython(self.editor),
        #     'Java': QsciLexerJava(self.editor),
        #     'Javascript': QsciLexerJavaScript(self.editor),
        #     'JSON': QsciLexerJSON(self.editor),
        #     'Markdown': QsciLexerMarkdown(self.editor),
        #     'None': None,
        # }
        # # lexmenu.addAction('Python', lambda: self.editor.set_lexer(lexers[]))
        # for label, lexerobj in lexers.items():
        #     lexmenu.addAction(label, functools.partial(self.editor.set_lexer, lexerobj))
        # self.lexbutton.setMenu(lexmenu)
        # self.information = f"{datetime.now().isoformat()}"
        # self.disk_info = QLabel(self.information)
        # self.disk_info.mou
        headerlayout.addWidget(self.disk_info)

        self.toggle_quickviewer_fold = QCheckBox("Toggle Fold")
        self.toggle_quickviewer_fold.setChecked(creator_context['quick_viewer_folding'])        
        self.toggle_quickviewer_fold.toggled.connect(self.changeViewerFold)
        headerlayout.addWidget(self.toggle_quickviewer_fold)

        self.filepath_label = QLabel(self.filepath)
        headerlayout.addWidget(self.filepath_label)
        headerlayout.addStretch(1)
        self.main_layout.addLayout(headerlayout)

        # self.main_layout.addWidget(self.editor)
        # buat widget utk status stdout stderr dlm 1 group box
        self.stdout_stderr_widget = QGroupBox('Status')
        stdout_layout = QHBoxLayout(self.stdout_stderr_widget)
        self.stdout = QTextBrowser()
        self.stdout.setStyleSheet('background-color: darkseagreen; font-size: 14px; font-family: MonoLisa, Terminal, Inconsolatas, Noto Sans, Open Sans;')
        self.stderr = QTextBrowser()
        self.stderr.setStyleSheet('background-color: lightcoral; font-size: 14px; font-family: MonoLisa, Terminal, Inconsolatas, Noto Sans, Open Sans;')
        stdout_layout.addWidget(self.stdout)
        stdout_layout.addWidget(self.stderr)
        # self.main_layout.addWidget(self.stdout_stderr_widget)
        self.stdout_stderr_widget.hide()

        # group status digabung dg editor utama dg splitter
        edit_status_splitter = QSplitter(Qt.Vertical)
        # edit_status_splitter.addWidget(self.editor)
        edit_status_splitter.addWidget(self.stack)
        edit_status_splitter.addWidget(self.stdout_stderr_widget)
        self.main_layout.addWidget(edit_status_splitter)

        footerlayout = QHBoxLayout()
        # self.mainbutton = QPushButton("footer1")
        # self.mainbutton.clicked.connect(lambda: print('footer1'))
        self.status = QLabel(self.filepath)
        footerlayout.addWidget(self.status)
        # currentlexer = self.editor.lexer()
        # kata = currentlexer.__doc__
        # footerlayout.addWidget(QLabel(kata))
        footerlayout.addStretch(1)
        self.main_layout.addLayout(footerlayout)

        # self.editor.textChanged.connect(lambda: self.unsaving_creator())
        self.editor.save_file.connect(lambda: self.saving_creator())

        self.setLayout(self.main_layout)

    def changeViewerFold(self):
        creator_context['quick_viewer_folding'] = self.toggle_quickviewer_fold.isChecked()

    def unsaving_creator(self):
        if not self.first_load:
            label = '*' + self.filepath
        else:            
            self.first_load = False
            label = self.filepath
        self.filepath_label.setText(label)

    def saving_creator(self):
        label = self.filepath
        self.filepath_label.setText(label)


background_image_stylesheet = '''
QuickViewerWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    wnd = QuickViewerWidget()
    wnd.setStyleSheet(background_image_stylesheet)
    wnd.show()
    wnd.resize(800, 600)
    wnd.setWindowTitle('Viewer')
    QShortcut(QKeySequence("Ctrl+Q"), wnd, activated=lambda: qApp.quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
