# https://stackoverflow.com/questions/54734244/create-a-full-screen-button-in-pyqt5
import sys
import pandas as pd
import matplotlib.pyplot  as plt
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class mainApplication(QWidget):

    def __init__(self, parent=None):
        super(mainApplication, self).__init__(parent)

        self.layoutMap = {}
        self.buttonMap = {}

        # Figure Bottom Right
        self.figure = plt.figure(figsize=(15,5))
        self.figure.set_facecolor('0.915')
        self.canvas = FigureCanvas(self.figure) 

        # Main Figure
#        self.setGeometry(600, 300, 1000, 600)

        self.topLeftBox    = self.topLeft()
        self.topRightBox   = self.topRight()
        self.bottomLeftBox = self.bottomLeft()
        self.bottomRight()

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.topLeftBox, 1, 0)
        self.mainLayout.addWidget(self.topRightBox, 1, 1)
        self.mainLayout.addWidget(self.bottomLeftBox, 2, 0)
        self.mainLayout.addWidget(self.bottomRightBox, 2, 1)
        self.mainLayout.setRowStretch(1, 1)
        self.mainLayout.setRowStretch(2, 1)
        self.mainLayout.setColumnStretch(0, 1)
        self.mainLayout.setColumnStretch(1, 1)
        self.saveLayout(self.mainLayout, "main")

        self.setLayout(self.mainLayout)

        self.setWindowTitle("Title")
        QApplication.setStyle("Fusion")
#        self.show()

    def bottomRight(self):

        self.bottomRightBox = QGroupBox("Bottom Right")

        # Create Select Button
        chooseButton = QPushButton("Select")
        chooseButton.setMaximumWidth(100)
        chooseButton.setMaximumHeight(20)
        self.saveButton(chooseButton)
        chooseButton.clicked.connect(self.selectFunction)

        # Create Full Screen Button
        self.fullScreenButton = QPushButton("Full")
        self.fullScreenButton.setMaximumWidth(100)
        self.fullScreenButton.setMaximumHeight(20)
        self.saveButton(self.fullScreenButton)
        self.fullScreenButton.clicked.connect(self.swichFullScreen)

        # Create Layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(chooseButton)
        layout.addWidget(self.fullScreenButton)
        layout.addStretch(1)

        self.saveLayout(layout, "full")


        # Add Layout to GroupBox
        self.bottomRightBox.setLayout(layout)   


    def selectFunction(self):

        # Select Data
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '/Data/')
        df = pd.read_csv(str(filePath))
        x = df.x.tolist()
        y = df.y.tolist()

        # Create Figure
        self.figure.clf()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_facecolor('0.915')
        ax.set_title('Graphique')

        # Draw Graph
        self.canvas.draw()

    def saveLayout(self,obj, text):
         self.layoutMap[text] = obj

    def findLayout(self,text):
         return self.layoutMap[text]

    def saveButton(self,obj):
         self.buttonMap[obj.text()] = obj

    def findButton(self,text):
         return self.buttonMap[text]


    def swichFullScreen(self):
#        self.setLayout(self.findLayout("full"))           # ---
#        self.show()                                       # ---
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        if self.sender().text()== "Full":
            self.topLeftBox.hide()
            self.topRightBox.hide()
            self.bottomLeftBox.hide()
            self.bottomRightBox.hide()
            self.mainLayout.addWidget(self.bottomRightBox, 0, 0, 1, 2)
            self.bottomRightBox.show()
            self.fullScreenButton.setText("NoFull")

        else:
            self.bottomRightBox.hide()
            self.topLeftBox.show()
            self.topRightBox.show()
            self.bottomLeftBox.show()
            self.mainLayout.addWidget(self.bottomRightBox, 2, 1)
            self.bottomRightBox.show()
            self.fullScreenButton.setText("Full")            

    def topLeft(self):
        textEdit = QTextEdit()
        return textEdit
    def topRight(self):
        textEdit = QTextEdit()
        return textEdit
    def bottomLeft(self):
        textEdit = QTextEdit()
        return textEdit
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^       

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = mainApplication()
    mainWindow.setGeometry(200, 100, 1000, 600)  
    mainWindow.show()
    sys.exit(app.exec_())
