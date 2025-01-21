# https://gist.githubusercontent.com/Axel-Erfurt/fe931658e72b8ee70ccebc6a86a5902e/raw/42316745225ac5b7301ae2047aff9a3cd6adc03e/PyQt5_Downloader.py
# https://gist.github.com/Axel-Erfurt/fe931658e72b8ee70ccebc6a86a5902e
import sys
from PyQt5.QtWidgets import (
    QWidget, 
    QPushButton, 
    QLineEdit, 
    QProgressBar, 
    QApplication, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel, 
    QFileDialog,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QSettings, QStandardPaths

import queue #If this template is not loaded, pyinstaller may not be able to run the requests template after packaging
import requests
import subprocess
################################################


################################################
class Downloader(QWidget):
  def __init__(self, *args, **kwargs):
      super(Downloader, self).__init__(*args, **kwargs)
      
      self.settings = QSettings("MyDownloader", "MyDownloader")
      self.setWindowTitle("Downloader")

      self.setWindowIcon(QIcon.fromTheme("download"))
      layout = QVBoxLayout(self)
      hlayout = QHBoxLayout()
      
      self.dpath = ""
      print(self.dpath)
      self.readSettings()
      self.url = ""
      self.fname = ""

      self.setFixedSize(600, 170)

      # Download Button
      self.pushButton = QPushButton(self, maximumWidth=100)
      self.pushButton.setToolTip('<b>Download</b>')
      self.pushButton.setText("Download")
      self.pushButton.setIcon(QIcon.fromTheme("download"))
      self.pushButton.setStyleSheet("QPushButton::hover {background: #729fcf;}")
      hlayout.addWidget(self.pushButton)
      self.pushButton.clicked.connect(self.on_pushButton_clicked)
      
      # Cancel Button
      self.cancelButton = QPushButton(self, maximumWidth=100)
      self.cancelButton.setText("Cancel")
      self.cancelButton.setIcon(QIcon.fromTheme("cancel"))
      self.cancelButton.setStyleSheet("QPushButton::hover {background: #729fcf;}")
      hlayout.addWidget(self.cancelButton)
      self.cancelButton.setEnabled(False)
      self.cancelButton.clicked.connect(self.on_cancelButton_clicked)
      
      # Settings Button
      self.settingsButton = QPushButton(self, maximumWidth=32)
      self.settingsButton.setToolTip("choose Download Folder")
      self.settingsButton.setIcon(QIcon.fromTheme("folder"))
      self.settingsButton.setStyleSheet("QPushButton::hover {background: #729fcf;}")
      hlayout.addWidget(self.settingsButton)
      self.settingsButton.clicked.connect(self.on_settingsButton_clicked)
      
      # Space to align Buttons left
      empty = QWidget()
      hlayout.addWidget(empty)
      
      # Bar
      self.progressBar = QProgressBar(self, minimumWidth=300)
      self.progressBar.setFixedHeight(14)
      self.progressBar.setStyleSheet("QProgressBar {font-size: 7pt;}")
      self.progressBar.setValue(0)
      
      # Url Field
      self.urlfield = QLineEdit()
      self.urlfield.setPlaceholderText("URL")
      self.urlfield.textChanged.connect(self.extractFilename)
      layout.addWidget(self.urlfield)
      
      # Name Field
      self.namefield = QLineEdit()
      self.namefield.setPlaceholderText("Filename")
      layout.addWidget(self.namefield)
      
      layout.addWidget(self.progressBar)
      
      # StatusBar
      self.lbl = QLabel("status")
      layout.addLayout(hlayout)
      layout.addWidget(self.lbl)
      
      self.lbl.setStyleSheet("QLabel {font-size: 8pt; background: transparent; color: #555753}")
      self.lbl.setText(f"Ready - Download Path: {self.dpath}")
      
      self.clip = QApplication.clipboard()
      if self.clip.text().startswith("http"):
          self.urlfield.setText(self.clip.text())
          
  def on_settingsButton_clicked(self):
      path = QFileDialog.getExistingDirectory(self, "Select Folder", self.dpath)
      if path:
          self.dpath = path
          self.settings.setValue("folder", self.dpath)
          self.lbl.setText(f"changed Download Path to: {self.dpath}")
      else:
          return
  
  def writeSettings(self):
      self.settings.setValue("folder", self.dpath)
      
  def readSettings(self):
      if self.settings.contains("folder"):
          self.dpath = self.settings.value("folder")
      else:
          self.dpath = QStandardPaths.standardLocations(QStandardPaths.MoviesLocation)[0]
      
  def extractFilename(self):
      t = self.urlfield.text().split('/')[-1]
      self.namefield.setText(f"{self.dpath}/{t}")

  def on_pushButton_clicked(self):
      if self.urlfield.text().startswith("http") or self.urlfield.text().startswith("ftp"):
          the_url = self.urlfield.text()
          the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
          the_filepath = self.namefield.text()
          the_fileobj = open(the_filepath, 'wb')
          #### Create a download thread
          self.downloadThread = downloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
          self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
          self.downloadThread.start()
          self.lbl.setText("Download started ...")
          self.cancelButton.setEnabled(True)

  # Setting progress bar
  def set_progressbar_value(self, value):
      self.progressBar.setValue(value)
      if value == 100:
          self.lbl.setText("Download success!")
          self.sendMessage()

  def on_cancelButton_clicked(self):
      self.downloadThread.terminate()
      self.lbl.setText("Download cancelled")
      self.cancelButton.setEnabled(False)
      
  def sendMessage(self):
      title = 'Downloader'
      message = 'Download success!'
      icon = "info"
      timeout = 5000
      msg = ["notify-send", "-i", icon, title, message, '-t', str(timeout)]
      subprocess.Popen(msg)


##################################################################
#Download thread
##################################################################
class downloadThread(QThread):
  download_proess_signal = pyqtSignal(int)                        #Create signal

  def __init__(self, url, filesize, fileobj, buffer):
      super(downloadThread, self).__init__()
      self.url = url
      self.filesize = filesize
      self.fileobj = fileobj
      self.buffer = buffer


  def run(self):
      try:
          rsp = requests.get(self.url, stream=True)                #Streaming download mode
          offset = 0
          for chunk in rsp.iter_content(chunk_size=self.buffer):
              if not chunk: break
              self.fileobj.seek(offset)                            #Setting Pointer Position
              self.fileobj.write(chunk)                            #write file
              offset = offset + len(chunk)
              proess = offset / int(self.filesize) * 100
              self.download_proess_signal.emit(int(proess))        #Sending signal
          #######################################################################
          self.fileobj.close()    #Close file
          self.exit(0)            #Close thread


      except Exception as e:
          print(e)

####################################
#Program entry
####################################
if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = Downloader()
  w.show()
  sys.exit(app.exec_())
  