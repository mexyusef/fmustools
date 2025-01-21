import cv2
import os
from .dirutils import absolutify, isabsolute, isdir, joiner, disini, suffix_filename, dirname
from .notifutils import notifpy
from .utils import trycopy


def images_to_video(output_video, list_of_images=[], image_folder=None, fps=15.0, delay=500):
	"""
	delay dalam milliseconds misalnya 500 utk 0.5 detik.
	"""
	print(f"""images_to_video
	output_video={output_video}
	list_of_images={list_of_images}
	image_folder={image_folder}
	fps={fps}
	delay={delay}
	""")
	fourcc = cv2.VideoWriter_fourcc(*"mp4v")

	if list_of_images:
		img = cv2.imread(list_of_images[0])
		height, width, layers = img.shape
		video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

		for image in list_of_images:
			video.write(cv2.imread(image))
			if delay:
				cv2.waitKey(delay) # wait

		cv2.destroyAllWindows()
		video.release()
		message = f'{list_of_images} => {output_video}'
	elif image_folder:
		images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
		images.sort()
		img = cv2.imread(images[0])
		height, width, layers = img.shape
		video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

		for image in images:
			video.write(cv2.imread(image))
			if delay:
				cv2.waitKey(delay) # wait

		cv2.destroyAllWindows()
		video.release()
		message = f'{image_folder} => {output_video}'
	else:
		# print("No images found.")
		message = "No images found."

	notifpy('/vidutils)images_to_video', message)
	trycopy(output_video)
