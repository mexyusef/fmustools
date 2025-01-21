#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年9月25日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: ShadowEffect
@description: 
"""
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit, QApplication



class AnimationShadowEffect(QGraphicsDropShadowEffect):

    def __init__(self, color, *args, **kwargs):
        super(AnimationShadowEffect, self).__init__(*args, **kwargs)
        self.setColor(color)
        self.setOffset(0, 0)
        self.setBlurRadius(0)
        self._radius = 0
        self.animation = QPropertyAnimation(self)
        self.animation.setTargetObject(self)
        self.animation.setDuration(2000)  # 一次循环时间
        self.animation.setLoopCount(-1)  # 永久循环
        self.animation.setPropertyName(b'radius')
        # 插入值
        self.animation.setKeyValueAt(0, 1)
        self.animation.setKeyValueAt(0.5, 30)
        self.animation.setKeyValueAt(1, 1)

    def start(self):
        self.animation.start()

    def stop(self, r=0):
        # 停止动画并修改半径值
        self.animation.stop()
        self.radius = r

    @pyqtProperty(int)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.setBlurRadius(r)

class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)

        # 绿色边框
        labelGreen = QLabel(self, pixmap=QPixmap('../clock/fmus-fm.png').scaled(100, 100))
        layout.addWidget(labelGreen)
        aniGreen = AnimationShadowEffect(Qt.darkGreen, labelGreen)
        labelGreen.setGraphicsEffect(aniGreen)
        aniGreen.start()

        # 红色边框,圆形图片
        labelRed = QLabel(self)
        labelRed.setMinimumSize(100, 100)
        labelRed.setMaximumSize(100, 100)
        labelRed.setStyleSheet('border-image: url(../clock/fmus-fm.png);border-radius: 50px;')
        layout.addWidget(labelRed)
        aniRed = AnimationShadowEffect(Qt.red, labelGreen)
        labelRed.setGraphicsEffect(aniRed)
        aniRed.start()

        # 蓝色边框button
        button = QPushButton('button', self)
        aniButton = AnimationShadowEffect(Qt.blue, button)
        layout.addWidget(button)
        button.setGraphicsEffect(aniButton)
        button.clicked.connect(aniButton.stop) # 按下button停止动画
        aniButton.start()

        # 青色边框输入框
        lineedit = QLineEdit(self)
        aniEdit = AnimationShadowEffect(Qt.cyan, lineedit)
        layout.addWidget(lineedit)
        lineedit.setGraphicsEffect(aniEdit)
        aniEdit.start()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
