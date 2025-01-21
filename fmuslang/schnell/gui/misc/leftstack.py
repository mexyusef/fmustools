
from random import randint

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QStackedWidget, QHBoxLayout, QListWidgetItem, QLabel
# Beautify the style sheet
Stylesheet = """
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}
/*被选中时的背景颜色和左边框颜色*/
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
/*鼠标悬停颜色*/
HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

/*右侧的层叠窗口的背景颜色*/
QStackedWidget {
    background: rgb(30, 30, 30);
}
/*模拟的页面*/
QLabel {
    color: white;
}
"""

class LeftTabWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setStyleSheet(Stylesheet)
        # 左右布局(左边一个QListWidget + 右边QStackedWidget)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # left list
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # Right Cascading Window
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)
        self.initUi()

    def initUi(self):
        # Initialize the interface
        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        # remove border
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # hide scrollbar
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # kita tambah listwidgetitem dg icon ke listWidget
        # Here we use the general text with the icon mode.(也可以直接用Icon模式,setViewMode)
        for i in range(20):
            item = QListWidgetItem(QIcon(f'icons/0%d.ico' % randint(1, 8)), str('Options %s' % i), self.listWidget)
            # 设置item的默认宽高(这里只有高度比较有用)
            item.setSizeHint(QSize(16777215, 60))
            # center text
            item.setTextAlignment(Qt.AlignCenter)

        # Simulate 20 more pages on the right(It won't be looped together with the above.)
        for i in range(20):
            label = QLabel('i am page %d' % i, self)
            label.setAlignment(Qt.AlignCenter)
            # 设置label的背景颜色(这里随机)
            # 这里加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
            label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
                randint(0, 255), randint(0, 255), randint(0, 255)))
            self.stackedWidget.addWidget(label)

