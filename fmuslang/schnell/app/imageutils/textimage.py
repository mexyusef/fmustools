from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def create_text_image(text, w=200, h=100, filename=None, font_size=None, bg_color='white', fg_color='black', show=True, font_path=None, alignment='center', wrap=False):
    # Create a blank image with the specified background color
    image = Image.new('RGB', (w, h), bg_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    if font_path:
        font = ImageFont.truetype(font_path, font_size if font_size else 20)
    else:
        font = ImageFont.load_default()

    # Auto-adjust font size if not specified
    if not font_size:
        font_size = 10  # Start with a reasonable font size
        font = ImageFont.truetype(font_path if font_path else "arial.ttf", font_size)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        while text_width < w * 0.9 and text_height < h * 0.9:  # Fill 90% of the image
            font_size += 1
            font = ImageFont.truetype(font_path if font_path else "arial.ttf", font_size)
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        font_size -= 1  # Decrease font size for better fit
        font = ImageFont.truetype(font_path if font_path else "arial.ttf", font_size)

    # Calculate text position based on alignment
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    if alignment == 'left':
        x = 0
    elif alignment == 'right':
        x = w - text_width
    else:  # center
        x = (w - text_width) / 2
    y = (h - text_height) / 2

    # Draw the text
    draw.text((x, y), text, fill=fg_color, font=font)

    # Save the image
    if filename is None:
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + '.png'
    image.save(filename)

    # Show the image if requested
    if show:
        image.show()

    return filename

def test_create_text_image():
    filename = create_text_image("HELLO WORLD", font_size=None, bg_color='white', fg_color='black', show=True, alignment='center', wrap=True)
    print(filename)
