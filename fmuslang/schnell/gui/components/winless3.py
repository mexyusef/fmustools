import sys
from PyQt5.QtCore import (
	Qt,
	pyqtProperty,
	pyqtSignal,
	pyqtSlot,

	QCoreApplication,
	QDir,
	QEvent,
	QFileInfo,
	QMetaObject,
	QMimeData,
	QModelIndex,
	QObject,
	QPoint,
	QPointF,
	QProcess,
	QPropertyAnimation,
	QRect,
	QRectF,
	QRegExp,
	QSize,
	QSizeF,
	QSortFilterProxyModel,
	QStringListModel,
	QTextCodec,
	QTime,
	QTimer,
	QUrl,
)
from PyQt5.QtGui import (
	QBrush,
	QColor,
	QCursor,
	QDrag,
	QEnterEvent,
	QFont,
	QFontDatabase,
	QFontInfo,
	QFontMetrics,	
	QFontMetricsF,
	QGradient,
	QIcon,
	QImage,
	QKeySequence,
	QLinearGradient,
	QMouseEvent,
	QPalette,
	QPainter,
	QPaintEvent,
	QPainterPath,
	QPen,
	QPixmap,
	QPolygon,
	QPolygonF,
	QRegExpValidator,
	QStandardItem,
	QStandardItemModel,
	QWindow,
)
from PyQt5.QtWidgets import (
	qApp,
	
	QAbstractItemView,
	QAbstractSlider,
	QAction,
	QApplication,
	QButtonGroup,    
	QCalendarWidget,
	QCheckBox,
	QComboBox,
	QCompleter,
	QDateTimeEdit,
	QDesktopWidget,
	QDial,
	QDialog,
	QFileDialog,
	QFileIconProvider,
	QFileSystemModel,
	QFormLayout,
	QFrame,
	QGraphicsDropShadowEffect,
	QGraphicsPixmapItem,
	QGraphicsScene,
	QGraphicsView,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLCDNumber,
	QLineEdit,
	QListView,
	QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMdiArea,	
	QMenu,
	QMessageBox,
	QPlainTextEdit,
	QProgressBar,
	QProxyStyle,
	QPushButton,
	QRadioButton,
	QRubberBand,
	QScrollArea,
	QScrollBar,
	QShortcut,
	QSizePolicy,
	QSlider,
	QSpacerItem,
	QSpinBox,
	QSplitter,
	QSplitterHandle,
	QStatusBar,
	QStyle,
	QStyleFactory,
	QSystemTrayIcon,
	QTabWidget,
	QTableView,
	QTableWidget,
	QTableWidgetItem,
	QTextBrowser,
	QTextEdit,
	QToolBar,
	QToolTip,
	QTreeView,
	QTreeWidget,
	QVBoxLayout,
	QWidget,
)


if __name__ == '__main__' or __name__ == 'winless3': # jk sama dg nama file = standalone
    from wembed import WindowEmbedder
else:
    from .wembed import WindowEmbedder


tulisan_html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<meta name="qrichtext" content="1" />

<style type="text/css">
p, li { white-space: pre-wrap; }
</style>

</head>

<body style="font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;">

<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
ini adalah daleman isi
</p>

<mg src="https://www.irishexaminer.com/cms_media/module_img/2150/1075112_1_articlelarge_bn-939518_ab66e273816a4b73b9eaa2d5e486d28a.jpg"/>
</body>
</html>
"""
class Ui_FormFrameless(object):

	def setupUi(self, FormFrameless):
		FormFrameless.setObjectName("FormFrameless")
		FormFrameless.resize(400, 300)		

		self.verticalLayout = QVBoxLayout(FormFrameless)
		self.verticalLayout.setContentsMargins(3, 3, 3, 3)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.widgetTitleBar = QWidget(FormFrameless)

		font = QFont()
		font.setFamily("Symbola")
		self.widgetTitleBar.setFont(font)
		self.widgetTitleBar.setObjectName("widgetTitleBar")

		self.horizontalLayout = QHBoxLayout(self.widgetTitleBar)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		spacerItem = QSpacerItem(253, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)

		self.buttonMinimum = QPushButton(self.widgetTitleBar)
		self.buttonMinimum.setMinimumSize(QSize(36, 36))
		self.buttonMinimum.setMaximumSize(QSize(36, 36))
		font = QFont()
		font.setFamily("webdings")
		self.buttonMinimum.setFont(font)
		self.buttonMinimum.setObjectName("buttonMinimum")
		self.horizontalLayout.addWidget(self.buttonMinimum)
		self.buttonMinimum.setToolTip("Minimum")
		self.buttonMinimum.setText("0")

		self.buttonMaximum = QPushButton(self.widgetTitleBar)
		self.buttonMaximum.setMinimumSize(QSize(36, 36))
		self.buttonMaximum.setMaximumSize(QSize(36, 36))
		font = QFont()
		font.setFamily("webdings")
		self.buttonMaximum.setFont(font)
		self.buttonMaximum.setObjectName("buttonMaximum")
		self.horizontalLayout.addWidget(self.buttonMaximum)
		self.buttonMaximum.setToolTip("Maximum")
		self.buttonMaximum.setText("1")


		self.buttonNormal = QPushButton(self.widgetTitleBar)
		self.buttonNormal.setMinimumSize(QSize(36, 36))
		self.buttonNormal.setMaximumSize(QSize(36, 36))
		font = QFont()
		font.setFamily("webdings")
		self.buttonNormal.setFont(font)
		self.buttonNormal.setObjectName("buttonNormal")	
		self.horizontalLayout.addWidget(self.buttonNormal)
		self.buttonNormal.setToolTip("Normal")
		self.buttonNormal.setText("2")

		self.buttonClose = QPushButton(self.widgetTitleBar)
		self.buttonClose.setMinimumSize(QSize(36, 36))
		self.buttonClose.setMaximumSize(QSize(36, 36))
		font = QFont()
		font.setFamily("webdings")
		self.buttonClose.setFont(font)
		self.buttonClose.setObjectName("buttonClose")
		self.horizontalLayout.addWidget(self.buttonClose)
		self.buttonClose.setToolTip("Close")
		self.buttonClose.setText("r")

		self.verticalLayout.addWidget(self.widgetTitleBar)

		# self.verticalLayout.addWidget(self.textEdit)
		self.verticalLayout.addWidget(FormFrameless.main_content)

		self.verticalLayout.setStretch(1, 1)

		# ternyata ini harus terakhir ! klo gak self.button* dll jadi hilang (gak dikenal)
		FormFrameless.setWindowTitle("Form")
		QMetaObject.connectSlotsByName(FormFrameless)

	# def retranslateUi(self, FormFrameless):
	# 	_translate = QCoreApplication.translate
	# 	FormFrameless.setWindowTitle(_translate("FormFrameless", "Form"))

class MainWindow(QWidget):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		layout = QVBoxLayout(self, spacing=0)
		layout.setContentsMargins(0, 0, 0, 0)
		# layout.addWidget(QPushButton('button', self))
		# layout.addWidget(QTextEdit(self))
		self.tab = QTabWidget()
		self.tab.setTabPosition(QTabWidget.South)

		self.widget_cmd = QWidget()
		self.widget_wsl = QWidget()
		self.widget_listener = QWidget()

		# jd gak bener munculkan embedder...
		# self.widget_cmd = WindowEmbedder(perintah=['pwd', 'sido', 'gs'])
		# self.widget_wsl = WindowEmbedder(perintah=['wsl', 'pwd', 'sido', 'gs'])
		# self.widget_listener = WindowEmbedder(perintah=['wsl', 'pwd', 'sido', 'W'])

		self.tab.addTab(self.widget_cmd, '1')
		self.tab.addTab(self.widget_wsl, '2')
		self.tab.addTab(self.widget_listener, '3')
		
		layout.addWidget(self.tab)

class FramelessWindow(QWidget, Ui_FormFrameless):

	def __init__(self, *args, **kwargs):
		super(FramelessWindow, self).__init__(*args, **kwargs)

		# sebelum setupUi hrs sediakan main_content
		# self.main_content = QTextEdit(self)
		# self.main_content.setFrameShape(QFrame.NoFrame)
		# self.main_content.setObjectName("textEdit")
		# self.main_content.setHtml(tulisan_html)
		self.main_content = MainWindow(self)

		self.setupUi(self)
		# 无边框
		self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		self.setMouseTracking(True)
		# 隐藏还原按钮
		self.buttonNormal.setVisible(False)
		# 标题栏按钮信号
		self.buttonMinimum.clicked.connect(self.showMinimized)
		self.buttonMaximum.clicked.connect(self.showMaximized)
		self.buttonNormal.clicked.connect(self.showNormal)
		self.buttonClose.clicked.connect(self.close)

		self.setStyleSheet('#widgetTitleBar{background: rgb(232, 232, 232);}')



	def changeEvent(self, event):
		"""窗口状态改变
		:param event:
		"""
		super(FramelessWindow, self).changeEvent(event)
		# 窗口状态改变时修改标题栏控制按钮
		visible = self.isMaximized()
		self.buttonMaximum.setVisible(not visible)
		self.buttonNormal.setVisible(visible)
		if visible:
			self.layout().setContentsMargins(0, 0, 0, 0)
		else:
			# TODO 与UI文件中的布局边距一致
			m = FramelessObject.Margins
			self.layout().setContentsMargins(m, m, m, m)

	def paintEvent(self, event):
		# 透明背景但是需要留下一个透明度用于鼠标捕获
		painter = QPainter(self)
		painter.fillRect(self.rect(), QColor(255, 255, 255, 1))


class FramelessObject(QObject):
	Margins = 3
	TitleHeight = 36
	Widgets = set()

	@classmethod
	def set_margins(cls, margins):
		cls.Margins = margins

	@classmethod
	def set_title_height(cls, height):
		cls.TitleHeight = height

	@classmethod
	def add_widget(cls, widget):
		cls.Widgets.add(widget)

	@classmethod
	def del_widget(cls, widget):
		if widget in cls.Widgets:
			cls.Widgets.remove(widget)

	def _get_edges(self, pos, width, height):
		edge = 0
		x, y = pos.x(), pos.y()

		if y <= self.Margins:
			edge |= Qt.TopEdge
		if x <= self.Margins:
			edge |= Qt.LeftEdge
		if x >= width - self.Margins:
			edge |= Qt.RightEdge
		if y >= height - self.Margins:
			edge |= Qt.BottomEdge

		return edge

	def _get_cursor(self, edges):
		if edges == Qt.LeftEdge | Qt.TopEdge or edges == Qt.RightEdge | Qt.BottomEdge:
			return Qt.SizeFDiagCursor
		elif edges == Qt.RightEdge | Qt.TopEdge or edges == Qt.LeftEdge | Qt.BottomEdge:
			return Qt.SizeBDiagCursor
		elif edges == Qt.LeftEdge or edges == Qt.RightEdge:
			return Qt.SizeHorCursor
		elif edges == Qt.TopEdge or edges == Qt.BottomEdge:
			return Qt.SizeVerCursor

		return Qt.ArrowCursor

	def is_titlebar(self, pos):
		return pos.y() <= self.TitleHeight

	def moveOrResize(self, window, pos, width, height):
		edges = self._get_edges(pos, width, height)
		if edges:
			if window.windowState() == Qt.WindowNoState:
				window.startSystemResize(edges)
		else:
			if self.is_titlebar(pos):
				window.startSystemMove()

	def eventFilter(self, obj, event):
		if obj.isWindowType():
			if event.type() == QEvent.MouseMove and obj.windowState() == Qt.WindowNoState:
				obj.setCursor(self._get_cursor(self._get_edges(event.pos(), obj.width(), obj.height())))
			elif event.type() == QEvent.TouchUpdate:
				self.moveOrResize(obj, event.pos(), obj.width(), obj.height())
		elif obj in self.Widgets and isinstance(event, QMouseEvent) and event.button() == Qt.LeftButton:
			if event.type() == QEvent.MouseButtonDblClick:
				if self.is_titlebar(event.pos()):
					if obj.windowState() == Qt.WindowFullScreen:
						pass
					elif obj.windowState() == Qt.WindowMaximized:
						obj.showNormal()
					else:
						obj.showMaximized()
			elif event.type() == QEvent.MouseButtonPress:
				self.moveOrResize(obj.windowHandle(), event.pos(), obj.width(), obj.height())
		return False


def resize_screen_ratio(object, screenw, screenh, w_ratio=1/6, h_ratio=1/6, posx_ratio=1/2, posy_ratio=1/2):
	"""
	screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
	screenw, screenh = screen_geometry.width(), screen_geometry.height()
	"""
	lebar, tinggi = int(screenw*w_ratio),int(screenh*h_ratio)
	object.resize(lebar, tinggi)
	posx = int((screenw-lebar)*posx_ratio)
	delta = 60
	posy = int((screenh-tinggi)*posy_ratio) # - delta
	object.move(posx, posy)

def main():
	app = QApplication(sys.argv)
	screen_geometry = QDesktopWidget().screenGeometry(-1)
	screenw, screenh = screen_geometry.width(), screen_geometry.height()

	fo = FramelessObject()
	app.installEventFilter(fo)

	w1 = FramelessWindow()
	resize_screen_ratio(w1, screenw, screenh, w_ratio=1/2, h_ratio=1/2, posx_ratio=0.01, posy_ratio=0.01)
	fo.add_widget(w1)
	w1.show()

	w2 = FramelessWindow()
	resize_screen_ratio(w2, screenw, screenh, w_ratio=1/2, h_ratio=1/2, posx_ratio=0.95, posy_ratio=0.01)
	fo.add_widget(w2)
	w2.show()

	w3 = FramelessWindow()
	resize_screen_ratio(w3, screenw, screenh, w_ratio=1/2, h_ratio=1/2, posx_ratio=0.01, posy_ratio=0.95)
	fo.add_widget(w3)
	w3.show()

	w4 = FramelessWindow()
	resize_screen_ratio(w4, screenw, screenh, w_ratio=1/2, h_ratio=1/2, posx_ratio=0.95, posy_ratio=0.95)
	fo.add_widget(w4)
	w4.show()

	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
