
import sys
import webbrowser
from PyQt5.QtGui import (
    QFont,
)
from PyQt5.QtCore import (
    Qt,
    pyqtSignal,
    
    QEasingCurve,
    QPoint,
    QPropertyAnimation,
    QTimer,    
)
from PyQt5.QtWidgets import (    
    QApplication,    
    QDesktopWidget,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QToolTip,
    QWidget,
)
from PyQt5 import QtCore, QtGui, QtWidgets


mystylesheet = """
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


class NotifyControl(object):

    def setupUi(self, NotifyContainer):

        NotifyContainer.setObjectName('NotifyContainer')
        NotifyContainer.setWindowTitle('Notification')

        screen_geometry = QDesktopWidget().screenGeometry(-1)
        sw, sh = screen_geometry.width(), screen_geometry.height()

        NotifyContainer.resize(sw//6, sh*1//3)
        NotifyContainer.setStyleSheet(mystylesheet)

        self.verticalLayout = QtWidgets.QVBoxLayout(NotifyContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widgetTitle = QtWidgets.QWidget(NotifyContainer)
        self.widgetTitle.setMinimumSize(QtCore.QSize(0, 26))
        self.widgetTitle.setObjectName("widgetTitle")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetTitle)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.labelTitle = QtWidgets.QLabel(self.widgetTitle)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")

        self.horizontalLayout_3.addWidget(self.labelTitle)
        spacerItem = QtWidgets.QSpacerItem(40, 20, 
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)

        self.buttonClose = QtWidgets.QPushButton(self.widgetTitle)
        self.buttonClose.setMinimumSize(QtCore.QSize(26, 26))
        self.buttonClose.setMaximumSize(QtCore.QSize(26, 26))
        self.buttonClose.setObjectName("buttonClose")
        self.buttonClose.setText('x')
        self.horizontalLayout_3.addWidget(self.buttonClose)
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

        self.content = QTableWidget(NotifyContainer)
        self.content.setColumnCount(2)
        # entah kenapa ini gak jalan? jadi hrs set jumlah kolom = 2 dulu spt di atas...
        column_labels = ['Title', 'URL']

        for i in range(1,3):
            item = QTableWidgetItem()
            self.content.setHorizontalHeaderItem(i, item)

        self.content.setHorizontalHeaderLabels(column_labels)
        # self.content.horizontalHeader().setVisible(False)
        # self.content.horizontalHeader().setVisible(True) # default visible

        # self.questionWidget.tableView.verticalHeader().setVisible(False)
        # self.questionWidget.tableView.horizontalHeader().setMinimumSectionSize(200)

        # header = self.content.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        self.verticalLayout.addWidget(self.content)

        self.content.setRowCount(len(NotifyContainer.data))

        # stretch all cols to content
        # self.content.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # stretch hanya first col
        self.content.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # https://stackoverflow.com/questions/38098763/pyside-pyqt-how-to-make-set-qtablewidget-column-width-as-proportion-of-the-a

        for i, row in enumerate(NotifyContainer.data):
            isi = f"[<font color='red'>{row['answers']}</font>][{row['tags']}] {row['title']}"
            isi = f"[{row['answers']}] {row['title']}"
            current_item = QTableWidgetItem(isi)
            tooltip = f"[<i>{row['tags']}</i>] <b>{row['summary']}</b>"
            current_item.setToolTip(tooltip)
            self.content.setItem(i, 0, current_item)
            # self.content.setItem(i, 0, QTableWidgetItem('palsu'))
            link_item = QTableWidgetItem(row['url'])
            tooltip2 = f"""<a href="{row['url']}"><u>{row['url']}</u></a>"""
            link_item.setToolTip(tooltip2)
            self.content.setItem(i, 1, link_item)
