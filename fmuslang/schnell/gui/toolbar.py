
# https://stackoverflow.com/questions/51829622/group-buttons-aesthetically-in-pyqt5

import os, random, string, sys
from PyQt5 import QtCore, QtGui, QtWidgets

disini = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
sidoarjodir = os.path.normpath(os.path.join(disini, '../..'))

def get_icon():
    pixmap = QtGui.QPixmap(16, 16)
    pixmap.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter()
    painter.begin(pixmap)
    painter.setFont(QtGui.QFont('Webdings', 11))
    painter.setPen(QtCore.Qt.GlobalColor(random.randint(4, 18)))
    painter.drawText(0, 0, 16, 16, QtCore.Qt.AlignCenter, random.choice(string.ascii_letters))
    painter.end()
    return QtGui.QIcon(pixmap)


def keluar():
    QtWidgets.qApp.quit()

button_handlers = {
    'exit': keluar,
    'edit_helper': lambda: os.system(f'code {os.path.join(disini, "helper.py")}'),
    'edit_toolbar': lambda: os.system(f'code {__file__}'),
    'edit_blitz': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/quick/blitz/__init__.py")}'),
    'edit_dahsyater': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/quick/dahsyater.py")}'),
    'edit_fullstack': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fullstack.py")}'),
    'edit_django_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fslang/django/__init__.py")}'),
    'edit_fastapi_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fslang/fastapi/__init__.py")}'),
    'edit_flask_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fslang/flask/__init__.py")}'),
    'edit_nest_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fslang/nest/__init__.py")}'),
    'edit_nodeantd_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fslang/node_antd/__init__.py")}'),
    'edit_springboot_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/transpiler/frontend/fslang/springboot/__init__.py")}'),
    'edit_fullstack_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "coords/fullstack/__init__.py")}'),
    'edit_base_coordinator': lambda: os.system(f'code {os.path.join(sidoarjodir, "schnell/app/coordinator.py")}'),
}

toolbar_data = [
    {
        "title": " App",
        "buttons": [
            {
                "text": "Edit current file",
                "path_icon": "SP_DialogHelpButton",
                "handler": "edit_active_file"
            },
            {
                "text": "Info current file",
                "path_icon": "SP_DialogNoButton",
                "handler": "info_active_file"
            },
        ]
    },
    {
        "title": "Edit files",
        "buttons": [
            {
                "text": "Edit blitz",
                "handler": "edit_blitz",
                "path_icon": ""
            },
            {
                "text": "Edit dahsyater",
                "handler": "edit_dahsyater",
                "path_icon": ""
            },
            {
                "text": "Edit fullstack",
                "handler": "edit_fullstack",
                "path_icon": ""
            },
        ]
    },
    {
        "title": "Edit coordinators",
        "buttons": [
            {
                "text": "Edit django",
                "handler": "edit_django_coordinator",
                "path_icon": ""
            },
            {
                "text": "Edit fastapi",
                "handler": "edit_fastapi_coordinator",
                "path_icon": ""
            },
            {
                "text": "Edit flask",
                "handler": "edit_flask_coordinator",
                "path_icon": ""
            },
            {
                "text": "Edit nest",
                "handler": "edit_nest_coordinator",
                "path_icon": ""
            },
            {
                "text": "Edit node/antd",
                "handler": "edit_nodeantd_coordinator",
                "path_icon": ""
            },
            {
                "text": "Edit springboot",
                "handler": "edit_springboot_coordinator",
                "path_icon": ""
            },
        ]
    },
    {
        "title": "Edit new coordinators",
        "buttons": [
            {
                "text": "Edit new FS coord",
                "handler": "edit_fullstack_coordinator",
                "path_icon": ""
            },
            {
                "text": "Edit base coord",
                "handler": "edit_base_coordinator",
                "path_icon": ""
            },
        ]
    },
    {
        "title": "Edit programs",
        "buttons": [
            {
                "text": "Edit helper",
                "handler": "edit_helper",
                "path_icon": "SP_TitleBarMaxButton"
            },
            {
                "text": "Edit toolbar",
                "handler": "edit_toolbar",
                "path_icon": "SP_FileLinkIcon"
            },
        ]
    },
    {
        "title": " System",
        "buttons": [
            {
                "text": "(Exit)",
                "path_icon": "SP_MessageBoxCritical",
                "handler": "exit"
            }
        ]
    },
]


class ToolButton(QtWidgets.QWidget):

    def __init__(self, text, path_icon, handler=None, parent=None):
        super(ToolButton, self).__init__(parent)

        lay = QtWidgets.QVBoxLayout(self)
        # path_icon = path_icon if path_icon else get_icon()

        self.toolButton = QtWidgets.QToolButton()
        the_icon = QtGui.QIcon(path_icon) if path_icon else get_icon()
        self.toolButton.setIcon(the_icon)
        if handler:
            self.toolButton.clicked.connect(handler)

        if path_icon:
            iconobj = getattr(QtWidgets.QStyle, path_icon)
            icon = QtWidgets.QApplication.style().standardIcon(iconobj)
        else:
            icon = get_icon()
        self.toolButton.setIcon(icon)

        # toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setIconSize(QtCore.QSize(16,16))
        label = QtWidgets.QLabel(text)
        lay.addWidget(self.toolButton, 0, QtCore.Qt.AlignCenter)
        lay.addWidget(label, 0, QtCore.Qt.AlignCenter)
        lay.setContentsMargins(0, 0, 0, 0)
    
    def set_handler(self, handler):
        self.toolButton.clicked.connect(handler)


class GroupButton(QtWidgets.QGroupBox):
    def __init__(self, info, parent=None):
        super(GroupButton, self).__init__(parent)
        title = info["title"]
        self.setTitle(title)
        # self.setStyleSheet('color: yellow; margin-top: 0; padding-bottom: 0; margin-bottom: 20px;')
        self.setStyleSheet('color: darkblue;')
        hlay = QtWidgets.QHBoxLayout(self)
        for info_button in info["buttons"]:
            text = info_button["text"]
            path_icon = info_button["path_icon"]
            btn = ToolButton(text, path_icon)
            if 'handler' in info_button:
                btn.set_handler(button_handlers[info_button['handler']])
            hlay.addWidget(btn)
        hlay.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(self.sizeHint())

class ToolbarWidgetOld(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ToolbarWidgetOld, self).__init__(parent)
        vlay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        for val in toolbar_data:
            gb = GroupButton(val)
            hlay.addWidget(gb)
        hlay.addStretch()
        vlay.addLayout(hlay)
        vlay.addStretch()


class ToolbarWidget(QtWidgets.QWidget):

    def info_active_file(self):
        curindex = self.tab_widget.main_control.currentIndex()
        curentry = self.files_dirs_list[curindex]
        fileentry = curentry['filepath']
        level = curentry['level']
        if level==1:
            # utk folder, curentry akan punya children...
            # index children ditentukan oleh curindex dari anak
            # fileentry dari dalam...
            # self.tab_widget punya self.tab_widget.folders yg di-key dg {widget, index} dan index setara dg curindex
            tabanak = [item['widget'] for item in self.tab_widget.folders if item['index']==curindex]
            # tabanak = self.tab_widget.folders
            if tabanak:
                tabanak = tabanak[0]
                tabanakwidget_index = tabanak.main_control.currentIndex()
                fileentry = curentry['children'][tabanakwidget_index]['filepath']

        print(f"""info_active_file
        current active: {curindex}
        entry utk current index: {curentry}
        level: {level}
        file entry: {fileentry}
        """)

    def edit_active_file(self):
        curindex = self.tab_widget.main_control.currentIndex()
        curentry = self.files_dirs_list[curindex]
        fileentry = curentry['filepath']
        level = curentry['level']
        if level==1:
            # utk folder, curentry akan punya children...
            # index children ditentukan oleh curindex dari anak
            tabanak = [item['widget'] for item in self.tab_widget.folders if item['index']==curindex]
            if tabanak:
                tabanak = tabanak[0]
                tabanakwidget_index = tabanak.main_control.currentIndex()
                fileentry = curentry['children'][tabanakwidget_index]['filepath']

        os.system(f'code {fileentry}')

    def __init__(self, parent=None, tab_widget=None, files_dirs_list=[]):
        super(ToolbarWidget, self).__init__(parent)

        self.tab_widget = tab_widget
        self.files_dirs_list = files_dirs_list
        # pastikan kita isi dulu, krn GroupButton akan gunakan
        # if tab_widget and files_dirs_list:
        button_handlers['edit_active_file'] = self.edit_active_file
        button_handlers['info_active_file'] = self.info_active_file

        hlay = QtWidgets.QHBoxLayout()
        for val in toolbar_data:
            groupButton = GroupButton(val)
            hlay.addWidget(groupButton)
        hlay.addStretch(1)
        self.setLayout(hlay)
        self.setMaximumHeight(80)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = ToolbarWidget()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
