from PyQt5.QtWebEngineWidgets import QWebEngineView

class PdfViewer(QWidget):
    """
    alamat = 'file:///c:/users/usef/downloads/Semeru.pdf'
    print('buka', alamat)
    win.webView.load(QUrl(alamat))
    """
    def __init__(self, parent = None):
        super(PdfViewer,self).__init__(parent)
        self.setWindowTitle("PDF Viewer")
        # self.setGeometry(0, 28, 1000, 750)
        self.layout = QVBoxLayout(self)
        self.webView = QWebEngineView()
        self.webView.urlChanged.connect(self.url_changed)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)

        tool_layout = QHBoxLayout()
        self.layout.addLayout(tool_layout)
        
        addButton = QToolButton(autoRaise=True)
        addButton.setText('Open')
        addButton.clicked.connect(lambda: self.not_mousePressEvent(None))
        addButton.setStyleSheet('background-color: cyan;')
        # quitButton = QToolButton(autoRaise=True)
        # quitButton.setText('Quit')
        # quitButton.clicked.connect(lambda: qApp.quit())
        # quitButton.setStyleSheet('background-color: red;')
        tool_layout.addWidget(addButton)
        # tool_layout.addSpacing(10)
        # tool_layout.addWidget(quitButton)

        self.layout.addWidget(self.webView)
    
    def url_changed(self):
        self.setWindowTitle(self.webView.title())

    def go_back(self):
        self.webView.back()

    def not_mousePressEvent(self, event):
        filename, ok = QFileDialog.getOpenFileName(None, 'Open file:', '.', 'PDF files (*.pdf)')
        if ok:
            # self.webView.load(QUrl(filename))
            self.webView.load(QUrl.fromLocalFile(filename))
    
