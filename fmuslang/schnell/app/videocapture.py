
import cv2
import numpy as np
import time
from PIL import ImageGrab

from constants import mapwarna
from .grabutils import grabber
from .utils import trycopy
from .notifutils import notifpy

screen_size = (1920, 1080)

def video_capture(
		outputfile='c:/tmp/mycapture.mp4', timeout=10, fps=24.0, text=None, bbox=None, x=0, y=0, w=screen_size[0], h=screen_size[1],
		warna='white', lineType = 2, font = cv2.FONT_HERSHEY_SIMPLEX,
		thickness=4,
		show_notif=True,
	):
	# Set the screen size
	# Set the codec and create a video writer object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')

	if not bbox:
		bbox = (x,y,w,h)
		out = cv2.VideoWriter(outputfile, fourcc, fps, screen_size)
	else:
		w = bbox[2]-bbox[0]
		h = bbox[3]-bbox[1]
		out = cv2.VideoWriter(outputfile, fourcc, fps, (w, h))

	# # Define the font and text for the recording indicator
	# font = cv2.FONT_HERSHEY_SIMPLEX
	# bottomLeftCornerOfText = (10,screen_size[1]-10)
	# fontScale = 1
	fontColor = mapwarna[warna] # (0,0,255) # Red color
	# lineType = 2
	positions = []
	if text:
		# format text: <x,y,scale,warna>tulisan atau <x,y>tulisan saja
		if '|' in text:
			pecah = text.split('|')
			for i, teks in enumerate(pecah, 1):
				fontScale = 2.0
				# pengali = 0.8
				# font = ImageFont.truetype(huruf, ukuranhuruf)
				print(f"i {i}, teks {teks}")
				x = 0.1
				y = 0.8
				if teks.startswith('<') and '>' in teks:
					kiri, kanan = [item.strip() for item in teks.split('>')]
					teks = kanan
					kiri = kiri.removeprefix('<')
					# for xy in [item.strip() for item in kiri.split(',')]:
					xy = kiri.split(',')
					if len(xy)==4:
						x,y,fontScale,warna=[item.strip() for item in xy]
						fontColor = mapwarna[warna]
						x=float(x)
						y=float(y)
						fontScale=float(fontScale)
					elif len(xy)==3:
						x,y,fontScale=[item.strip() for item in xy]
						x=float(x)
						y=float(y)
						fontScale=float(fontScale)
					elif len(xy)==2:
						x,y = [float(item.strip()) for item in xy]
				# else:
				x = int(x*w)
				y = int(y*h)
				item = (x,y, teks, fontScale,fontColor)
				positions.append(item)
		else:
			x = 0.1
			y = 0.8
			teks = text
			if teks.startswith('<') and '>' in teks:
				kiri, kanan = [item.strip() for item in teks.split('>')]
				teks = kanan
				kiri = kiri.removeprefix('<')
				# for xy in [item.strip() for item in kiri.split(',')]:
				xy = kiri.split(',')
				if len(xy)==4:
					x,y,fontScale,warna=[item.strip() for item in xy]
					fontColor = mapwarna[warna]
					x=float(x)
					y=float(y)
					fontScale=float(fontScale)
				elif len(xy)==3:
					x,y,fontScale=[item.strip() for item in xy]
					x=float(x)
					y=float(y)
					fontScale=float(fontScale)
				elif len(xy)==2:
					x,y = [float(item.strip()) for item in xy]
			# else:
			x = int(x*w)
			y = int(y*h)
			item = (x,y, teks, fontScale, fontColor)
			positions.append(item)

	print('video_capture, bbox:', bbox)

	# Record the start time
	start_time = time.time()

	while time.time() - start_time < timeout:
		# Capture the screen
		img = ImageGrab.grab(bbox=bbox)

		# Convert the image to a numpy array
		frame = np.array(img)

		# Convert the colors from BGR to RGB
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		# # Add the recording indicator text to the frame
		# cv2.putText(frame,'Recording...',
		#     bottomLeftCornerOfText,
		#     font,
		#     fontScale,
		#     fontColor,
		#     lineType)
		for (x,y, teks, fontScale,fontColor) in positions:
			# bisa bikin rect...
			if teks.startswith('rect'):
				'''
				rect(x,y,w,h)
				rect(x,y,w,h,color)
				cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
				'''
				# cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
				_, specs = teks.split('(')
				specs = specs.removesuffix(')')
				parts = [item.strip() for item in specs.split(',')]
				if len(parts)==4: # x,y,w,h
					x0,y0,w0,h0=[float(i) for i in parts]
					x0=int(x0*w)
					y0=int(y0*h)
					w0=int(w0*w)
					h0=int(h0*h)
					cv2.rectangle(frame, (x0, y0), (x0 + w0, y0 + h0), fontColor, thickness=-1)
				elif len(parts)==5: # x,y,w,h,warna
					x0,y0,w0,h0,warna=parts
					x0,y0,w0,h0=float(x0),float(y0),float(w0),float(h0)
					x0=int(x0*w)
					y0=int(y0*h)
					w0=int(w0*w)
					h0=int(h0*h)
					color = mapwarna[warna]
					cv2.rectangle(frame, (x0, y0), (x0 + w0, y0 + h0), color, thickness=-1)
			else:
				cv2.putText(frame, teks, (x,y), font, fontScale, color=fontColor, lineType=lineType, thickness=thickness)

		# Write the frame to the video file
		out.write(frame)

	# Release the resources
	out.release()
	cv2.destroyAllWindows()

	# print('saved to:', outputfile)
	if show_notif:
		notifpy('[video_capture]', f'saved to {outputfile}')
		trycopy(outputfile)
	return outputfile

# /video)filepath
# /video)filepath|10
# /video)filepath|60
# video_capture(timeout=10, outputfile='c:/tmp/mycapture.mp4')


def video_capture_grab(outputfile='c:/tmp/mycapture.mp4', timeout=10, fps=24.0, text=None, show_notif=True):
	def capture_setelah_bbox(bbox):
		assert bbox, "video_capture_grab => Bbox not set"
		print('video_capture_grab callback...')
		video_capture(outputfile=outputfile, timeout=timeout, fps=fps, text=text, bbox=bbox, show_notif=show_notif)
	grabber(capture_setelah_bbox)
