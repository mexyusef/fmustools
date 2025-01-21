# https://www.geeksforgeeks.org/pyqt5-create-a-user-form-to-get-information/

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import github
import os, sys, timeago, datetime
from PyQt5.QtCore import (
    pyqtSignal,
    Qt,
    QObject,
    QSize,
    QThread,
    QDateTime,
)
import csv


config = {}
configfilename = '.env'
curdir = os.path.dirname(os.path.abspath(__file__))
configfilepath = os.path.join(curdir, '.env')
with open(configfilepath) as fd:
    content = fd.readlines()
    for line in content:
        k,v = [item.strip() for item in line.split('=')]
        config[k] = v


repo_list = {}


def list_repo(account, username, page=1, per_page=100):
    """
    https://stackoverflow.com/questions/59861312/how-to-get-the-list-of-source-repositories-of-a-user-organisation-on-github
    """
    # global github
    token = config[account]
    g = github.Github(token)
    user = g.get_user(username)
    non_forks = []
    # for repo in user.get_repos(sort='updated', direction='desc', per_page=per_page, page=page):
    for repo in user.get_repos(sort='updated', direction='desc'):
        if repo.fork is False:
            non_forks.append(repo.name) # full_name
            repo_list[repo.name] = repo
    return non_forks

class WorkerThread(QThread):
    
    # https://stackoverflow.com/questions/43964766/pyqt-emit-signal-with-dict
    valueChange = pyqtSignal(object)

    def __init__(self, account, username, parent=None, *args, **kwargs):
        super(WorkerThread, self).__init__(parent=parent, *args, **kwargs)
        # self.account = account
        # self.username = username
        token = config[account]
        g = github.Github(token)
        self.user = g.get_user(username)

    def run(self):
        for repo in self.user.get_repos(sort='updated', direction='desc'):
            if repo.fork is False:
                data = {
                    'name': repo.name,
                    'full_name': repo.full_name,
                    'url': repo.clone_url,
                    'updated_at': repo.updated_at,
                    'description': repo.description,
                }
                # print('thread mengirim data:', data)
                self.valueChange.emit(data)
                # self.msleep(100)

class RepoEntry(QTableWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(RepoEntry, self).__init__(parent=parent, *args, **kwargs)

        # https://stackoverflow.com/questions/7727863/how-to-make-a-cell-in-a-qtablewidget-read-only
        self.setEditTriggers(QTableWidget.NoEditTriggers)

        self.setVerticalHeaderLabels(list(range(1,len(repo_list)+1)))
        self.setColumnCount(4)
        # self.setColumnWidth(0, 200)
        # self.setColumnWidth(4, 200)
        # self.setRowHeight(0, 100)
        self.setHorizontalHeaderLabels(["repo", "url", "updated_at", "description"])

    def doClearItem(self):
        """
        [slot] void QTableWidget::clear()
        Removes all items in the view. This will also remove all selections and headers.
        If you don't want to remove the headers, use QTableWidget::clearContents(). The table dimensions stay the same.
        """
        self.clearContents()

    def addRecord(self, repo):
        index = self.rowCount()
        self.setRowCount(index+1)

        reponame = repo['name']
        repourl = repo['url']
        repotime = repo['updated_at']
        repofname = repo['full_name']
        repodesc = repo['description']

        # print(f"""table signal receive
        # table index = {index}, row count = {self.rowCount()}
        # data = {reponame}
        # """)

        sekarang = datetime.datetime.now()
        lwi0 = QTableWidgetItem(reponame)
        lwi0.setToolTip(repofname)

        lwi1 = QTableWidgetItem(repourl)
        lwi1.setToolTip(repourl)

        dte = QDateTimeEdit()
        dte.setDateTime(repotime)
        dte.setDisplayFormat("yyyy/MM/dd hh:mm:ss")
        dte.setCalendarPopup(True)
        dte.setToolTip(timeago.format(repotime, sekarang))

        lwi3 = QTableWidgetItem(repodesc)
        if repodesc and repodesc.strip():
            lwi3.setToolTip(repodesc)
        else:
            lwi3.setToolTip(repofname)

        self.setItem(index, 0, lwi0)
        self.setItem(index, 1, lwi1)
        # self.setItem(i, 2, lwi2)
        self.setCellWidget(index, 2, dte)
        self.setItem(index, 3, lwi3)

    def setData(self, repos):
        self.doClearItem()
        jumlah = len(repos)
        self.setRowCount(jumlah)
        sekarang = datetime.datetime.now()

        for i,repo_name in enumerate(repos):
            repo = repo_list[repo_name]
            lwi0 = QTableWidgetItem(repo.name)            
            lwi0.setToolTip(repo.full_name)

            lwi1 = QTableWidgetItem(repo.clone_url)

            # lwi2 = QTableWidgetItem(repo.updated_at.isoformat())
            # lwi2.setToolTip(timeago.format(repo.updated_at, sekarang))
            dte = QDateTimeEdit()
            dte.setDateTime(repo.updated_at)
            dte.setDisplayFormat("yyyy/MM/dd hh:mm:ss")
            dte.setCalendarPopup(True)
            dte.setToolTip(timeago.format(repo.updated_at, sekarang))
            # https://stackoverflow.com/questions/47405395/python-how-to-pull-string-out-of-qdatetimeedit
            # dte.dateTime().toString(dte.displayFormat())
            dte.setReadOnly(True)

            lwi3 = QTableWidgetItem(repo.description)
            self.setItem(i, 0, lwi0)
            self.setItem(i, 1, lwi1)
            # self.setItem(i, 2, lwi2)
            self.setCellWidget(i, 2, dte)
            self.setItem(i, 3, lwi3)


class RepoUserWindow(QDialog):

    def __init__(self, parent=None, will_close=True):
        super(RepoUserWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Repo list")
        self.will_close = will_close

        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Get user repositories")

        layout = QVBoxLayout()
        
        self.user_name = QLineEdit()
        initial_repo = 'commitdev'
        self.user_name.setText(initial_repo)
        self.fetch_repos = QPushButton('Fetch repo list')
        self.export_csv = QPushButton('CSV')
        # self.export_csv.hide()
        self.repolist = RepoEntry(self)
        
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.user_name)
        btnLayout.addWidget(self.fetch_repos)
        btnLayout.addWidget(self.export_csv)
        # layout.addWidget(self.user_name)
        # layout.addWidget(self.fetch_repos)
        layout.addLayout(btnLayout)

        layout.addWidget(self.repolist)
        self.repoBox.setLayout(layout)
        self.fetch_repos.clicked.connect(self.fetch_repositories)
        self.export_csv.clicked.connect(self.handleSave)

        self.dialogButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialogButtonBox.accepted.connect(self.getInfo)
        self.dialogButtonBox.rejected.connect(self.reject)

        self.account_combo = QComboBox()
        self.account_combo.addItems(list(config.keys()))

        # self.account_combo.setCurrentIndex(2)
        self.account_combo.setCurrentText('uulum')

        account_layout = QFormLayout()
        account_layout.addRow(QLabel("Account"), self.account_combo)
        self.accountBox.setLayout(account_layout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.accountBox)
        mainLayout.addWidget(self.repoBox)
        mainLayout.addWidget(self.dialogButtonBox)
        self.setLayout(mainLayout)

    def getInfo(self):
        print(f"Repo name {self.user_name.text()}")
        if self.will_close:
            self.close()

    def fetch_repositories(self):
        account = self.account_combo.currentText()
        username = self.user_name.text()

        self.repolist.doClearItem()
        # repos = list_repo(account, username)
        # self.repolist.setData(repos)
        self.t = WorkerThread(account, username, parent=self)
        self.t.valueChange.connect(self.repolist.addRecord)
        self.t.start()

    # https://stackoverflow.com/questions/71140850/export-qtablewidget-to-csv-including-headers
    def handleSave(self):
        path, ok = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')

        # def rowdata(r, c):
        #     item = self.repolist.item(r, c)
        #     if item:
        #         return item.text()
        #     return 
        if ok:
            columns = range(self.repolist.columnCount())
            header = [self.repolist.horizontalHeaderItem(column).text() for column in columns]
            with open(path, 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel', lineterminator='\n')
                writer.writerow(header)
                for row in range(self.repolist.rowCount()):
                    # item = self.repolist.item(row, column)
                    # dte.dateTime().toString(dte.displayFormat())
                    # 0 = name, 1 = url, 2 = time, 3 = desc
                    # self.repolist.cellWidget(row, col)
                    writer.writerow(self.repolist.item(row, column).text() if column!=2 
                        else self.repolist.cellWidget(row, column).dateTime().toString(self.repolist.cellWidget(row, column).displayFormat())
                        for column in columns)


def set_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)


if __name__ == '__main__':
    app = QApplication([])
    set_theme(app)
    window = RepoUserWindow()
    window.show()
    sys.exit(app.exec())
