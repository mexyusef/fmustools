# https://www.geeksforgeeks.org/pyqt5-create-a-user-form-to-get-information/

from PyQt5.QtWidgets import *
import github
import os, sys
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,    
    QHBoxLayout, 
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


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


def list_repo(account):
    """
    https://stackoverflow.com/questions/59861312/how-to-get-the-list-of-source-repositories-of-a-user-organisation-on-github
    """
    # global github
    token = config[account]
    g = github.Github(token)
    user = g.get_user()
    # non_forks = []
    gists = []
    for gist in user.get_gists():        
        # print('raw data:', gist.raw_data)
        filesmap = gist.raw_data['files']
        name = '-'.join([item for item in filesmap.keys()])
        # print('nama gist:', name)
        repo_list[name] = gist
        gists.append(name)
    return gists


class ListItemWidget(QWidget):

    itemDeleted = pyqtSignal(QListWidgetItem)

    def __init__(self, text, item, *args, **kwargs):
        super(ListItemWidget, self).__init__(*args, **kwargs)
        self._item = item
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.reponame = QTabWidget(self)        
        the_gist = repo_list[text]
        for k,v in the_gist.raw_data['files'].items():
            content = v['content'] # k = coba1, dst.
            textwidget = QPlainTextEdit(content, self.reponame)
            textwidget.setStyleSheet('background-color: #11ff22;')
            textwidget.setMinimumHeight(100)
            self.reponame.addTab(textwidget, k)
            # print('gist content:', content)
        layout.addWidget(self.reponame)
        self.button = QPushButton('x', self, clicked=self.doDeleteItem)

        # self.reponame.setMinimumHeight(100)
        # self.button.setMinimumHeight(100)
        # self.setMinimumHeight(100)

        layout.addWidget(self.button)

    def tulisan(self):
        return self.reponame.text()

    def doDeleteItem(self):
        self.itemDeleted.emit(self._item)

    def sizeHint(self):
        return QSize(200, 200)


class ListWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(ListWidget, self).__init__(*args, **kwargs)


        main_layout = QVBoxLayout(self)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.listWidget = QListWidget(self)
        self.scrollLayout.addWidget(self.listWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # main_layout.addWidget(self.listWidget)
        main_layout.addWidget(self.scrollArea)


    def doDeleteItem(self, item):
        # row = self.listWidget.indexFromItem(item).row()
        # item = self.listWidget.takeItem(row)
        # self.listWidget.removeItemWidget(item)
        # del item
        # https://stackoverflow.com/questions/52522218/getting-qtwidgets-from-my-custom-qlistwidgetitem
        # item = self.ui.listWidget.item(i)
        widget = self.listWidget.itemWidget(item)
        nama = widget.reponame.text()
        judul = f'Hapus "{nama}"?'
        isi = f'Yakin mau hapus "{nama}"'
        choose = QMessageBox.information(
            None,
            judul,
            isi,
            # buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.Yes,
        )
        if choose == QMessageBox.Yes:
            print(f'Deleting "{nama}"...(in theory)')
            # hapus dari github...
            the_gist = repo_list[nama]
            res = the_gist.delete()
            print(res)

    def doClearItem(self):
        # Clear all items
        for _ in range(self.listWidget.count()):
            # delete item
            # The reason it is always 0 is that it has been deleted from the first line,After deleting the first line, the second line becomes the first line
            # this and delete list [] The data is a truth
            item = self.listWidget.takeItem(0)
            # delete widget
            self.listWidget.removeItemWidget(item)
            del item

    # def testData(self):
    #     for i in range(10):
    #         item = QListWidgetItem(self.listWidget)
    #         widget = ListItemWidget('item: {}'.format(i), item, self.listWidget)
    #         widget.itemDeleted.connect(self.doDeleteItem)
    #         self.listWidget.setItemWidget(item, widget)

    def setData(self, repos):
        self.doClearItem()
        for repo in repos:
            item = QListWidgetItem(self.listWidget)
            widget = ListItemWidget(f"{repo}", item, self.listWidget)
            # w,h = self.sizeHint().width(), 200
            # widget.setSizeHint(QSize(w,h))
            widget.setMinimumHeight(100)
            widget.itemDeleted.connect(self.doDeleteItem)
            self.listWidget.setItemWidget(item, widget)


class GistListWindow(QDialog):

    def __init__(self, parent=None, will_close=True):
        super(GistListWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Gist")
        self.will_close = will_close

        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Get Gist")

        # layout = QFormLayout()
        # layout.addRow(QLabel("Repo name"), self.repo_name)
        layout = QVBoxLayout()
        self.repolist = ListWidget(self)
        self.fetch_repos = QPushButton('Fetch gist list')
        layout.addWidget(self.fetch_repos)
        layout.addWidget(self.repolist)
        self.repoBox.setLayout(layout)
        self.fetch_repos.clicked.connect(self.fetch_repositories)

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
        # print(f"Repo name {self.repo_name.text()}")
        if self.will_close:
            self.close()

    def fetch_repositories(self):
        account = self.account_combo.currentText()
        repos = list_repo(account)
        self.repolist.setData(repos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GistListWindow()
    window.show()
    sys.exit(app.exec())
