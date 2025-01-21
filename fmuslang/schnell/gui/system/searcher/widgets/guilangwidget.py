from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

import sys, functools
# import os, shutil, threading, pyperclip

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# rootdir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([rootdir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

from constants import sidoarjodir, bylangsdir
if __name__ == '__main__':
    from startup import initialize_programming_data
    initialize_programming_data()
from schnell.app.executor import FileExecutor
from schnell.app.wcmderutils import (
    getlist, button_ketik_handler, operate_on_windows, to_top,
    create_fill_set, fill_set,
    create_fill_set_with_id_index,
    ketik_by_hwnd, ketik_by_index,
    get_items_for_combo,
    hapus_set_combo_items,
    data_for_item,
    is_window_visible,
    operate_on_windows_by_hwnd,
    to_top_by_hwnd,
    get_last_console_data,
)
from schnell.app.utils import env_get
from schnell.app.dirutils import normy, explore, joiner, files_filter
from schnell.app.fileutils import get_daftar, get_definition_by_key_permissive_start, file_content, not_binary, get_extension
from schnell.app.fmusutils import run_fmus_for_file, run_fmus_for_content, run_fmus_for_file_in_folder_in_thread
from schnell.app.systemutils import execute_command_in_dir, execute_command_in_dir_in_thread
from schnell.app.vscodeutils import create_snippet_wrapper
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.gui.system.searcher.widgets.common import get_icon, BlueButton
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
)
from schnell.gui.system.searcher.widgets.colorwidget import ColorWidget
from schnell.gui.system.searcher.widgets.buttonwidget import ButtonWidget
from schnell.gui.system.searcher.widgets.tkeditor import tkeditor
from schnell.gui.system.searcher.widgets.windower import WindowerWidget
from schnell.gui.system.searcher.widgets.lalangwidget import LalangWidget
from schnell.gui.system.searcher.widgets.showedit import ShowEditWindow
from schnell.gui.system.searcher.widgets.packagewidget import PackageWidget
from schnell.gui.system.searcher.widgets.creator import CreatorWidget
from schnell.gui.system.searcher.widgets.quickviewer import QuickViewerWidget
from schnell.gui.system.searcher.widgets.filemanip import filemanip

from schnell.gui.system.searcher.widgets.config import preset_directories
from schnell.gui.system.searcher.widgets.fmdata import guilang_items, fmdata
from schnell.app.quick.languages.guilang import guilang


guilang_button_styleshet = """
QPushButton {
    font-family: Verdana;
    font-size: 14pt;
    border-radius: 3px;
    background-color: darkorange;
    border: 1px solid darkblue;
    padding: 5px;
    margin: 2px;
}
QPushButton:hover {
    background-color: beige;
}
"""



class ExecutorThread(QThread):
    def __init__(self, program=None):
        super(ExecutorThread, self).__init__()
        if program:
            self.program = program
    def set_program(self, program):
        self.program = program
    def run(self):
        FileExecutor().exec(self.program)



class GuilangWidget(QWidget):

    buttonData = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def create_button_menu(self, menu_list):
        menu = QMenu('Button Menu')
        for item in menu_list:
            # item adlh dict label: content, label utk tampil di menu, content utk diinsert di editor
            # menu.addAction(get_icon(), item['label'], lambda: self.buttonData.emit(item['content']))
            menu.addAction(get_icon(), item['label'], functools.partial(self.buttonData.emit, item['content']))
            # self.buttonData.emit, data
        return menu

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.setHandleWidth(8)

        self.flow_buttons = FlowWidget()
        widgets = []
        for item in guilang_items:
            b = QPushButton(item)
            b.setStyleSheet(guilang_button_styleshet)
            if item in fmdata:
                data = fmdata[item]
                if isinstance(data, list):
                    menu = self.create_button_menu(data)
                    b.setMenu(menu)
                else:
                    b.clicked.connect(functools.partial(self.buttonData.emit, data))
            widgets.append(b)
        self.flow_buttons.add_items(widgets)

        editorlayout = QVBoxLayout()

        toolbarlayout = QHBoxLayout()
        toolbarlayout.addStretch(1)
        exec_button = QPushButton("Exec")
        exec_button.clicked.connect(self.execute_guicode)
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_guicode)
        output_button = QPushButton("Output")
        output_button.clicked.connect(self.output_guicode)
        toolbarlayout.addWidget(clear_button)
        toolbarlayout.addWidget(output_button)
        toolbarlayout.addWidget(exec_button)

        self.guicode_editor = EditorStandard(self) # guilang
        self.pyoutput_editor = EditorStandard(self) # py output
        # self.guicode_editor.insertAt()
        self.buttonData.connect(self.guicode_editor_insert_data)
        self.editor_tab = QTabWidget(self, tabPosition=QTabWidget.South)
        self.editor_tab.addTab(self.guicode_editor, 'Gui code')
        self.editor_tab.addTab(self.pyoutput_editor, 'Python')
        editorlayout.addWidget(self.editor_tab)

        editorlayout.addLayout(toolbarlayout)

        # self.main_layout.addWidget(self.flow_buttons, 4)
        # self.main_layout.addLayout(editorlayout, 6)

        editor_wrapper = QWidget()
        editor_wrapper.setLayout(editorlayout)
        self.main_splitter.addWidget(self.flow_buttons)
        self.main_splitter.addWidget(editor_wrapper)
        self.main_layout.addWidget(self.main_splitter)
        self.main_splitter.setStretchFactor(0, 3)
        self.main_splitter.setStretchFactor(1, 7)
        self.main_splitter.handle(1).setStyleSheet('background: 3px blue;')
        self.t = ExecutorThread()
        self.setLayout(self.main_layout)

    def clear_guicode(self):
        self.guicode_editor.setText('')
        self.editor_tab.setCurrentIndex(0)

    def output_guicode(self):
        program = self.guicode_editor.text().strip()
        if program:
            from schnell.app.fileutils import file_write_timestamped_under_rootdir
            result = guilang(program, returning=True)
            self.pyoutput_editor.setText(result)
            self.editor_tab.setCurrentIndex(1)
            # jk crash dll kita punya program terakhir utk troubleshoot
            file_write_timestamped_under_rootdir('result.txt', content=program, foldername='data/guilang-output')

    def execute_guicode(self):
        # guilang
        program = self.guicode_editor.text().strip()
        if program:
            result = guilang(program, returning=True)
            self.pyoutput_editor.setText(result)
            self.editor_tab.setCurrentIndex(1)
            self.t.set_program(program)
            self.t.start()
            # FileExecutor().exec(program)
            # ExecutorThread(program).start()

    def guicode_editor_insert_data(self, text):
        line, index = self.guicode_editor.getCursorPosition()
        self.guicode_editor.insertAt(text, line, index)


background_image_stylesheet = '''
GuilangWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''

def main():
    app = QApplication([])
    w = GuilangWidget()
    w.setStyleSheet(background_image_stylesheet)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
