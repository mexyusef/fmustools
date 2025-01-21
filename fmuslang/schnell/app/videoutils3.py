import cv2
import os

from .dirutils import absolutify, isabsolute, isdir, joiner, disini, suffix_filename, dirname
from .notifutils import notifpy
from .utils import trycopy


def video_to_images(video_input, start_frame=1, end_frame=-1, output_dir=None, print_frameno=False):
	basedir = dirname(video_input)
	# Open the video file
	cap = cv2.VideoCapture(video_input)

	# Get the total number of frames in the video
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# Set the end frame to the last frame if not specified
	if end_frame == -1:
		end_frame = total_frames

	# Make sure the start frame and end frame are within the total frame count
	start_frame = max(1, start_frame)
	end_frame = min(total_frames, end_frame)
	# print('video_to_clip, basedir:', basedir)
	if not output_dir:
		# Create a directory to save the images
		video_name = os.path.splitext(os.path.basename(video_input))[0]
		output_dir = f"{video_name}_images"
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)
	elif not isabsolute(output_dir) and not isdir(os.path.join(basedir, output_dir)): # jk kasih relative dir dan belum ada
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)



	# Add the time string as a label to the frame
	font = cv2.FONT_HERSHEY_SIMPLEX
	font_scale = 4
	color = (255, 255, 255)
	thickness = 4
	org = (50, 100) # Position of the text label


	# Read and save the frames as PNG images
	for i in range(start_frame, end_frame+1):
		cap.set(cv2.CAP_PROP_POS_FRAMES, i-1)
		ret, frame = cap.read()
		if ret:
			if print_frameno:
				# Add the frame number as text to the image
				# This text is positioned at (50,50) coordinate and it has green color (0,255,0), a font size of 1, and thickness of 2.
				frame = cv2.putText(frame, f"{i}", org, font, font_scale, color, thickness, cv2.LINE_AA)
			# Save the image as a PNG file
			cv2.imwrite(f"{output_dir}/{i:04d}.png", frame)

	# Release the video capture object
	cap.release()
	notifpy('/vidutils)video_to_images', f'lihat images di {output_dir}')
	trycopy(output_dir)


def video_to_clip(video_input, start_frame=1, end_frame=-1, output_dir=None):
	basedir = dirname(video_input)
	# Open the video file
	cap = cv2.VideoCapture(video_input)

	# Get the frame rate and resolution of the video
	fps = cap.get(cv2.CAP_PROP_FPS)
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

	# Get the total number of frames in the video
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# Set the end frame to the last frame if not specified
	if end_frame == -1:
		end_frame = total_frames

	# Make sure the start frame and end frame are within the total frame count
	start_frame = max(1, start_frame)
	end_frame = min(total_frames, end_frame)

	# Calculate the duration of the clip in seconds
	duration = (end_frame - start_frame + 1) / fps
	# print('video_to_clip, basedir:', basedir)
	if not output_dir:
		# Create a directory to save the clip
		video_name = os.path.splitext(os.path.basename(video_input))[0]
		output_dir = f"{video_name}_clips"
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)
	elif not isabsolute(output_dir) and not isdir(os.path.join(basedir, output_dir)): # jk kasih relative dir dan belum ada
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)

	# Set up the video writer
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	clip_name = f"{output_dir}/{start_frame:04d}-{end_frame:04d}.mp4"
	out = cv2.VideoWriter(clip_name, fourcc, fps, (width, height))

	# Read and write the frames to the clip
	for i in range(start_frame, end_frame+1):
		cap.set(cv2.CAP_PROP_POS_FRAMES, i-1)
		ret, frame = cap.read()
		if ret:
			out.write(frame)

	# Release the video capture and writer objects
	cap.release()
	out.release()
	notifpy('/vidutils)video_to_clip', f'lihat vidclip di {clip_name}')
	trycopy(clip_name)
	return clip_name


def video_to_images_seconds(video_input, start_second=0, end_second=-1, output_dir=None, print_frameno=False):
	"""
	video_to_images("path/to/video.mp4", start_second=10, end_second=30)
	"""
	basedir = dirname(video_input)
	# Open the video file
	cap = cv2.VideoCapture(video_input)

	# Get the frame rate and total number of frames in the video
	fps = cap.get(cv2.CAP_PROP_FPS)
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# Set the end second to the end of the video if not specified
	if end_second == -1:
		end_second = total_frames / fps

	# Make sure the start second and end second are within the video duration
	start_second = max(0, start_second)
	end_second = min(total_frames / fps, end_second)

	# Calculate the start and end frames based on the frame rate
	start_frame = int(start_second * fps)
	end_frame = int(end_second * fps)


	# Add the time string as a label to the frame
	font = cv2.FONT_HERSHEY_SIMPLEX
	font_scale = 4
	color = (255, 255, 255)
	thickness = 4
	org = (50, 100) # Position of the text label


	# Create a directory to save the images
	# video_name = os.path.splitext(os.path.basename(video_input))[0]
	# output_dir = f"{video_name}_frames"
	# os.makedirs(output_dir, exist_ok=True)
	if not output_dir:
		# Create a directory to save the clip
		video_name = os.path.splitext(os.path.basename(video_input))[0]
		output_dir = f"{video_name}_frames"
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)
	elif not isabsolute(output_dir) and not isdir(os.path.join(basedir, output_dir)): # jk kasih relative dir dan belum ada
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)

	# Read and save the frames as PNG images
	for i in range(start_frame, end_frame+1):
		cap.set(cv2.CAP_PROP_POS_FRAMES, i)
		ret, frame = cap.read()
		if ret:

			current_second = i / fps
			hours, rem = divmod(current_second, 3600)
			minutes, seconds = divmod(rem, 60)
			millisec = int((current_second - int(current_second)) * 1000)
			time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{millisec:03d}"

			if print_frameno:
				# Add the frame number as text to the image
				# This text is positioned at (50,50) coordinate and it has green color (0,255,0), a font size of 1, and thickness of 2.
				frame = cv2.putText(frame, f"{i} - {time_str}", org, font, font_scale, color, thickness, cv2.LINE_AA)

			# Save the current frame with the time string as its name
			frame_name = f"{output_dir}/{i:06d}_{time_str.replace(':','_')}.png"
			cv2.imwrite(frame_name, frame)

			# frame_name = f"{output_dir}/{i:06d}.png"
			# cv2.imwrite(frame_name, frame)

	# Release the video capture object
	cap.release()
	notifpy('/vidutils)video_to_images_seconds', f'lihat images di {output_dir}')
	trycopy(output_dir)
	return output_dir


def video_to_clip_seconds(video_input, start_second=0, end_second=-1, output_dir=None):
	basedir = dirname(video_input)
	"""
	video_to_clip("path/to/video.mp4", start_second=10, end_second=30)
	"""
	# Open the video file
	cap = cv2.VideoCapture(video_input)

	# Get the frame rate and total number of frames in the video
	fps = cap.get(cv2.CAP_PROP_FPS)
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# Set the end second to the end of the video if not specified
	if end_second == -1:
		end_second = total_frames / fps

	# Make sure the start second and end second are within the video duration
	start_second = max(0, start_second)
	end_second = min(total_frames / fps, end_second)

	# Calculate the start and end frames based on the frame rate
	start_frame = int(start_second * fps)
	end_frame = int(end_second * fps)

	# Set the output video file name
	if not output_dir:
		# Create a directory to save the clip
		video_name = os.path.splitext(os.path.basename(video_input))[0]
		output_dir = f"{video_name}_clips"
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)
	elif not isabsolute(output_dir) and not isdir(os.path.join(basedir, output_dir)): # jk kasih relative dir dan belum ada
		output_dir = os.path.join(basedir, output_dir)
		os.makedirs(output_dir, exist_ok=True)

	video_name = f"{start_second:.2f}s_{end_second:.2f}s"
	# output_path = f"{video_name}_clip.mp4"
	output_path = f"{output_dir}/{video_name}_clip.mp4"

	# Create the video writer object using the same parameters as the input video
	# fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

	# Read and write the frames to the output video
	for i in range(start_frame, end_frame+1):
		cap.set(cv2.CAP_PROP_POS_FRAMES, i)
		ret, frame = cap.read()
		if ret:
			out.write(frame)

	# Release the video capture and writer objects
	cap.release()
	out.release()
	notifpy('/vidutils)video_to_clip_seconds', f'lihat images di {output_path}')
	trycopy(output_path)
	return output_path


def video_to_clip2_seconds(video_input, start_second=0, end_second=-1):
	# Open the video file
	cap = cv2.VideoCapture(video_input)

	# Get the frame rate and total number of frames in the video
	fps = cap.get(cv2.CAP_PROP_FPS)
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# Set the end second to the end of the video if not specified
	if end_second == -1:
		end_second = total_frames / fps

	# Make sure the start second and end second are within the video duration
	start_second = max(0, start_second)
	end_second = min(total_frames / fps, end_second)

	# Calculate the start and end frames based on the start and end seconds
	start_frame = int(start_second * 1000)
	end_frame = int(end_second * 1000)

	# Set the output video file name
	video_name = f"{start_second:.2f}s_{end_second:.2f}s_{video_input}"
	output_path = f"{video_name}_clip.mp4"

	# Create the video writer object using the same parameters as the input video
	# fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

	# Set the position of the video capture object to the start frame
	cap.set(cv2.CAP_PROP_POS_MSEC, start_frame)

	# Read and write the frames to the output video
	while cap.get(cv2.CAP_PROP_POS_MSEC) <= end_frame:
		ret, frame = cap.read()
		if ret:
			out.write(frame)

	# Release the video capture and writer objects
	cap.release()
	out.release()
	notifpy('/vidutils)video_to_clip2_seconds', f'lihat images di {output_path}')
	trycopy(output_path)
	return output_path
