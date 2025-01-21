
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
		self.item.setSizeHint(QSize(self.minimumWidth(), 300))


class CustomButton(QPushButton):
	def __init__(self, item, *args, **kwargs):
		super(CustomButton, self).__init__(*args, **kwargs)
		self.item = item
		self.setCheckable(True)
	def resizeEvent(self, event):
		super(CustomButton, self).resizeEvent(event)
		self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class FoldedListWidget(QListWidget):

	def __init__(self, *args, **kwargs):
		super(FoldedListWidget, self).__init__(*args, **kwargs)
		self.setStyleSheet('#testBtn { min-height:40px; background:green; } ')
		for i in range(3):
			# tiap list item punya 2 komponen: button dan content
			# item = button
			item = QListWidgetItem(self)		
			fold_button = CustomButton(item, 'fold me', self, objectName='testBtn') # set parent dari button = item			
			self.setItemWidget(item, fold_button) # item, button = parent, child
			# item2 = content
			item2 = QListWidgetItem(self)
			anak = WidgetAnak(item2, self) # set parent dari widgetanak = item2
			self.setItemWidget(item2, anak) # item, anak = parent, child
			# buka yg pertama saja...
			if i != 0:
				item2.setHidden(True)
				fold_button.setChecked(True)
			fold_button.toggled.connect(item2.setHidden) # last, sambungkan button di item ke toggle item2


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
