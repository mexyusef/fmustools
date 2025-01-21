import cv2, math, os, time
import numpy as np

from .constants import (
	jempol0, telunjuk0, tengah0, manis0, kelingking0,
	tips,
	tebal,
	magenta, purple, cyan, yellow, red, green, blue,
	default_loc,

	bahukiri, bahukanan,
)

from .common import (
	beda_lebar,
	beda_tinggi, 
	divide_screen,
	flip_image,
	initialise,
	initialise_wh,
	kotak, bulat, garis, center, jarak,
	lm_xy,
	ruas_in_kotak,
	ruas_in_which_kotak,
	show_wait,
	show_wait_escape,
	real_quit,
)

class PoseTracking():

	def __init__(self, 
							 mode=False, 
							 upBody=False, 
							 smooth=True, 
							 detectionCon=0.5, 
							 trackCon=0.5):
		self.mode = mode
		self.upBody = upBody
		self.smooth = smooth
		self.detectionCon = detectionCon
		self.trackCon = trackCon
		import mediapipe as mp
		self.mpDraw = mp.solutions.drawing_utils
		self.mpPose = mp.solutions.pose
		self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)


	def findPose(self, img, draw=True):
		try:
			imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		except Exception as err:
			print('Mungkin video telah selesai...', err)
			return None

		self.results = self.pose.process(imgRGB)
		if self.results.pose_landmarks:
			if draw:
				self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
		return img


	def findPosition(self, img, draw=True):
		self.lmList = []
		if self.results.pose_landmarks:
			for id, lm in enumerate(self.results.pose_landmarks.landmark):
				h, w, c = img.shape
				# print(id, lm)
				cx, cy = int(lm.x * w), int(lm.y * h)
				self.lmList.append([id, cx, cy])
				if draw:
					cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
		return self.lmList


	def findAngle(self, img, p1, p2, p3, draw=True):
		# Get the landmarks
		x1, y1 = self.lmList[p1][1:]
		x2, y2 = self.lmList[p2][1:]
		x3, y3 = self.lmList[p3][1:]

		# Calculate the Angle
		angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
		if angle < 0:
			angle += 360

		# print(angle)

		# Draw
		if draw:
			cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
			cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
			cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
			cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
			cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
			cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
			cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
			cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
			cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
		
		return angle


	def run(self):
		try:
			self.runInternal()
		except EOFError:
			print('Quitting')

		self.quit()

	def quit(self):
		cv2.destroyAllWindows()
		print('end')
		# real_quit()


	def runInternal(self):
		pTime, cTime = 0, 0
		cap = cv2.VideoCapture('/home/usef/dwhelper/gaia.mp4')
		# detector = poseDetector()
		while True:
			success, img = cap.read()
			img = self.findPose(img)
			
			if img is None:
				print('quitting while krn img is None')
				break

			lmList = self.findPosition(img, draw=False)

			if len(lmList) != 0:
				# print(lmList[14])
				# cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
				# leftshoulders = lmList[bahukiri][1:]
				leftshoulders = lm_xy(lmList, bahukiri, 30, 30)
				# rightshoulders = lmList[bahukanan][1:]
				rightshoulders = lm_xy(lmList, bahukanan, -30, 30)
				bulat(img, *leftshoulders, warna=red)
				bulat(img, *rightshoulders, warna=yellow)

			cTime = time.time()
			fps = 1 / (cTime - pTime)
			pTime = cTime

			cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

			# cv2.imshow("Image", img)
			# cv2.waitKey(1)
			if show_wait_escape(img):
				break

		cap.release()
		cv2.destroyAllWindows()

