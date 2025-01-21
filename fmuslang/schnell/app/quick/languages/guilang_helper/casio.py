from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math, sys


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
    def __init__(self, parent = None):
        super(DigitalClock,self).__init__(parent)
        self.setupUi(self)
        # self.setStyleSheet('background-color')
        self.setWindowFlags(Qt.FramelessWindowHint) # Rimless
        self.setAcceptDrops(True)
        self.lcdNumber.display('00:00:00')
        time_slot = QTimer(self)
        time_slot.timeout.connect(self.clock_ticking)
        time_slot.start(1000)

    def clock_ticking(self):
        time_format = QTime.currentTime()
        time_format = time_format.toString("hh:mm:ss")
        self.lcdNumber.display(time_format)
        QApplication.processEvents()

