# gaya yg kita ikutin adlh...
# ini utk...
"""
ada dir berisi mk files
kita bikin:
buttons of masing2 mk
menus of toc dari mk
"""

# from json import tool
import os, sys, textwrap
import pyperclip
import functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
sys.path.append(sidoarjodir)
if __name__ == '__main__':
    envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
    from dotenv import load_dotenv
    load_dotenv(envfile)
    schnelldir = os.environ['ULIBPY_BASEDIR']
    rootdir = os.environ['ULIBPY_ROOTDIR']
    # sys.path.extend([rootdir, schnelldir])
    from startup import initialize_programming_data
    initialize_programming_data()
else:
    from schnell.app.utils import env_get
    rootdir = env_get('ULIBPY_ROOTDIR')

from schnell.app.dirutils import files, files_filter, dirs, joiner, bongkar
from schnell.app.envvalues import sidoarjo_absolute
from schnell.app.fileutils import (
    get_daftar,
    get_definition_by_key_permissive_start,
    get_definition_by_key_permissive_start_with_lineno,
    replace_entry_in_mkfile,
)
from schnell.app.stringutils import sanitize_chars
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import get_icon, set_theme
from schnell.creator.context import context as global_context
from schnell.gui.system.searcher.widgets.editor_fmus import EditorFmus
from schnell.app.quick import handle_publish_to_redis
from schnell.gui.system.searcher.widgets.verticaltab import TabWidget
from schnell.gui.system.searcher.widgets.lshelp_style import lshelp_stylesheet

rootpath = joiner(rootdir, 'database/refcards')

push_button_stylesheet = """
QPushButton {
    background-color: burlywood;
    font-family: Verdana, Consolas;
    font-size: 16px;
    padding: 10px;
    margin: 5px;
    border-radius: 2px;
    border: 1px solid darkblue;
}
QPushButton:checked {
    background-color: darkgoldenrod;
    border: 1px solid red;
}
QPushButton:hover {
    background-color: cornsilk;
}
"""


class ListContainer(QWidget):

    def __init__(self, filepath, toc, container, lshelpwidget, page_index, *args, **kwargs):
        super(ListContainer, self).__init__(*args, **kwargs)

        self.filepath = filepath
        self.container = container
        self.lshelpwidget = lshelpwidget
        self.toc = toc  # get_daftar(self.filepath)
        self.page_index = page_index
        self.contents = {}

        self.main_layout = QHBoxLayout(self, spacing=0)
        self.setStyleSheet(lshelp_stylesheet)
        self.initUi()

        self.splitter = QSplitter(self)
        self.splitter.setHandleWidth(8)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.addWidget(self.listWidget)
        self.splitter.addWidget(self.container)

        self.main_layout.addWidget(self.splitter)

    def daftar(self, index):
        return self.toc[index % len(self.toc)]

    def initUi(self):


        self.listWidget = QListWidget(self)
        # self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        self.listWidget.currentRowChanged.connect(lambda row: self.lshelpwidget.ganti_toc(self.page_index, self.filepath, self.daftar(row)))
        # remove border
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # hide scrollbar
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.buatWidgets()
    
    def buatWidgets(self):
        icon = QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion)
        for isi in self.toc:
            isi_file = get_definition_by_key_permissive_start(self.filepath, isi)
            self.contents[isi] = isi_file
            judul = textwrap.shorten(isi, width=60, placeholder="###")
            item = QListWidgetItem(icon, judul, self.listWidget)
            w, h = 16777215, 60
            item.setSizeHint(QSize(w,h))

class LSHelpWidget(QWidget):

    button_data_signal = pyqtSignal(str)
    toggle_top_signal = pyqtSignal(bool)
    toggle_bot_signal = pyqtSignal(bool)

    def change_rootpath(self, rootpath):
        self.rootpath = rootpath
        # rootpath_label.setText(self.rootpath)
        # self.rootpath_label_after_f12.setText(self.rootpath)

    # def add_extra_buttons(self, more_extra_buttons):
    #     self.extra_buttons.extend(more_extra_buttons)
    #     if more_extra_buttons:
    #         for btn in more_extra_buttons:
    #             self.flowwidget.add_item(btn)

    def __init__(self,
        parent=None,
        rootpath='ULIBPY_ROOTDIR/schnell/data/kenza',
        copy_after_insert=False,
        extra_buttons=[],
        extra_buttons_to_connect_to_editor=[],
        lexer='py',
        # gptchat = None,
        ):

        super().__init__(parent=parent)
        self.lexer = lexer
        self.rootpath = bongkar(rootpath)
        self.copy_after_insert = copy_after_insert
        self.extra_buttons = extra_buttons
        self.skip_delete_widgets = extra_buttons
        self.extra_buttons_to_connect_to_editor = extra_buttons_to_connect_to_editor
        # self.gptchat = gptchat
        self.filemanager = parent
        self.last_filepath_barisentry = ''
        self.tab_pages = []
        self.lineno = -1
        self.last_file = None
        self.initUI()

    # def setGptChat(self, gptchat):
    #     self.gptchat = gptchat

    def recreate_buttons(self):
        """
        recreate content mk helper
        semua akan dihapus lalu ditambah ulang
        """
        # self.rootpath sudah terisi benar
        # files mk
        self.daftar_filepath = files_filter(self.rootpath, extension=['.mk', '.fmus'])
        self.filepath_to_barisentry = {}
        # {filemk: daftar, filemk: daftar, ...}
        for item in self.daftar_filepath:
            self.filepath_to_barisentry[item] = get_daftar(joiner(self.rootpath, item))
        widgets = []
        for item in self.daftar_filepath:
            # item = key = filename dg .mk
            b_label = sanitize_chars( item.removesuffix('.mk').removesuffix('.fmus') )
            b = QPushButton(b_label)
            if item in self.filepath_to_barisentry:
                # data berisi daftar baris_entry
                # item adlh filename .mk
                data = self.filepath_to_barisentry[item]
                filepath_mk = joiner(self.rootpath, item)
                if len(data)==1:
                    # satu baris_entry, gak pake menu, langsung klik button
                    satu = data[0]
                    filepath_barisentry = filepath_mk + ':' + satu
                    # b.clicked.connect(functools.partial(self.button_data_signal.emit, satu))
                    # b.clicked.connect(functools.partial(self.button_data_signal.emit, filepath_barisentry))
                    b.clicked.connect(functools.partial(self.signal_open_file, filepath_barisentry))
                else:
                    menu = self.create_button_menu(data, filepath_mk)
                    b.setMenu(menu)
            widgets.append(b)


    def signal_open_file(self, filepath_barisentry):
        self.button_data_signal.emit(filepath_barisentry)
        self.last_filepath_barisentry = filepath_barisentry

    def edit_last_file(self):
        from schnell.app.utils import edit_entry
        edit_entry(self.last_file, self.lineno)
        # self.f12.setToolTip(self.last_file)

    def buttons_go_clear(self, page_index):
        """
        ini adlh bagian dari container = labels+buttons+shared editor
        nanti digabung dg shared listwidget
        """

        rootpath_label = QLabel('')
        rootpath_label.setStyleSheet('border: 1px solid fuchsia; border-radius: 3px; background-color: beige;')
        rootpath_label.setText(self.rootpath)
        filepath_label = QLabel('')
        filepath_label.setStyleSheet('border: 1px solid fuchsia; border-radius: 3px; background-color: beige;')
        filepath_label.setText('')
        barisentry_label = QLabel('')
        barisentry_label.setStyleSheet('border: 1px solid fuchsia; border-radius: 3px; background-color: beige;')
        barisentry_label.setText('')

        rootpath_go = QPushButton('Go')
        rootpath_go.setStyleSheet(push_button_stylesheet)
        rootpath_go.setToolTip('Recreate buttons\nrootpath harus sudah terisi')

        clear_button = QPushButton('Clear')
        clear_button.setStyleSheet(push_button_stylesheet)
        clear_button.setToolTip('Clear guicode')

        toggle_expansion_button = QPushButton('Exp')
        toggle_expansion_button.setStyleSheet(push_button_stylesheet)
        toggle_expansion_button.setToolTip('Toggle $$link= $$img= expansion')
        toggle_expansion_button.setCheckable(True)
        toggle_expansion_button.clicked.connect(self.toggle_expansion)

        save_button = QPushButton('Save')
        save_button.setStyleSheet(push_button_stylesheet)
        save_button.setToolTip('Save guicode')

        # rootpath_go.clicked.connect(self.recreate_buttons) # rootpath hrs sudah terisi
        # harus bisa pilih
        # clear_button.clicked.connect(self.clear_guicode)
        # harus bisa pilih
        # save_button.clicked.connect(lambda: self.guicode_editor.save_file.emit(True))
        # self.listWidget.currentRowChanged.connect(lambda: self.lshelpwidget.ganti_toc(self.page_index, self.filepath, self.daftar(row)))
        # toolbar_layout.addStretch(1)

        # button: top, bot, f12
        toggle_layout = QHBoxLayout()

        toggle_top = QPushButton('top')
        toggle_top.setStyleSheet(push_button_stylesheet)
        toggle_top.setCheckable(True)
        toggle_top.toggled.connect(self.toggle_top_signal.emit)

        toggle_bot = QPushButton('bot')
        toggle_bot.setStyleSheet(push_button_stylesheet)
        toggle_bot.setCheckable(True)
        toggle_bot.toggled.connect(self.toggle_bot_signal.emit)

        button_f12 = QPushButton('F12')
        button_f12.setStyleSheet(push_button_stylesheet)
        button_f12.setToolTip('Edit last file')
        button_f12.clicked.connect(self.edit_last_file)

        toggle_layout.addWidget(toggle_top)
        toggle_layout.addWidget(toggle_bot)
        toggle_layout.addWidget(button_f12)

        # text field
        toolbar_layout = QVBoxLayout()
        jajar_horisontal = QHBoxLayout()
        jajar_horisontal.addWidget(rootpath_label)
        # jajar_horisontal.addWidget(filepath_label)
        # jajar_horisontal.addWidget(barisentry_label)
        

        # buttons
        toolbar_horizontal = QHBoxLayout()
        toolbar_horizontal.addWidget(rootpath_go)
        toolbar_horizontal.addWidget(clear_button)
        toolbar_horizontal.addWidget(save_button)
        toolbar_horizontal.addWidget(toggle_expansion_button)
        toolbar_horizontal.addLayout(toggle_layout)

        jajar_horisontal.addLayout(toolbar_horizontal)

        filepath_entry_horisontal = QHBoxLayout()
        filepath_entry_horisontal.addWidget(filepath_label)
        filepath_entry_horisontal.addWidget(barisentry_label)

        toolbar_layout.addLayout(jajar_horisontal)
        toolbar_layout.addLayout(filepath_entry_horisontal)
        return (toolbar_layout,rootpath_label,filepath_label,barisentry_label,rootpath_go,clear_button,save_button)


    def create_listwidget_and_share_editor(self, filepath, toc):

        # self.recreate_buttons()

        # editorlayout = QVBoxLayout()
        # self.guicode_editor = EditorStandard(self, lexer=self.lexer)  # guilang
        my_guicode_editor = EditorFmus(self, lexer=self.lexer)
        page_index=len(self.tab_pages)

        # toolbar_layout berisi: fields + buttons
        # toolbar_layout,rootpath_label,filepath_label,barisentry_label,rootpath_go,clear_button,save_button
        toolbar_layout,rootpath_label,filepath_label,barisentry_label,rootpath_go,clear_button,save_button = self.buttons_go_clear(page_index)

        # rootpath_go.clicked.connect(self.recreate_buttons) # rootpath hrs sudah terisi
        # harus bisa pilih
        clear_button.clicked.connect(lambda: self.clear_guicode(my_guicode_editor))
        # harus bisa pilih
        # save_button.clicked.connect(lambda: my_guicode_editor.save_file.emit(True))
        save_button.clicked.connect(lambda: self.save_file(my_guicode_editor))

        # sejajar = wrapper: toolbar_layout + flow layout
        sejajar = QHBoxLayout()
        sejajar.addLayout(toolbar_layout)
        # sejajar.addWidget(self.flowwidget)
        # wrap sejajar utk disusun vertikal dg editor via splitter
        top_wrapper = QWidget()
        top_wrapper.setLayout(sejajar)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(top_wrapper)
        splitter.addWidget(my_guicode_editor)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 9)
        splitter.handle(1).setStyleSheet('background: 3px blue;')
        
        tab_page = ListContainer(filepath, toc, splitter, self, page_index=page_index)
        self.tab_pages.append({
            'index': page_index,
            'filepath': filepath,
            'page': tab_page,
            'editor': my_guicode_editor,
            ################################################################
            'rootpath_label':rootpath_label,
            'filepath_label':filepath_label,
            'barisentry_label':barisentry_label,
            'rootpath_go':rootpath_go,
            'clear_button':clear_button,
            'save_button':save_button,
        })

        return tab_page


    def go_reinitialize_tab_page(self, filepath):
        toc = get_daftar(filepath)
        tab_page = self.create_listwidget_and_share_editor(filepath, toc)
        return tab_page

    def initUI(self):    
        ######################################################################################################
        # self.main_tab = TabWidget(self)
        self.main_tab = QTabWidget(self)
        # harus cari info cara reload tabs...apa harus ada layout.addWidget lagi?
        # atau cukup reinitialize main_tab?
        self.daftar_filepath = files_filter(self.rootpath, extension=['.mk', '.fmus'])
        self.filepath_to_barisentry = {}
        # {filemk: daftar, filemk: daftar, ...}
        for item in self.daftar_filepath:
            toc = get_daftar(joiner(self.rootpath, item))
            self.filepath_to_barisentry[item] = toc
            tab = self.create_listwidget_and_share_editor(joiner(self.rootpath, item), toc)
            # utk bisa reload satu tab page, hrs tau gimana cara remove page dan add page pada index yg sama di tabwidget
            self.main_tab.addTab(tab, item.removesuffix('.mk').removesuffix('.fmus'))
        ######################################################################################################
        self.main_layout = QVBoxLayout()
        # self.main_layout.addLayout(sejajar, 3)
        # self.main_layout.addLayout(editorlayout, 7)
        # self.main_layout.addWidget(splitter)
        self.main_layout.addWidget(self.main_tab)
        self.setLayout(self.main_layout)
        # self.handle_signals()
        # for btn in self.extra_buttons_to_connect_to_editor:
        #     btn.button_data_signal.connect(self.guicode_editor_insert_data)

    def ganti_toc(self, page_index, filepath, baris_entry):
        self.last_file = filepath
        filepath_label = self.tab_pages[page_index]['filepath_label']
        barisentry_label = self.tab_pages[page_index]['barisentry_label']
        filepath_label.setText(self.last_file.removeprefix(sidoarjo_absolute))
        barisentry_label.setText(baris_entry)
        self.last_entry = baris_entry
        content, self.lineno = get_definition_by_key_permissive_start_with_lineno(self.last_file, self.last_entry)
        # print(f"""
        # ganti_toc
        # ganti_toc(filepath, baris_entry) = {filepath}, {baris_entry}
        # content = {content}
        # """)
        if content:
            editor = self.tab_pages[page_index]['editor']
            editor.setText(content)
            if self.copy_after_insert:
                pyperclip.copy(content) 

    def handle_signals(self, guicode_editor):
        guicode_editor.save_file.connect(lambda _: self.save_file(guicode_editor))
        guicode_editor.replrequest.connect(self.handle_ctrl_k_replrequest)
        # self.guicode_editor.fmusrequest.connect(self.handle_ctrl_m_fmusrequest)
        guicode_editor.fmus_repl_request.connect(self.handle_ctrl_k)
        guicode_editor.englishrequest.connect(self.handle_ctrl_w_writerservice)
        guicode_editor.publishrequest.connect(self.handle_redis_publish_request)

    def handle_redis_publish_request(self, code):
        handle_publish_to_redis(code)

    def handle_ctrl_w_writerservice(self, code):
        from schnell.db.writer_service import process_writer        
        result = process_writer(code)
        handle_publish_to_redis(result)

    def handle_ctrl_k_replrequest(self, bariskalimat_baris):
        from schnell.app.fmusutils import run_fmus_for_content_in_thread_notify
        # replrequest = pyqtSignal(tuple)
        # self.replrequest.emit((bariskalimat, baris))
        bariskalimat, baris = bariskalimat_baris
        if not bariskalimat.endswith('\n'):
            bariskalimat += '\n'
        # alert(f"bariskalimat = {bariskalimat}\nbaris = {baris}", 'ctrl+k')
        run_fmus_for_content_in_thread_notify(bariskalimat, os.getcwd(), title='Oneliner', body=bariskalimat[:80]+'...')
        pass

    def handle_ctrl_m_fmusrequest(self, bariskalimat, barismulai, kolommulai, barisakhir, kolomakhir):
        from schnell.app.fmusutils import run_fmus_for_content_in_thread_notify
        # fmusrequest = pyqtSignal(str, int, int, int, int)
        # self.fmusrequest.emit(bariskalimat, barismulai, kolommulai, barisakhir, kolomakhir)
        # alert(f"bariskalimat = {bariskalimat}\nbarismulai = {barismulai}\nkolommulai = {kolommulai}\nbarisakhir = {barisakhir}\nkolomakhir = {kolomakhir}", 'ctrl+m')
        if not bariskalimat.endswith('\n'):
            bariskalimat += '\n'
        run_fmus_for_content_in_thread_notify(bariskalimat, os.getcwd(), title='Multiliner', body=bariskalimat[:80]+'...')
        pass

    def handle_ctrl_k(self, bariskalimat):
        from schnell.app.fmusutils import run_fmus_for_content_in_thread_notify
        if not bariskalimat.endswith('\n'):
            bariskalimat += '\n'
        run_fmus_for_content_in_thread_notify(bariskalimat, os.getcwd(), title='Ctrl+K', body=bariskalimat[:80]+'...')

    def dummy_terima_data(self, text):
        print('mkhelp terima data:', text)
        pass

    def clear_guicode(self, guicode_editor):
        guicode_editor.setText('')
        # self.editor_tab.setCurrentIndex(0)

    def toggle_expansion(self):
        global_context['fmus_expansion_mode'] = not global_context['fmus_expansion_mode']

    # def guicode_editor_insert_data(self, text):
    #     if '.mk:' in text:
    #         filepath, baris_entry = text.split('.mk:')
    #         self.last_file = filepath + '.mk'
    #     else:
    #         filepath, baris_entry = text.split('.fmus:')
    #         self.last_file = filepath + '.fmus'
    #     filepath_label.setText(self.last_file.removeprefix(sidoarjo_absolute))
    #     barisentry_label.setText(baris_entry)
    #     self.last_entry = baris_entry
    #     content, self.lineno = get_definition_by_key_permissive_start_with_lineno(self.last_file, self.last_entry)
    #     if content:
    #         self.guicode_editor.setText(content)
    #         if self.copy_after_insert:
    #             pyperclip.copy(content)

    # def reopen_last_file(self):
    #     if self.last_filepath_barisentry:
    #         self.guicode_editor_insert_data(self.last_filepath_barisentry)
    #         # print('[mkhelp] opening {self.last_filepath_barisentry}.')
    #     # else:
    #     #     print('[mkhelp] NOT opening {self.last_filepath_barisentry}.')

    def save_file(self, guicode_editor):
        """
        cek gimana jk 
        user sudah buka, last_file terset....
        """
        if self.last_file and self.last_entry:
            file_content = guicode_editor.text()
            replace_entry_in_mkfile(self.last_entry, file_content, self.last_file)
        else:
            print('mkhelp editor: self.last_file not set')


background_image_stylesheet = '''
FileManager {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def main():
    app = QApplication([])
    ex = LSHelpWidget()
    ex.setStyleSheet(background_image_stylesheet)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
