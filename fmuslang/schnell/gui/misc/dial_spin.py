# https://gist.github.com/DataSolveProblems/df711e8eb47f38abb06f70fc35597f8b

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDial, QSpinBox)
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(400, 300)

		f = QFont('', 16)

		dial = QDial(self)
		dial.resize(175, 175)
		dial.move(30, 30)
		dial.setNotchesVisible(True)

		spinbox = QSpinBox(self)
		spinbox.resize(50, 50)
		spinbox.move(250, 100)
		spinbox.setFont(f)

		dial.valueChanged.connect(spinbox.setValue)
		spinbox.valueChanged.connect(dial.setValue)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = MainWindow()
	demo.show()

	sys.exit(app.exec_())
#
