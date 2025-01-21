from concurrent.futures import process
from inspect import trace
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
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import get_icon, set_theme
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.gui.system.searcher.widgets.config import replang_active_languages

concepts = [
    'anonymous_function',
    'assignment',
    'class',
    'const',
    'constructor',
    'enum',
    'exception',
    'export',
    'field',
    'for',
    'function',
    'function_call',
    'if',
    'import',
    'interface',
    'literal',
    'match',
    'method',
    'operator',
    'package',
    'range',
    'scope',
    'switch',
    'type_alias',
    'var',
    'while',
    'array_ops',
    'dataframe_ops',
    'data_ops',
    'datetime_ops',
    'dict_ops',
    'faker_ops',
    'gui_ops',
    'number_ops',
    'orm_ops',
    'react_ops',
    'redis_ops',
    'set_ops',
    'stdout_ops',
    'string_ops',
    'tuple_ops',
]


class LalangWidget(QWidget):

    def radios_toggled_for_radios0(self, value):
        toggled_radio = self.sender()
        print(f'{toggled_radio.text()} is {"ON" if toggled_radio.isChecked() else "OFF"}')

    def handle_concept(self):
        b = self.sender()
        code = b.property('info')
        # handle process....
        result = f"insert concept {code}"
        self.editor_input.append(result)

    def set_input_completer(self):
        model = self.completer.model()
        model.setStringList(self.history)

    def tekan_enter(self):        
        # lalangsource = 'c:/users/usef/work/sidoarjo/data/github/lalang/src'
        lalangsource = 'c:/github/lalang/src'
        sys.path.insert(0, lalangsource)
        from lalang import process_language

        tulisan = self.line_edit.text().strip()
        if tulisan:
            # get bhs
            bahasa = self.radiobuttongroup.checkedButton().text()
            try:
                list_result = process_language(bahasa + '/' + tulisan, returning=True)
                result = '\n'.join(list_result)
            except Exception as err:
                import traceback
                result = f'Gagal: {err}\n{traceback.format_exc()}'

            # self.editor_output.setText(result)
            # self.editor_output.setText(result + '\n\n')
            if not result.endswith('\n'):
                result += '\n'
            line, index = self.editor_output.getCursorPosition()
            self.editor_output.insertAt(result, line, index)

            self.line_edit.setText('')
            if tulisan not in self.history:
                self.history.append(tulisan)
                self.set_input_completer()

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()

        self.radios = []
        radiolayout = QHBoxLayout()
        radiolayout.addStretch(1)
        self.radiobuttongroup = QButtonGroup(self)
        for i,bhs in enumerate(replang_active_languages):
            b = QRadioButton(bhs)
            # self.radios[i].toggled.connect(self.radios_toggled_for_radios0)
            self.radiobuttongroup.addButton(b)
            self.radios.append(b)
            radiolayout.addWidget(b)
        radiolayout.addStretch(1)
        self.radios[0].setChecked(True)

        self.flow_widget = FlowWidget()
        self.flow_widget.setStyleSheet("""
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
        widgets = []
        for item in concepts:
            b = QPushButton(item)
            b.setProperty('info', item)
            b.clicked.connect(self.handle_concept)
            widgets.append(b)
        self.flow_widget.add_items(widgets)

        self.history = []
        self.completer = QCompleter(self.history)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.line_edit = QLineEdit("")
        # self.line_edit.returnPressed.connect(lambda: print(f'Enter: {self.line_edit.text()}'))
        self.line_edit.setFont(QFont("Consolas", 16))
        self.line_edit.setStyleSheet('background-color: oldlace; height: 48px;')
        self.line_edit.returnPressed.connect(self.tekan_enter)
        self.line_edit.setCompleter(self.completer)
        
        # self.line_edit.selectionChanged.connect(lambda: print('selection changed'))
        # self.line_edit.textChanged.connect(lambda value: print(value))
        # self.line_edit.textEdited.connect(lambda value: print(value))        
        self.editor_input = EditorStandard(self)        
        self.editor_output = EditorStandard(self)

        split = QSplitter(Qt.Vertical)
        top = QVBoxLayout()
        top.addLayout(radiolayout)
        top.addWidget(self.flow_widget)
        bottom = QVBoxLayout()
        bottom.addWidget(self.line_edit)
        bottom.addWidget(self.editor_input)
        bottom.addWidget(self.editor_output)
        topgb = QGroupBox()
        topgb.setLayout(top)
        bottomgb = QGroupBox()
        bottomgb.setLayout(bottom)
        split.addWidget(topgb)
        split.addWidget(bottomgb)
        split.setStretchFactor(0, 1)
        split.setStretchFactor(1, 3)
        split.handle(1).setStyleSheet('background: 3px blue;')

        # self.main_layout.addLayout(radiolayout)
        # self.main_layout.addWidget(self.flow_widget)

        # self.main_layout.addWidget(self.line_edit)
        # self.main_layout.addWidget(self.editor_input)
        # self.main_layout.addWidget(self.editor_output)
        self.main_layout.addWidget(split)

        self.setLayout(self.main_layout)


background_image_stylesheet = '''
LalangWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    ex = LalangWidget()
    ex.setStyleSheet(background_image_stylesheet)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
