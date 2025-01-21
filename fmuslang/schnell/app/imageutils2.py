from typing import List
import cv2
import numpy as np
from PIL import ImageGrab

from .grabutils import grabber
from .dirutils import absolutify, isabsolute, joiner, disini, suffix_filename, dirname, isfile, bongkar
from .notifutils import notifpy
from .utils import trycopy


def merge_images(list_of_images: List[str], output_image: str = '', method: str = 'horizontal'):
	"""
	images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
	merge_images('merged_image_horizontal.jpg', images, method='horizontal')
	merge_images('merged_image_vertical.jpg', images, method='vertical')

	"""
	if method not in ['horizontal', 'vertical']:
		raise ValueError('Method should be either "horizontal" or "vertical"')
	if not list_of_images:
		raise ValueError('input images gak boleh kosong')
	if not output_image:
		output_image = suffix_filename(list_of_images[0], '_merged')
	for img in images:
		if not isfile(img):
			raise ValueError(f'{img} tidak ditemukan')

	# Load all images
	images = [cv2.imread(img) for img in list_of_images]

	# Get the maximum height and width of all images
	max_height = max([img.shape[0] for img in images])
	max_width = max([img.shape[1] for img in images])

	# Create a canvas to merge all images
	if method == 'horizontal':
		canvas = np.zeros((max_height, max_width * len(images), 3), dtype=np.uint8)
	else:
		canvas = np.zeros((max_height * len(images), max_width, 3), dtype=np.uint8)

	# Merge all images into the canvas
	for i, img in enumerate(images):
		if method == 'horizontal':
			canvas[:img.shape[0], i * max_width:(i + 1) * max_width] = img
		else:
			canvas[i * max_height:(i + 1) * max_height, :img.shape[1]] = img

	# Save the output image
	cv2.imwrite(output_image, canvas)
	notifpy('/imgutils)merge_images', f'lihat merged images di {output_image}')
	trycopy(output_image)


def merge_images2(list_of_images: List[str], output_image: str = '', method: str = 'horizontal'):
	if method not in ['horizontal', 'vertical']:
		raise ValueError('Method should be either "horizontal" or "vertical"')
	if not list_of_images:
		raise ValueError('input images gak boleh kosong')
	if not output_image:
		output_image = suffix_filename(list_of_images[0], '_merged')

	# Load all images
	images = [cv2.imread(img) for img in list_of_images]

	# Get the maximum height and width of all images
	max_height = max([img.shape[0] for img in images])
	max_width = max([img.shape[1] for img in images])

	# Create a canvas to merge all images
	if method == 'horizontal':
		canvas = np.zeros((max_height, max_width * len(images), 3), dtype=np.uint8)
	else:
		canvas = np.zeros((max_height * len(images), max_width, 3), dtype=np.uint8)

	# Merge all images into the canvas
	offset = 0
	for img in images:
		h, w = img.shape[:2]
		if method == 'horizontal':
			new_canvas = np.zeros((max_height, w, 3), dtype=np.uint8)
			new_canvas[:h, :w] = img
			canvas[:, offset:offset+w] = new_canvas
			offset += w
		else:
			new_canvas = np.zeros((h, max_width, 3), dtype=np.uint8)
			new_canvas[:h, :w] = img
			canvas[offset:offset+h, :] = new_canvas
			offset += h

	# Save the output image
	cv2.imwrite(output_image, canvas)
	notifpy('/imgutils)merge_images2', f'lihat merged images di {output_image}')
	trycopy(output_image)


def get_screen_bbox():
	screen = cv2.VideoCapture(0)
	width = int(screen.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(screen.get(cv2.CAP_PROP_FRAME_HEIGHT))
	screen.release()
	return (0, 0, width, height)


def screen_capture(output_file, whole_screen=False):
	print("""[imgutils2/screen_capture]
	=> {output_file}
	""")
	def capture_setelah_bbox(bbox):
		assert bbox, "Bbox not set"
		print('image_capture_grab callback, bbox:', bbox)
		img = ImageGrab.grab(bbox)
		img.save(output_file, "PNG")
		img.close()
	if not whole_screen:
		grabber(capture_setelah_bbox)
	else:
		capture_setelah_bbox(get_screen_bbox())
