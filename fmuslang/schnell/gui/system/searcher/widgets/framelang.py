
import functools
import os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# bylangsdir = os.environ['ULIBPY_BYLANGSDIR']
# sys.path.extend([sidoarjodir, schnelldir])
import sys
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

from constants import sidoarjodir, bylangsdir
from schnell.app.dirutils import files, dirs, joiner
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
from schnell.app.utils import env_get
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import get_icon, set_theme
from schnell.gui.system.searcher.widgets.config import bahasa
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard


repl_keywords = []


class FramelangWidget(QWidget):

    change_radio = pyqtSignal(str)
    repl_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.initUI()

    def radio_toggle_handler(self, value):
        # print(f"""
        # group:
        # group checked id {self.radio_group.checkedId()}
        # group checked button {self.radio_group.checkedButton()}
        # group buttons {self.radio_group.buttons()}
        # radio tercek berdasarkan group = {self.radio_group.checkedButton().text()}
        # """)
        newbahasa = self.radio_group.checkedButton().text()
        self.change_radio.emit(newbahasa)

    def edit_last_file(self):
        from schnell.app.utils import edit_entry
        edit_entry(self.last_file, self.lineno)

    def initUI(self):

        self.main_layout = QVBoxLayout()

        self.langchoice = QComboBox(self)
        # self.langchoice.addItems(['satu', 'dua', 'tiga', 'empat', 'lima'])
        self.langchoice.addItems(bahasa)
        self.langchoice.currentTextChanged.connect(self.change_bahasa)
        # self.langchoice.currentIndexChanged.connect(self.change_bahasa)
        # self.langchoice.textChanged.connect(lambda value: print(value))
        self.f12 = QPushButton("f12")
        self.f12.setStyleSheet('background-color: blanchedalmond; color: indigo; font-size: 18px;')
        self.f12.clicked.connect(self.edit_last_file)
        self.flow_bahasa = FlowWidget()
        self.flow_bahasa.add_item(self.langchoice)
        self.flow_bahasa.setStyleSheet("""
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
QComboBox {
    font-family: Verdana, Consolas;
    font-size: 17px;
    padding: 10px;
}
        """)
        self.lineno = -1
        self.last_file = None
        self.bylangsdir = env_get('ULIBPY_BYLANGSDIR')
        self.radios = []
        self.radio_group = QButtonGroup(self)
        for i,bhs in enumerate(bahasa,1):
            # if i == 0:
            #     radio.setChecked(True)
            radio = QRadioButton(bhs)
            radio.toggled.connect(self.radio_toggle_handler)
            self.radios.append(radio)
            self.radio_group.addButton(radio, i)
            self.flow_bahasa.add_item(radio)
        self.flow_bahasa.add_item(self.f12)
        self.radios[0].setChecked(True)
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
        self.change_bahasa(self.langchoice.currentText())
        self.change_radio.connect(lambda bhs: self.langchoice.setCurrentText (bhs))

        self.editor = EditorStandard(self)
        self.repl_result.connect(lambda result: self.editor.setText(result))

        # self.main_layout.addWidget(self.flow_bahasa, 1)
        # self.main_layout.addWidget(self.flower, 2)
        # self.main_layout.addWidget(self.editor, 7)

        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.addWidget(self.flow_bahasa)
        self.main_splitter.addWidget(self.flower)
        self.main_splitter.addWidget(self.editor)
        self.main_splitter.setHandleWidth(8)
        self.main_splitter.handle(1).setStyleSheet('background: 3px blue;')
        self.main_splitter.handle(2).setStyleSheet('background: 3px blue;')

        self.main_splitter.setStretchFactor(0, 1)
        self.main_splitter.setStretchFactor(1, 2)
        self.main_splitter.setStretchFactor(2, 7)
        self.main_layout.addWidget(self.main_splitter)

        self.setLayout(self.main_layout)
        self.setWindowTitle('Replang')

    def change_bahasa(self, bhs):
        # repl_keywords adlh daftar files dlm direktori bhs (devops, django, dsb)
        repl_keywords = files(joiner(bylangsdir, bhs))
        widgets = []
        for keyword in repl_keywords:
            menu = self.generate_menu(keyword)
            # action diambil dari property 'info' button, jangan dari text nya
            b = QPushButton(keyword.removesuffix('.mk'))
            b.setMenu(menu)
            b.setProperty('info', keyword)
            menu.setProperty('button', b)
            widgets.append(b)
        self.flower.clear_add_items(widgets)

    def generate_menu(self, keyword):
        menu = QMenu(keyword) # menu title dan button text kita bikin sama
        bhs = self.langchoice.currentText()
        # # 4/12/23 kita matikan dulu yg akses redis
        # from schnell.app.redisutils import search_keys_cached, search_bongkar
        # name = f'{bhs}\\{keyword}'
        # daftar_filepath_baris_entry = search_bongkar(f'ULIBPY_BYLANGSDIR\\{name}*')
        # daftar_baris_entry = []
        # for item in daftar_filepath_baris_entry:
        #     names = item.split('mk:')
        #     name = names[1]
        #     daftar_baris_entry.append(name)
        # for name in sorted(daftar_baris_entry):
        #     menu.addAction(get_icon(), name, self.handle_menu_action)
        return menu

    def handle_menu_action(self):
        """
        action triggered
            pengirim: CIP class init pass
            menu = class
            button = class
            bhs = py        
        """
        pengirim = self.sender()
        menu = pengirim.parent()
        button = menu.property('button')
        # print(f"""action triggered
        # pengirim: {pengirim.text()}
        # menu = {menu.title()}
        # button = {button.text()}
        # bhs = {self.langchoice.currentText()}
        # """)
        baris_entry = pengirim.text()
        # keyword = button.text()
        keyword = button.property('info')
        bhs = self.langchoice.currentText()
        # self.last_file = os.path.join(self.bylangsdir, f'{keyword}.{bhs}.mk')
        self.last_file = os.path.join(self.bylangsdir, bhs, keyword)
        try:
            result, self.lineno = get_definition_by_key_permissive_start_with_lineno(self.last_file, baris_entry)
            result = result.strip()
            self.repl_result.emit(result)
        except Exception as err:
            print(err)



background_image_stylesheet = '''
FramelangWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    w = FramelangWidget()
    w.setStyleSheet(background_image_stylesheet)
    w.resize(1200, 800)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
