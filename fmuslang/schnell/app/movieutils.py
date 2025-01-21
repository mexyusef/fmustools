# pip install moviepy
# pip install scikit-image
# https://pypi.org/project/moviepy/
# https://zulko.github.io/moviepy/


# moviepy/config_defaults.py
# IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\magick.exe"
# IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\convert.exe"

# https://zulko.github.io/moviepy/getting_started/compositing.html
# from moviepy.editor import VideoFileClip, ImageClip
# filename = "judulfilm.mp4"
# clip = VideoFileClip(filename)
# fps= 1.0 # take one frame per second
# nframes = clip.duration*fps # total number of frames used
# total_image = sum(clip.iter_frames(fps,dtype=float,logger='bar'))
# average_image = ImageClip(total_image/ nframes)
# average_image.save_frame("average_test.png")


from moviepy.editor import *
import numpy as np

# from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient
from skimage import transform as tf
# 1
# select the subclip between t=50s and t=60s, 
# add a title at the center of the screen, 
# and write the result to a new file

# video = VideoFileClip("myHolidays.mp4").subclip(50,60)

# # Make the text. Many more options are available.
# txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...

# 2
# load a video of my last holidays,
# lower the volume, add a title in the center of the video for the first ten seconds,
# and write the result in a file:

# # Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
# clip = VideoFileClip("myHolidays.mp4").subclip(50,60)

# # Reduce the audio volume (volume x 0.8)
# clip = clip.volumex(0.8)

# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')

# # Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(10)

# # Overlay the text clip on the first video clip
# video = CompositeVideoClip([clip, txt_clip])

# # Write the result to a file (many options available !)
# video.write_videofile("myHolidays_edited.webm")