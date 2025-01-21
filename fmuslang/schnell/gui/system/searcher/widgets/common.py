import functools, random, string, os, sys, subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([sidoarjodir, schnelldir])

from constants import sidoarjodir
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import basename, bongkar
from schnell.app.fileutils import (
	content_length, file_length, line_number_expression,
	get_daftar,
	get_definition_by_key_permissive_start,
	get_definition_double_entry_aware,
	file_write,
	file_content,
	get_extension,
)
from schnell.app.dirutils import (
	joiner,
	files_filter,
	get_cwd,
	tempdir,
	timestamp,
	walk_fullpath,
)
from schnell.app.utils import env_get


mkhelp_initial_path = joiner(sidoarjodir, 'mkhelp')
snippets_initial_path = joiner(sidoarjodir, 'data/snippets')
epmus_initial_path = joiner(sidoarjodir, 'database/geura')
kenza_us_dir = joiner(sidoarjodir, 'data/kenza-us')
kenza_us_files = walk_fullpath(kenza_us_dir, filtered_end_list=['.us', '.fm'])

def reload_kenza_us_files():
	"""
	jadi ada konsep gini
	filetreewidget: import kenza_us_files
	common: define kenza_us_files
	jk kita panggil reload_kenza_us_files() di sini...maka yg terupdate adlh kenza_us_files di common, tapi di filetreewidget belum terupdate
	"""
	# global kenza_us_files
	kenza_us_files = walk_fullpath(kenza_us_dir, filtered_end_list=['.us', '.fm'])
	return kenza_us_files

provider_languagesdir = joiner(sidoarjodir, 'providers/languages')
mkfiles = files_filter(provider_languagesdir, extension=['.mk'])
mkfiles_without_mk = [item.removesuffix('.mk') for item in mkfiles]
bahasa_filepaths = dict(zip(mkfiles_without_mk, [joiner(provider_languagesdir, item) for item in mkfiles]))

autocompletion_file = joiner(sidoarjodir, 'providers/models/autocompletion.mk')
autocompletions = {}
for entry in get_daftar(autocompletion_file):
	terima = get_definition_double_entry_aware(autocompletion_file, entry)
	if terima:
		autocompletions[entry] = [item for item in terima.splitlines() if item.strip()]

standard_dahsyat_file = joiner(sidoarjodir, 'providers/models/tables.mk')
standard_dahsyat_model = get_definition_double_entry_aware(standard_dahsyat_file, 'Todo')
standard_dahsyat_toc = get_daftar(standard_dahsyat_file)
sample_data_dahsyat_tables = dict(zip(standard_dahsyat_toc, [get_definition_by_key_permissive_start(standard_dahsyat_file, item) for item in standard_dahsyat_toc]))

context_menu_for_dirs = files_filter(joiner(sidoarjodir, 'providers/directories'), extension=['.mk'], abs_path=True)
context_menu_for_dirs_with_entries = {k:get_daftar(k) for k in context_menu_for_dirs}

context_menu_for_files = files_filter(joiner(sidoarjodir, 'providers/files'), extension=['.mk'], abs_path=True)
context_menu_for_files_with_entries = {k:get_daftar(k) for k in context_menu_for_files}

context_menu_for_dahsyat = files_filter(joiner(sidoarjodir, 'providers/dahsyaters'), extension=['.mk'], abs_path=True)
context_menu_for_dahsyat_with_entries = {k:get_daftar(k) for k in context_menu_for_dahsyat}

predefined_commands_file = joiner(sidoarjodir, 'providers/models/predefined_commands.mk')
predefined_commands_line = 'directory commands'
predefined_commands = [item for item in get_definition_by_key_permissive_start(predefined_commands_file, predefined_commands_line).splitlines() if item.strip()]

yarn_add_packages_dev_file = joiner(sidoarjodir, 'providers/models/combo_choices.mk')
yarn_add_packages_dev_line = 'yarn add --dev'
yarn_add_packages_dev = [item for item in get_definition_by_key_permissive_start(yarn_add_packages_dev_file, yarn_add_packages_dev_line).splitlines() if item.strip()]

yarn_add_packages_file = joiner(sidoarjodir, 'providers/models/combo_choices.mk')
yarn_add_packages_line = 'yarn add'
yarn_add_packages = [item for item in get_definition_by_key_permissive_start(yarn_add_packages_file, yarn_add_packages_line).splitlines() if item.strip()]

csvmodels_sourcefile = joiner(sidoarjodir, 'database/refcards/models.mk')
csvmodels_toc = get_daftar(csvmodels_sourcefile)
sample_data_csvlang = dict(zip(csvmodels_toc, [get_definition_by_key_permissive_start(csvmodels_sourcefile, item) for item in csvmodels_toc]))


context_menu_stylesheet = """
QMenu {
	/* Translucent effect */
	background-color: rgba(255, 255, 255, 230);
	border: none;
	border-radius: 4px;
}
QMenu::item {
	border-radius: 4px;
	/* This distance is cumbersome and needs to be fine-tuned based on factors such as menu length and icons */
	padding: 8px 48px 8px 36px; /* 36px is the distance from the text to the left*/
	background-color: transparent;
}
/* Mouseover and press effects */
QMenu::item:selected {
	border-radius: 0px;
	color: blue;
	background-color: rgba(32, 32, 32, 32);
	/* background-color: transparent; */
}
/*
QMenu::item:hovered {
	border-radius: 0px;
	background-color: transparent;
}
*/
/* disable effect */
QMenu::item:disabled {
	background-color: transparent;
}
/* icon distance to the left */
QMenu::icon {
	left: 15px;
}
/* split line effect */
QMenu::separator {
	height: 1px;
	background-color: rgb(232, 236, 243);
}
"""


main_button_style = """
BlueButton {
	color: yellow;
	background-color: royalblue;
	margin: 10px;
	padding: 10px;
	font-size: 18px;
	font-family: Verdana, Consolas;
	/* Limit min and max size */
	/* min-width: 96px; */
	/* max-width: 96px; */
	/* padding-left: 20px; */
	/* padding-right: 20px; */
	/* margin-right: 10px; */
	/* min-height: 96px; */
	max-height: 32px;
	border-radius: 12px; /* round */
	border-bottom: 2px solid #663399;
}
BlueButton:hover {
	background-color: #64b5f6;
	color: orangered;
	font-weight: bold;
	font-size: 24px;
}
BlueButton:pressed {
	background-color: #bbdefb;
}
"""


def get_icon():
	pixmap = QPixmap(16, 16)
	pixmap.fill(Qt.transparent)
	painter = QPainter()
	painter.begin(pixmap)
	painter.setFont(QFont('Webdings', 11))
	painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
	painter.drawText(0, 0, 16, 16, Qt.AlignCenter, random.choice(string.ascii_letters))
	painter.end()
	return QIcon(pixmap)


def about_qt():
	QApplication.instance().aboutQt()


def set_theme(app):
	app.setStyle("Fusion")
	palette = QPalette()
	palette.setColor(QPalette.Window, Qt.white)
    # palette.setColor(QPalette.WindowText, Qt.white)
	palette.setColor(QPalette.Base, Qt.green)
    # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # palette.setColor(QPalette.ToolTipBase, Qt.black)
    # palette.setColor(QPalette.ToolTipText, Qt.white)
    # palette.setColor(QPalette.Text, Qt.white)
    # palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # palette.setColor(QPalette.ButtonText, Qt.white)
    # palette.setColor(QPalette.BrightText, Qt.red)
    # palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # palette.setColor(QPalette.HighlightedText, Qt.black)
	app.setPalette(palette)


def screensize():
	screen_geometry = QDesktopWidget().screenGeometry(-1)
	w = screen_geometry.width()
	h = screen_geometry.height()
	return w,h


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, posy_ratio=1/2, w_ratio=1/6, h_ratio=0, delta=50, centering=True):
	"""
	screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
	screenw, screenh = screen_geometry.width(), screen_geometry.height()
	resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
	resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

	object hrs punya method resize dan move.
	"""
	if h_ratio <= 0:
		h_ratio = w_ratio
	if posy_ratio <= 0:
		posy_ratio = posx_ratio
	lebar, tinggi = int(screenw*w_ratio), int(screenh*h_ratio)
	object.resize(lebar, tinggi)
	if centering:
		posx = int((screenw-lebar)*posx_ratio)
	else:
		posx = int(screenw*posx_ratio)
	posy = int((screenh-tinggi)*posy_ratio) - delta
	object.move(posx, posy)


def resize_screen_ratio_wrapper(object, posx_ratio=1/2, posy_ratio=1/2, w_ratio=1/6, h_ratio=0, delta=50, centering=True):
	screen_geometry = QDesktopWidget().screenGeometry(-1)
	screenw, screenh = screen_geometry.width(), screen_geometry.height()
	resize_screen_ratio(object, screenw, screenh, posx_ratio, posy_ratio, w_ratio, h_ratio, delta, centering=centering)


def resize_screen_ratio_wrapper_simple(obj, x=1/2, y=1/2, w=3/4, h=0.9, delta=60, centering=True):
	# print(f"""x={x}, y={y}, w={w}, h={h}, delta={delta}""")
	resize_screen_ratio_wrapper(obj, posx_ratio=x,posy_ratio=y,w_ratio=w,h_ratio=h,delta=delta, centering=centering)


class BlueButton(QPushButton):

	def __init__(self, menu=None, text=None, parent=None):
		super().__init__(text, parent)
		if menu:
			self.setMenu(menu)
		# self.setObjectName('MainButton')
		# self.setText(text)
		self.setStyleSheet(main_button_style)


class ClockWidget(QLabel):
	# vintage clock
	def __init__(self, parent=None):
		super(ClockWidget, self).__init__(parent)
		self.timer = QTimer()  # timer
		self.timer.timeout.connect(self.update)
		self.timer.start(1000)  # Update every 1s
		self.setMinimumSize(QSize(100, 100))

	def textRectF(self,radius,pointsize,angle):

		recf = QRectF()
		recf.setX(radius*math.cos(angle*math.pi/180.0)-pointsize*2)
		recf.setY(radius*math.sin(angle*math.pi/180.0)-pointsize/2.0)
		recf.setWidth(pointsize*4)#Width Height
		recf.setHeight(pointsize)
		return recf

	def paintEvent(self, event):
		panjang_jam = -50
		panjang_menit = -65
		panjang_detik = -80
		hour_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_jam)]
		minute_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_menit)]
		second_points = [QPoint(5,8),QPoint(-5,8),QPoint(0,panjang_detik)]

		hour_color = QColor(0,0,250,200)
		minute_color = QColor(0,250,0,175)
		second_color = QColor(250,0,0,150) # QColor(0,160,230,150)

		min_len = min(self.width(),self.height())
		time = QTime.currentTime() # get current time
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.translate(self.width()/2,self.height()/2) # Pan to center of window
		painter.scale(min_len/200.0,min_len/200.0) # scaling

		#---------- draw the hour hand ------------
		painter.setPen(Qt.NoPen)
		painter.setBrush(hour_color)#color
		painter.save()
		# according to 1 hour = 30degree, rotate counterclockwise in the direction of water quality
		painter.rotate(30.0*((time.hour()+time.minute()/60.0)))
		painter.drawConvexPolygon(QPolygon(hour_points))
		painter.restore() # save Exit to reset the brush

		painter.setPen(hour_color)
		#draw hour line(360/12 = 30 degrees)
		for i in range(12):
			painter.drawLine(88,0,96,0)#draw horizontal lines
			painter.rotate(30.0)# Rotate at the original rotation angle;

		radius = 100 # radius
		font = painter.font()
		font.setBold(True)
		painter.setFont(font)
		pointSize = font.pointSize() # font size
		# print(pointSize)

		#draw hour text
		for i in range(12):
			nhour = i + 3 # from level 3 point to draw
			if(nhour>12):
				nhour -= 12
			painter.drawText(self.textRectF(radius*0.8,pointSize,i*30),Qt.AlignCenter,str(nhour))

		#draw the minute hand;
		painter.setPen(Qt.NoPen)
		painter.setBrush(minute_color)
		painter.save()

		# 1 minute is 6degree
		painter.rotate(6.0*(time.minute()+time.second()/60.0))
		painter.drawConvexPolygon(QPolygon(minute_points))
		painter.restore()

		# draw minute line
		painter.setPen(minute_color)
		for i in range(60):
			if(i%5 !=0):
				painter.drawLine(92,0,96,0)
			painter.rotate(6.0)

		# Draw the second hand
		painter.setPen(Qt.NoPen)
		painter.setBrush(second_color)
		painter.save()
		# draw second line
		painter.rotate(6.0*time.second())
		painter.drawConvexPolygon(QPolygon(second_points))
		painter.restore()

		painter.setPen(second_color)
		for i in range(360):
			if(i%5!=0 or i%30!=0): # draw
				painter.drawLine(94,0,96,0)
			painter.rotate(1.0) # rotate


class WidgetAnak1(QWidget):
	def __init__(self, item, *args, **kwargs):
		super(WidgetAnak1, self).__init__(*args, **kwargs)
		self.item = item # jk gak handle resize, gak keliatan

		listfold0_pagelayout_0 = QVBoxLayout(self)

		clock0 = ClockWidget(self)
		listfold0_pagelayout_0.addWidget(clock0)
 
	def resizeEvent(self, event):
		super(WidgetAnak1, self).resizeEvent(event)
		self.item.setSizeHint(QSize(self.minimumWidth(), 300))


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		# Form.resize(335, 50)
		# Form.resize(150, 25)

		self.lcdNumber = QLCDNumber(Form)
		# self.lcdNumber.setStyleSheet('border: 1px solid blue; color: yellow;')
		self.lcdNumber.setStyleSheet('color: blue;')
		# self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 250, 50))
		self.lcdNumber.setGeometry(QRect(0, 0, 100, 40))
		# self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.lcdNumber.setContextMenuPolicy(Qt.DefaultContextMenu)
		self.lcdNumber.setFrameShape(QFrame.NoFrame)
		self.lcdNumber.setSmallDecimalPoint(False)
		self.lcdNumber.setDigitCount(8)
		self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
		self.lcdNumber.setProperty("value", 2021.0)
		self.lcdNumber.setObjectName("lcdNumber")

		self.retranslateUi(Form)
		QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))


class DigitalClock(QWidget, Ui_Form):
	# digital watch
	def __init__(self, parent = None):
		super(DigitalClock,self).__init__(parent)
		self.setupUi(self)
		# self.setStyleSheet('background-color')
		self.setWindowFlags(Qt.FramelessWindowHint) # Rimless
		self.setAcceptDrops(True)
		self.lcdNumber.display('00:00:00')
		time_slot = QTimer(self)
		time_slot.timeout.connect(self.clock_ticking)
		time_slot.start(1000)

	def clock_ticking(self):
		time_format = QTime.currentTime()
		time_format = time_format.toString("hh:mm:ss")
		self.lcdNumber.display(time_format)
		QApplication.processEvents()


class WidgetAnak2(QWidget):
	def __init__(self, item, *args, **kwargs):
		super(WidgetAnak2, self).__init__(*args, **kwargs)
		self.item = item # jk gak handle resize, gak keliatan

		listfold0_pagelayout_1 = QVBoxLayout(self)

		casio0 = DigitalClock(self)
		casio0.setMinimumHeight(100)
		listfold0_pagelayout_1.addWidget(casio0)

	def resizeEvent(self, event):
		super(WidgetAnak2, self).resizeEvent(event)
		self.item.setSizeHint(QSize(self.minimumWidth(), 300))


class FoldButton(QPushButton):
	def __init__(self, item, *args, **kwargs):
		super(FoldButton, self).__init__(*args, **kwargs)
		self.item = item
		self.setCheckable(True)
	def resizeEvent(self, event):
		super(FoldButton, self).resizeEvent(event)
		self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class FoldedListWidget(QListWidget):
	def __init__(self, widgets=[]):
		super(FoldedListWidget, self).__init__()
		self.setStyleSheet('#testBtn { min-height:40px; background:green; } ')


		i = 0
		# tiap list item punya 2 komponen: button dan content
		# item = button
		item = QListWidgetItem(self)		
		fold_button = FoldButton(item, 'lihat analog', self, objectName='testBtn') # set parent dari button = item			
		self.setItemWidget(item, fold_button) # item, button = parent, child
		# item2 = content
		item2 = QListWidgetItem(self)
		# anak = WidgetAnak1(item2, self) # set parent dari widgetanak = item2
		anak = widgets[i]
		self.setItemWidget(item2, anak) # item, anak = parent, child
		# buka yg pertama saja...
		if i != 0:
			item2.setHidden(True)
			fold_button.setChecked(True)
		fold_button.toggled.connect(item2.setHidden) # last, sambungkan button di item ke toggle item2

		i = 1
		# tiap list item punya 2 komponen: button dan content
		# item = button
		item = QListWidgetItem(self)		
		fold_button = FoldButton(item, 'lihat digital', self, objectName='testBtn') # set parent dari button = item			
		self.setItemWidget(item, fold_button) # item, button = parent, child
		# item2 = content
		item2 = QListWidgetItem(self)
		anak = widgets[i]
		self.setItemWidget(item2, anak) # item, anak = parent, child
		# buka yg pertama saja...
		if i != 0:
			item2.setHidden(True)
			fold_button.setChecked(True)
		fold_button.toggled.connect(item2.setHidden) # last, sambungkan button di item ke toggle item2


class MkfileButton(QWidget):

	# <<MkfileButton>>.new_button_data_signal.connect(<<MKHelpWidget>>.guicode_editor_insert_data)
	new_button_data_signal = pyqtSignal(str)

	def __init__(self, filepath_mk):
		super().__init__()
		filename_mk = basename(filepath_mk)
		self.button = QPushButton(filename_mk.removesuffix('.mk'))
		self.button.setProperty('object_wrapper', self)
		self.button.setProperty('mkfilebutton', self)
		# partial_method = functools.partial(self.button.setProperty, 'object_wrapper', self)
		# partial_method()
		# new_button_data_signal = pyqtSignal(str)
		self.filepath_mk = bongkar(filepath_mk)
		self.entries = get_daftar(self.filepath_mk)
		self.mkfile_to_button()

	def create_button_menu(self, menu_list):
		menu = QMenu('Button Menu')
		for item in sorted(menu_list):
			filepath_barisentry = self.filepath_mk + ':' + item
			menu.addAction(get_icon(), item, functools.partial(self.signal_new_barisentry, filepath_barisentry))
		return menu

	def get_button(self):
		# self.button.setProperty('object_wrapper', self)
		# self.button.setProperty('mkfilebutton', self)
		return self.button

	def connect_to_editor(self, handler):
		self.new_button_data_signal.connect(handler)

	def mkfile_to_button(self):
		if len(self.entries)==1:
			# satu baris_entry, gak pake menu, langsung klik button
			satu = self.entries[0]
			filepath_barisentry = self.filepath_mk + ':' + satu
			self.button.clicked.connect(functools.partial(self.signal_new_barisentry, filepath_barisentry))
		else:
			menu = self.create_button_menu(self.entries)
			self.button.setMenu(menu)
		# return self.button

	def signal_new_barisentry(self, filepath_barisentry):
		self.new_button_data_signal.emit(filepath_barisentry)
		# print('extra button pilih:', filepath_barisentry)


def create_menu_editors(parent):
	menu_cmds = QMenu(parent)

	for label, exepath in programming_data['j']['editors'].items():
		# if programming_data['debug']:
		# 	print(f'create_menu_editors, {label} => {exepath}.')
		menu_cmds.addAction(
			# QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
			get_icon(),
			label,
			functools.partial(subprocess.Popen, exepath)
		)
	return menu_cmds


def create_menu_cmds(parent):
	menu_cmds = QMenu(parent)

	for label, exepath in programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['filetreewidget'].items():
		menu_cmds.addAction(
			QApplication.style().standardIcon(QStyle.SP_FileIcon),
			label,
			functools.partial(subprocess.Popen, f"{programming_data['j']['programs']['vscodecmd']} {exepath}")
		)
	for label, exepath in programming_data['j']['browsers']['programs'].items():
		menu_cmds.addAction(
			QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
			label,
			functools.partial(subprocess.Popen, exepath['exe'])
		)
	return menu_cmds
