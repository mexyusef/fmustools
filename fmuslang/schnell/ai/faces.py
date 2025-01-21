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
)

class FaceTracking():

	def __init__(self, minDetectionCon=0.5):
		import mediapipe as mp
		self.minDetectionCon = minDetectionCon
		self.mpFaceDetection = mp.solutions.face_detection
		self.mpDraw = mp.solutions.drawing_utils
		self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

	def findFaces(self, img, draw=True):
		try:
			imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		except Exception as err:
			print('Mungkin video telah selesai...', err)
			return None, None

		self.results = self.faceDetection.process(imgRGB)
		# print(self.results)
		bboxs = []

		if self.results.detections:
			for id, detection in enumerate(self.results.detections):
				bboxC = detection.location_data.relative_bounding_box
				ih, iw, ic = img.shape
				bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
				bboxs.append([id, bbox, detection.score])
				if draw:
					img = self.fancyDraw(img,bbox)
					cv2.putText(img, f'{int(detection.score[0] * 100)}%',
														(bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
														2, (255, 0, 255), 2)

		return img, bboxs

	def fancyDraw(self, img, bbox, l=30, t=5, rt= 1):
		x, y, w, h = bbox
		x1, y1 = x + w, y + h
		cv2.rectangle(img, bbox, (255, 0, 255), rt)
		# Top Left  x,y
		cv2.line(img, (x, y), (x + l, y), (255, 0, 255), t)
		cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)
		# Top Right  x1,y
		cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
		cv2.line(img, (x1, y), (x1, y+l), (255, 0, 255), t)
		# Bottom Left  x,y1
		cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
		cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)
		# Bottom Right  x1,y1
		cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
		cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)
		return img



	def run(self):
		try:
			self.runInternal()
		except EOFError:
			print('Quitting')

		self.quit()

	def quit(self):
		cv2.destroyAllWindows()
		print('end')


	def runInternal(self):
		pTime, cTime = 0, 0
		cap = cv2.VideoCapture('/home/usef/dwhelper/gaia.mp4')
		# detector = FaceDetector()
		while True:
			success, img = cap.read()
			img, bboxs = self.findFaces(img)
			
			if img is None:
				print('quitting while krn img is None')
				break

			print(bboxs)

			cTime = time.time()
			fps = 1 / (cTime - pTime)
			pTime = cTime

			cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

			cv2.imshow("Image", img)
			cv2.waitKey(1)




class FaceMesh():

	def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
		self.staticMode = staticMode
		self.maxFaces = maxFaces
		self.minDetectionCon = minDetectionCon
		self.minTrackCon = minTrackCon
		import mediapipe as mp
		self.mpDraw = mp.solutions.drawing_utils
		self.mpFaceMesh = mp.solutions.face_mesh
		self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.minDetectionCon, self.minTrackCon)
		self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)
	

	def findFaceMesh(self, img, draw=True):
		try:
			self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		except Exception as err:
			print('Mungkin video telah selesai...', err)
			return None, None

		self.results = self.faceMesh.process(self.imgRGB)
		faces = []
		if self.results.multi_face_landmarks:
			for faceLms in self.results.multi_face_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS, self.drawSpec, self.drawSpec)

				face = []
				for id,lm in enumerate(faceLms.landmark):
					#print(lm)
					ih, iw, ic = img.shape
					x,y = int(lm.x*iw), int(lm.y*ih)
					#cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 1)
					#print(id,x,y)
					face.append([x,y])

				faces.append(face)

		return img, faces
	

	# def fancyDraw(self, img, bbox, l=30, t=5, rt= 1):
	# 	x, y, w, h = bbox
	# 	x1, y1 = x + w, y + h
	# 	cv2.rectangle(img, bbox, (255, 0, 255), rt)
	# 	# Top Left  x,y
	# 	cv2.line(img, (x, y), (x + l, y), (255, 0, 255), t)
	# 	cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)
	# 	# Top Right  x1,y
	# 	cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
	# 	cv2.line(img, (x1, y), (x1, y+l), (255, 0, 255), t)
	# 	# Bottom Left  x,y1
	# 	cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
	# 	cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)
	# 	# Bottom Right  x1,y1
	# 	cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
	# 	cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)
	# 	return img



	def run(self):
		try:
			self.runInternal()
		except EOFError:
			print('Quitting')

		self.quit()

	def quit(self):
		cv2.destroyAllWindows()
		print('end')


	def runInternal(self):
		pTime, cTime = 0, 0
		cap = cv2.VideoCapture('/home/usef/dwhelper/gaia.mp4')
		# detector = FaceDetector()
		while True:
			success, img = cap.read()
			img, faces = self.findFaceMesh(img)
			
			if img is None:
				print('quitting while krn img is None')
				break

			# if len(faces)!= 0:
			# 	print(faces[0])

			cTime = time.time()
			fps = 1 / (cTime - pTime)
			pTime = cTime

			cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

			cv2.imshow("Image", img)
			cv2.waitKey(1)

