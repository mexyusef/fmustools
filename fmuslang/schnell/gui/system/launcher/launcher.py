#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtWidgets import (
	QApplication,
	QCheckBox,
	QDesktopWidget,
	QDialog,
	QFormLayout,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMessageBox,
	QMenu,
	QPushButton,
	QScrollArea,
	QShortcut,
	QTextEdit,
	QToolTip,
	QVBoxLayout,
	QWidget,
	qApp,
)


default_stylesheet = """
background-color:skyblue;
"""

def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, delta = 60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    lebar, tinggi = int(screenw*ratio),int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)


class BlockWidget(QWidget):

    def __init__(self, parent=None, angka_mulai=0, style_sheet=default_stylesheet, effect=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.angka_mulai = angka_mulai
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents) # scrollAreaWidgetContents ber-layout = grid
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        if effect:
            self.setGraphicsEffect(effect)

        rows = 20
        cols = 5
        for i in range(rows):
            for j in range(cols):
                btn = QPushButton(f"{self.angka_mulai}")
                
                btn.setStyleSheet(style_sheet)
                btn.setToolTip(f'This is <i>button</i> number <b>{i}, {j}</b> or <u>{self.angka_mulai}</u>.')

                aniButton = AnimationShadowEffect(Qt.blue, btn)
                btn.setGraphicsEffect(aniButton)
                aniButton.start()
                # btn.clicked.connect(self.button_clicked)
                self.gridLayout.addWidget(btn, i, j)

                self.angka_mulai += 1

        lay = QVBoxLayout()
        lay.addWidget(self.scrollArea)
        self.setLayout(lay)
        # self.setMinimumWidth(500)

class AnimationShadowEffect(QGraphicsDropShadowEffect):

    def __init__(self, color, *args, **kwargs):
        super(AnimationShadowEffect, self).__init__(*args, **kwargs)
        self.setColor(color)
        self.setOffset(0, 0)
        self.setBlurRadius(0)
        self._radius = 0
        self.animation = QPropertyAnimation(self)
        self.animation.setTargetObject(self)
        self.animation.setDuration(2000)
        self.animation.setLoopCount(-1)
        self.animation.setPropertyName(b'radius')
        self.animation.setKeyValueAt(0, 1)
        self.animation.setKeyValueAt(0.5, 30)
        self.animation.setKeyValueAt(1, 1)

    def start(self):
        self.animation.start()

    def stop(self, r=0):
        self.animation.stop()
        self.radius = r

    @pyqtProperty(int)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.setBlurRadius(r)

class LauncherWindow(QWidget):

    def __init__(self, *args, **kwargs):

        super(LauncherWindow, self).__init__(*args, **kwargs)

        layout = QHBoxLayout(self)

        # labelGreen = QLabel(self, pixmap=QPixmap('../clock/fmus-fm.png').scaled(100, 100))
        # layout.addWidget(labelGreen)
        # aniGreen = AnimationShadowEffect(Qt.darkGreen, labelGreen)
        # labelGreen.setGraphicsEffect(aniGreen)
        # aniGreen.start()

        # labelRed = QLabel(self)
        # labelRed.setMinimumSize(100, 100)
        # labelRed.setMaximumSize(100, 100)
        # labelRed.setStyleSheet('border-image: url(../clock/fmus-fm.png);border-radius: 50px;')
        # layout.addWidget(labelRed)
        # aniRed = AnimationShadowEffect(Qt.red, labelGreen)
        # labelRed.setGraphicsEffect(aniRed)
        # aniRed.start()

        # button = QPushButton('button', self)


        bw = BlockWidget(self)
        # layout.addWidget(button)
        # button.setGraphicsEffect(aniButton)
        # button.clicked.connect(aniButton.stop) # 按下button停止动画
        layout.addWidget(bw)

        # lineedit = QLineEdit(self)
        # aniEdit = AnimationShadowEffect(Qt.cyan, lineedit)
        # layout.addWidget(lineedit)
        # lineedit.setGraphicsEffect(aniEdit)
        # aniEdit.start()
        QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())

def main():
    app = QApplication(sys.argv)
    w = LauncherWindow()
    w.setWindowTitle('Launcher')

    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w, screenw, screenh, ratio=3/4)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

