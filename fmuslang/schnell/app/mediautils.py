import imageio, os, random, requests, subprocess, sys
import cv2
import vlc
from io import BytesIO as BIO
from io import StringIO as SIO
from PIL import Image as IMG
from base64 import b64encode as encode
from base64 import b64decode as decode
from PIL import (
	Image,
	ImageColor,
	ImageDraw,
	ImageFilter,
	ImageFont,
	ImageSequence
)

try:
	from PIL import (
		ImageTk
	)
except ImportError as ie:
	pass

if sys.platform != 'linux':
	from PIL import ImageGrab


import urllib.request
import tempfile

from pilkit.processors import ProcessorPipeline, ResizeToFit, SmartResize
from constants import (
	DEFAULT_OUTPUTDIR,
	sizes,
	mapwarna,
	default_font_scale,
	thickness
)
from .appconfig import programming_data
from .dirutils import joiner, normy, bongkar, suffix_filename, absolutify
from .fileutils import is_binary
from .gifutils import resize_gif, resize_gif2
from .utils import trycopy, platform
# from .envvalues import datadir
from .regexutils import ukuranhuruf_posy

_fonts = ["arial", "impact.ttf"]
_rgb_colors = {
	'black': (0, 0, 0),
	'white': (255, 255, 255),
}

# if platform() not in ['termux']:
# 	import tkinter as tk


font = cv2.FONT_HERSHEY_SIMPLEX

def screen_capture(filename = 'screenshot.png'):
	from .screencapture import ScreenCapture
	ScreenCapture(filename).mainloop()


class ImageHandler:


	last_pil_image = None


	def __init__(self):
		pass


	def open_image(self, filepath, convert=False):
		if convert:
			return Image.open(filepath).convert("RGBA")
		return Image.open(filepath)


	def get_image(self, urlpath):
		return requests.get(urlpath).content


	def open_image_bytestring(self, bytedata):
		databytes = BIO(bytedata)
		return Image.open(databytes)


	def open_image_url(self, urlpath):
		databytes = BIO(self.get_image(urlpath))
		return Image.open(databytes)


	def open_show_image(self, urlpath=None, url_random=1, save_file=None):
		"""
		ULIBPY_RANDOM_IMAGE=https://picsum.photos/640/480
		ULIBPY_RANDOM_IMAGE2=https://source.unsplash.com/random
		"""
		if urlpath is None:
			if url_random == 1:
				urlpath = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_RANDOM_IMAGE"] # os.environ.get('ULIBPY_RANDOM_IMAGE')
			else:
				urlpath = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_RANDOM_IMAGE2"] # os.environ.get('ULIBPY_RANDOM_IMAGE2')
		
		gambar = self.open_image_url(urlpath)
		ImageHandler.last_pil_image = gambar
		if save_file:
			gambar.save(save_file, 'PNG')
		else:
			gambar.show()


	def open_draw_show_image(self, text, urlpath=None, url_random=1, ukuran = 70, save_file=None, pemisah='||', warna = (10,10,255), w=1920,h=1080):
		"""
		bisa tulis atas bawah:
		atas
		atas||bawah
		atas||bawah||tengah
		"""
		if urlpath is None:
			if url_random == 1:
				urlpath = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_RANDOM_IMAGE"] # os.environ.get('ULIBPY_RANDOM_IMAGE')
			else:
				urlpath = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_RANDOM_IMAGE2"] # os.environ.get('ULIBPY_RANDOM_IMAGE2')

		gambar = self.open_image_url(urlpath)
		draw = ImageDraw.Draw(gambar)
		# posisi = (0,0)

		# huruf = '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf'
		# huruf = '/usr/share/sphinx_rtd_theme/static/fonts/RobotoSlab-Regular.ttf'
		# huruf = '/usr/share/vlc/skins2/fonts/FreeSans.ttf'
		huruf = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_MEME_FONT"]
		# ULIBPY_MEME_FONT => '/usr/share/vlc/skins2/fonts/FreeSans.ttf'
		huruf_tulisan = font=ImageFont.truetype(huruf, ukuran)
		atas = text
		bawah = None
		tengah = None
		if pemisah in text:
			if text.count(pemisah) == 1:
				atas, bawah = [item.strip() for item in text.split(pemisah)]

		tulisan_w, tulisan_h = draw.textsize(atas, huruf_tulisan)
		# draw.text(posisi, text, warna, font=ImageFont("Roboto-Regular.ttf", 24))
		# https://stackoverflow.com/questions/37924130/pil-add-a-text-at-the-bottom-middle-of-image
		draw.text(((w-tulisan_w)//2, 0), atas, warna, huruf_tulisan)
		if bawah:
			tulisan_w, tulisan_h = draw.textsize(bawah, huruf_tulisan)
			draw.text(((w-tulisan_w)//2, h-tulisan_h), bawah, warna, huruf_tulisan)

		ImageHandler.last_pil_image = gambar
		if save_file:
			gambar.save(save_file, 'PNG')
		else:
			gambar.show()


	def ask_save(self, basedir, filename):
		if ImageHandler.last_pil_image:
			newfile = input(f'Filename tanpa .png utk simpan [{filename}.png]? ')
			if newfile.strip():
				filename = newfile.strip() 
				
			filename += '.png'
			filepath = os.path.join(basedir, filename)
			ImageHandler.last_pil_image.save(filepath, 'PNG', optimize=True)
			print('Saved to', filepath)


	def open_image_blob(self, imgblob):
		"""dari wand-image make_blob"""
		# return Image.open(io.BytesIO(imgblob))
		return Image.open(BIO(imgblob))


	def sharpen_image(self, pil_image):
		pil_image.filter(ImageFilter.SHARPEN)


	def image_size(self, filepath):
		return self.open_image(filepath).size


	def new_image(self, w, h, background='black'):
		return Image.new('RGBA', (w,h), background)


	def get_frames_from_gif(self, gif_pil_img):
		return [frame.copy() for frame in ImageSequence.Iterator(gif_pil_img)]


	def get_duration_from_gif(self, gif_pil_img):
		return gif_pil_img.info['duration']


	def tk_image_from_pil_image(self, pil_image):
		'''https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python'''
		return ImageTk.PhotoImage(pil_image)


	def show(self, pil_image):
		pil_image.show() # https://github.com/amueller/word_cloud/blob/master/examples/simple.py


	def overlay(self, bottom_img, top_img, x=0, y=0):
		bottom_img.paste(top_img, (x, y))


	def image_drawer(self, pil_image):
		return ImageDraw.Draw(pil_image)


	def draw_rect(self, img_drawer, x=0,y=0, w=100,h=100, background='black'):
		img_drawer.rectangle(((x,y), (w,h)), fill=background)


	def get_font(self, font_name="arial", font_size=None):
		if font_size:
			return ImageFont.truetype(font_name, font_size)
		else:
			return ImageFont.truetype(font_name)


	def transpose_font(self, font, orientation):
		return ImageFont.TransposedFont(font, orientation=orientation)


	def draw_text(self, img_drawer, text, x=0, y=0, color=_rgb_colors['white'], text_font="arial"):
		img_drawer.text((x,y), text, color, font=self.get_font(text_font))


	def draw_outline_text(self, img_drawer, text, x=0, y=0, color=_rgb_colors['white'], outcolor=_rgb_colors['black'], font=None):
		"""
		cara bikin outline
		https://github.com/danieldiekmeier/memegenerator/blob/master/memegenerator.py
		"""
		if not font:
			font = self.get_font(font_size=50)
			
		img_drawer.text((x-2,y-2), text, outcolor, font=font)
		img_drawer.text((x+2,y-2), text, outcolor, font=font)
		img_drawer.text((x+2,y+2), text, outcolor, font=font)
		img_drawer.text((x-2,y+2), text, outcolor, font=font)

		img_drawer.text((x,y), text, color, font=font)


	def drawer_text_size(self, drawer, text, font):
		return drawer.textsize(text, font)


	def draw_center_outline(self, pil_image, text, x, y, font):
		drawer = self.image_drawer(pil_image)
		w, _ = self.drawer_text_size(drawer, text, font)
		self.draw_outline_text(drawer, text, x=x, y=y, font=font)
		# save_imagename(pil_image, 'delete.png')

	def meme_clipboard_top(self, text):
		im = self.save_clipboard_to_file()
		drawer = self.image_drawer(im)
		self.draw_outline_text(drawer, text)
		# im.show?
		self.save_imagename(im, 'delete.png')


	def meme_clipboard_topcenter(self, text, save_filename='delete.png'):
		im = self.save_clipboard_to_file()
		font, x, y = self.get_top_or_bottom_xy(im, text)
		# font = get_font("arial", 50)
		self.draw_center_outline(im, text, x, y, font)
		# print 'font [%d] x %d y %d im w %d im h %d' % (text_size_from_font(text, font)[0], x, y, im.width, im.height)
		# im.show?
		self.save_imagename(im, save_filename)


	def meme_clipboard_top_bottom(self, top_text, bottom_text, save_filename='delete.png'):
		im = self.save_clipboard_to_file()
		# for text in [top_text, bottom_text]:
		font, x, y = self.get_top_or_bottom_xy(im, top_text)
		self.draw_center_outline(im, top_text, x, y, font)

		font, x, y = self.get_top_or_bottom_xy(im, bottom_text, bottom=True)
		self.draw_center_outline(im, bottom_text, x, y, font)

		self.save_imagename(im, save_filename)


	def text_size(self, text, text_font="arial"):
		"""
		w, h
		w+10, h+10 utk margin 10px
		"""
		return ImageFont.truetype(text_font).getsize(text)


	def text_size_from_font(self, text, font):
		"""
		w, h
		w+10, h+10 utk margin 10px
		"""
		return font.getsize(text)


	def get_top_or_bottom_xy(self, pil_image, text, bottom=False):
		seperlima = int ( pil_image.height / 5 )
		font = self.get_font(font_size=seperlima)
		ukur_w, ukur_h = font.getsize(text)
		while ukur_w > pil_image.width:
			seperlima -= 1
			font = self.get_font(font_size=seperlima)
			ukur_w, ukur_h = font.getsize(text)
		# skrg ukur_w sudah siap...
		x = (pil_image.width / 2) - (ukur_w / 2)
		y = 0 if not bottom else (pil_image.height - ukur_h)
		return (font, x, y)


	def grab_bbox(self, bbox):
		"""
		bbox = (x, y, w, h)
		"""
		if not bbox:
			return ImageGrab.grab()
		return ImageGrab.grab(bbox)


	def grab_self(self):
		return ImageGrab.grab()


	def grab_clipboard(self):
		return ImageGrab.grabclipboard()


	def save_clipboard_to_file(self, location='/tmp', filename='delete', ext='png'):
		pil_image = self.grab_clipboard()
		filename = '%s.%s' % (filename, ext)
		filepath = os.path.join(location, filename)
		pil_image.save(filepath, ext.upper())
		return pil_image


	def grab_save(self, filepath, bbox=None, fileformat='PNG'):
		img = self.grab_bbox(bbox)
		self.save_image(img, filepath, fileformat)
		return img


	def crop_image(self, pil_image, bbox):
		"""
		bbox = (x1, y1, x2, y2)
		"""
		return pil_image.crop(bbox)


	def save_image(self, pil_image, filepath, fileformat='PNG'): # JPEG
		pil_image.save(filepath, fileformat)


	def save_imagename(self, pil_image, filename, fileformat='PNG'): # JPEG
		self.save_image(pil_image, os.path.join('/tmp', filename), fileformat)


	def convert_image(self, pil_image, image_format='RGB'): # grayscale = 'L'
		return pil_image.convert(image_format)


	def resize_image(self, pil_image, w, h):
			"""
			https://www.daniweb.com/programming/software-development/code/216637/resize-an-image-python
			Image.NEAREST, BILINEAR, BICUBIC, ANTIALIAS
			"""
			return pil_image.resize([w, h], Image.ANTIALIAS)


	def meme_simple(self, code):
		self.meme_clipboard_topcenter(code)


	def meme_standard(self, code):
		if code.count('/') == 1:
			atas, bawah = code.split('/')
			self.meme_clipboard_top_bottom(atas.strip(), bawah.strip(), atas[:10]+'.png')


# def word_cloud(code):
# 	'''
# 	sementara code diabaikan, bisa tentukan: jumlah words dan joiner
# 	'''
# 	from datagenerator import join_generated_words
# 	show_wordcloud(join_generated_words()) # default 10 words, joiner=space

# def show_wordcloud(text):
# 	from wordcloud import wordcloud_to_pil_image
# 	show(wordcloud_to_pil_image(text))

# def clipboard_save(filename):
#   def decorator(func):
#     def wrapper(*args):
#       im = save_clipboard_to_file()
#       func(im, *args) # modifikasi argumen dari fungsi
#       save_imagename(im, filename)
#       return im
#     return wrapper
#   return decorator

# def show_decorator(func):
#   def wrapper(im, *args):
#     func(*args)
#     im.show()
#     return im
#   return wrapper

"""
http://blog.lipsumarium.com/caption-memes-in-python/
ada utk wrap text
tp itu nanti saja...

https://www.makeartwithpython.com/blog/deal-with-it-generator-face-recognition/

https://gist.github.com/omz/4034426

https://github.com/danieldiekmeier/memegenerator/blob/master/memegenerator.py
utk text size dan position yg pas berdasarkan image.

seperlima = int ( pil_image.height / 5 )
font = get_font(font_size=seperlima)
ukur_w, _ = font.getsize(text)
while ukur_w > pil_image.width:
	seperlima -= 1
	font = get_font(font_size=seperlima)
	ukur_w, _ = font.getsize(text)
# skrg ukur_w sudah siap...
pos_x = (pil_image.width / 2) - (ukur_w / 2)
pos_y = 0
"""


def buka_file(filepath):
	"""
	kita hasilkan file biner terdekod b64
	misal punya file gambar
	kita pengen konversi data bytes nya ke b64 encoded
	"""
	content = None
	with open(filepath, 'rb') as fd:
		content = fd.read()	
	return encode(content)


def get_stringified_image_asb64(filepath):
	if os.path.exists(filepath):
		with open(filepath, 'rb') as fd:
			content = fd.read()
			konversi = encode(content) # b'...
			stringified = konversi.decode('utf-8') # str
			return stringified
	return None


def stringified_image_asb64(filepath):
	if os.path.exists(filepath):
		with open(filepath, 'rb') as fd:
			print(f'[mediautils:stringified_image_asb64] reading: {filepath}')
			content = fd.read()
			# b64encode content file gambar menjadi b'...
			konversi = encode(content) # b'...
			stringified = konversi.decode('utf-8') # str
			print(stringified)
			trycopy(stringified)
	else:
		print(f'[mediautils:stringified_image_asb64] file not found: {filepath}')


def encode_file_content(filepath):
	from .fileutils import file_content_binary
	content = file_content_binary(filepath)
	return encode(content).decode('utf-8') # skrg jd string


def entrify_encode_file_content(filepath):
	start = '--% ' + filepath
	end = '--#'
	return start + '\n' + encode_file_content(filepath) + '\n' + end + '\n'


def baca_file(filepath):
	"""baca str data dari file...dan konversi ke bentuk bytes (dari str)
	"""
	with open(filepath, 'r') as fd:
		content = fd.read()

	asbytes = str.encode(content)
	return asbytes


def lihat_gambar(filepath):
	gambar = Image.open(filepath)
	gambar.show()


def capture_gambar(filepath, delay=1):
	from .utils import platform
	filepath = normy(filepath)
	if platform() in ['linux']:
		ambiler = 'gnome-screenshot'
		opsi = f'-a -d {delay} -f {filepath}'
		os.system(f"{ambiler} {opsi}")
	else:
		# https://askubuntu.com/questions/221644/quicker-alternative-to-gnome-screenshot-no-animation-quick-no-frills
		# import -window root screenshot.png
		# scrot, shutter-project.org
		# imagemagick windows <- download
		screen_capture(filepath)


def get_gambar(alamat, delay=1, filepath=None):
	"""
	https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
	"""
	import urllib.request
	if not filepath:
		filename = 'download.jpg'
		if alamat.endswith('.jpg') or alamat.endswith('.png'):
			filename = alamat.split('/')[-1]
		basesimpan = '/tmp'
		filepath = os.path.join(basesimpan, filename)
	urllib.request.urlretrieve(alamat, filepath)


def capture_lihat_gambar(filepath, delay=1):
	"""
	digunakan:
	- img64 
	- img64 <filepath>
	"""
	# ambiler = 'gnome-screenshot'
	# opsi = f'-a -d {delay} -f {filepath}'
	# os.system(f"{ambiler} {opsi}")
	# gambar = Image.open(filepath)
	# gambar.show()
	capture_gambar(filepath, delay)
	lihat_gambar(filepath)


def get_lihat_gambar(url, delay=1, filepath=None):
	get_gambar(url, delay, filepath)
	lihat_gambar(filepath)


def capture_stringified_image_asb64(filepath, delay=1):
	capture_gambar(filepath, delay)
	stringified_image_asb64(filepath)


def capture_lihat_stringified_image_asb64(filepath, delay=1):
	capture_lihat_gambar(filepath, delay)
	stringified_image_asb64(filepath)


def get_lihat_stringified_image_asb64(alamat, delay=1):
	filepath = '/tmp/hapus.jpg'
	if alamat.endswith('.jpg') or alamat.endswith('.png'):
		pecah = alamat.split('/')
		filepath = '/'.join([os.path.dirname(filepath), pecah[-1]])
		print(f'saving file {filepath}...')
	get_lihat_gambar(alamat, delay, filepath)
	stringified_image_asb64(filepath)


def requests_get_lihat_stringified_image_asb64(alamat, delay=1):
	r = requests.get(alamat, stream=True)
	if r.status_code == 200:
		filepath = '/tmp/hapus.jpg'
		if alamat.endswith('.jpg') or alamat.endswith('.png'):
			pecah = alamat.split('/')
			filepath = '/'.join([os.path.dirname(filepath), pecah[-1]])
			print(f'saving file {filepath}...')
		with open(filepath, 'wb') as f:
			for chunk in r:
				f.write(chunk)
		stringified_image_asb64(filepath)


def baca_text(content):
	"""
	input:
		content str (misal dari clipboard atau hasil baca file)
	output:
		representasi bytes nya

	kembalian adlh data terdekod b64
	bisa show_decoded utk show
	bisa write_decoded utk tulis ke file
	"""
	asbytes = str.encode(content)
	return asbytes


def show_decoded(terdekod):
	data = decode(terdekod)
	gambar = IMG.open(BIO(data))
	gambar.show()


def write_decoded(terdekod, filepath):
	try:
		data = decode(terdekod)
		# binary mode doesn't take an encoding argument
		with open(filepath, 'wb') as fd:
			fd.write(data)
	except Exception as err:
		from schnell.app.printutils import indah4
		import traceback
		indah4(f'''[mediautils]
		gagal tulis atau baca decode = {filepath}
		pesan = {err}
		trace = {traceback.format_exc()}
		''', warna='red')
		input('press any key... ')


def baca_tulis_text(content, filepath):
	"""
	dari content data decoded, kita tulis ke file sbg data yg sudah dibuka
	misa jk image tersimpan sbg data terdecoded
	kita pengen tulis ke file gambar
	"""
	asbytes = baca_text(content)
	write_decoded(asbytes, filepath)


def generate_favicon_notworking(filepath, savebasedir='/tmp', savefilename='favicon.ico'):
	# from PIL import Image
	# filename = r'logo.png'
	img = IMG.open(filepath)
	savepath = os.path.join(savebasedir, savefilename)
	img.save(savepath)


def generate_favicon(filepath, savebasedir='/tmp', savefilename='favicon.ico'):
	# img = IMG.open(filepath)
	savepath = os.path.join(savebasedir, savefilename)
	# img.save(savepath)
	img = imageio.imread(filepath)
	imageio.imwrite(savepath, img)


def r(enum_):
	return random.choice(list(enum_))


def generate_avatar(filepath):
	import py_avataaars

	avatar = py_avataaars.PyAvataaar(
		accessories_type=r(py_avataaars.AccessoriesType),
		# clothe_color=r(py_avataaars.ClotheColor),
		clothe_graphic_type=r(py_avataaars.ClotheGraphicType),
		clothe_type=r(py_avataaars.ClotheType),
		eye_type=r(py_avataaars.EyesType),
		eyebrow_type=r(py_avataaars.EyebrowType),
		facial_hair_type=r(py_avataaars.FacialHairType),
		# facial_hair_color=r(py_avataaars.FacialHairColor),
		hair_color=r(py_avataaars.HairColor),
		# hat_color=r(py_avataaars.ClotheColor),
		mouth_type=r(py_avataaars.MouthType),
		nose_type=r(py_avataaars.NoseType),
		skin_color=r(py_avataaars.SkinColor),
		style=py_avataaars.AvatarStyle.CIRCLE,
		top_type=r(py_avataaars.TopType),
	)
	avatar.render_png_file(filepath)


def random_picsum(text=None):
	if text:
		ImageHandler().open_draw_show_image(text, save_file='picsum.png')
	else:
		ImageHandler().open_show_image(save_file='picsum.png')


def random_unsplash(text=None):
	if text:
		ImageHandler().open_draw_show_image(text, url_random=2, save_file='unsplash.png')
	else:
		ImageHandler().open_show_image(url_random=2, save_file='unsplash.png')

# https://stackoverflow.com/questions/44231209/resize-rectangular-image-to-square-keeping-ratio-and-fill-background-with-black/44231784
def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
	x, y = im.size
	size = max(min_size, x, y)
	new_im = Image.new('RGBA', (size, size), fill_color)
	new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
	return new_im

# https://stackoverflow.com/questions/45507/is-there-a-python-library-for-generating-ico-files
def make_favicon(imagefile, outputfolder='.', icofile='favicon.ico'):
	img = Image.open(imagefile)
	# icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
	# img.save(icofile, sizes=icon_sizes)
	# The Pillow docs say that by default it will generate sizes [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)] 
	# and any size bigger than the original size or 255 will be ignored.
	icopath = os.path.join(outputfolder, icofile)
	img.save(icopath)


def faviconGenerator(originalImage, outputDirectory):
	for size in sizes:
		im = Image.open(originalImage)
		processor = ProcessorPipeline([ResizeToFit(size[1][0], size[1][1])])
		result = processor.process(im)
		background = Image.new('RGBA', size[2], (255, 255, 255, 0))
		background.paste(
	  result, (int((size[2][0] - result.size[0]) / 2), int((size[2][1] - result.size[1]) / 2))
	)
		background.save(outputDirectory + "/" + size[0] + ".png")
		print("{}.png generated".format(size[0]))

# faviconGenerator(originalImage, directory)
# faviconGenerator(filepath, favfolder)


def screen_size():
	import tkinter as tk
	root = tk.Tk()
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	return (w,h)


def show_image(image_path):
	Image.open(image_path).show()


play_image = show_image


def play_video(video_path):
	p = vlc.MediaPlayer(video_path)
	p.play()
	input('Press any key to stop playback... ')
	p.stop()


show_video = play_video


def play_video_loop(video_path):
	# p = vlc.MediaPlayer(video_path)
	# def end_callback(event):
	#     p.stop()
	#     p.play()
	# event_manager = p.event_manager()
	# event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, end_callback)
	# p.play()
	p = vlc.MediaPlayer(f"--input-repeat={-1}")
	p.set_mrl(video_path)
	p.play()


def getxy(text, animation, font, pengali=0.8):
	"""
	teks atas 20% -> 0.2
	teks bawah 20% -> 0.8
	"""
	text_width, text_height = font.getsize(text)
	# Calculate the position for the text
	x_pos = int((animation[0].shape[1] - text_width) / 2)
	y_pos = int(animation[0].shape[0] * pengali - (text_height/2))
	return x_pos, y_pos


def put_text_on_image(img, text, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=default_font_scale, thickness=thickness, color='white'):
	"""
	gabung = put_text_on_image(overlay, text, color=color, font_scale=font_scale, thickness=thickness)
	img[y:y+h, x:x+w] = gabung

	bandingkan
	schnell.app.mediautils
		def write_text_on_gif_animation(text, filepath_input, filepath_output, huruf='arial.ttf', ukuranhuruf=40, warna=(255,255,255)):
	"""

	def get_text_width(text, font, font_scale, thickness):
		(width, _) = cv2.getTextSize(text, font, font_scale, thickness)[0]
		return width

	def get_text_height(text, font, font_scale, thickness):
		(_, height) = cv2.getTextSize(text, font, font_scale, thickness)[0]
		return height

	# Get image dimensions
	height, width = img.shape[:2]
	warna = mapwarna[color]

	# Set spacing between lines of text
	v_spacing = int(1.5 * get_text_height(text, font, font_scale, thickness))

	# Split the text into lines based on newlines
	lines = text.splitlines()

	# Initialize variables for drawing text
	x = 0
	y = get_text_height(text, font, font_scale, thickness)

	# Draw the text onto the image
	for line in lines:
		# Split the line into parts based on the image width
		while get_text_width(line, font, font_scale, thickness) > width:
			i = 1
			while get_text_width(line[:i], font, font_scale, thickness) < width:
				i += 1
			part = line[:i-1]
			line = line[i-1:]
			cv2.putText(img, part, (x, y), font, font_scale, warna, thickness)
			y += v_spacing

		# Draw the line onto the image
		cv2.putText(img, line, (x, y), font, font_scale, warna, thickness)
		y += v_spacing

	return img


DEFAULT_FONT = 'impact.ttf'
def write_text_on_gif_animation(text, filepath_input, filepath_output=None, huruf=DEFAULT_FONT, ukuranhuruf=40, warna=(255,255,255), resize=1.0):
	"""
	write_text_on_gif_animation('atas|tengah|bawah', 'trump.gif', 'trump2.gif')
	write_text_on_gif_animation('atas|bawah', 'trump.gif', 'trump2.gif')
	write_text_on_gif_animation('bawah', 'trump.gif', 'trump2.gif')
	"""
	print(f"[write_text_on_gif_animation] #1 filepath_input={filepath_input}, filepath_output={filepath_output}, resize={resize}")
	text = text.strip()
	filepath_input = filepath_input.strip()

	if resize > 0.0 and resize != 1.0:
		print(f"[write_text_on_gif_animation] resizing {filepath_input} => width_factor={resize} times.")
		filepath_input = resize_gif2(filepath_input, width_factor=resize)

	if not filepath_output:
		filepath_output = suffix_filename(filepath_input, '_with_text')
	else:
		filepath_output = filepath_output.strip()
	# filepath_input = absolutify(normy(filepath_input))
	# filepath_output = absolutify(normy(filepath_output))
	print(f"[write_text_on_gif_animation] #2 filepath_input={filepath_input}, filepath_output={filepath_output}")

	# Open the GIF animation
	animation = imageio.mimread(filepath_input)
	# Get the font and set the size
	font = ImageFont.truetype(huruf, ukuranhuruf)

	positions = []

	if '|' in text:
		pecah = text.split('|')
		for i, teks in enumerate(pecah, 1):
			pengali = 0.8
			font = ImageFont.truetype(huruf, ukuranhuruf)
			print(f"i {i}, teks {teks}")
			# jika <spec>tulisan, maka <spec> bisa berisi <#ukuranhuruf, .pengali>
			if teks.startswith('<') and '>' in teks:
				# kiri, kanan = [item.strip() for item in teks.split('>',1)]
				kiri, kanan = [item.strip() for item in teks.split('>')]
				teks = kanan
				kiri = kiri.removeprefix('<')
				for ukuranhuruf_or_pengali in [item.strip() for item in kiri.split(',')]:
					# jk #item maka ukuranhuruf, e.g. #60, jk .5 maka pengali = pos_y
					if ukuranhuruf_or_pengali.startswith('#'):
						ukuranhuruf = int(ukuranhuruf_or_pengali.removeprefix('#'))
						font = ImageFont.truetype(huruf, ukuranhuruf)
					else:
						pengali = float(ukuranhuruf_or_pengali)
			else:
				# jika tulisan saja => bisa tulisbawah, tulisatas|tulisbawah, tulisatas|tulistengah|tulisbawah
				if len(pecah)==3:
					# satu|dua|tiga -> 0.2=satu, 0.5dua, 0.8tiga
					if i==1:
						pengali = 0.2
					elif i==2:
						pengali = 0.5
					# else:
					# 	pengali = 0.8
				elif len(pecah)==2 and i==1:
					# satu|dua -> 0.2=satu, 0.8dua
					pengali = 0.2
			position = getxy(teks, animation, font, pengali)
			positions.append((position, teks))
	else:
		pengali = 0.8
		print(f"only one text: {text}")
		if text.startswith('<') and '>' in text:
			kiri, kanan = [item.strip() for item in text.split('>')]
			text = kanan
			kiri = kiri.removeprefix('<')
			for ukuranhuruf_or_pengali in [item.strip() for item in kiri.split(',')]:
				# jk #item maka ukuranhuruf, e.g. #60, jk .5 maka pengali = pos_y
				if ukuranhuruf_or_pengali.startswith('#'):
					ukuranhuruf = int(ukuranhuruf_or_pengali.removeprefix('#'))
					font = ImageFont.truetype(huruf, ukuranhuruf)
				else:
					pengali = float(ukuranhuruf_or_pengali)
		position = getxy(text, animation, font, pengali=pengali)
		positions.append((position, text))

	# Set the stroke width as a percentage of the font size
	stroke_width_percent = 20 # 20% of font size
	stroke_width = int(round(ukuranhuruf * (stroke_width_percent / 100.0)))

	# Modify each frame of the animation
	modified_frames = []
	for frame in animation:
		# Create a PIL image from the current frame
		pil_image = Image.fromarray(frame)

		# Create a drawing context
		draw = ImageDraw.Draw(pil_image)

		# Add text to the image
		# draw.text((x_pos, y_pos), text, font=font, fill=warna)
		for pos in positions:
			position, text = pos
			x, y = position
			draw.text((x, y), text, font=font, fill=warna, width=stroke_width)

		# Append the modified frame to the list of modified frames
		modified_frames.append(pil_image)

	# Save the modified animation
	print(f"[write_text_on_gif_animation] saving to filepath_output={filepath_output}")
	imageio.mimsave(filepath_output, modified_frames, duration=0.1)
	from schnell.app.imageutils import tampilkan_gif_animation
	tampilkan_gif_animation(filepath_output)
	print(f"[write_text_on_gif_animation] {filepath_output}")
	trycopy(filepath_output)


def write_text_on_gif_animation_from_url(text, alamat, filepath_output=None, huruf='arial.ttf', ukuranhuruf=40, warna=(255,255,255), resize=1.0):
	filepath_input = alamat
	with urllib.request.urlopen(alamat) as response:
		with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmp_file:
			tmp_file.write(response.read())
			filepath_input = tmp_file.name
	write_text_on_gif_animation(text=text, filepath_input=filepath_input, filepath_output=filepath_output, huruf=huruf, ukuranhuruf=ukuranhuruf, warna=warna, resize=resize)


def internal_image_viewer(image_file):
	pyfile = bongkar('ULIBPY_ROOTDIR/schnell/app/imageutils.py')
	os.system(f'python {pyfile} {image_file}')
	print(f'[internal_image_viewer] {image_file}.')


def internal_video_viewer(image_file):
	pyfile = bongkar('ULIBPY_ROOTDIR/schnell/app/showutils.py')
	os.system(f'python {pyfile} {image_file}')
	print(f'[internal_video_viewer] {image_file}.')


def internal_image_viewer_from_url(urlpath, show_text_file=None):
	import tempfile
	import urllib.request

	content = ''
	with urllib.request.urlopen(urlpath) as response:
		with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
			content = response.read()
			tmp_file.write(content)
			tmp_file_path = tmp_file.name

	if os.path.isfile(tmp_file_path):
		# subprocess.call([photos_exe, tmp_file_path])
		# os.remove(tmp_file_path)
		if is_binary(tmp_file_path):
			internal_image_viewer(tmp_file_path)
		elif show_text_file:
			# text
			text_content = '*'*10 + tmp_file_path + '\n' + urlpath + '\n' + '*'*10 + '\n' + content.decode('utf-8')
			show_text_file(text_content)
