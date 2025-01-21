
import os
import shutil
import functools

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FileTreeWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        root_folder = 'C:\\'
        self.main_layout = QGridLayout()
        self.collapse_button = QPushButton('Collapse all', self)
        self.goto_lineedit = QLineEdit(root_folder, self)
        self.goto_lineedit.setStyleSheet('background-color: khaki; font-size: 16px; font-family: Consolas; padding: 5px;')
        self.history = []
        self.completer = QCompleter(self.history)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.goto_lineedit.setCompleter(self.completer)
        self.goto_lineedit.returnPressed.connect(self.tekan_enter)
        self.goto_button = QPushButton('Go', self)
        self.folder_view = QTreeView(self)
        self.folder_model = QFileSystemModel(self)

        self.main_layout.addWidget(self.collapse_button, 0, 0)
        # self.main_layout.addWidget(self.goto_lineedit, 0, 1, 1, 2)
        self.main_layout.addWidget(self.goto_lineedit, 0, 1)
        self.main_layout.addWidget(self.goto_button, 0, 2)
        self.main_layout.addWidget(self.folder_view, 1, 0, 3, 3)
        self.goto_button.setMaximumWidth(70)

        self.folder_model.setRootPath(None)
        # self.folder_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.folder_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.Files)
        self.folder_view.setModel(self.folder_model)
        # self.folder_view.setRootIndex(self.folder_model.index(None))
        self.folder_model.setRootPath(root_folder)
        for row in range(self.folder_model.rowCount()):
            index = self.folder_model.index(row, 0)
            self.folder_view.expand(index)
        self.folder_view.clicked[QModelIndex].connect(self.clicked_onfolder)
        # self.folder_view.hideColumn(1)
        # self.folder_view.hideColumn(2)
        # self.folder_view.hideColumn(3)
        # self.folder_view.setColumnWidth(0, 200)
        # perbandingan: 3:1:1:1

        self.folder_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.folder_view.customContextMenuRequested.connect(functools.partial(self.folder_view_context_menu))
        self.folder_view.doubleClicked.connect(self.klik_ganda)

        self.goto_button.clicked.connect(functools.partial(self.go_to))
        self.collapse_button.clicked.connect(functools.partial(self.collapse_tree))


        self.setLayout(self.main_layout)
        self.setWindowTitle('nice window')
        QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        
        self.resize(800, 600)

        # total_width = self.folder_view.width()
        total_width = self.width()
        width_portion = (3,1,1,1)
        total_portion = sum(width_portion)
        # print(f"""
        # total_width = {total_width}
        # width_portion = {width_portion}
        # total_portion = {total_portion}
        # """)
        for i in range(4):
            portion = total_width*width_portion[i]//total_portion
            # print(f"{i} = {portion}")
            self.folder_view.setColumnWidth(i, portion)
        # self.expand_top_node()
        # self.folder_model.directoryLoaded.connect(self.expand_top_node)
        # self.expand_top_node(self.folder_model.index(None))
        self.show()

    # def expand_top_node(self, index):
    #     """
    #     https://stackoverflow.com/questions/47596847/how-to-expand-top-level-qtreeview-items
    #     https://stackoverflow.com/questions/24920360/fully-expand-a-qtreeview-representing-a-qfilesystemmodel
    #     """
    #     # index = self.folder_model.index(path)
    #     # print('path root', self.folder_model.filePath(index.child(0,0)))
    #     print('path root', self.folder_model.rootPath())
    #     print('path QDir', self.folder_model.rootDirectory())
    #     self.folder_view.expand(index)  # expand the item
    #     for i in range(self.folder_model.rowCount(index)):
    #     #     # fetch all the sub-folders
    #         child = index.child(i, 0)
    #         self.folder_view.expand(child)
    #     #     if self.folder_model.isDir(child):
    #     #         self.folder_model.setRootPath(self.folder_model.filePath(child))


    def set_input_completer(self):
        model = self.completer.model()
        model.setStringList(self.history)

    def klik_ganda(self, index):
        if self.folder_model.isDir(index):
            filePath = self.folder_model.filePath(index)
            if filePath not in self.history:
                self.history.append(filePath)
                self.set_input_completer()

    def tekan_enter(self):
        filePath = self.goto_lineedit.text().strip()
        if filePath and os.path.isdir(filePath):
            tulisan_index = self.folder_model.index(filePath)
            self.folder_view.expand(tulisan_index)
            if filePath not in self.history:
                self.history.append(filePath)
                self.set_input_completer()

    def create_newdir(self, parentdir):
        name, done = QInputDialog.getText(None, 'Masukkan nama direktori', 'Silahkan masukkan nama direktori untuk dibuat:')
        if done and name.strip():
            if os.path.isfile(parentdir):
                parentdir = os.path.dirname(parentdir)
            filepath = os.path.join(parentdir, name.strip())
            os.mkdir(filepath)

    def create_edit_file(self, parentdir):
        name, done = QInputDialog.getText(None, 'Masukkan nama file', 'Masukkan nama file beserta ekstensi:')
        print(f"""[create_edit_file]
        name = {name}
        name.strip() = {name.strip()}
        """)
        if done and name.strip():
            if os.path.isfile(parentdir):
                parentdir = os.path.dirname(parentdir)
            filepath = os.path.join(parentdir, name.strip())
            os.system(f'code "{filepath}"')

    def rename_file(self, filePath):
        dirPath = os.path.dirname(filePath)
        index = self.folder_view.selectedIndexes()
        if not index:
            return
        else:
            index = index[0]
        model = index.model()
        current_filename = model.data(index)
        # print(f"""[rename_file]
        # index = {index} = <PyQt5.QtCore.QModelIndex object at 0x000001AD362CB7D0>
        # model = {model} = <PyQt5.QtWidgets.QFileSystemModel object at 0x000001AD362CEE60>
        # filePath = {filePath}        
        # data_pada_index = {data_pada_index} = filename
        # """)
        # self.folder_view.edit(index)
        input_filename, ok = QInputDialog.getText(self, "New Name", "Enter a name", QLineEdit.Normal, current_filename)
        input_filename = input_filename.strip()
        if not ok or not input_filename:
            return
        new_filename = os.path.join(dirPath, input_filename)
        os.rename(filePath, new_filename)

    def delete_file(self, filePath):
        indexes = self.folder_view.selectedIndexes()
        for i in indexes:
            self.folder_model.remove(i)

    def move_file(self, parentdir):
        if os.path.isfile(parentdir):
            parentdir = os.path.dirname(parentdir)
        print("MOVE")
        ask = QFileDialog.getExistingDirectory(self, "Open Directory to move file", parentdir,
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        if ask == '':
            return
        new_path = ask.replace('\\', '/')
        indexes = self.folder_view.selectedIndexes()[::4]
        for i in indexes:
            new_filename = new_path + '/' + self.folder_model.fileName(i)
            shutil.move(self.folder_model.filePath(i), new_filename)

    def copy_file(self, parentdir):
        if os.path.isfile(parentdir):
            parentdir = os.path.dirname(parentdir)
        print("COPY")
        ask = QFileDialog.getExistingDirectory(self, "Open Directory to copy file", parentdir,
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        new_path = ask.replace('\\', '/')
        indexes = self.folder_view.selectedIndexes()[::4]
        for i in indexes:
            new_filename = new_path + '/' + self.folder_model.fileName(i)
            shutil.copy2(self.folder_model.filePath(i), new_filename)

    def rename_folder(self, filePath):
        # index = self.folder_view.selectedIndexes()
        # if not index:
        #     return
        # else:
        #     index = index[0]
        # self.folder_view.edit(index)
        dirPath = os.path.dirname(filePath)
        index = self.folder_view.selectedIndexes()
        if not index:
            return
        else:
            index = index[0]
        model = index.model()
        current_filename = model.data(index)
        # print(f"""[rename_file]
        # index = {index} = <PyQt5.QtCore.QModelIndex object at 0x000001AD362CB7D0>
        # model = {model} = <PyQt5.QtWidgets.QFileSystemModel object at 0x000001AD362CEE60>
        # filePath = {filePath}        
        # data_pada_index = {data_pada_index} = filename
        # """)
        # self.folder_view.edit(index)
        input_filename, ok = QInputDialog.getText(self, "New Name", "Enter a name", QLineEdit.Normal, current_filename)
        input_filename = input_filename.strip()
        if not ok or not input_filename:
            return
        new_filename = os.path.join(dirPath, input_filename)
        os.rename(filePath, new_filename)

    def delete_folder(self, filePath):
        indexes = self.folder_view.selectedIndexes()
        for i in indexes:
            self.folder_model.remove(i)

    def folder_view_context_menu(self, point):
        index = self.folder_view.indexAt(point)
        menu = QMenu()
        # fileName = self.folder_model.fileName(index)
        filePath = self.folder_model.filePath(index)
        # menu.addAction(fileName)
        menu.addAction(filePath)
        menu.addSeparator()
        menu.addAction('New Folder', lambda: self.create_newdir(filePath))
        menu.addAction('New File', lambda: self.create_edit_file(filePath))
        if os.path.isfile(filePath):
            menu.addAction('Rename File', lambda: self.rename_file(filePath))
            menu.addAction('Delete File', lambda: self.delete_file(filePath))
            menu.addAction('Move File', lambda: self.move_file(filePath))
            menu.addAction('Copy File', lambda: self.copy_file(filePath))
        elif os.path.isdir(filePath):
            menu.addAction('Rename folder', lambda: self.rename_folder(filePath))
            menu.addAction('Delete folder', lambda: self.delete_folder(filePath))
        menu.exec_(self.folder_view.mapToGlobal(point))

    def clicked_onfolder(self, index):
        selection_model = self.folder_view.selectionModel()
        index = selection_model.currentIndex()
        dir_path = self.folder_model.filePath(index)
        # self.folder_model.setRootPath(dir_path)
        # self.folder_view.setRootIndex(self.folder_model.index(dir_path))

    def go_to(self):
        dir_path = self.goto_lineedit.text().replace('\\', '/')
        print(dir_path)
        # harusnya di sini adlh...selection...
        # self.folder_model.setRootPath(dir_path)
        # self.folder_view.setRootIndex(self.folder_model.index(dir_path))
        # self.folder_model.setRootPath()

    def collapse_tree(self):
        self.folder_view.collapseAll()

