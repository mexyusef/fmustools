import random, string
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *


ULIBPY_BASEDIR = r'c:\users\usef\work\sidoarjo\schnell'
SIDOARJODIR = r'c:\Users\usef\work\sidoarjo'
PORT = 50007


def get_icon():
  # test mock icon
  pixmap = QPixmap(16, 16)
  pixmap.fill(Qt.transparent)
  painter = QPainter()
  painter.begin(pixmap)
  painter.setFont(QFont('Webdings', 11))
  painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
  painter.drawText(0, 0, 16, 16, Qt.AlignCenter,
                   random.choice(string.ascii_letters))
  painter.end()
  return QIcon(pixmap)


def about_qt():
  QApplication.instance().aboutQt()


icon_provider = QFileIconProvider()
def _file_icon(path):
  return icon_provider.icon(QFileInfo(path))


def set_app_info(app, name):
    app.setOrganizationName('helanic')
    app.setOrganizationDomain('answeror.com')

def set_version(s):
    s.setVersion(QDataStream.Qt_4_0)


def write(con, callback):
    block = QByteArray()
    out = QDataStream(block, QIODevice.WriteOnly)
    set_version(out)
    callback(out)
    con.write(block)


def lcs(x, y):
    n = len(x)
    m = len(y)
    table = dict()  # a hashtable, but we'll use it as a 2D array here

    for i in range(n+1):     # i=0,1,...,n
        for j in range(m+1):  # j=0,1,...,m
            if i == 0 or j == 0:
                table[i, j] = 0
            elif x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i-1, j], table[i, j-1])

    # Now, table[n, m] is the length of LCS of x and y.

    # Let's go one step further and reconstruct
    # the actual sequence from DP table:

    def recon(i, j):
        if i == 0 or j == 0:
            return []
        elif x[i-1] == y[j-1]:
            return recon(i-1, j-1) + [x[i-1]]
        elif table[i-1, j] > table[i, j-1]:
            return recon(i-1, j)
        else:
            return recon(i, j-1)

    return recon(n, m)
