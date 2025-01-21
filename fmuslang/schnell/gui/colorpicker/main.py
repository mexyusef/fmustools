from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QTextEdit
from pyqt_color_picker import ColorPickerWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        # te = QTextEdit()
        colorPicker = ColorPickerWidget(orientation='vertical')
        lay = QHBoxLayout()
        # lay.addWidget(te)
        lay.addWidget(colorPicker)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
# https://github.com/yjg30737/pyqt-color-picker
