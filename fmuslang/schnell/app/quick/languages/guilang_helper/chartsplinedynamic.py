from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DynamicSpline(QChart):
    def __init__(self):
        super().__init__()
        self.m_step = 0
        self.m_x = 5
        self.m_y = 1
        # initialize image
        self.series = QSplineSeries(self)
        green_pen = QPen(Qt.red)
        green_pen.setWidth(3)
        self.series.setPen(green_pen)
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()
        self.series.append(self.m_x, self.m_y)

        self.addSeries(self.series)
        self.addAxis(self.axisX, Qt.AlignBottom)
        self.addAxis(self.axisY, Qt.AlignLeft)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
        self.axisX.setTickCount(5)
        self.axisX.setRange(0, 10)
        self.axisY.setRange(-5, 10)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handleTimeout)
        self.timer.start()

    def handleTimeout(self):
        x = self.plotArea().width() / self.axisX.tickCount()
        y = (self.axisX.max() - self.axisX.min()) / self.axisX.tickCount()
        self.m_x += y
        # In PyQt 5.11.3 and above, QtCore.QRandomGenerator.global() was renamed to global_()
        self.m_y = QRandomGenerator.global_().bounded(5) - 2.5
        self.series.append(self.m_x, self.m_y)
        self.scroll(x, 0)
        if self.m_x >= 100:
            self.timer.stop()

class ChartSplineDynamic(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartSplineDynamic, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = DynamicSpline()
        self.setChart(chart)
        chart.setTitle('Simple dynamicsplinechart example')
        chart.legend().hide()
        chart.setAnimationOptions(QChart.AllAnimations)
