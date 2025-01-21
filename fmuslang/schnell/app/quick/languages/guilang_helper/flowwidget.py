from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5 import QtWidgets as QW, QtGui as QG, QtCore as QC


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


class FlowWidget(QWidget):

    def __init__(self, parent=None, widgets=[], *args, **kwargs):
        
        super(FlowWidget, self).__init__(parent, *args, **kwargs)
        self.main_layout = QVBoxLayout()
        self.flow_widget = QWidget(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        # scrollarea gunakan widget yg akan dilayout dg flowLayout
        self.scrollArea.setWidget(self.flow_widget)
        self.flowLayout = FlowLayout(self.flow_widget)

        for widget in widgets:
            self.flowLayout.addWidget(widget)

        self.main_layout.addWidget(self.scrollArea)
        self.setLayout(self.main_layout)

    def clearLayout(self):
        while self.flowLayout.count():
            child = self.flowLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def add_items(self, widgets):
        for widget in widgets:
            self.flowLayout.addWidget(widget)

    def add_item(self, widget):
        self.flowLayout.addWidget(widget)

    def clear_add_items(self, widgets):
        self.clearLayout()
        self.add_items(widgets)
