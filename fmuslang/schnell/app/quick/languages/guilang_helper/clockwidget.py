from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math, sys


class ClockWidget(QLabel):
    # vintage clock
    def __init__(self, parent=None):
        super(ClockWidget, self).__init__(parent)
        self.timer = QTimer()  # timer
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every 1s
        self.setMinimumSize(QSize(100, 100))

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
        # according to 1 hour = 30degree, rotate counterclockwise in the direction of water quality
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

        # 1 minute is 6degree
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


def main():
    app = QApplication([])
    # set_theme(app)
    w = ClockWidget()
    # w.setStyleSheet(background_image_stylesheet)
    w.setStyleSheet("background-color: #ffffff;")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

