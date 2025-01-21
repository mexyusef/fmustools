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
    QGraphicsDropShadowEffect,
    QGridLayout,
	QGroupBox,
    QHBoxLayout,
    QLabel,
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

class ClockWidget(QLabel):
    # vintage clock
    def __init__(self,parent  =None):
        super(ClockWidget,self).__init__(parent)
        self.timer = QTimer()  # timer
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every 1s

    def textRectF(self,radius,pointsize,angle):

        recf = QRectF()
        recf.setX(radius*math.cos(angle*math.pi/180.0)-pointsize*2)
        recf.setY(radius*math.sin(angle*math.pi/180.0)-pointsize/2.0)
        recf.setWidth(pointsize*4)#Width Height
        recf.setHeight(pointsize)
        return recf

    def paintEvent(self, event):
        panjang_jam = -50
        panjang_menit = -65
        panjang_detik = -80
        hour_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_jam)]
        minute_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_menit)]
        second_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_detik)]

        hour_color = QColor(0,0,250,200)
        minute_color = QColor(0,250,0,175)
        second_color = QColor(250,0,0,150) # QColor(0,160,230,150)

        min_len = min(self.width(),self.height())
        time = QTime.currentTime() # get current time
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2,self.height()/2) # Pan to center of window
        painter.scale(min_len/200.0,min_len/200.0) # scaling

        #---------- draw the hour hand ------------
        painter.setPen(Qt.NoPen)
        painter.setBrush(hour_color)#color
        painter.save()
        # according to 1 hour = 30°, rotate counterclockwise in the direction of water quality
        painter.rotate(30.0*((time.hour()+time.minute()/60.0)))
        painter.drawConvexPolygon(QPolygon(hour_points))
        painter.restore() # save Exit to reset the brush

        painter.setPen(hour_color)
        #draw hour line(360/12 = 30 degrees)
        for i in range(12):
            painter.drawLine(88,0,96,0)#draw horizontal lines
            painter.rotate(30.0)# Rotate at the original rotation angle;

        radius = 100 # radius
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
        pointSize = font.pointSize() # font size
        # print(pointSize)

        #draw hour text
        for i in range(12):
            nhour = i + 3 # from level 3 point to draw
            if(nhour>12):
                nhour -= 12
            painter.drawText(self.textRectF(radius*0.8,pointSize,i*30),Qt.AlignCenter,str(nhour))

        #draw the minute hand;
        painter.setPen(Qt.NoPen)
        painter.setBrush(minute_color)
        painter.save()

        # 1 minute is 6°
        painter.rotate(6.0*(time.minute()+time.second()/60.0))
        painter.drawConvexPolygon(QPolygon(minute_points))
        painter.restore()

        # draw minute line
        painter.setPen(minute_color)
        for i in range(60):
            if(i%5 !=0):
                painter.drawLine(92,0,96,0)
            painter.rotate(6.0)

        # Draw the second hand
        painter.setPen(Qt.NoPen)
        painter.setBrush(second_color)
        painter.save()
        # draw second line
        painter.rotate(6.0*time.second())
        painter.drawConvexPolygon(QPolygon(second_points))
        painter.restore()

        painter.setPen(second_color)
        for i in range(360):
            if(i%5!=0 or i%30!=0): # draw
                painter.drawLine(94,0,96,0)
            painter.rotate(1.0) # rotate




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
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

    def initUi(self):
        layout = QVBoxLayout(self)
        # 重点： 这个widget作为背景和圆角
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout.addWidget(self.widget)

        # 在widget中添加ui
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
        widget1 = ClockWidget()
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
