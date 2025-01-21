
import webbrowser
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal, QRandomGenerator
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox, QToolBar, QLineEdit
from PyQt5.QtCore import QEasingCurve
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QGradient, QLinearGradient, QPainter, QPen
# pip install PyQtChart
from PyQt5.QtChart import QChartView, QChart, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtChart import QPieSeries
from PyQt5.QtChart import QScatterSeries
from PyQt5.QtChart import QSplineSeries
from PyQt5.QtChart import QLineSeries, QAreaSeries
from PyQt5.QtChart import QValueAxis

import random
from PyQt5.QtCore import QDateTime, QDate, QUrl
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel, QComboBox, QDateEdit, QDateTimeEdit, QSpinBox


class MessageBox(QMessageBox):

    def __init__(self, *args, count=5, time=1000, auto=False, **kwargs):
        super(MessageBox, self).__init__(*args, **kwargs)
        self._count = count
        self._time = time
        self._auto = auto  # 是否自动关闭
        assert count > 0  # 必须大于0
        assert time >= 500  # 必须>=500毫秒
        self.setStandardButtons(self.Close)  # 关闭按钮
        self.closeBtn = self.button(self.Close)  # 获取关闭按钮
        self.closeBtn.setText('close(%s)' % count)
        self.closeBtn.setEnabled(False)
        self._timer = QTimer(self, timeout=self.doCountDown)
        self._timer.start(self._time)
        print('Whether to close automatically', auto)

    def doCountDown(self):
        self.closeBtn.setText('close(%s)' % self._count)
        self._count -= 1
        if self._count <= 0:
            self.closeBtn.setText('close')
            self.closeBtn.setEnabled(True)
            self._timer.stop()
            if self._auto: # auto close
                self.accept()
                self.close()


class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("i am a form")
        self.setWindowIcon(QIcon("male.png"))
        self.resize(920, 240)
        self.setColumnCount(6)
        self.setRowCount(2)
        # 设置表格有两行五列。
        self.setColumnWidth(0, 200)
        self.setColumnWidth(4, 200)
        self.setRowHeight(0, 100)
        # 设置第一行高度为100px，第一列宽度为200px。

        self.table()

    def table(self):
        self.setItem(0, 0, QTableWidgetItem("your name"))
        self.setItem(0, 1, QTableWidgetItem("gender"))
        self.setItem(0, 2, QTableWidgetItem("date of birth"))
        self.setItem(0, 3, QTableWidgetItem("Profession"))
        self.setItem(0, 4, QTableWidgetItem("income"))
        self.setItem(0, 5, QTableWidgetItem("progress bar"))
        # 添加表格的文字内容.
        self.setHorizontalHeaderLabels(["first row", "second line", "The third row", "fourth row", "The fifth line", "sixth row"])
        self.setVerticalHeaderLabels(["first row", "the second list"])
        # 设置表头
        lbp = QLabel()
        lbp.setPixmap(QPixmap("youPicture.png"))
        self.setCellWidget(1, 1, lbp)
        # 在表中添加一张图片
        twi = QTableWidgetItem("Graph")
        twi.setFont(QFont("Times", 10, ))
        self.setItem(1, 0, twi)

        # 添加一个自己设置了大小和类型的文字。
        dte = QDateTimeEdit()
        dte.setDateTime(QDateTime.currentDateTime())
        dte.setDisplayFormat("yyyy/MM/dd")
        dte.setCalendarPopup(True)
        self.setCellWidget(1, 2, dte)
        # 添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
        cbw = QComboBox()
        cbw.addItem("doctor")
        cbw.addItem("teacher")
        cbw.addItem("lawyer")
        self.setCellWidget(1, 3, cbw)
        # 添加了一个下拉选择框
        sb = QSpinBox()
        sb.setRange(1000, 10000)
        sb.setValue(5000)  # 设置最开始显示的数字
        sb.setDisplayIntegerBase(10)  # 这个是显示数字的进制，默认是十进制。
        sb.setSuffix("Rupiah")  # 设置后辍
        sb.setPrefix("IDR: ")  # 设置前辍
        sb.setSingleStep(100)
        self.setCellWidget(1, 4, sb)
        # 添加一个进度条

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.setCellWidget(1, 5, self.progressBar)
        self.step = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        # 信号连接到槽
        self.timer.timeout.connect(self.onTimerOut)
        self.count = 0

    def onTimerOut(self):  # 重写timerEvent
        self.count += 1
        if self.count >= 100:  # value >= 100时，停止计时器
            self.timer.stop()
            print("Finish")
            # self.progressBar.setValue(self.step)
        else:
            print(self.count)
            self.progressBar.setValue(self.count)
            # return
            # self.step += 1

class DynamicSpline(QChart):
    def __init__(self):
        super().__init__()
        self.m_step = 0
        self.m_x = 5
        self.m_y = 1
        # 初始化图像
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
        # 在PyQt5.11.3及以上版本中，QRandomGenerator.global()被重命名为global_()
        self.m_y = QRandomGenerator.global_().bounded(5) - 2.5
        self.series.append(self.m_x, self.m_y)
        self.scroll(x, 0)
        if self.m_x >= 100:
            self.timer.stop()

class MyDynamicSplineChart(QChartView):
    def __init__(self, *args, **kwargs):
        super(MyDynamicSplineChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        self.setRenderHint(QPainter.Antialiasing)

        chart = DynamicSpline()
        chart.setTitle("Dynamic spline chart")
        chart.legend().hide()
        chart.setAnimationOptions(QChart.AllAnimations)
        self.setChart(chart)

class MySplineChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MySplineChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple splinechart example')
        # 添加Series
        self.getSeries(chart)
        # 创建默认xy轴
        chart.createDefaultAxes()
        chart.legend().setVisible(False)

    def getSeries(self, chart):
        # 第一组
        series = QSplineSeries(chart)
        series << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) \
        << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        chart.addSeries(series)

        # 第二组
        series = QSplineSeries(chart)
        series << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) \
        << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)
        chart.addSeries(series)

class MyScatterChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyScatterChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)
        # 生成模拟数据
        self.m_dataTable = self.generateRandomData(3, 10, 7)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Scatter chart')
        # 添加Series
        self.getSeries(chart)
        # 创建默认xy轴
        chart.createDefaultAxes()
        chart.legend().setVisible(False)

    def getSeries(self, chart):
        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName('Series ' + str(i))
            chart.addSeries(series)

    def generateRandomData(self, listCount, valueMax, valueCount):
        # 生成模拟随机数据
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

class MyPieChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyPieChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple piechart example')
        # 添加Series
        chart.addSeries(self.getSeries())

    def getSeries(self):
        series = QPieSeries()
        slice0 = series.append('10%', 1)
        series.append('20%', 2)
        series.append('70%', 7)
        # 显示label文字
        series.setLabelsVisible()
        series.setPieSize(0.5)
        # 使第一块突出显示
        slice0.setLabelVisible()
        slice0.setExploded()
        # 设置第一块颜色
        slice0.setColor(QColor(255, 0, 0, 100))
        return series

class MyLineChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyLineChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # Antialiasing
        self.setRenderHint(QPainter.Antialiasing)

        # chart
        chart = QChart()
        self.setChart(chart)
        # set title
        chart.setTitle('Simple linechart example')
        # Turn on animation effects
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # Add to/increase Series
        series = self.getSeries(chart)
        chart.addSeries(series)
        # Classification
        # categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # Category x-axis
        # axis = QBarCategoryAxis()
        # axis.append(categories)
        # Create default grid
        chart.createDefaultAxes()
        # replace the default x-axis
        # chart.setAxisX(axis, series)
        # show legend
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

class MyAreaChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyAreaChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple areachart example')
        # 添加Series
        chart.addSeries(self.getSeries())
        # 创建默认轴线
        chart.createDefaultAxes()
        # 设置xy轴的范围
        chart.axisX().setRange(0, 20)
        chart.axisY().setRange(0, 10)

    def getSeries(self):
        # 创建Series
        series0 = QLineSeries(self)
        series1 = QLineSeries(self)

        # 添加数据
        series0 << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) \
        << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        series1 << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) \
        << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)

        # 创建区域图
        series = QAreaSeries(series0, series1)
        series.setName('Batman')

        # 画笔
        pen = QPen(0x059605)
        pen.setWidth(3)
        series.setPen(pen)

        # 设置画刷
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, QColor(0x3cc63c))
        gradient.setColorAt(1.0, QColor(0x26f626))
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        series.setBrush(gradient)

        return series

class MyBarChart(QChartView):

    def __init__(self, *args, **kwargs):
        super(MyBarChart, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # Antialiasing
        self.setRenderHint(QPainter.Antialiasing)

        # chart
        chart = QChart()
        self.setChart(chart)
        # set title
        chart.setTitle('Simple barchart example')
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
        # Create 5 pillars
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
        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series

mystylesheet = """
QWidget#widgetTitle {
    background-color: rgb(76, 169, 106);
}
QWidget#widgetBottom {
    border-top-style: solid;
    border-top-width: 2px;
    border-top-color: rgb(185, 218, 201);
}
QLabel#labelTitle {
    color: rgb(255, 255, 255);
}
QLabel#labelContent {
    padding: 5px;
}
QPushButton {
    border: none;
    background: transparent;
}
QPushButton#buttonClose {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}
QPushButton#buttonClose:hover {
    background-color: rgb(212, 64, 39);
}
QPushButton#buttonView {
    color: rgb(255, 255, 255);
    border-radius: 5px;
    border: solid 1px rgb(76, 169, 106);
    background-color: rgb(76, 169, 106);
}
QPushButton#buttonView:hover {
    color: rgb(0, 0, 0);
}
"""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
</head>
<body>
    <p>
        This is a simple HTML page.
    </p>
</body>
</html>
"""
# pip install pyqtwebengine
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class MyWebview(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.loadPage()

        self.toolBar = QToolBar()

        self.backBtn = QPushButton(self)
        self.backBtn.setEnabled(False)
        self.backBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/left-32.png'))
        self.backBtn.clicked.connect(self.back)
        self.toolBar.addWidget(self.backBtn)

        self.forBtn = QPushButton(self)
        self.forBtn.setEnabled(False)
        self.forBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forBtn.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forBtn)

        self.address = QLineEdit(self)
        self.address.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.address)

        vbox.addWidget(self.toolBar, 10)
        vbox.addWidget(self.webEngineView, 90)

        self.webEngineView.page().urlChanged.connect(self.onLoadFinished)
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QWebEngineView')
        self.show()

    def loadPage(self):

        self.webEngineView.setHtml(html_content)


    def load(self):

        url = QUrl.fromUserInput(self.address.text())

        if url.isValid():
            self.webEngineView.load(url)


    def onLoadFinished(self):

        if self.webEngineView.history().canGoBack():
            self.backBtn.setEnabled(True)
        else:
            self.backBtn.setEnabled(False)

        if self.webEngineView.history().canGoForward():
            self.forBtn.setEnabled(True)
        else:
            self.forBtn.setEnabled(False)

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def urlChanged(self, url):
        self.address.setText(url.toString())

class Ui_NotifyForm(object):

    def setupUi(self, NotifyForm):

        NotifyForm.setObjectName("NotifyForm")
        # NotifyForm.resize(300, 600)
        NotifyForm.resize(400, 800)
        NotifyForm.setStyleSheet(mystylesheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(NotifyForm) # ini jadi layout of choice dong ya...setara NotifyForm.setLayout(self.verticalLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widgetTitle = QtWidgets.QWidget(NotifyForm)
        self.widgetTitle.setMinimumSize(QtCore.QSize(0, 26))
        self.widgetTitle.setObjectName("widgetTitle")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetTitle)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.labelTitle = QtWidgets.QLabel(self.widgetTitle)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")

        self.horizontalLayout_3.addWidget(self.labelTitle)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.buttonClose = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonClose.setMinimumSize(QtCore.QSize(26, 26))
        self.buttonClose.setMaximumSize(QtCore.QSize(26, 26))
        self.buttonClose.setObjectName("buttonClose")

        self.horizontalLayout_3.addWidget(self.buttonClose)

        self.verticalLayout.addWidget(self.widgetTitle)

        self.labelContent = QtWidgets.QLabel(NotifyForm)
        self.labelContent.setText("")
        self.labelContent.setWordWrap(True)
        self.labelContent.setObjectName("labelContent")

        # self.grid = QGridLayout()
        # total = 25

        # for i in range(total):
        #     self.grid.addWidget(QPushButton(f"Baris {i}"), i, 1)
        # self.grid.addWidget(self.labelContent, total, 1)

        # # self.verticalLayout.addWidget(self.labelContent)
        # self.win = QWidget()
        # self.win.setLayout(self.grid)

        # https://stackoverflow.com/questions/41616864/pyqt-expand-grid-in-scroll-area
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

        for i in range(100):
            if i==50:
                chart = MyBarChart()
                self.gridLayout.addWidget(chart, i, 1, 1+4, 100) # span row 5 
            else:
                for j in range(100):
                    btn = QtWidgets.QPushButton(f"{i},{j}")
                    btn.clicked.connect(lambda: MessageBox(self, text='Countdown to close dialog', auto=random.randrange(0, 2)).exec_())
                    self.gridLayout.addWidget(btn, i+4 if i>50 else i, j)
        
        self.gridLayout.addWidget(self.labelContent, 100, 1, -1, 100)


        # verticallayout addwidget = tab, tab berisi 2: 1 scrollarea, 2 barchart, dst...

        self.tabWidget = QtWidgets.QTabWidget(NotifyForm)
        self.tabWidget.addTab(self.scrollArea, "Pertama")
        self.tabWidget.setObjectName("tabWidget")

        self.tab0 = MyTable()
        self.tab0.setObjectName("table")
        self.tabWidget.addTab(self.tab0, "Tabel")


        self.tab = MyLineChart() # QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "Line chart")

        self.tab_2 = MyAreaChart() # QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Areachart")

        self.tab_3 = MyBarChart()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "Barchart")

        self.tab4 = MyPieChart()
        self.tab4.setObjectName("tab4")
        self.tabWidget.addTab(self.tab4, "Pie chart")

        self.tab5 = MyScatterChart()
        self.tab5.setObjectName("tab5")
        self.tabWidget.addTab(self.tab5, "Scatter chart")

        self.tab6 = MySplineChart()
        self.tab6.setObjectName("tab6")
        self.tabWidget.addTab(self.tab6, "Spline chart")

        self.tab7 = MyDynamicSplineChart()
        self.tab7.setObjectName("tab7")
        self.tabWidget.addTab(self.tab7, "Dynamic Spline")

        self.tab8 = MyWebview()
        self.tab8.setObjectName("tab8")
        self.tabWidget.addTab(self.tab8, "Webview")

        self.tabWidget.setCurrentIndex(0)
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "折线图"))

        self.verticalLayout.addWidget(self.tabWidget)
        # self.verticalLayout.addWidget(self.scrollArea)
        # self.verticalLayout.addWidget(self.win)

        self.widgetBottom = QtWidgets.QWidget(NotifyForm)
        self.widgetBottom.setObjectName("widgetBottom")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.buttonView = QtWidgets.QPushButton(self.widgetBottom)
        self.buttonView.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonView.setObjectName("buttonView")

        self.horizontalLayout.addWidget(self.buttonView)

        self.verticalLayout.addWidget(self.widgetBottom)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(NotifyForm)
        QtCore.QMetaObject.connectSlotsByName(NotifyForm)

    def retranslateUi(self, NotifyForm):
        _translate = QtCore.QCoreApplication.translate
        NotifyForm.setWindowTitle(_translate("NotifyForm", "notification"))
        self.buttonClose.setText(_translate("NotifyForm", "r"))
        self.buttonView.setText(_translate("NotifyForm", "Go"))


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     NotifyForm = QtWidgets.QWidget()
#     ui = Ui_NotifyForm()
#     ui.setupUi(NotifyForm)
#     NotifyForm.show()
#     sys.exit(app.exec_())

class WindowNotify(QWidget, Ui_NotifyForm):

    SignalClosed = pyqtSignal()  # Popup close signal

    def __init__(self, title="", content="", timeout=5000, *args, **kwargs):
        super(WindowNotify, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setTitle(title).setContent(content)
        self._timeout = timeout
        self._init()

    def setTitle(self, title):
        if title:
            self.labelTitle.setText(title)
        return self

    def title(self):
        return self.labelTitle.text()

    def setContent(self, content):
        if content:
            self.labelContent.setText(content)
        return self

    def content(self):
        return self.labelContent.text()

    def setTimeout(self, timeout):
        if isinstance(timeout, int):
            self._timeout = timeout
        return self

    def timeout(self):
        return self._timeout

    def onView(self):
        print("onView")
        webbrowser.open_new_tab("https://google.com")

    def onClose(self):
        # When the close button is clicked
        print("onClose")
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)  # Start the bounce animation

    def _init(self):
        # Hide Taskbar|Remove Borders|Show Top
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # close button event
        self.buttonClose.clicked.connect(self.onClose)
        # Click the View button
        self.buttonView.clicked.connect(self.onView)
        # whether the logo is being displayed
        self.isShow = True
        # time out
        self._timeouted = False
        # desktop
        self._desktop = QApplication.instance().desktop()
        # window initial start position
        self._startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.screenGeometry().height()
        )
        # window popup end position
        self._endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.availableGeometry().height() - self.height() - 5
        )
        # Initialize the position to the lower right corner
        self.move(self._startPos)

        # animation
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(1000)  # 1s

        # Bounce timer
        self._timer = QTimer(self, timeout=self.closeAnimation)

    def show(self, title="", content="", timeout=5000):
        self._timer.stop()  # Stop the timer to prevent problems with the previous timer when the second popup pops up
        self.hide()  # hide first
        self.move(self._startPos)  # Initialize the position to the lower right corner
        super(WindowNotify, self).show()
        self.setTitle(title).setContent(content).setTimeout(timeout)
        return self

    def showAnimation(self):
        print("showAnimation isShow = True")
        # show animation
        self.isShow = True
        self.animation.stop()  # Stop the previous animation and start again
        self.animation.setStartValue(self.pos())

        # https://www.pythonguis.com/tutorials/qpropertyanimation/
        # https://doc.qt.io/qt-5/qeasingcurve.html
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        self.animation.setEndValue(self._endPos)
        self.animation.start()
        # After 5 seconds of popping, if there is no focus, it will pop back
        self._timer.start(self._timeout)

        # QTimer.singleShot(self._timeout, self.closeAnimation)

    def closeAnimation(self):
        print("closeAnimation hasFocus", self.hasFocus())
        # turn off animation
        if self.hasFocus():
            # If there is still focus after the countdown for 5 seconds after the pop-up, you need to actively trigger the shutdown after losing the focus.
            self._timeouted = True
            return  # Do not close if it has focus
        self.isShow = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    def onAnimationEnd(self):
        # animation ends
        # print("onAnimationEnd isShow", self.isShow)
        if not self.isShow:
            # print("onAnimationEnd close()")
            self.close()
            # print("onAnimationEnd stop timer")
            self._timer.stop()
            # print("onAnimationEnd close and emit signal")
            self.SignalClosed.emit()

    def enterEvent(self, event):
        super(WindowNotify, self).enterEvent(event)
        # Set the focus (it seems useless, but after a mouse click, this method is useful)
        # print("enterEvent setFocus Qt.MouseFocusReason")
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, event):
        super(WindowNotify, self).leaveEvent(event)
        # remove focus
        # print("leaveEvent clearFocus")
        self.clearFocus()
        if self._timeouted:
            QTimer.singleShot(1000, self.closeAnimation)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = QWidget()
    notify = WindowNotify(parent=window)

    layout = QHBoxLayout(window)

    b1 = QPushButton("Open 1", window, clicked=lambda: notify.show(timeout=10000,content='Wieke cinta: ' + b1.text()).showAnimation())
    b2 = QPushButton("Open 2", window, clicked=lambda: notify.show(content='Yang disuka gaia adlh: ' + b2.text()).showAnimation())

    layout.addWidget(b1)
    layout.addWidget(b2)

    window.show()

    sys.exit(app.exec_())
