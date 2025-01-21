
import functools
import os, random, string, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *
import decimal, datetime

envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
schnelldir = os.environ['ULIBPY_BASEDIR']
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
sys.path.extend([sidoarjodir, schnelldir])

from schnell.gui.system.searcher.widgets.common import get_icon, set_theme
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
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
from schnell.app.utils import env_get

from faker import Faker
palsu = Faker()
excludes = [
    'add_provider', 'binary', 'cache_pattern',
    'del_arguments',
    'factories', 'format',
    'get_arguments',
    'get_formatter',
    'get_formatters',
    'get_providers',
    'generator_attrs',
    'locales',
    'parse',
    'provider',
    'providers',
    'pytimezone',
    'random',
    'seed', 'seed_instance', 'seed_locale',
    'set_arguments', 'set_formatter',
    'tar',
    'time_series', # generator
    'unique',
    'weights',
    'zip',
]
palsu_contents = [i for i in dir(palsu) if not i.startswith('_') and not i in excludes]

overridden_functions = {
    # https://faker.readthedocs.io/en/master/providers/faker.providers.lorem.html
    'paragraph': [
        {'label': '()', 'func': lambda: palsu.paragraph()},
        {'label': '(nb_sentences=5)', 'func': lambda: palsu.paragraph(nb_sentences=5)},
        {'label': '(nb_sentences=10)', 'func': lambda: palsu.paragraph(nb_sentences=5)},
    ],
    'paragraphs': [
        {'label': '()', 'func': lambda: palsu.paragraphs()},
        {'label': '(nb=5)', 'func': lambda: palsu.paragraphs()},
        {'label': '(nb=10)', 'func': lambda: palsu.paragraphs()},
    ],
    'sentence': [
        {'label': '()', 'func': lambda: palsu.sentence()},
        {'label': '(nb_words=10)', 'func': lambda: palsu.sentence(nb_words=10)},
    ],
    'sentences': [
        {'label': '()', 'func': lambda: palsu.sentences()},
        {'label': '(nb=5)', 'func': lambda: palsu.sentences(nb=5)},
        {'label': '(nb=10)', 'func': lambda: palsu.sentences(nb=10)},
    ],
    'text': [
        {'label': '()', 'func': lambda: palsu.text()},
        {'label': '(max_nb_chars=500)', 'func': lambda: palsu.text(max_nb_chars=500)},
    ],
    'texts': [
        {'label': '()', 'func': lambda: palsu.texts()},
        {'label': '(nb_texts=5)', 'func': lambda: palsu.texts(nb_texts=5)},
    ],
    # 'word': [
    #     {'label': '()', 'func': lambda: palsu.word()},
    # ],
    'words': [
        {'label': '()', 'func': lambda: palsu.words()},
        {'label': '(nb=5)', 'func': lambda: palsu.words(nb=5)},
    ],
    # https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html    
    'password': [
        {'label': '()', 'func': lambda: palsu.password()},
        {'label': '(length=40)', 'func': lambda: palsu.password(length=40)},
    ],
    # https://faker.readthedocs.io/en/master/providers/faker.providers.python.html
    'pyint': [
        {'label': '()', 'func': lambda: palsu.pyint()},
        {'label': '(min_value=0,max_value=100)', 'func': lambda: palsu.pyint(min_value=0,max_value=100)},
        {'label': '(min_value=0,max_value=100,step=5)', 'func': lambda: palsu.pyint(min_value=0,max_value=100,step=5)},
        {'label': '(min_value=0,max_value=50)', 'func': lambda: palsu.pyint(min_value=0,max_value=50)},
        {'label': '(min_value=10,max_value=50)', 'func': lambda: palsu.pyint(min_value=10,max_value=50)},
        {'label': '(min_value=-100,max_value=100)', 'func': lambda: palsu.pyint(min_value=-100,max_value=100)},
    ],
    'pylist': [
        {'label': '()', 'func': lambda: palsu.pylist()},
        {'label': '(nb_elements=5)', 'func': lambda: palsu.pylist(nb_elements=5)},
        {'label': '(variable_nb_elements=True)', 'func': lambda: palsu.pylist(variable_nb_elements=True)},
        {'label': '(value_types=[int])', 'func': lambda: palsu.pylist(value_types=[int])},
    ],
}


class FakerlangWidget(QWidget):

    change_radio = pyqtSignal(str)
    repl_result = pyqtSignal(str)
    # faker_result = pyqtSignal(str)

    def change_orientation(self):
        orient = self.changeable_splitter.orientation()
        # print(orient, Qt.Horizontal, Qt.Vertical)
        if orient == Qt.Horizontal:
            self.changeable_splitter.setOrientation(Qt.Vertical)
        else:
            self.changeable_splitter.setOrientation(Qt.Horizontal)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.combo_faker_functions = QComboBox(self)
        # self.combo_faker_functions.addItems(['satu', 'dua', 'tiga', 'empat', 'lima'])
        self.combo_faker_functions.addItems(palsu_contents)
        self.combo_faker_functions.currentTextChanged.connect(self.change_bahasa)
        self.change_orient_button = QPushButton('Toggle H/V')
        self.change_orient_button.clicked.connect(self.change_orientation)
        self.output_as_list = QCheckBox('Output as list')
        self.output_as_list.setChecked(False)
        self.jumlah = QSpinBox()
        self.jumlah.setRange(1, 100)
        self.jumlah.setValue(5)
        self.jumlah.setStyleSheet('background-color: cornsilk; min-width: 50px;')
        jumlah_label = QLabel(str(self.jumlah.value()))
        jumlah_label.setStyleSheet('background-color: cornsilk; min-width: 50px;')
        self.jumlah.valueChanged.connect(lambda val: jumlah_label.setText(str(val)))
        jumlah_layout = QHBoxLayout()
        jumlah_layout.addWidget(jumlah_label)
        jumlah_layout.addWidget(self.jumlah)
        jumlah_group = QGroupBox('Jumlah')
        jumlah_group.setLayout(jumlah_layout)
        self.flow_bahasa = FlowWidget()
        self.flow_bahasa.add_item(self.combo_faker_functions)
        self.flow_bahasa.add_item(self.change_orient_button)
        self.flow_bahasa.add_item(self.output_as_list)
        self.flow_bahasa.add_item(jumlah_group)
        self.flow_bahasa.setStyleSheet("""
QPushButton {
    font-family: Verdana;
    font-size: 17px;
    padding: 10px;
    margin: 5px;
}
QComboBox {
    font-family: Verdana;
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
        # self.change_bahasa(self.combo_faker_functions.currentText())
        # self.change_radio.connect(lambda bhs: self.combo_faker_functions.setCurrentText (bhs))
        self.important_buttons = []
        self.init_buttons()
        for b in self.important_buttons:
            self.flow_bahasa.add_item(b)

        self.editor = EditorStandard(self)
        self.repl_result.connect(lambda result: self.editor.setText(result))

        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.addWidget(self.flow_bahasa)
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

        # self.resize(800, 600)
        self.setWindowTitle('Fakerlang')
        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # self.show()

    def init_buttons(self):
        widgets = []
        for keyword in palsu_contents:
            # menu = self.generate_menu(keyword)
            b = QPushButton(keyword)
            b.setProperty('info', keyword)
            if keyword in overridden_functions:
                faker_menu = QMenu()
                for kv in overridden_functions[keyword]:
                    faker_menu.addAction(kv['label'], functools.partial(self.faker_by_menu_action, kv['func']))
                b.setMenu(faker_menu)
                self.important_buttons.append(b)
            else:
                b.clicked.connect(functools.partial(self.change_bahasa_by_button, b.property('info')))
            widgets.append(b)
        self.flower.clear_add_items(widgets)


    def faker_by_menu_action(self, function):
        total = []
        for i in range(self.jumlah.value()):
            result = function()
            if not isinstance(result, (str)):
                result = str(result)
            total.append(result)
        if self.output_as_list.isChecked():
            result = '[' + ', '.join(total) + ']'
        else:
            output_delimiter_non_list = '\n'
            result = output_delimiter_non_list.join(total)
        self.repl_result.emit(result)


    def change_bahasa_by_button(self, bhs):
        self.combo_faker_functions.setCurrentText(bhs)
        total = []
        for i in range(self.jumlah.value()):
            result = getattr(palsu, bhs)()
            # print(bhs, '=>', result, 'sender:', type(self.sender()))
            # if isinstance(result, bytes):
            #     result = str(result)
            # elif isinstance(result, bool):
            #     result = str(result)
            # elif isinstance(result, (int, float)):
            #     result = str(result)
            # elif isinstance(result, decimal.Decimal):
            #     result = str(result)
            # elif isinstance(result, (tuple, list, dict, set)):
            #     result = str(result)
            # # elif isinstance(result, tzfile): # pytimezone
            # #     result = str(result)
            # elif isinstance(result, (datetime.date, datetime.time, datetime.datetime, datetime.timedelta)):
            #     result = str(result)
            if not isinstance(result, (str)):
                result = str(result)
            total.append(result)
        if self.output_as_list.isChecked():
            result = '[' + ', '.join(total) + ']'
        else:
            output_delimiter_non_list = '\n'
            result = output_delimiter_non_list.join(total)
        self.repl_result.emit(result)

    def change_bahasa(self, bhs):
        total = []
        for i in range(self.jumlah.value()):
            result = getattr(palsu, bhs)()
            # print(bhs, '=>', result, 'sender:', type(self.sender()))
            # if isinstance(result, bytes):
            #     result = str(result)
            # elif isinstance(result, bool):
            #     result = str(result)
            # elif isinstance(result, (int, float)):
            #     result = str(result)
            # elif isinstance(result, decimal.Decimal):
            #     result = str(result)
            # elif isinstance(result, (tuple, list, dict, set)):
            #     result = str(result)
            # elif isinstance(result, (datetime.date, datetime.time, datetime.datetime, datetime.timedelta)):
            #     result = str(result)
            if not isinstance(result, (str)):
                result = str(result)
            total.append(result)
        output_delimiter_non_list = '\n'
        result = output_delimiter_non_list.join(total)
        self.repl_result.emit(result)


background_image_stylesheet = '''
FakerlangWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    ex = FakerlangWidget()
    ex.setStyleSheet(background_image_stylesheet)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
