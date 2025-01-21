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
import random

class ChartScatter(QChartView):

    def generateRandomData(self, listCount, valueMax, valueCount):

        random.seed()
        dataTable = []
        for i in range(listCount):
            dataList = []
            yValue = 0.0
            f_valueCount = float(valueCount)
            for j in range(valueCount):
                yValue += random.uniform(0, valueMax) / f_valueCount
                value = QPointF(j + random.random() * valueMax / f_valueCount, yValue)
                label = 'Slice ' + str(i) + ':' + str(j)
                dataList.append((value, label))
            dataTable.append(dataList)
        return dataTable

    def __init__(self, *args, **kwargs):
        super(ChartScatter, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        chart = QChart()
        self.setChart(chart)
        chart.setTitle('Simple scatterchart example')
        self.m_dataTable = self.generateRandomData(3, 10, 7)
        self.getSeries(chart)
        chart.createDefaultAxes()
        chart.legend().setVisible(False)

    def getSeries(self, chart):
        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName('Series ' + str(i))
            chart.addSeries(series)
