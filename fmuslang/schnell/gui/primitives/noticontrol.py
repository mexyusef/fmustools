import random, string, sys
import webbrowser
from PyQt5.QtGui import (
    QFont,
    QIcon,
    QPainter,
    QPixmap,
)
from PyQt5.QtCore import (
    Qt,
    pyqtSignal,
    
    QEasingCurve,
    QPoint,
    QPropertyAnimation,
    QSize,
    QTimer,
)
from PyQt5.QtWidgets import (
    qApp,

    QAction,
    QApplication,
    QDesktopWidget,
    QHBoxLayout,
    QMenu,
    QPushButton,
    QStyle,
    QSystemTrayIcon,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QToolTip,
    QVBoxLayout,
    QWidget,
)
from PyQt5 import QtCore, QtGui, QtWidgets


mystylesheet = """
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

QWidget#widgetTitle {
    background-color: rgb(76, 169, 106);
}
QWidget#widgetBottom {
    border-top-style: solid;
    border-top-width: 2px;
    border-top-color: rgb(185, 218, 201);
}
QLabel#labelTitle {
    color: rgb(255, 255, 255);
}
QLabel#labelContent {
    padding: 5px;
}
QPushButton {
    border: none;
    background: transparent;
}
QPushButton#buttonState {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}
QPushButton#buttonState:hover {
    background-color: rgb(64, 239, 212);
}
QPushButton#buttonState:checked {
    background-color: orange;
    border-style: outset;
}
QPushButton#buttonReset {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}
QPushButton#buttonReset:hover {
    background-color: rgb(64, 39, 212);
}
QPushButton#buttonClose {
    font-family: "webdings";
    color: rgb(255, 255, 255);
}
QPushButton#buttonClose:hover {
    background-color: rgb(212, 64, 39);
}
QPushButton#buttonView {
    color: rgb(255, 255, 255);
    border-radius: 5px;
    border: solid 1px rgb(76, 169, 106);
    background-color: rgb(76, 169, 106);
}
QPushButton#buttonView:hover {
    color: rgb(0, 0, 0);
}
"""
# print('__name__ adlh:', __name__)
if __name__ in ['__main__', 'noticontrol']: # jk sama dg nama file = standalone
    from clock import ClockWidget
    from notiembed import WindowEmbedder
else:
    from .clock import ClockWidget
    from .notiembed import WindowEmbedder


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
    QApplication.instance().aboutQt()

class NotifyControl(object):

    def init_menu(self, NotifyContainer):
        # transparent background
        # NotifyContainer.context_menu.setAttribute(Qt.WA_TranslucentBackground)
        # No border, remove built-in shadow
        NotifyContainer.context_menu.setWindowFlags(NotifyContainer.context_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        # Simulate menu items
        about = NotifyContainer.context_menu.addAction(get_icon(), 'About Qt', about_qt)
        # quarter = NotifyContainer.context_menu.addAction(get_icon(), '1/4 screen', lambda: self.resize_screen_ratio(1/4))
        # half = NotifyContainer.context_menu.addAction(get_icon(), '1/2 screen', lambda: self.resize_screen_ratio(1/2))        
        # threequarter = NotifyContainer.context_menu.addAction(get_icon(), '3/4 screen', lambda: self.resize_screen_ratio(3/4))
        # defaultsize = NotifyContainer.context_menu.addAction(get_icon(), 'default size', lambda: self.resize_screen_ratio(1/6))

        # NotifyContainer.context_menu.addAction(get_icon(), 'bottom left', lambda: self.to_bottomleft())
        # NotifyContainer.context_menu.addAction(get_icon(), 'bottom right', lambda: self.to_bottomright())

        NotifyContainer.context_menu.addSeparator()
        NotifyContainer.context_menu.addAction(get_icon(), 'cmd git status', lambda: self.widget_cmd.send_message('git status'))
        NotifyContainer.context_menu.addAction(get_icon(), 'cmd pwd', lambda: self.widget_cmd.send_message('pwd'))

        NotifyContainer.context_menu.addSeparator()
        NotifyContainer.context_menu.addAction(get_icon(), 'wsl git status')

        NotifyContainer.context_menu.addSeparator()
        NotifyContainer.context_menu.addAction(get_icon(), 'listener git status')
        # activate tab
        # menu = QMenu('Activate tab', NotifyContainer.context_menu)
        # menu.setAttribute(Qt.WA_TranslucentBackground)
        # menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        # menu.addAction(get_icon(), 'clock', lambda: self.main_control.setCurrentIndex(0))
        # menu.addAction(get_icon(), 'form', lambda: self.main_control.setCurrentIndex(1))
        # menu.addAction(get_icon(), 'code', lambda: self.main_control.setCurrentIndex(2))
        # menu.addAction(get_icon(), 'repl', lambda: self.main_control.setCurrentIndex(3))
        # menu.addAction(get_icon(), 'mmm', lambda: self.main_control.setCurrentIndex(4))
        # NotifyContainer.context_menu.addMenu(menu)
        # No border, remove built-in shadow
        # NotifyContainer.context_menu.addAction(get_icon(), 'Tray', self.systemtrayicon)
        NotifyContainer.context_menu.addSeparator()
        NotifyContainer.context_menu.addAction(get_icon(), 'Reset size', lambda: NotifyContainer.onReset())
        NotifyContainer.context_menu.addAction(get_icon(), 'Quit', lambda: qApp.quit())

    def setupTrayAndContext(self, NotifyContainer):
        # NotifyContainer.tray_icon = QSystemTrayIcon(NotifyContainer)
        # NotifyContainer.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        # show_action = QAction("Show", NotifyContainer)
        # quit_action = QAction("Exit", NotifyContainer)
        # hide_action = QAction("Hide", NotifyContainer)
        # show_action.triggered.connect(NotifyContainer.show)
        # hide_action.triggered.connect(NotifyContainer.hide)
        # quit_action.triggered.connect(QApplication.instance().quit)
        # tray_menu = QMenu()
        # tray_menu.addAction(show_action)
        # tray_menu.addAction(hide_action)
        # tray_menu.addAction(quit_action)
        # NotifyContainer.tray_icon.setContextMenu(tray_menu)
        # NotifyContainer.tray_icon.show()
        NotifyContainer.context_menu = QMenu(NotifyContainer)

        self.init_menu(NotifyContainer)

    def setupUi(self, NotifyContainer):

        NotifyContainer.setObjectName('NotifyContainer')
        NotifyContainer.setWindowTitle('Notification')
        # NotifyContainer.setWindowOpacity(0.8)

        # screen_geometry = QDesktopWidget().screenGeometry(-1)
        # sw, sh = screen_geometry.width(), screen_geometry.height()
        # NotifyContainer.resize(sw//6, sh*1//3)        
        NotifyContainer.setStyleSheet(mystylesheet)

        self.setupTrayAndContext(NotifyContainer)

        self.verticalLayout = QVBoxLayout(NotifyContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        # window title widget
        self.widgetTitle = QWidget(NotifyContainer)
        self.widgetTitle.setMinimumSize(QSize(0, 26))
        self.widgetTitle.setObjectName("widgetTitle")

        # window title layout for window title widget
        self.layout_window_title = QHBoxLayout(self.widgetTitle)
        self.layout_window_title.setContentsMargins(10, 0, 0, 0)
        self.layout_window_title.setSpacing(0)
        self.layout_window_title.setObjectName("layout_window_title")

        # window title label/text
        self.labelTitle = QtWidgets.QLabel(self.widgetTitle)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")

        # spacer
        self.layout_window_title.addWidget(self.labelTitle)
        spacerItem = QtWidgets.QSpacerItem(40, 20, 
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.layout_window_title.addItem(spacerItem)

        # reset button
        self.buttonState = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonState.setMinimumSize(QtCore.QSize(26, 26))
        self.buttonState.setMaximumSize(QtCore.QSize(26, 26))
        self.buttonState.setObjectName("buttonState")
        self.buttonState.setCheckable(True)
        self.buttonState.setText('*')

        self.buttonReset = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonReset.setMinimumSize(QtCore.QSize(50, 26))
        self.buttonReset.setMaximumSize(QtCore.QSize(50, 26))
        self.buttonReset.setObjectName("buttonReset")
        self.buttonReset.setText('[({})]')

        # close button
        self.buttonClose = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonClose.setMinimumSize(QtCore.QSize(26, 26))
        self.buttonClose.setMaximumSize(QtCore.QSize(26, 26))
        self.buttonClose.setObjectName("buttonClose")
        self.buttonClose.setText('r')

        self.layout_window_title.addWidget(self.buttonState)
        self.layout_window_title.addWidget(self.buttonReset)
        self.layout_window_title.addWidget(self.buttonClose)

        self.verticalLayout.addWidget(self.widgetTitle)

        self.setCenterContent(NotifyContainer)

        self.widgetBottom = QtWidgets.QWidget(NotifyContainer)
        self.widgetBottom.setObjectName("widgetBottom")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem1)

        self.buttonView = QtWidgets.QPushButton(self.widgetBottom)
        self.buttonView.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonView.setObjectName("buttonView")
        self.buttonView.setText('Go')
        self.horizontalLayout.addWidget(self.buttonView)

        self.verticalLayout.addWidget(self.widgetBottom)
        self.verticalLayout.setStretch(1, 1)

        QtCore.QMetaObject.connectSlotsByName(NotifyContainer)

    def setCenterContent(self, NotifyContainer):
        # print('setContent, parent:', NotifyContainer)
        QToolTip.setFont(QFont('SansSerif', 10))

        # self.content = QTableWidget(NotifyContainer)

        # self.content.setColumnCount(2)
        # # entah kenapa ini gak jalan? jadi hrs set jumlah kolom = 2 dulu spt di atas...
        # column_labels = ['Title', 'URL']

        # for i in range(1,3):
        #     item = QTableWidgetItem()
        #     self.content.setHorizontalHeaderItem(i, item)

        # self.content.setHorizontalHeaderLabels(column_labels)
        # # self.content.horizontalHeader().setVisible(False)
        # # self.content.horizontalHeader().setVisible(True) # default visible

        # # self.questionWidget.tableView.verticalHeader().setVisible(False)
        # # self.questionWidget.tableView.horizontalHeader().setMinimumSectionSize(200)

        # # header = self.content.horizontalHeader()
        # # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        # self.verticalLayout.addWidget(self.content)

        self.main_layout = QVBoxLayout()
        self.main_control = QTabWidget(self, tabPosition=QTabWidget.East)
        self.main_layout.addWidget(self.main_control)

        clock = ClockWidget()

        # mode development
        # self.widget_cmd = QWidget()
        self.widget_wsl = QWidget()
        self.widget_listener = QWidget()

        # mode production
        self.widget_cmd = WindowEmbedder(perintah=['pwd', 'sido', 'gs'])
        # self.widget_wsl = WindowEmbedder(perintah=['wsl', 'pwd', 'sido', 'gs'])
        # self.widget_listener = WindowEmbedder(perintah=['wsl', 'pwd', 'sido', 'W'])

        self.main_control.addTab(clock, '0')
        self.main_control.addTab(self.widget_cmd, '1')
        self.main_control.addTab(self.widget_wsl, '2')
        self.main_control.addTab(self.widget_listener, '3')

        # self.verticalLayout.addWidget(clock)
        self.verticalLayout.addLayout(self.main_layout)

        # self.content.setRowCount(len(NotifyContainer.data))

        # # stretch all cols to content
        # # self.content.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # # stretch hanya first col
        # self.content.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # # https://stackoverflow.com/questions/38098763/pyside-pyqt-how-to-make-set-qtablewidget-column-width-as-proportion-of-the-a

        # for i, row in enumerate(NotifyContainer.data):
        #     isi = f"[<font color='red'>{row['answers']}</font>][{row['tags']}] {row['title']}"
        #     isi = f"[{row['answers']}] {row['title']}"
        #     current_item = QTableWidgetItem(isi)
        #     tooltip = f"[<i>{row['tags']}</i>] <b>{row['summary']}</b>"
        #     current_item.setToolTip(tooltip)
        #     self.content.setItem(i, 0, current_item)
        #     # self.content.setItem(i, 0, QTableWidgetItem('palsu'))
        #     link_item = QTableWidgetItem(row['url'])
        #     tooltip2 = f"""<a href="{row['url']}"><u>{row['url']}</u></a>"""
        #     link_item.setToolTip(tooltip2)
        #     self.content.setItem(i, 1, link_item)
