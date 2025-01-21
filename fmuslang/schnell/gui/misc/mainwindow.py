# https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/
import sys
from PyQt5.QtGui import (
    QBrush,
	QColor,
	QDrag,
	QFont,
	QIcon,
	QKeySequence,
	QPalette,
	QPainter,
	QPainterPath,
	QPen,
	QPixmap,
	QPolygon,
	QPolygonF,
	QRegExpValidator,
	QWindow,
)

from PyQt5.QtCore import (
    Qt,
    pyqtProperty,
    pyqtSignal,
    pyqtSlot,

    QCoreApplication,
	QDir,
    QEvent,
	QMetaObject,
	QMimeData,
	QObject,
	QPoint,
	QPointF,
	QProcess,
    QPropertyAnimation,
	QRect,
	QRectF,
	QRegExp,
    QSize,
	QStringListModel,
	QTime,
	QTimer,
	QUrl,
)
from PyQt5.QtWidgets import (
    QAction,
    QApplication, 
    QCheckBox,
    QDialog, 
    QDialogButtonBox,
    QGroupBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):

    def addToolbarPair(self, text, toolbar):
        tb_lbl = QLabel(text)
        if 'check' in text:
            tb_cb = QCheckBox()
        elif 'spin' in text:
            tb_cb = QSpinBox()
        elif 'radio' in text:
            tb_cb = QRadioButton()
        else:
            tb_cb = QLineEdit()
        pair = QWidget()
        formlayout = QFormLayout()
        formlayout.addRow(tb_lbl, tb_cb)
        pair.setLayout(formlayout)
        toolbar.addWidget(pair)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")

        # The `Qt` namespace has a lot of attributes to customize
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action)

        # tb_lbl = QLabel("paircheckbox")
        # tb_cb = QCheckBox()
        # pair = QWidget()
        # formlayout = QFormLayout()
        # formlayout.addRow(tb_lbl, tb_cb)
        # pair.setLayout(formlayout)
        # toolbar.addWidget(pair)
        self.addToolbarPair('mycheck', toolbar)
        self.addToolbarPair('myradio', toolbar)
        self.addToolbarPair('spin me', toolbar)
        self.addToolbarPair('other form', toolbar)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")

        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
