from PIL import Image
from schnell.app.dirutils import suffix_filename

def resize_image_with_crop_and_padding(image_path, new_width, new_height, output_path=None, horizontal_crop_ratio=(1, 1), vertical_crop_ratio=(1, 1), background_color=(255, 255, 255)):
	image = Image.open(image_path)
	width, height = image.size

	if not output_path:
		output_path = suffix_filename(image_path, '_scaled')
	# Calculate the crop area
	horizontal_total_crop = max(width - new_width, 0)
	vertical_total_crop = max(height - new_height, 0)

	left_crop = horizontal_total_crop * (horizontal_crop_ratio[0] / (horizontal_crop_ratio[0] + horizontal_crop_ratio[1]))
	right_crop = horizontal_total_crop - left_crop

	top_crop = vertical_total_crop * (vertical_crop_ratio[0] / (vertical_crop_ratio[0] + vertical_crop_ratio[1]))
	bottom_crop = vertical_total_crop - top_crop

	# Crop the image
	cropped_image = image.crop((left_crop, top_crop, width - right_crop, height - bottom_crop))

	# Create a new image with the desired size and white background
	final_image = Image.new('RGB', (new_width, new_height), background_color)

	# Calculate the position to paste the cropped image onto the background
	paste_x = (new_width - cropped_image.width) // 2
	paste_y = (new_height - cropped_image.height) // 2

	# Paste the cropped image onto the background
	final_image.paste(cropped_image, (paste_x, paste_y))

	# Save the final image
	final_image.save(output_path)

def test_resize_image_with_crop_and_padding():
	resize_image_with_crop_and_padding('path/to/input_image.jpg', 300, 300, horizontal_crop_ratio=(1.5, 1), vertical_crop_ratio=(1, 1))

def resize_image_with_scaling_and_padding(image_path, new_width, new_height, output_path=None, background_color=(255, 255, 255)):
	image = Image.open(image_path)
	width, height = image.size

	if not output_path:
		output_path = suffix_filename(image_path, '_scaled')

	# Calculate the scaling factor and new size
	scale_factor = min(new_width / width, new_height / height)
	scaled_width = int(width * scale_factor)
	scaled_height = int(height * scale_factor)

	# Resize the image
	scaled_image = image.resize((scaled_width, scaled_height))

	# Create a new image with the desired size and white background
	final_image = Image.new('RGB', (new_width, new_height), background_color)

	# Calculate the position to paste the scaled image onto the background
	paste_x = (new_width - scaled_width) // 2
	paste_y = (new_height - scaled_height) // 2

	# Paste the scaled image onto the background
	final_image.paste(scaled_image, (paste_x, paste_y))

	# Save the final image
	final_image.save(output_path)

def test_resize_image_with_scaling_and_padding():
	resize_image_with_scaling_and_padding('path/to/input_image.jpg', 300, 300)
