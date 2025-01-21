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


class ChartLine(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartLine, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple linechart example')
        chart.setAnimationOptions(QChart.SeriesAnimations)
        series = self.getSeries(chart)
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self, chart):
        series = QLineSeries(chart)
        series.append(0, 6)
        series.append(1, 32)
        series.append(2, 4)
        series.append(3, 18)
        series.append(4, 10)
        return series
