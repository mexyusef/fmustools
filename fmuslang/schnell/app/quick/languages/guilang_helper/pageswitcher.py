
class __PAGE_SWITCHER_NAME__(QWidget):

    def __init__(self, pages=1):
        super().__init__()
        self.pages = pages
        self.initUI()

    def initUI(self):
        self.resize(1200, 800)

        self.main_layout = QVBoxLayout(self)
        self.tool_layout = QHBoxLayout()

        self.stackedWidget = SlidingStackedWidget()

        self.prev = QPushButton(self)
        self.prev.setObjectName("pushButtonPrev")
        self.prev.setText('<<')
        
        self.first = QPushButton(self)
        self.first.setObjectName("pushButtonFirst")
        self.first.setText('|<')

        self.last = QPushButton(self)
        self.last.setObjectName("pushButtonLast")
        self.last.setText('>|')

        self.next = QPushButton(self)
        self.next.setObjectName("pushButtonNext")
        self.next.setText('>>')

        self.tool_layout.addWidget(self.prev)
        self.tool_layout.addWidget(self.first)
        for num in range(self.pages):
            btn = QPushButton(self)
            btn.setObjectName(f"page_{num}")
            btn.setText(f"{num}")
            self.tool_layout.addWidget(btn)
            btn.clicked.connect(partial(self.stackedWidget.slideInIdx, num))
        self.tool_layout.addWidget(self.last)
        self.tool_layout.addWidget(self.next)

        self.prev.clicked.connect(self.stackedWidget.slideInPrev)
        self.next.clicked.connect(self.stackedWidget.slideInNext)
        self.first.clicked.connect(self.stackedWidget.slideInFirst)
        self.last.clicked.connect(self.stackedWidget.slideInLast)

        # for num in range(10):
        #     self.stackedWidget.addWidget(QLabel(f"Page no {num}"))

__TEMPLATE_WIDGET_ITEMS__

        self.main_layout.addLayout(self.tool_layout)
        self.main_layout.addWidget(self.stackedWidget)

