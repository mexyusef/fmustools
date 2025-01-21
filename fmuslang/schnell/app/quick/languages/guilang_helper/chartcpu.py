from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from psutil import cpu_percent

class CpuLineChart(QChart):
    def __init__(self, *args, **kwargs):
        super(CpuLineChart, self).__init__(*args, **kwargs)
        self.m_count = 10
        self.legend().hide()
        self.m_series = QSplineSeries(self)
        self.m_series.setPen(QPen(QColor('#3B8CFF'), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.addSeries(self.m_series)
        self.m_axisX = QDateTimeAxis(self)
        self.m_axisX.setTickCount(self.m_count + 1)
        self.m_axisX.setFormat('hh:mm:ss')
        now = QDateTime.currentDateTime()
        self.m_axisX.setRange(now.addSecs(-self.m_count), now)
        self.addAxis(self.m_axisX, Qt.AlignBottom)
        self.m_series.attachAxis(self.m_axisX)
        self.m_axisY = QValueAxis(self)
        self.m_axisY.setLabelFormat('%d')
        self.m_axisY.setMinorTickCount(4)
        self.m_axisY.setTickCount(self.m_count + 1)
        self.m_axisY.setRange(0, 100)
        self.addAxis(self.m_axisY, Qt.AlignLeft)
        self.m_series.attachAxis(self.m_axisY)
        self.m_series.append([QPointF(now.addSecs(-i).toMSecsSinceEpoch(), 0) for i in range(self.m_count, -1, -1)])
        self.m_timer = QTimer()
        self.m_timer.timeout.connect(self.update_data)
        self.m_timer.start(1000)

    def update_data(self):
        value = cpu_percent()
        now = QDateTime.currentDateTime()
        self.m_axisX.setRange(now.addSecs(-self.m_count), now)
        points = self.m_series.pointsVector()
        points.pop(0)
        points.append(QPointF(now.toMSecsSinceEpoch(), value))
        self.m_series.replace(points)

class ChartCpu(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartCpu, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = CpuLineChart()
        self.setChart(chart)
        chart.setTitle('Simple cpu example')
