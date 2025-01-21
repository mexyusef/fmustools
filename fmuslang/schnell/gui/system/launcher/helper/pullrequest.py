

# https://stackoverflow.com/questions/17423598/how-can-i-get-a-list-of-all-pull-requests-for-a-repo-through-the-github-api
# g = Github(login_or_token=$YOUR_TOKEN, per_page=100)
# r = g.get_repo($REPO_NUMBER)
# for pull in r.get_pulls('all'):
#     # You can access pulls

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import github
import os, sys
from PyQt5.QtCore import Qt, QSize, pyqtSignal
# from PyQt5.QtWidgets import (
#     QApplication,    
#     QHBoxLayout, 
#     QLineEdit,
#     QListWidget,
#     QListWidgetItem,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )


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


def list_pull_request(account, repo_name):
    """
    https://stackoverflow.com/questions/59861312/how-to-get-the-list-of-source-repositories-of-a-user-organisation-on-github
    """
    # global github
    token = config[account]
    g = github.Github(token)
    r = g.get_repo(repo_name)
    # user = g.get_user()
    # non_forks = []
    pulls = []
    for pull in r.get_pulls(state='open', sort='created', base='main', direction='desc'):
        # print('pull', pull)
        name = pull.title
        repo_list[name] = pull
        pulls.append(name)

    return pulls


class ListItemWidget(QWidget):

    itemDeleted = pyqtSignal(QListWidgetItem)

    def __init__(self, text, item, *args, **kwargs):
        super(ListItemWidget, self).__init__(*args, **kwargs)
        self._item = item
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # self.reponame = QTabWidget(self)
        # the_gist = repo_list[text]
        # for k,v in the_gist.raw_data['files'].items():
        #     content = v['content'] # k = coba1, dst.
        #     textwidget = QPlainTextEdit(content, self.reponame)
        #     textwidget.setStyleSheet('background-color: #11ff22;')
        #     self.reponame.addTab(textwidget, k)
        #     # print('gist content:', content)
        self.reponame = QLineEdit(text, self)
        self.reponame.setReadOnly(True)

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
            print(f'Deleting "{nama}"...(in theory)')
            # hapus dari github...
            # the_gist = repo_list[nama]
            # res = the_gist.delete()
            # print(res)

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
            widget.setToolTip(repo_list[repo].body)
            widget.setToolTipDuration(20000) # 20 detik
            widget.itemDeleted.connect(self.doDeleteItem)
            self.listWidget.setItemWidget(item, widget)


class PullRequestWindow(QDialog):

    def __init__(self, parent=None):
        super(PullRequestWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Pull Requests")
        # self.setGeometry(100, 100, 300, 400)

        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Get Pull Requests")

        self.repo_name = QLineEdit()
        initial_repo = 'iterative/dvc' # vercel/next.js
        self.repo_name.setText(initial_repo)

        layout = QVBoxLayout()
        self.repolist = ListWidget(self)
        self.fetch_repos = QPushButton('Fetch pull requests')
        layout.addWidget(self.repo_name)
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
        self.close()

    def fetch_repositories(self):
        repo_name = self.repo_name.text()
        if '/' in repo_name: # iterative/dvc
            account = self.account_combo.currentText()
            repos = list_pull_request(account, repo_name)
            self.repolist.setData(repos)


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

def main():
    app = QApplication([])
    set_theme(app)
    window = PullRequestWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
