import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget
from PyQt5.Qt import QTableWidgetItem, QAbstractItemView
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createTable()
        lstSelection = [0, 3, 4]
        self.selectRows(lstSelection)
    def initUI(self):
        self.resize(600, 600)
        self.rows = [['a1', 'b1', 'c1'], 
                     ['a2', 'b2', 'c2'], 
                     ['a3', 'b3', 'c3'], 
                     ['a4', 'b4', 'c4'], 
                     ['a5', 'b5', 'c5']]                     
    def createTable(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(self.width(), self.height())
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(len(self.rows[0]))
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        for row in enumerate(self.rows):
            for col in enumerate(row[1]):
                item = QTableWidgetItem()
                item.setText(col[1])
                self.tableWidget.setItem(row[0], col[0], item)
    def selectRows(self, selection: list):
        for i in selection:
            self.tableWidget.selectRow(i)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())
# https://gist.github.com/DataSolveProblems/b0ea227c54debb09156af872b3b72b73
