
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FoldButton(QPushButton):
    def __init__(self, item, *args, **kwargs):
        super(FoldButton, self).__init__(*args, **kwargs)
        self.item = item
        self.setCheckable(True)
    def resizeEvent(self, event):
        super(FoldButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class FoldedListWidget(QListWidget):
    def __init__(self, *args, **kwargs):
        super(FoldedListWidget, self).__init__(*args, **kwargs)
        self.setStyleSheet('#testBtn { min-height:40px; background:green; } ')

__TEMPLATE_WIDGET_ITEMS__
