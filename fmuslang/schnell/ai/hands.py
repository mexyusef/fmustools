import cv2, math, os, time
import numpy as np

from .constants import (
	jempol0, telunjuk0, tengah0, manis0, kelingking0,
	tips,
	tebal,
	magenta, purple, cyan, yellow, red, green, blue,
	default_loc,
	
)
from .common import (
	beda_lebar,
	beda_tinggi, 
	divide_screen,
	flip_image,
	initialise,
	initialise_wh,
	kotak, bulat, garis, center, jarak,
	ruas_in_kotak,
	ruas_in_which_kotak,
	show_wait,
	show_wait_escape,
)

class HandTracking():

	def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
		self.mode = mode
		self.maxHands = maxHands
		self.detectionCon = detectionCon
		self.trackCon = trackCon

		import mediapipe as mp
		
		self.mpHands = mp.solutions.hands
		# gunakan pip install mediapipe==0.8.8		
		# https://github.com/google/mediapipe/issues/2818
		# https://giters.com/google/mediapipe/issues/2818
		# In the new version the model complexity attribute is added
		self.modelComplexity = 1
		self.hands = self.mpHands.Hands(self.mode, self.maxHands,
			# self.modelComplexity,
			self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils


	def findHands(self, img, draw=True):
		"""
		img adlh cv image hasil 
		success, img = capdevice.read()

		opencv = bgr
		mediapipe = rgb
		"""
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)
		# print(results.multi_hand_landmarks)
		if self.results.multi_hand_landmarks:
			for handLms in self.results.multi_hand_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
		return img


	def findPosition(self, img, handNo=0, draw=True):
		lmList = []
		if self.results.multi_hand_landmarks:
			# hanya 1 tangan
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				# print(id, lm)
				h, w, c = img.shape
				cx, cy = int(lm.x * w), int(lm.y * h)
				# print(id, cx, cy)
				lmList.append([id, cx, cy])
				if draw:
					cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

		return lmList


	def findPositionBbox(self, img, handNo=0, draw=True):
		xList = []
		yList = []
		bbox = []
		self.lmList = []

		if self.results.multi_hand_landmarks:
			# hanya 1 tangan
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				# print(id, lm)
				h, w, c = img.shape
				cx, cy = int(lm.x * w), int(lm.y * h)
				xList.append(cx)
				yList.append(cy)
				# print(id, cx, cy, xList)
				self.lmList.append([id, cx, cy])
				if draw:
					cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

			xmin, xmax = min(xList), max(xList)
			ymin, ymax = min(yList), max(yList)
			bbox = xmin, ymin, xmax, ymax

			if draw:
				# print('xmin:', xmin, 'xlist:', xList, 'ymin:', ymin, 'ylist:', yList)
				cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

		return self.lmList, bbox


	def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
		"""
		findDistance(tip1, tip2, cvimg)
		"""
		x1, y1 = self.lmList[p1][1:]
		x2, y2 = self.lmList[p2][1:]
		cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

		if draw:
			cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
			cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
			cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
			cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
			length = math.hypot(x2 - x1, y2 - y1)

		return length, img, [x1, y1, x2, y2, cx, cy]


	def fingersUp(self):
		"""
		[1,1,1,1,1]
		jk jempol..kelingking open
		"""
		fingers = []

		fingers.append(1 if beda_lebar(self.lmList, jempol0) else 0)
		for tip in tips[1:]:
			buka = beda_tinggi(self.lmList, tip)
			fingers.append(1 if buka else 0)

		return fingers


	def runInternal(self):
		pTime, cTime = 0, 0
		cap, w, h = initialise_wh()
		# detector = HandTracking()

		while True:
			success, img = cap.read()
			img = flip_image(img)
			img = self.findHands(img)
			self.lmList = self.findPosition(img, draw=False)

			if len(self.lmList) != 0:
				# print(lmList[jempol0])
				if beda_tinggi( self.lmList, telunjuk0 ):
					lm = self.lmList[telunjuk0]
					# print('telunjuk open di kotak', ruas_in_which_kotak(w, h, lm), f'utk lm {lm[1]},{lm[2]}')
					print('telunjuk open di kotak', ruas_in_which_kotak(w, h, lm))
					# print('telunjuk open di kotak', lmList[telunjuk0])

				# if beda_lebar( lmList, jempol0 ):
				# 	print('jempol is open')

			cTime = time.time()
			fps_ = 1 / (cTime - pTime)
			fps = str(int(fps_))
			pTime = cTime

			cv2.putText(img, fps, default_loc, cv2.FONT_HERSHEY_PLAIN, 3, magenta, tebal)

			divide_screen(cap, img)

			if show_wait_escape(img):
				break
		
		cap.release()
		cv2.destroyAllWindows()
		print('selesai')


	def run(self):
		try:
			self.runInternal()
		except EOFError:
			print('Quitting')

		self.quit()

	def quit(self):
		cv2.destroyAllWindows()
		print('end')

	def painterInternal(self):
		pTime, cTime = 0, 0
		cap, w, h = initialise_wh()
		# detector = HandTracking()

		while True:
			success, img = cap.read()
			img = flip_image(img)
			img = self.findHands(img)
			self.lmList = self.findPosition(img, draw=False)

			if len(self.lmList) != 0:
				# if beda_tinggi( lmList, telunjuk0 ):
				# 	lm = lmList[telunjuk0]
				# 	print('telunjuk open di kotak', ruas_in_which_kotak(w, h, lm))

				telunjuk = self.lmList[telunjuk0][1:]
				x1,y1=telunjuk
				tengah = self.lmList[tengah0][1:]
				x2,y2=tengah

				fingers = self.fingersUp()
				print(fingers)

				if fingers[1] and fingers[2]:
					print('selection')
					kotak(img, x1,y1-25,x2,y2+25,warna=purple)
				elif fingers[1] and not fingers[2]:
					print('drawing')
					bulat(img, x1,y1)

			cTime = time.time()
			fps_ = 1 / (cTime - pTime)
			fps = str(int(fps_))
			pTime = cTime

			cv2.putText(img, fps, default_loc, cv2.FONT_HERSHEY_PLAIN, 3, magenta, tebal)

			divide_screen(cap, img)

			if show_wait_escape(img):
				break
		
		cap.release()
		cv2.destroyAllWindows()

	def painter(self):
		try:
			self.painterInternal()
		except EOFError:
			print('Quitting')

		self.quit()


	def distanceInternal(self):
		pTime, cTime = 0, 0
		cap, w, h = initialise_wh()

		while True:
			success, img = cap.read()
			img = flip_image(img)
			img = self.findHands(img)
			self.lmList = self.findPosition(img, draw=False)

			if len(self.lmList) != 0:
				jempol = self.lmList[jempol0][1:]
				x0,y0 = jempol
				telunjuk = self.lmList[telunjuk0][1:]
				x1,y1 = telunjuk
				tengah = self.lmList[tengah0][1:]
				x2,y2 = tengah
				# bulatkan ujung
				bulat(img, x0,y0, warna=cyan)
				bulat(img, x1,y1, warna=cyan)
				# bulat(img, x2,y2, warna=blue)
				d = jarak(*jempol, *telunjuk)
				cx,cy = center(x0,y0,x1,y1)
				if d < 50:
					bulat(img, cx,cy, warna=purple)
				else:
					bulat(img, cx,cy, warna=cyan)
				garis(img,*jempol,*telunjuk, warna=green)

			divide_screen(cap, img)

			# show_wait(img)
			if show_wait_escape(img):
				break
		
		cap.release()
		cv2.destroyAllWindows()

	def distance(self):
		try:
			self.distanceInternal()
		except EOFError:
			print('Quitting')

		self.quit()





	def bboxInternal(self):
		pTime, cTime = 0, 0
		cap, w, h = initialise_wh()
		# detector = HandTracking()

		while True:
			success, img = cap.read()
			img = flip_image(img)
			img = self.findHands(img)
			self.lmList, bbox = self.findPositionBbox(img, draw=True)

			if len(self.lmList) != 0:
				# print(lmList[jempol0])
				# if beda_tinggi( self.lmList, telunjuk0 ):
					# lm = self.lmList[telunjuk0]
					# print('telunjuk open di kotak', ruas_in_which_kotak(w, h, lm), f'utk lm {lm[1]},{lm[2]}')
					# print('telunjuk open di kotak', ruas_in_which_kotak(w, h, lm))
					# print('telunjuk open di kotak', lmList[telunjuk0])

				# if beda_lebar( lmList, jempol0 ):
				# 	print('jempol is open')

				# gampang jarak telunjuk dan jempol
				# gampang click = jarak jauh
				fingers = self.fingersUp()
				# index, middle = fingers[1], fingers[2]
				thumb, index = fingers[0], fingers[1]
				if thumb and index:
					length, img, lineInfo = self.findDistance(telunjuk0, jempol0, img)
					# if length < 40:
					# 	lm = self.lmList[telunjuk0]
					# 	bulat(img, lineInfo[4], lineInfo[5], warna=green)
					# 	print('pilihan kotak', ruas_in_which_kotak(w, h, lm))

					if length > 80:
						lm = self.lmList[jempol0] # jempol jadi pemilih kotak
						bulat(img, lineInfo[4], lineInfo[5], warna=green)
						print('pilihan kotak', ruas_in_which_kotak(w, h, lm))


			divide_screen(cap, img)

			if show_wait_escape(img):
				break
		
		cap.release()
		cv2.destroyAllWindows()
		print('selesai')


	def bbox(self):
		try:
			self.bboxInternal()
		except EOFError:
			print('Quitting')
