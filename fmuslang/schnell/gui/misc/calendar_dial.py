import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QCalendarWidget, QDial, QVBoxLayout)
from PyQt5.QtCore import QDate

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(700, 500)

		self.dial = QDial()
		self.dial.resize(400, 400)
		self.dial.setMinimum(0)
		self.dial.setMaximum(100)
		self.dial.valueChanged.connect(self.update_calendar)

		self.calendar = QCalendarWidget()
		self.calendar.setGridVisible(True)
		self.calendar.setSelectedDate(QDate.currentDate())

		layout = QVBoxLayout()
		layout.addWidget(self.calendar)
		layout.addWidget(self.dial)
		self.setLayout(layout)

	def update_calendar(self):
		print(QDate.currentDate().addDays(self.dial.value()).getDate())
		self.calendar.setSelectedDate(QDate.currentDate().addDays(self.dial.value()))

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = MainWindow()
	demo.show()

	sys.exit(app.exec_())
#
# https://gist.github.com/DataSolveProblems/c0ea695c02edec65809eea5b0edf11a9
