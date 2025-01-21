# https://www.geeksforgeeks.org/pyqt5-create-a-user-form-to-get-information/

from cProfile import label
from PyQt5.QtWidgets import *
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import github

if __name__ == '__main__':
    from combomulti import CheckableComboBox
else:
    from gui.system.launcher.helper.combomulti import CheckableComboBox
"""
r = g.get_repo('vercel/next.js')
def get_issues(
    self,
    milestone=github.GithubObject.NotSet,
    state=github.GithubObject.NotSet,
    assignee=github.GithubObject.NotSet,
    mentioned=github.GithubObject.NotSet,
    labels=github.GithubObject.NotSet,
    sort=github.GithubObject.NotSet,
    direction=github.GithubObject.NotSet,
    since=github.GithubObject.NotSet,
    creator=github.GithubObject.NotSet,
):

https://github.com/vercel/next.js/labels/good%20first%20issue

r = g.get_repo('vercel/next.js')
issues = r.get_issues(state='open', sort='created', labels=['good first issue'])
issues = r.get_issues(sort='created', labels=['good first issue'])
daftar = [f'[{item.number}] {item.title}' for item in issues]
for d in daftar:
    print(d)

"""

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


def reset_repo_list():
    global repo_list
    repo_list = {}

def get_issues(account, repo_name, sort='updated', labels=['good first issue']):
    """
    https://stackoverflow.com/questions/59861312/how-to-get-the-list-of-source-repositories-of-a-user-organisation-on-github
    """
    reset_repo_list()
    token = config[account]
    g = github.Github(token)
    r = g.get_repo(repo_name)
    # non_forks = []
    issues = []
    for issue in r.get_issues(state='open', sort=sort, labels=labels, direction='desc'):
        # daftar = [f'[{item.number}] {item.title}' for item in issues]
        name = issue.title
        repo_list[name] = issue
        issues.append(name)

    return issues


def get_issue_labels(account, repo_name):
    labels = []
    token = config[account]
    g = github.Github(token)
    r = g.get_repo(repo_name)
    for lbl in r.get_labels():
        labels.append(lbl.name)
    return labels

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

    def __init__(self, main_window, *args, **kwargs):
        super(ListWidget, self).__init__(*args, **kwargs)

        self.main_window = main_window
        layout = QVBoxLayout(self)
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)

        self.main_window.issue_signal.connect(self.menerima_sinyal)

    def menerima_sinyal(self, text):
        print('ListWidget menerima:', text)
        self.setData()

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
        for _ in range(self.listWidget.count()):
            item = self.listWidget.takeItem(0)
            self.listWidget.removeItemWidget(item)
            del item

    def setData(self):
        self.doClearItem()
        for issue_name, issue in repo_list.items():
            item = QListWidgetItem(self.listWidget)
            widget = ListItemWidget(f"{issue_name}", item, self.listWidget)
            widget.setToolTip(issue.body)
            widget.setToolTipDuration(20000) # 20 detik
            widget.itemDeleted.connect(self.doDeleteItem)
            self.listWidget.setItemWidget(item, widget)


class IssueWindow(QDialog):

    issue_signal = pyqtSignal(str)

    def __init__(self, parent=None, will_close=True):
        super(IssueWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Gist")
        self.will_close = will_close

        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Get Repo Issues")

        self.repo_name = QLineEdit()
        initial_repo = 'vercel/next.js'
        self.repo_name.setText(initial_repo)

        self.state_box = QGroupBox("Issue state")
        self.check_open = QCheckBox()
        self.check_open.setChecked(True)
        state_layout = QFormLayout()
        state_layout.addRow(QLabel("Open"), self.check_open)
        self.state_box.setLayout(state_layout)

        self.sort_box = QGroupBox("Issue sort")
        # self.check_created = QCheckBox() # harusnya Radio shg bisa pilih: created, updated...
        # self.check_created.setChecked(True)
        self.check_created = QComboBox()
        self.check_created.addItems(['updated', 'created'])
        self.check_created.setCurrentIndex(0)
        sort_layout = QFormLayout()
        sort_layout.addRow(QLabel("Created"), self.check_created)
        self.sort_box.setLayout(sort_layout)

        self.labels_box = QGroupBox("Issue labels")
        # gunakan ipynb utk get labels utk issue...
        self.check_good_first_issue = QCheckBox()
        self.check_good_first_issue.setChecked(True)

        # CheckableComboBox
        self.selected_labels = CheckableComboBox()
        self.selected_labels.addItems(['good first issue', 'template: bug'])
        self.selected_labels.setCurrentIndex(0)

        labels_layout = QFormLayout()
        self.fetch_labels = QPushButton('Fetch')
        self.fetch_labels.clicked.connect(self.do_fetch_labels)
        labels_layout.addRow(self.fetch_labels)
        # labels_layout.addRow(QLabel("Good First Issue"), self.check_good_first_issue)
        labels_layout.addRow(QLabel("Issue labels"), self.selected_labels)
        self.labels_box.setLayout(labels_layout)

        self.createForm()

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

        # second_splitter = QSplitter(self)
        # second_splitter.setHandleWidth(8)
        # second_splitter.setOrientation(Qt.Horizontal)
        # self.left = RepoWindow(will_close=False)
        # self.right = RepoListWindow(will_close=False)
        # second_splitter.addWidget(self.left)
        # second_splitter.addWidget(self.right)
        # layout.addWidget(second_splitter)

        self.setLayout(mainLayout)

    def do_fetch_labels(self):
        reponame = self.repo_name.text().strip()
        if reponame:
            account = self.account_combo.currentText()
            labels = get_issue_labels(account, reponame)
            if labels:
                self.selected_labels.replaceItems(labels)

    def getInfo(self):
        reponame = self.repo_name.text().strip()
        if reponame:
            account = self.account_combo.currentText()
            # get_issues akan populate repo_list dg repo_list[issuetitle] = issueobj
            sort_arg = self.check_created.currentText()
            labels_arg = self.selected_labels.currentData()
            print(f"""
            Repo name: {reponame}
            sort by = {sort_arg}
            labels = {', '.join(labels_arg)}
            state open = {'Yes' if self.check_open.isChecked() else 'No'}
            """)
            get_issues(account, reponame, sort_arg, labels_arg)
            self.issue_signal.emit(reponame)

        if self.will_close:
            self.close()

    def createForm(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Repo name"), self.repo_name)
        layout.addRow(QLabel("Sort created"), self.sort_box)
        layout.addRow(QLabel("State"), self.state_box)
        layout.addRow(QLabel("Labels"), self.labels_box)
        self.repoBox.setLayout(layout)


# class IssueAllWindow(QWidget):
class IssueAllWindow(QDialog):
    def __init__(self, parent=None):
        super(IssueAllWindow, self).__init__(parent=parent)
        layout = QVBoxLayout()

        second_splitter = QSplitter(self)
        second_splitter.setHandleWidth(8)
        second_splitter.setOrientation(Qt.Horizontal)
        self.left = IssueWindow(will_close=False)
        self.right = ListWidget(self.left)
        second_splitter.addWidget(self.left)
        second_splitter.addWidget(self.right)
        layout.addWidget(second_splitter)

        self.setLayout(layout)


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
    window = IssueAllWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
