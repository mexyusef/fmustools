# https://gist.githubusercontent.com/Axel-Erfurt/ec3133dffd0c28f97a759f07c63e15b1/raw/883470910941ac19c69256e483211f3efd95c510/SpeedTest.py
# https://gist.github.com/Axel-Erfurt/ec3133dffd0c28f97a759f07c63e15b1
import csv, codecs, time, os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from PyQt5.QtCore import (QFile, QFileInfo, QPoint, QRect, QSettings, QSize,
      Qt, QTextStream, QProcess, QDir)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow,
      QTableWidget, QTableWidgetItem, QComboBox, QAbstractItemView)

class MainWindow(QMainWindow):
  def __init__(self):
      super(MainWindow, self).__init__()

      self.path = QDir(QDir.homePath()  + '/SpeedTest')
      if not QDir.exists(self.path):
          print("Dir not exists, creating now ...")
          dir = QDir()
          newfolder = QDir.homePath()  + '/SpeedTest'
          dir.mkpath(newfolder)
      self.myfile = QDir.homePath()  + '/SpeedTest' + '/SpeedTest.csv'
      self.isChanged = False
      self.setStyleSheet(stylesheet(self))
      self.speedtestExec = "/usr/local/bin/speedtest-cli"
      self.cmd = ''
      self.list = []
      self.date = ""
      self.time = ""
      self.download = ""
      self.upload = ""
      self.ping = ""
      self.server = ""
      self.process = QProcess(self)
      self.process.started.connect(lambda: self.showMessage("running Speed Test"))
#        self.process.finished.connect(lambda: self.showMessage("Test ended"))
      self.process.finished.connect(self.processFinished)
      self.process.readyRead.connect(self.processOut)

      self.tableview = QTableWidget()
      self.tableview.setColumnCount(6)
      self.setHeaders()
      self.tableview.verticalHeader().setVisible(False)
      self.tableview.horizontalHeader().setVisible(False)
      self.tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
      self.setCentralWidget(self.tableview)
      self.setWindowIcon(QIcon.fromTheme('network'))
      self.createToolBars()
      self.createStatusBar()
      self.readSettings()
      self.loadCsvOnOpen()
      self.fillComboBox()
      self.setMinimumSize(440, 220)

  def showChartDL(self):      
      data = []
      for row in range(self.tableview.rowCount()):
          data.append(float(self.tableview.item(row, 2).text()))
      print(data) 
      performance = data
      y_pos = np.arange(len(performance))
      plt.bar(y_pos, performance, align='center', alpha=0.5)
      plt.xticks(y_pos, "")
      plt.ylabel('Mbit/s')
      plt.title('Speed Test Chart - Download')
#        plt.savefig("/tmp/dl.png")
      plt.show()

  def showChartUpload(self):  
      plt.rcParams['toolbar'] = 'None'    
      data = []
      for row in range(self.tableview.rowCount()):
          data.append(float(self.tableview.item(row, 3).text()))
      print(data) 
      performance = data
      y_pos = np.arange(len(performance))
      plt.bar(y_pos, performance, align='center', alpha=0.5)
      plt.xticks(y_pos, "")
      plt.ylabel('Mbit/s')
      plt.title('Speed Test Chart - Upload')
      plt.tight_layout()
      plt.show()

  def fillComboBox(self):
      plt.rcParams['toolbar'] = 'None'   
      cmd = self.speedtestExec + " --list"
      serverlist = []
      myprocess = QProcess()
      myprocess.start(cmd)
      myprocess.waitForFinished(-1)
      output = str(myprocess.readAll(), encoding = 'utf8').rstrip()       
      serverlist.append(output)
      out = ','.join(serverlist)
      out = out.partition("Retrieving speedtest.net configuration...")[2]
      out = out.partition('\n')[2]
      mylist = out.rsplit('\n')
      self.combo.addItem("auto")
      self.combo.addItems(mylist)
      self.combo.setCurrentIndex(1)

  def setHeaders(self):
      self.tableview.horizontalHeader().setVisible(True)
      font = QFont()
      font.setPointSize(8)
      self.tableview.horizontalHeader().setFont(font)
      self.tableview.setColumnWidth(0, 80)
      self.tableview.setColumnWidth(1, 60)
      self.tableview.setColumnWidth(2, 70)
      self.tableview.setColumnWidth(3, 60)
      self.tableview.setColumnWidth(4, 60)
      self.tableview.setColumnWidth(5, 100)
      self.tableview.setHorizontalHeaderItem(0, QTableWidgetItem("Date"))
      self.tableview.setHorizontalHeaderItem(1, QTableWidgetItem("Time"))
      self.tableview.setHorizontalHeaderItem(2, QTableWidgetItem("Download"))
      self.tableview.setHorizontalHeaderItem(3, QTableWidgetItem("Upload"))
      self.tableview.setHorizontalHeaderItem(4, QTableWidgetItem("Ping"))
      self.tableview.setHorizontalHeaderItem(5, QTableWidgetItem("Server"))

  def showMessage(self, message):
      self.statusBar().showMessage(message)

  def closeEvent(self, event):
      self.writeSettings()
      if self.isChanged == True:
          self.writeCSV()
      event.accept()

  def createActions(self):
      root = QFileInfo(__file__).absolutePath()

  def createToolBars(self):
      self.tb = self.addToolBar("File")
      self.tb.setMovable(False)
      self.testAct = QAction(QIcon.fromTheme('media-playback-start'), "Start", self,
              statusTip="Test starten",
              triggered=self.startTest)
      self.tb.addAction(self.testAct)
      self.combo = QComboBox()
      self.combo.setFixedWidth(400)
      self.tb.addWidget(self.combo)
      self.chartActD = QAction(QIcon.fromTheme('chart'), "Download Chart", self,
              statusTip="show Chart",
              triggered=self.showChartDL)
      self.tb.addAction(self.chartActD)
      self.chartActU = QAction(QIcon.fromTheme('chart'), "Upload Chart", self,
              statusTip="show Chart",
              triggered=self.showChartUpload)
      self.tb.addAction(self.chartActU)

  def startTest(self):
      self.started = time.time()
      self.list = []
      self.date = ""
      self.time = ""
      self.download = ""
      self.upload = ""
      self.ping = ""
      self.server = ""
      if self.combo.currentText() == "auto":
          print("auto")
          self.cmd = self.speedtestExec
      else:
          myserver = self.combo.currentText().partition(")")[0]
          self.cmd = self.speedtestExec + " --server "  + myserver
      print("Speed Test started *** " + self.cmd)
      if QFile.exists(self.speedtestExec):
#            self.stopwatch(90)
          self.process.start(self.cmd)
      else:
          self.showMessage("speedtest-cli not found")

  def createStatusBar(self):
      self.showMessage("Ready")

  def readSettings(self):
      settings = QSettings("Axel Schneider", "SpeedTest")
      pos = settings.value("pos", QPoint(200, 200))
      size = settings.value("size", QSize(400, 400))
      self.resize(size)
      self.move(pos)

  def writeSettings(self):
      settings = QSettings("Axel Schneider", "SpeedTest")
      settings.setValue("pos", self.pos())
      settings.setValue("size", self.size())

  def loadCsvOnOpen(self):
      filename = self.myfile
      if QFile.exists(filename):
          f = open(filename, 'r', encoding='utf-8')
          self.tableview.setRowCount(0)
          self.tableview.setColumnCount(0)
          for rowdata in csv.reader(f, delimiter='\t'):
              row = self.tableview.rowCount()
              self.tableview.insertRow(row)
              if len(rowdata) == 0:
                  self.tableview.setColumnCount(len(rowdata) + 1)
              else:
                  self.tableview.setColumnCount(len(rowdata))
              for column, data in enumerate(rowdata):
                  item = QTableWidgetItem(data)
                  self.tableview.setItem(row, column, item)
#            self.tableview.selectRow(0)
          self.tableview.horizontalHeader().setStretchLastSection(True)
          self.setHeaders()
          self.tableview.resizeRowsToContents()
          last = self.tableview.rowCount() - 1
          self.tableview.selectRow(last)

  def addRow(self):
      row = self.tableview.rowCount()
      newItem = QTableWidgetItem(time.strftime('%d.%m.%Y'))
      self.tableview.insertRow(row)
      self.tableview.horizontalHeader().setStretchLastSection(True)
      column = 0
      self.tableview.setItem(row,column, newItem)
      newItem = QTableWidgetItem(time.strftime('%H:%M'))
      column = 1
      self.tableview.setItem(row,column, newItem)
      newItem = QTableWidgetItem(self.download)
      column = 2
      self.tableview.setItem(row,column, newItem)
      newItem = QTableWidgetItem(self.upload)
      column = 3
      self.tableview.setItem(row,column, newItem)
      newItem = QTableWidgetItem(self.ping)
      column = 4
      self.tableview.setItem(row,column, newItem)
      newItem = QTableWidgetItem(self.server)
      column = 5
      self.tableview.setItem(row,column, newItem)
      self.isChanged = True
      last = self.tableview.rowCount() - 1
      self.tableview.selectRow(last)
      self.ended = time.time() - self.started
      m, s = divmod(time.time() - self.started, 60)
      h, m = divmod(m, 60)
      time_str = "%02d:%02d" % (m, s)
      print('Operation completed in', time_str)
      self.tableview.resizeRowsToContents()
      self.showMessage('Speed Test completed in ' +  time_str)

  def processOut(self):
          try:
              output = str(self.process.readAll(), encoding = 'utf8').rstrip()
          except Error:
              output = str(self.process.readAll()).rstrip()          
          self.list.append(output)

  def processFinished(self):
          out = ','.join(self.list)
          self.download = out.partition("Download: ")[2]
          self.download = self.download.partition(' Mbit/s')[0]

          self.upload = out.partition("Upload: ")[2]
          self.upload = self.upload.partition(' Mbit/s')[0]

          self.ping = out.partition("km]: ")[2]
          self.ping = self.ping.partition(' ms')[0]
          self.ping = self.ping.partition('.')[0]

          self.server = out.partition("Hosted by ")[2]
          self.server = self.server.partition(' [')[0]

          self.addRow()

#    def writeCSV(self):
#        with open(self.myfile, 'w') as stream:
#            print("saving", self.myfile)
#            writer = csv.writer(stream, delimiter='\t')
#            for row in range(self.tableview.rowCount()):
#                rowdata = []
#                for column in range(self.tableview.columnCount()):
#                    item = self.tableview.item(row, column)
#                    if item is not None:
#                        rowdata.append(item.text())
#                    else:
#                        rowdata.append('')
#                writer.writerow(rowdata)
#        self.isChanged = False

  def writeCSV(self):
      with open(self.myfile, 'w') as stream:
          print("saving", self.myfile)
          writer = csv.writer(stream, delimiter='\t')
          for row in range(self.tableview.rowCount()):
              rowdata = []
              for column in range(self.tableview.columnCount()):
                  item = self.tableview.item(row, column)
                  if item is not None:
                      rowdata.append(item.text())
                  else:
                      rowdata.append('')
              writer.writerow(rowdata)
      self.isChanged = False

def stylesheet(self):
      return """
      QTableWidget
      {
          border: 1px solid grey;
          border-radius: 0px;
          font-family: Noto Sans;
          font-size: 8pt;
          background-color: #ebebeb;
          selection-color: #ffffff
      }

        
      QTableWidget::item:selected 
      {
          color: #F4F4F4;
          background: qlineargradient(x1:0, y1:0, x1:2, y1:2, stop:0 #bfc3fb, stop:1 #324864);
      } 
  """

if __name__ == '__main__':

  import sys
  app = QApplication(sys.argv)
  mainWin = MainWindow()
  mainWin.show()
  sys.exit(app.exec_())
