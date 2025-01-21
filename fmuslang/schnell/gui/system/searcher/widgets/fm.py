import os, sys, tempfile
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *
from PyQt5.QtWebEngineWidgets import *

from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent.parent.parent.parent)
#                              file        wid    sea    sys    gui    sch    sido
sys.path.append(sidoarjodir)

from constants import APPGENDIR, filemanager_background_style
from schnell.app.appconfig import programming_data
from schnell.app.dirutils import normy, explore, joiner, files_filter, bongkar
from schnell.app.fileutils import get_daftar, get_definition_by_key_permissive_start, file_content, not_binary, get_extension
from schnell.app.imageutils import ImageView
from schnell.app.redisquiutils import redis_subscribe_image
from schnell.app.stringutils import uuid1
from schnell.app.threadutils import mulai
from schnell.app.utils import env_get

# from schnell.gui.system.searcher.widgets.tkeditor import tkeditor
# from schnell.gui.system.searcher.widgets.serverhttp import ServerHttpWidget
# from schnell.gui.system.searcher.widgets.quicklangs import QuickLangsWidget
# from schnell.gui.system.searcher.widgets.actorwidget import ActorWidget
from schnell.gui.system.searcher.widgets.mkhelp import MKHelpWidget
from schnell.gui.system.searcher.widgets.guilangwidget import GuilangWidget

from schnell.gui.system.searcher.widgets.quickviewer import QuickViewerWidget

from schnell.gui.system.searcher.widgets.common import (
    MkfileButton,
    get_icon,
    BlueButton,
    context_menu_stylesheet,
    resize_screen_ratio_wrapper,
    bahasa_filepaths,
    context_menu_for_dirs_with_entries,
    context_menu_for_files_with_entries,
    predefined_commands,
    yarn_add_packages_dev,
    yarn_add_packages,
    mkhelp_initial_path,
    snippets_initial_path,
    epmus_initial_path,
)
from schnell.gui.system.searcher.widgets.filetreewidget import FileTreeWidget
from schnell.gui.system.searcher.widgets.quickbundle import QuickBundleWidget
# from schnell.gui.system.searcher.widgets.quickconfigurable import QuickConfigurableWidget
# from schnell.gui.system.searcher.widgets.karyawidget import KaryaWidget
# from schnell.gui.system.searcher.widgets.dailywidget import DailyWidget
# from schnell.gui.system.searcher.widgets.lshelp import LSHelpWidget


import ctypes
myappid = 'fulgent.de.fmus.tools.0.0.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class FileManager(QWidget):

    def show_image_redis_subscribe(self, filepath):
        print(f'[fm.py][show_image_redis_subscribe] => {filepath}.')
        self.show_image(filepath)

    def __init__(self, publisher=None):
        super().__init__()
        self.publisher = publisher
        # self.gptchat = gptchat  # AttributeError: can't set attribute 'gptchat'
        self.gptchat = None
        # self.subsciber = redis_subscribe_image(callback=lambda filepath: self.show_image(filepath))
        self.initUI()
        self.subsciber = redis_subscribe_image(self.show_image_redis_subscribe)

    def setGptChat(self, gptchat):
        print('FM, set gptchat to', gptchat)
        self.gptchat = gptchat

    def insert_gpt_help(self):
        content = file_content(joiner(sidoarjodir, 'database/zpt/gpt-help.txt'))
        self.tab_chatgpt.guicode_editor.insert_at_top.emit(content)

    def initUI(self):

        self.main_layout = QHBoxLayout()
        self.main_tab = QTabWidget(self)

        self.setWindowTitle('FM' + f" [{uuid1()}]")
        self.setWindowIcon(QIcon(joiner(env_get('ULIBPY_ROOTDIR'), 'fmus-fmus.png')))

        self.quickviewer_tab = QWidget(self)
        self.quickviewer_tab.setStyleSheet('background-color: tan;')
        layout_for_quickviewer_tab = QVBoxLayout(self.quickviewer_tab)
        self.quickviewer = QuickViewerWidget()
        layout_for_quickviewer_tab.addWidget(self.quickviewer)
        self.main_tab.addTab(self.quickviewer_tab, 'Viewer')

        # self.hf = BrowseHuggingFace()
        # self.oa = BrowseOpenAssistant()
        # self.main_tab.addTab(self.hf, 'HF')
        # self.main_tab.addTab(self.oa, 'OA')
        # self.bard = BrowseWebsite('https://bard.google.com/')
        # self.main_tab.addTab(self.bard, 'Bad')
        bundle2 = QuickBundleWidget(programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['fm']['quickbundlewidget_quick'])
        # bundle2 = QuickBundleWidget([
        #     'quick-js.json',
        #     'quick-c.json',
        #     'quick-py.json',
        #     'quick-java.json',
        #     'quick-do.json',
        #     'quick-rust.json',
        #     'quick-riset.json',
        #     'quick-karya.json',
        #     'quick-upw.json',
        #     'quick-db.json',
        #     'quick-mobile.json',
        #     'quick-cloud.json',
        #     'quick-ext.json',
        #     'quick-api.json',
        #     'quick-htmlcss.json',
        # ])
        self.main_tab.addTab(bundle2, 'QUICKS')

        # epmus mkhelp
        u_button = QPushButton('u')
        # u_button.clicked.connect(lambda: os.system(f"u"))        
        u_button.clicked.connect(lambda: mulai(os.system, 'u'))
        # tambah C:\Users\usef\work\sidoarjo\providers\directories\docker-compose.mk
        dockercompose_button = MkfileButton('ULIBPY_ROOTDIR/providers/directories/docker-compose.mk')
        # dockercompose_button = dockercompose_button_obj.mkfile_to_button()
        android_coords_button = MkfileButton('ULIBPY_ROOTDIR/providers/directories/android-coords.mk')
        appgen_coords_button = MkfileButton('ULIBPY_ROOTDIR/providers/directories/appgen-coords.mk')
        appgen_coords2_button = MkfileButton('ULIBPY_ROOTDIR/providers/directories/appgen-coords2.mk')
        appgenfs_button = MkfileButton('ULIBPY_ROOTDIR/providers/directories/appgen-fs.mk')
        # appgen_generated = MkfileButton(joiner(APPGENDIR, 'appgen.fmus'))  # matikan 4/12/23
        byexamples_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/byexamples.fmus')
        # byexamples_go_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/byexamples-go.fmus')
        byexamples_java_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/byexamples-java.fmus')
        byexamples_jsts_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/byexamples-jsts.fmus')
        byexamples_rs_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/byexamples-rust.fmus')
        firebase_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/firebase.fmus')
        ml_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/ml.fmus')
        vamp_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/vamp.fmus')
        # webrtc_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/webrtcasm.fmus')
        karya_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/karya.fmus')
        rwe_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/rwe.fmus')
        nextjs_button = MkfileButton('ULIBPY_ROOTDIR/data/by-examples/nextjs.fmus')
        draftprojects_button = MkfileButton('ULIBPY_ROOTDIR/data/draft-projects/draftprojects.fmus')
        provider_names = [
            'batchers.mk',
            # 'corona.mk',
            'devops.mk',
            'flutter-coords.mk',
            # 'gql-frontend.mk',
            # 'graphql.mk',
            # 'prisma.mk',
            'ts_js_go_java_py.mk',
            'karya-mobile.mk',
        ]
        provider_list = [MkfileButton(f'ULIBPY_ROOTDIR/providers/directories/{item}') for item in provider_names]
        self.tab_epmus = MKHelpWidget(parent=self, rootpath=epmus_initial_path,
            # copy_after_insert=True, # kita matikan ini gak perlu lagi.
            # extra_buttons=[u_button, dockercompose_button],
            # extra_buttons_to_connect_to_editor=[dockercompose_button])
            extra_buttons=[u_button,
                dockercompose_button.get_button(),
                android_coords_button.get_button(),
                *[item.get_button() for item in provider_list],
                karya_button.get_button(),
                appgen_coords_button.get_button(),
                appgen_coords2_button.get_button(),
                appgenfs_button.get_button(),
                # appgen_generated.get_button(),
                firebase_button.get_button(),
                ml_button.get_button(),
                vamp_button.get_button(),
                # webrtc_button.get_button(),
                rwe_button.get_button(),
                nextjs_button.get_button(),
                draftprojects_button.get_button(),
                byexamples_button.get_button(),
                # byexamples_go_button.get_button(),
                byexamples_java_button.get_button(),
                byexamples_jsts_button.get_button(),
                byexamples_rs_button.get_button(),
                ],
            extra_buttons_to_connect_to_editor=[dockercompose_button,
                android_coords_button,
                *[item for item in provider_list],
                appgen_coords_button,
                appgen_coords2_button,
                appgenfs_button,
                # appgen_generated,
                byexamples_button,
                firebase_button,
                draftprojects_button,
                ml_button, vamp_button,
                # webrtc_button,
                karya_button, rwe_button, nextjs_button,
                # byexamples_go_button,
                byexamples_java_button,
                byexamples_jsts_button,
                byexamples_rs_button,
                ])
        # )
        # dockercompose_button.button_data_signal.connect(self.tab_epmus.dummy_terima_data)
        self.main_tab.addTab(self.tab_epmus, 'Epmus')

        self.tab_backendlang = MKHelpWidget(parent=self, rootpath=bongkar('ULIBPY_ROOTDIR/database/backendlang'))
        self.main_tab.addTab(self.tab_backendlang, 'BE')

        self.tab_guilang = MKHelpWidget(parent=self, rootpath=bongkar('ULIBPY_ROOTDIR/database/by-langs/guilang'))
        self.main_tab.addTab(self.tab_guilang, 'GUI')

        # # matikan 4-des-23
        # bundle = QuickBundleWidget(programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['fm']['quickbundlewidget_e'])
        # self.main_tab.addTab(bundle, 'E')
        bundle3 = QuickBundleWidget(programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['fm']['quickbundlewidget_misclang'])
        self.main_tab.addTab(bundle3, 'Misclang')

        # create = QuickConfigurableWidget('ULIBPY_ROOTDIR/schnell/data/create/create-a.json',)
        # self.main_tab.addTab(create, 'CRE')

        # # 4-des-2023, matikan actor widget
        # self.tab_actor = QWidget(self)
        # self.tab_actor.setStyleSheet('background-color: tan;')
        # actor_layout = QHBoxLayout(self.tab_actor) # utk content tab 1
        # self.actor_widget = ActorWidget()
        # actor_layout.addWidget(self.actor_widget)
        # self.main_tab.addTab(self.tab_actor, 'ACTOR')

        # 4 des 23, matikan 'bahas'
        # lshelp = LSHelpWidget()
        # self.main_tab.addTab(lshelp, 'BAHAS')

        self.tab_guilang = QWidget(self)
        self.tab_guilang.setStyleSheet('background-color: tan;')
        layout_for_tab_guilang = QVBoxLayout(self.tab_guilang) # utk content tab 2
        layout_for_tab_guilang.addWidget(GuilangWidget())
        self.main_tab.addTab(self.tab_guilang, 'Guilang')

        # # matikan 4 dec 2023
        # self.tab_server = QWidget(self)
        # self.tab_server.setStyleSheet('background-color: tan;')
        # tab1_pagelayout_0 = QHBoxLayout(self.tab_server) # utk content tab 1
        # self.server_http = ServerHttpWidget(self.publisher)
        # # self.browsing_http = BrowsingHttpWidget()
        # tab1_pagelayout_0.addWidget(self.server_http)
        # # tab1_pagelayout_0.addWidget(self.browsing_http)
        # self.main_tab.addTab(self.tab_server, 'Server')

        # # matikan 4-12-23
        # self.quick_langs_widget = QuickLangsWidget()
        # self.quick_langs_widget.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.quick_langs_widget, 'Quick Langs')

        # self.tab_dahsyater = DahsyaterWidget()
        # self.tab_dahsyater.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.tab_dahsyater, 'Dahsyater')
        # self.csvlanger = CsvlangWidget()
        # # self.csvlanger.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.csvlanger, 'Csvlang')
        # self.replanger = ReplangWidget()
        # self.replanger.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.replanger, 'Replang')
        # self.framelanger = FramelangWidget()
        # self.framelanger.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.framelanger, 'Framework lang')
        # self.tab_lalangwidget = LalangWidget()
        # self.tab_lalangwidget.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.tab_lalangwidget, 'Lalang')
        # self.tab_fakerlang = FakerlangWidget()
        # self.tab_fakerlang.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.tab_fakerlang, 'Fakerlang')

        # # self.tab_cmder = QWidget(self)
        # # self.tab_cmder.setStyleSheet('background-color: tan;')
        # # layout_for_tab_cmder = QVBoxLayout(self.tab_cmder) # utk content tab 2
        # # layout_for_tab_cmder.addWidget(self.cmder)
        # self.color_widget = ColorWidget()
        # self.button_widget = ButtonWidget()
        # self.cmder = CmderWidget()
        # cmder_color = QSplitter(Qt.Horizontal)
        # cmder_color.addWidget(self.cmder)
        # cmder_color.addWidget(self.color_widget)
        # cmder_color_button = QSplitter(Qt.Vertical)
        # cmder_color_button.addWidget(cmder_color)
        # cmder_color_button.addWidget(self.button_widget)
        # self.main_tab.addTab(cmder_color_button, 'Cmder')

        # self.windower = WindowerWidget()
        # self.windower.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.windower, 'Windower')

        # self.repoallwidget = RepoAllWindow()
        # self.repoallwidget.setStyleSheet('background-color: tan;')
        # self.main_tab.addTab(self.repoallwidget, 'Github Repo')

        # dari 340 ke 600mb footprint
        # self.tab_languages = QWidget(self)
        # self.tab_languages.setStyleSheet('background-color: tan;')
        # layout_for_tab_languages = QVBoxLayout(self.tab_languages) # utk content tab 2
        # self.stackoverflow = StackOverflowWidgetBase()
        # layout_for_tab_languages.addWidget(self.stackoverflow)
        # self.main_tab.addTab(self.tab_languages, 'SO')

        # self.main_tab.currentChanged.connect(lambda page: print(f'tab self.main_tab page {page}'))
        self.imageview = ImageView(image=bongkar('ULIBPY_ROOTDIR/fmus.jpg'), background=Qt.black)
        self.imageview.hide()

        # mending kita ubah ke splitter...
        self.file_tree = FileTreeWidget()
        # self.file_tree.setStyleSheet('background-color: bisque; min-width: 300px;')
        self.file_tree.setStyleSheet('background-color: bisque;')

        # 4-12-23, quick-langs dan server-http dimatikan
        # self.file_tree.request_cmd.connect(self.quick_langs_widget.cmder.create_cmd)
        # self.file_tree.request_wsl.connect(self.quick_langs_widget.cmder.create_cmd_and_type_away)
        # self.file_tree.request_docker_compose_up.connect(lambda workingDir: self.quick_langs_widget.cmder.create_cmd_and_type_away(workingDir, ['wsl', '', '', 'docker-compose up']))
        # self.file_tree.set_rootpath.connect(self.quick_langs_widget.tab_dahsyater.change_rootpath)

        # self.file_tree.set_rootpath.connect(self.server_http.change_rootpath)

        # new_file_clicked sudha dipastikan non-binary file
        # self.file_tree.new_file_clicked.connect(lambda filepath: self.quickviewer.editor.setText(file_content(filepath)))
        self.file_tree.new_file_clicked.connect(lambda filepath: self.quickviewer.set_filepath(filepath))
        self.file_tree.imagefile_clicked.connect(lambda filepath: self.quickviewer.set_imagepath(filepath))
        self.file_tree.pdffile_clicked.connect(lambda filepath: self.quickviewer.set_pdfpath(filepath))

        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_splitter.addWidget(self.file_tree)
        self.main_splitter.addWidget(self.main_tab)
        self.main_splitter.setHandleWidth(8)
        self.main_splitter.handle(1).setStyleSheet('background: 3px blue;')
        self.main_splitter.setStretchFactor(0, 4)
        self.main_splitter.setStretchFactor(1, 6)
        # self.main_layout.addWidget(self.flow_buttons, 4)
        # self.main_layout.addLayout(editorlayout, 6)
        self.main_layout.addWidget(self.main_splitter)

        self.setLayout(self.main_layout)

        # self.resize(1300, 900)
        # self.setWindowTitle('File Manager')
        # resize_screen_ratio_wrapper(self, posx_ratio=0.4, posy_ratio=0.25, w_ratio=1, h_ratio=.95)
        # 13/12/22 matikan, krn showmaximized di clock.py
        resize_screen_ratio_wrapper(self, posy_ratio=0.4, w_ratio=0.95, h_ratio=.9)

    def setRedisPublisher(self, publisher):
        """
        from make_redis_help import redis_publish
        self.internal_clocker.setRedisPublisher(redis_publish)
        """
        self.publisher = publisher
        # matikan 4-12-23
        # self.server_http.setRedisPublisher(self.publisher)

    def show_image(self, filepath):
        self.imageview.setPixmap(filepath)
        self.imageview.show()

    def show_image_from_url(self, urlpath):
        with urllib.request.urlopen(urlpath) as response:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(response.read())
                tmp_file_path = tmp_file.name

        if os.path.isfile(tmp_file_path):
            # subprocess.call([photos_exe, tmp_file_path])
            # os.remove(tmp_file_path)
            self.show_image(tmp_file_path)


def main():
    app = QApplication([])
    ex = FileManager()
    ex.setStyleSheet(filemanager_background_style)
    # ex.show()
    ex.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
