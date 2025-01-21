import os, random, string, sys, functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.Qsci import *

from schnell.app.dirutils import isfile

envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
bylangsdir = os.environ['ULIBPY_BYLANGSDIR']
sys.path.extend([sidoarjodir, schnelldir])
from schnell.app.fmusutils import run_fmus_for_content_in_thread
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import (
    get_icon,
    set_theme,
    screensize,
    standard_dahsyat_model,
    context_menu_for_dahsyat_with_entries,
    context_menu_stylesheet,
)

from schnell.app.fileutils import (
    content_length, file_length, line_number_expression,
    get_daftar,
    get_definition_by_key_permissive_start,
    get_definition_double_entry_aware,
)
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.app.fmusutils import run_fmus_for_file, run_fmus_for_content, run_fmus_for_file_in_folder_in_thread


class DashsyatMenu(QMenu):


    def __init__(self, filePath, title='', parent=None):
        super().__init__(parent=parent)
        # self.setStyleSheet(context_menu_stylesheet)
        self.screenw, self.screenh = screensize()
        self.setTitle(title)
        # self.createActions()
        self.create_providers_menu(filePath)
        self.createTopAction()


    def createTopAction(self):
        self.widget = QWidget(self)
        self.layout = QVBoxLayout()
        # self.widget.setLayout(self.layout)
        self.topAction = QWidgetAction(self)
        self.topAction.setDefaultWidget(self.widget)
        self.editor = EditorStandard(self)
        self.editor.setText(standard_dahsyat_model)
        self.layout.addWidget(self.editor)
        self.footer = QLabel('__________________________________________________________________________________________________________________________________________________________________________')
        self.footer.setStyleSheet('font-family: Consolas;')
        self.layout.addWidget(self.footer)
        slider = QSlider(Qt.Vertical)
        slider.setFixedHeight(self.screenh // 2)
        wrapper = QHBoxLayout()
        wrapper.addLayout(self.layout)
        wrapper.addWidget(slider)
        self.widget.setLayout(wrapper)

        self.addAction(self.topAction)


    def create_providers_menu(self, filePath):
        # menu_provider = QMenu('Providers (files)')
        dirPath = filePath
        if not os.path.isdir(filePath):
            dirPath = os.path.dirname(filePath)
        for mk_filename,v in context_menu_for_dahsyat_with_entries.items():
            filename = os.path.basename(mk_filename).removesuffix('.mk')
            # menu_per_file = QMenu(filename, menu_provider)
            menu_per_file = QMenu(filename, self)
            for entry in v:
                # menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, dirPath, mk_filename, entry))
                menu_per_file.addAction(entry, functools.partial(self.run_fmus_in_directory_in_thread, dirPath, mk_filename, entry))
            # menu_provider.addMenu(menu_per_file)
            self.addMenu(menu_per_file)
        # menu_provider.addAction(get_icon(), 'Reload', lambda: self.reload_context_menu_providers(filePath))
        # self.provider_menu = menu_provider
        # return self.provider_menu


    def run_fmus_in_directory_in_thread(self, targetDir, sourcefilePath, barisEntry):
        # self.showedit.show()
        # self.showedit.quit_signal.connect(lambda content: run_fmus_for_content(content, set_dir=filePath))
        # run_fmus_for_file(filePath, barisEntry)
        print(f"""[fm][run_fmus_in_directory_in_thread]
        targetDir {targetDir}, sourcefilePath [{sourcefilePath}], barisEntry [{barisEntry}]
        """)
        # run_fmus_for_file_in_folder_in_thread(targetDir, sourcefilePath, barisEntry)
        # run_fmus_for_content_in_thread(content, dirpath=tempdir(), filepath=None)
        csvcode = self.editor.text()
        content = get_definition_double_entry_aware(sourcefilePath, barisEntry)
        content = content.replace('__CSVCODE__', csvcode)
        content = ''.join(content.splitlines())  # gabung semua lines
        if csvcode and content:
            if not content.endswith('\n'):
                content += '\n'
            run_fmus_for_content_in_thread(content, dirpath=targetDir, filepath=None)
