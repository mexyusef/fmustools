from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

# main window
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, alamat="http://www.google.com", *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.alamat = alamat
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)

        # adding action when double clicked
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        # adding action when tab is changed
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # making tabs closeable
        self.tabs.setTabsClosable(True)

        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # making tabs as central widget
        self.setCentralWidget(self.tabs)

        # creating a status bar
        self.status = QStatusBar()

        # setting status bar to the main window
        self.setStatusBar(self.status)

        # creating a tool bar for navigation
        self.navtb = QToolBar("Navigation")

        # adding tool bar tot he main window
        self.addToolBar(self.navtb)

        # creating back action
        back_btn = QAction("Back", self)

        # setting status tip
        back_btn.setStatusTip("Back to previous page")

        # adding action to back button
        # making current tab to go back
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        # adding this to the navigation tool bar
        self.navtb.addAction(back_btn)

        # similarly adding next button
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        self.navtb.addAction(next_btn)

        # similarly adding reload button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        self.navtb.addAction(reload_btn)

        # creating home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")

        # adding action to home button
        home_btn.triggered.connect(self.navigate_home)
        self.navtb.addAction(home_btn)

        # adding a separator
        self.navtb.addSeparator()

        # creating a line edit widget for URL
        self.urlbar = QLineEdit()

        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding line edit to tool bar
        self.navtb.addWidget(self.urlbar)

        # similarly adding stop action
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        self.navtb.addAction(stop_btn)

        # creating first tab
        self.add_new_tab(QUrl(self.alamat), "Homepage")

        # showing all the components
        self.show()

        # setting window title
        self.setWindowTitle("KBREPL")

    # method for adding new tab
    def add_new_tab(self, qurl=None, label="Blank", text="New Tab"):

        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl("http://www.google.com")

        # creating a QWebEngineView object
        browser = QWebEngineView()
        browser.settings().setAttribute(
            QWebEngineSettings.FullScreenSupportEnabled, True
        )

        # setting url to browser
        browser.setUrl(qurl)

        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_urlbar(qurl, browser)
        )

        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(
                i, browser.page().title()
            )
        )

        browser.page().fullScreenRequested.connect(
            lambda request, browser=browser: self.handle_fullscreen_requested(
                request, browser
            )
        )

    def handle_fullscreen_requested(self, request, browser):
        request.accept()

        if request.toggleOn():
            self.showFullScreen()
            self.statusBar().hide()
            self.navtb.hide()
            self.tabs.tabBar().hide()
        else:
            self.showNormal()
            self.statusBar().show()
            self.navtb.show()
            self.tabs.tabBar().show()

    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # wen tab is changed
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

    # action to go to home
    def navigate_home(self):

        # go to google
        self.tabs.currentWidget().setUrl(QUrl(self.alamat))

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
    def update_urlbar(self, q, browser=None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():

            return

        # set text to the url bar
        self.urlbar.setText(q.toString())

        # set cursor position
        self.urlbar.setCursorPosition(0)

        def _downloadRequested(item):  # QWebEngineDownloadItem
            print("downloading to", item.path())
            item.accept()

        browser.page().profile().downloadRequested.connect(_downloadRequested)

def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, delta = 60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    lebar, tinggi = int(screenw*ratio),int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)

def main(alamat=None):
    app = QApplication(sys.argv)
    # setting name to the application
    app.setApplicationName("KBREPL")
    if alamat:
        # print('IE beralamat:', alamat)
        window = MainWindow(alamat)
    else:
        # print('IE tanpa alamat:')
        window = MainWindow()
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    scrw, scrh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(window, scrw, scrh, ratio=3/4)
    app.exec_()

# https://stackoverflow.com/questions/66294413/how-to-create-full-screen-mode-for-youtube-videos-in-pyqt5-webbrowser

if __name__ == '__main__':
    main()
