import datetime, math, os, random, string, sys, time
from pyqtkeybind import keybinder
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from pathlib import Path
sidoarjodir = r'c:\users\usef\work\sidoarjo'
SIDOARJODIR = sidoarjodir
sys.path.append(sidoarjodir)

ICON_FILEPATH = os.path.join(SIDOARJODIR, 'assistant.ico')

import ctypes
myappid = 'schnell.gui.fmusserver.0.0.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == '__main__':
	from startup import initialize_programming_data
	initialize_programming_data()


from constants import background_image_stylesheet
from schnell.app.audioutils import denger, speak, angka
from schnell.app.dirutils import joiner
from schnell.app.datetimeutils import jam, timestamp_for_file, menit, seconds_till_next_hour, seconds_till_next_minutes
from schnell.app.printutils import indah3
from schnell.app.exceptionutils import print_err
from schnell.creator.context import context as global_context
from schnell.creator.repl_language.replify import replify_check_language
from schnell.gui.system.searcher.widgets.common import get_icon, about_qt, set_theme, context_menu_stylesheet
from schnell.gui.system.searcher.widgets.common import resize_screen_ratio_wrapper_simple
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget


from fmuseditor import FmusEditor, FmusEditorWrapper


main_button_style = """
#MainButton {
	/* color: aquamarine; */
	color: burlywood;
	/* background-color: royalblue; */
	background-color: navy;
	/* Limit min and max size */
	/* min-width: 96px; */
	/* max-width: 96px; */
	/* padding-left: 20px; */
	/* padding-right: 20px; */
	/* margin-right: 10px; */
	font-size: 14px;

	/* min-height: 96px; */
	max-height: 32px;
	border-radius: 12px; /* round */
	border-bottom: 2px solid #663399;
}

#MainButton:hover {
	background-color: #64b5f6;
}

#MainButton:pressed {
	background-color: #bbdefb;
}
"""


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


class AnalogClock(QLabel):

	def __init__(self,parent  =None):
		super(AnalogClock,self).__init__(parent)
		self.timer = QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(1000)

	def textRectF(self, radius, pointsize, angle):
		recf = QRectF()
		recf.setX(radius*math.cos(angle*math.pi/180.0)-pointsize*2)
		recf.setY(radius*math.sin(angle*math.pi/180.0)-pointsize/2.0)
		recf.setWidth(pointsize*4)  #Width Height
		recf.setHeight(pointsize)
		return recf

	def paintEvent(self, event):
		panjang_jam = -50
		panjang_menit = -65
		panjang_detik = -80
		hour_points = [QPoint(5,8), QPoint(-5,8), QPoint(0,panjang_jam)]
		minute_points = [QPoint(5,8), QPoint(-5,8), QPoint(0,panjang_menit)]
		second_points = [QPoint(5,8), QPoint(-5,8), QPoint(0,panjang_detik)]

		hour_color = QColor(45, 40, 168, 200)
		minute_color = QColor(30, 30, 127, 150)
		second_color = QColor(46, 42, 145, 150)  # QColor(0,160,230,150)

		min_len = min(self.width(),self.height())
		time = QTime.currentTime() #get current time
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(self.width()/2,self.height()/2)  #Pan to center of window
		painter.scale(min_len/200.0,min_len/200.0)  #scaling

		#----------jarum jam------------
		painter.setPen(Qt.NoPen)
		painter.setBrush(hour_color)#color
		painter.save()
		# according to 1 hour = 30°, rotate counterclockwise in the direction of water quality
		painter.rotate(30.0*((time.hour()+time.minute()/60.0)))
		painter.drawConvexPolygon(QPolygon(hour_points))
		painter.restore()  # save Exit to reset the brush

		painter.setPen(hour_color)
		# draw hour line(360/12 = 30 degrees)
		for i in range(12):
			painter.drawLine(88,0,96,0)  #draw horizontal lines
			painter.rotate(30.0)  # Rotate at the original rotation angle;

		radius = 100
		font = painter.font()
		font.setBold(True)
		painter.setFont(font)
		pointSize = font.pointSize()
		# print(pointSize)

		# draw hour text
		for i in range(12):
			nhour = i + 3  # from level 3 point to draw
			if (nhour>12):
				nhour -= 12
			painter.drawText(self.textRectF(radius*0.75, pointSize*3, i*30), Qt.AlignCenter, str(nhour))

		# draw the minute hand;
		painter.setPen(Qt.NoPen)
		painter.setBrush(minute_color)
		painter.save()

		# 1 menit = 6 derajat
		painter.rotate(6.0*(time.minute()+time.second()/60.0))
		painter.drawConvexPolygon(QPolygon(minute_points))
		painter.restore()

		# titik menit
		painter.setPen(minute_color)
		for i in range(60):
			if(i%5 !=0):
				painter.drawLine(92,0,96,0)
			painter.rotate(6.0)

		# jarum detik
		painter.setPen(Qt.NoPen)
		painter.setBrush(second_color)
		painter.save()
		# garis detik
		painter.rotate(6.0*time.second())
		painter.drawConvexPolygon(QPolygon(second_points))
		painter.restore()

		painter.setPen(second_color)
		for i in range(360):
			if (i % 5 != 0 or i % 30 != 0):
				painter.drawLine(94,0,96,0)
			painter.rotate(1.0)


class DigitalClock(QWidget):

	def change_size(self, lebar, tinggi):
		lebar = int(lebar / 3.2)
		tinggi = int(tinggi / 4.5)
		# print(f'DigitalClock => lebar {lebar}, tinggi {tinggi}')
		self.lcdNumber.setGeometry(QRect(5, 5, lebar, tinggi))

	def __init__(self, parent):
		super(DigitalClock,self).__init__(parent)

		self.lcdNumber = QLCDNumber(self)
		# self.lcdNumber.setStyleSheet('border: 1px solid blue; color: yellow;')
		self.lcdNumber.setStyleSheet('color: chartreuse; background-color: darkblue; padding-left: 10px; padding-right: 10px;')
		lebar = parent.width()
		tinggi = parent.height()
		# # print(f'lebar {lebar}, tinggi {tinggi}')
		# self.lcdNumber.setGeometry(QRect(0, 0, lebar, tinggi))
		# print(f'DigitalClock parent => lebar {lebar}, tinggi {tinggi}')
		self.change_size(lebar, tinggi)
		# self.lcdNumber.setGeometry(QRect(0, 0, 100, 40))
		# self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.lcdNumber.setContextMenuPolicy(Qt.DefaultContextMenu)
		self.lcdNumber.setFrameShape(QFrame.NoFrame)
		self.lcdNumber.setSmallDecimalPoint(False)
		self.lcdNumber.setDigitCount(8)
		# self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
		self.lcdNumber.setProperty("value", 2021.0)
		self.lcdNumber.setObjectName("lcdNumber")

		# https://stackoverflow.com/questions/14478574/changing-the-digit-color-of-qlcd-number
		# palette = self.lcdNumber.palette()
		# palette.setColor(palette.Background, QColor(0, 170, 255))
		# self.lcdNumber.setPalette(palette)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAcceptDrops(True)
		self.lcdNumber.display('00:00:00')
		time_slot = QTimer(self)
		time_slot.timeout.connect(self.clock_ticking)
		time_slot.start(1000)

		# tiap hour 00
		self.play_sound_timer = QTimer(self)
		self.play_sound_timer.timeout.connect(self.play_sound)
		self.play_sound_timer.setInterval(1000*60*60)
		# https://stackoverflow.com/questions/58893977/how-to-align-a-qtimer-interval-with-the-system-time
		QTimer.singleShot(seconds_till_next_hour(nexthour=1, millisecond=True), self.startAlarm)
		QTimer.singleShot(seconds_till_next_minutes(nextminute=1, millisecond=True), self.startAlarm)

		# tiap minute 30
		self.thirty_minutes = QTimer(self)
		self.thirty_minutes.setInterval(1000*60*60)
		self.thirty_minutes.timeout.connect(self.play_thirty)
		QTimer.singleShot(seconds_till_next_minutes(nextminute=30, millisecond=True), self.play_thirty_start)

	def play_thirty_start(self):
		self.thirty_minutes.start()
		self.play_thirty()

	def play_thirty(self):
		if not global_context['clock_reminder']:
			return
		denger('c:/windows/media/tada.wav')
		speak(f'Thirty minutes has passed since {angka(jam())}. Please stand up and count to thirty.')

	def startAlarm(self):
		self.play_sound_timer.start()
		# self.play_sound('I hope you are ready for the next adventure...')
		self.play_sound()

	def play_sound(self, kalimat=None):
		if not global_context['clock_reminder']:
			return
		print('playing sound at', timestamp_for_file())
		denger()
		if not kalimat:
			from schnell.app.writers.file_handler import ambil_acak
			katakata = ambil_acak()
			print(f"[schnell.gui.fmusserver][play_sound] {katakata}")
			# pastikan masuk ke jam berikutnya dulu
			_menit = menit()
			while not _menit in [0, '0', '00'] and int(_menit)>57:  # 58,59 blocking
				print(f"Sleeping 1s krn menit '{_menit}' belum '00' pada jam '{jam()}'")
				time.sleep(1.0)
				_menit = menit()
			if _menit in ['00', '01']:
				speak(f"Hello Yusef, the time is now {angka(jam())} o'clock. Please keep that in mind, brother! Please stand up and count to sixty. Then remember these words {katakata}")
			else:
				speak(f"Hello Yusef, the time is now {angka(jam())} hour and {angka(_menit)} minutes. Remember that, brother! Please stand up and count to sixty. Then remember these words {katakata}")
		else:
			speak(kalimat)

	def clock_ticking(self):
		time_format = QTime.currentTime()
		time_format = time_format.toString("hh:mm:ss")
		self.lcdNumber.display(time_format)
		QApplication.processEvents()


class ReplInput(QLineEdit):
	def __init__(self, query_searching, history=[], minwidth=0, cssminwidth=50, cssminheight=30):
		super().__init__()
		# if minwidth > 0:
		# 	self.setMaximumWidth(minwidth)
		self.setMinimumWidth(80)
		# self.setMaximumWidth(80)
		self.returnPressed.connect(query_searching)
		# self.installEventFilter(self)
		self.setStyleSheet(f"height: {cssminheight}px; min-width: {cssminwidth}px; font-size: 16px; font-family: Consolas; background-color: oldlace;")
		self.history = history
		self.history_pointer = 0

	def keyPressEvent(self, event):
		super().keyPressEvent(event)
		if self.history:
			# curtext = self.text()
			key = event.key()
			# key_modifiers = PyQt5.QtWidgets.QApplication.keyboardModifiers()
			if key == Qt.Key_Up:
				# self.history_pointer -= 1 if self.history_pointer>0 else len(self.history)-1
				if self.history_pointer>0:
					self.history_pointer -= 1
				else:
					self.history_pointer = len(self.history)-1
				self.setText(self.history[self.history_pointer])
			elif key == Qt.Key_Down:
				# self.history_pointer += 1 if self.history_pointer<len(self.history) else 0
				if self.history_pointer<len(self.history)-1:
					self.history_pointer += 1
				else:
					self.history_pointer = 0
				self.setText(self.history[self.history_pointer])


def sidoarjo_menu(self, get_icon):
	self.sidomuncul = QMenu('Sidoarjo', self)
	self.sidomuncul.setIcon(get_icon())
	self.sidomuncul.addAction(get_icon(), 'Open sidoarjo', lambda: os.system(f'code {SIDOARJODIR}/'))
	return self.sidomuncul


class LCDLabelExample(QWidget):
	def __init__(self, tulisan):
		super().__init__()
		self.text = tulisan
		self.init_ui()

	def init_ui(self):
		self.setStyleSheet('color: chartreuse; background-color: darkblue; padding: 2px 5px;')
		lcd_label = QLabel(self.text)
		# Set a custom font for the QLabel
		lcd_font = QFont("LCD", 10, QFont.Bold)  # You can change "LCD" to other available fonts
		lcd_label.setFont(lcd_font)

		# Create a layout and add the QLabel to it
		layout = QVBoxLayout()
		layout.addWidget(lcd_label)
		# Set the layout for the main window
		self.setLayout(layout)

		# # Set the window properties
		# self.setWindowTitle(self.text)
		# self.setGeometry(100, 100, 300, 100)
		# # Show the window
		# self.show()


class CornerWidget(QWidget):
	def __init__(self, parent = None):
		super(CornerWidget, self).__init__(parent)
		self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

		self.setWindowOpacity(0.95)  # jadi jelek utk editor

		self.main_layout = QHBoxLayout(self)
		self.rolex = AnalogClock(self)
		self.right_pane_layout = QVBoxLayout()

		self.casio = DigitalClock(self)
		casioEffect = AnimationShadowEffect(Qt.blue, self.casio)
		self.casio.setGraphicsEffect(casioEffect)
		casioEffect.start()
		
		# utk button with date
		self.sidoarjo_menu = sidoarjo_menu(self, get_icon)
		self.sidoarjo_menu.setStyleSheet(context_menu_stylesheet)
		# utk repl inputter
		self.history = []
		self.completer = QCompleter(self.history)
		self.completer.setCompletionMode(QCompleter.PopupCompletion)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)

		main_button_label = datetime.datetime.today().strftime('%a %d %b %Y')
		# self.label_date = QLabel(main_button_label)
		self.label_date = LCDLabelExample(main_button_label)
		# self.button_with_date = QPushButton(main_button_label, self)
		# self.main_button_menu = QMenu(self)
		# # lihat C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\clock.py
		# # utk pengisian self.main_button_menu
		# self.button_with_date.setMenu(self.main_button_menu)
		# self.button_with_date.setObjectName('MainButton')
		# self.button_with_date.setStyleSheet(main_button_style)

		self.inputter = ReplInput(self.query_searching, self.history)
		self.inputter.setCompleter(self.completer)


		self.right_pane_layout.addWidget(self.casio)  # analog clock at top
		self.right_pane_layout.addWidget(self.inputter)  # repl input at middle
		self.right_pane_layout.addWidget(self.label_date)
		# self.right_pane_layout.addWidget(self.button_with_date)  # button with date at bottom

		self.previous_main_widget = QWidget()
		self.previous_main_layout = QHBoxLayout(self.previous_main_widget)
		self.previous_main_layout.addWidget(self.rolex, stretch=5)  # analog clock
		self.previous_main_layout.addLayout(self.right_pane_layout, stretch=5)  # digital clock+date

		self.main_widget = QTabWidget(self)
		self.main_widget.addTab(self.previous_main_widget, 'Clock')
		# self.main_widget.addTab(self.inputter, 'REPL')
		self.fmuseditor = FmusEditorWrapper()
		self.main_widget.addTab(self.fmuseditor, 'Edit')
		self.main_widget.tabBar().hide()
		self.main_layout.addWidget(self.main_widget)

		self.inputter.setFocus()

		self.init_menu()
		self.init_tray()

		screen_geometry = QDesktopWidget().screenGeometry(-1)
		self.w, self.h = screen_geometry.width(), screen_geometry.height()
		self.resize_screen_ratio(ratio=1/5)  # ukuran form

		self.setWindowTitle('Overclock')
		QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
		self.show()


	def init_tray(self):
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(QIcon(QPixmap(ICON_FILEPATH)))
		self.setTrayMenu()
		self.toggle_tray()


	def setTrayMenu(self):
		self.start_icon = QApplication.style().standardIcon(QStyle.SP_MediaPlay)
		self.stop_icon = QApplication.style().standardIcon(QStyle.SP_MediaStop)
		exit_icon = QApplication.style().standardIcon(QStyle.SP_BrowserStop)
		show_action = QAction(get_icon(), "Menu Show", self)
		quit_action = QAction(exit_icon, "Menu Exit", self)
		# hide_action = QAction(get_icon(), "Menu Hide", self)
		show_action.triggered.connect(self.show)
		# hide_action.triggered.connect(self.hide)
		quit_action.triggered.connect(QApplication.instance().quit)
		self.tray_menu = QMenu()
		self.editor_menu = QMenu('Edit', self.tray_menu)
		self.editor_menu.setIcon(get_icon())
		self.editor_menu.addAction(get_icon(), 'Edit searcher.py (me)', lambda: os.system(
			f'vscode {SIDOARJODIR}/gui/system/searcher/searcher.py'))
		self.tray_menu.addMenu(self.editor_menu)
		self.tray_menu.addAction(get_icon(), 'About', about_qt)
		self.tray_menu.addAction(show_action)
		self.tray_menu.addAction(quit_action)
		self.tray_menu.setWindowFlags(self.tray_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
		self.tray_icon.setContextMenu(self.tray_menu)


	def trayMessage(self, judul, isi, lama=500):
		self.tray_icon.showMessage(judul, isi, QSystemTrayIcon.Information, lama)


	def toggle_tray(self):
		if self.isVisible():
			self.tray_icon.hide()
		else:
			self.tray_icon.show()			


	def setApplicationIcon(self, filepath):
		self.setWindowIcon(QIcon(filepath))


	def publisher(self, pesan):
		try:
			res = replify_check_language(pesan, os.getcwd())
			indah3(res, warna='yellow')
		except Exception as err:
			print_err(err)


	def query_searching(self):
		query = self.inputter.text()
		# if self.publisher:
		self.publisher(query)
		self.inputter.setText('')
		if query not in self.history:
			self.history.append(query)
		self.set_input_completer()


	def set_input_completer(self):
		model = self.completer.model()
		model.setStringList(self.history)


	def resize_screen_ratio(self, ratio=1/6, delta = 20):
		lebar, tinggi = int(self.w*ratio), int(self.h*ratio)
		self.resize(lebar, tinggi)
		posx = self.w - lebar
		posy = self.h - tinggi - delta
		self.move(posx, posy)
		self.casio.change_size(lebar, tinggi)


	def to_bottomright(self):
		lebar = self.width()
		posx = self.w - lebar
		delta = 60
		tinggi = self.height()
		posy = self.h - tinggi - delta
		self.move(posx, posy)


	def to_bottomleft(self):
		posx = 0
		delta = 60
		tinggi = self.height()
		posy = self.h - tinggi - delta
		self.move(posx, posy)


	def contextMenuEvent(self, event):
		self.context_menu.exec_(event.globalPos())


	def init_menu(self):
		self.context_menu = QMenu(self)
		# self.context_menu.setAttribute(Qt.WA_TranslucentBackground, True)
		self.context_menu.setWindowFlags(self.context_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
		# self.context_menu.setWindowFlags(self.context_menu.windowFlags() | Qt.FramelessWindowHint)
		self.context_menu.setStyleSheet(context_menu_stylesheet)
		about = self.context_menu.addAction(get_icon(), 'About', about_qt)
		self.context_menu.addSeparator()
		self.screen_menu = QMenu('Screen menu', self)
		self.screen_menu.setIcon(get_icon())
		self.context_menu.addMenu(self.screen_menu)
		# print('seiko 002')
		smaller = self.screen_menu.addAction(get_icon(), 'Smaller', lambda: self.resize_screen_ratio(1/8))
		smallest = self.screen_menu.addAction(get_icon(), 'Smallest', lambda: self.resize_screen_ratio(1/10))
		quarter = self.screen_menu.addAction(get_icon(), '1/4 screen', lambda: self.resize_screen_ratio(1/4))
		half = self.screen_menu.addAction(get_icon(), '1/2 screen', lambda: self.resize_screen_ratio(1/2))
		threequarter = self.screen_menu.addAction(get_icon(), '3/4 screen', lambda: self.resize_screen_ratio(3/4))
		self.screen_menu.addAction(get_icon(), 'Bottom left', lambda: self.to_bottomleft())
		self.screen_menu.addAction(get_icon(), 'Bottom right', lambda: self.to_bottomright())
		self.screen_menu.addSeparator()
		self.screen_menu.addAction(get_icon(), 'Reset', lambda: self.resize_screen_ratio(1/6))
		self.context_menu.addAction(get_icon(), 'Reset', lambda: self.resize_screen_ratio(1/6))
		self.context_menu.addSeparator()
		self.context_menu.addAction(get_icon(), '(0) Main', lambda: self.main_widget.setCurrentIndex(0))
		self.context_menu.addAction(get_icon(), '(1) Edit', lambda: self.main_widget.setCurrentIndex(1))
		self.context_menu.addSeparator()
		self.context_menu.addAction(get_icon(), 'Quit', lambda: qApp.quit())


	def exit_not_close(self):
		# QApplication.quit() # ini salah/gagal, jadi restart
		QApplication.instance().quit()


class WinEventFilter(QAbstractNativeEventFilter):

	def __init__(self, keybinder):
		self.keybinder = keybinder
		super().__init__()

	def nativeEventFilter(self, eventType, message):
		ret = self.keybinder.handler(eventType, message)
		return ret, 0


def main():
	app = QApplication([])
	set_theme(app)
	window = CornerWidget()
	# window.setStyleSheet(background_image_stylesheet)
	window.setStyleSheet("background-color: #ffffff;")


	# prepare mk
	mkwindow = MKHelpWidget()
	mkwindow.setStyleSheet(background_image_stylesheet)
	resize_screen_ratio_wrapper_simple(mkwindow,x=0.4,w=0.6,delta=50,centering=False)
	mkwindow.hide()


	keybinder.init()


	def exit_app():
		window.exit_not_close()

	def toggle_clock():
		if window.isVisible():
			window.hide()
			window.trayMessage('FMUSSERVER', 'App is running here in the tray.\nctrl+alt+shift+k to show.')
		else:
			window.show()
			window.inputter.setFocus()

	def toggle_filemanager():
		if mkwindow.isVisible():
			mkwindow.hide()
		else:
			mkwindow.show()

	def screenshot_clipboard():
		from schnell.app.ocrutils import clipboard_screenshot3
		clipboard_screenshot3()

	def run_ocr_local():
		from schnell.app.ocrutils import ocr_screenshot
		ocr_screenshot()

	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+A", callback_toggle)
	keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+E", exit_app)
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+F", unregister)
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+G", show_menu)
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+H", view_helper)
	keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+J", toggle_filemanager)
	keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+K", toggle_clock)
	keybinder.register_hotkey(window.winId(), "Shift+Ctrl+L", screenshot_clipboard) # capture -> clipboard
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+M", view_mmm)
	keybinder.register_hotkey(window.winId(), "Shift+Ctrl+O", run_ocr_local) # capture -> text (ocr)
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+U", run_u)
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+U", run_u2) # run fmuslang
	# keybinder.register_hotkey(window.winId(), "Shift+Ctrl+Alt+Y", run_y) # run replify

	win_event_filter = WinEventFilter(keybinder)
	event_dispatcher = QAbstractEventDispatcher.instance()
	event_dispatcher.installNativeEventFilter(win_event_filter)

	window.setApplicationIcon(joiner(SIDOARJODIR, 'usef.png'))
	window.show()
	# sys.exit(app.exec_())
	app.exec_()

	# keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+Y")
	# keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+U")
	keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+O")
	# keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+M")
	keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+L")
	keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+K")
	keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+J")
	# keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+H")
	# keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+G")
	keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+Alt+E")
	# kita pake:
	# cs-o utk ocr
	# cs-l utk image to clipboard
	# csa-k utk show/hide corner widget
	# csa-j utk show/hide mkwindow
	# csa-e utk exit


if __name__ == '__main__':
	main()
