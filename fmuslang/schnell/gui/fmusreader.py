import os, sys, traceback, textwrap

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import (
    QsciScintilla,
    QsciLexerJSON, 
    QsciLexerPython, 
    QsciLexerMarkdown,
)


from dotenv import load_dotenv
envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
load_dotenv(envfile)

sidoarjodir = os.environ['ULIBPY_ROOTDIR']
schnelldir = os.environ['ULIBPY_BASEDIR']
sys.path.extend([sidoarjodir, schnelldir])

# print(f"""[gui.system.help.helper]
# sidoarjodir = {sidoarjodir}
# schnelldir = {schnelldir}
# """)

from schnell.app.transpiler.frontend.main import process_language
from schnell.app.printutils import indah4
from schnell.app.dirutils import files_filter, sdirs, bongkar
from schnell.app.fileutils import file_write, get_daftar, file_content, get_definition_by_key_permissive_start


stackedwidget_stylesheet = """
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}

QListWidget {
    min-width: 150px;
    max-width: 400px;
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

/* https://stackoverflow.com/questions/38369015/customuzing-qtabwidget-with-style-sheets */
QTabWidget::pane {
  border: 1px solid lightgray;
  top:-1px; 
  background: rgb(245, 245, 245);; 
} 

QTabBar::tab {
  background: rgb(230, 230, 230); 
  border: 1px solid lightgray; 
  padding: 15px;
} 

QTabBar::tab:selected { 
  background: rgb(245, 123, 245); 
  margin-bottom: -1px; 
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
    lebar, tinggi = int(screenw*wratio), int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)

class CodeScintilla(QsciScintilla):

    def __init__(self, *args, **kwargs):
        super(CodeScintilla, self).__init__(*args, **kwargs)
        self.init()
        self.linesChanged.connect(self.onLinesChanged)

    def onLinesChanged(self):
        self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + 6)

    def init(self):
        self.setUtf8(True)

        lexer = QsciLexerMarkdown(self)
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

    def __init__(self, filepath, *args, **kwargs):
        super(ListStackedWidget, self).__init__(*args, **kwargs)

        self.filepath = filepath

        # hbox utk kiri dan kanan
        layout = QHBoxLayout(self, spacing=0)
        # layout.setContentsMargins(0, 0, 0, 0)

        # di kiri list
        self.listWidget = QListWidget(self)
        # self.listWidget.setMinimumWidth(200)

        # di kanan stacked
        self.stackedWidget = QStackedWidget(self)
        # self.stackedWidget.setMaximumWidth(800)

        self.initUi()

        # layout.addWidget(self.listWidget, 40)
        # layout.addWidget(self.stackedWidget, 60)
        self.splitter = QSplitter(self)
        self.splitter.setHandleWidth(8)
        self.splitter.setOrientation(Qt.Horizontal)

        self.splitter.addWidget(self.listWidget)
        self.splitter.addWidget(self.stackedWidget)
        layout.addWidget(self.splitter)

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
        # # Here we use the general text with the icon mode.(You can also use Icon mode directly,setViewMode)
        # for i in range(20):
        #     item = QListWidgetItem(QIcon('Data/0%d.ico' % randint(1, 8)), str('select item %s' % i), self.listWidget)
        #     # Set the default width and height of the item(Only height is useful here)
        #     item.setSizeHint(QSize(16777215, 60))
        #     # center text
        #     item.setTextAlignment(Qt.AlignCenter)

        # # Simulate 20 more pages on the right(It won't be looped together with the above.)
        # for i in range(20):
        #     # label = QLabel('i am page %d' % i, self)
        #     # label.setAlignment(Qt.AlignCenter)
        #     # # Set the background color of the label(random here)
        #     # # A margin is added here(It is convenient to distinguish the color of QStackedWidget and QLabel)
        #     # label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
        #     #     randint(0, 255), randint(0, 255), randint(0, 255)))
        #     label = CodeScintilla()
        #     label.setText(f"code nomor {i}")
        #     self.stackedWidget.addWidget(label)

        toc = get_daftar(self.filepath)
        # https://www.pythonguis.com/faq/built-in-qicons-pyqt/icons-builtin.png
        # icon = QApplication.style().standardIcon(QStyle.SP_MediaPlay)
        icon = QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion)

        for isi in toc:

            editor = CodeScintilla()
            isi_file = get_definition_by_key_permissive_start(self.filepath, isi)
            editor.setText(isi_file)
            # editor = QWidget()
            self.stackedWidget.addWidget(editor)

            judul = textwrap.shorten(isi, width=60, placeholder="###")
            # judul = isi
            # print(judul)
            item = QListWidgetItem(icon, judul, self.listWidget)
            # w, h = 250, 60
            # item.setMinimumWidth(200)
            w, h = 16777215, 60
            # w, h = 16777215, 50
            item.setSizeHint(QSize(w,h)) # ini bikin kecil jk h gak specify misal 50/60

            # item.setTextAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    from toolbar import ToolbarWidget
else:
    from .toolbar import ToolbarWidget

all_files_dirs_list = []

MAX_RECURSE=2
class GroupWidget(QWidget):

    def __init__(self, helpdir, toolbar_button=False, level=0):
        """
        toolbar_button = True
            top level, tab = file
        toolbar_button = False
            second level, tab = folder
        """
        global all_files_dirs_list

        super().__init__()

        self.main_layout = QVBoxLayout()
        self.main_control = QTabWidget()

        self.daftar_file = files_filter(helpdir, extension=['.mk', '.fmus'])
        self.folders = []
        self.current_files = [{'filepath': os.path.join(helpdir, item), 'level':level} for item in self.daftar_file]

        if toolbar_button:
            self.toolbar_layout = QHBoxLayout()
            self.button_group = ToolbarWidget(self, self, all_files_dirs_list)
            self.toolbar_layout.addWidget(self.button_group)
            # self.main_layout.addWidget(ToolbarWidget())
            self.label_info = QLabel('Informasi masuk sini')
            # self.main_layout.addWidget(self.label_info)
            self.toolbar_layout.addWidget(self.label_info)
            self.main_layout.addLayout(self.toolbar_layout)
            # utk top level (level=0 atai toolbar_button=True), semua files masuk sini (ini belum direktori)
            all_files_dirs_list += self.current_files
        else:
            # utk level=1, lengkapi item {filepath,level} dg {children}
            all_files_dirs_list[-1]['children'] = self.current_files

        self.main_layout.addWidget(self.main_control)

        for file_mk in self.daftar_file:
            filename = os.path.basename(file_mk).removesuffix('.mk')
            filepath = os.path.join(helpdir, file_mk)
            self.main_control.addTab(ListStackedWidget(filepath), filename)
        self.setLayout(self.main_layout)
        # tambah recursive GroupWidget jk ada folder di dalam helpdir?
        dirlist = sdirs(helpdir)
        if dirlist and level<MAX_RECURSE:
            for dirname in dirlist:
                dirlengkap = os.path.join(helpdir, dirname)
                # utk level=0, tambah node level=1, nanti di pemanggilan GroupWidget berikutnya, akan dicantolkan childrennya
                # dg cara: all_files_dirs_list[-1]['children'] = self.current_files
                diritem = {'filepath': dirlengkap, 'level':level+1}
                all_files_dirs_list.append(diritem)
                # recursive
                group_folder = GroupWidget(dirlengkap, toolbar_button=False, level=level+1)
                self.folders.append({'widget': group_folder, 'index': self.main_control.count()})
                tab_index = self.main_control.addTab(group_folder, dirname)
                tab_icon = QApplication.style().standardIcon(QStyle.SP_DirIcon)
                self.main_control.setTabIcon(tab_index, tab_icon)
                self.main_control.setIconSize(QSize(32, 32))
                # https://stackoverflow.com/questions/57305452/add-icon-to-tab-qtabwidget
                # self.main_control.setTabShape(QTabWidget.Triangular)
                # self.main_control.setTabShape(QTabWidget.Rounded) # default

        QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())

relative_from_schnelldir = 'gui/system/help'
relative_from_sidoarjodir = 'schnell/gui/system/help'

def set_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(23, 23, 23))
    # palette.setColor(QPalette.WindowText, Qt.white)
    # palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # palette.setColor(QPalette.ToolTipBase, Qt.black)
    # palette.setColor(QPalette.ToolTipText, Qt.white)
    # palette.setColor(QPalette.Text, Qt.white)
    # palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # palette.setColor(QPalette.ButtonText, Qt.white)
    # palette.setColor(QPalette.BrightText, Qt.red)
    # palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

def main(helpdir=relative_from_sidoarjodir):
    app = QApplication(sys.argv)
    # set_theme(app)
    app.setStyleSheet(stackedwidget_stylesheet)
    if not helpdir.startswith(sidoarjodir):
        helpdir = bongkar(helpdir)
        if not helpdir.startswith(relative_from_sidoarjodir):
            helpdir = os.path.normpath(os.path.join(sidoarjodir, helpdir))
    # print('helpdir #1:', helpdir)
    w = GroupWidget(helpdir, toolbar_button=True, level=0)
    w.setWindowTitle('Help! (by qt.h or qt.he or perhaps qt.hr?)')
    w.setWindowIcon(QIcon(QPixmap(os.path.join(sidoarjodir, 'fmus-fm.png'))))
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=0.8, wratio=1.0)
    w.raise_()
    w.show()
    #sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    # C:\Users\usef\work\sidoarjo\data\system
    # C:\Users\usef\work\sidoarjo\data\model-data
    if len(sys.argv)==2:
        argumen = sys.argv[1]
        if argumen == '.':
            argumen = os.getcwd()
        main(argumen)
    else:
        main()
