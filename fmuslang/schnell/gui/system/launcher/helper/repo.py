# https://www.geeksforgeeks.org/pyqt5-create-a-user-form-to-get-information/

from PyQt5.QtWidgets import *
import os, sys
from PyQt5.QtCore import Qt
import github


config = {}
configfilename = '.env'
curdir = os.path.dirname(os.path.abspath(__file__))
configfilepath = os.path.join(curdir, '.env')
with open(configfilepath) as fd:
    content = fd.readlines()
    for line in content:
        k,v = [item.strip() for item in line.split('=')]
        config[k] = v



"""
create_repo(
    name – string
    description – string
    homepage – string
    license_template – string
    gitignore_template – string

default true
    has_issues – bool
    has_wiki – bool
    has_downloads – bool
    has_projects – bool
    auto_init – bool
    allow_squash_merge – bool
    allow_merge_commit – bool
    allow_rebase_merge – bool
default false
    private – bool
    delete_branch_on_merge – bool
)
hapus1_repo = u.create_repo(name='hapus2', description='ini contoh utk dihapus yg kedua', private=True, license_template='mit', gitignore_template='Python')
"""
def create_repo(account,
    name, description,
    license_template='',
    gitignore_template='',
    homepage = '',
    private=True,
    auto_init=True,
    has_issues=True,
    has_wiki=True,
    has_downloads=True,
    has_projects=True,
    allow_squash_merge=True,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    delete_branch_on_merge=False,
    ):
    token = config[account]
    g = github.Github(token)
    user = g.get_user()
    kwargs = {
        'name':name,
        'description':description,        
        'homepage':homepage,
        'private':private,
        'auto_init':auto_init,
        'has_issues':has_issues,
        'has_wiki':has_wiki,
        'has_downloads':has_downloads,
        'has_projects':has_projects,
        'allow_squash_merge':allow_squash_merge,
        'allow_merge_commit':allow_merge_commit,
        'allow_rebase_merge':allow_rebase_merge,
        'delete_branch_on_merge':delete_branch_on_merge,
    }
    if license_template:
        kwargs.update({'license_template':license_template,})
    if gitignore_template:
        kwargs.update({'gitignore_template':gitignore_template,})        
    da_repo = user.create_repo(**kwargs)
    return da_repo


class RepoWindow(QDialog):

    def __init__(self, parent=None, will_close=True):
        super(RepoWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Repo")
        self.will_close = will_close
        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Create Github Repo")

        # self.ageSpinBar = QSpinBox()

        self.license_list = [
            '',
            'mit',
            'apache-2.0',
            'cc', 'isc',
            'gpl', 'gpl-2.0', 'gpl-3.0',
            'lgpl', 'lgpl-2.1', 'lgpl-3.0',
            'ms-pl', 'mpl-2.0',
        ]
        self.gitignore_list = ['', 'Python', 'C++', 'Go', 'Java', 'Node', 'Rust']

        self.name = QLineEdit()
        self.description = QLineEdit()
        self.homepage = QLineEdit()

        self.license_template = QComboBox()
        self.license_template.addItems(self.license_list)
        self.gitignore_template = QComboBox()
        self.gitignore_template.addItems(self.gitignore_list)

        self.private = QCheckBox()
        self.private.setCheckState(Qt.Checked)
        self.has_issues = QCheckBox()
        self.has_issues.setCheckState(Qt.Checked)
        self.has_wiki = QCheckBox()
        self.has_wiki.setCheckState(Qt.Checked)
        self.has_downloads = QCheckBox()
        self.has_downloads.setCheckState(Qt.Checked)
        self.has_projects = QCheckBox()
        self.has_projects.setCheckState(Qt.Checked)
        self.auto_init = QCheckBox() # utk empty readme
        self.auto_init.setCheckState(Qt.Checked)
        self.allow_squash_merge = QCheckBox()
        self.allow_squash_merge.setCheckState(Qt.Checked)
        self.allow_merge_commit = QCheckBox()
        self.allow_merge_commit.setCheckState(Qt.Checked)
        self.allow_rebase_merge = QCheckBox()
        self.allow_rebase_merge.setCheckState(Qt.Checked)
        self.delete_branch_on_merge = QCheckBox()
        # self.delete_branch_on_merge.setCheckState(Qt.Checked)

        self.readme = QPlainTextEdit()

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
        self.setLayout(mainLayout)

    def getInfo(self):
        reponame = self.name.text().strip()
        print(f"Name {reponame}")
        print(f"Description {self.description.text()}")
        print(f"Homepage {self.homepage.text()}")
        print(f"License {self.license_template.currentText()}")
        print(f"Gitignore {self.gitignore_template.currentText()}")

        print(f"""
        self.private = {'Yes' if self.private.isChecked() else 'No'}
        self.auto_init = {'Yes' if self.auto_init.isChecked() else 'No'}
        self.delete_branch_on_merge = {'Yes' if self.delete_branch_on_merge.isChecked() else 'No'}
        """)

        if reponame:
            account = self.account_combo.currentText()
            # homepage = self.homepage.text().strip()
            kwargs = {
                'account': account,
                'name': reponame,
                'description': self.description.text(),
                'private': True if self.private.isChecked() else False,
                'auto_init': True if self.auto_init.isChecked() else False,
                'private': True if self.private.isChecked() else False,

                'license_template': self.license_template.currentText(),
                'gitignore_template': self.gitignore_template.currentText(),

                'homepage': self.homepage.text().strip(),

                'has_issues': True if self.has_issues.isChecked() else False,
                'has_wiki': True if self.has_wiki.isChecked() else False,
                'has_downloads': True if self.has_downloads.isChecked() else False,
                'has_projects': True if self.has_projects.isChecked() else False,
                'allow_squash_merge': True if self.allow_squash_merge.isChecked() else False,
                'allow_merge_commit': True if self.allow_merge_commit.isChecked() else False,
                'allow_rebase_merge': True if self.allow_rebase_merge.isChecked() else False,

                'delete_branch_on_merge': True if self.delete_branch_on_merge.isChecked() else False,
            }
            # if self.license_template.currentText():
            #     kwargs.update({'license_template': self.license_template.currentText()})
            # if self.gitignore_template.currentText():
            #     kwargs.update({'gitignore_template': self.gitignore_template.currentText()})
            # if self.homepage.text().strip():
            #     kwargs.update({'homepage': self.homepage.text().strip()})
            
            r = create_repo(**kwargs)
            print(r)

        if self.will_close:
            self.close()

    def createForm(self):

        layout = QFormLayout()

        layout.addRow(QLabel("Name"), self.name)
        layout.addRow(QLabel("Private"), self.private)
        layout.addRow(QLabel("Auto init"), self.auto_init) # empty readme

        layout.addRow(QLabel("Description"), self.description)
        layout.addRow(QLabel("Homepage"), self.homepage)
        layout.addRow(QLabel("License"), self.license_template)
        layout.addRow(QLabel("Gitignore"), self.gitignore_template)
        
        layout.addRow(QLabel("Has issues"), self.has_issues)
        layout.addRow(QLabel("Has wiki"), self.has_wiki)
        layout.addRow(QLabel("Has downloads"), self.has_downloads)
        layout.addRow(QLabel("Has projects"), self.has_projects)        
        layout.addRow(QLabel("Allow squash merge"), self.allow_squash_merge)
        layout.addRow(QLabel("Allow merge commit"), self.allow_merge_commit)
        layout.addRow(QLabel("Allow rebase merge"), self.allow_rebase_merge)
        layout.addRow(QLabel("Delete branch on merge"), self.delete_branch_on_merge)
        layout.addRow(QLabel("README.md"), self.readme)

        self.repoBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RepoWindow()
    window.show()
    sys.exit(app.exec())

"""
TODO:
handle jk masukkan README.md
jadi hrs bisa create repo yg berisi file...
"""
