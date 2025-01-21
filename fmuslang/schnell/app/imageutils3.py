from PIL import (
	Image,
	ImageChops,
	ImageColor, 
	ImageDraw, 
	ImageFilter, 
	ImageFont,  
	ImageSequence
)
import numpy as np
from .dirutils import absolutify, isabsolute, joiner, disini, suffix_filename, dirname, isfile, bongkar
from .notifutils import notifpy
from .utils import trycopy


def convert_to_rgb(png_file_input, png_file_output=None):
	if not png_file_output:
		png_file_output = suffix_filename(png_file_input, '_to_rgb')
	Image.open(png_file_input).convert('RGB').save(png_file_output)
	return png_file_output


def convert_jpeg_to_transparent_png(jpeg_file_path: str, png_file_path: str=None) -> str:
	"""
	input_file_path = "input.jpg"
	output_file_path = "output.png"

	converted_file_path = convert_jpeg_to_transparent_png(input_file_path, output_file_path)

	print(f"Converted JPEG file {input_file_path} to transparent PNG file {converted_file_path}")

	"""
	if not png_file_path:
		png_file_path = suffix_filename(jpeg_file_path, '_converted_to_png', replace_ext='.png')
	# Open the JPEG image
	jpeg_image = Image.open(jpeg_file_path)

	# Convert the image to RGBA mode, which supports transparency
	rgba_image = jpeg_image.convert("RGBA")

	# Create a new transparent image with the same size as the original
	transparent_image = Image.new("RGBA", rgba_image.size, (0, 0, 0, 0))

	# Paste the RGBA image onto the transparent image
	transparent_image.paste(rgba_image, (0, 0), rgba_image)

	# Save the resulting image as a PNG file
	transparent_image.save(png_file_path)

	notifpy('/imgutils)convert_jpeg_to_transparent_png', f'lihat output di {png_file_path}')
	trycopy(png_file_path)

	# Return the path of the converted PNG file
	return png_file_path


def create_mask_on_png(png_file_input, x=.5, y=.5, w=.5, h=.5, png_file_path=None):
	"""
	create_mask_on_png("input.png", x=.5, y=.5, w=.5, h=.5)
	"""
	if not png_file_path:
		png_file_path = suffix_filename(png_file_input, '_masked')
	# Open the input image
	img = Image.open(png_file_input).convert("RGBA")

	# Get the dimensions of the input image
	width, height = img.size

	# Calculate the coordinates of the rectangle
	x1 = int(width * x - width * w / 2)
	y1 = int(height * y - height * h / 2)
	x2 = int(width * x + width * w / 2)
	y2 = int(height * y + height * h / 2)

	# Create a new transparent mask image
	mask = Image.new("RGBA", img.size, (0, 0, 0, 0))

	# Draw a rectangle on the mask image
	draw = ImageDraw.Draw(mask)
	draw.rectangle((x1, y1, x2, y2), fill=(255, 255, 255, 255))

	# Apply the mask to the input image
	result = Image.alpha_composite(img, mask)

	# Save the result to a new file
	result.save(png_file_path)
	return png_file_path


def scale_image_file(image_file: str, scale_factor=0.5, output_file=None) -> str:
	if not output_file:
		output_file = suffix_filename(image_file, f'scaled_to_{scale_factor}')
	# Determine the file extension
	file_ext = image_file.split(".")[-1].lower()

	# Open the image file using Pillow or NumPy depending on the file extension
	if file_ext == "jpg" or file_ext == "jpeg":
		image = Image.open(image_file)
	elif file_ext == "png":
		image = np.array(Image.open(image_file))
	else:
		raise ValueError("Unsupported file extension")

	# Scale the image using Pillow or NumPy depending on the file extension
	if file_ext == "jpg" or file_ext == "jpeg":
		scaled_image = image.resize((int(image.size[0] * scale_factor), int(image.size[1] * scale_factor)))
	elif file_ext == "png":
		scaled_image = np.array(Image.fromarray(image).resize((int(image.shape[1] * scale_factor), int(image.shape[0] * scale_factor))), np.uint8)
	else:
		raise ValueError("Unsupported file extension")

	# Save the scaled image as a PNG file
	# output_file = "scaled." + file_ext
	if file_ext == "jpg" or file_ext == "jpeg":
		scaled_image.save(output_file)
	elif file_ext == "png":
		Image.fromarray(scaled_image).save(output_file)

	notifpy('/imgutils)scale_image_file', f'lihat output di {output_file}')
	trycopy(output_file)

	# Return the path of the scaled image file
	return output_file


def image_to_square(image_input, image_output=None):
	if not image_output:
		image_output = suffix_filename(image_input, '_squared')
	with Image.open(image_input) as img:
		width, height = img.size
		min_dimension = min(width, height)
		cropped_img = img.crop((0, 0, min_dimension, min_dimension))
		resized_img = cropped_img.resize((min_dimension, min_dimension))
		resized_img.save(image_output)

	notifpy('/imgutils)scale_image_file', f'lihat output di {image_output}')
	trycopy(image_output)


def overlay_image(original_image, overlay_image, output_path=None, transparency=1.0, scale_percent=100, x=0.5, y=0.5):
	"""
	overlay_image('original_image.png', 'overlay_image.png', transparency=0.5, scale=0.8, x=0.3, y=0.4)
	"""
	if not output_path:
		output_path = suffix_filename(original_image, '_overlaid')
	# Open the images
	original = Image.open(original_image).convert('RGBA')
	overlay = Image.open(overlay_image).convert('RGBA')

	# Calculate the position of the overlay image
	position_x = int(x * original.width)
	position_y = int(y * original.height)

	# Scale the overlay image
	if scale_percent != 100:
		overlay = overlay.resize((int(overlay.width * scale_percent/100), int(overlay.height * scale_percent/100)))

	# Create a new image with transparency
	merged = Image.new('RGBA', original.size)

	# Apply transparency to the overlay image
	if transparency < 1.0:
		overlay = Image.blend(overlay, Image.new('RGBA', overlay.size, (255, 255, 255, int(255 * transparency))), transparency)

	print(f"""overlay_image
	original_image={original_image}, {original.size}
	overlay_image={overlay_image}, {overlay.size}
	output_path={output_path}
	transparency={transparency}
	scale_percent={scale_percent}
	x={x}, position_x={position_x}
	y={y}, position_y={position_y}
	""")

	if overlay.mode == 'RGBA':
		print("Overlay image has an alpha channel.")
	else:
		print("Overlay image does not have an alpha channel.")
	# Overlay the images
	merged.paste(original, (0, 0))
	merged.paste(overlay, (position_x, position_y), overlay)

	# Save the resulting image
	merged.save(output_path)


# def overlay_image2(original_image, overlay_image, output_path=None, transparency=1.0, scale=1.0, x=0.5, y=0.5, save_without_profile=True):
# 	"""
# 	overlay_image2('original_image.png', 'overlay_image.png', transparency=0.5, scale=0.8, x=0.3, y=0.4)
# 	"""
# 	if not output_path:
# 		output_path = suffix_filename(original_image, '_overlaid')
# 	# Open the images
# 	original = Image.open(original_image)
# 	overlay = Image.open(overlay_image)

# 	# Calculate the position of the overlay image
# 	position_x = int(x * original.width)
# 	position_y = int(y * original.height)

# 	# Scale the overlay image
# 	overlay = overlay.resize((int(overlay.width * scale), int(overlay.height * scale)))

# 	# Create a new image with transparency
# 	merged = Image.new('RGBA', original.size)

# 	# Apply transparency to the overlay image
# 	overlay = Image.blend(overlay, Image.new('RGBA', overlay.size, (255, 255, 255, int(255 * transparency))), transparency)

# 	# Overlay the images
# 	merged.paste(original, (0, 0))
# 	merged.paste(overlay, (position_x, position_y), overlay)

# 	# Save the resulting image without ICC profile
# 	save_kwargs = {}
# 	if save_without_profile:
# 		save_kwargs['icc_profile'] = original.info.get('icc_profile')

# 	merged.save(output_path, **save_kwargs)

def overlay_image2(original_image, overlay_image, output_path=None, transparency=1.0, scale=1.0, x=0.5, y=0.5, save_without_profile=True):
	if not output_path:
		output_path = suffix_filename(original_image, '_overlaid')
	original = Image.open(original_image).convert("RGBA")
	overlay = Image.open(overlay_image).convert("RGBA")

	# Calculate the position of the overlay image
	position_x = int(x * (original.width - overlay.width))
	position_y = int(y * (original.height - overlay.height))

	# Scale the overlay image
	overlay = overlay.resize((int(overlay.width * scale), int(overlay.height * scale)))

	# Create a new image with transparency
	merged = Image.new('RGBA', original.size)

	# Apply transparency to the overlay image
	overlay = Image.blend(overlay, Image.new('RGBA', overlay.size, (255, 255, 255, int(255 * transparency))), transparency)

	# Overlay the images
	merged.paste(original, (0, 0))
	merged.paste(overlay, (position_x, position_y), overlay)

	# Save the resulting image without ICC profile
	save_kwargs = {}
	if save_without_profile:
		save_kwargs['icc_profile'] = original.info.get('icc_profile')

	merged.save(output_path, **save_kwargs)

# # Example usage
# overlay_image('original_image.png', 'overlay_image.png', transparency=0.5, scale=0.8, x=0.3, y=0.4)
# from PIL import Image
import numpy as np

def overlay_image3(original_image, overlay_image, output_path=None, transparency=1.0, scale=1.0, x=0.5, y=0.5, save_without_profile=True):
	# Open the images
	if not output_path:
		output_path = suffix_filename(original_image, '_overlaid3')
	original = Image.open(original_image).convert("RGBA")
	overlay = Image.open(overlay_image).convert("RGBA")

	# Calculate the position of the overlay image
	position_x = int(x * (original.width - overlay.width))
	position_y = int(y * (original.height - overlay.height))

	# Scale the overlay image
	overlay = overlay.resize((int(overlay.width * scale), int(overlay.height * scale)))

	# Convert images to NumPy arrays
	original_array = np.array(original)
	overlay_array = np.array(overlay)

	# Normalize the alpha channel of the overlay image
	overlay_array[:, :, 3] = int(255 * transparency)

	# Calculate the region to overlay the image
	region = np.s_[position_y:position_y + overlay_array.shape[0], position_x:position_x + overlay_array.shape[1]]

	# Blend the images
	result_array = np.where(overlay_array[:, :, 3] > 0, overlay_array, original_array[region])

	# Create a new image from the NumPy array
	result = Image.fromarray(result_array.astype(np.uint8))

	# Save the resulting image without ICC profile
	save_kwargs = {}
	if save_without_profile:
		save_kwargs['icc_profile'] = original.info.get('icc_profile')

	result.save(output_path, **save_kwargs)

# # Example usage
# overlay_image('original_image.png', 'overlay_image.png', transparency=0.5, scale=0.8, x=0.3, y=0.4)

DEFAULT_FONT = 'impact.ttf'


def getxy(text, animation, font, pengali=0.8):
	"""
	teks atas 20% -> 0.2
	teks bawah 20% -> 0.8
	"""
	text_width, text_height = font.getsize(text)
	# Calculate the position for the text
	width, height = animation.size  # animation.shape[1], animation.shape[0]
	x_pos = int((width - text_width) / 2)
	y_pos = int(height * pengali - (text_height/2))
	return x_pos, y_pos


def write_text_on_image(text, filepath_input, filepath_output=None, huruf=DEFAULT_FONT, ukuranhuruf=40, warna=(255,255,255)):
	text = text.strip()
	filepath_input = filepath_input.strip()

	if not filepath_output:
		filepath_output = suffix_filename(filepath_input, '_with_text')
	else:
		filepath_output = filepath_output.strip()

	font = ImageFont.truetype(huruf, ukuranhuruf)

	file_ext = filepath_input.split(".")[-1].lower()
	# if file_ext == "jpg" or file_ext == "jpeg":
	# 	# image = Image.open(image_file)
	# 	animation = Image.open(filepath_input).convert("RGBA")
	# elif file_ext == "png":
	# 	animation = np.array(Image.open(filepath_input))
	# else:
	# 	raise ValueError("Unsupported file extension")
	animation = Image.open(filepath_input).convert("RGBA")

	positions = []
	if '|' in text:
		pecah = text.split('|')
		for i, teks in enumerate(pecah, 1):
			pengali = 0.8
			font = ImageFont.truetype(huruf, ukuranhuruf)
			print(f"i {i}, teks {teks}")
			if teks.startswith('<') and '>' in teks:
				kiri, kanan = [item.strip() for item in teks.split('>')]
				teks = kanan
				kiri = kiri.removeprefix('<')
				for ukuranhuruf_or_pengali in [item.strip() for item in kiri.split(',')]:
					if ukuranhuruf_or_pengali.startswith('#'):
						ukuranhuruf = int(ukuranhuruf_or_pengali.removeprefix('#'))
						font = ImageFont.truetype(huruf, ukuranhuruf)
					else:
						pengali = float(ukuranhuruf_or_pengali)
			else:
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
				if ukuranhuruf_or_pengali.startswith('#'):
					ukuranhuruf = int(ukuranhuruf_or_pengali.removeprefix('#'))
					font = ImageFont.truetype(huruf, ukuranhuruf)
				else:
					pengali = float(ukuranhuruf_or_pengali)
		position = getxy(text, animation, font, pengali=pengali)
		positions.append((position, text))

	stroke_width_percent = 20 # 20% of font size
	stroke_width = int(round(ukuranhuruf * (stroke_width_percent / 100.0)))

	draw = ImageDraw.Draw(animation)
	for pos in positions:
		position, text = pos
		x, y = position
		draw.text((x, y), text, font=font, fill=warna, width=stroke_width)

	# if file_ext == "jpg" or file_ext == "jpeg":
	# 	animation.save(filepath_output)
	# elif file_ext == "png":
	# 	Image.fromarray(animation).save(filepath_output)
	animation.save(filepath_output)

	notifpy('/imgutils)write_text_on_image', f'lihat output di {filepath_output}')
	trycopy(filepath_output)
