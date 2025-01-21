
import os, random, string, sys
import re, requests
from bs4 import BeautifulSoup
import bs4

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *


initial_page = 1
max_pages = 50
default_tag = 'python'

background_image_stylesheet = '''
StackOverflowWidget {
    border-image: url("bg.jpg");
    background-repeat: no-repeat; 
    background-position: center;
}
'''


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, posy_ratio=1/2, w_ratio=1/6, h_ratio=0, delta=60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)
    object, screenw, screenh, posx_ratio=1/2, posy_ratio=1/2, w_ratio=1/6, h_ratio=0, delta=60

    object hrs punya method resize dan move.
    """
    if h_ratio <= 0:
        h_ratio = w_ratio
    if posy_ratio <= 0:
        posy_ratio = posx_ratio
    lebar, tinggi = int(screenw*w_ratio), int(screenh*h_ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)
    posy = int((screenh-tinggi)*posy_ratio) - delta
    object.move(posx, posy)


def get_data_stackoverflow(prefix_url = 'https://stackoverflow.com', code = f'{default_tag} {initial_page}'):
    """
    qt.so 2
    qt.so python 5
    qt.so rust
    """
    default_parser = 'html.parser'
    so_url = f'{prefix_url}/questions__TAG__?tab=newest&pagesize=50__PAGE__'
    # tag_tpl = '/tagged/python'
    # page_tpl = '&page=5'
    m = re.match(r'([A-Za-z]+)?\s*(\d+)?', code).groups()
    # (None, '9')
    # ('rust ', '9')
    # ('rust', None)
    if m[0] or m[1]:
        if m[0]:
            so_url = so_url.replace('__TAG__', '/tagged/'+m[0])
        else:
            so_url = so_url.replace('__TAG__', '')
        if m[1]:
            so_url = so_url.replace('__PAGE__', '&page='+m[1])
        else:
            so_url = so_url.replace('__PAGE__', '')
    else:
        so_url = so_url.replace('__TAG__', '')
        so_url = so_url.replace('__PAGE__', '')

    isi = requests.get(so_url).content
    soup = BeautifulSoup(isi, default_parser)
    doctype, html = [item for item in list(soup.children) if type(item) is not bs4.element.NavigableString]
    head, body = [item for item in list(html.children) if type(item) is not bs4.element.NavigableString]

    # question_links = body.findAll('a', class_='s-link')
    # question_links = [item for item in question_links if item.attrs['href'].startswith('/questions/')]
    # satu = [item.text for item in question_links]
    # dua = [prefix_url+item.attrs['href'] for item in question_links]
    # return [{'title': a, 'url': b} for (a,b) in zip(satu,dua)]
    results = []
    blocks = body.findAll('div', class_='s-post-summary')
    for block in blocks:
        stat_links = block.findAll('div', class_='s-post-summary--stats')[0]
        question_links = block.findAll('div', class_='s-post-summary--content')[0]
        stat = stat_links.findAll('div', class_='s-post-summary--stats-item')[1]
        stat = stat.find('span')
        answers = stat.text
        q_link = question_links.find('a')
        text = q_link.text
        url = prefix_url+q_link.attrs['href']
        d_sum = question_links.findAll('div', class_='s-post-summary--content-excerpt')[0]
        summary = d_sum.text.strip()
        tags = question_links.findAll('div', class_='s-post-summary--meta-tags')[0]
        tags_ref = tags.findAll('a')
        tags = ', '.join([a.text for a in tags_ref])

        item = {
            'title': text,
            'url': url,
            'summary': summary,
            'answers': answers,
            'tags': tags,
        }
        results.append(item)
    return results


class BrowserWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(BrowserWindow, self).__init__(*args, **kwargs)
        self.tabs = QTabWidget()
        self.urls = []
        self.default_url = 'http://www.google.com'        
        self.tabs.setDocumentMode(True)  # making document mode true		
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)  # adding action when double clicked		
        self.tabs.currentChanged.connect(self.current_tab_changed)  # adding action when tab is changed		
        self.tabs.setTabsClosable(True)  # making tabs closeable		
        self.tabs.tabCloseRequested.connect(self.close_current_tab)  # adding action when tab close is requested		
        self.setCentralWidget(self.tabs)  # making tabs as central widget
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navtb = QToolBar("Navigation")  # creating a tool bar for navigation		
        self.addToolBar(navtb)  # adding tool bar tot he main window		
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        # adding action to back button
        # making current tab to go back
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        # similarly adding reload button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)
        # creating home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        # adding action to home button
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        # adding a separator
        navtb.addSeparator()
        # creating a line edit widget for URL
        self.urlbar = QLineEdit()
        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        # adding line edit to tool bar
        navtb.addWidget(self.urlbar)
        # similarly adding stop action
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)
        # creating first tab
        self.add_new_tab(self.default_url, 'Homepage')
        
        self.setWindowTitle("My Browser")
        self.hide()

    def new_url(self, alamat):
        self.add_new_tab(alamat, alamat.removeprefix('https://'))

    def add_new_tab(self, qurl = None, label ="Blank"):
        if qurl is None:
            qurl = self.default_url
        if qurl in self.urls:
            self.tabs.setCurrentIndex(self.urls.index(qurl))
            return
        self.urls.append(qurl)
        qurl = QUrl(qurl)
        browser = QWebEngineView()
        browser.setZoomFactor(1.5)
        browser.setUrl(qurl)  # setting url to browser        
        i = self.tabs.addTab(browser, label)  # setting tab index
        self.tabs.setCurrentIndex(i)
        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser = browser: self.update_urlbar(qurl, browser))
        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i = i, browser = browser: self.tabs.setTabText(i, browser.page().title()))

    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):
        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # when tab is changed
    def current_tab_changed(self, i):
        # get the curl
        qurl = self.tabs.currentWidget().url()
        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())
        # update the title
        self.update_title(self.tabs.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):
        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return
        # else remove the tab
        self.tabs.removeTab(i)

    # method for updating the title
    def update_title(self, browser):
        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return
        # get the page title
        title = self.tabs.currentWidget().page().title()
        # set the window title
        self.setWindowTitle("% s - Geek PyQt5" % title)

    # action to go to home
    def navigate_home(self):
        # go to google
        self.tabs.currentWidget().setUrl(QUrl(self.default_url))

    # method for navigate to url
    def navigate_to_url(self):
        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())
        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")
        # set the url
        self.tabs.currentWidget().setUrl(q)

    # method to update the url
    def update_urlbar(self, q, browser = None):
        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():
            return
        # set text to the url bar
        self.urlbar.setText(q.toString())
        # set cursor position
        self.urlbar.setCursorPosition(0)


class StackOverflowInternal(QWidget):

    url_signal = pyqtSignal(str)
    show_hide_state = pyqtSignal(bool)
    toggle_table_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.bold_font = QFont("Roman times", 12, QFont.Bold)
        try:
            self.data = get_data_stackoverflow()
        except:
            self.data = []
        self.initUI()

    def setContent(self):

        self.content.setRowCount(len(self.data))
        self.content.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        # https://stackoverflow.com/questions/38098763/pyside-pyqt-how-to-make-set-qtablewidget-column-width-as-proportion-of-the-a
        for i, row in enumerate(self.data):
            # print(f"{i}. {row}")
            # isi = f"[<font color='red'>{row['answers']}</font>][{row['tags']}] {row['title']}"
            isi = f"[{row['answers']}] {row['title']}"
            current_item = QTableWidgetItem(isi)
            current_item.setFont(self.bold_font)
            # current_item.setFont(QFont("Consolas", 12, QFont.Bold))
            tooltip = f"[<i>{row['tags']}</i>] <b>{row['summary']}</b>"
            current_item.setToolTip(tooltip)
            self.content.setItem(i, 0, current_item)
            # self.content.setItem(i, 0, QTableWidgetItem('palsu'))
            link_item = QTableWidgetItem(row['url'])
            tooltip2 = f"""<a href="{row['url']}"><u>{row['url']}</u></a>"""
            link_item.setToolTip(tooltip2)
            self.content.setItem(i, 1, link_item)

    def load_so(self):
        prefix = self.combo0.currentText()
        tag = self.edit_tag.text()
        page = self.page.value()
        print(f"""
        prefix      = {prefix}
        tag         = {tag}
        page        = {page}
        """)

        self.data = get_data_stackoverflow(prefix_url=prefix, code=f'{tag} {page}')
        # https://stackoverflow.com/questions/15848086/how-to-delete-all-rows-from-qtablewidget
        self.content.setRowCount(0)
        self.setContent()

    def toggle_table(self, state):
        self.toggle_table_signal.emit(state)
        self.content.setHidden(state)
        if self.toggle_table_button.isChecked():
            self.toggle_table_button.setText('Show table')
        else:
            self.toggle_table_button.setText('Hide table')

    def toggle_browser(self, state):
        self.show_hide_state.emit(state)
        if self.toggle_browser_button.isChecked():
            self.toggle_browser_button.setText('Show browser')
        else:
            self.toggle_browser_button.setText('Hide browser')

    def combo_change_index(self, index):
        print(index)
        self.edit_tag.setText('')

    def next_page(self):
        curpage = self.page.value()
        if curpage >= max_pages:
            return
        self.page.setValue(curpage+1)
        self.load_so()

    def prev_page(self):
        curpage = self.page.value()
        if curpage <= 1:
            return
        self.page.setValue(curpage-1)
        self.load_so()

    def setToolbar(self):
        self.tool_layout = QHBoxLayout()
        self.combo0 = QComboBox(self)
        self.combo0.addItems([
            'https://stackoverflow.com',
            'https://stackexchange.com',
            'https://ai.stackexchange.com',
            'https://android.stackexchange.com',
            'https://askubuntu.com',
            'https://bioinformatics.stackexchange.com',
            'https://codegolf.stackexchange.com',
            'https://codereview.stackexchange.com',
            'https://conlang.stackexchange.com',
            'https://cseducators.stackexchange.com',
            'https://cstheory.stackexchange.com',
            'https://datascience.stackexchange.com',
            'https://dba.stackexchange.com',
            'https://devops.stackexchange.com',
            'https://engineering.stackexchange.com',
            'https://gamedev.stackexchange.com',
            'https://gis.stackexchange.com',
            'https://languagelearning.stackexchange.com',
            'https://opensource.stackexchange.com',
            'https://pm.stackexchange.com',
            'https://puzzling.stackexchange.com',
            'https://reverseengineering.stackexchange.com',
            'https://scicomp.stackexchange.com',
            'https://security.stackexchange.com',
            'https://serverfault.com',
            'https://softwareengineering.stackexchange.com',
            'https://sqa.stackexchange.com',
            'https://stats.stackexchange.com',
            'https://superuser.com',
            'https://unix.stackexchange.com',
            'https://ux.stackexchange.com',
            'https://webapps.stackexchange.com',
            'https://webmasters.stackexchange.com',
            'https://writing.stackexchange.com',
        ])
        self.combo0.currentTextChanged.connect(lambda value: print(value))
        self.combo0.setStyleSheet('height: 32px; background-color: bisque; font-family: Consolas; font-size: 16px;')
        self.combo0.currentIndexChanged.connect(self.combo_change_index)
        # combo0.textChanged.connect(lambda value: print(value))
        self.tool_layout.addWidget(self.combo0)
        lbl1 = QLabel("Tag")

        self.tool_layout.addWidget(lbl1)
        self.edit_tag = QLineEdit("python")
        self.edit_tag.setStyleSheet('height: 32px; background-color: bisque; font-family: Consolas; font-size: 16px;')
        self.edit_tag.returnPressed.connect(self.load_so)
        self.tool_layout.addWidget(self.edit_tag)

        lbl3 = QLabel("Page")
        self.tool_layout.addWidget(lbl3)

        self.page = QSpinBox()
        self.page.setRange(1, max_pages)
        self.page.setValue(initial_page)
        self.page.valueChanged.connect(lambda value: print('val:', value))
        # spin4.textChanged.connect(lambda value: print('text:', value))
        self.tool_layout.addWidget(self.page)

        lefticon = QApplication.style().standardIcon(QStyle.SP_ArrowLeft)
        righticon = QApplication.style().standardIcon(QStyle.SP_ArrowRight)
        left = QPushButton(lefticon, "")
        right = QPushButton(righticon, "")
        left.setStyleSheet('padding: 5px; background-color: chocolate; font-family: Consolas; font-size: 16px;')
        right.setStyleSheet('padding: 5px; background-color: chocolate; font-family: Consolas; font-size: 16px;')
        left.clicked.connect(self.prev_page)
        right.clicked.connect(self.next_page)
        self.tool_layout.addWidget(left)        
        self.tool_layout.addWidget(right)

        self.tool_layout.addStretch(1)

        self.toggle_table_button = QPushButton("Toggle table")
        self.toggle_table_button.setCheckable(True)
        self.toggle_table_button.setChecked(True)
        self.toggle_table_button.setStyleSheet("""
            QPushButton {background:rgb(66, 66, 66); color: white;} 
            QPushButton::checked {background:rgb(255, 255, 0); color: blue;}
        """)
        self.tool_layout.addWidget(self.toggle_table_button)
        self.toggle_table_button.toggled.connect(lambda state: self.toggle_table(state))

        self.use_system_browser = QCheckBox("Use system browser")
        self.use_system_browser.stateChanged.connect(lambda state: print('use system browser' if state==Qt.Checked else 'use internal browser'))
        self.tool_layout.addWidget(self.use_system_browser)

        self.toggle_browser_button = QPushButton("Toggle browser")
        self.toggle_browser_button.setCheckable(True)
        self.toggle_browser_button.setChecked(True)
        self.toggle_browser_button.setStyleSheet("""
            QPushButton {background:rgb(66, 66, 66); color: white;} 
            QPushButton::checked {background:rgb(255, 255, 0); color: blue;}
        """)
        self.tool_layout.addWidget(self.toggle_browser_button)
        self.toggle_browser_button.toggled.connect(lambda state: self.toggle_browser(state))

        load_button = QPushButton("load")
        load_button.clicked.connect(self.load_so)
        self.tool_layout.addWidget(load_button)
        self.stackoverflow_layout.addLayout(self.tool_layout)

    def initUI(self):
        self.resize(1200, 800)
        self.stackoverflow_layout = QVBoxLayout()

        self.content = QTableWidget(self)
        self.setToolbar()

        column_labels = ['Title', 'URL']
        self.content.setColumnCount(len(column_labels))
        for i in range(1,len(column_labels)+1):
            item = QTableWidgetItem()
            self.content.setHorizontalHeaderItem(i, item)
        self.content.setHorizontalHeaderLabels(column_labels)
        self.stackoverflow_layout.addWidget(self.content)
        self.setContent()
        self.content.itemClicked.connect(self.onClicked)

        self.setLayout(self.stackoverflow_layout)
        self.setWindowTitle('Stackoverflow')

    @pyqtSlot(QTableWidgetItem)
    def onClicked(self, it):
        print('url:', it.text(), 'row:', it.row(), 'col:', it.column())
        if it.column()==1: # url
            alamat = it.text()
            if self.use_system_browser.isChecked():
                import webbrowser
                webbrowser.open_new(alamat)
            else:
                self.url_signal.emit(alamat)


class StackOverflow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print('so 001')
        self.main_layout = QVBoxLayout()
        stackoverflow_splitter = QSplitter(Qt.Vertical)
        print('so 002')
        widgetbrowser = BrowserWindow()
        print('so 003')
        stackoverflow_splitter.addWidget(widgetbrowser)
        stackoverflow_widget = StackOverflowInternal()
        stackoverflow_splitter.addWidget(stackoverflow_widget)
        print('so 004')
        stackoverflow_widget.url_signal.connect(widgetbrowser.new_url)
        stackoverflow_widget.show_hide_state.connect(widgetbrowser.setHidden)
        print('so 005')
        # https://stackoverflow.com/questions/29537762/pyqt-qsplitter-setsizes-usage
        # stackoverflow_widget.toggle_table_signal.connect(lambda state: stackoverflow_splitter.setStretchFactor(10,1) if state else stackoverflow_splitter.setStretchFactor(5,5))
        stackoverflow_widget.toggle_table_signal.connect(lambda state: stackoverflow_splitter.setSizes([500,100]) if state else stackoverflow_splitter.setSizes([400,400]))
        stackoverflow_splitter.handle(1).setStyleSheet('background: 3px blue;')
        print('so 006')
        self.main_layout.addWidget(stackoverflow_splitter)
        self.setLayout(self.main_layout)
        # self.resize(800, 600)
        self.setWindowTitle('Stackoverflow')
        print('so 007')

"""
TODO:
setiap ganti combobox maka tag dikosongkan
krn gak make sense ada tag "python" utk writing stackexchange misalnya.
"""


class CustomTitleBar(QWidget):

    clickPos = None

    def __init__(self, parent):
        super(CustomTitleBar, self).__init__(parent)
        self.setAutoFillBackground(True)
        
        self.setBackgroundRole(QPalette.Shadow)
        # alternatively:
        # palette = self.palette()
        # palette.setColor(palette.Window, Qt.black)
        # palette.setColor(palette.WindowText, Qt.white)
        # self.setPalette(palette)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addStretch()

        self.title = QLabel("My Own Bar", self, alignment=Qt.AlignCenter)
        # if setPalette() was used above, this is not required
        self.title.setForegroundRole(QPalette.Light)

        style = self.style()
        ref_size = self.fontMetrics().height()
        ref_size += style.pixelMetric(style.PM_ButtonMargin) * 2
        self.setMaximumHeight(ref_size + 2)

        btn_size = QSize(ref_size, ref_size)
        for target in ('min', 'normal', 'max', 'close'):
            btn = QToolButton(self, focusPolicy=Qt.NoFocus)
            layout.addWidget(btn)
            btn.setFixedSize(btn_size)

            iconType = getattr(style, 
                'SP_TitleBar{}Button'.format(target.capitalize()))
            btn.setIcon(style.standardIcon(iconType))

            if target == 'close':
                colorNormal = 'red'
                colorHover = 'orangered'
            else:
                colorNormal = 'palette(mid)'
                colorHover = 'palette(light)'
            btn.setStyleSheet('''
                QToolButton {{
                    background-color: {};
                }}
                QToolButton:hover {{
                    background-color: {}
                }}
            '''.format(colorNormal, colorHover))

            signal = getattr(self, target + 'Clicked')
            btn.clicked.connect(signal)

            setattr(self, target + 'Button', btn)

        self.normalButton.hide()

        self.updateTitle(parent.windowTitle())
        parent.windowTitleChanged.connect(self.updateTitle)

        self.gripSize = 16
        grip = QSizeGrip(self) # satu grip akan otomatis di kiri atas
        grip.resize(self.gripSize, self.gripSize)
        # self.grips = []
        # for _ in range(4):
        #     grip = QSizeGrip(self)
        #     grip.resize(self.gripSize, self.gripSize)
        #     self.grips.append(grip)

    def updateTitle(self, title=None):
        if title is None:
            title = self.window().windowTitle()
        width = self.title.width()
        width -= self.style().pixelMetric(QStyle.PM_LayoutHorizontalSpacing) * 2
        self.title.setText(self.fontMetrics().elidedText(
            title, Qt.ElideRight, width))

    def windowStateChanged(self, state):
        self.normalButton.setVisible(state == Qt.WindowMaximized)
        self.maxButton.setVisible(state != Qt.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    def closeClicked(self):
        self.window().close()

    def maxClicked(self):
        self.window().showMaximized()

    def normalClicked(self):
        self.window().showNormal()

    def minClicked(self):
        self.window().showMinimized()

    def resizeEvent(self, event):
        self.title.resize(self.minButton.x(), self.height())
        self.updateTitle()


class StackOverflowWidgetBase(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # self.titleBar = CustomTitleBar(self)
        # self.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.grips = []
        self.gripSize = 16
        for _ in range(2): # buat 2 grip utk ditaro di bawah ki-ka
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

        self.initUI()

    # def changeEvent(self, event):
    #     if event.type() == event.WindowStateChange:
    #         self.titleBar.windowStateChanged(self.windowState())

    # def resizeEvent(self, event):
    #     self.titleBar.resize(self.width(), self.titleBar.height())

    #     rect = self.rect()
    #     # # top right
    #     # self.grips[0].move(rect.right() - self.gripSize, 0)
    #     # bottom right
    #     self.grips[0].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    #     # bottom left
    #     self.grips[1].move(0, rect.bottom() - self.gripSize)

    def initUI(self):

        self.main_layout = QHBoxLayout()
        stackoverflow0 = StackOverflow()
        self.main_layout.addWidget(stackoverflow0)
        self.setLayout(self.main_layout)        
        self.setWindowTitle('Stackoverflow')
        self.setStyleSheet(background_image_stylesheet)


class StackOverflowWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.titleBar = CustomTitleBar(self)
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.grips = []
        self.gripSize = 16
        for _ in range(2): # buat 2 grip utk ditaro di bawah ki-ka
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

        self.initUI()

    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            self.titleBar.windowStateChanged(self.windowState())

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

        rect = self.rect()
        # # top right
        # self.grips[0].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[0].move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[1].move(0, rect.bottom() - self.gripSize)

    def initUI(self):

        self.main_layout = QHBoxLayout()
        stackoverflow0 = StackOverflow()
        self.main_layout.addWidget(stackoverflow0)
        self.setLayout(self.main_layout)
        self.setWindowTitle('Stackoverflow')
        self.setStyleSheet(background_image_stylesheet)


def main():
    app = QApplication([])
    ex = StackOverflowWidget()
    QShortcut(QKeySequence("Ctrl+Q"), ex, activated=lambda: qApp.quit())
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(ex, screenw, screenh, w_ratio=0.95, h_ratio=0.9)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
