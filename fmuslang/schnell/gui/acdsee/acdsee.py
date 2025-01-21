#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年3月21日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: Splitter
@description: 
"""
import os, random, string, sys

# from lxml.etree import HTML
# from PyQt5.QtCore import QPointF, Qt, QRectF, QSizeF


from PyQt5.QtNetwork import (QNetworkAccessManager, QNetworkRequest)
from PyQt5.QtSvg import QSvgWidget

from PyQt5.QtCore import (
    Qt,
    QSortFilterProxyModel,
    QDir,
    QFileInfo,
    QPoint, QPointF,
    QPropertyAnimation,
    QRectF,
    QSize, QSizeF,
    QUrl,
    QTimer,
    QModelIndex,
    pyqtSignal,
    pyqtSlot,
)

from PyQt5.QtGui import (
    QBrush, 
    QColor,
    QEnterEvent,
    QFont,
    QGradient,
    QIcon,
    QImage,
    QLinearGradient,
    QPainter,
    QPaintEvent,
    QPen,
    QPixmap,
    QPolygonF,
    QStandardItem,
    QStandardItemModel,
)

from PyQt5.QtWidgets import (
    QAbstractSlider,
    QApplication, 
    QDesktopWidget,
    QFileDialog,
    QFileIconProvider,
    QFileSystemModel,
    QGraphicsView, QGraphicsPixmapItem, QGraphicsScene,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListView,
    QListWidget,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSpacerItem,
    QSizePolicy,
    QSpacerItem,
    QSplitter,
    QSplitterHandle,
    QTextEdit,
    QTreeView,
    QTreeWidget,
    QVBoxLayout,
    QWidget,
)
# from matplotlib.image import thumbnail

"""
I want to get the file path and the file name from a Tree View in pyqt5.
I had it working, but I wanted to implement searching, which works,
but doing that I sacrificed the ability to get the filename and file path.
This is my tree:

class Folder_Screeen(QDialog):
    def __init__(self, parent = None):
        super(Folder_Screeen, self).__init__(parent)
        self.path = expanduser(os.path.dirname(os.path.realpath(__file__)))
        self.pathRoot = QDir.rootPath()

        self.labelFileName = QLabel(self)
        self.labelFileName.setText("Search:")
        self.labelFileName.resize(100, 30)

        self.txtSearch = QLineEdit(self)
        self.txtSearch.textChanged.connect(self.on_textChanged)
        self.thumbnail = QLabel(self)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries | QDir.Dirs | QDir.Files)
        self.proxy_model = QSortFilterProxyModel(recursiveFilteringEnabled = True, filterRole = QFileSystemModel.FileNameRole)
        self.proxy_model.setSourceModel(self.model)
        self.model.setReadOnly(False)
        self.model.setNameFilterDisables(False)

        self.indexRoot = self.model.index(self.model.rootPath())

        self.treeView = QTreeView(self)
        self.treeView.setModel(self.proxy_model)
        self.adjust_root_index()
        # self.treeView.setRootIndex(self.model.index(self.path))
        self.treeView.setRootIndex(self.proxy_model.mapFromSource(self.model.index(self.path)))
        self.treeView.clicked.connect(self.on_treeView_clicked)
        # self.treeView.setSelectionMode(self.SingleSelection)
        self.treeView.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeView.setAnimated(True)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)
        self.treeView.setDragEnabled(True)
        self.treeView.setAcceptDrops(True)
        self.treeView.setDropIndicatorShown(True)
        self.treeView.setEditTriggers(QTreeView.NoEditTriggers)
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.showContextMenu)

    @QtCore.pyqtSlot(str)
    def on_textChanged(self):
        self.proxy_model.setFilterWildcard("*{}*".format(self.txtSearch.text()))
        self.adjust_root_index()

    def adjust_root_index(self):
        root_index = self.model.index(self.path)
        proxy_index = self.proxy_model.mapFromSource(root_index)
        self.treeView.setRootIndex(proxy_index)

    def btnAddFolder(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Create Folder", "","All Files (*)", options=options)
        if fileName:
            print(fileName)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            if self.lineEditFilePath.text() != '':
                os.remove(self.lineEditFilePath.text())

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())# print(indexItem)
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.thumbnail.setPixmap(QPixmap(filePath))
        self.thumbnail.setAlignment(Qt.AlignRight | Qt.AlignBottom)

        print(fileName)
        print(filePath)

    def dragEnterEvent(self, event):
        m = event.mimeData()
        if m.hasUrls():
            for url in m.urls():
                if url.isLocalFile():
                    event.accept()
                    return
        event.ignore()

    def dropEvent(self, event):
        if event.source():
            QTreeView.dropEvent(self, event)
        else:
            ix = self.indexAt(event.pos())
            if not self.model().isDir(ix):
                ix = ix.parent()
            pathDir = self.model().filePath(ix)
            m = event.mimeData()
            if m.hasUrls():
                urlLocals = [url for url in m.urls() if url.isLocalFile()]
                accepted = False
                for urlLocal in urlLocals:
                    path = urlLocal.toLocalFile()
                    info = QFileInfo(path)
                    n_path = QDir(pathDir).filePath(info.fileName())
                    o_path = info.absoluteFilePath()
                    if n_path == o_path:
                        continue
                    if info.isDir():
                        QDir().rename(o_path, n_path)
                    else:
                        qfile = QFile(o_path)
                        if QFile(n_path).exists():
                            n_path += "(copy)"
                        qfile.rename(n_path)
                    accepted = True
                if accepted:
                    event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def showContextMenu(self, point):
        ix = self.treeView.indexAt(point)
        if ix.column() == 0:
            menu = QMenu()
            menu.addAction("Rename")
            action = menu.exec_(self.treeView.mapToGlobal(point))
            if action:
                if action.text() == "Rename":
                    self.treeView.edit(ix)
    # TREE VIEW END ====================================

I don't get any output of any kind, just a empty string or the main system drive.
The solotuons works if I change this line of code on line 26
self.treeView.setModel(self.proxy_model)
to
self.treeView.setModel(self.model)
"""
envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
bylangsdir = os.environ['ULIBPY_BYLANGSDIR']
sys.path.extend([sidoarjodir, schnelldir])

# from schnell.app.utils import env_get
from schnell.app.dirutils import joiner


imagedir = 'images'

ScrollPixel = 40

Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

context_menu_stylesheet = """
QMenu {
    /* 半透明效果 */
    background-color: rgba(255, 255, 255, 230);
    border: none;
    border-radius: 4px;
}

QMenu::item {
    border-radius: 4px;
    /* 这个距离很麻烦需要根据菜单的长度和图标等因素微调 */
    padding: 8px 48px 8px 36px; /* 36px是文字距离左侧距离*/
    background-color: transparent;
}

/* 鼠标悬停和按下效果 */
QMenu::item:selected {
    border-radius: 0px;
    /* 半透明效果 */
    background-color: rgba(232, 232, 232, 232);
}

/* 禁用效果 */
QMenu::item:disabled {
    background-color: transparent;
}

/* 图标距离左侧距离 */
QMenu::icon {
    left: 15px;
}

/* 分割线效果 */
QMenu::separator {
    height: 1px;
    background-color: rgb(232, 236, 243);
}
"""

frameless_window_stylesheet = """
/*标题栏*/
TitleBar {
    background-color: rgb(54, 157, 180);
}

/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
    background-color: rgb(54, 157, 180);
}

/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {
    background-color: rgb(48, 141, 162);
}
#buttonClose:hover {
    color: white;
    background-color: rgb(232, 17, 35);
}

/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {
    background-color: rgb(44, 125, 144);
}
#buttonClose:pressed {
    color: white;
    background-color: rgb(161, 73, 92);
}
"""


def get_icon():
    # test mock icon
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
    # About Qt
    QApplication.instance().aboutQt()


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
        image = kwargs.pop('image', f'{imagedir}/head.jpg')
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
            self.fitInView(QRectF(self._item.pos(), QSizeF(
                self.pixmap.size())), Qt.KeepAspectRatio)
        self.update()

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
        _factor = self.transform().scale(
            factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            # Prevent too big and too small
            return
        self.scale(factor, factor)


class ImageItemWidget(QWidget):

    def __init__(self, pixmapimage, *args, **kwargs):
        super(ImageItemWidget, self).__init__(*args, **kwargs)
        self.setMaximumSize(220, 380)
        self.setMaximumSize(220, 380)
        layout = QVBoxLayout(self) # layout utk widget
        layout.setContentsMargins(0, 0, 0, 0)
        # self.clabel = QLabel(self, pixmap=QPixmap("images/head.jpg"))
        self.clabel = QLabel(self, pixmap=pixmapimage)
        layout.addWidget(self.clabel)

    def sizeHint(self):
        # The size of each item control
        return QSize(220, 380)


class ImageGridWidget(QWidget):

    Page = 0
    loadStarted = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super(ImageGridWidget, self).__init__(*args, **kwargs)
        self._layout = QGridLayout(self, spacing=20)
        self._layout.setContentsMargins(20, 20, 20, 20)
        self.setStyleSheet('border: 5px solid green;')
        # Asynchronous Network Download Manager
        # self._manager = QNetworkAccessManager(self)
        # self._manager.finished.connect(self.onFinished)
        self.cols = 5
        # self.rows = 10
        self.scale = 120
        
        self._makeItem(10, 5)


    def _makeItem(self, rows, cols):
        pass
        # for row in range(rows):
        #     for col in range(cols):
        #         iwidget = ImageItemWidget(row, col)
        #         self._layout.addWidget(iwidget, row, col)

    def clear_layout(self):
        """
        https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
        """
        for i in reversed(range(self._layout.count())): 
            widgetToRemove = self._layout.itemAt(i).widget()
            # remove it from the layout list
            self._layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    def reload(self, dirpath):
        self.clear_layout()
        items = [os.path.join(dirpath, item) for item in os.listdir(dirpath) if os.path.splitext(item)[1] in ['.jpg', '.png'] ]
        if items:
            row = 1
            for item in items:                
                col = 1
                # for c in range(self.cols):
                print('grid item:', item)
                # thumbnail = item.scaled(self.scale, self.scale, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                thumbnail = QPixmap(item)
                self._layout.addWidget(ImageItemWidget(thumbnail), row, col)
                col += 1
                if col > 3:
                    row += 1
                    col = 1


class BigImageView(QGraphicsView):
    """图片查看控件"""

    def __init__(self, *args, **kwargs):
        image = kwargs.pop('image', None)
        background = kwargs.pop('background', None)
        super(BigImageView, self).__init__(*args, **kwargs)
        self.setCursor(Qt.OpenHandCursor)
        self.setBackground(background)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                            QPainter.SmoothPixmapTransform)
        self.setCacheMode(self.CacheBackground)
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        self._item = QGraphicsPixmapItem()  # 放置图像
        self._item.setFlags(QGraphicsPixmapItem.ItemIsFocusable |
                            QGraphicsPixmapItem.ItemIsMovable)
        self._scene = QGraphicsScene(self)  # 场景
        self.setScene(self._scene)
        self._scene.addItem(self._item)
        rect = QApplication.instance().desktop().availableGeometry()
        self.resize(int(rect.width() * 2 / 3), int(rect.height() * 2 / 3))

        self.pixmap = None
        self._delta = 0.1  # 缩放
        self.setPixmap(image)

    def setBackground(self, color):
        """设置背景颜色
        :param color: 背景颜色
        :type color: QColor or str or GlobalColor
        """
        if isinstance(color, QColor):
            self.setBackgroundBrush(color)
        elif isinstance(color, (str, Qt.GlobalColor)):
            color = QColor(color)
            if color.isValid():
                self.setBackgroundBrush(color)

    def setPixmap(self, pixmap, fitIn=True):
        """加载图片
        :param pixmap: 图片或者图片路径
        :param fitIn: 是否适应
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
            self.fitInView(QRectF(self._item.pos(), QSizeF(
                self.pixmap.size())), Qt.KeepAspectRatio)
        self.update()

    def setSceneDims(self):
        if not self.pixmap:
            return
        self.setSceneRect(QRectF(QPointF(0, 0), QPointF(self.pixmap.width(), self.pixmap.height())))

    def fitInView(self, rect, flags=Qt.IgnoreAspectRatio):
        """剧中适应
        :param rect: 矩形范围
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
        """放大"""
        self.zoom(1 + self._delta)

    def zoomOut(self):
        """缩小"""
        self.zoom(1 - self._delta)

    def zoom(self, factor):
        """缩放
        :param factor: 缩放的比例因子
        """
        _factor = self.transform().scale(
            factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            # 防止过大过小
            return
        self.scale(factor, factor)


class ImageView(QListView):

    def __init__(self, *args, **kwargs):
        super(ImageView, self).__init__(*args, **kwargs)
        self.setFrameShape(self.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setEditTriggers(self.NoEditTriggers)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(self.DragDrop)
        self.setDefaultDropAction(Qt.IgnoreAction)
        self.setSelectionMode(self.ExtendedSelection)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.setFlow(self.LeftToRight)
        self.setWrapping(True)
        self.setResizeMode(self.Adjust)
        self.setSpacing(6)
        self.setViewMode(self.IconMode)
        self.setWordWrap(True)
        self.setSelectionRectVisible(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 解决拖动到顶部或者底部自动滚动
        self.setAutoScrollMargin(150)
        self.verticalScrollBar().setSingleStep(ScrollPixel)
        # 设置model
        self.dmodel = QStandardItemModel(self)
        self.setModel(self.dmodel)

        # 大图控件
        self.bigView = BigImageView(background='#323232')

    def addItem(self, image):
        if isinstance(image, str):
            image = QPixmap(image)
        # 添加一个item
        item = QStandardItem()
        # 记录原始图片
        item.setData(image, Qt.UserRole + 1)  # 用于双击的时候取出来
        # 缩放成小图并显示
        scale = 120
        # item.setData(image.scaled(60, 60, Qt.IgnoreAspectRatio, Qt.SmoothTransformation), Qt.DecorationRole)
        item.setData(image.scaled(scale, scale, Qt.IgnoreAspectRatio, Qt.SmoothTransformation), Qt.DecorationRole)
        # 添加item到界面中
        self.dmodel.appendRow(item)

    def count(self):
        return self.dmodel.rowCount()

    def setCurrentRow(self, row):
        self.setCurrentIndex(self.dmodel.index(row, 0))

    def currentRow(self):
        return self.currentIndex().row()

    def updateGeometries(self):
        # 一次滑动20px
        super(ImageView, self).updateGeometries()
        self.verticalScrollBar().setSingleStep(ScrollPixel)

    def closeEvent(self, event):
        # 关闭预览窗口
        self.bigView.close()
        super(ImageView, self).closeEvent(event)

    def wheelEvent(self, event):
        # 修复滑动bug
        if self.flow() == QListView.LeftToRight:
            bar = self.horizontalScrollBar()
            value = ScrollPixel if event.angleDelta().y() < 0 else (0 - ScrollPixel)
            bar.setSliderPosition(bar.value() + value)
        else:
            super(ImageView, self).wheelEvent(event)

    def mouseDoubleClickEvent(self, event):
        # 列表双击,如果有item则进入item处理流程,否则调用打开图片功能
        index = self.indexAt(event.pos())
        if index and index.isValid():
            item = self.dmodel.itemFromIndex(index)
            if item:
                # 取出原图用来新窗口显示
                image = item.data(Qt.UserRole + 1)
                self.bigView.setPixmap(image)
                self.bigView.show()
            return
        super(ImageView, self).mouseDoubleClickEvent(event)



    def reload(self, dirpath):
        # self.clear_layout()
        items = [os.path.join(dirpath, item) for item in os.listdir(dirpath) if os.path.splitext(item)[1] in ['.jpg', '.png'] ]
        if items:
            for item in items:
                self.addItem(item)


class ImageGallery(QScrollArea):

    def __init__(self, *args, **kwargs):
        super(ImageGallery, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setFrameShape(self.NoFrame)
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignCenter)
        self._loadStart = False
        # grid window
        self._widget = ImageGridWidget(self)
        self._widget.loadStarted.connect(self.setLoadStarted)
        self.setWidget(self._widget)
        # Connect vertical scroll bar scroll events
        self.verticalScrollBar().actionTriggered.connect(self.onActionTriggered)
        # progress bar
        # self.loadWidget = QSvgWidget(self, minimumHeight=120, minimumWidth=120, visible=False)
        # self.loadWidget.load(Svg_icon_loading)

    def setLoadStarted(self, started):
        self._loadStart = started
        # self.loadWidget.setVisible(started)

    def onActionTriggered(self, action):
        # Here to judge the action=QAbstractSlider.SliderMove, which can avoid the problem of window size changing
        # Also prevent multiple loading of the same url
        if action != QAbstractSlider.SliderMove or self._loadStart:
            return
        # Using sliderPosition to get the value can satisfy both mouse sliding and dragging judgments
        if self.verticalScrollBar().sliderPosition() == self.verticalScrollBar().maximum():
            # can go to the next page
            # self._widget.load()
            pass

    def resizeEvent(self, event):
        super(ImageGallery, self).resizeEvent(event)


class TitleBar(QWidget):
    # 窗口最小化信号
    windowMinimumed = pyqtSignal()
    # 窗口最大化信号
    windowMaximumed = pyqtSignal()
    # 窗口还原信号
    windowNormaled = pyqtSignal()
    # 窗口关闭信号
    windowClosed = pyqtSignal()
    # 窗口移动
    windowMoved = pyqtSignal(QPoint)

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)
        # 支持qss设置背景
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mPos = None
        self.iconSize = 20  # 图标的默认大小
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self.setPalette(palette)
        # 布局
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # 窗口图标
        self.iconLabel = QLabel(self)
        #         self.iconLabel.setScaledContents(True)
        layout.addWidget(self.iconLabel)
        # 窗口标题
        self.titleLabel = QLabel(self)
        self.titleLabel.setMargin(2)
        layout.addWidget(self.titleLabel)
        # 中间伸缩条
        layout.addSpacerItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        # 利用Webdings字体来显示图标
        font = self.font() or QFont()
        font.setFamily('Webdings')
        # 最小化按钮
        self.buttonMinimum = QPushButton(
            '0', self, clicked=self.windowMinimumed.emit, font=font, objectName='buttonMinimum')
        layout.addWidget(self.buttonMinimum)
        # 最大化/还原按钮
        self.buttonMaximum = QPushButton(
            '1', self, clicked=self.showMaximized, font=font, objectName='buttonMaximum')
        layout.addWidget(self.buttonMaximum)
        # 关闭按钮
        self.buttonClose = QPushButton(
            'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
        layout.addWidget(self.buttonClose)
        # 初始高度
        self.setHeight()

    def showMaximized(self):
        if self.buttonMaximum.text() == '1':
            # 最大化
            self.buttonMaximum.setText('2')
            self.windowMaximumed.emit()
        else:  # 还原
            self.buttonMaximum.setText('1')
            self.windowNormaled.emit()

    def setHeight(self, height=38):
        """设置标题栏高度"""
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        # 设置右边按钮的大小
        self.buttonMinimum.setMinimumSize(height, height)
        self.buttonMinimum.setMaximumSize(height, height)
        self.buttonMaximum.setMinimumSize(height, height)
        self.buttonMaximum.setMaximumSize(height, height)
        self.buttonClose.setMinimumSize(height, height)
        self.buttonClose.setMaximumSize(height, height)

    def setTitle(self, title):
        """设置标题"""
        self.titleLabel.setText(title)

    def setIcon(self, icon):
        """设置图标"""
        self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))

    def setIconSize(self, size):
        """设置图标大小"""
        self.iconSize = size

    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(TitleBar, self).enterEvent(event)

    def mouseDoubleClickEvent(self, event):
        super(TitleBar, self).mouseDoubleClickEvent(event)
        self.showMaximized()

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()


class FramelessWindow(QWidget):
    # 四周边距
    Margins = 5

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self._pressed = False
        self.Direction = None
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 无边框
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # 鼠标跟踪
        self.setMouseTracking(True)
        # 布局
        layout = QVBoxLayout(self, spacing=0)
        # 预留边界用于实现无边框窗口调整大小
        layout.setContentsMargins(self.Margins, self.Margins, self.Margins, self.Margins)
        # 标题栏
        self.titleBar = TitleBar(self)
        layout.addWidget(self.titleBar)
        # 信号槽
        self.titleBar.windowMinimumed.connect(self.showMinimized)
        self.titleBar.windowMaximumed.connect(self.showMaximized)
        self.titleBar.windowNormaled.connect(self.showNormal)
        self.titleBar.windowClosed.connect(self.close)
        self.titleBar.windowMoved.connect(self.move)
        self.windowTitleChanged.connect(self.titleBar.setTitle)
        self.windowIconChanged.connect(self.titleBar.setIcon)

    def setTitleBarHeight(self, height=38):
        """设置标题栏高度"""
        self.titleBar.setHeight(height)

    def setIconSize(self, size):
        """设置图标的大小"""
        self.titleBar.setIconSize(size)

    def setWidget(self, widget):
        """设置自己的控件"""
        if hasattr(self, '_widget'):
            return
        self._widget = widget
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self._widget.setAutoFillBackground(True)
        palette = self._widget.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self._widget.setPalette(palette)
        self._widget.installEventFilter(self)
        self.layout().addWidget(self._widget)

    def move(self, pos):
        if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
            # 最大化或者全屏则不允许移动
            return
        super(FramelessWindow, self).move(pos)

    def showMaximized(self):
        """最大化,要去除上下左右边界,如果不去除则边框地方会有空隙"""
        super(FramelessWindow, self).showMaximized()
        self.layout().setContentsMargins(0, 0, 0, 0)

    def showNormal(self):
        """还原,要保留上下左右边界,否则没有边框无法调整"""
        super(FramelessWindow, self).showNormal()
        self.layout().setContentsMargins(
            self.Margins, self.Margins, self.Margins, self.Margins)

    def eventFilter(self, obj, event):
        """事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式"""
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
        return super(FramelessWindow, self).eventFilter(obj, event)

    def paintEvent(self, event):
        """由于是全透明背景窗口,重绘事件中绘制透明度为1的难以发现的边框,用于调整窗口大小"""
        super(FramelessWindow, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 255, 255, 1), 2 * self.Margins))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        super(FramelessWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self._mpos = event.pos()
            self._pressed = True

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        super(FramelessWindow, self).mouseReleaseEvent(event)
        self._pressed = False
        self.Direction = None

    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        super(FramelessWindow, self).mouseMoveEvent(event)
        pos = event.pos()
        xPos, yPos = pos.x(), pos.y()
        wm, hm = self.width() - self.Margins, self.height() - self.Margins
        if self.isMaximized() or self.isFullScreen():
            self.Direction = None
            self.setCursor(Qt.ArrowCursor)
            return
        if event.buttons() == Qt.LeftButton and self._pressed:
            self._resizeWidget(pos)
            return
        if xPos <= self.Margins and yPos <= self.Margins:
            # 左上角
            self.Direction = LeftTop
            self.setCursor(Qt.SizeFDiagCursor)
        elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
            # 右下角
            self.Direction = RightBottom
            self.setCursor(Qt.SizeFDiagCursor)
        elif wm <= xPos and yPos <= self.Margins:
            # 右上角
            self.Direction = RightTop
            self.setCursor(Qt.SizeBDiagCursor)
        elif xPos <= self.Margins and hm <= yPos:
            # 左下角
            self.Direction = LeftBottom
            self.setCursor(Qt.SizeBDiagCursor)
        elif 0 <= xPos <= self.Margins and self.Margins <= yPos <= hm:
            # 左边
            self.Direction = Left
            self.setCursor(Qt.SizeHorCursor)
        elif wm <= xPos <= self.width() and self.Margins <= yPos <= hm:
            # 右边
            self.Direction = Right
            self.setCursor(Qt.SizeHorCursor)
        elif self.Margins <= xPos <= wm and 0 <= yPos <= self.Margins:
            # 上面
            self.Direction = Top
            self.setCursor(Qt.SizeVerCursor)
        elif self.Margins <= xPos <= wm and hm <= yPos <= self.height():
            # 下面
            self.Direction = Bottom
            self.setCursor(Qt.SizeVerCursor)

    def _resizeWidget(self, pos):
        """调整窗口大小"""
        if self.Direction == None:
            return
        mpos = pos - self._mpos
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:  # 左上角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
        elif self.Direction == RightBottom:  # 右下角
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
        elif self.Direction == RightTop:  # 右上角
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos.setX(pos.x())
        elif self.Direction == LeftBottom:  # 左下角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos.setY(pos.y())
        elif self.Direction == Left:  # 左边
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            else:
                return
        elif self.Direction == Right:  # 右边
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            else:
                return
        elif self.Direction == Top:  # 上面
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            else:
                return
        elif self.Direction == Bottom:  # 下面
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
            else:
                return
        self.setGeometry(x, y, w, h)


class FileIconProvider(QFileIconProvider):
    """Icon provider class"""

    def __init__(self, *args, **kwargs):
        super(FileIconProvider, self).__init__(*args, **kwargs)
        self.DirIcon = QIcon(f"{imagedir}/folder.png")
        self.TxtIcon = QIcon(f"{imagedir}/file.png")

    def icon(self, type_info):
        '''
        :param fileInfo: 参考http://doc.qt.io/qt-5/qfileinfo.html
        '''
        if isinstance(type_info, QFileInfo):
            # 如果type_info是QFileInfo类型则用getInfoIcon来返回图标
            return self.getInfoIcon(type_info)
        # 如果type_info是QFileIconProvider自身的IconType枚举类型则执行下面的方法
        # 这里只能自定义通用的几种类型，参考http://doc.qt.io/qt-5/qfileiconprovider.html#IconType-enum
        '''
        QFileIconProvider::Computer     0
        QFileIconProvider::Desktop      1
        QFileIconProvider::Trashcan     2
        QFileIconProvider::Network      3
        QFileIconProvider::Drive        4
        QFileIconProvider::Folder       5
        QFileIconProvider::File         6
        '''
        if type_info == QFileIconProvider.Folder:
            # 如果是文件夹
            return self.DirIcon
        return super(FileIconProvider, self).icon(type_info)

    def getInfoIcon(self, type_info):
        if type_info.isDir():  # 文件夹
            return self.DirIcon
        if type_info.isFile() and type_info.suffix() == "txt":  # 文件并且是txt
            return self.TxtIcon
        return super(FileIconProvider, self).icon(type_info)

# basedir = os.getcwd()

class FileTree(QTreeView):

    def __init__(self, curdir=os.getcwd(), *args, **kwargs):
        super(FileTree, self).__init__(*args, **kwargs)

        # https://stackoverflow.com/questions/58881818/how-to-get-selected-item-in-qfilesystemmodel-and-qtreeview
        self.model = QFileSystemModel()
        self.model.setIconProvider(FileIconProvider())  # 设置为自定义的图标提供类
        print(f"[FileTree] curdir = {curdir}")
        # curdir = QDir.currentPath()
        self.model.setRootPath(curdir)

        # self.model.setRootPath(QDir.rootPath())
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries | QDir.Dirs | QDir.Files)
        # self.proxy_model = QSortFilterProxyModel(recursiveFilteringEnabled = True, filterRole = QFileSystemModel.FileNameRole)
        # self.proxy_model.setSourceModel(self.model)
        
        # self.model.setReadOnly(False)
        # self.model.setNameFilterDisables(False)

        # self.setModel(self.proxy_model)
        self.setModel(self.model)
        the_index = self.model.index(curdir)
        # self.expand(the_index)
        self.setRootIndex(the_index)
        # self.setAnimated(False)
        self.setAnimated(True)
        self.setIndentation(20)
        self.setSortingEnabled(True)
        self.setWindowTitle("Dir View")


class SplitterHandle(QSplitterHandle):

    clicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(SplitterHandle, self).__init__(*args, **kwargs)
        # 如果不设置这个，则鼠标只能在按下后移动才能响应mouseMoveEvent
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        super(SplitterHandle, self).mousePressEvent(event)
        if event.pos().y() <= 24:
            # 发送点击信号
            self.clicked.emit()

    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        # 当y坐标小于24时,也就是顶部的矩形框高度
        if event.pos().y() <= 24:
            # 取消鼠标样式
            self.unsetCursor()
            event.accept()
        else:
            # 设置默认的鼠标样式并可以移动
            self.setCursor(Qt.SplitHCursor if self.orientation()
                                              == Qt.Horizontal else Qt.SplitVCursor)
            super(SplitterHandle, self).mouseMoveEvent(event)

    def paintEvent(self, event):
        # 绘制默认的样式
        super(SplitterHandle, self).paintEvent(event)
        # 绘制顶部扩展按钮
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.red)
        # 画矩形
        painter.drawRect(0, 0, self.width(), 24)
        # 画三角形
        painter.setBrush(Qt.red)
        painter.drawPolygon(QPolygonF([
            QPointF(0, (24 - 8) / 2),
            QPointF(self.width() - 2, 24 / 2),
            QPointF(0, (24 + 8) / 2)
        ]))


class Splitter(QSplitter):

    def onClicked(self):
        print('clicked')

    def createHandle(self):
        if self.count() == 1:
            # 这里表示第一个分割条
            handle = SplitterHandle(self.orientation(), self)
            handle.clicked.connect(self.onClicked)
            return handle
        return super(Splitter, self).createHandle()


class SplitterWindow(QMainWindow):

    def pilih_image(self, index):
        # print(f'pilih image, idx:', index)
        # index = self.indexAt(event.pos())
        if index and index.isValid():
            item = self.gallery.dmodel.itemFromIndex(index)
            if item:
                # 取出原图用来新窗口显示
                image = item.data(Qt.UserRole + 1)
                # print('pilih image, img:', image)
                self.imageview.setPixmap(image)

    @pyqtSlot(QModelIndex)
    def pilih_folder(self, index):
        """
        {0: 'Acer (C:)', 1: <PyQt5.QtGui.QIcon object at 0x0000023171708040>, 2: 'Acer (C:)'}
        {0: 'Users', 1: <PyQt5.QtGui.QIcon object at 0x0000023171708040>, 2: 'Users'}
        {0: 'usef', 1: <PyQt5.QtGui.QIcon object at 0x0000023171708040>, 2: 'usef'}
        {0: 'Pictures', 1: <PyQt5.QtGui.QIcon object at 0x0000023171708040>, 2: 'Pictures'}


        {0: 'Pictures', 1: <PyQt5.QtGui.QIcon object at 0x000002500DA98040>, 2: 'Pictures'} 
        selected: 
        [
            <PyQt5.QtCore.QModelIndex object at 0x000002500D5C7D10>, 
            <PyQt5.QtCore.QModelIndex object at 0x000002500D5C7C30>, 
            <PyQt5.QtCore.QModelIndex object at 0x000002500D5C7D80>, 
            <PyQt5.QtCore.QModelIndex object at 0x000002500D5C7DF0>
        ]
        """
        # https://stackoverflow.com/questions/29680105/how-to-get-the-pyqt-qtreeview-item-child-using-double-click-event
        # selected = self.filesystem_tree.selectedIndexes()
        # selected_data = [item.data() for item in selected]
        # item = selected[0]
        # nilai = item.data() # Pictures
        # # nilai = item.model().itemFromIndex(index).text()
        # # nilai = item.model().itemData(index)
        # # nilai = self.name_of_model.filePath(index)
        # # nilai = index.model().filePath(index)
        # print(nilai, 'selected:', selected_data)

        # https://stackoverflow.com/questions/58881818/how-to-get-selected-item-in-qfilesystemmodel-and-qtreeview
        # source_index = self.filesystem_tree.proxy_model.mapToSource(index)
        # indexItem = self.filesystem_tree.model.index(source_index.row(), 0, source_index.parent())
        indexItem = index
        fileName = self.filesystem_tree.model.fileName(indexItem)
        filePath = self.filesystem_tree.model.filePath(indexItem)

        # self.thumbnail.setPixmap(QPixmap(filePath))
        # self.thumbnail.setAlignment(Qt.AlignRight | Qt.AlignBottom)

        # print(f"filename = {fileName}, path = {filePath}")

        # reload gallery
        if os.path.isdir(filePath):
            self.gallery.reload(filePath)
        
    def __init__(self, screenw, screenh, basedir=os.getcwd(), parent=None):
        super(SplitterWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(int(screenw * 3/4), int(screenh * 3/4))
        self.setWindowTitle('Image Browser')

        print(f"[SplitterWindow] basedir = {basedir}")

        splitter = Splitter(self)
        splitter.setHandleWidth(8)

        self.filesystem_tree = FileTree(curdir=basedir)
        # self.gallery = ImageGallery()
        self.gallery = ImageView()
        self.imageview = AcdseeWidget()

        # self.filesystem_tree.doubleClicked.connect(self.pilih_folder)
        self.filesystem_tree.clicked.connect(self.pilih_folder)
        self.gallery.clicked.connect(self.pilih_image)

        second_splitter = QSplitter(self)
        second_splitter.setHandleWidth(8)
        second_splitter.setOrientation(Qt.Vertical)
        # harusnya gunakan istilah: gallery + viewer
        # di atas adlh list of image thumbnails = ImageView
        second_splitter.addWidget(self.gallery)
        # di bawah adlh viewer utk image yg terpilih = AcdseeWidget
        second_splitter.addWidget(self.imageview)

        splitter.addWidget(self.filesystem_tree)
        # splitter.addWidget(listwidget)
        # splitter.addWidget(treewidget)
        splitter.addWidget(second_splitter)
        # Qt.Vertical 垂直   Qt.Horizontal 水平
        splitter.setOrientation(Qt.Horizontal)
        self.setCentralWidget(splitter)

        self.initial_path = None

    def open(self):
        file_path = QFileDialog.getExistingDirectory(self, 'select file folder', '.')
        if file_path ==None:
            QMessageBox.information(self,'hint','The file is empty, please try again')
        else:
            self.initial_path = file_path


def acdsee(basedir=os.getcwd()):
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    main = SplitterWindow(screenw, screenh, basedir)
    # main.show()
    w = FramelessWindow()
    w.setStyleSheet(frameless_window_stylesheet)
    w.setWindowTitle(f' [Image Browser][{basedir}] ')
    w.setWindowIcon(QIcon(joiner(sidoarjodir, 'fmus.ico')))
    # w.resize(int(screenw*3/4), int(screenh*3/4))
    w.setWidget(main)
    # w.showMaximized()
    return w


def acdsee_app(basedir=os.getcwd()):
    # print(f'''
    # sys.argv: {sys.argv}
    # len: {len(sys.argv)}
    # ''')
    app = QApplication(sys.argv)
    # QWidget: Must construct a QApplication before a QWidget
    # https://stackoverflow.com/questions/35887237/current-screen-size-in-python3-with-pyqt5
    # basedir = os.getcwd()
    if len(sys.argv) == 2:
        basedir = sys.argv[1]
    # screen_geometry = QDesktopWidget().screenGeometry(-1)
    # screenw, screenh = screen_geometry.width(), screen_geometry.height()
    # main = SplitterWindow(screenw, screenh, basedir)
    # # main.show()
    # w = FramelessWindow()
    # w.setStyleSheet(frameless_window_stylesheet)
    # w.setWindowTitle(' [Image Browser] ')
    # w.setWindowIcon(QIcon('fmus.ico'))
    # w.resize(int(screenw*3/4), int(screenh*3/4))
    # w.setWidget(main)
    w = acdsee(basedir)
    # w.show()
    w.showMaximized()
    sys.exit(app.exec_())


def image_browser(basedir=None):
    try:
        acdsee(basedir=basedir)
    except:
        acdsee_app(basedir=basedir)


if __name__ == '__main__':
    acdsee_app()
