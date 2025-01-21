from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys

envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
bylangsdir = os.environ['ULIBPY_BYLANGSDIR']
sys.path.extend([sidoarjodir, schnelldir])

from schnell.gui.system.searcher.widgets.common import context_menu_stylesheet, about_qt, get_icon


class AcdseeWidget(QGraphicsView):
    """Image viewing controls"""

    def doShow(self):
        try:
            # Attempt to cancel the signal that closes the window after the animation is complete
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # The transparency range gradually increases from 0 to 1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # Close the window when the animation is complete
        # Transparency range gradually decreases from 1 to 0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def init_menu(self):
        # transparent background
        self.context_menu.setAttribute(Qt.WA_TranslucentBackground)
        # No border, remove built-in shadow
        self.context_menu.setWindowFlags(self.context_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        # Simulate menu items
        for i in range(10):
            if i % 2 == 0:
                action = self.context_menu.addAction('menu %d' % i, about_qt)
                action.setEnabled(i % 4)
            elif i % 3 == 0:
                self.context_menu.addAction(get_icon(), 'menu %d' % i, about_qt)
            if i % 4 == 0:
                self.context_menu.addSeparator()
            if i % 5 == 0:
                # Secondary menu
                menu = QMenu('Secondary menu %d' % i, self.context_menu)
                # transparent background
                menu.setAttribute(Qt.WA_TranslucentBackground)
                # No border, remove built-in shadow
                menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
                for j in range(3):
                    menu.addAction(get_icon(), 'Submenu %d' % j)
                self.context_menu.addMenu(menu)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QPixmap(file_path))
            event.accept()
        else:
            event.ignore()

    def __init__(self, *args, **kwargs):
        """
        self.acdsee = AcdseeWidget(self)
        """
        image = kwargs.pop('image', f'../logo.jpg')
        background = kwargs.pop('background', Qt.black)
        super(AcdseeWidget, self).__init__(*args, **kwargs)

        self.setAcceptDrops(True)

        self.setStyleSheet(context_menu_stylesheet)
        self.setCursor(Qt.OpenHandCursor)
        self.setBackground(background)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.SmoothPixmapTransform)
        self.setCacheMode(self.CacheBackground)
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        self._item = QGraphicsPixmapItem()  # place image
        self._item.setFlags(QGraphicsPixmapItem.ItemIsFocusable | QGraphicsPixmapItem.ItemIsMovable)
        self._scene = QGraphicsScene(self)  # Scenes
        self.setScene(self._scene)
        self._scene.addItem(self._item)
        rect = QApplication.instance().desktop().availableGeometry(self)
        self.resize(int(rect.width() * 2 / 3), int(rect.height() * 2 / 3))

        self.pixmap = None
        self._delta = 0.1  # zoom
        self.setPixmap(image)
        # tambah context menu
        self.context_menu = QMenu(self)
        self.init_menu()

        # sblm show, tapi gak berhasil, hrsnya wkt panggil di button click: imagebutton
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(1000)  # Duration 1 second

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def setBackground(self, color):
        """set background color
        :param color: background color
        :type color: QColor or str or GlobalColor
        """
        if isinstance(color, QColor):
            self.setBackgroundBrush(color)
        elif isinstance(color, (str, Qt.GlobalColor)):
            color = QColor(color)
            if color.isValid():
                self.setBackgroundBrush(color)

    def setPixmap(self, pixmap, fitIn=True):
        """load image
        :param pixmap: image or image path
        :param fitIn: Whether to adapt
        :type pixmap: QPixmap or QImage or str
        :type fitIn: bool
        """
        if isinstance(pixmap, QPixmap):
            self.pixmap = pixmap
        elif isinstance(pixmap, QImage):
            self.pixmap = QPixmap.fromImage(pixmap)
        elif isinstance(pixmap, str) and os.path.isfile(pixmap):
            self.pixmap = QPixmap(pixmap)
        else:
            return
        self._item.setPixmap(self.pixmap)
        self._item.update()
        self.setSceneDims()
        if fitIn:
            self.fitInView(QRectF(self._item.pos(), QSizeF(self.pixmap.size())), Qt.KeepAspectRatio)
        self.update()

    def set_image(self, filepath):
        self.setPixmap(filepath)

    def setSceneDims(self):
        if not self.pixmap:
            return
        self.setSceneRect(QRectF(QPointF(0, 0), QPointF(self.pixmap.width(), self.pixmap.height())))

    def fitInView(self, rect, flags=Qt.IgnoreAspectRatio):
        """Adaptation in the play
        :param rect: Rectangular extent
        :param flags:
        :return:
        """
        if not self.scene() or rect.isNull():
            return
        unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        viewRect = self.viewport().rect()
        sceneRect = self.transform().mapRect(rect)
        x_ratio = viewRect.width() / sceneRect.width()
        y_ratio = viewRect.height() / sceneRect.height()
        if flags == Qt.KeepAspectRatio:
            x_ratio = y_ratio = min(x_ratio, y_ratio)
        elif flags == Qt.KeepAspectRatioByExpanding:
            x_ratio = y_ratio = max(x_ratio, y_ratio)
        self.scale(x_ratio, y_ratio)
        self.centerOn(rect.center())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def zoomIn(self):
        """enlarge"""
        self.zoom(1 + self._delta)

    def zoomOut(self):
        """zoom out"""
        self.zoom(1 - self._delta)

    def zoom(self, factor):
        """zoom
        :param factor: scaling factor
        """
        _factor = self.transform().scale(factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            # Prevent too big and too small
            return
        self.scale(factor, factor)
