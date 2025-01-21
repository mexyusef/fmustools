from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * # QGraphicsLineItem, QGraphicsProxyWidget
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


class ChartLineStack(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartLineStack, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        self.category = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.initChart()

        # prompt widget
        self.toolTipWidget = GraphicsProxyWidget('line', self._chart)

        # line
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        pen.setWidth(1)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # Some fixed calculations to reduce the amount of calculation in mouseMoveEvent
        # Get the min and max of x and y axis
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.min_x, self.max_x = axisX.min(), axisX.max()
        self.min_y, self.max_y = axisY.min(), axisY.max()

    def resizeEvent(self, event):
        super(ChartLineStack, self).resizeEvent(event)
        # need to be recalculated when the window size changes
        # Top left vertex in coordinate system
        self.point_top = self._chart.mapToPosition(QPointF(self.min_x, self.max_y))
        # Coordinate origin coordinates
        self.point_bottom = self._chart.mapToPosition(QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / (self._chart.axisX().tickCount() - 1)

    def mouseMoveEvent(self, event):
        super(ChartLineStack, self).mouseMoveEvent(event)
        pos = event.pos()
        # Convert the mouse position to the corresponding xy value
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round((x - self.min_x) / self.step_x)
        # Get the type and point of all normally displayed series in the coordinate system
        points = [(serie, serie.at(index)) for serie in self._chart.series() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        if points:
            pos_x = self._chart.mapToPosition(QPointF(index * self.step_x + self.min_x, self.min_y))
            self.lineItem.setLine(pos_x.x(), self.point_top.y(), pos_x.x(), self.point_bottom.y())
            self.lineItem.show()
            try:
                title = self.category[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # If the distance from the mouse position to the right is less than the tip width
            x = pos.x() - t_width if self.width() - pos.x() - 20 < t_width else pos.x()
            # If the height of the mouse position from the bottom is less than the tip height
            y = pos.y() - t_height if self.height() - pos.y() - 20 < t_height else pos.y()
            """
            File "C:\work\hapus\kerja\hapus\notif6.py", line 166, in mouseMoveEvent
                title, points, QPoint(x, y))
            TypeError: arguments did not match any overloaded call:
            QPoint(): too many arguments
            QPoint(int, int): argument 2 has unexpected type 'float'
            QPoint(QPoint): argument 1 has unexpected type 'int'
            """
            self.toolTipWidget.show(title, points, QPoint(int(x), int(y)))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender() # signal sender
        if not marker:
            return
        visible = not marker.series().isVisible()
        # hide or show series
        marker.series().setVisible(visible)
        marker.setVisible(True) # To ensure that the marker is always displayed
        # transparency
        alpha = 1.0 if visible else 0.4
        # Set the transparency of the label
        brush = marker.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # Set the transparency of the marker
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)
        # Set brush opacity
        pen = marker.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)

    def handleMarkerHovered(self, status):
        # Set the brush width of the series
        marker = self.sender() # signal sender
        if not marker:
            return
        series = marker.series()
        if not series:
            return
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        series.setPen(pen)

    def handleSeriesHoverd(self, point, state):
        # Set the brush width of the series
        series = self.sender() # signal sender
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if state else -1))
        series.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="Line chart stacking")
        self._chart.setAcceptHoverEvents(True)
        # SeriesAnimation
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        dataTable = [
            ["email marketing", [120, 132, 101, 134, 90, 230, 210]],
            ["affiliate advertising", [220, 182, 191, 234, 290, 330, 310]],
            ["video ad", [150, 232, 201, 154, 190, 330, 410]],
            ["direct interview", [320, 332, 301, 334, 390, 330, 320]],
            ["search engine", [820, 932, 901, 934, 1290, 1330, 1320]]
        ]
        for series_name, data_list in dataTable:
            series = QLineSeries(self._chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName(series_name)
            series.setPointsVisible(True)  # show dots
            series.hovered.connect(self.handleSeriesHoverd)  # mouseover
            self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # Create default axes
        axisX = self._chart.axisX()  # x-axis
        axisX.setTickCount(7)  # Set 7 ticks on the x-axis
        axisX.setGridLineVisible(False)  # Hide the line up from the x-axis
        axisY = self._chart.axisY()
        axisY.setTickCount(7)  # Set 7 ticks on the y-axis
        axisY.setRange(0, 1500)  # Set the y-axis range
        # custom x-axis
        axis_x = QCategoryAxis(
            self._chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
        axis_x.setTickCount(7)
        axis_x.setGridLineVisible(False)
        min_x = axisX.min()
        max_x = axisX.max()
        step = (max_x - min_x) / (7 - 1)  # 7 ticks
        for i in range(0, 7):
            axis_x.append(self.category[i], min_x + i * step)
        self._chart.setAxisX(axis_x, self._chart.series()[-1])
        # legend for chart
        legend = self._chart.legend()
        # Set the legend to be styled by the Series
        legend.setMarkerShape(QLegend.MarkerShapeFromSeries)
        # Iterate over markers on legend and bind signals
        for marker in legend.markers():
            # click event
            marker.clicked.connect(self.handleMarkerClicked)
            # mouseover event
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)

