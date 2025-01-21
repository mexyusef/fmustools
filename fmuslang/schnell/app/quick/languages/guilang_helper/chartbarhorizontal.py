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


class ChartBarHorizontal(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartBarHorizontal, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple horizontal barchart example')
        # Turn on animation effects
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # Add to/increase Series
        series = self.getSeries()
        chart.addSeries(series)
        # Classification
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # Category x-axis
        axis = QBarCategoryAxis()
        axis.append(categories)
        # Create default grid
        chart.createDefaultAxes()
        # replace the default x-axis
        chart.setAxisX(axis, series)
        # show legend
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self):
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        set2 = QBarSet('Axel')
        set3 = QBarSet('Mary')
        set4 = QBarSet('Samantha')
        # adding data
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2
        # Create column bars
        series = QHorizontalBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series
