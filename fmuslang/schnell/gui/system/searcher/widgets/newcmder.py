import math, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
# schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)


if __name__ == '__main__':
	from startup import initialize_programming_data
	initialize_programming_data()

from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import get_icon, set_theme
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.gui.system.searcher.widgets.common import BlueButton


class NewCmder(QWidget):

	def __init__(self, parent = None):
		super(NewCmder, self).__init__(parent)
		self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
		# self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
		# self.setAttribute(Qt.WA_TranslucentBackground, True)
		self.setWindowOpacity(0.8)
		self.main_layout = QHBoxLayout(self)

		self.flower = FlowWidget()
		self.main_layout.addWidget(self.flower, 8)

		self.editor = QLineEdit()
		self.editor.setFont(QFont("Consolas", 16))
		self.editor.setStyleSheet('background-color: oldlace; height: 48px;')

		self.button_menu = QMenu('Button')
		self.button_menu.setIcon(get_icon())
		# self.button_menu.addAction(get_icon(), 'Open C:/work/upw/', lambda: os.system(f'code C:/work/upw/'))
		self.button_menu.addAction('Create+fill+set')
		self.button_menu.addAction('Fill+set')
		self.button_menu.addAction('Toggle show/hide')
		self.button_menu.addAction('Ketik')
		self.button_menu.addAction('List')
		self.button_menu.addAction('Hapus kosong')
		self.button_menu.addAction('Set topmost')
		self.button_menu.addAction('Set not topmost')
		self.button_menu.addAction('Set top')
		self.button_menu.addAction('Bring to top')
		self.button_menu.addAction('Minimize')
		self.button_menu.addAction('Maximize')
		self.button_menu.addAction('Restore')
		self.button_menu.addAction('Normal')
		self.button_menu.addAction('Close')

		editor_layout = QVBoxLayout()
		self.main_layout.addLayout(editor_layout, 2)
		self.main_button = BlueButton(self.button_menu, "Menu")
		self.exit_button = BlueButton(None, "Exit")
		self.exit_button.clicked.connect(lambda: qApp.quit())
		button_layout = QHBoxLayout()
		button_layout.addWidget(self.main_button)
		button_layout.addWidget(self.exit_button)
		editor_layout.addWidget(self.editor, 6)
		editor_layout.addLayout(button_layout, 4)

		for i in range(100):
			b = BlueButton(self.button_menu, f"Btn {i}")
			self.flower.add_item(b)

		screen_geometry = QDesktopWidget().screenGeometry(-1)
		self.w,self.h = screen_geometry.width(), screen_geometry.height()
		self.resize_screen_ratio()

		self.setWindowTitle('white blue')
		QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
		self.show()
		self.setStyleSheet("background-color: #ffffff;")

	def resize_screen_ratio(self, wratio=0.8, hratio=1/5, delta = 20):
		lebar, tinggi = int(self.w*wratio), int(self.h*hratio)
		self.resize(lebar, tinggi)
		posx = (self.w - lebar)//2
		posy = self.h - tinggi - delta
		self.move(posx, posy)
		# self.casio.change_size(lebar, tinggi)


def main():
	app = QApplication([])
	w = NewCmder()
	# w.setStyleSheet(background_image_stylesheet)
	w.setStyleSheet("background-color: #ffffff;")
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
