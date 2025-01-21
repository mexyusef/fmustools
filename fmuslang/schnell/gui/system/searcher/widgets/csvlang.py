
import math, os, random, string, sys, functools
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

from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.gui.system.searcher.widgets.common import get_icon, set_theme, sample_data_csvlang, csvmodels_toc, sample_data_dahsyat_tables, standard_dahsyat_toc
from schnell.app.dirutils import joiner, joinhere
from schnell.app.fileutils import get_daftar, get_definition_by_key_permissive_start, file_content
from schnell.gui.system.searcher.widgets.noter import NoteBrowser


csvlang_types = [
    'string',
    'text',
    'varchar',
    'integer',
    'number', 'auto', 'bigint', 'float', 'double', 'decimal', 'boolean', 'date', 'timestamp', 'enum', 'serial', 'slug', 'image', 'blob', 'django_foreign_key', 'django_one_to_one', 'django_one_to_many', 'django_many_to_many', 'array_of', 'empty_array', 'json', 'jsonb', 'url',
    'uuid',
    'uuidv1',
    'uuidv4',
]

type_subtype_map = {
    'string': [
        '',
        'name',
        'first_name',
        'last_name',
        'email',
        'name_female',
        'name_male',
        'password',
        'bcrypt_value',
        'simple_profile',
        'city',
        'country',
        'color_name',
        'job',
        'company',
        'address',
        'user_agent',
        'text',
        'word',
        'words',
        'sentence',
        'language_name',
        'locale',
        'phone_number',
        'country_calling_code',
        'credit_card_number',
        'credit_card_full',
        'msisdn',
        'ssn',
    ],
    'text': [],
    'varchar': [],
    'integer': [],
    'number': [
        'random_number',
        'random_int',
        'random_digit',
        'pyfloat',
        'pydecimal',
        'pyint',
        'pybool',
        'i128',
        'i64',
        'i32',
        'i16',
        'i8',
        'u128',
        'u64',
        'u32',
        'u16',
        'u8',
        'phone_number',
        'country_calling_code',
        'credit_card_number',
        'credit_card_full',
        'msisdn',
        'ssn',
        'coordinate',
        'latitude',
        'longitude',
        'latlng',
        'local_latlng',
        'location_on_land',
    ],
    'auto': [],
    'bigint': [],
    'float': [],
    'double': [],
    'decimal': [],
    'boolean': [],
    'date': [
        '',
        'date',
        'time',
        'date_time',
        'iso8601',
        'unix_time',
        'simple_profile',
        'date_time_between',
    ],
    'timestamp': [],
    'enum': [],
    'serial': [],
    'slug': [],
    'image': [],
    'blob': [],
    'django_foreign_key': [],
    'django_one_to_one': [],
    'django_one_to_many': [],
    'django_many_to_many': [],
    'array_of': [],
    'empty_array': [],
    # 'json': [],
    # 'jsonb': [],
    'url': [],
    'uuid': [],
    # 'uuidv1': [],
    # 'uuidv4': [],
}


csvgen_items = {
    'mongoose': 'mg', 
    'sequelize': 'sqlz', 
    'sql_postgres': 'pg',
    'sql_mssql': 'ms',
    'sql_mysql': 'my',
    'sql_sqlite': 'sqlt',
    'nest_typeorm': 'torm',
    'nest_mongoose': 'mg2',
    'prisma': 'pris',
    'hibernate': 'hbr',
    'mybatis': 'bts',
    'struct_go': 'go',
    'struct_rs': 'rs',
    'struct_kt': 'kt',
    'struct_ts': 'ts',
    'struct_java': 'java',
    'django_orm': 'dj',
    'be_flask': 'fl',
    'be_fastapi': 'fa',
    'help_nest_mongo': 'nsm',
    'help_nest_postgres': 'nsp',
    'json1': 'json1',
    'json2': 'json2',
    'csv': 'csv',
}


class CsvlangWidget(QWidget):

    def reload_sample(self):
        global sample_data_csvlang, csvmodels_toc, csvmodels_sourcefile
        # toc = get_daftar(sourcefile)
        # sample_data_csvlang = dict(zip(toc, [get_definition_by_key_permissive_start(sourcefile, item) for item in toc]))
        csvmodels_toc = get_daftar(csvmodels_sourcefile)
        sample_data_csvlang = dict(zip(csvmodels_toc, [get_definition_by_key_permissive_start(csvmodels_sourcefile, item) for item in csvmodels_toc]))

        self.combo_datasample.clear()
        self.combo_datasample.addItems(sample_data_csvlang)

    def ganti_types(self, nilai):
        pengunci = self.combo_types.currentText()
        self.combo_subtypes.clear()
        if pengunci in type_subtype_map:
            if type_subtype_map[pengunci]:
                self.combo_subtypes.addItems(type_subtype_map[pengunci])

    def ganti_sample(self, nilai):
        table = self.combo_datasample.currentText()
        if table: # wkt reload bisa kosong, krn diclear()
            kata = sample_data_csvlang[table]
            self.editor_input.append(kata + '\n\n')

    def ganti_sample2(self, nilai):
        table = self.combo_tablesample.currentText()
        if table: # wkt reload bisa kosong, krn diclear()
            kata = sample_data_dahsyat_tables[table]
            self.editor_input.append(kata + '\n\n')

    def generate_csv(self):
        program = self.editor_input.text().strip()
        provider = self.csvgen_combo.currentText()
        
        if program and provider in csvgen_items.keys():
            '''
            mungkin ini csv yg salah...
            schnell.langs.ucsv.processor.py
            schnell.langs.ucsv.grammar.grammar.py
            (bandingkan: schnell.app.transpiler.mycsv.csv_operation.py)
            digunakan di schnell.app.fmusutils.py
            def get_rootnode(program):
                return schnell.langs.ucsv.processor.process_language(program, print)
            tapi ini kembalikan RootNode alih2 string atau list.
            '''
            from schnell.app.transpiler.mycsv.main import process_language
            provider_ = csvgen_items[provider]
            program_ = f"{provider_}/{program}"
            print('[searcher.widgets.csvlang][generate_csv] program:', program_)
            try:
                result = process_language(program_, returning=True)
            except Exception as err:
                print(err)
                result = f'Gagal: {err}'
            if result:
                self.editor_output.append(result + '\n\n')
            else:
                self.editor_output.append('No result found, check errors.')

    def __init__(self):
        super().__init__()
        self.initUI()

        self.setStyleSheet("""
* {
    background-color: tan;
}
QPushButton {
    font-family: Verdana, Consolas;
    font-size: 17px;
    padding: 10px;
    margin: 5px;
}
QPushButton:hover {
    background-color: papayawhip;
}
QComboBox {
    font-family: Verdana, Consolas;
    font-size: 17px;
    padding: 10px;
}
""")

    def initUI(self):

        self.main_layout = QVBoxLayout()
        self.main_splitter = QSplitter(Qt.Horizontal)

        # page input
        split0_page_0 = QWidget(self)
        split0_pagelayout_0 = QVBoxLayout(split0_page_0)
        inputlayout = QVBoxLayout()
        # combo sample provider
        data_label = QLabel('refcards/models:')
        self.combo_datasample = QComboBox(self)
        self.combo_datasample.addItems(list(sample_data_csvlang.keys()))
        self.combo_datasample.currentTextChanged.connect(self.ganti_sample)
        data_label.setBuddy(self.combo_datasample)
        self.load_sample = QPushButton('Reload')
        self.load_sample.clicked.connect(self.reload_sample)
        # pane 1, top berisi: Sample table: <Todo> (Reload)
        data2_label = QLabel('providers/models/tables:')
        self.combo_tablesample = QComboBox(self)
        self.combo_tablesample.addItems(list(sample_data_dahsyat_tables.keys()))
        self.combo_tablesample.currentTextChanged.connect(self.ganti_sample2)
        label_combo_hlayout = QHBoxLayout()
        label_combo_hlayout.addWidget(data_label)
        label_combo_hlayout.addWidget(self.combo_datasample)
        label_combo_hlayout.addWidget(self.load_sample)
        label_combo_hlayout.addWidget(data2_label)
        label_combo_hlayout.addWidget(self.combo_tablesample)
        label_combo_hlayout.addStretch(1)
        inputlayout.addLayout(label_combo_hlayout)
        # buttons: <mongoose> (generate) (clear) (create)
        inputtoolbarlayout = QHBoxLayout()
        csvgen_layout = QHBoxLayout()
        self.csvgen_combo = QComboBox(self)
        self.csvgen_combo.addItems(list(csvgen_items.keys()))
        self.csvgen_combo.currentTextChanged.connect(lambda value: print(value))
        csvgen_layout.addWidget(self.csvgen_combo)
        csvgen_button = QPushButton("generate")
        csvgen_button.clicked.connect(self.generate_csv)
        csvgen_layout.addWidget(csvgen_button)
        inputtoolbarlayout.addLayout(csvgen_layout)
        inputtoolbarlayout.addStretch(1)
        
        self.button_helper_choose = QPushButton("helper")
        button_helper_menu = QMenu(self)
        self.button_helper_choose.setMenu(button_helper_menu)
        inputtoolbarlayout.addWidget(self.button_helper_choose)
        # lengkapi button_helper_menu stlh dapatkan jumlah stack pada helper

        self.button_input_clear = QPushButton("clear")
        self.button_input_clear.clicked.connect(lambda: self.editor_input.clear())
        inputtoolbarlayout.addWidget(self.button_input_clear)
        self.button_input_create = QPushButton("create")
        self.button_input_create.clicked.connect(lambda: print('create'))
        inputtoolbarlayout.addWidget(self.button_input_create)
        inputlayout.addLayout(inputtoolbarlayout)
        # input editor (the real deal)
        self.editor_input = EditorStandard(self)
        inputlayout.addWidget(self.editor_input)
        split0_pagelayout_0.addLayout(inputlayout)                
        self.main_splitter.addWidget(split0_page_0)        
        # page output (editor di tengah terlalu ramping)
        output_widget_wrapper = QWidget(self)
        output_widget_layout = QVBoxLayout(output_widget_wrapper)
        self.editor_output = EditorStandard(self)
        output_widget_layout.addWidget(self.editor_output)
        # page helper, vbox berisi: combo type+subtype, form layout, plainedit = self.helper_output
        helper_wrapper_widget = QWidget(self)
        helper_wrapper_layout = QVBoxLayout(helper_wrapper_widget)
        helperlayout = QVBoxLayout()
        combolayout = QHBoxLayout()
        self.combo_types = QComboBox(self)
        self.combo_types.addItems(csvlang_types)
        self.combo_types.currentTextChanged.connect(self.ganti_types)
        # self.combo_types.currentIndexChanged.connect(lambda index: print(index))
        # self.combo_types.textChanged.connect(lambda value: print(value))
        combolayout.addWidget(self.combo_types)
        self.combo_subtypes = QComboBox(self)
        self.combo_subtypes.addItems([])
        self.combo_subtypes.currentTextChanged.connect(lambda value: print(value))
        # self.combo_subtypes.currentIndexChanged.connect(lambda index: print(index))
        # self.combo_subtypes.textChanged.connect(lambda value: print(value))
        combolayout.addWidget(self.combo_subtypes)
        helperlayout.addLayout(combolayout)
        self.ganti_types(None) # initialize subtypes di awal
        helper_wrapper_layout.addLayout(helperlayout)
        group1 = QGroupBox("Table constraints")
        layout_for_group1 = QVBoxLayout()                
        self.form_constraints = QFormLayout()
        self.form_constraints.addRow('unique', QCheckBox())
        self.form_constraints.addRow('nullable (not required)', QCheckBox()) # lawan dari required
        self.form_constraints.addRow('primary key', QCheckBox())
        self.form_constraints.addRow('auto increment', QCheckBox())
        self.form_constraints.addRow('blank', QCheckBox())
        self.form_constraints.addRow('editable', QCheckBox())
        self.form_constraints.addRow('db index', QCheckBox())
        self.form_constraints.addRow('auto now', QCheckBox())
        self.form_constraints.addRow('auto now add', QCheckBox())
        self.form_constraints.addRow('trim', QCheckBox())
        self.form_constraints.addRow('uppercase', QCheckBox())
        self.form_constraints.addRow('lowercase', QCheckBox())
        self.form_constraints.addRow('max length', QSpinBox())
        self.form_constraints.addRow('min length', QSpinBox())
        self.form_constraints.addRow('max digits', QSpinBox())
        self.form_constraints.addRow('decimal places', QSpinBox())
        self.form_constraints.addRow('default', QLineEdit())
        self.form_constraints.addRow('references', QLineEdit())
        self.form_constraints.addRow('references key', QLineEdit())
        self.form_constraints.addRow('enum: >name? items >default?', QLineEdit())
        layout_for_group1.addLayout(self.form_constraints)
        # layout_for_group1.addStretch(1)
        group1.setLayout(layout_for_group1)
        helper_wrapper_layout.addWidget(group1)
        self.helper_output = QPlainTextEdit("output utk helper")
        # self.helper_output.returnPressed.connect(lambda: print('Enter'))
        # self.helper_output.selectionChanged.connect(lambda: print('selection changed'))
        # self.helper_output.textChanged.connect(lambda value: print(value))
        # self.helper_output.textEdited.connect(lambda value: print(value))
        helper_wrapper_layout.addWidget(self.helper_output)
        # original helper_wrapper_widget, kita ubah ke stackwidget berisi notebrowser
        self.help_note = NoteBrowser(content=file_content(joinhere(__file__, 'csvlang-help.txt')))
        self.help_stack = QStackedWidget()
        self.help_stack.addWidget(self.help_note)
        self.help_stack.addWidget(helper_wrapper_widget)
        # self.main_splitter.addWidget(helper_wrapper_widget)
        for index in range(self.help_stack.count()):
            # button_helper_menu.addAction(f'{index}', lambda: self.help_stack.setCurrentIndex(index+1))
            button_helper_menu.addAction(f'{index}', functools.partial(self.help_stack.setCurrentIndex, index))


        # output kita split saja
        output_help_splitter = QSplitter(Qt.Vertical)
        output_help_splitter.addWidget(output_widget_wrapper)
        output_help_splitter.addWidget(self.help_stack)
        output_help_splitter.handle(1).setStyleSheet('background: 3px green;')
        # self.main_splitter.addWidget(output_widget_wrapper)
        # self.main_splitter.addWidget(self.help_stack)
        self.main_splitter.addWidget(output_help_splitter)
        # self.main_splitter.setOrientation(Qt.Horizontal)
        # self.main_splitter.setHandleWidth(8)
        # self.main_splitter.setStretchFactor(0, 5)
        # self.main_splitter.setStretchFactor(1, 5)
        self.main_splitter.handle(1).setStyleSheet('background: 3px blue;')
        # self.main_splitter.handle(2).setStyleSheet('background: 3px blue;')
        self.main_layout.addWidget(self.main_splitter)
        self.setLayout(self.main_layout)

        self.setWindowTitle('Csvlang')
        # QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
        # self.show()
        self.resize(1200, 800)


background_image_stylesheet = '''
CsvlangWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    set_theme(app)
    ex = CsvlangWidget()
    ex.setStyleSheet(background_image_stylesheet)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
