# https://www.geeksforgeeks.org/pyqt5-create-a-user-form-to-get-information/

from PyQt5.QtWidgets import *
import github
import os, sys
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QListWidgetItem, QVBoxLayout, QListWidget, QApplication


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
    non_forks = []
    # repos = []
    for repo in user.get_repos():
        if repo.fork is False:
            non_forks.append(repo.name) # full_name
            repo_list[repo.name] = repo
    return non_forks


class ListItemWidget(QWidget):

    itemDeleted = pyqtSignal(QListWidgetItem)

    def __init__(self, text, item, *args, **kwargs):
        super(ListItemWidget, self).__init__(*args, **kwargs)
        self._item = item
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.reponame = QLineEdit(text, self)
        self.reponame.setReadOnly(True)
        layout.addWidget(self.reponame)
        layout.addWidget(QPushButton('x', self, clicked=self.doDeleteItem))

    def tulisan(self):
        return self.reponame.text()

    def doDeleteItem(self):
        self.itemDeleted.emit(self._item)

    def sizeHint(self):
        return QSize(200, 40)


class ListWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(ListWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # self.clearBtn = QPushButton('empty', self, clicked=self.doClearItem)
        # layout.addWidget(self.clearBtn)
        # self.testData()

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
            print(f'Deleting "{nama}"...')
            # hapus dari github...
            the_repo = repo_list[nama]
            res = the_repo.delete()
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

    def testData(self):
        for i in range(10):
            item = QListWidgetItem(self.listWidget)
            widget = ListItemWidget('item: {}'.format(i), item, self.listWidget)
            widget.itemDeleted.connect(self.doDeleteItem)
            self.listWidget.setItemWidget(item, widget)

    def setData(self, repos):
        self.doClearItem()
        for repo in repos:
            item = QListWidgetItem(self.listWidget)
            widget = ListItemWidget(f"{repo}", item, self.listWidget)
            widget.itemDeleted.connect(self.doDeleteItem)
            self.listWidget.setItemWidget(item, widget)


class RepoListWindow(QDialog):

    def __init__(self, parent=None, will_close=True):
        super(RepoListWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Repo list")
        self.will_close = will_close

        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Get own repositories")

        # layout = QFormLayout()
        # layout.addRow(QLabel("Repo name"), self.repo_name)
        layout = QVBoxLayout()
        self.repolist = ListWidget(self)
        self.fetch_repos = QPushButton('Fetch repo list')
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
        print(f"Repo name {self.repo_name.text()}")
        # print(f"File name {self.file_name.text()}")
        # print(f"Description {self.description.text()}")
        # print(f"""
        # self.private = {'Yes' if self.private.isChecked() else 'No'}
        # self.auto_init = {'Yes' if self.auto_init.isChecked() else 'No'}
        # self.delete_branch_on_merge = {'Yes' if self.delete_branch_on_merge.isChecked() else 'No'}
        # """)

        if self.will_close:
            self.close()

    def fetch_repositories(self):
        account = self.account_combo.currentText()
        repos = list_repo(account)
        self.repolist.setData(repos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RepoListWindow()
    window.show()
    sys.exit(app.exec())
