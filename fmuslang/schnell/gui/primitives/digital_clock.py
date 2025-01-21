import math, sys
from PyQt5.QtWidgets import (
    qApp,
    
	QAbstractItemView,
    QApplication,
    QCheckBox,
	QCalendarWidget,
	QComboBox,
	QDesktopWidget,
	QDialog,
	QFileDialog,
	QFileSystemModel,
	QFormLayout,
    QFrame,
    QGraphicsDropShadowEffect,
    QGridLayout,
	QGroupBox,
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
	QListView,
    QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMdiArea,
	QMessageBox,
	QMenu,
	QPlainTextEdit,
    QPushButton,
	QRadioButton,
	QRubberBand,
    QScrollArea,	
	QShortcut,
	QSizePolicy,
	QSlider,
	QSpacerItem,
	QStyle,
	QTextBrowser,
	QTextEdit,
	QToolTip,
	QVBoxLayout,
    QWidget,
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
	QProcess,
    QPropertyAnimation,
    QRect,
	QRectF,
    QSize,
	QStringListModel,
	QTime,
	QTimer,
	QUrl,
)
from PyQt5.QtGui import (
    QBrush,
	QColor,
	QDrag,
	QIcon,
	QKeySequence,
	QPalette,
	QPainter,
	QPen,
	QPixmap,
	QPolygon,
	QWindow,
)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(335, 50)
        # Form.resize(150, 25)

        self.lcdNumber = QLCDNumber(Form)
        # self.lcdNumber.setStyleSheet('border: 1px solid blue; color: yellow;')
        self.lcdNumber.setStyleSheet('color: blue;')
        # self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 250, 50))
        self.lcdNumber.setGeometry(QRect(0, 0, 100, 40))
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.lcdNumber.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 2021.0)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class DigitalClock(QWidget, Ui_Form):
    # digital watch
    def __init__(self,parent = None):
        super(DigitalClock,self).__init__(parent)
        self.setupUi(self)
        # self.setStyleSheet('background-color')
        self.setWindowFlags(Qt.FramelessWindowHint) # Rimless
        self.setAcceptDrops(True)
        self.lcdNumber.display('00:00:00')
        time_slot =QTimer(self)
        time_slot.timeout.connect(self.event_1)
        time_slot.start(1000)

    def event_1(self):
        time_format = QTime.currentTime()
        time_format = time_format.toString("hh:mm:ss")
        self.lcdNumber.display(time_format)
        QApplication.processEvents()



dialog_stylesheet = """
#Custom_Widget {
    background: white;
    border-radius: 10px;
}

#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: white;
    background: red;
}
QSpacerItem {
    background: green;
}
"""

class Dialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(dialog_stylesheet)
        self.initUi()
        # add shadow
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

    def initUi(self):
        layout = QVBoxLayout(self)
        # Highlights: this widget as background and rounded corners
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout.addWidget(self.widget)

        # add ui in widget
        layout = QGridLayout(self.widget)
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # row 1
        layout.addItem(spacer1, 0, 0) # layout item = spacer
        layout.addWidget(QPushButton('r', self, clicked=self.accept, objectName='closeButton'), 0, 1)
        
        # row 2
        # spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # layout.addItem(spacer2, 1, 0)
        # widget1 = QWidget()
        # widget1.setStyleSheet('background: green;')
        # widget1 = QColorDialog()
        widget1 = DigitalClock()
        layout.addWidget(widget1, 1, 0, -1, 2)

    def sizeHint(self):
        return QSize(600, 400)


def main():
    app = QApplication(sys.argv)
    w = Dialog()
    w.exec_()
    # QTimer.singleShot(200, app.quit)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
