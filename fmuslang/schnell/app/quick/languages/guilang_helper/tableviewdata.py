
class TableViewData(QTableView):

    def __init__(self, parent=None):
        super(TableViewData, self).__init__(parent)
        self.resize(800, 600)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)  # right-click menu
        self.setEditTriggers(self.NoEditTriggers)  # Editing is prohibited
        self.doubleClicked.connect(self.onDoubleClick)
        self.addAction(QAction("copy", self, triggered=self.copyData))
        self.my_model = QStandardItemModel()  # model
        self.initHeader()  # Initialize the header
        self.setModel(self.my_model)
        self.initData()  # Initialize mock data

    def onDoubleClick(self, index):
        print(index.row(), index.column(), index.data())

    def keyPressEvent(self, event):
        super(TableViewData, self).keyPressEvent(event)
        # Ctrl + C
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.copyData()

    def copyData(self):
        count = len(self.selectedIndexes())
        if count == 0:
            return
        if count == 1:  # only copied one
            QApplication.clipboard().setText(self.selectedIndexes()[0].data())  # copy to clipboard
            QMessageBox.information(self, "hint", "A data has been copied")
            return
        rows = set()
        cols = set()
        for index in self.selectedIndexes():  # get all selected
            rows.add(index.row())
            cols.add(index.column())
            # print(index.row(),index.column(),index.data())
        if len(rows) == 1:  # One line
            QApplication.clipboard().setText("\t".join([index.data() for index in self.selectedIndexes()]))  # copy
            QMessageBox.information(self, "hint", "A row of data has been copied")
            return
        if len(cols) == 1:  # a row
            QApplication.clipboard().setText("\r\n".join([index.data() for index in self.selectedIndexes()]))  # copy
            QMessageBox.information(self, "hint", "A column of data has been copied")
            return
        mirow, marow = min(rows), max(rows)  # Most (less/more) rows
        micol, macol = min(cols), max(cols)  # Most (less/more) columns
        print(mirow, marow, micol, macol)
        arrays = [
            ["" for _ in range(macol - micol + 1)] for _ in range(marow - mirow + 1)
        ]  # Create a 2D array (and exclude preceding empty rows and columns)
        print(arrays)
        # Data input
        for index in self.selectedIndexes():  # iterate over all selected
            arrays[index.row() - mirow][index.column() - micol] = index.data()
        print(arrays)
        data = ""  # final result
        for row in arrays:
            data += "\t".join(row) + "\r\n"
        print(data)
        QApplication.clipboard().setText(data)  # copy to clipboard
        QMessageBox.information(self, "hint", "copied")

    def initHeader(self):
        for i in range(5):
            self.my_model.setHorizontalHeaderItem(i, QStandardItem("header" + str(i + 1)))

    def initData(self):
        for row in range(100):
            for col in range(5):
                self.my_model.setItem(row, col, QStandardItem("row: {row},col: {col}".format(row=row + 1, col=col + 1)))

