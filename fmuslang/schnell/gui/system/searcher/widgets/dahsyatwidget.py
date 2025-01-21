# utk dahsyater...

import functools, decimal, datetime
import os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([sidoarjodir, schnelldir])

from schnell.app.redisutils import search_keys_cached, search_bongkar
from schnell.app.fileutils import (
	file_content,
	file_lines,
	line_contains,
	get_definition_by_key_permissive_start,
	get_definition_by_key_permissive_start_with_lineno,
	get_daftar,
	create_if_empty_file,
	ulib_history,
)
# from schnell.app.utils import env_get

from schnell.app.quick.dahsyater import provider_to_location

# palsu_contents = list(provider_to_location.keys()) [::-1]
provider_to_location_keys = sorted(list(provider_to_location.keys()) [::-1])
# dahsyater_project_list = '\n'.join(provider_to_location_keys)

# bisa juga kategori_sumber, misal blog_mexyusef_myblog, blog_someone_project, dsb
from schnell.gui.system.searcher.widgets.config import system_template, system_template_dict
from schnell.gui.system.searcher.widgets.noter import NoteBrowser
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import get_icon, set_theme
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard


class DahsyaterWidget(QWidget):


    # change_radio = pyqtSignal(str)
    repl_result = pyqtSignal(str)
    # faker_result = pyqtSignal(str)


    def change_orientation(self):
        orient = self.changeable_splitter.orientation()
        # print(orient, Qt.Horizontal, Qt.Vertical)
        if orient == Qt.Horizontal:
            self.changeable_splitter.setOrientation(Qt.Vertical)
        else:
            self.changeable_splitter.setOrientation(Qt.Horizontal)


    def change_rootpath(self, rootpath):
        self.rootpath = rootpath
        self.rootpath_label.setText(self.rootpath)


    def generate_dahsyat_internal(self):
        from schnell.app.quick.dahsyater import dahsyater
        import threading
        csvcode = self.editor.text().strip()
        provider = self.dahsyater_project.currentText()
        # change folder
        os.chdir(self.rootpath)
        print(f'Change working dir to {self.rootpath}')
        if csvcode:
            args = provider + '|' + csvcode
        else:
            args = provider
        # biar gak ngehang...
        x = threading.Thread(target=dahsyater, args=(args,))
        x.start()


    def generate_dahsyat(self):
        if not self.rootpath:
            res = QMessageBox.information(None, "No rootpath bruh?", 'Get the hell out of here', QMessageBox.Ok | QMessageBox.Cancel)
            print(f"{res}, ok = {QMessageBox.Ok}, cancel = {QMessageBox.Cancel}")
            return
        else:
            res = QMessageBox.information(None, f"{self.rootpath}", f'Sure to run "{self.dahsyater_project.currentText()}" in {self.rootpath}?', QMessageBox.Ok | QMessageBox.Cancel)
            if res == QMessageBox.Ok:
                self.generate_dahsyat_internal()


    def generate_dahsyater_by_button(self, project):
        # project = self.sender()
        self.dahsyater_project.setCurrentText(project)
        self.generate_dahsyat()


    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.dahsyater_project = QComboBox(self)
        # self.dahsyater_project berisi pilihan project dahsyater
        # self.dahsyater_project.addItems(provider_to_location_keys)
        for i,(k,v) in enumerate(provider_to_location.items()):
            self.dahsyater_project.addItem(k)
            # fungsi = provider_to_location[k]
            lengkap = f"{v.__module__}.{v.__name__}"
            self.dahsyater_project.setItemData(i, lengkap, Qt.ToolTipRole)
        self.dahsyater_project.currentTextChanged.connect(self.change_dahsyater_project)
        self.change_orient_button = QPushButton('Toggle H/V')
        self.change_orient_button.setStyleSheet('background-color: beige; border: 2px solid #73AD21; border-radius: 5px;')
        self.change_orient_button.clicked.connect(self.change_orientation)
        self.rootpath = ''
        self.rootpath_label = QLabel(self.rootpath)
        self.generate = QPushButton('Generate')
        self.generate.setObjectName('generate_button')
        self.generate.clicked.connect(self.generate_dahsyat)
        self.generate.setStyleSheet("""
#generate_button {
    background-color: fuchsia;
    border-radius: 5px;
    border: 1px solid darkblue;
}
#generate_button:hover{ 
    background-color: blueviolet;
    color:lightsalmon; 
}""")
        self.flow_bahasa = FlowWidget()
        # combobox project dahsyater
        self.flow_bahasa.add_item(self.dahsyater_project)
        # toggle h/v button
        self.flow_bahasa.add_item(self.change_orient_button)
        # label rootpath jika terset
        self.flow_bahasa.add_item(self.rootpath_label)
        # generate dahsyater button
        self.flow_bahasa.add_item(self.generate)
        for project in provider_to_location_keys:
            b = QPushButton(project)
            b.setProperty('info', project)
            b.clicked.connect(functools.partial(self.generate_dahsyater_by_button, project))
            # tooltip berdasar nama panjang
            fungsi = provider_to_location[project]
            lengkap = f"{fungsi.__module__}.{fungsi.__name__}"
            b.setToolTip(lengkap)
            b.setStyleSheet("""
QPushButton {
    background-color: wheat;
    border-radius: 5px;
    border: 1px solid darkblue;
}
QPushButton:hover {
    background-color: papayawhip;
}""")
            self.flow_bahasa.add_item(b)
        self.flow_bahasa.setStyleSheet("""
QPushButton {
    font-family: Verdana, Consolas;
    font-size: 17px;
    padding: 10px;
    margin: 5px;
}
QComboBox {
    font-family: Verdana, Consolas;
    font-size: 17px;
    padding: 10px;
}
""")

        self.flower = FlowWidget()
        self.flower.setStyleSheet("""
QPushButton {
    background-color: burlywood;
    font-family: Verdana, Consolas;
    font-size: 16px;
    padding: 10px;
    margin: 5px;
    border-radius: 2px;
}
QPushButton:hover {
    background-color: cornsilk;
}
""")
        # self.change_dahsyater_project(self.dahsyater_project.currentText())
        # self.change_radio.connect(lambda bhs: self.dahsyater_project.setCurrentText (bhs))
        self.init_buttons()

        self.editor = EditorStandard(self)
        self.repl_result.connect(lambda result: self.editor.setText(result))

        # add: wrap self.flow_bahasa menjadi self.flow_bahasa + notebrowser
        # NoteBrowser menggunakan content default dari dahsyater code
        self.dahsyater_help_note = NoteBrowser()
        flow_plus_note = QGroupBox('Pilih proyek')
        flow_plus_note_layout = QHBoxLayout()
        flow_plus_note.setLayout(flow_plus_note_layout)
        flow_plus_note_layout.addWidget(self.flow_bahasa)
        flow_plus_note_layout.addWidget(self.dahsyater_help_note)
        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.addWidget(flow_plus_note)
        # self.flower dan self.editor bisa H atau V
        self.changeable_splitter = QSplitter(Qt.Horizontal)
        self.changeable_splitter.addWidget(self.flower)
        self.changeable_splitter.addWidget(self.editor)
        self.main_splitter.addWidget(self.changeable_splitter)
        self.main_splitter.setHandleWidth(8)
        self.changeable_splitter.setHandleWidth(8)
        self.main_splitter.handle(1).setStyleSheet('background: 3px blue;')
        self.changeable_splitter.handle(1).setStyleSheet('background: 3px red;')

        self.main_splitter.setStretchFactor(0, 1)
        self.main_splitter.setStretchFactor(1, 2)
        self.main_splitter.setStretchFactor(2, 7)
        self.main_layout.addWidget(self.main_splitter)

        self.setLayout(self.main_layout)

        self.setWindowTitle('Dahsyater')
        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())

    def init_buttons(self):
        widgets = []
        for keyword in system_template:
            # menu = self.generate_menu(keyword)
            b = QPushButton(keyword)
            b.setProperty('info', keyword)
            # b.clicked.connect(functools.partial(self.change_dahsyater_project, b.property('info')))
            b.clicked.connect(functools.partial(self.change_system_template, b.property('info')))
            widgets.append(b)
        self.flower.clear_add_items(widgets)


    def change_system_template(self, bhs):
        # print('masukkan system template', bhs)
        data = system_template_dict[bhs]
        self.editor.setText(data)


    def change_dahsyater_project(self, bhs):
        print('do something specific to dahsyater', bhs)


background_image_stylesheet = '''
DahsyaterWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    ex = DahsyaterWidget()
    ex.setStyleSheet(background_image_stylesheet)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
