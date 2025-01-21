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


class ChartSpline(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartSpline, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple splinechart example')
        self.getSeries(chart)
        chart.createDefaultAxes()
        chart.legend().setVisible(False)

    def getSeries(self, chart):
        series = QSplineSeries(chart)
        series << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        chart.addSeries(series)
        series = QSplineSeries(chart)
        series << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)
        chart.addSeries(series)
