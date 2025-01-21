from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

m_valueMax = 10


def generateRandomData(listCount=3, valueMax=10, valueCount=7):
    random.seed()
    dataTable = []
    for i in range(listCount):
        dataList = []
        yValue = 0.0
        f_valueCount = float(valueCount)
        for j in range(valueCount):
            yValue += random.uniform(0, valueMax) / f_valueCount
            value = j + random.random() * m_valueMax / f_valueCount, yValue
            label = "Slice " + str(i) + ":" + str(j)
            dataList.append((value, label))
        dataTable.append(dataList)
    return dataTable


m_dataTable = generateRandomData()

def getChart(title):
    chart = QChart(title=title)
    for i, data_list in enumerate(m_dataTable):
        series = QLineSeries(chart)
        for value, _ in data_list:
            series.append(*value)
        series.setName("Series " + str(i))
        chart.addSeries(series)
    chart.createDefaultAxes()
    return chart


def customAxisX(chart):
    series = chart.series()
    if not series:
        return
    axisx = QCategoryAxis(
        chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
    minx = chart.axisX().min()
    maxx = chart.axisX().max()
    tickc = chart.axisX().tickCount()
    if tickc < 2:
        axisx.append("label0", minx)
    else:
        step = (maxx - minx) / (tickc - 1)
        for i in range(0, tickc):
            axisx.append("lable%s" % i, minx + i * step)
    chart.setAxisX(axisx, series[-1])


def customTopAxisX(chart):
    series = chart.series()
    if not series:
        return
    category = ["%d month" % i for i in range(1, 9)]
    axisx = QCategoryAxis(
        chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
    axisx.setGridLineVisible(False)
    axisx.setTickCount(len(category))
    chart.axisX().setTickCount(len(category))
    minx = chart.axisX().min()
    maxx = chart.axisX().max()
    tickc = chart.axisX().tickCount()
    step = (maxx - minx) / (tickc - 1)
    for i in range(0, tickc):
        axisx.append(category[i], minx + i * step)
    chart.addAxis(axisx, Qt.AlignTop)
    series[-1].attachAxis(axisx)


def customAxisY(chart):
    series = chart.series()
    if not series:
        return
    category = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    axisy = QCategoryAxis(
        chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
    axisy.setGridLineVisible(False)
    axisy.setTickCount(len(category))
    miny = chart.axisY().min()
    maxy = chart.axisY().max()
    tickc = axisy.tickCount()
    if tickc < 2:
        axisy.append(category[0])
    else:
        step = (maxy - miny) / (tickc - 1)
        for i in range(0, tickc):
            axisy.append(category[i], miny + i * step)
    chart.addAxis(axisy, Qt.AlignRight)
    series[-1].attachAxis(axisy)

class ChartCustomAxis(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartCustomAxis, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        layout = QHBoxLayout(self)
        chart = getChart("Custom x-axis (equivalent to the original x-axis value)")
        customAxisX(chart)
        layout.addWidget(QChartView(chart, self))
        chart = getChart("Customize to add the right y-axis (equally divided, not corresponding to the left)")
        customAxisY(chart)
        layout.addWidget(QChartView(chart, self))
        chart = getChart("Custom top x-axis (divided by existing new x-axis)")
        customTopAxisX(chart)
        layout.addWidget(QChartView(chart, self))

# baca doc di schnell/gui/misc/notif7 baris 850
