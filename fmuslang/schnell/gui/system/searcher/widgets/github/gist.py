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


# fcontent = github.InputFileContent(content=content, new_name='coba1')
# da_gist = user.create_gist(public=False, files={'coba1.txt':fcontent}, description='first gist')
# g = create_gist(gistname, gistcontent, gistdesc, gistfile, isprivate)
def create_gist(account, gistname, gistcontent, gistdesc, gistfile, isprivate):
    token = config[account]
    g = github.Github(token)
    user = g.get_user()
    if not gistfile:
        gistfile = gistname + '.txt'
    fcontent = github.InputFileContent(content=gistcontent, new_name=gistname)
    da_gist = user.create_gist(public=not isprivate, files={gistfile: fcontent}, description=gistdesc)
    return da_gist


class GistWindow(QDialog):

    def __init__(self, parent=None, will_close=True):
        super(GistWindow, self).__init__(parent=parent)

        self.setWindowTitle("Github Gist")
        self.will_close = will_close

        self.accountBox = QGroupBox("Github Account")
        self.repoBox = QGroupBox("Create Github Gist")
        # self.ageSpinBar = QSpinBox()
        # self.license_list = [
        #     'mit',
        #     'apache-2.0',
        #     'cc', 'isc',
        #     'gpl', 'gpl-2.0', 'gpl-3.0',
        #     'lgpl', 'lgpl-2.1', 'lgpl-3.0',
        #     'ms-pl', 'mpl-2.0',
        # ]
        # self.gitignore_list = ['Python', 'C++', 'Go', 'Java', 'Node', 'Rust']

        self.description = QLineEdit()
        self.gist_name = QLineEdit()
        self.file_name = QLineEdit() # jk kosong, samakan dg gist_name + .txt

        # self.license_template = QComboBox()
        # self.license_template.addItems(self.license_list)
        # self.gitignore_template = QComboBox()
        # self.gitignore_template.addItems(self.gitignore_list)

        self.private = QCheckBox()
        self.private.setCheckState(Qt.Checked)

        self.gist_content = QPlainTextEdit()

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
        """
        create_gist(public, files, description=NotSet) Calls:

        POST /gists
        Parameters:    

            public – bool
            files – dict of string to github.InputFileContent.InputFileContent
            description – string

        Return type:
        github.Gist.Gist

        fcontent = github.InputFileContent(content=content, new_name='coba1')
        da_gist = u.create_gist(public=False, files={'coba1.txt':fcontent}, description='first gist')
        """
        gistname = self.gist_name.text()
        gistcontent = self.gist_content.toPlainText()
        gistfile = self.file_name.text().strip()
        gistdesc = self.description.text()
        isprivate = True if self.private.isChecked() else False
        print(f"Gist name {gistname}")
        print(f"File name {gistfile}")
        print(f"Description {gistdesc}")
        print(f"Content {gistcontent}")
        print(f"""self.private = {'Yes' if self.private.isChecked() else 'No'}""")

        if gistname.strip() and gistcontent.strip():
            account = self.account_combo.currentText()
            # fcontent = github.InputFileContent(content=content, new_name='coba1')
            # da_gist = user.create_gist(public=False, files={'coba1.txt':fcontent}, description='first gist')
            g = create_gist(account, gistname, gistcontent, gistdesc, gistfile, isprivate)
            print(g)

        if self.will_close:
            self.close()

    def createForm(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Gist name"), self.gist_name)
        layout.addRow(QLabel("Private"), self.private)
        layout.addRow(QLabel("Description"), self.description)
        layout.addRow(QLabel("File name (def = gist+.txt)"), self.file_name)
        layout.addRow(QLabel("Content"), self.gist_content)
        
        self.repoBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GistWindow()
    window.show()
    sys.exit(app.exec())


"""
stlh berhasil create gist, hrs ada notifikasi
"""
