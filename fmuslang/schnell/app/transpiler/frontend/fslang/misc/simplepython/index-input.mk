--% index/fmus
simpleton,d(/mk)
	main.py,f(e=__FILE__=/main.py)
	clock.py,f(e=__FILE__=/clock.py)
	background.py,f(e=__FILE__=/background.py)
--#

--% /background.py
import wx

# Create a .png image with something drawn on a white background
# and put the path to it here.
IMAGE_PATH = '/home/usef/Pictures/oprek.png'

class ShapedFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Shaped Window", style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER )
		self.hasShape = False
		self.delta = wx.Point(0,0)

		# Load the image
		image = wx.Image(IMAGE_PATH, wx.BITMAP_TYPE_PNG)
		image.SetMaskColour(255,255,255)
		image.SetMask(True)            
		self.bmp = wx.BitmapFromImage(image)

		self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
		dc = wx.ClientDC(self)
		dc.DrawBitmap(self.bmp, 0,0, True)
		self.SetWindowShape()
		self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
		self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
		self.Bind(wx.EVT_MOTION, self.OnMouseMove)
		self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)

	def SetWindowShape(self, evt=None):
		#r = wx.RegionFromBitmap(self.bmp)
		r = wx.Region(self.bmp)
		self.hasShape = self.SetShape(r)

	def OnDoubleClick(self, evt):
		if self.hasShape:
			self.SetShape(wx.Region())
			self.hasShape = False
		else:
			self.SetWindowShape()

	def OnPaint(self, evt):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.bmp, 0,0, True)

	def OnExit(self, evt):
		self.Close()

	def OnLeftDown(self, evt):
		self.CaptureMouse()
		pos = self.ClientToScreen(evt.GetPosition())
		origin = self.GetPosition()
		self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

	def OnMouseMove(self, evt):
		if evt.Dragging() and evt.LeftIsDown():
			pos = self.ClientToScreen(evt.GetPosition())
			newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
			self.Move(newPos)

	def OnLeftUp(self, evt):
		if self.HasCapture():
			self.ReleaseMouse()


if __name__ == '__main__':
	app = wx.PySimpleApp()
	ShapedFrame().Show()
	app.MainLoop()
--#

--% /clock.py
import PyQt5, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import (QsciScintilla, QsciLexerCustom)
from PyQt5.QtCore import (
	pyqtSlot as qslot,
	pyqtSignal as qsignal,
	Qt as K,
	QCoreApplication,	
	QEvent, 
	QPoint,
	QTime, 
	QTimer,
	
)
from PyQt5.QtGui import (
	QBrush,
	QIcon,
	QPalette,
	QPainter,
	QPen,
	QPixmap,
	QPolygon,
	QKeySequence as kunci,
)
from PyQt5.QtWidgets import (
	QApplication,
	QDialog,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QMainWindow,
	QMenu,
	QPushButton,
	QScrollArea,
	QShortcut,
	QTextEdit,
	QVBoxLayout,
	QWidget,
	qApp,
)

button_style = """
QPushButton {
	background-color: none;
	color: white; border-radius: 6px;
	font-size: 18px;
}
"""

lebar = 1000
tinggi = 700
tengahx = 150
tengahy = 60
kalimat = 'hello there'
lebartext = 400
tinggitext = 100
textx = (lebar - lebartext) // 2
texty = (tinggi - tinggitext) // 2
# utk jam
nilai_opaque = 0.98
# xstart = 1200
# ystart = 70
w = 400
h = 400
xstart = (lebar - w) // 2
ystart = (tinggi - h) // 2


class MyClock(QWidget):
	def __init__(self, parent=None):
		super(MyClock, self).__init__(parent)
		self.parent = parent
		timer = QTimer(self)
		timer.timeout.connect(self.update)
		timer.start(1000)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.X11BypassWindowManagerHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		# setting window geometry
		self.setGeometry(xstart, ystart, w, h)
		# jarum jam berbentuk segitiga
		self.jarum_jam = QtGui.QPolygon([QPoint(6, 7), QPoint(-6, 7), QPoint(0, -50)])
		self.jarum_menit = QPolygon([QPoint(6, 7), QPoint(-6, 7), QPoint(0, -70)])
		self.jarum_detik = QPolygon([QPoint(1, 1), QPoint(-1, 1), QPoint(0, -90)])
		self.warna_jam = K.blue
		self.warna_menit = K.green
		self.warna_detik = K.red
		self.warna_mark = K.yellow

	def paintEvent(self, event):
		ukuran = min(self.width(), self.height())

		painter = QPainter(self)
		painter.setOpacity(nilai_opaque)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(self.width() / 2, self.height() / 2)
		painter.scale(ukuran / 200, ukuran / 200)

		def drawPointer(color, rotation, pointer):
			painter.setBrush(QBrush(color))
			painter.save()
			painter.rotate(rotation)
			painter.drawConvexPolygon(pointer)
			painter.restore()
		
		ticking = QTime.currentTime()
		# set current pen as no pen
		painter.setPen(QtCore.Qt.NoPen)
		# draw each hand
		drawPointer(self.warna_jam, (30 * (ticking.hour() + ticking.minute() / 60)), self.jarum_jam)
		drawPointer(self.warna_menit, (6 * (ticking.minute() + ticking.second() / 60)), self.jarum_menit)
		drawPointer(self.warna_detik, (6 * ticking.second()), self.jarum_detik)
		# drawing background
		# ini persiapan bikin mark 5 menit?
		painter.setPen(QPen(self.warna_mark))
		for i in range(0, 60):
			if (i % 5) == 0:
				# drawing background lines
				painter.drawLine(87, 0, 97, 0)
			painter.rotate(6)
		painter.end()


class MainWindow(QMainWindow):
	def mousePressEvent(self, event):
		# QtGui.qApp.quit()
		print('stopping...')
		# QCoreApplication.quit()
		self.close_window()
		QApplication.processEvents()

	def __init__(self):
		QMainWindow.__init__(self)

		# < Styles >
		self.background_style_css = "background-color: rgba(33, 130, 133, 100); border-radius: 4px;"
		self.close_button_style_css = button_style
		# </ Styles >

		# < Global Settings >
		self.setFixedSize(lebar, tinggi)
		self.move(tengahx, tengahy)
		# </ Global Settings >

		# < Main Style >
		self.main_back = QLabel(self)
		self.main_back.resize(lebar, tinggi)
		self.main_back.setStyleSheet(self.background_style_css)
		# </ Main Style >

		# < Text Label >
		# self.text_label = QLabel(self)
		# self.text_label.move(textx, texty)
		# self.text_label.resize(lebartext, tinggitext)
		# self.text_label.setText(kalimat)
		# < Text Label >
		self.jam = MyClock(self)

		# < Header Style >
		self.setAttribute(K.WA_TranslucentBackground)
		# This Line Set Your Window Always on To
		self.setWindowFlags(K.SplashScreen | K.FramelessWindowHint | K.WindowStaysOnTopHint)
		# </ Header Style >

	def terminal_ask(self):
		while True:
			print("If you want to close this window, type stop: ")
			get_input = input()
			if get_input.lstrip().rstrip().lower() == "stop":
				self.close_window()
			else:
				print("Invalid Syntax, Try it again.")
			QApplication.processEvents()

	def close_window(self):
		self.close()
		sys.exit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	window.terminal_ask()
	sys.exit(app.exec_())
--#

--% /main.py
def main():
	pass

if __name__ == '__main__':
  main()
--#
