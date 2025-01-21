from PyQt5.QtChart import *
from PyQt5.QtGui import *
import random
from PyQt5.QtWidgets import * # QGraphicsLineItem, QGraphicsProxyWidget

class ChartBarStack(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartBarStack, self).__init__(*args, **kwargs)
        # self.resize(__LEBAR__, __TINGGI__)
        self.setMinimumHeight(200)
        self.setRenderHint(QPainter.Antialiasing)
        self.initChart()
        self.toolTipWidget = GraphicsProxyWidget('bar', self._chart)
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.category_len = len(axisX.categories())
        self.min_x, self.max_x = -0.5, self.category_len - 0.5
        self.min_y, self.max_y = axisY.min(), axisY.max()
        self.point_top = self._chart.mapToPosition(QPointF(self.min_x, self.max_y))

    def mouseMoveEvent(self, event):
        super(ChartBarStack, self).mouseMoveEvent(event)
        pos = event.pos()
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round(x)
        serie = self._chart.series()[0]
        bars = [(bar, bar.at(index))
                for bar in serie.barSets() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        #         print(bars)
        if bars:
            right_top = self._chart.mapToPosition(QPointF(self.max_x, self.max_y))
            step_x = round((right_top.x() - self.point_top.x()) / self.category_len)
            posx = self._chart.mapToPosition(QPointF(x, self.min_y))
            self.lineItem.setLine(posx.x(), self.point_top.y(), posx.x(), posx.y())
            self.lineItem.show()
            try:
                title = self.categories[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            x = pos.x() - t_width if self.width() - pos.x() - 20 < t_width else pos.x()
            y = pos.y() - t_height if self.height() - pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, bars, QPoint(int(x), int(y)))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return

        brush = bar.brush()
        color = brush.color()
        alpha = 0.0 if color.alphaF() == 1.0 else 1.0
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar.setBrush(brush)
        # marker
        brush = marker.labelBrush()
        color = brush.color()
        alpha = 0.4 if color.alphaF() == 1.0 else 1.0

        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)

        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

    def handleMarkerHovered(self, status):
        marker = self.sender()
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def handleBarHoverd(self, status, index):
        bar = self.sender()
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="Column chart stacking")
        self._chart.setAcceptHoverEvents(True)
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        names = ["Email Marketing", "Affiliate Advertising", "Video Advertising", "Direct Access", "Search Engines"]
        series = QBarSeries(self._chart)
        for name in names:
            bar = QBarSet(name)
            for _ in range(7):
                bar.append(random.randint(0, 10))
            series.append(bar)
            bar.hovered.connect(self.handleBarHoverd)
        self._chart.addSeries(series)
        self._chart.createDefaultAxes()
        axis_x = QBarCategoryAxis(self._chart)
        axis_x.append(self.categories)
        self._chart.setAxisX(axis_x, series)
        legend = self._chart.legend()
        legend.setVisible(True)
        for marker in legend.markers():
            marker.clicked.connect(self.handleMarkerClicked)
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)

