from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

class FileIconProvider(QFileIconProvider):
    """Icon provider class"""

    def __init__(self, *args, **kwargs):
        super(FileIconProvider, self).__init__(*args, **kwargs)
        # self.DirIcon = QIcon(f"{imagedir}/folder.png")
        self.DirIcon = QApplication.style().standardIcon(QStyle.SP_DirIcon)
        # self.TxtIcon = QIcon(f"{imagedir}/file.png")
        self.TxtIcon = QApplication.style().standardIcon(QStyle.SP_FileDialogDetailedView)

    def icon(self, type_info):
        '''
        :param fileInfo: 参考http://doc.qt.io/qt-5/qfileinfo.html

        QFileIconProvider::Computer     0
        QFileIconProvider::Desktop      1
        QFileIconProvider::Trashcan     2
        QFileIconProvider::Network      3
        QFileIconProvider::Drive        4
        QFileIconProvider::Folder       5
        QFileIconProvider::File         6
        '''
        if isinstance(type_info, QFileInfo):
            # 如果type_info是QFileInfo类型则用getInfoIcon来返回图标
            return self.getInfoIcon(type_info)
        # 如果type_info是QFileIconProvider自身的IconType枚举类型则执行下面的方法
        # 这里只能自定义通用的几种类型，参考http://doc.qt.io/qt-5/qfileiconprovider.html#IconType-enum

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

    #@pyqtSlot(QModelIndex)
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

        # https://stackoverflow.com/questions/58881818/how-to-get-selected-item-in-qfilesystemmodel-and-qtreeview
        # source_index = self.filesystem_tree.proxy_model.mapToSource(index)
        # indexItem = self.filesystem_tree.model.index(source_index.row(), 0, source_index.parent())
        indexItem = index
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        normPath = os.path.normpath(filePath)
        print(index, fileName, filePath, normPath)

        # reload gallery
        if os.path.isdir(normPath):
            print(normPath)
            os.chdir(normPath)
            self.model.setRootPath(normPath)
            self.setModel(self.model)
            the_index = self.model.index(normPath)
            self.setRootIndex(the_index)
            self.setWindowTitle(normPath)

    def __init__(self, curdir=os.getcwd(), *args, **kwargs):
        super(FileTree, self).__init__(*args, **kwargs)

        # https://stackoverflow.com/questions/58881818/how-to-get-selected-item-in-qfilesystemmodel-and-qtreeview
        self.model = QFileSystemModel()
        self.model.setIconProvider(FileIconProvider())  # 设置为自定义的图标提供类
        print(f"[FileTree] curdir = {curdir}")
        # curdir = QDir.currentPath()
        self.model.setRootPath(curdir)

        self.model.setFilter(QDir.AllEntries | QDir.Dirs | QDir.Files)
        # self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries | QDir.Dirs | QDir.Files)
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
        self.setWindowTitle(os.path.normpath(curdir))
        self.clicked.connect(self.pilih_folder)
