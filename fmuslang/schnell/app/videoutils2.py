import cv2
import numpy as np
import os, datetime, math
from PIL import Image

from .dirutils import absolutify, isabsolute, joiner, disini, suffix_filename, dirname
from .notifutils import notifpy
from .utils import trycopy
from .mediautils import mapwarna


def add_overlay(video_path, overlay_path, video_output=None, scale_percent=100, x=0.5, y=0.5):
	"""
	overlay image to video
	"""
	if not video_output:
		video_output = suffix_filename(video_path, '_overlayed')
	# Read the video
	cap = cv2.VideoCapture(video_path)

	# Read the overlay image with alpha channel
	overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

	# Get the width and height of the overlay image
	overlay_height, overlay_width, _ = overlay.shape

	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(video_output, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

	while cap.isOpened():
		ret, frame = cap.read()
		if ret:
			# Resize the overlay image
			scale_width = int(overlay_width * scale_percent / 100)
			scale_height = int(overlay_height * scale_percent / 100)
			overlay_resized = cv2.resize(overlay, (scale_width, scale_height))
			# Check if the overlay image has an alpha channel
			overlay_channels = overlay_resized.shape[2]

			# Get the region of interest on the video frame
			roi = frame[0:overlay_resized.shape[0], 0:overlay_resized.shape[1]]

			# Create a mask for the overlay image
			# mask = overlay_resized[:, :, 3]
			if overlay_channels == 4:
				# Create a mask for the overlay image
				mask = overlay_resized[:, :, 3]
			else:
				# If alpha channel is not present, use a white mask
				mask = cv2.cvtColor(overlay_resized, cv2.COLOR_BGR2GRAY)

			# Invert the mask
			mask_inv = cv2.bitwise_not(mask)

			# Extract the color channels from the overlay image
			overlay_rgb = overlay_resized[:, :, 0:3]

			# Apply the mask to the overlay image
			overlay_fg = cv2.bitwise_and(overlay_rgb, overlay_rgb, mask=mask)

			# Apply the inverted mask to the region of interest
			roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

			# Add the overlay image and the region of interest
			dst = cv2.add(roi_bg, overlay_fg)

			# Replace the region of interest on the video frame with the merged image
			frame[0:overlay_resized.shape[0], 0:overlay_resized.shape[1]] = dst

			# Write the merged frame to the output video
			out.write(frame)

			# # Display the merged frame
			# cv2.imshow('frame', frame)
			# if cv2.waitKey(1) & 0xFF == ord('q'):
			# 	break
		else:
			break

	# Release the resources
	cap.release()
	out.release()
	cv2.destroyAllWindows()
	notifpy('/vidutils)add_overlay', f'{video_path} menjadi {video_output}')
	trycopy(video_output)


def add_overlay2(video_path, overlay_path, video_output=None, scale_percent=100, x=0, y=0):
	"""
	overlay image to video
	"""
	if not video_output:
		video_output = suffix_filename(video_path, '_overlaid')
	# Read the video
	cap = cv2.VideoCapture(video_path)

	# Read the overlay image with alpha channel
	overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

	# Get the width and height of the overlay image
	overlay_height, overlay_width, _ = overlay.shape

	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(video_output, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

	while cap.isOpened():
		ret, frame = cap.read()
		if ret:
			# Resize the overlay image
			scale_width = int(overlay_width * scale_percent / 100)
			scale_height = int(overlay_height * scale_percent / 100)
			overlay_resized = cv2.resize(overlay, (scale_width, scale_height))

			# Check if the overlay image has an alpha channel
			overlay_channels = overlay_resized.shape[2]

			# Calculate the region of interest on the video frame
			x_pos = int(x * overlay_width)
			y_pos = int(y * overlay_height)
			roi = frame[y_pos:y_pos+overlay_resized.shape[0], x_pos:x_pos+overlay_resized.shape[1]]

			# Create a mask for the overlay image
			if overlay_channels == 4:
				# Create a mask for the overlay image
				mask = overlay_resized[:, :, 3]
			else:
				# If alpha channel is not present, use a white mask
				mask = cv2.cvtColor(overlay_resized, cv2.COLOR_BGR2GRAY)

			# Invert the mask
			mask_inv = cv2.bitwise_not(mask)

			# Extract the color channels from the overlay image
			overlay_rgb = overlay_resized[:, :, 0:3]

			# Apply the mask to the overlay image
			overlay_fg = cv2.bitwise_and(overlay_rgb, overlay_rgb, mask=mask)

			# Apply the inverted mask to the region of interest
			roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

			# Add the overlay image and the region of interest
			dst = cv2.add(roi_bg, overlay_fg)

			# Replace the region of interest on the video frame with the merged image
			frame[y_pos:y_pos+overlay_resized.shape[0], x_pos:x_pos+overlay_resized.shape[1]] = dst

			# Write the merged frame to the output video
			out.write(frame)

		else:
			break

	# Release the resources
	cap.release()
	out.release()
	cv2.destroyAllWindows()


def add_overlay3(video_path, overlay_path, video_output=None, x=0, y=0, transparency=1.0, scale_percent=100):
	"""
	overlay image to video
	"""
	if not video_output:
		video_output = suffix_filename(video_path, '_overlaid')
	# Read the video
	cap = cv2.VideoCapture(video_path)

	# Read the overlay image with alpha channel
	overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

	# Get the width and height of the overlay image
	overlay_height, overlay_width, _ = overlay.shape

	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(video_output, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

	while cap.isOpened():
		ret, frame = cap.read()
		if ret:
			# Resize the overlay image
			scale_width = int(overlay_width * scale_percent / 100)
			scale_height = int(overlay_height * scale_percent / 100)
			overlay_resized = cv2.resize(overlay, (scale_width, scale_height))

			# Check if the overlay image has an alpha channel
			overlay_channels = overlay_resized.shape[2]
			if overlay_channels == 4:
				# Create a mask for the overlay image
				mask = overlay_resized[:, :, 3]
				# Multiply the alpha channel with the overlay image's RGB channels
				overlay_resized = cv2.cvtColor(overlay_resized, cv2.COLOR_BGRA2RGBA)
				overlay_resized[:, :, :3] *= (mask[:, :, None] / 255.0) * transparency
				overlay_resized = cv2.cvtColor(overlay_resized, cv2.COLOR_RGBA2BGRA)
			else:
				# If alpha channel is not present, use a white mask
				mask = cv2.cvtColor(overlay_resized, cv2.COLOR_BGR2GRAY)

			# Invert the mask
			mask_inv = cv2.bitwise_not(mask)

			# Get the region of interest on the video frame
			x_offset = int(x * overlay_width)
			y_offset = int(y * overlay_height)
			roi = frame[y_offset:y_offset + overlay_resized.shape[0], x_offset:x_offset + overlay_resized.shape[1]]

			# Apply the mask to the overlay image
			if overlay_channels == 4:
				overlay_fg = overlay_resized[:, :, :3]
				overlay_alpha = overlay_resized[:, :, 3:4]
				overlay_fg = cv2.bitwise_and(overlay_fg, overlay_fg, mask=mask)
				overlay_alpha = cv2.bitwise_and(overlay_alpha, overlay_alpha, mask=mask)
				overlay_resized = cv2.merge([overlay_fg, overlay_alpha])
			else:
				overlay_resized = cv2.bitwise_and(overlay_resized, overlay_resized, mask=mask)

			# Apply the inverted mask to the region of interest
			roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

			# Add the overlay image and the region of interest
			dst = cv2.add(roi_bg, overlay_resized)

			# Replace the region of interest on the video
			# Replace the region of interest on the video frame with the merged image
			frame[y:y+overlay_resized.shape[0], x:x+overlay_resized.shape[1]] = dst

			# Write the merged frame to the output video
			out.write(frame)

			# # Display the merged frame
			# cv2.imshow('frame', frame)
			# if cv2.waitKey(1) & 0xFF == ord('q'):
			#   break
		else:
			break

	# Release the resources
	cap.release()
	out.release()
	cv2.destroyAllWindows()


def create_image_grid(images, scale, output_path):
	"""
	Creates a new image containing all images in a 2x2 grid.
	
	Args:
		images (list): List of 4 images with same size.
		scale (float): Scaling factor to reduce size of each image.
		output_path (str): Path to save resulting image.
	"""
	# Load images and resize them
	resized_images = []
	for image in images:
		resized_image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
		resized_images.append(resized_image)

	# Create the 2x2 grid
	top_row = np.hstack((resized_images[0], resized_images[1]))
	bottom_row = np.hstack((resized_images[2], resized_images[3]))
	grid = np.vstack((top_row, bottom_row))

	# Save the resulting image
	cv2.imwrite(output_path, grid)


def create_image_grid2(images, scale=0.25, output_path=None):
	"""
	images = terima pil images
	Creates a new image containing all images arranged in a grid.
	The grid dimensions are based on the number of images:
	- 4 images: 2x2 grid
	- 5-9 images: 3x3 grid
	- 10-16 images: 4x4 grid
	- and so on
	
	Args:
		images (list): List of images with same size.
		scale (float): Scaling factor to reduce size of each image.
		output_path (str): Path to save resulting image.
	"""
	if not images:
		print('no images')
		return
	# if not output_path:
	# 	firstimage = images[0]
	# 	output_path = dirname(firstimage)

	num_images = len(images)

	# Determine grid size based on number of images
	rows = math.ceil(math.sqrt(num_images))
	cols = math.ceil(num_images / rows)
	grid_size = (rows, cols)

	# Load images and resize them
	resized_images = []
	for image in images:
		resized_image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
		resized_images.append(resized_image)

	# Create the grid
	grid = np.zeros((int(grid_size[0] * resized_images[0].shape[0]),
					 int(grid_size[1] * resized_images[0].shape[1]),
					 3), dtype=np.uint8)

	for i, resized_image in enumerate(resized_images):
		row = int(i / grid_size[1])
		col = i % grid_size[1]
		grid[row * resized_image.shape[0]:(row + 1) * resized_image.shape[0], 
			 col * resized_image.shape[1]:(col + 1) * resized_image.shape[1]] = resized_image
	
	# Save the resulting image
	cv2.imwrite(output_path, grid)
	notifpy('/vidutils)create_image_grid2', f'lihat grid images di {output_path}')
	trycopy(output_path)


def create_image_grid3(image_paths, scale=0.25, output_path=None):
	"""
	images = terima image paths

	Creates a new image containing all images arranged in a grid.
	The grid dimensions are based on the number of images:
	- 4 images: 2x2 grid
	- 5-9 images: 3x3 grid
	- 10-16 images: 4x4 grid
	- and so on
	
	Args:
		image_paths (list): List of file paths to images.
		scale (float): Scaling factor to reduce size of each image.
		output_path (str): Path to save resulting image.
	"""
	if not image_paths:
		print('no images')
		return
	if not output_path:
		firstimage = image_paths[0]
		output_path = suffix_filename(firstimage, '_gridded')

	print(f"output_path={output_path}, image_paths={image_paths}")

	images = [cv2.imread(image_path) for image_path in image_paths]
	num_images = len(images)
	
	# Determine grid size based on number of images
	rows = math.ceil(math.sqrt(num_images))
	cols = math.ceil(num_images / rows)
	grid_size = (rows, cols)
	
	# Load images and resize them
	resized_images = []
	for image in images:
		resized_image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
		resized_images.append(resized_image)
	
	# Create the grid
	grid = np.zeros((int(grid_size[0] * resized_images[0].shape[0]), 
					 int(grid_size[1] * resized_images[0].shape[1]), 
					 3), dtype=np.uint8)
	
	for i, resized_image in enumerate(resized_images):
		row = int(i / grid_size[1])
		col = i % grid_size[1]
		grid[row * resized_image.shape[0]:(row + 1) * resized_image.shape[0], 
			 col * resized_image.shape[1]:(col + 1) * resized_image.shape[1]] = resized_image
	
	# Save the resulting image
	cv2.imwrite(output_path, grid)


def create_shots(input_video_file, number_of_shots=8):
	cap = cv2.VideoCapture(input_video_file)
	fps = cap.get(cv2.CAP_PROP_FPS)
	frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	seconds = frame_count / fps
	interval = seconds / number_of_shots
	shots = []
	current_time = 0
	count = 0
	while count < number_of_shots and current_time <= seconds:
		cap.set(cv2.CAP_PROP_POS_MSEC, current_time * 1000)
		ret, frame = cap.read()
		if ret:
			# Add time text in the upper right corner
			# time_str = str(datetime.timedelta(seconds=current_time))
			time_str = "{:02d}:{:02d}:{:02d}".format(int(current_time // 3600), int((current_time % 3600) // 60), int(current_time % 60))
			cv2.putText(frame, time_str, (frame.shape[1]-200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
			shots.append(frame)
			count += 1
		current_time += interval
	cap.release()
	return shots


def write_shots(input_video_file, number_of_shots=8, notify=True):
	# if not os.path.exists(output_dir):
	#     os.makedirs(output_dir)
	shots = create_shots(input_video_file, number_of_shots)
	# filename_format = os.path.splitext(os.path.basename(input_video_file))[0] + "_{:02d}.jpg"
	filenames = [suffix_filename(input_video_file, '_{:02d}'.format(i), replace_ext='jpg') for i in range(number_of_shots)]
	for i, shot in enumerate(shots):
		# filename = os.path.join(output_dir, filename_format.format(i))
		filename = filenames[i]
		cv2.imwrite(filename, shot)

	if notify:
		notifpy('/vidutils)write_shots', f'{input_video_file} menjadi {filenames}')
		trycopy('\n'.join(filenames))

	return filenames


def screenshots_grid(input_video_file, number_of_shots=8, scale=0.25, output_path=None):
	image_paths = write_shots(input_video_file, number_of_shots, notify=False)
	create_image_grid3(image_paths, scale=scale, output_path=output_path)
	notifpy('/vidutils)screenshots_grid', f'{input_video_file} menjadi {output_path}')
	trycopy(output_path)


def draw_line(image, x_percent, y_percent, color=(0,255,0), thickness=4):
	if isinstance(color, str):
		color = mapwarna[color]
	height, width, _ = image.shape
	x = int(x_percent * width)
	y = int(y_percent * height)
	start_point = (x, y)
	end_point = (width, y)
	cv2.line(image, start_point, end_point, color, thickness)
	return image


def draw_rectangle(image, x_percent=0.25, y_percent=0.25, w_percent=0.5, h_percent=0.5, color=(0,255,0), fill=True):
	if isinstance(color, str):
		color = mapwarna[color]
	height, width, _ = image.shape
	x = int(x_percent * width)
	y = int(y_percent * height)
	w = int(w_percent * width)
	h = int(h_percent * height)
	start_point = (x, y)
	end_point = (x + w, y + h)
	if fill:
		cv2.rectangle(image, start_point, end_point, color, -1)
	else:
		cv2.rectangle(image, start_point, end_point, color, 2)
	return image


def draw_rectangles_on_video(input_file, x_percent=0.25, y_percent=0.25, w_percent=0.5, h_percent=0.5, output_file=None, color=(0,255,0), fill=True):
	if isinstance(color, str):
		color = mapwarna[color]
	if not output_file:
		output_file = suffix_filename(input_file, '_rectangled')
	cap = cv2.VideoCapture(input_file)
	fps = cap.get(cv2.CAP_PROP_FPS)
	frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break
		frame_with_rect = draw_rectangle(frame, x_percent, y_percent, w_percent, h_percent, color, fill)
		out.write(frame_with_rect)

	cap.release()
	out.release()
	notifpy('/vidutils)draw_rectangles_on_video', f'{input_file} menjadi {output_file}')
	trycopy(output_file)


def draw_circle(image, x_percent, y_percent, radius_percent, color, fill=True):
	height, width, _ = image.shape
	x = int(x_percent * width)
	y = int(y_percent * height)
	radius = int(radius_percent * width)
	if fill:
		cv2.circle(image, (x, y), radius, color, -1)
	else:
		cv2.circle(image, (x, y), radius, color, 2)
	return image


def draw_oval(image, x_percent, y_percent, w_percent, h_percent, angle, startAngle, endAngle, color, fill=True):
	height, width, _ = image.shape
	x = int(x_percent * width)
	y = int(y_percent * height)
	w = int(w_percent * width)
	h = int(h_percent * height)
	if fill:
		cv2.ellipse(image, (x, y), (w, h), angle, startAngle, endAngle, color, -1)
	else:
		cv2.ellipse(image, (x, y), (w, h), angle, startAngle, endAngle, color, 2)
	return image
