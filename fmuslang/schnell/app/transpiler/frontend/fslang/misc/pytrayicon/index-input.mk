--% index/fmus
pytray,d(/mk)
	main.py,f(e=__FILE__=/main.py)
	icon.png,f(img=ava1)
	icon1.png,f(img=ava1)
	icon2.png,f(img=ava1)
	icon3.png,f(img=ava1)
	run.sh,f(n=python main.py)
	$*chmod a+x run.sh
--#

--% /main.py
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
# https://www.geeksforgeeks.org/pyqt5-message-box/
# https://stackoverflow.com/questions/37201338/how-to-place-custom-image-onto-qmessagebox
# messagebox = QtGui.QMessageBox(QtGui.QMessageBox.Warning, 
# "Title text", "body text", 
# buttons = QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok, parent=self)
# messagebox.setDefaultButton(QtGui.QMessageBox.Cancel)
# exe = messagebox.exec_()
# After creating the QMessageBox, just call 
# messagebox.setIconPixmap(QPixmap(":/images/image_file))
# where image_file is the path to your image resource.

def show_info_messagebox():
  msg = QMessageBox()
  # msg.setIcon(QMessageBox.Information)
  # msg.setIconPixmap(QPixmap(":/icon1.png"))
  # msg.setIcon(icon3)
  msg.setIconPixmap(pixmap3)

  # setting message for Message Box
  msg.setText("Information ")
    
  # setting Message box window title
  msg.setWindowTitle("Information MessageBox")

  # declaring buttons on Message Box
  msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
  # start the app
  retval = msg.exec_()

def show_warning_messagebox():
  msg = QMessageBox()
  msg.setIcon(QMessageBox.Warning)
  # msg.setIconPixmap(QPixmap(":/icon2.png"))
  msg.setIconPixmap(pixmap2)
  # msg.setWindowIcon(QIcon(":/icon2.png"));

  # setting message for Message Box
  msg.setText("Warning")
    
  # setting Message box window title
  msg.setWindowTitle("Warning MessageBox")

  # declaring buttons on Message Box
  msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
  # start the app
  retval = msg.exec_()

def show_critical_messagebox():
  msg = QMessageBox()
  msg.setIcon(QMessageBox.Critical)

  # setting message for Message Box
  msg.setText("Critical")
    
  # setting Message box window title
  msg.setWindowTitle("Critical MessageBox")

  # declaring buttons on Message Box
  msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
  # start the app
  retval = msg.exec_()

# https://www.geeksforgeeks.org/system-tray-applications-using-pyqt5/
app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# https://stackoverflow.com/questions/42248147/qmessagebox-seticon-doesnt-set-the-icon
# image = QImage()
# image.loadFromData(data)
# https://www.programcreek.com/python/example/106694/PyQt5.QtGui.QImage
image1 = QImage('./icon1.png')
pixmap1 = QPixmap(image1).scaledToHeight(32, Qt.SmoothTransformation)

image2 = QImage('./icon2.png')
pixmap2 = QPixmap(image2).scaledToHeight(32, Qt.SmoothTransformation)

icon3 = QIcon('./icon3.png')
image3 = QImage('./icon3.png')
pixmap3 = QPixmap(image3).scaledToHeight(32, Qt.SmoothTransformation)

# Adding an icon
iconfile = "icon.png"
menulabel1 = "Pertama"
menulabel2 = "Kedua"
icon = QIcon(iconfile)
  
# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options
menu = QMenu()
# TODO: kasih aksi pada QAction berikut
option1 = QAction("Pertama")
option2 = QAction("Kedua")
option3 = QAction("Ketiga")
# https://www.geeksforgeeks.org/pyqt5-qaction/
# adding triggered action to the first action
option1.triggered.connect(lambda: show_info_messagebox())
# adding triggered action to the second action
option2.triggered.connect(lambda: show_warning_messagebox())
option3.triggered.connect(lambda: show_critical_messagebox())

menu.addAction(option1)
menu.addAction(option2)
menu.addAction(option3)
  
# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)
  
# Adding options to the System Tray
tray.setContextMenu(menu)
  
app.exec_()
--#
