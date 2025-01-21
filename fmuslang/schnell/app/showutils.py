import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

font = cv2.FONT_HERSHEY_SIMPLEX
# org = (self.video_width-150, 50)
org = (150, 150)
font_scale = 4
color = (255, 255, 255)
thickness = 10

class VideoPlayer(QWidget):
	def __init__(self, initial_video=None):
		super().__init__()
		self.file_name = initial_video
		self.initUI()
		if self.file_name:
			self.play_video()

	def play_video(self):
		"""
		play: self.file_name
		"""
		self.cap = cv2.VideoCapture(self.file_name)
		# Set properties of video label and timer
		self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
		self.video_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.video_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.video_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.video_label.setFixedSize(self.video_width, self.video_height)
		self.timer.start(int(1000/self.fps))
	
	def initUI(self):
		# Create menu to open mp4 file
		menubar = QMenuBar(self)
		fileMenu = menubar.addMenu('File')
		openFile = QAction('Open', self)
		openFile.triggered.connect(self.open_file)
		fileMenu.addAction(openFile)

		# Create canvas to play mp4 video
		self.video_label = QLabel(self)
		self.video_label.setAlignment(Qt.AlignCenter)

		# Create play/pause button
		self.play_button = QPushButton('Play', self)
		self.play_button.clicked.connect(self.play_pause)

		# Create current time information label of video
		self.time_label = QLabel(self)

		# Create timer to update current time label and overlay frame number
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_video)
		self.frame_num = 0

		# Create layout
		vbox = QVBoxLayout()
		vbox.addWidget(self.video_label)
		hbox = QHBoxLayout()
		hbox.addWidget(self.play_button)
		hbox.addWidget(self.time_label)
		vbox.addLayout(hbox)
		self.setLayout(vbox)

		# Set window properties
		# self.setWindowTitle('Video Player')
		# self.setGeometry(100, 100, 600, 400)
		# self.show()

	def open_file(self):
		# Open file dialog to select mp4 file
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, 'Select Video File', '', 'Video Files (*.mp4)', options=options)
		if fileName:
			self.file_name = fileName
			self.cap = cv2.VideoCapture(self.file_name)

			# Set properties of video label and timer
			self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
			self.video_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
			self.video_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
			self.video_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
			self.video_label.setFixedSize(self.video_width, self.video_height)
			self.timer.start(int(1000/self.fps))

	def play_pause(self):
		# Play or pause video
		if self.play_button.text() == 'Play':
			self.play_button.setText('Pause')
			self.timer.start(int(1000/self.fps))
		else:
			self.play_button.setText('Play')
			self.timer.stop()

	def keyPressEvent(self, event):
		# Space key press to toggle play/pause
		if event.key() == Qt.Key_Space:
			self.play_pause()

	def update_video(self):
		# Update current time label and overlay frame number
		ret, frame = self.cap.read()
		if ret:
			self.frame_num += 1
			if self.frame_num > self.video_length:
				self.frame_num = 1
				self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

			# Overlay frame number on top right corner of frame
			frame = cv2.putText(frame, f'{self.frame_num}', org, font, font_scale, color, thickness, cv2.LINE_AA)

			# Set frame to video label
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
			pixmap = QPixmap.fromImage(img)
			self.video_label.setPixmap(pixmap)

			# Update current time label
			current_time = int(self.cap.get(cv2.CAP_PROP_POS_MSEC)/1000)
			total_time = int(self.video_length/self.fps)
			self.time_label.setText(f'{current_time}/{total_time} sec')

		else:
			self.timer.stop()
			self.cap.release()
			self.play_button.setText('Play')
			self.frame_num = 0


if __name__ == '__main__':
	app = QApplication(sys.argv)
	filepath = r'c:\fr\work\bow3e.mp4'
	if len(sys.argv)==2 and sys.argv[1]:
		filepath = sys.argv[1]
	player = VideoPlayer(filepath)
	player.setWindowTitle(filepath)
	player.setGeometry(50, 50, 600, 400)
	player.show()
	sys.exit(app.exec_())
