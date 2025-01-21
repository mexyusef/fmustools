#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QSize, QTimer, pyqtSlot
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication,    
    QColorDialog,
    QDialog,
    QGraphicsDropShadowEffect,      
    QGridLayout,
    QPushButton,
    QSpacerItem,
    QSizePolicy, 
    QVBoxLayout,
    QWidget,

    qApp,
)


Stylesheet = """
#Custom_Widget {
    background: white;
    border-radius: 10px;
}

#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: white;
    background: red;
}
QSpacerItem {
    background: green;
}
"""


class MyColorPicker(QWidget):
    """
    https://stackoverflow.com/questions/48527705/pyside-qcolordialog-signals
    """
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.color_chooser = QColorDialog()
        color = self.color_chooser.getColor()
        if color.isValid():
            print(f"""[{color}]
            name: {color.name()}
            R {color.red()} G {color.green()} B {color.blue()}            
            RGB {color.rgb()} RGBA {color.rgba()} torgb as QColor: {color.toRgb()}
            A {color.alpha()} H {color.hue()} L {color.lightness()} S {color.saturation()}            
            """)
            # value: {color.value()}
            # {color.colorNames()}
            # qApp.quit()
            # QApplication.instance().quit()
        sys.exit(0)

    # def __init__(self, *args, **kwargs):
    #     QWidget.__init__(self, *args, **kwargs)
    #     self.color_chooser = QColorDialog()
    #     if self.color_chooser.exec_() == QColorDialog.Accepted:
    #         print(self.color_chooser.currentColor())

class Dialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(Stylesheet)

        self.initUi()

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

    def initUi(self):
        layout = QVBoxLayout(self)
        # 重点： 这个widget作为背景和圆角
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout.addWidget(self.widget)

        # 在widget中添加ui
        layout = QGridLayout(self.widget)
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # row 1
        layout.addItem(spacer1, 0, 0) # layout item = spacer
        layout.addWidget(QPushButton('r', self, clicked=self.accept, objectName='closeButton'), 0, 1)
        
        # row 2
        # spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # layout.addItem(spacer2, 1, 0)
        # widget1 = QWidget()
        # widget1.setStyleSheet('background: green;')
        # widget1 = QColorDialog()
        widget1 = MyColorPicker()
        layout.addWidget(widget1, 1, 0, -1, 2)
        # TODO: connect kan quit dari widget1 ke closing our dialog...

    def sizeHint(self):
        return QSize(600, 400)

    # def accept(self) -> None:
    #     super().accept()
    #     qApp.quit()


def main():
    app = QApplication(sys.argv)
    w = Dialog()
    w.raise_()
    w.exec_()
    # QTimer.singleShot(200, app.quit)
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    main()
