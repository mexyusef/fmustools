from PyQt5.QtChart import *
from PyQt5.QtGui import *
# from PyQt5.QtChart import (
#     QAreaSeries,
#     QBarCategoryAxis,
#     QBarSeries,
#     QBarSet,    
#     QCategoryAxis,
#     QChart,
#     QChartView,
#     QDateTimeAxis,
#     QHorizontalBarSeries,
#     QHorizontalPercentBarSeries,
#     QLegend,
#     QLineSeries,
#     QPercentBarSeries,
#     QPieSeries,
#     QScatterSeries,
#     QSplineSeries,
#     QStackedBarSeries,
#     QValueAxis,
# )


class ChartArea(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartArea, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple areachart example')
        # chart.setAnimationOptions(QChart.SeriesAnimations)
        # series = self.getSeries(chart)
        # chart.addSeries(series)
        chart.addSeries(self.getSeries())
        chart.createDefaultAxes()
        # chart.legend().setVisible(True)
        # chart.legend().setAlignment(Qt.AlignBottom)
        chart.axisX().setRange(0, 20)
        chart.axisY().setRange(0, 10)

    def getSeries(self):
        # series = QLineSeries(chart)
        # series.append(0, 6)
        # series.append(1, 32)
        # series.append(2, 4)
        # series.append(3, 18)
        # series.append(4, 10)
        # return series
        series0 = QLineSeries(self)
        series1 = QLineSeries(self)
        series0 << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        series1 << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)
        series = QAreaSeries(series0, series1)
        series.setName('Batman')
        pen = QPen(0x059605)  # pen = QPen(Qt.red)
        pen.setWidth(3)
        series.setPen(pen)
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, QColor(0x3cc63c))  # gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(0x26f626))  # gradient.setColorAt(1.0, QColor(0, 255, 0))
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        series.setBrush(gradient)
        return series
