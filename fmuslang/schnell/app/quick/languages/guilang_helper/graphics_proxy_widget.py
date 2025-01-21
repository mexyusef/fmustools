
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):

    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, points):
        self.titleLabel.setText(title)
        for serie, point in points:
            if serie not in self.Cache:
                item = ToolTipItem(serie.color(), (serie.name() or "-") + ":" + str(point.y()), self)
                self.layout().addWidget(item)
                self.Cache[serie] = item
            else:
                self.Cache[serie].setText(
                    (serie.name() or "-") + ":" + str(point.y()))
            self.Cache[serie].setVisible(serie.isVisible())
        self.adjustSize()


class ToolTipWidgetForBar(QWidget):

    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidgetForBar, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidgetForBar{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, bars):
        self.titleLabel.setText(title)
        for bar, value in bars:
            if bar not in self.Cache:
                item = ToolTipItem(bar.color(), (bar.label() or "-") + ":" + str(value), self)
                self.layout().addWidget(item)
                self.Cache[bar] = item
            else:
                self.Cache[bar].setText(
                    (bar.label() or "-") + ":" + str(value))
            brush = bar.brush()
            color = brush.color()
            self.Cache[bar].setVisible(color.alphaF() == 1.0)
        self.adjustSize()


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, mode='line', *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)

        self.tipWidget = ToolTipWidget()
        if mode == 'bar':
            self.tipWidget = ToolTipWidgetForBar()

        self.setWidget(self.tipWidget)
        self.hide()

    def show(self, title, points, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, points)
        super(GraphicsProxyWidget, self).show()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()
