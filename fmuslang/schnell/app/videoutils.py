import time
import cv2
import numpy as np
from typing import List
import imageio

from .dirutils import absolutify, isabsolute, joiner, disini, suffix_filename
from .utils import trycopy
from .notifutils import notifpy

# https://github.com/Andrey1994/screen_recorder_sdk
# https://screen-recorder-sdk.readthedocs.io/en/latest/Examples.html#python-basic-demo
# pip install screen-recorder-sdk

# https://github.com/deepch/RTSPtoWeb
# youtube-dl, ffmpeg


def merge_videos_to_gif(videos: List[str], output_file: str, fps=30.0, show_notif=True):
  # Initialize the video files
  input_videos = [cv2.VideoCapture(v) for v in videos]

  # # Get the video dimensions and FPS
  # width = int(input_videos[0].get(cv2.CAP_PROP_FRAME_WIDTH))
  # height = int(input_videos[0].get(cv2.CAP_PROP_FRAME_HEIGHT))

  # Initialize the list of frames
  frames = []

  # Read all frames from each video and append to the list
  for vid in input_videos:
    while True:
      ret, frame = vid.read()
      if not ret:
        break
      # Convert the frame from BGR to RGB
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      frames.append(frame)

  # Release the resources
  for vid in input_videos:
    vid.release()

  # Write the frames to a GIF animation
  imageio.mimsave(output_file, frames, fps=fps)
  if show_notif:
    notifpy('/vidutils)merge_videos_to_gif', f'{videos} saved to {output_file}')
    trycopy(output_file)


def mp4_to_gif(video_input, gif_output, lebar=400):
  from moviepy.editor import VideoFileClip

  clip = VideoFileClip(video_input)
  # clip = clip.resize(width=lebar)
  clip.write_gif(gif_output)
  print(f"mp4_to_gif: {video_input} => {gif_output}.")


# def convert_mp4_to_gif(videos, gif_output):
#   from moviepy.editor import VideoFileClip

#   # clip = VideoFileClip(video_input)
#   # # clip = clip.resize(width=lebar)
#   # clip.write_gif(gif_output)
#   # print(f"mp4_to_gif: {video_input} => {gif_output}.")


def reverse_mp4(video_input, video_output=None, fps=24.0):
  if not video_output:
    video_output = suffix_filename(video_input, '_reversed')
  cap = cv2.VideoCapture(video_input)

  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(video_output, fourcc, fps,
                        (int(cap.get(3)), int(cap.get(4))))

  cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT)-1)

  while cap.isOpened():
    ret, frame = cap.read()
    # if ret:
    # 	out.write(frame)
    # 	# cv2.imshow('Reversed Video', frame)
    # 	# if cv2.waitKey(25) & 0xFF == ord('q'):
    # 	#   break
    # 	cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES)-2)
    # else:
    # 	break
    if ret:
      out.write(frame)
      # cv2.imshow('Reversed Video', frame)
      # if cv2.waitKey(25) & 0xFF == ord('q'):
      # 	break
      cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES)-2)
      if cap.get(cv2.CAP_PROP_POS_FRAMES) <= 0:
        break
    else:
      break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
  notifpy('/vidutils)reverse_mp4', f'{video_input} saved to {video_output}')
  trycopy(video_output)


def merge_videos(videos: List[str], fps=30.0, video_output=None):
  if not videos:
    print('[videoutils#merge_videos] no videos', videos)
    return
  video1 = videos[0]
  if not video_output:
    video_output = suffix_filename(video1, '_merged_video')
  # Initialize the video files
  input_videos = [cv2.VideoCapture(v) for v in videos]

  # Get the video dimensions and FPS
  width = int(input_videos[0].get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(input_videos[0].get(cv2.CAP_PROP_FRAME_HEIGHT))
  # fps = 30.0

  # Create a VideoWriter object to write the output video
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(video_output, fourcc, fps,
                        (width * len(videos), height))

  # Read the frames from each video and write to the output video
  while True:
    frames = []
    for vid in input_videos:
      ret, frame = vid.read()
      if not ret:
        break
      frames.append(frame)
    if not frames:
      break
    # Concatenate the frames horizontally
    frame = cv2.hconcat(frames)
    out.write(frame)

  # Release the resources
  for vid in input_videos:
    vid.release()
  out.release()
  cv2.destroyAllWindows()
  notifpy('/vidutils)merge_videos', f'{videos} saved to {video_output}')
  trycopy(video_output)
# def merge_videos(videos: List[str], fps=30.0, video_output=None):
# 	if not videos:
# 		print('[videoutils#merge_videos] no videos', videos)
# 		return
# 	video1 = videos[0]
# 	if not video_output:
# 		video_output = suffix_filename(video1, '_merged_video')
# 	# Get the video dimensions and FPS
# 	width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
# 	height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 	# Create a VideoWriter object to write the output video
# 	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# 	out = cv2.VideoWriter(video_output, fourcc, fps, (width, height))

# 	# Read the frames from each video and write to the output video
# 	while True:
# 		ret1, frame1 = video1.read()
# 		ret2, frame2 = video2.read()
# 		ret3, frame3 = video3.read()
# 		if not ret1 or not ret2 or not ret3:
# 				break
# 		# Concatenate the frames horizontally
# 		frame = cv2.hconcat([frame1, frame2, frame3])
# 		out.write(frame)

# 	# Release the resources
# 	# video1.release()
# 	# video2.release()
# 	# video3.release()
# 	for v in videos:
# 		v.release()
# 	out.release()
# 	cv2.destroyAllWindows()


def capture_screen(filepath='snapshot.png', coba=5, cwd=True):
  from screen_recorder_sdk import screen_recorder
  # filepath = absolutify(filepath)

  # if not isabsolute(filepath):
  #   from .envvalues import datadir
  #   filepath = joiner(datadir, filepath)

  if cwd:
    filepath = joiner(disini(), filepath)
  else:
    filepath = absolutify(filepath)

  screen_recorder.enable_dev_log()
  params = screen_recorder.RecorderParams()
  screen_recorder.init_resources(params)

  #  screen_recorder_sdk.screen_recorder.get_screenshot(max_attempts=1)
  screen_recorder.get_screenshot(coba).save(filepath)
  screen_recorder.stop_video_recording()

  screen_recorder.free_resources()
  print('recording result:', filepath)


def record_screen(filepath='recording.mp4', long_seconds=60, bit_rate=2, frame_rate=30, hardware=True, cwd=True):
  from screen_recorder_sdk import screen_recorder
  if cwd:
    filepath = joiner(disini(), filepath)
  else:
    filepath = absolutify(filepath)
  screen_recorder.enable_dev_log()
  params = screen_recorder.RecorderParams()
  # params.pid = 0 # use it to set process Id to capture
  # params.desktop_num = 0 # use it to set desktop num, counting from 0
  screen_recorder.init_resources(params)

  # screen_recorder_sdk.
  # screen_recorder.
  # start_video_recording(filename, frame_rate=30, bit_rate=8000000, use_hw_transfowrms=True)
  bit_rate = bit_rate * 1000000
  screen_recorder.start_video_recording(
      filepath, frame_rate, bit_rate, hardware)
  time.sleep(long_seconds)
  screen_recorder.stop_video_recording()

  screen_recorder.free_resources()
  print('recording result:', filepath, 'long:',
        long_seconds, 'bitrate:', bit_rate)


if __name__ == "__main__":
  record_screen()
