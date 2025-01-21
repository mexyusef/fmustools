#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView #, QWebEngineSettings
# from os import path

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(0, 28, 1000, 750)

        self.webView = QWebEngineView()
        self.webView.urlChanged.connect(self.url_changed)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.setCentralWidget(self.webView)

    def url_changed(self):
        self.setWindowTitle(self.webView.title())

    def go_back(self):
        self.webView.back()

def main():    
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    alamat = 'file:///c:/users/usef/downloads/Semeru.pdf'
    print('buka', alamat)
    win.webView.load(QUrl(alamat))
    # if len(sys.argv) > 1:
    #     alamat = f"file://{sys.argv[1]}"
    #     alamat = 'file:///c:/users/usef/downloads/Semeru.pdf'
    #     print('buka', alamat)
    #     win.webView.load(QUrl(alamat))
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

