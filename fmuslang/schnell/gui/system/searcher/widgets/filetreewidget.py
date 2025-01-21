# from fileinput import filename
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

import os, sys, functools, shutil, threading, pyperclip, time, subprocess
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# rootdir = os.environ['ULIBPY_ROOTDIR']
from pathlib import Path
current_file_path = Path(__file__).resolve()
rootdir = current_file_path.parent
sys.path.append(rootdir)
# sys.path.extend([rootdir, schnelldir])

from schnell.app.appconfig import programming_data
# from startup import programming_data
# from schnell.app.executor import FileExecutor
# from schnell.app.wcmderutils import (
#     getlist, button_ketik_handler, operate_on_windows, to_top,
#     create_fill_set, fill_set,
#     create_fill_set_with_id_index,
#     ketik_by_hwnd, ketik_by_index,
#     get_items_for_combo,
#     hapus_set_combo_items,
#     data_for_item,
#     is_window_visible,
#     operate_on_windows_by_hwnd,
#     to_top_by_hwnd,
#     get_last_console_data,
# )
from schnell.app.dirutils import normy, explore, joiner, files_filter, fmus_operate_on_listdir, bongkar
from schnell.app.fileutils import get_daftar, get_definition_by_key_permissive_start, file_content, not_binary, get_extension
from schnell.app.fmusutils import (
    run_fmus_for_file,
    run_fmus_for_content,
    run_fmus_for_file_in_folder_in_thread,
    run_us_in_folder_in_thread,
)
from schnell.app.systemutils import execute_command_in_dir, execute_command_in_dir_in_thread, execute_command, execute_in_thread
from schnell.app.threadutils import mulai
from schnell.app.utils import env_get
from schnell.app.vscodeutils import create_snippet_wrapper
from schnell.gui.system.searcher.widgets.common import get_icon # , BlueButton
from schnell.gui.system.searcher.widgets.dahsyatmenu import DashsyatMenu
from schnell.gui.system.searcher.widgets.common import (
    context_menu_stylesheet,
    resize_screen_ratio_wrapper,
    bahasa_filepaths,
    context_menu_for_dirs_with_entries,
    context_menu_for_files_with_entries,
    predefined_commands,
    yarn_add_packages_dev,
    yarn_add_packages,
    reload_kenza_us_files,
    kenza_us_files,
    kenza_us_dir,
)
# from schnell.gui.system.searcher.widgets.colorwidget import ColorWidget
# from schnell.gui.system.searcher.widgets.buttonwidget import ButtonWidget
from schnell.gui.system.searcher.widgets.tkeditor import tkeditor
# from schnell.gui.system.searcher.widgets.windower import WindowerWidget
# from schnell.gui.system.searcher.widgets.lalangwidget import LalangWidget
from schnell.gui.system.searcher.widgets.showedit import ShowEditWindow
from schnell.gui.system.searcher.widgets.packagewidget import PackageWidget
from schnell.gui.system.searcher.widgets.creator import CreatorWidget
# from schnell.gui.system.searcher.widgets.quickviewer import QuickViewerWidget
from schnell.gui.system.searcher.widgets.filemanip import filemanip
from schnell.gui.system.searcher.widgets.config import preset_directories
from schnell.gui.system.searcher.widgets.exec_commands import exec_code_sidoarjo, exec_notepad
from schnell.gui.system.searcher.widgets.common import create_menu_cmds, create_menu_editors
from schnell.gui.system.searcher.widgets.mkcommand import create_menu_mkcommand

from constants import (
    sidoarjodir,
    schnelldir,
    button_stylesheet1,
    button_stylesheet2,
)


kenzadir = normy(joiner(sidoarjodir, 'data/kenza'))
preset_directories += [
    normy(sidoarjodir),
    normy(joiner(sidoarjodir, 'coords')),
    kenzadir,
    normy(joiner(sidoarjodir, 'database/ageh')),
    normy(joiner(sidoarjodir, 'database/geura')),
    normy(joiner(sidoarjodir, 'database/refcards')),
    normy(joiner(schnelldir, 'app/quick/blitz/')),
    normy(joiner(schnelldir, 'app/transpiler/frontend/fslang/django/')),
]
# kenzadir = bongkar(programming_data['j']['directories']['kenza'])
# preset_directories += [bongkar(item) for item in programming_data['j']['directories']['presets']]

class FileTreeWidget(QWidget):

    request_cmd = pyqtSignal(str)
    request_wsl = pyqtSignal(str)
    request_docker_compose_up = pyqtSignal(str)
    set_rootpath = pyqtSignal(str)
    new_file_clicked = pyqtSignal(str)
    imagefile_clicked = pyqtSignal(str)
    pdffile_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        root_folder = programming_data['j']['directories']['root']  # 'C:\\'
        self.collapse_button = QPushButton('', self)
        self.collapse_button.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogHelpButton))
        self.preset_location = QPushButton('', self)
        self.preset_location.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogNewFolder))
        self.preset_menu = QMenu(self)

        for folder in preset_directories:
            self.preset_menu.addAction(
                QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
                folder,
                functools.partial(self.ganti_direktori, folder)
            )
        self.preset_location.setMenu(self.preset_menu)

        self.goto_lineedit = QLineEdit(root_folder, self)
        self.goto_lineedit.setStyleSheet('background-color: khaki; font-size: 16px; font-family: Arial, Consolas; min-width: 100px;')
        self.set_rootpath.connect(self.goto_lineedit.setText)
        self.history = []
        self.completer = QCompleter(self.history)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.goto_lineedit.setCompleter(self.completer)
        self.goto_lineedit.returnPressed.connect(self.tekan_enter)
        self.goto_button = QPushButton('', self)
        self.goto_button.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
        self.folder_view = QTreeView(self)
        self.folder_model = QFileSystemModel(self)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.collapse_button, 0, 0)
        self.main_layout.addWidget(self.preset_location, 0, 1)
        self.main_layout.addWidget(self.goto_lineedit, 0, 2)
        self.main_layout.addWidget(self.goto_button, 0, 3)

        self.button_sido = QPushButton("Sido")
        self.button_sido.setStyleSheet(button_stylesheet1)
        self.button_editors = QPushButton("Edit")
        self.button_editors.setMenu(create_menu_editors(self))
        self.button_editors.setStyleSheet(button_stylesheet1)
        self.button_mkhelp = QPushButton("MK")
        self.button_mkhelp.setStyleSheet(button_stylesheet1)
        self.button_cmds = QPushButton("cmds")
        self.button_cmds.setStyleSheet(button_stylesheet1)
        # self.button_cmds.setMenu(self.create_menu_cmds())
        self.button_cmds.setMenu(create_menu_cmds(self))
        self.button_mkcommand = QPushButton("Perintah")
        self.button_mkcommand.setStyleSheet(button_stylesheet1)
        self.button_mkcommand.setMenu(create_menu_mkcommand(self))

        self.button_sido.clicked.connect(lambda: mulai(exec_code_sidoarjo))
        # self.button_editors.clicked.connect(lambda: mulai(exec_notepad, ()))
        self.button_mkhelp.clicked.connect(functools.partial(execute_in_thread, f'python {programming_data["j"]["scripts"]["mkhelp"]}'))
        # functools.partial(execute_in_thread, r'python C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\mkhelp.py')

        self.main_layout.addWidget(self.button_sido, 1, 0)
        self.main_layout.addWidget(self.button_editors, 1, 1)
        self.main_layout.addWidget(self.button_mkhelp, 1, 2)
        self.main_layout.addWidget(self.button_cmds, 1, 3)
        self.main_layout.addWidget(self.button_mkcommand, 1, 4)

        # self.toolbar_layout = QHBoxLayout()
        # self.toolbar_layout.addWidget(self.collapse_button)
        # self.toolbar_layout.addWidget(self.preset_location)
        # self.toolbar_layout.addWidget(self.goto_lineedit)
        # self.toolbar_layout.addWidget(self.goto_button)
        # self.toolbar_layout.addStretch(1)
        # self.main_layout.addLayout(self.toolbar_layout, 0, 0)
        self.main_layout.addWidget(self.folder_view, 2, 0, 3, 5)
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

        self.menu_git_clone = QMenu('🙈 Git clone')
        # git_clone_input_menu = QMenu('Git clone', self.menu_git_clone)
        self.git_clone_input_widget = QLineEdit(self.menu_git_clone)
        self.git_clone_input_widget.setStyleSheet('background-color: oldlace; height: 32px; font-family: Verdana; font-size: 16pt;')
        git_clone_input_action = QWidgetAction(self.menu_git_clone)
        git_clone_input_action.setDefaultWidget(self.git_clone_input_widget)
        self.menu_git_clone.addAction(git_clone_input_action)
        self.menu_git_clone.addAction('Clone from clipboard', self.git_clone_from_clipboard)
        self.git_clone_input_widget.returnPressed.connect(self.git_clone_from_input)
        # self.menu_git_clone.addMenu(git_clone_input_menu)
            
        self.provider_menu = QMenu('Providers')
        self.provider_menu.addAction(get_icon(), 'Reload', lambda: self.reload_context_menu_providers(None))
        self.provider_menu_for_file = QMenu('Providers (files)')
        self.provider_menu_for_file.addAction(get_icon(), 'Reload', lambda: self.reload_context_menu_providers_for_file(None))

        self.lineedit_menu = QMenu('Enter command here', self)
        self.lineedit_menu_control = QLineEdit(self.lineedit_menu)
        self.lineedit_menu_control.setFont(QFont("Verdana", 16))
        self.lineedit_menu_control.setStyleSheet('background-color: oldlace; height: 32px;')
        self.lineedit_menu_action = QWidgetAction(self.lineedit_menu)
        label_edit = QHBoxLayout()
        label_edit.addWidget(QLabel('Command:'))
        label_edit.addWidget(self.lineedit_menu_control)
        label_edit_widget = QWidget()
        label_edit_widget.setLayout(label_edit)
        # self.lineedit_menu_action.setDefaultWidget(self.lineedit_menu_control)
        self.lineedit_menu_action.setDefaultWidget(label_edit_widget)
        self.lineedit_menu.addAction(self.lineedit_menu_action)
        self.lineedit_menu_control.returnPressed.connect(self.handler_for_lineedit_menu_control)
        self.command_history = []
        self.command_completer = QCompleter(self.command_history)
        self.command_completer.setCompletionMode(QCompleter.PopupCompletion)
        self.command_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineedit_menu_control.setCompleter(self.command_completer)

        self.yarn_add_menu = QMenu('yarn add', self)
        self.yarn_add_menu_action = QWidgetAction(self.yarn_add_menu)
        self.packager_widget = PackageWidget(items=yarn_add_packages, callback=self.yarn_add_callback)
        self.yarn_add_menu_action.setDefaultWidget(self.packager_widget)
        self.yarn_add_menu.addAction(self.yarn_add_menu_action)

        self.yarn_add_menu_dev = QMenu('yarn add -D', self)
        self.yarn_add_menu_action2 = QWidgetAction(self.yarn_add_menu_dev)
        self.packager_widget_dev = PackageWidget(items=yarn_add_packages_dev, callback=self.yarn_add_dev_callback)
        self.yarn_add_menu_action2.setDefaultWidget(self.packager_widget_dev)
        self.yarn_add_menu_dev.addAction(self.yarn_add_menu_action2)

        self.quick_creator_menu = QMenu('Quick!', self)
        self.quick_creator_widget = CreatorWidget(parent=self.quick_creator_menu)
        self.quick_creator_action = QWidgetAction(self.quick_creator_menu)
        self.quick_creator_action.setDefaultWidget(self.quick_creator_widget)
        self.quick_creator_menu.addAction(self.quick_creator_action)

        self.choosecommand_menu = QMenu('Choose command here', self)
        container = QWidget()
        container_layout = QHBoxLayout(container)
        self.do_execute = QPushButton('Exec', container)
        self.do_execute.setStyleSheet(button_stylesheet2)
        self.do_execute.clicked.connect(self.handler_for_combobox_menu_control_by_button)
        self.choosecommand_menu_control = QComboBox(self.choosecommand_menu)
        self.choosecommand_menu_control.setFont(QFont("Verdana", 16))
        self.choosecommand_menu_control.setStyleSheet('background-color: oldlace; height: 32px;')
        self.choosecommand_menu_action = QWidgetAction(self.choosecommand_menu)
        container_layout.addWidget(self.choosecommand_menu_control)
        container_layout.addWidget(self.do_execute)
        # self.choosecommand_menu_action.setDefaultWidget(self.choosecommand_menu_control)
        self.choosecommand_menu_action.setDefaultWidget(container)
        self.choosecommand_menu.addAction(self.choosecommand_menu_action)
        # self.choosecommand_menu_control.currentIndexChanged.connect(self.handler_for_combobox_menu_control)
        self.choosecommand_menu_control.addItems(predefined_commands)


        self.click_command_menu = QMenu('Click choose command', self)
        self.click_command_packager_widget = PackageWidget(items=predefined_commands, callback=self.click_command_callback, button_mode=True)
        self.click_command_action = QWidgetAction(self.click_command_menu)        
        self.click_command_action.setDefaultWidget(self.click_command_packager_widget)
        self.click_command_menu.addAction(self.click_command_action)


        self.folder_view.setExpandsOnDoubleClick(True)
        self.folder_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.folder_view.doubleClicked.connect(self.klik_ganda)
        self.folder_view.clicked.connect(self.klik_tunggal)
        self.folder_view.selectionModel().selectionChanged.connect(self.klik_dengan_keyboard)
        # self.folder_view.clicked[QModelIndex].connect(self.clicked_onfolder)
        self.folder_view.customContextMenuRequested.connect(functools.partial(self.folder_view_context_menu))
        self.goto_button.clicked.connect(functools.partial(self.go_to))
        self.collapse_button.clicked.connect(functools.partial(self.collapse_tree))

        # self.context_menu = QMenu()
        # self.kenza_us_menu = self.create_us_executors_menu()

        self.setLayout(self.main_layout)
        self.setWindowTitle('FM')

        # total_width = self.folder_view.width()
        total_width = self.width()
        width_portion = (3,1,1,1)
        total_portion = sum(width_portion)
        
        self.set_rootpath.connect(self.save_current_rootpath)

        for i in range(4):
            portion = total_width*width_portion[i]//total_portion
            # print(f"{i} = {portion}")
            self.folder_view.setColumnWidth(i, portion)
        # self.expand_top_node()
        # self.folder_model.directoryLoaded.connect(self.expand_top_node)
        # self.expand_top_node(self.folder_model.index(None))
        # self.show()
        self.showedit = ShowEditWindow(title='Quick edit Fmus program', initial_text='.,d\n\t')

        self.quickedit_menu = QMenu('Quick create file', self)
        self.quickedit_menu_control = QLineEdit(self.quickedit_menu)
        self.quickedit_menu_control.setFont(QFont("Verdana", 16))
        self.quickedit_menu_control.setStyleSheet('background-color: oldlace; height: 32px;')
        self.quickedit_menu_action = QWidgetAction(self.quickedit_menu)
        self.quickedit_menu_action.setDefaultWidget(self.quickedit_menu_control)
        self.quickedit_menu.addAction(self.quickedit_menu_action)
        self.quickedit_menu_control.returnPressed.connect(self.create_edit_file_quick)

        self.peekfile_menu = QMenu('Peek file', self)
        self.peekfile_menu_wrapper = QWidget()
        self.peekfile_menu_layout = QVBoxLayout(self.peekfile_menu_wrapper)
        # dummy_text = QLabel('ini adalah tulisan yang sengaja dibuat panjang untuk membuat showedit jadi melebar, tampaknya ini cukup berhasil untuk menipu text editor sehingga menjadi benar2 lebar...')
        dummy_text = QLabel('__________________________________________________________________________________________________________________________________________________________________________')
        dummy_text.setStyleSheet('font-family: Consolas;')
        self.peekfile_menu_layout.addWidget(dummy_text)
        self.peekfile_menu_control = ShowEditWindow(compact=True)
        self.peekfile_menu_action = QWidgetAction(self.peekfile_menu)
        self.peekfile_menu_layout.addWidget(self.peekfile_menu_control)
        # self.peekfile_menu_action.setDefaultWidget(self.peekfile_menu_control)
        self.peekfile_menu_action.setDefaultWidget(self.peekfile_menu_wrapper)
        self.peekfile_menu.addAction(self.peekfile_menu_action)

    def create_menu_cmds(self):
        # vscodecmd = programming_data['j']['programs']['vscodecmd']
        # fleetcmd = programming_data['j']['programs']['fleetcmd']
        self.menu_cmds = QMenu(self)

        for label, exepath in programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['filetreewidget'].items():
            self.menu_cmds.addAction(
                QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
                label,
                functools.partial(subprocess.Popen, f"{programming_data['j']['programs']['vscodecmd']} {exepath}")
            )
        for label, exepath in programming_data['j']['browsers']['programs'].items():
            self.menu_cmds.addAction(
                QApplication.style().standardIcon(QStyle.SP_DirOpenIcon),
                label,
                functools.partial(subprocess.Popen, exepath['exe'])
            )
        return self.menu_cmds

    def set_input_completer(self):
        model = self.completer.model()
        model.setStringList(self.history)

    def clicked_onfolder(self, index):
        selection_model = self.folder_view.selectionModel()
        index = selection_model.currentIndex()
        dir_path = self.folder_model.filePath(index)
        # self.folder_model.setRootPath(dir_path)
        # self.folder_view.setRootIndex(self.folder_model.index(dir_path))

    def klik_tunggal(self, index):
        if self.folder_model.isDir(index):
            self.folder_view.expand(index)
        else:
            filepath = self.folder_model.filePath(index)
            ext = get_extension(filepath)
            if not_binary(filepath):
                self.new_file_clicked.emit(filepath)
            elif ext.lower() in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
                self.imagefile_clicked.emit(filepath)
            elif ext.lower() in ['pdf']:
                self.pdffile_clicked.emit(filepath)

    def klik_dengan_keyboard(self, selected, deselected):
        """
        https://stackoverflow.com/questions/13919652/how-to-react-to-keyboard-selection-on-qttreeview
        https://stackoverflow.com/questions/38455913/how-can-i-set-the-keyboard-focus-for-a-qtreeview-item
        https://stackoverflow.com/questions/23006325/selecting-items-in-a-qtreeview-with-keyboard-arrows
        """
        indexes = selected.indexes()
        if indexes:            
            index = indexes[0]
            filepath = self.folder_model.filePath(index)
            ext = get_extension(filepath)
            if not_binary(filepath):
                self.new_file_clicked.emit(filepath)
            elif ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
                self.imagefile_clicked.emit(filepath)
            elif ext in ['pdf']:
                self.pdffile_clicked.emit(filepath)

    def klik_ganda(self, index):
        if self.folder_model.isDir(index):
            filePath = self.folder_model.filePath(index)
            self.set_rootpath.emit(filePath)
            if filePath not in self.history:
                self.history.append(filePath)
                self.set_input_completer()

    def ganti_direktori(self, folder):
        # print('ganti', folder)
        index = self.folder_model.index(folder)
        # self.folder_view.setExpandsOnDoubleClick(True)
        # https://stackoverflow.com/questions/7462054/get-and-set-the-active-row-in-qtreeview-programmatically-pyqt
        self.folder_view.setCurrentIndex(index)
        self.folder_view.expand(index)
        filePath = self.folder_model.filePath(index)
        self.set_rootpath.emit(filePath)
        if filePath not in self.history:
            self.history.append(filePath)
            self.set_input_completer()

    def save_current_rootpath(self, filePath):
        self.rootpath = filePath

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
            if not os.path.isdir(parentdir):
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
            if not os.path.isdir(parentdir):
                parentdir = os.path.dirname(parentdir)
            filepath = os.path.join(parentdir, name.strip())
            os.system(f'code "{filepath}"')

    def create_edit_file_quick(self):
        filename = self.quickedit_menu_control.text().strip()
        # dirpath dari control.property('dirpath')
        dirpath = self.quickedit_menu_control.property('dirpath')
        if filename and dirpath:
            filepath = os.path.join(dirpath, filename)
            print('quick create file:', filepath)
            self.showedit = ShowEditWindow(filepath, title=filepath, initial_text='')
            self.showedit.show()

    def edit_file_quick(self):
        # filename = self.quickedit_menu_control.text().strip()
        # dirpath dari control.property('dirpath')
        filepath = self.quickedit_menu_control.property('filepath')
        if filepath:
            # filepath = os.path.join(dirpath, filename)
            print('quick edit file:', filepath)
            self.showedit = ShowEditWindow(filepath, title=filepath, initial_text=file_content(filepath))
            self.showedit.show()

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

    def move_file(self, parentdir, starting_dir=None):
        if not os.path.isdir(parentdir):
            parentdir = os.path.dirname(parentdir)
        if starting_dir is None:
            starting_dir = parentdir
        ask = QFileDialog.getExistingDirectory(self, "Open Directory to move file", starting_dir,
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        if ask == '':
            return
        new_path = ask.replace('\\', '/')
        indexes = self.folder_view.selectedIndexes()[::4]  # name, size, type, date
        for i in indexes:
            new_filename = new_path + '/' + self.folder_model.fileName(i)
            shutil.move(self.folder_model.filePath(i), new_filename)

    def copy_file(self, parentdir):
        if not os.path.isdir(parentdir):
            parentdir = os.path.dirname(parentdir)
        ask = QFileDialog.getExistingDirectory(self, "Open Directory to copy file", parentdir,
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        new_path = ask.replace('\\', '/')
        indexes = self.folder_view.selectedIndexes()[::4]
        for i in indexes:
            source_file = self.folder_model.filePath(i)
            file_name = self.folder_model.fileName(i)
            new_filename = new_path + '/' + file_name
            counter = 1
            while source_file == new_filename:
                file_name_orig, ext = os.path.splitext(new_filename)
                new_filename = file_name_orig + str(counter) + ext
                counter += 1
            # PermissionError: [Errno 13] Permission denied: '/jfx-maven.fmus'
            shutil.copy2(source_file, new_filename)

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

    def copy_folder(self, parentdir):
        if not os.path.isdir(parentdir):
            parentdir = os.path.dirname(parentdir)
        ask = QFileDialog.getExistingDirectory(self, "Open Directory to copy folder", parentdir,
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        new_path = ask.replace('\\', '/')
        new_folder = os.path.basename(parentdir)
        new_path = os.path.join(new_path, new_folder)
        if os.path.normpath(new_path) != os.path.normpath(parentdir):
            print(f"""copy folder
            oldpath = {parentdir}
            newpath = {new_path}
            """)
            shutil.copytree(parentdir, new_path)
        else:
            counter = 2
            new_path += f'_{counter}'
            while os.path.isdir(new_path):
                counter += 1
                new_path += f'_{counter}'
            shutil.copytree(parentdir, new_path)

    def move_folder(self, parentdir):
        if not os.path.isdir(parentdir):
            parentdir = os.path.dirname(parentdir)
        ask = QFileDialog.getExistingDirectory(self, "Open Directory to move folder", parentdir,
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        new_path = ask.replace('\\', '/')
        if os.path.normpath(new_path) != os.path.normpath(parentdir):
            print(f"""move folder
            oldpath = {parentdir}
            newpath = {new_path}
            """)
            shutil.move(parentdir, new_path)

    def run_sublime_thread(self, filePath):
        argumen = f'"C:/Program Files/Sublime Text/sublime_text.exe" {filePath}'
        t = threading.Thread(target=os.system, args=(argumen,))
        t.start()

    def git_clone_from_input(self):
        """
        both dari clipboard dan input, filepath kita ambil dari property parent menu
        krn langsung handle utk keduanya
        """
        alamat = self.git_clone_input_widget.text().strip()
        if not alamat.startswith('https://'):
            return
        cmd = 'git clone ' + alamat
        if self.menu_git_clone.property('filepath'):
            filePath = self.menu_git_clone.property('filepath')
            if not os.path.isdir(filePath):
                filePath = os.path.dirname(filePath)
            execute_command_in_dir_in_thread(cmd, filePath)

    def git_clone_from_clipboard(self):
        import pyperclip
        alamat = pyperclip.paste()
        if not alamat.startswith('https://'):
            return
        cmd = 'git clone ' + alamat
        if self.menu_git_clone.property('filepath'):
            filePath = self.menu_git_clone.property('filepath')
            if not os.path.isdir(filePath):
                filePath = os.path.dirname(filePath)
            execute_command_in_dir_in_thread(cmd, filePath)

    def click_command_callback(self, cmd):
        if self.context_menu.property('filepath'):
            filePath = self.context_menu.property('filepath')
            execute_command_in_dir_in_thread(cmd, filePath)

    def yarn_add_callback(self, packages):
        cmd = f'yarn add {packages}'
        print(cmd)
        if self.packager_widget.property('filepath'):
            filePath = self.packager_widget.property('filepath')
            if not os.path.isdir(filePath):
                filePath = os.path.dirname(filePath)
            execute_command_in_dir_in_thread(cmd, filePath)

    def yarn_add_dev_callback(self, packages):
        cmd = f'yarn add -D {packages}'
        print(cmd)
        if self.packager_widget_dev.property('filepath'):
            filePath = self.packager_widget_dev.property('filepath')
            if not os.path.isdir(filePath):
                filePath = os.path.dirname(filePath)
            execute_command_in_dir_in_thread(cmd, filePath)

    def handler_for_lineedit_menu_control(self):
        filePath = self.lineedit_menu_control.property('filepath')
        if not os.path.isdir(filePath):
            filePath = os.path.dirname(filePath)
        perintah = self.lineedit_menu_control.text()
        # print(f'{filePath} => {perintah}')
        # stat = execute_command_in_dir(perintah, filePath, command_is_string=True)
        execute_command_in_dir_in_thread(perintah, filePath)
        self.lineedit_menu_control.setText('')
        if perintah not in self.command_history:
            self.command_history.append(perintah)
            self.command_completer.model().setStringList(self.command_history)

    def handler_for_combobox_menu_control(self):
        filePath = self.choosecommand_menu_control.property('filepath')
        if not filePath:
            return # di awal, nilai None
        pilihan = self.choosecommand_menu_control.currentText()
        print(f"perintah utk dikerjakan: [{pilihan}] di dalam {filePath}.")
        if self.do_execute.checkState == Qt.Checked:
            # stat = execute_command_in_dir(pilihan, filePath, command_is_string=True)
            # print('status:', stat)
            execute_command_in_dir_in_thread(pilihan, filePath)

    def handler_for_combobox_menu_control_by_button(self):
        filePath = self.do_execute.property('filepath')
        if not filePath:
            return # di awal, nilai None
        elif not os.path.isdir(filePath):
            filePath = os.path.dirname(filePath)
        pilihan = self.choosecommand_menu_control.currentText()
        print(f"perintah utk dikerjakan: [{pilihan}] di dalam {filePath}.")
        # stat = execute_command_in_dir(pilihan, filePath, command_is_string=True)
        execute_command_in_dir_in_thread(pilihan, filePath)
        # self.reorder_predefined_commands(pilihan, self.choosecommand_menu_control.currentIndex())
        self.reorder_predefined_commands(pilihan)
    
    def reorder_predefined_commands(self, text):
        predefined_commands[:] = [text] + [item for item in predefined_commands if item != text]

    def create_providers_menu(self, filePath):
        if not os.path.isdir(filePath):
            filePath = os.path.dirname(filePath)  # bisa digunakan utk file
        menu_provider = QMenu('Providers')
        for mk_filename,v in context_menu_for_dirs_with_entries.items():
            '''
            BUGS:
            menu_per_file = QMenu(filename) hanya muncul 1x walau ada bbrp file
            (harus kasih parent menu!)
            '''
            # k = filename.mk, v = entries
            # run_fmus_in_directory_in_thread
            # masalahnya k ini fullpath
            filename = os.path.basename(mk_filename).removesuffix('.mk').removesuffix('.fmus')
            # print('create_providers_menu => looping:', mk_filename, 'dg value:', v, 'nama menu:', filename)
            # pelajaran penting!
            # ternyata hrs kasih parent, jk gak
            menu_per_file = QMenu(filename, menu_provider)
            for entry in v:
                # pake lambda di sini jadi hanya v terakhir yg dipake utk semua v
                # menu_per_file.addAction(entry, lambda: self.run_fmus_in_directory_in_thread(filePath, mk_filename, entry))
                menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, filePath, mk_filename, entry))
                # ini argumen yg salah
                # menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, (filePath, mk_filename, entry)))
            menu_provider.addMenu(menu_per_file)
        menu_provider.addAction(get_icon(), 'Reload', lambda: self.reload_context_menu_providers(filePath))
        self.provider_menu = menu_provider
        return self.provider_menu

    def create_providers_menu_for_file(self, filePath):
        menu_provider = QMenu('Providers (files)')
        dirPath = os.path.dirname(filePath)
        for mk_filename,v in context_menu_for_files_with_entries.items():
            filename = os.path.basename(mk_filename).removesuffix('.mk').removesuffix('.fmus')
            menu_per_file = QMenu(filename, menu_provider)
            for entry in v:
                menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, dirPath, mk_filename, entry))
            menu_provider.addMenu(menu_per_file)
        menu_provider.addAction(get_icon(), 'Reload', lambda: self.reload_context_menu_providers_for_file(filePath))
        self.provider_menu_for_file = menu_provider
        return self.provider_menu_for_file

    def create_us_executors_menu(self):
        # global kenza_us_files
        filePath = self.context_menu.property('filepath')
        if not filePath:
            return None
        if os.path.isfile(filePath):
            filePath = os.path.dirname(filePath)
        menu_provider = QMenu('Kenza us files')
        for us_filename in kenza_us_files:
            jarak = os.path.relpath(us_filename, kenza_us_dir)
            if jarak != os.path.basename(us_filename):
                filename = jarak.removesuffix('.mk').removesuffix('.fmus').removesuffix('.us').removesuffix('.fm')
            else:
                filename = os.path.basename(us_filename).removesuffix('.mk').removesuffix('.fmus').removesuffix('.us').removesuffix('.fm')
            # menu_per_file = QMenu(filename, menu_provider)
            # for entry in v:
            #     menu_per_file.addAction(entry, functools.partial(self.run_us_in_directory_in_thread, filePath, mk_filename, entry))
            # menu_provider.addMenu(menu_per_file)
            menu_provider.addAction(filename, functools.partial(self.run_us_in_directory_in_thread, filePath, us_filename))
        menu_provider.addAction(get_icon(), 'Reload', lambda: self.reload_kenza_us_files())
        self.kenza_us_menu = menu_provider
        return self.kenza_us_menu

    def reload_kenza_us_files(self):
        global kenza_us_files
        kenza_us_files = reload_kenza_us_files()
        self.create_us_executors_menu()

    def reload_context_menu_providers(self, filePath):
        global context_menu_for_dirs_with_entries, context_menu_for_dirs
        context_menu_for_dirs = files_filter(joiner(sidoarjodir, 'providers/directories'), extension=['.mk'], abs_path=True)
        context_menu_for_dirs_with_entries = {k:get_daftar(k) for k in context_menu_for_dirs}
        # print('reload_context_menu_providers:', context_menu_for_dirs_with_entries)
        self.create_providers_menu(filePath)

    def reload_context_menu_providers_for_file(self, filePath):
        global context_menu_for_files_with_entries, context_menu_for_files
        context_menu_for_files = files_filter(joiner(sidoarjodir, 'providers/files'), extension=['.mk'], abs_path=True)
        context_menu_for_files_with_entries = {k:get_daftar(k) for k in context_menu_for_files}
        # print('reload_context_menu_providers:', context_menu_for_dirs_with_entries)
        self.create_providers_menu_for_file(filePath)

    def shell_execute(self, filePath):
        import win32api
        dirPath = filePath
        if not os.path.isdir(filePath):
            dirPath = os.path.dirname(filePath)
        win32api.ShellExecute(0,    # NULL since it's not associated with a window
            "open",                 # the operation to perform. May be "open", "print", or None, which defaults to "open".
            filePath,               # path to the document file to print
            None,                   # no parameters, since the target is a document file
            dirPath,                # current directory, same as NULL here
            0)                      # SW_HIDE passed to app associated with the file type

    def generate_signal(self, signal, filePath):
        signal.emit(filePath)
        pyperclip.copy(filePath)  # masukkan ke folder krn berguna utk berbagai hal        

    def folder_view_context_menu(self, point):
        index = self.folder_view.indexAt(point)
        self.context_menu = QMenu()
        self.context_menu.setStyleSheet(context_menu_stylesheet)
        fileName = self.folder_model.fileName(index)
        filePath = self.folder_model.filePath(index)
        self.context_menu.addAction(filePath, lambda: explore(filePath))
        self.context_menu.addAction(f"ShellExecute filePath", lambda: self.shell_execute(filePath))
        self.context_menu.addSeparator()
        self.context_menu.addAction(f"code {filePath}", lambda: os.system(f"code {filePath}"))
        self.context_menu.addSeparator()

        # properties
        self.context_menu.setProperty('filepath', filePath)
        self.packager_widget.setProperty('filepath', filePath)
        self.packager_widget_dev.setProperty('filepath', filePath)
        self.lineedit_menu_control.setProperty('filepath', filePath)
        self.choosecommand_menu_control.setProperty('filepath', filePath)
        self.do_execute.setProperty('filepath', filePath)
        self.quickedit_menu_control.setProperty('dirpath', filePath)
        self.menu_git_clone.setProperty('filepath', filePath)

        if os.path.isdir(filePath):
            # self.quick_creator_widget.setProperty('dirpath', filePath)
            self.quick_creator_widget.set_filepath_dirpath(dirpath=filePath)
        else:
            self.quickedit_menu_control.setProperty('dirpath', os.path.dirname(filePath))
            # self.quick_creator_widget.setProperty('dirpath', os.path.dirname(filePath))
            # self.quick_creator_widget.setProperty('filepath', filePath)
            self.quick_creator_widget.set_filepath_dirpath(filepath=filePath, dirpath=os.path.dirname(filePath))
        self.context_menu.addMenu(self.quick_creator_menu)
        self.context_menu.addMenu(self.quickedit_menu)
        self.context_menu.addSeparator()
        # dahsyat menu
        # self.dahsyat_menu = DashsyatMenu('Dahsyat', self)
        # self.dahsyat_menu.create_providers_menu(filePath)
        self.dahsyat_menu = DashsyatMenu(filePath, 'Dahsyat', self)
        self.context_menu.addMenu(self.dahsyat_menu)
        self.create_providers_menu(filePath)
        self.context_menu.addMenu(self.provider_menu)
        self.kenza_menu = self.mkmenu_from_dir(kenzadir)
        self.context_menu.addMenu(self.kenza_menu)        
        self.context_menu.addMenu(self.create_us_executors_menu())
        self.context_menu.addSeparator()
        self.context_menu.addMenu(self.lineedit_menu)
        self.context_menu.addMenu(self.choosecommand_menu)
        self.context_menu.addMenu(self.click_command_menu)
        self.context_menu.addMenu(self.menu_git_clone)
        if os.path.isfile(filePath):
            self.context_menu.addAction(get_icon(), 'Move to kenza', lambda: self.move_file(filePath, kenzadir))
        # self.context_menu.addAction(get_icon(), 'New WSL here', lambda: self.request_wsl.emit(filePath))
        # self.context_menu.addAction(get_icon(), 'docker-compose up', lambda: self.request_docker_compose_up.emit(filePath))
        self.context_menu.addAction(get_icon(), 'Copy path', lambda: pyperclip.copy(filePath))
        self.context_menu.addAction(get_icon(), 'New CMD here', lambda: self.generate_signal(self.request_cmd, filePath))
        self.context_menu.addAction(get_icon(), 'New WSL here', lambda: self.generate_signal(self.request_wsl, filePath))
        self.context_menu.addAction(get_icon(), 'docker-compose up', lambda: self.generate_signal(self.request_docker_compose_up, filePath))
        self.context_menu.addAction(get_icon(), 'Run Fmus here', lambda: self.run_fmus_in_directory(filePath))
        self.context_menu.addAction(get_icon(), 'Run Fmus clipboard here', lambda: self.run_fmus_clipboard_in_directory(filePath))
        if os.path.isdir(filePath):
            self.context_menu.addAction(get_icon(), f'{fileName} => fmus all subfolders', lambda: fmus_operate_on_listdir(filePath))
        self.context_menu.addAction(get_icon(), f'{fileName} => fmus', lambda: self.generate_fmus_for_folder(filePath))
        self.context_menu.addAction(get_icon(), f'{fileName} => fmus with index', lambda: self.generate_fmus_for_folder(filePath, True))
        self.context_menu.addSeparator()
        if os.path.isdir(filePath):
            self.context_menu.addSeparator()
            project_menu = QMenu('Project', self.context_menu)
            # project_menu.addMenu(self.menu_standard_project)
            # project_menu.addMenu(self.menu_mobile_project)
            # project_menu.addMenu(self.menu_create_project)
            project_menu.addMenu(self.yarn_add_menu)
            project_menu.addMenu(self.yarn_add_menu_dev)
            self.context_menu.addMenu(project_menu)
            # self.context_menu.addMenu(self.menu_standard_project)
            # self.context_menu.addMenu(self.menu_mobile_project)
            # self.context_menu.addMenu(self.menu_create_project)
            # self.context_menu.addMenu(self.yarn_add_menu)
            # self.context_menu.addMenu(self.yarn_add_menu_dev)
            self.context_menu.addSeparator()
            # self.context_menu.addAction('Git clone here')
            self.context_menu.addAction('Download URL here')
            self.context_menu.addSeparator()
        else:
            if not_binary(filePath):
                # self.context_menu: file peek
                self.peekfile_menu_control.set_info(filePath, file_content(filePath))
                self.context_menu.addMenu(self.peekfile_menu)
                # self.context_menu: file manipulation
                filemanip_menu = filemanip(filePath, self.context_menu)
                # tambah "peek file" sendiri ke filemanip
                filemanipulation_menu_control = ShowEditWindow(filepath=filePath, title=filePath, initial_text=file_content(filePath), compact=True)
                filemanipulation_menu_action = QWidgetAction(filemanip_menu)
                filemanipulation_menu_action.setDefaultWidget(filemanipulation_menu_control)
                filemanip_menu.addAction(filemanipulation_menu_action)
                self.context_menu.addMenu(filemanip_menu)

        if os.path.isfile(filePath):
            if not_binary(filePath):
                self.context_menu.addAction('👀View File', lambda: tkeditor(filePath))
            # self.create_providers_menu(filePath)
            # self.context_menu.addMenu(self.provider_menu)
            self.create_providers_menu_for_file(filePath)
            self.context_menu.addMenu(self.provider_menu_for_file)
            self.context_menu.addAction('Rename File', lambda: self.rename_file(filePath))
            self.context_menu.addAction('Move File', lambda: self.move_file(filePath))
            self.context_menu.addAction('Copy File', lambda: self.copy_file(filePath))
            self.context_menu.addAction(f'🔥Delete File {os.path.basename(filePath)}', lambda: self.delete_file(filePath))
            if filePath.endswith('.mk') or filePath.endswith('.fmus'):
                daftar = get_daftar(filePath)
                if daftar:
                    fmus_menu = QMenu(fileName)
                    for baris_entry in daftar:
                        fmus_menu.addAction(baris_entry, functools.partial(self.run_fmus_from_file, filePath, baris_entry))
                    self.context_menu.addMenu(fmus_menu)
                    # fmus/mk => vscode
                    vscode_menu = QMenu(f"{fileName} => vscode")
                    vscode_menu.addAction('Global snippet here', lambda: self.vscode_global(filePath))
                    # vscode_menu.addAction('Global snippet here', self.vscode_global)
                    for lang in programming_data['j']['schnell']['app']['vscodeutils']['vscode_language_identifiers']:
                        vscode_menu.addAction(f"Language snippet {lang}", lambda: self.vscode_local(filePath, lang))
                    self.context_menu.addMenu(vscode_menu)

        elif os.path.isdir(filePath):
            self.context_menu.addAction('Rename folder', lambda: self.rename_folder(filePath))
            self.context_menu.addAction(f'Delete folder {filePath}', lambda: self.delete_folder(filePath))
            self.context_menu.addAction('Copy folder', lambda: self.copy_folder(filePath))
            self.context_menu.addAction(f'Move folder {filePath}', lambda: self.move_folder(filePath))

        self.context_menu.addAction('💥New Folder', lambda: self.create_newdir(filePath))
        self.context_menu.addAction('⚡New File', lambda: self.create_edit_file(filePath))

        self.context_menu.exec_(self.folder_view.mapToGlobal(point))

    def run_fmus_from_file(self, filePath, baris_entry):
        """
        list kasus di sini
        - klik kanan file fmus, exec baris entry
        di sini rootpath sama dg dirpath(filepath)
        """
        print(f"""[fm][run_fmus_from_file] cek jk self.rootpath belum terset. berarti selection mungkin dg keyboard.
        hrs diset ke dir dari filepath jk file, atau ke filepath jk dir.
        {filePath}, {baris_entry}
        """)
        dirPath = os.path.dirname(filePath)
        if not hasattr(self, 'rootpath'):
            self.rootpath = dirPath
        res = QMessageBox.information(None, f"{filePath}", f'Sure to run "{filePath}:{baris_entry}" in {self.rootpath}?', QMessageBox.Ok | QMessageBox.Cancel)
        if res == QMessageBox.Ok:
            os.chdir(self.rootpath)
            # filePath hrs dicopy dulu ke target
            if self.rootpath != dirPath:
                targetfilePath = shutil.copy2(filePath, self.rootpath)
            else:
                targetfilePath = filePath
            # jalankan fmus file baru di self.rootpath
            x = threading.Thread(target=run_fmus_for_file, args=(targetfilePath, baris_entry,))
            x.start()
            # loncat ke folder hasil, juga penanda bhw proses sudah selesai
            self.folder_view.setCurrentIndex(self.folder_model.index(self.rootpath))

    def run_fmus_clipboard_in_directory(self, filePath):
        from schnell.app.threadutils import mulai
        if os.path.isfile(filePath):
            filePath = os.path.dirname(filePath)
        content = pyperclip.paste()
        if not content.endswith('\n'):
            content += '\n'
        # run_fmus_for_content(content, dirpath=filePath, start_fresh=True)
        mulai(target=run_fmus_for_content, args=(content,), kwargs={'dirpath':filePath, 'start_fresh':True})

    def run_fmus_in_directory(self, filePath):
        if os.path.isfile(filePath):
            filePath = os.path.dirname(filePath)
        self.showedit.show()
        self.showedit.quit_signal.connect(lambda content: run_fmus_for_content(content, dirpath=filePath, start_fresh=True))

    def run_fmus_in_directory_in_thread(self, targetDir, sourcefilePath, barisEntry):
        if os.path.isfile(targetDir):
            targetDir = os.path.dirname(targetDir)
        print(f"""[fm][run_fmus_in_directory_in_thread]
        targetDir {targetDir}, sourcefilePath [{sourcefilePath}], barisEntry [{barisEntry}]
        """)
        run_fmus_for_file_in_folder_in_thread(targetDir, sourcefilePath, barisEntry)

    def run_us_in_directory_in_thread(self, targetDir, sourcefilePath):
        if os.path.isfile(targetDir):
            targetDir = os.path.dirname(targetDir)
        targetDir = os.path.normpath(targetDir)
        print(f"""[fm][run_us_in_directory_in_thread]
        targetDir {targetDir}, sourcefilePath (us/fm file) [{sourcefilePath}]]
        """)
        run_us_in_folder_in_thread(targetDir, sourcefilePath)

    def go_to(self):
        dir_path = self.goto_lineedit.text().replace('\\', '/')
        print(dir_path)
        # harusnya di sini adlh...selection...
        # self.folder_model.setRootPath(dir_path)
        # self.folder_view.setRootIndex(self.folder_model.index(dir_path))
        # self.folder_model.setRootPath()

    def collapse_tree(self):
        self.folder_view.collapseAll()

    def generate_fmus_for_folder(self, filePath, create_index=False):
        """
        filePath selalu folder, jadi jk terima file, ambil dulu dirnamenya.
        """
        from schnell.app.fmusutils import reverse_folder
        if os.path.isfile(filePath):
            filePath = os.path.dirname(filePath)
        reverse_folder(filePath, create_index=create_index)

    def vscode_global(self, filePath):
        base_folder = os.path.dirname(filePath) if os.path.isfile(filePath) else filePath
        base_folder = os.path.join(base_folder, '.vscode')
        create_snippet_wrapper(filePath, base_folder=base_folder, language=None)

    def vscode_local(self, filePath, language):
        base_folder = os.path.dirname(filePath) if os.path.isfile(filePath) else filePath
        base_folder = os.path.join(base_folder, '.vscode')
        create_snippet_wrapper(filePath, base_folder=base_folder, language=language)

    def mkmenu_handle_file(self, filePath, fileName):
        """
            if filePath.endswith('.mk') or filePath.endswith('.fmus'):
                daftar = get_daftar(filePath)
                if daftar:
                    fmus_menu = QMenu(fileName)
                    for baris_entry in daftar:
                        fmus_menu.addAction(baris_entry, functools.partial(self.run_fmus_from_file, filePath, baris_entry))
                    menu.addMenu(fmus_menu)
                    # fmus/mk => vscode
                    vscode_menu = QMenu(f"{fileName} => vscode")
                    vscode_menu.addAction('Global snippet here', lambda: self.vscode_global(filePath))
                    # vscode_menu.addAction('Global snippet here', self.vscode_global)
                    for lang in vscode_language_identifiers:
                        vscode_menu.addAction(f"Language snippet {lang}", lambda: self.vscode_local(filePath, lang))
                    menu.addMenu(vscode_menu)
        """
        menu = QMenu(fileName, self.context_menu)
        target = self.context_menu.property('filepath')
        # menu.addAction(fileName, lambda: print(f"copy file from {filePath} to {target}"))
        menu.addAction(fileName, lambda: self.salin_file(filePath, target))

        # daftar = get_daftar(filePath)
        # if daftar:
        #     # fmus_menu = QMenu(fileName)
        #     # for baris_entry in daftar:
        #     #     fmus_menu.addAction(baris_entry, functools.partial(self.run_fmus_from_file, filePath, baris_entry))
        #     # menu.addMenu(fmus_menu)
        #     # # fmus/mk => vscode
        #     # vscode_menu = QMenu(f"{fileName} => vscode")
        #     # vscode_menu.addAction('Global snippet here', lambda: self.vscode_global(filePath))
        #     # # vscode_menu.addAction('Global snippet here', self.vscode_global)
        #     # for lang in vscode_language_identifiers:
        #     #     vscode_menu.addAction(f"Language snippet {lang}", lambda: self.vscode_local(filePath, lang))
        #     # menu.addMenu(vscode_menu)
        #     print(f'{filePath} punya daftar:', daftar)
        # else:
        #     print(f'{filePath} NO punya daftar')

        # vscode_menu = QMenu(f"{fileName} => vscode", menu)
        # vscode_menu.addAction('Global snippet here', lambda: self.vscode_global(filePath))
        # menu.addMenu(vscode_menu)
        menu.addAction('Global snippet here', lambda: self.vscode_global(filePath))
        return menu

    # @functools.lru_cache(maxsize=128)
    def mkmenu_from_dir(self, basedir, ttl_cache=None):
        """
        utamanya utk dir kenza
        tiap mk jadi entry menu item
        """
        menu = QMenu(os.path.basename(basedir), self)
        menu.setIcon(QApplication.style().standardIcon(QStyle.SP_DirIcon))
        daftar_semua = os.listdir(basedir)
        a = list(filter(lambda x: os.path.isfile(os.path.join(basedir, x)), daftar_semua))
        b = list(filter(lambda x: os.path.isdir(os.path.join(basedir, x)), daftar_semua))
        for item in b+a:  # dir first
            lengkap = os.path.join(basedir, item)
            if os.path.isdir(lengkap):
                childmenu = self.mkmenu_from_dir(lengkap)
                if childmenu:
                    menu.addMenu(childmenu)
            else:
                # menu.addAction(item)
                if not item.endswith('.mk') and not item.endswith('.fmus'):
                    target = self.context_menu.property('filepath')
                    if os.path.isfile(target):
                        target = os.path.dirname(target)
                    menu.addAction(item, functools.partial(self.salin_file, lengkap, target))
                else:
                    menu.addMenu(self.mkmenu_handle_file(lengkap, item))

        menu.addAction('Reload', self.reload_kenza_menu)
        return menu

    def reload_kenza_menu(self):
        self.kenza_menu = self.mkmenu_from_dir(kenzadir, ttl_cache=time.time())

    def salin_file(self, sumber, target):
        if os.path.isfile(target):
            target = os.path.dirname(target)
        shutil.copy2(sumber, target)
        print(f"copy file from {sumber} to {target}")
