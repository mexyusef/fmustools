import os, sys
from functools import partial

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import (
    Qt, 
    pyqtProperty, 
    QEasingCurve, 
    QPoint, 
    QPropertyAnimation, 
    QParallelAnimationGroup, 
    QTimer,
)
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtWidgets import (
	QApplication,
	QCheckBox,
	QDesktopWidget,
	QDialog,
	QFormLayout,
    QGraphicsDropShadowEffect,
	QGridLayout,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QListWidget,
	QListWidgetItem,
	QMainWindow,
	QMessageBox,
	QMenu,
	QPushButton,
	QScrollArea,
	QShortcut,
    QStackedWidget,
	QTextEdit,
	QToolTip,
	QVBoxLayout,
	QWidget,
	qApp,
)


from gui.system.launcher.helper.gist import GistWindow
from gui.system.launcher.helper.repo import RepoWindow
from gui.system.launcher.helper.issue import IssueWindow
from gui.system.launcher.helper.issue import IssueAllWindow
from gui.system.launcher.helper.gistall import GistWindow as GistAllWindow
from gui.system.launcher.helper.repoall import RepoAllWindow
from gui.system.launcher.helper.pullrequest import PullRequestWindow
from gui.system.launcher.helper.repolist import RepoListWindow
from gui.system.launcher.helper.gistlist import GistListWindow
from app.utils import env_get


sidoarjo_folder = env_get('ULIBPY_ROOTDIR')


def handle_186_1(parent):
    QMessageBox.critical(
        None,
        "Critical",
        "Critical body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )


def handle_186_2(parent):
    QMessageBox.information(
        None,
        "Information",
        "Information body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )


def handle_186_3(parent):
    QMessageBox.warning(
        None,
        "Warning",
        "Warning body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )


def handle_186_4(parent):
    QMessageBox.question(
        None,
        "Question",
        "Question body",
        buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        defaultButton=QMessageBox.Discard,
    )



def handle_164_issueall(parent):
    w = IssueAllWindow(parent)
    w.show()

def handle_164_gistall(parent):
    w = GistAllWindow(parent)
    # print('GistAllWindow', w)
    w.show()
    # print('GistAllWindow stlh show')

def handle_164_repoall(parent):
    w = RepoAllWindow(parent)
    w.show()

def handle_164_pullrequest(parent):
    w = PullRequestWindow(parent)
    w.show()

def handle_164_gistlist(parent):
    w = GistListWindow(parent)
    w.show()
def handle_164_gist(parent):
    w = GistWindow(parent)
    w.show()

def handle_164_repolist(parent):
    w = RepoListWindow(parent)
    w.show()
def handle_164_repo(parent):
    w = RepoWindow(parent)
    w.show()


def handle_164_issue(parent):
    w = IssueWindow(parent)
    w.show()


def handle_164_edit_github_readme(parent):
    readme_path = os.path.normpath(os.path.join(os.path.normpath(sidoarjo_folder), 'data/github/README.md'))
    os.system(f"code {readme_path}")


def handle_164_edit_github_folder(parent):
    readme_path = os.path.normpath(os.path.join(os.path.normpath(sidoarjo_folder), 'data/github/'))
    os.system(f"code {readme_path}")


def handle_164_edit_github_cmd_folder(parent):
    github_folder = os.path.normpath(os.path.join(os.path.normpath(sidoarjo_folder), 'data/github/'))
    perintah = f"cmd.exe /c start /D {github_folder}"
    print(perintah)
    os.system(perintah)


def handle_172_edit_gui_readme(parent):
    readme_path = os.path.normpath(os.path.join(os.path.normpath(sidoarjo_folder), 'data/gui/README.md'))
    os.system(f"code {readme_path}")


button_groups_by_number = {
    '164': {
        'gist': handle_164_gist,
        'gist list': handle_164_gistlist,
        'repo': handle_164_repo,
        'repo list': handle_164_repolist,
        'gist all': handle_164_gistall,
        'repo all': handle_164_repoall,
        'issue all': handle_164_issueall,
        'issue': handle_164_issue,
        'pullrequest': handle_164_pullrequest,
        'github readme': handle_164_edit_github_readme,
        'github folder': handle_164_edit_github_folder,
        'github cmd folder': handle_164_edit_github_cmd_folder,
    },
    '172': {
        'gui readme': handle_172_edit_gui_readme,
    },
    '186': {
        'critical': handle_186_1,
        'information': handle_186_2,
        'warning': handle_186_3,
        'question': handle_186_4,
    },
    '187': {
        'kritis': handle_186_1,
        'info': handle_186_2,
        'tanya': handle_186_4,
    },
}
