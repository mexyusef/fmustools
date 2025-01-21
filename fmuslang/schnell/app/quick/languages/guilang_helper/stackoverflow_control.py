
class StackOverflowInternal(QWidget):

    url_signal = pyqtSignal(str)
    show_hide_state = pyqtSignal(bool)
    toggle_table_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.bold_font = QFont("Roman times", 12, QFont.Bold)
        self.data = get_data_stackoverflow()
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
        self.setWindowTitle('__JUDUL__')

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

        self.main_layout = QVBoxLayout()
        stackoverflow_splitter = QSplitter(Qt.Vertical)

        widgetbrowser = BrowserWindow()
        stackoverflow_splitter.addWidget(widgetbrowser)
        stackoverflow_widget = StackOverflowInternal()
        stackoverflow_splitter.addWidget(stackoverflow_widget)

        stackoverflow_widget.url_signal.connect(widgetbrowser.new_url)
        stackoverflow_widget.show_hide_state.connect(widgetbrowser.setHidden)
        # https://stackoverflow.com/questions/29537762/pyqt-qsplitter-setsizes-usage
        # stackoverflow_widget.toggle_table_signal.connect(lambda state: stackoverflow_splitter.setStretchFactor(10,1) if state else stackoverflow_splitter.setStretchFactor(5,5))
        stackoverflow_widget.toggle_table_signal.connect(lambda state: stackoverflow_splitter.setSizes([500,100]) if state else stackoverflow_splitter.setSizes([400,400]))

        stackoverflow_splitter.handle(1).setStyleSheet('background: 3px blue;')

        self.main_layout.addWidget(stackoverflow_splitter)
        self.setLayout(self.main_layout)

        # self.resize(800, 600)
        self.setWindowTitle('__JUDUL__')

"""
TODO:
setiap ganti combobox maka tag dikosongkan
krn gak make sense ada tag "python" utk writing stackexchange misalnya.
"""