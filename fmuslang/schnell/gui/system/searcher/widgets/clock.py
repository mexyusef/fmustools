import datetime, math, random, string, sys, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# rootdir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([rootdir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
sys.path.append(sidoarjodir)

if __name__ == '__main__':
	from startup import initialize_programming_data
	initialize_programming_data()

from schnell.app.audioutils import denger, speak, angka
from schnell.app.datetimeutils import jam, timestamp_for_file, menit, seconds_till_next_hour, seconds_till_next_minutes
from schnell.app.utils import GOOGLESEARCH, buka
from schnell.creator.context import context as global_context
from schnell.gui.system.searcher.widgets.menu import sidoarjo_menu, runner_menu
# from schnell.gui.system.searcher.widgets.so import StackOverflowWidget as SoWidget
from schnell.gui.system.searcher.widgets.colorwidget import ColorWidget
from schnell.gui.system.searcher.widgets.fm import FileManager
from schnell.gui.system.searcher.widgets.common import get_icon, about_qt, set_theme, context_menu_stylesheet
from schnell.gui.system.searcher.widgets.replhelp import search_edit



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

	def change_size(self, w, h):
		lebar = w // 3
		tinggi = h // 4
		# print(f'lebar {lebar}, tinggi {tinggi}')
		self.lcdNumber.setGeometry(QRect(0, 0, lebar, tinggi))

	def __init__(self, parent):
		super(DigitalClock,self).__init__(parent)

		self.lcdNumber = QLCDNumber(self)
		# self.lcdNumber.setStyleSheet('border: 1px solid blue; color: yellow;')
		self.lcdNumber.setStyleSheet('color: chartreuse; background-color: darkblue;')
		# lebar = parent.width() // 5
		# tinggi = parent.height() // 15
		# # print(f'lebar {lebar}, tinggi {tinggi}')
		# self.lcdNumber.setGeometry(QRect(0, 0, lebar, tinggi))

		self.change_size(parent.width(), parent.height())
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
			print(f"[gui.system.searcher.widgets.clock][play_sound] {katakata}")
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


class GoogleSearchWidget(QLineEdit):
	def __init__(self):
		super().__init__()
		self.setStyleSheet("height: 60px; font-size: 20px; font-family: Consolas; background-color: oldlace;")
		self.returnPressed.connect(self.cari_google)
		self.history = []
		self.completer = QCompleter(self.history)
		self.completer.setCompletionMode(QCompleter.PopupCompletion)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.setCompleter(self.completer)


	def cari_google(self):
		query = self.text()
		print(f'cari [{query}] di google')
		if query not in self.history:
			self.history.append(query)
		self.set_input_completer()
		__TEXTPLACEHOLDER__ = query.replace(' ', '+')
		alamat = GOOGLESEARCH.replace('__TEXTPLACEHOLDER__', __TEXTPLACEHOLDER__)
		buka(alamat)

	def set_input_completer(self):
		model = self.completer.model()
		model.setStringList(self.history)


class ReplInput(QLineEdit):
	def __init__(self, query_searching, history=[], minwidth=0, cssminwidth=100):
		super().__init__()
		if minwidth > 0:
			self.setMaximumWidth(minwidth)
		# self.setMinimumWidth(150)
		self.returnPressed.connect(query_searching)
		# self.installEventFilter(self)
		self.setStyleSheet(f"height: 40px; min-width: {cssminwidth}px; font-size: 16px; font-family: Consolas; background-color: oldlace;")
		self.history = history
		self.history_pointer = 0
		# self.history = []
		# self.completer = QCompleter(self.history)
		# self.completer.setCompletionMode(QCompleter.PopupCompletion)
		# self.completer.setCaseSensitivity(Qt.CaseInsensitive)

	# def setCompleter(self, completer):
	#     self.setCompleter(completer)

	# def eventFilter(self, obj, event):
	#     if event.type() == QEvent.KeyPress:
	#         # if event.key() == Qt.Key_Return and self.inputter.hasFocus():
	#         #     print('Enter pressed by event filter...')
	#         if event.key() == Qt.Key_Up:
	#             print('up')
	#         elif event.key() == Qt.Key_Down:
	#             print('down')
	#     return super().eventFilter(obj, event)

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


class CornerWidget(QWidget):

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

	def resize_screen_ratio(self, ratio=1/6, delta = 20):
		lebar, tinggi = int(self.w*ratio), int(self.h*ratio)
		self.resize(lebar, tinggi)
		posx = self.w - lebar
		posy = self.h - tinggi - delta
		self.move(posx, posy)
		self.casio.change_size(lebar, tinggi)

	def setCmderToggler(self, toggler):
		self.menu_runner.addAction(get_icon(), 'Cmder', toggler)

	def setRedisPublisher(self, publisher):
		self.publisher = publisher
		self.filemanager.setRedisPublisher(self.publisher)

	def setGptChat(self, gptchat):
		self.filemanager.setGptChat(gptchat)

	def init_menu(self):
		# print('seiko 001')
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
		# print('seiko 003')
		# self.tab_menu = QMenu('Tab', self)
		# self.tab_menu.setIcon(get_icon())
		# self.context_menu.addMenu(self.tab_menu)
		# self.tab_menu.addAction(get_icon(), '1', lambda: self.main_widget.setCurrentIndex(0))
		# self.tab_menu.addAction(get_icon(), '2', lambda: self.main_widget.setCurrentIndex(1))
		self.context_menu.addAction(get_icon(), '(0) Main', lambda: self.main_widget.setCurrentIndex(0))
		# print('seiko 004')
		self.context_menu.addAction(get_icon(), '(1) Google', lambda: self.main_widget.setCurrentIndex(1))
		# print('seiko 005')
		self.context_menu.addAction(get_icon(), '(2) REPL', lambda: self.main_widget.setCurrentIndex(2))
		# print('seiko 006')
		self.context_menu.addSeparator()
		# print('seiko 007')
		# misc menu
		# ini koneksi internet di
		# C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\so.py, L:269, self.data = get_data_stackoverflow()
		# sowidget = SoWidget() # instantiate gak bisa di dalam addAction
		# print('seiko 008')
		# self.context_menu.addAction(get_icon(), 'SO', lambda: sowidget.show())
		# print('seiko 009')
		colorwidget = ColorWidget()
		self.context_menu.addAction(get_icon(), 'Colors', lambda: colorwidget.show())
		# print('seiko 010')
		self.filemanager = FileManager(self.publisher)
		self.context_menu.addAction(get_icon(), 'FM', lambda: self.filemanager.showMaximized())
		# print('seiko 011')
		# replang = ReplangWidget()
		# self.context_menu.addAction(get_icon(), 'Replang', lambda: replang.show())
		# framelang = FramelangWidget()
		# self.context_menu.addAction(get_icon(), 'Framelang', lambda: framelang.show())
		# csvlang = CsvlangWidget()
		# self.context_menu.addAction(get_icon(), 'Csvlang', lambda: csvlang.show())
		self.context_menu.addSeparator()
		self.context_menu.addMenu(self.sidoarjo_menu)
		self.context_menu.addSeparator()
		self.context_menu.addMenu(self.menu_runner)
		self.context_menu.addSeparator()
		# menu = QMenu('Activate tab', self.context_menu)
		# menu.addAction(get_icon(), 'Waktu', lambda: self.main_control.setCurrentIndex(0))
		# self.context_menu.addMenu(menu)
		# print('seiko 012')
		self.context_menu.addSeparator()
		self.context_menu.addAction(get_icon(), 'Quit', lambda: qApp.quit())
		# print('seiko 013')

	def contextMenuEvent(self, event):
		self.context_menu.exec_(event.globalPos())

	# def eventFilter(self, obj, event):
	#     if event.type() == QEvent.KeyPress and obj is self.inputter:
	#         # if event.key() == Qt.Key_Return and self.inputter.hasFocus():
	#         #     print('Enter pressed by event filter...')
	#         if event.key() == Qt.Key_Up:
	#             print('UP')
	#         elif event.key() == Qt.Key_Down:
	#             print('DOWN')
	#     return super().eventFilter(obj, event)

	def query_searching(self):
		query = self.inputter.text()
		if self.publisher:
			self.publisher(query)
			self.inputter.setText('')
			if query not in self.history:
				self.history.append(query)
			self.set_input_completer()


	def set_input_completer(self):
		model = self.completer.model()
		model.setStringList(self.history)


	def __init__(self, parent = None):
		super(CornerWidget, self).__init__(parent)
		# print('rolex 001')
		# self.parent = parent
		self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
		# self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
		# self.setAttribute(Qt.WA_TranslucentBackground, True)
		# print('rolex 002')
		self.setWindowOpacity(0.8)
		self.main_layout = QHBoxLayout(self)
		# print('rolex 003')
		self.rolex = AnalogClock(self)
		# rolexEffect = AnimationShadowEffect(Qt.green, self.rolex)
		# self.rolex.setGraphicsEffect(rolexEffect)
		# rolexEffect.start()
		# print('rolex 004')
		self.right_pane_layout = QVBoxLayout()
		self.casio = DigitalClock(self)
		casioEffect = AnimationShadowEffect(Qt.blue, self.casio)
		self.casio.setGraphicsEffect(casioEffect)
		casioEffect.start()
		# print('rolex 005')
		self.sidoarjo_menu = sidoarjo_menu(self, get_icon)
		self.sidoarjo_menu.setStyleSheet(context_menu_stylesheet)
		# print('rolex 006')
		main_button_label = datetime.datetime.today().strftime('%a %d %b %Y')
		self.main_button = QPushButton(main_button_label, self)
		self.main_button_menu = QMenu(self)
		# print('rolex 007')
		def search_edit_wrapper(callback=None):
			# from .replhelp import search_edit
			name, done = QInputDialog.getText(None, 'Masukkan nama file', 'Masukkan nama file utk dicari dan diedit:')
			name = name.strip()
			if done and name:
				if not callback:
					search_edit(name)
				else:
					callback(name)        
		self.search_edit_file_menu = QMenu('Search+edit file')
		mywidget = QLineEdit(self.search_edit_file_menu)
		mywidget.setStyleSheet('background-color: oldlace; height: 32px; font-family: Verdana; font-size: 16pt;')
		def search_edit_wrapper_by_enter():
			filename = mywidget.text().strip()
			if filename:
				search_edit(filename)
		mywidget.returnPressed.connect(search_edit_wrapper_by_enter)
		myaction = QWidgetAction(self.search_edit_file_menu)
		myaction.setDefaultWidget(mywidget)
		# print('rolex 008')
		self.search_edit_file_menu.addAction(myaction)
		self.main_button_menu.addAction(get_icon(), 'Search+edit', search_edit_wrapper)
		self.main_button_menu.addMenu(self.search_edit_file_menu)
		# print('rolex 009')
		def search_bongkar_redis():
			from schnell.app.redisutils import search_bongkar
			from rich.pretty import pprint
			name, done = QInputDialog.getText(None, 'Masukkan key redis', 'Masukkan key redis utk dicari dan diprint:')
			name = name.strip()
			if done and name:
				res = search_bongkar(f'ULIBPY_ROOTDIR*{name}*')
				pprint(res)
		self.main_button_menu.addAction(get_icon(), 'Search key redis with ULIBPY_ROOTDIR', search_bongkar_redis)
		def search_redis_asis():
			from schnell.app.redisutils import search_keys_cached
			from rich.pretty import pprint
			name, done = QInputDialog.getText(None, 'Masukkan key redis', 'Masukkan key redis utk dicari dan diprint:')
			name = name.strip()
			if done and name:
				res = search_keys_cached(f'*{name}*')
				pprint(res)
		self.main_button_menu.addAction(get_icon(), 'Search key redis asis', search_redis_asis)
		# self.main_button.setMenu(self.sidoarjo_menu)
		self.main_button.setMenu(self.main_button_menu)
		self.main_button.setObjectName('MainButton')
		self.main_button.setStyleSheet(main_button_style)
		# print('rolex 010')
		self.right_pane_layout.addWidget(self.casio)
		self.publisher = None
		# self.inputter = QLineEdit()
		# # self.inputter.setMaximumWidth(300)
		# self.inputter.setMaximumWidth(150)
		# # self.inputter.setMinimumWidth(150)
		# self.inputter.returnPressed.connect(self.query_searching)
		# # self.inputter.installEventFilter(self)
		# self.inputter.setStyleSheet("height: 40px; min-width: 100px; font-size: 16px; font-family: Consolas; background-color: oldlace;")
		self.history = []
		self.completer = QCompleter(self.history)
		self.completer.setCompletionMode(QCompleter.PopupCompletion)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		# self.inputter = ReplInput(self.query_searching, 150, 100)
		self.inputter = ReplInput(self.query_searching, self.history, 0, 100)
		self.inputter.setCompleter(self.completer)
		self.right_pane_layout.addWidget(self.inputter)
		self.right_pane_layout.addWidget(self.main_button)
		# print('rolex 011')
		# kita ubah jadi tab widget...old struktur masuk previous_main_widget
		# self.main_layout.addWidget(self.rolex)
		# self.main_layout.addLayout(self.right_pane_layout)
		self.previous_main_widget = QWidget()
		self.previous_main_layout = QHBoxLayout(self.previous_main_widget)
		self.previous_main_layout.addWidget(self.rolex, stretch=5)
		self.previous_main_layout.addLayout(self.right_pane_layout, stretch=5)
		# print('rolex 012')
		self.google = GoogleSearchWidget()
		self.main_widget = QTabWidget(self)
		self.main_widget.addTab(self.previous_main_widget, 'Clock')
		self.main_widget.addTab(self.google, 'Googler')
		self.main_widget.addTab(self.inputter, 'REPL')
		# tab 2 = google search
		# tab 3 = new repl lang dari redis langsung
		self.main_widget.tabBar().hide()
		self.main_layout.addWidget(self.main_widget)
		# print('rolex 013')
		# self.set_input_completer()
		self.inputter.setFocus()
		self.menu_runner = runner_menu(self, get_icon)
		# print('rolex 014')
		self.init_menu()
		# print('rolex 015')
		screen_geometry = QDesktopWidget().screenGeometry(-1)
		self.w,self.h = screen_geometry.width(), screen_geometry.height()
		self.resize_screen_ratio()
		# print('rolex 016')
		self.setWindowTitle('Overclock')
		QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
		self.show()
		# print('rolex 017')

# background_image_stylesheet = '''
# MainWindow {
#     border-image: url("bg.jpg");
#     background-repeat: no-repeat; 
#     background-position: center;
# }
# '''


def main():
	app = QApplication([])
	set_theme(app)
	w = CornerWidget()
	# w.setStyleSheet(background_image_stylesheet)
	w.setStyleSheet("background-color: #ffffff;")
	w.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
