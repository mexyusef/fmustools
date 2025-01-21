class MediumWebInternal(QWidget):

    url_signal = pyqtSignal(str)
    show_hide_state = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.bold_font = QFont("Roman times", 12, QFont.Bold)
        self.data = get_data_medium()
        self.initUI()

    def setContent(self):
        self.content.setRowCount(len(self.data))
        # https://stackoverflow.com/questions/38098763/pyside-pyqt-how-to-make-set-qtablewidget-column-width-as-proportion-of-the-a
        # set resizable utk kolom 0
        # self.content.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        # self.content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        for i, row in enumerate(self.data):
            # judul
            # column_labels = ['Title', 'Summary', 'Author/Date/Reading', 'URL']
            judul = f"{row['title']}"
            current_item = QTableWidgetItem(judul)
            current_item.setFont(self.bold_font)
            current_item.setToolTip(f"<b>{judul}</b>")
            self.content.setItem(i, 0, current_item)
            # info
            preview = row['summary']
            preview_item = QTableWidgetItem(preview)
            # preview_item.setFont(self.bold_font)
            preview_item.setToolTip(f"<i>{preview}</i>")
            self.content.setItem(i, 1, preview_item)
            # author
            # date
            # readingtime
            author = f"{row['postname']}, {row['postdate']}, {row['readingtime']}"
            author_item = QTableWidgetItem(author)
            # preview_item.setFont(self.bold_font)
            author_item.setToolTip(f"{author}")
            self.content.setItem(i, 2, author_item)
            # url
            # self.content.setItem(i, 0, QTableWidgetItem('palsu'))
            link_item = QTableWidgetItem(row['url'])
            link_item.setToolTip(f"""<a href="{row['url']}"><u>{row['url']}</u></a>""")
            self.content.setItem(i, 3, link_item)

            # commentlink_item = QTableWidgetItem(row['commenturl'])
            # commentlink_item.setToolTip(f"""<a href="{row['commenturl']}"><u>{row['commenturl']}</u></a>""")
            # self.content.setItem(i, 4, commentlink_item)

    def load_so(self):
        prefix = self.combo0.currentText()
        tag = self.edit_tag.text()
        page = self.page.value()
        print(f"""
        prefix      = {prefix}
        tag         = {tag}
        page        = {page}
        """)

        # self.data = get_data_medium(code=f'{tag} {page}')
        self.data = get_data_medium(code=f'{tag}')
        self.content.setRowCount(0)
        self.setContent()

    def setToolbar(self):
        self.tool_layout = QHBoxLayout()
        self.combo0 = QComboBox(self)
        self.combo0.addItems([
            'https://medium.com',
        ])
        self.combo0.currentTextChanged.connect(lambda value: print(value))
        self.combo0.currentIndexChanged.connect(lambda index: print(index))
        # combo0.textChanged.connect(lambda value: print(value))
        self.tool_layout.addWidget(self.combo0)
        lbl1 = QLabel("Tag")

        self.tool_layout.addWidget(lbl1)
        self.edit_tag = QLineEdit("python")
        self.edit_tag.returnPressed.connect(self.load_so)
        self.tool_layout.addWidget(self.edit_tag)

        lbl3 = QLabel("Page")
        self.tool_layout.addWidget(lbl3)

        self.page = QSpinBox()
        self.page.setRange(1,50)
        self.page.setValue(1)
        self.page.valueChanged.connect(lambda value: print('val:', value))
        # spin4.textChanged.connect(lambda value: print('text:', value))
        self.tool_layout.addWidget(self.page)
        self.tool_layout.addStretch(1)

        self.use_system_browser = QCheckBox("Use system browser")
        self.use_system_browser.stateChanged.connect(lambda state: print('use system browser' if state==Qt.Checked else 'use internal browser'))
        self.tool_layout.addWidget(self.use_system_browser)

        show_hide = QPushButton("Toggle")
        show_hide.setCheckable(True)
        show_hide.setChecked(True)
        show_hide.setStyleSheet("""
            QPushButton {background:rgb(66, 66, 66); color: white;} 
            QPushButton::checked {background:rgb(255, 255, 0); color: blue;}
        """)
        self.tool_layout.addWidget(show_hide)
        show_hide.toggled.connect(lambda state: self.show_hide_state.emit(state))

        load_button = QPushButton("load")
        load_button.clicked.connect(self.load_so)
        self.tool_layout.addWidget(load_button)
        self.logrocket_layout.addLayout(self.tool_layout)

    @pyqtSlot(QTableWidgetItem)
    def onClicked(self, it):
        print('url:', it.text(), 'row:', it.row(), 'col:', it.column())
        alamat = it.text()
        if alamat and it.column()in[3]: # url+comment url            
            if self.use_system_browser.isChecked():
                import webbrowser
                webbrowser.open_new(alamat)
            else:
                self.url_signal.emit(alamat)
        # state = not it.data(SelectedRole)
        # it.setData(SelectedRole, state)
        # it.setBackground(
        #     QColor(100, 100, 100) if state else QColor(0, 0, 0)
        # )

    def initUI(self):
        self.resize(1200, 800)
        self.logrocket_layout = QVBoxLayout()
        
        self.setToolbar()

        self.content = QTableWidget(self)
        column_labels = ['Title', 'Summary', 'Author/Date/Reading', 'URL']
        self.content.setColumnCount(len(column_labels))
        for i in range(1,len(column_labels)+1):
            item = QTableWidgetItem()
            self.content.setHorizontalHeaderItem(i, item)
        self.content.setHorizontalHeaderLabels(column_labels)
        self.logrocket_layout.addWidget(self.content)
        self.setContent()
        self.content.itemClicked.connect(self.onClicked)

        self.setLayout(self.logrocket_layout)
        self.setWindowTitle('__JUDUL__')


class MediumWeb(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.main_layout = QVBoxLayout()
        logrocket_splitter = QSplitter(Qt.Vertical)

        widgetbrowser = BrowserWindow()
        logrocket_splitter.addWidget(widgetbrowser)
        logrocket0 = MediumWebInternal()
        logrocket_splitter.addWidget(logrocket0)

        logrocket0.url_signal.connect(widgetbrowser.new_url)
        logrocket0.show_hide_state.connect(widgetbrowser.setHidden)

        logrocket_splitter.handle(1).setStyleSheet('background: 3px blue;')

        self.main_layout.addWidget(logrocket_splitter)
        self.setLayout(self.main_layout)

        # self.resize(800, 600)
        self.setWindowTitle('__JUDUL__')

