from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *



PORT = 50007



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

