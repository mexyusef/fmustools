import os, random, string, sys
import pyperclip
import functools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

# gaya yg kita ikutin adlh...
# ini utk...
"""
ada dir berisi mk files
kita bikin:
buttons of masing2 mk
menus of toc dari mk
"""

# ini wajib agar icon bisa jalan
import ctypes
myappid = 'schnell.gui.system.searcher.widgets.mkhelp.0.0.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# from json import tool
make_mkcommand_button = False
global_warna = None

if __name__ == '__main__':
    from pathlib import Path
    sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
    # schnelldir = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
    #                              file        wid    sea    sys    gui    sch    sido
    sys.path.append(sidoarjodir)

    # load env utk encryption etc
    from constants import sidoarjodir
    from dotenv import load_dotenv
    load_dotenv(os.path.join(sidoarjodir, 'schnell/.env'))

    from startup import initialize_programming_data, programming_data
    initialize_programming_data()
    global_warna = programming_data['colors']['mkhelp'] # "cornsilk"
    make_mkcommand_button = True
else:
    from schnell.app.utils import env_get
    # sidoarjodir = env_get('ULIBPY_ROOTDIR')
from constants import sidoarjodir, button_stylesheet1, push_button_stylesheet, label_stylesheet1, background_image_stylesheet

from schnell.app.dirutils import files, files_filter, dirs, joiner
from schnell.app.envvalues import sidoarjo_absolute
from schnell.app.fileutils import (
    get_daftar,
    get_definition_by_key_permissive_start_with_lineno,
    replace_entry_in_mkfile,
)
from schnell.app.printutils import indah3, indah4
from schnell.app.quick import handle_publish_to_redis
from schnell.app.stringutils import sanitize_chars, uuid1
from schnell.app.threadutils import mulai

from schnell.creator.context import context as global_context

from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.common import get_icon, resize_screen_ratio_wrapper_simple, create_menu_cmds, create_menu_editors
from schnell.gui.system.searcher.widgets.editor_fmus import EditorFmus
from schnell.gui.system.searcher.widgets.exec_commands import exec_code_sidoarjo

from schnell.gui.system.searcher.widgets.mkhelp_label import ClickableLabel

rootpath = joiner(sidoarjodir, 'database/refcards')


class MKHelpWidget(QWidget):

    button_data_signal = pyqtSignal(str)
    toggle_top_signal = pyqtSignal(bool)
    toggle_bot_signal = pyqtSignal(bool)

    def change_rootpath(self, rootpath):
        self.rootpath = rootpath
        self.rootpath_label.setText(self.rootpath)
        self.rootpath_label_after_f12.setText(self.rootpath)

    def add_extra_buttons(self, more_extra_buttons):
        self.extra_buttons.extend(more_extra_buttons)
        if more_extra_buttons:
            for btn in more_extra_buttons:
                self.flowwidget.add_item(btn)

    def __init__(self,
        parent=None,
        rootpath=rootpath,
        copy_after_insert=False,
        extra_buttons=[],
        extra_buttons_to_connect_to_editor=[],
        lexer='py',
        factor_top=1,
        factor_bottom=9
        # gptchat = None,
        ):

        super().__init__(parent=parent)
        self.lexer = lexer
        self.rootpath = rootpath
        self.copy_after_insert = copy_after_insert
        self.extra_buttons = extra_buttons
        self.skip_delete_widgets = extra_buttons
        self.extra_buttons_to_connect_to_editor = extra_buttons_to_connect_to_editor
        # self.gptchat = gptchat
        self.factor_top=factor_top
        self.factor_bottom=factor_bottom
        self.filemanager = parent
        self.last_filepath_barisentry = ''
        self.initUI()
        self.setWindowTitle(self.rootpath + f" [{uuid1()}]")

    # def setGptChat(self, gptchat):
    #     self.gptchat = gptchat

    def recreate_buttons(self):
        """
        recreate content mk helper
        semua akan dihapus lalu ditambah ulang
        """
        # self.rootpath sudah terisi benar
        self.guilang_items = files_filter(self.rootpath, extension=['.mk', '.fmus'])
        # key adlh filename relative (e.g. reference.mk), values adlh semua barisentry pd file tsb.
        self.guilang_dict = {}
        for item in self.guilang_items:
            self.guilang_dict[item] = get_daftar(joiner(self.rootpath, item))
        widgets = []
        for item in self.guilang_items:
            # item = key = filename dg .mk
            b_label = sanitize_chars( item.removesuffix('.mk').removesuffix('.fmus') )
            b = QPushButton(b_label)
            if item in self.guilang_dict:
                # data berisi daftar baris_entry
                # item adlh filename .mk
                data = self.guilang_dict[item]
                filepath_mk = joiner(self.rootpath, item)
                if len(data)==1:
                    # satu baris_entry, gak pake menu, langsung klik button
                    satu = data[0]
                    filepath_barisentry = filepath_mk + ':' + satu
                    # b.clicked.connect(functools.partial(self.button_data_signal.emit, satu))
                    # b.clicked.connect(functools.partial(self.button_data_signal.emit, filepath_barisentry))
                    b.clicked.connect(functools.partial(self.signal_open_file, filepath_barisentry))
                else:
                    # jk file MK berisi bbrp barisentry, gunakan menu.addAction alih2 clicked handler
                    menu = self.create_button_menu(data, filepath_mk)
                    b.setMenu(menu)
            widgets.append(b)
        self.flowwidget.clear_add_items(widgets)
        self.create_add_f12()
        # RuntimeError: wrapped C/C++ object of type QLabel has been deleted
        # self.flowwidget.add_item(self.rootpath_label_after_f12)
        self.create_rootpath_label_after_f12()
        if self.extra_buttons:
            for btn in self.extra_buttons:
                # btn.property('mkfilebutton').connect_to_editor(self.guicode_editor_insert_data)
                # print('parentwid:', btn.parentWidget())
                # if hasattr(btn, 'button_data_signal'):
                #     btn.button_data_signal.connect(self.guicode_editor_insert_data)
                # else:
                #     if hasattr(btn, 'object_wrapper') and btn.property('object_wrapper'):
                #         print('extra button:', btn.text(), 'gak punya data signal tapi punya object_wrapper')
                #     else:
                #         print('extra button:', btn.text(), 'gak punya data signal dan tidak punya object_wrapper')
                # # # coba gambling bisa gak nih
                # # 'QPushButton' object has no attribute 'filepath_mk'
                # if hasattr(btn, 'object_wrapper') and btn.property('object_wrapper'):
                #     mkfilebutton = btn.property('object_wrapper')
                #     _filepath_mk = mkfilebutton.filepath_mk
                #     _entries = get_daftar(_filepath_mk)
                #     print(f'extra_buttons => file: {_filepath_mk}, entries {_entries}')
                #     extramenu = self.create_button_menu(_entries, _filepath_mk)
                #     btn.setMenu(extramenu)
                # # else:
                # #     print('no object_wrapper')
                self.flowwidget.add_item(btn)

    def create_button_menu(self, menu_list, filepath_mk):
        menu = QMenu('Button Menu')
        for item in sorted(menu_list):
            filepath_barisentry = filepath_mk + ':' + item
            # item adlh dict label: content, label utk tampil di menu, content utk diinsert di editor
            # menu.addAction(get_icon(), item['label'], lambda: self.button_data_signal.emit(item['content']))
            # menu.addAction(get_icon(), item, functools.partial(self.button_data_signal.emit, filepath_barisentry))
            menu.addAction(get_icon(), item, functools.partial(self.signal_open_file, filepath_barisentry))
            # self.button_data_signal.emit, data
        return menu

    def signal_open_file(self, filepath_barisentry):
        self.button_data_signal.emit(filepath_barisentry)
        self.last_filepath_barisentry = filepath_barisentry

    def create_rootpath_label_after_f12(self):
        self.rootpath_label_after_f12 = QLabel('')
        self.rootpath_label_after_f12.setStyleSheet('border: 1px solid fuchsia; border-radius: 3px; background-color: beige; min-width: 80px;')
        self.rootpath_label_after_f12.setText(self.rootpath)
        self.flowwidget.add_item(self.rootpath_label_after_f12)

    def create_add_f12(self):
        """
        gara2:
        Traceback (most recent call last):
        File "C:/Users/usef/work/sidoarjo/schnell/gui/system/searcher/widgets/mkhelp.py", line 348, in recreate_buttons
            self.flowwidget.add_item(self.f12)
        File "C:/Users/usef/work/sidoarjo/schnell/gui/system/searcher/widgets/mkhelp.py", line 231, in add_item
            self.flowLayout.addWidget(widget)
        RuntimeError: wrapped C/C++ object of type QPushButton has been deleted
        """
        self.f12 = QPushButton("f12")
        self.f12.setStyleSheet('background-color: blanchedalmond; color: indigo; font-size: 18px;')
        self.f12.clicked.connect(self.edit_last_file)
        self.flowwidget.add_item(self.f12)

    def edit_last_file(self):  # handler f12 sebenarnya
        from schnell.app.utils import edit_entry
        edit_entry(self.last_file, self.lineno)
        self.f12.setToolTip(self.last_file)

    # self.mkcommand_menu = create_menu_mkcommand(self)
    # self.mkcommand_menu.addSeparator()
    # def reload_mkcommand(parent):
    #     parent.mkcommand_button.setMenu(parent.mkcommand_menu)
    # # self.mkcommand_menu.addAction("Reload", lambda: os.system(f"code {filePath}"))
    # self.mkcommand_button.setMenu(self.mkcommand_menu)

    def reload_mkcommand_menu(self):
        # TODO: ini spt nya belum menghasilkan yg kita inginkan, jk tambah perintah di config_quick.json, tapi tetap belum ter-render
        # utk efektif programming_language hrs direload juga
        from startup import reload_config
        reload_config('config_quick.json')
        self.set_mkcommand_menu()

    def set_mkcommand_menu(self):
        try:
            from .mkcommand import create_menu_mkcommand
        except:
            from mkcommand import create_menu_mkcommand
        mkcommand_menu = create_menu_mkcommand(self)
        mkcommand_menu.addSeparator()
        mkcommand_menu.addAction('Reload', self.reload_mkcommand_menu)
        return mkcommand_menu

    def initUI(self):
        self.flowwidget = FlowWidget(skip_delete_widgets=self.skip_delete_widgets)
        self.flowwidget.setStyleSheet(push_button_stylesheet)

        self.lineno = -1
        self.last_file = None

        # ada sblm recreate_buttons
        self.rootpath_label_after_f12 = QLabel('')
        self.rootpath_label_after_f12.setStyleSheet('border: 1px solid fuchsia; border-radius: 3px; background-color: beige; min-width: 80px;')
        self.rootpath_label_after_f12.setText(self.rootpath)
        self.recreate_buttons()

        # editorlayout = QVBoxLayout()
        # self.guicode_editor = EditorStandard(self, lexer=self.lexer)  # guilang
        self.guicode_editor = EditorFmus(self, warna=global_warna, lexer=self.lexer)

        self.button_data_signal.connect(self.guicode_editor_insert_data)
        # editorlayout.addWidget(self.guicode_editor)
        # editorlayout.addLayout(toolbarlayout)

        self.rootpath_label = ClickableLabel('')
        self.rootpath_label.setStyleSheet(label_stylesheet1)
        self.rootpath_label.setText(self.rootpath)
        self.filepath_label = ClickableLabel('')
        self.filepath_label.setStyleSheet(label_stylesheet1)
        self.filepath_label.setText('')
        self.barisentry_label = QLabel('')
        self.barisentry_label.setStyleSheet(label_stylesheet1)
        self.barisentry_label.setText('')

        self.rootpath_go = QPushButton('Go')
        self.rootpath_go.setStyleSheet(push_button_stylesheet)
        self.rootpath_go.setToolTip('Recreate buttons\nrootpath harus sudah terisi')
        self.rootpath_go.clicked.connect(self.recreate_buttons) # rootpath hrs sudah terisi

        save_button = QPushButton('Save')
        save_button.setStyleSheet(push_button_stylesheet)
        save_button.setToolTip('Save guicode')
        save_button.clicked.connect(lambda: self.guicode_editor.save_file.emit(True))
        # toolbar_layout.addStretch(1)
        # antara Go dan Clear kasih top dan bottom utk toggle atas bawah
        toggle_layout = QHBoxLayout()


        self.button_f12 = QPushButton('F12')
        self.button_f12.setStyleSheet(push_button_stylesheet)
        self.button_f12.setToolTip('Edit last file')
        self.button_f12.clicked.connect(self.edit_last_file)

        self.button_sidoarjo = QPushButton("Sido")
        self.button_sidoarjo.clicked.connect(lambda: mulai(exec_code_sidoarjo))
        self.button_sidoarjo.setStyleSheet(button_stylesheet1)
        self.button_editors = QPushButton("Editors")
        self.button_editors.setMenu(create_menu_editors(self))
        self.button_editors.setStyleSheet(button_stylesheet1)
        # self.button_editors.clicked.connect(lambda: mulai(exec_notepad, ()))
        self.button_edit_files = QPushButton("Edit files")
        self.button_edit_files.setMenu(create_menu_cmds(self))
        self.button_edit_files.setStyleSheet(button_stylesheet1)
        # deactivate, 8-jul-23
        # toggle_layout.addWidget(toggle_top)  # top
        # deactivate, 8-jul-23
        # toggle_layout.addWidget(toggle_bot)  # bot
        toggle_layout.addWidget(self.button_f12)
        if make_mkcommand_button:
            self.mkcommand_button = QPushButton("Perintah")
            # from mkcommand import create_menu_mkcommand
            # self.mkcommand_menu = create_menu_mkcommand(self)
            # self.mkcommand_menu.addSeparator()
            # def reload_mkcommand(parent):
            #     parent.mkcommand_button.setMenu(parent.mkcommand_menu)
            # # self.mkcommand_menu.addAction("Reload", lambda: os.system(f"code {filePath}"))
            # self.mkcommand_button.setMenu(self.mkcommand_menu)
            self.mkcommand_button.setStyleSheet(button_stylesheet1)
            self.mkcommand_button.setMenu(self.set_mkcommand_menu())
            toggle_layout.addWidget(self.mkcommand_button)

        toolbar_layout = QVBoxLayout()
        toolbar_layout.addWidget(self.rootpath_label)
        toolbar_layout.addWidget(self.filepath_label)
        toolbar_layout.addWidget(self.barisentry_label)
        # toolbar_layout.addLayout(toggle_layout)
        # toolbar_layout.addWidget(clear_button)
        toolbar_horizontal = QHBoxLayout()
        toolbar_horizontal.addWidget(self.rootpath_go)
        # deactivate, 8-jul-23
        # toolbar_horizontal.addWidget(clear_button)  # Clear
        # deactivate, 8-jul-23
        # toolbar_horizontal.addWidget(self.toggle_expansion_button)  # Exp
        toolbar_horizontal.addWidget(self.button_sidoarjo)
        toolbar_horizontal.addWidget(self.button_editors)
        toolbar_horizontal.addWidget(self.button_edit_files)
        toolbar_horizontal.addLayout(toggle_layout)
        toolbar_layout.addLayout(toolbar_horizontal)
        
        sejajar = QHBoxLayout()
        sejajar.addLayout(toolbar_layout)
        sejajar.addWidget(self.flowwidget)
        # self.main_layout.addWidget(self.rootpath_label, 1)

        top_wrapper = QWidget()
        top_wrapper.setLayout(sejajar)
        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.addWidget(top_wrapper)
        self.splitter.addWidget(self.guicode_editor)
        self.splitter.setStretchFactor(0, self.factor_top)
        self.splitter.setStretchFactor(1, self.factor_bottom)
        self.splitter.handle(1).setStyleSheet('background: 3px blue;')

        self.main_layout = QVBoxLayout()
        # self.main_layout.addLayout(sejajar, 3)
        # self.main_layout.addLayout(editorlayout, 7)
        self.main_layout.addWidget(self.splitter)
        self.setLayout(self.main_layout)

        self.handle_signals()

        # toggle_top.setChecked(True)
        # toggle_bot.setChecked(True)

        # terakhir extra_buttons_to_connect_to_editor konek kan ke dummy handler
        # entah kenapa, walaupun konek ke dummy_terima_data tapi masuk juga ke guicode_editor_insert_data
        # mungkin gara2 nama signal yg sama
        for btn in self.extra_buttons_to_connect_to_editor:
            # btn.property('object_wrapper').button_data_signal.connect(self.dummy_terima_data)
            # btn.parent().button_data_signal.connect(self.dummy_terima_data)
            # btn.button_data_signal.connect(self.dummy_terima_data)
            # btn.button_data_signal.connect(self.guicode_editor_insert_data)
            btn.new_button_data_signal.connect(self.guicode_editor_insert_data)

    def handle_signals(self):
        self.guicode_editor.save_file.connect(self.save_file)
        self.guicode_editor.replrequest.connect(self.handle_ctrl_k_replrequest)
        # self.guicode_editor.fmusrequest.connect(self.handle_ctrl_m_fmusrequest)
        self.guicode_editor.fmus_repl_request.connect(self.handle_ctrl_k)
        self.guicode_editor.englishrequest.connect(self.handle_ctrl_w_writerservice)
        self.guicode_editor.publishrequest.connect(self.handle_redis_publish_request)

    def handle_redis_publish_request(self, code):
        handle_publish_to_redis(code)

    def handle_ctrl_w_writerservice(self, code):
        from schnell.db.writer_service import process_writer
        result = process_writer(code)
        indah4(result)
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

    def clear_guicode(self):
        self.guicode_editor.setText('')
        # self.editor_tab.setCurrentIndex(0)

    def toggle_expansion(self):
        global_context['fmus_expansion_mode'] = not global_context['fmus_expansion_mode']

    def guicode_editor_insert_data(self, text):
        """
        insert content dari file.mk:barisentry atau file.fmus:barisentry ke editor
        file.mk/fmus -> self.last_file -> filepath_label
        barisentry -> self.last_entry -> barisentry_label
        """
        # line, index = self.guicode_editor.getCursorPosition()
        # self.guicode_editor.insertAt(text, line, index)
        # self.guicode_editor.setText(text)
        # filepath, baris_entry = text.rsplit(':', 1)

        # FileNotFoundError: [Errno 2] No such file or directory:
        # 'C:/Users/usef/work/sidoarjo/database/refcards/karya.mk:load schnell .env for windows, envfile = "c'
        # load schnell .env for windows, envfile = "c'
        # utk baris entry:
        # load schnell .env for windows, envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
        if '.mk:' in text:
            filepath, baris_entry = text.split('.mk:')
            self.last_file = filepath + '.mk'
        else:
            filepath, baris_entry = text.split('.fmus:')
            self.last_file = filepath + '.fmus'
        self.filepath_label.setText(self.last_file.removeprefix(sidoarjo_absolute))
        self.barisentry_label.setText(baris_entry)
        self.last_entry = baris_entry
        content, self.lineno = get_definition_by_key_permissive_start_with_lineno(self.last_file, self.last_entry)
        if content:
            self.guicode_editor.setContent(content)
            if self.copy_after_insert:
                pyperclip.copy(content)

    def reopen_last_file(self):
        if self.last_filepath_barisentry:
            self.guicode_editor_insert_data(self.last_filepath_barisentry)
            # print('[mkhelp] opening {self.last_filepath_barisentry}.')
        # else:
        #     print('[mkhelp] NOT opening {self.last_filepath_barisentry}.')

    def save_file(self, _):
        """
        cek gimana jk 
        user sudah buka, last_file terset....
        """
        if self.last_file and self.last_entry:
            file_content = self.guicode_editor.text()
            # print(f"""[mkhelp][save_file]
            # self.last_file = [{self.last_file}]
            # self.last_entry = [{self.last_entry}]
            # """)
            replace_entry_in_mkfile(self.last_entry, file_content, self.last_file)
        else:
            print('mkhelp editor: self.last_file not set')


def main():
    app = QApplication([])
    if len(sys.argv)==2:
        argument = sys.argv[1]
        if argument == '.':
            argument = os.getcwd()
        window = MKHelpWidget(rootpath=argument)
    else:
        window = MKHelpWidget()
    window.setStyleSheet(background_image_stylesheet)
    # window.setWindowTitle('Mortal Kombat')
    resize_screen_ratio_wrapper_simple(window,x=0.4,w=0.6,delta=50,centering=False)  # ini agar geser kanan, 3/4 dibagi 2
    window.setWindowIcon(QIcon(joiner(sidoarjodir, 'editor.png')))
    # window.setWindowIcon(QIcon(joiner(sidoarjodir, 'editor.ico')))
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
