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


class ChartPie(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartPie, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple piechart example')
        chart.addSeries(self.getSeries())

    def getSeries(self):
        series = QPieSeries()
        slice0 = series.append('10%', 1)
        series.append('20%', 2)
        series.append('70%', 7)
        series.setLabelsVisible()
        series.setPieSize(0.5)
        slice0.setLabelVisible()
        slice0.setExploded()
        slice0.setColor(QColor(255, 0, 0, 100))
        return series
