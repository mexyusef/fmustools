import os
import tempfile
import urllib.request
from PIL import Image
import cv2
import imageio

from .dirutils import suffix_filename
from .grabutils import grabber
from .utils import trycopy
from .notifutils import notifpy

# # URL of the GIF to download
# gif_url = "https://example.com/example.gif"
# # Create a temporary file to save the GIF in
# with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as temp_file:
#     # Download the GIF from the URL
#     with urllib.request.urlopen(gif_url) as url:
#         gif_data = url.read()
#     # Write the GIF data to the temporary file
#     temp_file.write(gif_data)
# # Open the GIF file with Pillow
# with Image.open(temp_file.name) as im:
#     # Determine the new width and height
#     new_width = im.width * 4
#     new_height = int(im.height * (new_width / im.width))
#     # Resize the image
#     im_resized = im.resize((new_width, new_height))
#     # Save the resized image
#     im_resized.save('resized.gif', format='GIF')
# # Remove the temporary file when you're done with it
# os.unlink(temp_file.name)


def resize_gif(gif_path, width_factor=1.0, height_factor=0):

	new_gif_path = suffix_filename(gif_path, f'_resized_{width_factor}x')

	with Image.open(gif_path) as im:

		# Determine the new width and height
		new_width = int(im.width * width_factor)
		new_height = int(im.height * (new_width / im.width))

		# Resize the image
		im_resized = im.resize((new_width, new_height))

		# Save the resized image
		im_resized.save(new_gif_path, format='GIF')

	return new_gif_path


def resize_gif2(gif_path, width_factor=1.0, height_factor=0):
	new_gif_path = suffix_filename(gif_path, f'_resized_{width_factor}x')
	print(f"resize_gif2: {gif_path} => {new_gif_path}")
	# Load the GIF animation
	animation = cv2.VideoCapture(gif_path)

	# Get the width and height of the first frame
	success, frame = animation.read()
	height, width, _ = frame.shape

	# Define the new width for the animation
	new_width = int(width * width_factor)

	# Calculate the new height to maintain aspect ratio
	new_height = int((new_width / width) * height)

	# Create a list to store the resized frames
	resized_frames = []

	# Loop through all frames of the animation
	while True:
		# Read the next frame
		success, frame = animation.read()
		
		# Break the loop if no more frames are available
		if not success:
			break
		# Convert the color channels from BGR to RGB
		frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		# Resize the frame
		resized_frame = cv2.resize(frame_rgb, (new_width, new_height))
		
		# Append the resized frame to the list
		resized_frames.append(resized_frame)

	# Release the resources
	animation.release()

	# Save the resized frames as a GIF file using imageio
	imageio.mimsave(new_gif_path, resized_frames, duration=0.1)
	return new_gif_path



from .videocapture import video_capture_grab, video_capture
# video_capture(
# 	outputfile='c:/tmp/mycapture.mp4', timeout=10, fps=30.0, text=None, bbox=None, x=0, y=0, w=screen_size[0], h=screen_size[1],
# 	warna='white', lineType = 2, font = cv2.FONT_HERSHEY_SIMPLEX,
# 	thickness=4,
# )
# video_capture_grab(outputfile='c:/tmp/mycapture.mp4', timeout=10, fps=30.0, text=None)
from .videoutils import merge_videos_to_gif


def screen_capture_to_gif(outputfile, timeout=10, fps=15.0, fullscreen=False, show_notif=True):
	"""
	outputfile adlh gif
	"""

	# ini akan sama dg kembalian video_capture(), tapi dibutuhkan utk input ke video_capture
	output_mp4_file = suffix_filename(outputfile, '_screenrecord', replace_ext='.mp4')

	def capture_setelah_bbox(bbox):
		assert bbox, "screen_capture_to_gif => bbox not set"
		print('screen_capture_to_gif callback...')
		# video_capture(outputfile=outputfile, timeout=timeout, fps=fps, text=text, bbox=bbox)
		output_video = video_capture(outputfile=output_mp4_file, timeout=timeout, fps=fps, bbox=bbox, show_notif=False)
		merge_videos_to_gif([output_video], output_file=outputfile, fps=fps, show_notif=False)

	if fullscreen:
		output_video = video_capture(outputfile=output_mp4_file, timeout=timeout, fps=fps, show_notif=False)
		merge_videos_to_gif([output_video], output_file=outputfile, fps=fps, show_notif=False)
	else:
		grabber(capture_setelah_bbox)

	if show_notif:
		notifpy('/gif)screen_capture_to_gif', f'lihat output di {outputfile}')
		trycopy(outputfile)
