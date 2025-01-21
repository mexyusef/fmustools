# import os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyperclip, functools
from .flowwidget import FlowWidget


class ButtonWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
QPushButton {
    background-color: beige;
    font-size: 14px;
    height: 32px;
    border-radius: 3px;
    border: 1px solid darkblue;
}
QPushButton:hover {
    background-color: bisque;
}
""")
        self.initUI()

    def initUI(self):
        all_icons = [i for i in dir(QStyle) if i.startswith('SP_')]
        self.main_layout = QVBoxLayout()
        flow0 = FlowWidget()
        widgets = []
        for index,icon_name in enumerate(all_icons):
            icon_obj = getattr(QStyle, icon_name)
            the_icon = QApplication.style().standardIcon(icon_obj)
            # b = QPushButton(f"[{index}] {icon_name}", self)
            b = QPushButton(icon_name, self)
            b.setIcon(the_icon)
            b.setProperty('nama', icon_name)
            # b.setStyleSheet(f'background-color: beige; font-size: 12px; height: 32px;')
            b.clicked.connect(functools.partial(pyperclip.copy, f"QApplication.style().standardIcon(QStyle.{icon_name})"))
            widgets.append(b)
        flow0.add_items(widgets)
        self.main_layout.addWidget(flow0)
        self.setLayout(self.main_layout)
