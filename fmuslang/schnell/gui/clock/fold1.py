
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
	QWidget, 
	QPushButton, 
	QFormLayout,
	QLineEdit, 
	QListWidget,
	QListWidgetItem,
	QCheckBox
)

from PyQt5.QtWidgets import QDesktopWidget
# from PyQt5.QtCore import QDesktopWidget
# from PyQt5.QtGui import QDesktopWidget
class WidgetAnak(QWidget):
	def __init__(self, item, *args, **kwargs):
		super(WidgetAnak, self).__init__(*args, **kwargs)
		self.item = item # jk gak handle resize, gak keliatan

		layout = QFormLayout(self)
		layout.addRow('satu', QLineEdit(self))
		layout.addRow('dua', QLineEdit(self))
		layout.addRow('tiga', QLineEdit(self))
		layout.addRow('empat', QLineEdit(self))
		layout.addRow('lima', QLineEdit(self))
		layout.addRow('enam', QLineEdit(self))
		layout.addRow('tujuh', QLineEdit(self))
		layout.addRow('delapan', QLineEdit(self))
		layout.addRow('sembilan', QLineEdit(self))
		layout.addRow('sepuluh', QLineEdit(self))

	def resizeEvent(self, event):
		super(WidgetAnak, self).resizeEvent(event)
		# print('[fold1 = WidgetAnak] tinggiku adlh:', self.height())
		# jk gak handle resize, gak keliatan
		# self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))
		self.item.setSizeHint(QSize(self.minimumWidth(), 300))

	# def hideChild(self, v):
	# 	'''
	# 	handle setHidden(true/false)
	# 	'''
	# 	# self.button.setVisible(not v)
	# 	self.adjustSize()


class CustomButton(QPushButton):
	def __init__(self, item, *args, **kwargs):
		super(CustomButton, self).__init__(*args, **kwargs)
		self.item = item
		self.setCheckable(True)

	def resizeEvent(self, event):
		super(CustomButton, self).resizeEvent(event)
		# print('[fold1 = CustomButton] tinggiku adlh:', self.height())
		# self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))
		self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class FoldedListWidget(QListWidget):

	def buat_anak(self, i):
		item = QListWidgetItem(self)
		self.btn.toggled.connect(item.setHidden)
		anak = WidgetAnak(item, self)
		self.setItemWidget(item, anak)
		# buka yg pertama saja...
		if i != 0:
			item.setHidden(True)
			self.btn.setChecked(True) # gimana cara toggle programmatically

	def __init__(self, *args, **kwargs):
		super(FoldedListWidget, self).__init__(*args, **kwargs)
		self.setStyleSheet('#testBtn{min-height:40px; background:green;}')
		for i in range(3):
			item = QListWidgetItem(self)
			self.btn = CustomButton(item, 'fold', self, objectName='testBtn')
			# self.btn = QPushButton('fold', self)
			# self.btn.objectName='testBtn'
			# self.btn.setCheckable(True)
			# self.btn.item = item
			self.setItemWidget(item, self.btn)
			self.buat_anak(i)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	# app.setStyleSheet('#testBtn{min-height:40px; background:green;}')
	wnd = FoldedListWidget()
	screen_geometry = QDesktopWidget().screenGeometry(-1)
	w,h = screen_geometry.width(), screen_geometry.height()
	wnd.resize(int(w*3/4), int(h*3/4))
	wnd.show()
	sys.exit(app.exec_())
