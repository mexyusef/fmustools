from PyQt5.QtCore import (
    QAbstractAnimation,
    QEasingCurve,
    QEvent,
    QPropertyAnimation,
    QRect,
    Qt,
)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

import random


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(500, 500)

        cent_widget = QWidget()
        self.setCentralWidget(cent_widget)

        layout = QVBoxLayout(cent_widget)
        layout.addWidget(MyItem(), alignment=Qt.AlignCenter)


class MyItem(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setBaseSize(200, 250)
        self.setMinimumSize(self.baseSize())
        self.resize(self.baseSize())

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setStyleSheet(
            "background: {}".format(QColor(*random.sample(range(255), 3)).name())
        )

        # Animation
        self.zoom_factor = 1.2

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutSine)
        self.anim.setDuration(250)

    def enterEvent(self, event: QEvent) -> None:

        initial_rect = self.geometry()
        final_rect = QRect(
            0,
            0,
            int(initial_rect.width() * self.zoom_factor),
            int(initial_rect.height() * self.zoom_factor),
        )
        final_rect.moveCenter(initial_rect.center())

        print(f"""
        initial = {initial_rect}
        final = {final_rect}

        {initial_rect.getCoords()}
        {initial_rect.getRect()}
        """)

        self.anim.setStartValue(initial_rect)
        self.anim.setEndValue(final_rect)
        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.start()

    def leaveEvent(self, event: QEvent) -> None:
        self.anim.setDirection(QAbstractAnimation.Backward)
        self.anim.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
# https://stackoverflow.com/questions/66988388/resize-widget-from-center-when-animating-the-size-property
