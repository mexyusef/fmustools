import numpy as np
import cv2
import random
import requests
from urllib.request import urlopen

mapwarna = {
    'blue': (255,0,0),
    'green': (0,255,0),
    'red': (0,0,255),

    'cyan': (255,255,0),
    'magenta': (255,0,255),
    'yellow': (0,255,255),

    'white': (255,255,255),
    'black': (0,0,0),
}

font = cv2.FONT_HERSHEY_SIMPLEX
default_font_scale = 1
thickness = 2

img = np.zeros((__TINGGI__, __LEBAR__, 3), dtype=np.uint8)
#img.fill(__WARNA__) # or img[:] = 255
img[:] = __WARNA__


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

def create_rect(x,y,w,h,warna='red'):
    # global img
    x,y,w,h = int(x),int(y),int(w),int(h)
    cv2.rectangle(img, (x,y), (x+w,y+h), mapwarna[warna], -1)

def create_circle(x,y,w,h,warna='red'):
    # global img
    center = (x+(w//2), y+(h//2))
    radius = min(w,h)//2
    cv2.circle(img, center, radius, mapwarna[warna], -1)

def create_eclipse(x,y,w,h,warna='red'):
    # global img
    center = (x+(w//2), y+(h//2))
    radius = min(w,h)//2
    ax1 = w//2
    ax2 = h//2
    angle = 0
    startangle = 0
    endangle = 360
    cv2.eclipse(img, center, (ax1,ax2), angle, startangle, endangle, mapwarna[warna], -1)

def create_image2(alamat, x,y,w,h, alpha=0.5):
    global img
    x,y,w,h = int(x),int(y),int(w),int(h)
    req = urlopen(alamat)
    #print(alamat, ':', req)
    image = np.asarray(bytearray(req.read()), dtype=np.uint8)
    #image = cv2.imdecode(image, -1)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if w==0 or h==0:
        h,w,_=image.shape
    else:
        image = cv2.resize(image.copy(), (w,h))

    #img = np.uint8(img*alpha + image*(1-alpha))

    #print(f'''
    #x = {x}
    #y = {y}
    #w = {w}
    #    x+w = {x+w}
    #h = {h}
    #    y+h = {y+h}
    #shape 1 = {img.shape}
    #shape 2 = {image.shape}
    #''')

    #https://stackoverflow.com/questions/56002672/display-an-image-over-another-image-at-a-particular-co-ordinates-in-opencv
    #img[x:x+w,y:y+h,:] = image[0:w,0:h,:]
    img[y:y+image.shape[0], x:x+image.shape[1]] = image

def create_image(alamat, x, y, w, h, alpha=0.5):
    global img
    x, y, w, h = int(x), int(y), int(w), int(h)
    req = urlopen(alamat)

    image = np.asarray(bytearray(req.read()), dtype=np.uint8)

    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if w == 0 or h == 0:
        h, w, _ = image.shape
    else:
        image = cv2.resize(image.copy(), (w, h))

    overlay = image.copy()
    alpha = max(0, min(1, alpha))  # Make sure alpha is in the range [0,1]
    cv2.addWeighted(overlay, alpha, img[y:y + h, x:x + w], 1 - alpha, 0, img[y:y + h, x:x + w])

def write_on_rectangle(text, x, y, w, h, color='blue', font_scale=default_font_scale, thickness=thickness, warna_rectangle = (255,255,255), alpha=0.5):
    '''
    contoh:
    write_on_rectangle("""LMAO""", 250.0, 100.0, 330.0, 100.0, font_scale=3.75, thickness=10, color="red", warna_rectangle=mapwarna["green"], alpha=0.9)
    '''
    
    global img, put_text_on_image
    x,y,w,h = int(x),int(y),int(w),int(h)
    warna_tulisan = mapwarna[color]
    black = np.zeros((h, w, 3), np.uint8)  # Create a black image with the specified size

    # Convert the color from a string to a tuple of BGR values
    #if isinstance(color, str):
    #    color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))[::-1]

    overlay = black.copy()
    cv2.rectangle(overlay, (0, 0), (w, h), warna_rectangle, -1)
    alpha = max(0, min(1, alpha))
    cv2.addWeighted(overlay, alpha, black, 1 - alpha, 0, black)

    gabung = put_text_on_image(overlay, text, color=color, font_scale=font_scale, thickness=thickness)

    # Set the position of the rectangle within the image
    #x, y = int(x), int(y)
    #img = np.zeros((y + h, x + w, 3), np.uint8)
    #img[:, :] = (255, 255, 255) # background putih, harusnya sesuai dg main color
    img[y:y+h, x:x+w] = gabung

    #return img_with_rect

def create_line():
    pass

def create_text(x, y, tulisan, warna='black', scale=1.5, thick=2):
    # (image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    x,y = int(x),int(y)
    if y == 0:
        y = 25 # biar keliatan
    cv2.putText(img, tulisan, (x,y), font, scale, mapwarna[warna], thick)

__TEMPLATE_CODE__

cv2.imshow(r'__FILEPATH__', img)
__TEMPLATE_TULIS_FILEPATH__
cv2.waitKey(0)
cv2.destroyAllWindows()