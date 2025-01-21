# https://gist.githubusercontent.com/Axel-Erfurt/08613e953aea2ef88c499f853076cae5/raw/4203ab158ef6e1240237fceeeeefeb4f4914e366/YouTubeDL.py
# https://gist.github.com/Axel-Erfurt/08613e953aea2ef88c499f853076cae5
#############################################################################
from PyQt5.QtCore import (QFile, QPoint, QRect, QSize, QStandardPaths, 
Qt, QProcess, QSettings)
from PyQt5.QtGui import QIcon, QFont, QClipboard
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow, QLineEdit, QProgressBar,
QMessageBox, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QMessageBox, QToolButton, QComboBox)

quote = str(chr(34))
class MainWindow(QMainWindow):
  def __init__(self):
      super(MainWindow, self).__init__()
      btnwidth = 155
      self.ytdlExec = ""
      self.ytUrl = ''
      self.OutFolder = '/tmp'
      self.settings = QSettings('YouTubeDL', 'YTDL')
      self.setAttribute(Qt.WA_DeleteOnClose)
      self.createStatusBar()
      pyfile = QStandardPaths.findExecutable("youtube-dl")
      if not pyfile == "":
          print("found " + pyfile)
          self.ytdlExec = pyfile
      else:
          self.msgbox("youtube-dl not found\nPlease install youtube-dl")

      self.cmd = ''
      self.process = QProcess(self)
      self.process.started.connect(lambda: self.showMessage("creating List"))
      self.process.finished.connect(lambda: self.showMessage("finished creating List"))
      self.process.finished.connect(self.processFinished)
      self.process.readyRead.connect(self.processOut)

      self.dlProcess = QProcess(self)
      self.dlProcess.setProcessChannelMode(QProcess.MergedChannels)
      self.dlProcess.started.connect(lambda: self.showMessage("download started"))
      self.dlProcess.finished.connect(lambda: self.showMessage("download finished"))
      self.dlProcess.finished.connect(lambda: self.setWindowTitle("YouTube Download GUI"))
      self.dlProcess.readyRead.connect(self.dlProcessOut)

      self.list = []

      self.setGeometry(0, 0, 600, 220)
      self.setFixedSize(600, 220)
      self.setStyleSheet(myStyleSheet(self))
      self.setWindowIcon(QIcon.fromTheme("video-playlist"))
      #### path
      lblUrl = QLabel()
      lblUrl.setText("insert URL or YouTube id:")
      lblUrl.setAlignment(Qt.AlignRight)
      lblUrl.setFixedWidth(btnwidth)
      lblUrl.setFont(QFont("Noto Sans", 9))
      lblUrl.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
      self.lblURLpath = QLineEdit("")
      self.lblURLpath.setPlaceholderText("insert URL and press ENTER to get list of available files")
      self.lblURLpath.returnPressed.connect(self.fillCombo)

      hlayout = QHBoxLayout()
      hlayout.addWidget(lblUrl)
      hlayout.addWidget(self.lblURLpath)

      #### output path
      btnOutPath = QToolButton()
      btnOutPath.setFont(QFont("Noto Sans", 9))
      btnOutPath.setIcon(QIcon.fromTheme("gtk-open"))
      btnOutPath.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
      btnOutPath.setText("select Output Folder")
      btnOutPath.setFixedWidth(btnwidth)
      btnOutPath.clicked.connect(self.openOutFolder)
      self.lblOutPath = QLineEdit()
      self.lblOutPath.setPlaceholderText("insert output folder path")
      self.lblOutPath.textChanged.connect(self.updateOutputPath)

      hlayout2 = QHBoxLayout()
      hlayout2.addWidget(btnOutPath)
      hlayout2.addWidget(self.lblOutPath)

      #### ytdlExec path
      btnYTDLpath = QToolButton()
      btnYTDLpath.setFont(QFont("Noto Sans", 9))
      btnYTDLpath.setIcon(QIcon.fromTheme("document-open"))
      btnYTDLpath.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
      btnYTDLpath.setText("select youtube-dl")
      btnYTDLpath.setFixedWidth(btnwidth)
      btnYTDLpath.clicked.connect(self.selectYTDL)
      self.lblYTDLpath = QLineEdit(str(self.ytdlExec))
      self.lblYTDLpath.textChanged.connect(self.updatelblYTDLpath)
      self.lblYTDLpath.setPlaceholderText("insert path to youtube-dl")


      hlayout3 = QHBoxLayout()
      hlayout3.addWidget(btnYTDLpath)
      hlayout3.addWidget(self.lblYTDLpath)

      dlBtn = QToolButton()
      dlBtn.setIcon(QIcon.fromTheme("download"))
      dlBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
      dlBtn.setText("Download")
      dlBtn.setFont(QFont("Noto Sans", 14))
      dlBtn.clicked.connect(self.downloadSelected)
      dlBtn.setFixedWidth(btnwidth)
      dlBtn.setFixedHeight(32)

      dlCancelBtn = QToolButton()
      dlCancelBtn.setIcon(QIcon.fromTheme("cancel"))
      dlCancelBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
      dlCancelBtn.setText("Cancel")
      dlCancelBtn.setFont(QFont("Noto Sans", 14))
      dlCancelBtn.clicked.connect(self.cancelDownload)
      dlCancelBtn.setFixedWidth(btnwidth)
      dlCancelBtn.setFixedHeight(32)

      self.dlCombo = QComboBox()
      self.dlCombo.setFixedHeight(26)

      self.pbar = QProgressBar()
      self.pbar.setFixedHeight(16)
      self.pbar.setFont(QFont("Helvetica", 7))
      self.pbar.setMaximum(100)
      self.pbar.setMinimum(0)
      self.pbar.setValue(0)

      btnLayout = QHBoxLayout()
      btnLayout.addWidget(dlBtn)
      btnLayout.addWidget(dlCancelBtn)

      vlayout = QVBoxLayout()
      vlayout.addLayout(hlayout)
      vlayout.addLayout(hlayout2)
      vlayout.addLayout(hlayout3)
      vlayout.addWidget(self.dlCombo)
      vlayout.addWidget(self.pbar)
      vlayout.addLayout(btnLayout)

      mywidget = QWidget()
      mywidget.setLayout(vlayout)

      self.setCentralWidget(mywidget)

      self.clip = QApplication.clipboard()
      if self.clip.text().startswith("http"):
          self.lblURLpath.setText(self.clip.text())
          self.fillCombo()
      else:
          if len(self.clip.text()) < 12:
              self.lblURLpath.setText(self.clip.text())
              self.fillCombo()

      self.readSettings()
      self.setWindowTitle("YouTube Download GUI")

  def closeEvent(self, e):
      self.writeSettings()
      e.accept()

  def readSettings(self):
      print("reading settings")
      if self.settings.contains('geometry'):
          self.setGeometry(self.settings.value('geometry'))
      if self.settings.contains('outFolder'):
          self.lblOutPath.setText(self.settings.value('outFolder'))

  def writeSettings(self):
      print("writing settings")
      self.settings.setValue('outFolder', self.OutFolder)
      self.settings.setValue('geometry', self.geometry())

  def updateOutputPath(self):
      self.OutFolder = self.lblOutPath.text()
      self.showMessage("output path changed to: " + self.lblOutPath.text())

  def updatelblYTDLpath(self):
      self.ytdlExec = self.lblYTDLpath.text()
      self.showMessage("youtube-dl path changed to: " +self.lblYTDLpath.text())

  def showMessage(self, message):
      self.statusBar().showMessage(message, 0)

  def selectYTDL(self):
        fileName,_ = QFileDialog.getOpenFileName(self, "locate ytdlExec", "/usr/local/bin/ytdlExec",  "exec Files (*)")
        if fileName:
          self.lblYTDLpath.setText(fileName)
          self.ytdlExec = fileName

  def openOutFolder(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.Directory)
      fileName = dlg.getExistingDirectory()
      if fileName:
          self.lblOutPath.setText(fileName)


  def fillCombo(self):
      self.dlCombo.clear()
      if QFile.exists(self.ytdlExec):
          self.list = []
          self.ytUrl = self.lblURLpath.text()
          if not self.lblURLpath.text() == "":
              print("fill Combo")
              self.process.start(self.ytdlExec,['-F', self.ytUrl])
      else:
          self.showMessage("youtube-dl missing")
      
  def processOut(self):
          try:
              output = str(self.process.readAll(), encoding = 'utf8').rstrip()
          except Error:
              output = str(self.process.readAll()).rstrip()          
          self.list.append(output)

  def processFinished(self):
          out = ','.join(self.list)
          out = out.partition("resolution note")[2]
          out = out.partition('\n')[2]
          mylist = out.rsplit('\n')
          self.dlCombo.addItems(mylist)
          count = self.dlCombo.count()
          self.dlCombo.setCurrentIndex(count-1)

  def downloadSelected(self):
      if QFile.exists(self.ytdlExec):
          self.pbar.setValue(0)
          quality = self.dlCombo.currentText().partition(" ")[0]
          options = []
          options.append('-f')
          options.append(quality)
          options.append("-o")
          options.append("%(title)s.%(ext)s")
          options.append(self.ytUrl)
          if not quality == "":
              self.showMessage("download started")
              print("download selected quality:", quality)
              self.dlProcess.setWorkingDirectory(self.OutFolder)
              self.dlProcess.start(self.ytdlExec, options)
          else:
              self.showMessage("list of available files is empty")
      else:
          self.showMessage("youtube-dl missing")

  def dlProcessOut(self):
      try:
          out = str(self.dlProcess.readAll(), encoding = 'utf8').rstrip()
      except Error:
          out = str(self.dlProcess.readAll()).rstrip()
      out = out.rpartition("[download] ")[2]
      self.showMessage("Progress: " + out)
      self.setWindowTitle(out)
      out = out.rpartition("%")[0].rpartition(".")[0]
      if not out == "":
          try:
              pout = int(out)
              self.pbar.setValue(pout)
          except ValueError:
              pass

  def cancelDownload(self):
      if self.dlProcess.state() == QProcess.Running:
          print("process is running, will be cancelled")
          self.dlProcess.close()
          self.showMessage("Download cancelled")
          self.pbar.setValue(0)
      else:
          self.showMessage("process is not running")

  def createStatusBar(self):
      self.statusBar().showMessage("Ready")

  def msgbox(self, message):
      QMessageBox.warning(self, "Message", message)

def myStyleSheet(self):
  return """

QStatusBar
{
font-family: Helvetica;
font-size: 8pt;
color: #666666;
}
QProgressBar:horizontal {
border: 1px solid gray;
border-radius: 2px;
background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d3d3d3, stop:1 #e9e9e9);
padding: 1px;
text-align: right;
margin-right: 4ex;
}
QProgressBar::chunk:horizontal 
{
background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 blue, stop: 1 white);
margin-right: 2px;
width: 8px;
}
  """    


if __name__ == '__main__':
  import sys
  app = QApplication(sys.argv)
  mainWin = MainWindow()
  mainWin.show()
  sys.exit(app.exec_())
