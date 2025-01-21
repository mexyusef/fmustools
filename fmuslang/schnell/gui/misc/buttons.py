import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,    
    QTextEdit,
    QToolBox,
)
from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets as QW, QtGui as QG, QtCore as QC
import pyperclip as PC

class MyListItem(QWidget):
    def __init__(self, index, icon_name, icon_obj, item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._item = item
        self.nama = icon_name
        self.the_icon = QApplication.style().standardIcon(icon_obj)
        self.the_button = QPushButton(f"[{index}] {icon_name}", self)
        self.the_button.setIcon(self.the_icon)
        the_font = QG.QFont('Noto Sans', 14)
        self.the_button.setFont(the_font)
        self.the_button.setIconSize(QC.QSize(32,32))
        self.the_button.clicked.connect(self.tekan)
        layout = QW.QHBoxLayout(self)
        layout.addWidget(self.the_button)
    def tekan(self):
        PC.copy(self.nama)


class MyFontListItem(QWidget):
    def __init__(self, text, the_font, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._item = item
        self.editor = QW.QPlainTextEdit(self)
        self.editor.setPlainText(text)
        self.editor.setFont(the_font)
        layout = QW.QHBoxLayout(self)
        layout.addWidget(self.editor)

# add dari pyqt5/examples/layouts

class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


class MyWidget(QW.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.split = QW.QSplitter(self)

        all_icons = [i for i in dir(QW.QStyle) if i.startswith('SP_')]
        self.list = QW.QListWidget(self)
        self.list_fonts = QW.QListWidget(self)

        w,h = self.sizeHint().width(), 120

        # https://stackoverflow.com/questions/33885146/python-get-list-of-available-fonts-on-system
        self.families = QG.QFontDatabase().families()

        # icons list
        for index,icon in enumerate(all_icons):
            # icon adlh icon name, utk peroleh obj-nya, ambil dari QStyle
            # gagal, berhasil stlh set size
            icon_obj = getattr(QW.QStyle, icon)
            li = QW.QListWidgetItem(self.list)

            # ini wajib ternyata, klo gak, gak muncul widget item            
            li.setSizeHint(QC.QSize(w,h))

            the_item = MyListItem(index, icon, icon_obj, li, self.list)
            self.list.setItemWidget(li, the_item)

            # # berhasil
            # the_icon = self.the_icon = QApplication.style().standardIcon(getattr(QW.QStyle, icon))
            # li = QW.QListWidgetItem(the_icon, icon, self.list)

        # fonts
        self.tulisan = "wieke and gaia are 2 opposite personalities"
        for index,font_str in enumerate(self.families):
            li = QW.QListWidgetItem(self.list_fonts)
            li.setSizeHint(QC.QSize(w,h))
            the_font = QG.QFont(font_str, 16)
            the_item = MyFontListItem(f"[{index}. {font_str}] {self.tulisan}", the_font, self.list)
            self.list_fonts.setItemWidget(li, the_item)

        # utk di tengah, icons flow layout
        self.flow_layout = QWidget(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        # scrollarea gunakan widget yg akan dilayout dg flowLayout
        self.scrollArea.setWidget(self.flow_layout)
        flowLayout = FlowLayout(self.flow_layout)
        for index,icon_name in enumerate(all_icons):
            icon_obj = getattr(QW.QStyle, icon_name)
            the_icon = QApplication.style().standardIcon(icon_obj)
            the_button = QPushButton(f"[{index}] {icon_name}", self)
            the_button.setIcon(the_icon)
            # the_button.setToolTip(f"")
            flowLayout.addWidget(the_button)

        # self.setCentralWidget(self.list)
        self.split.addWidget(self.list)
        # self.split.addWidget(self.flow_layout)
        self.split.addWidget(self.scrollArea)
        self.split.addWidget(self.list_fonts)
        self.setCentralWidget(self.split)
        self.setMinimumHeight(800)
        self.setMinimumWidth(1000)

def main():
    app = QApplication(sys.argv)

    demo = MyWidget()
    demo.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
