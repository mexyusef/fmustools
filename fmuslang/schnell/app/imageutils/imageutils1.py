# https://www.thepythoncode.com/article/extract-text-from-images-or-scanned-pdf-python
import cv2
from PIL import Image
import os, math, re
import numpy as np
import pandas as pd
import subprocess
# from PIL import Image
from io import BytesIO
import platform
import tempfile
import urllib.request
import imageio
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtCore import QPointF, Qt, QRectF, QSizeF
from PyQt5.QtGui import QPainter, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene
# photos_exe = r"C:\Program Files\WindowsApps\Microsoft.Windows.Photos_8wekyb3d8bbwe\Microsoft.Photos.exe"
# photos_exe = r"C:\Program Files\WindowsApps\Microsoft.PhotosLegacy_2023.11030.15002.0_x64__8wekyb3d8bbwe\Microsoft.Photos.exe"
photos_exe = r"C:\Program Files\WindowsApps\Microsoft.Windows.Photos_2023.11010.17009.0_x64__8wekyb3d8bbwe\PhotosApp.exe"
# Microsoft.Windows.Photos_2023.11010.17009.0_x64__8wekyb3d8bbwe


def microsoft_photos(image_path):
    # photos_exe = r"C:\Program Files\WindowsApps\Microsoft.Windows.Photos_8wekyb3d8bbwe\Microsoft.Photos.exe"
    subprocess.call([photos_exe, image_path])
    # subprocess.call(["start", "microsoft.photos:", f"//{image_path}"])

def microsoft_photos_from_url(url):
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(response.read())
            tmp_file_path = tmp_file.name
    
    if os.path.isfile(tmp_file_path):
        subprocess.call([photos_exe, tmp_file_path])
        os.remove(tmp_file_path)
    else:
        print(f"File not found: {tmp_file_path}")

def show_image(image_path):
    from tkinter import Tk, Label, PhotoImage
    # Load image from file
    image = Image.open(image_path)

    # Display image using platform-specific viewer
    if platform.system() == 'Darwin':  # macOS
        image.show()
    else:  # Windows or Linux
        with BytesIO() as buffer:
            image.save(buffer, format='PNG')
            buffer.seek(0)
            img_data = buffer.read()
        
        root = Tk()
        root.title('Image Viewer')
        img = PhotoImage(data=img_data)
        label = Label(root, image=img)
        label.pack()
        root.mainloop()

# Show image using Matplotlib
def show_image_mpl(image_path):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    # Load image from file
    img = mpimg.imread(image_path)

    # Display image using Matplotlib
    plt.imshow(img)
    plt.show()

# Show image using OpenCV
def show_image_cv(image_path):
    # Load image from file
    img = cv2.imread(image_path)

    # Display image using OpenCV
    try:
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as err:
        print('gagal imshow:', err)

# Show image using Pygame
def show_image_pygame(image_path):
    import pygame
    # Initialize Pygame
    pygame.init()

    # Load image from file
    img = pygame.image.load(image_path)

    # Create Pygame window and display image
    screen = pygame.display.set_mode(img.get_rect().size)
    screen.blit(img, img.get_rect())
    pygame.display.flip()

    # Wait for window to close
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit Pygame
    pygame.quit()

# Show image from URL using Matplotlib
def show_image_url_mpl(url):
    import urllib.request
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    # Load image from URL
    with urllib.request.urlopen(url) as url_response:
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

    # Display image using Matplotlib
    plt.imshow(img)
    plt.show()

# Show image from URL using OpenCV
def show_image_url_cv(url):
    import urllib.request
    import cv2

    # Load image from URL
    with urllib.request.urlopen(url) as url_response:
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

    # Display image using OpenCV
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Show image from URL using Pygame
def show_image_url_pygame(url):
    import urllib.request
    import pygame

    # Initialize Pygame
    pygame.init()

    # Load image from URL
    with urllib.request.urlopen(url) as url_response:
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
    img = pygame.surfarray.make_surface(img.swapaxes(0, 1))

    # Create Pygame window and display image
    screen = pygame.display.set_mode(img.get_size())
    screen.blit(img, (0, 0))
    pygame.display.flip()

    # Wait for window to close
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit Pygame
    pygame.quit()

# Show image from URL using Tkinter
def show_image_url_tk(url):
    import urllib.request
    from PIL import Image, ImageTk
    import tkinter as tk

    # Load image from URL
    with urllib.request.urlopen(url) as url_response:
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

    # Create Tkinter window and display image
    root = tk.Tk()
    root.geometry('%dx%d' % (img.shape[1], img.shape[0]))
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    label = tk.Label(root, image=imgtk)
    label.pack()
    root.mainloop()


# Image Pre-Processing Functions to improve output accurracy
# Convert to grayscale

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove noise
def remove_noise(img):
    return cv2.medianBlur(img, 5)

# Thresholding
def threshold(img):
    # return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# dilation
def dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)

# erosion
def erode(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(img, kernel, iterations=1)

# opening -- erosion followed by a dilation
def opening(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# canny edge detection
def canny(img):
    return cv2.Canny(img, 100, 200)

# skew correction
def deskew(img):
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

# template matching
def match_template(img, template):
    return cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

def convert_img2bin(img):
    """
    Pre-processes the image and generates a binary output
    """
    # Convert the image into a grayscale image
    output_img = grayscale(img)
    # Invert the grayscale image by flipping pixel values.
    # All pixels that are grater than 0 are set to 0 and all pixels that are = to 0 are set to 255
    output_img = cv2.bitwise_not(output_img)
    # Converting image to binary by Thresholding in order to show a clear separation between white and blacl pixels.
    output_img = threshold(output_img)
    return output_img

def display_img(title, img):
    """Displays an image on screen and maintains the output until the user presses a key"""
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.setWindowTitle('img', title)
    cv2.resizeWindow('img', 1200, 900)
    # Display Image on screen
    cv2.imshow('img', img)
    # Mantain output until user presses a key
    cv2.waitKey(0)
    # Destroy windows when user presses a key
    cv2.destroyAllWindows()

def pix2np(pix):
    """
    Converts a pixmap buffer into a numpy array
    """
    # pix.samples = sequence of bytes of the image pixels like RGBA
    #pix.h = height in pixels
    #pix.w = width in pixels
    # pix.n = number of components per pixel (depends on the colorspace and alpha)
    im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.h, pix.w, pix.n)
    try:
        im = np.ascontiguousarray(im[..., [2, 1, 0]])  # RGB To BGR
    except IndexError:
        # Convert Gray to RGB
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
        im = np.ascontiguousarray(im[..., [2, 1, 0]])  # RGB To BGR
    return im

def generate_ss_text(ss_details):
    """Loops through the captured text of an image and arranges this text line by line.
    This function depends on the image layout.
    
    function iterates throughout the captured text of an image and arranges the grabbed text line by line. It depends on the image layout and may require tweaking for some image formats.
    """
    # Arrange the captured text after scanning the page
    parse_text = []
    word_list = []
    last_word = ''
    # Loop through the captured text of the entire page
    for word in ss_details['text']:
        # If the word captured is not empty
        if word != '':
            # Add it to the line word list
            word_list.append(word)
            last_word = word
        if (last_word != '' and word == '') or (word == ss_details['text'][-1]):
            parse_text.append(word_list)
            word_list = []
    return parse_text

def search_for_text(ss_details, search_str):
    """Search for the search string within the image content"""
    # Find all matches within one page
    results = re.findall(search_str, ss_details['text'], re.IGNORECASE)
    # In case multiple matches within one page
    for result in results:
        yield result

def save_page_content(pdfContent, page_id, page_data):
    """Appends the content of a scanned page, line by line, to a pandas DataFrame."""
    if page_data:
        for idx, line in enumerate(page_data, 1):
            line = ' '.join(line)
            pdfContent = pdfContent.append(
                {'page': page_id, 'line_id': idx, 'line': line}, ignore_index=True
            )
    return pdfContent

def save_file_content(pdfContent, input_file):
    """Outputs the content of the pandas DataFrame to a CSV file having the same path as the input_file
    but with different extension (.csv)"""
    content_file = os.path.join(os.path.dirname(input_file), os.path.splitext(
        os.path.basename(input_file))[0] + ".csv")
    pdfContent.to_csv(content_file, sep=',', index=False)
    return content_file

def calculate_ss_confidence(ss_details: dict):
    """Calculate the confidence score of the text grabbed from the scanned image.
    write a function that calculates the confidence score of the text grabbed from the scanned image
    """
    # page_num  --> Page number of the detected text or item
    # block_num --> Block number of the detected text or item
    # par_num   --> Paragraph number of the detected text or item
    # line_num  --> Line number of the detected text or item
    # Convert the dict to dataFrame
    df = pd.DataFrame.from_dict(ss_details)
    # Convert the field conf (confidence) to numeric
    df['conf'] = pd.to_numeric(df['conf'], errors='coerce')
    # Elliminate records with negative confidence
    df = df[df.conf != -1]
    # Calculate the mean confidence by page
    conf = df.groupby(['page_num'])['conf'].mean().tolist()
    return conf[0]

def draw1():
    r1 = 70
    r2 = 30

    ang = 60

    d = 170
    h = int(d/2*math.sqrt(3))

    dot_red = (256,128)
    dot_green = ( int(dot_red[0]-d/2), dot_red[1]+h)
    dot_blue = ( int(dot_red[0]+d/2), dot_red[1]+h)

    # tan = float(dot_red[0]-dot_green[0])/(dot_green[1]-dot_red[0])
    # ang = math.atan(tan)/math.pi*180

    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    black = (0, 0, 0)

    full = -1

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img, dot_red, r1, red, full)
    # print(
    #   'img:', img,
    #   '.green:', dot_green,
    #   'r1:', r1,
    #   'green:', green,
    #   'full:', full
    # )
    cv2.circle(
        img,
        dot_green,
        r1,
        green,
        full
    )
    cv2.circle(img, dot_blue, r1, blue, full)
    cv2.circle(img, dot_red, r2, black, full)
    cv2.circle(img, dot_green, r2, black, full)
    cv2.circle(img, dot_blue, r2, black, full)

    cv2.ellipse(img, dot_red, (r1, r1), ang, 0, ang, black, full)
    cv2.ellipse(img, dot_green, (r1, r1), 360-ang, 0, ang, black, full)
    cv2.ellipse(img, dot_blue, (r1, r1), 360-2*ang, ang, 0, black, full)

    # filepath = "opencv_logo.png"
    # cv2.imwrite(filepath, img)
    # img = Image.open(filepath)
    # img.show()
    cv2.imshow('img', img)
    cv2.waitKey(0)

def draw2():
    img=np.zeros((500,500,3), np.uint8)

    cv2.ellipse(img, (250,100), (70,70), 135, 0, 270, (0,0,255),50)
    cv2.ellipse(img, (150,280), (70,70), 10, 0, 270, (0,255,0),50)
    cv2.ellipse(img, (350,280), (70,70), 315, 0, 270, (255,0,0),50)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(75,450), font, 3,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow('img', img)
    cv2.waitKey(0)

class ImageView(QGraphicsView):

    def __init__(self, *args, **kwargs):
        image = kwargs.pop('image', None)
        background = kwargs.pop('background', None)
        self.quit_mode = kwargs.pop('quit_mode', False)
        super(ImageView, self).__init__(*args, **kwargs)
        self.setCursor(Qt.OpenHandCursor)
        self.setBackground(background)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                            QPainter.SmoothPixmapTransform)
        self.setCacheMode(self.CacheBackground)
        self.setViewportUpdateMode(self.SmartViewportUpdate)
        self._item = QGraphicsPixmapItem()
        self._item.setFlags(QGraphicsPixmapItem.ItemIsFocusable | QGraphicsPixmapItem.ItemIsMovable)
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self._scene.addItem(self._item)
        rect = QApplication.instance().desktop().availableGeometry(self)
        w = rect.width()
        h = rect.height()
        self.resize(int(w * 0.9), int(h * 0.9))

        self.pixmap = None
        self._delta = 0.1
        self.setPixmap(image)

    def setBackground(self, color):
        if isinstance(color, QColor):
            self.setBackgroundBrush(color)
        elif isinstance(color, (str, Qt.GlobalColor)):
            color = QColor(color)
            if color.isValid():
                self.setBackgroundBrush(color)

    def setPixmap(self, pixmap, fitIn=True):
        if isinstance(pixmap, QPixmap):
            self.pixmap = pixmap
        elif isinstance(pixmap, QImage):
            self.pixmap = QPixmap.fromImage(pixmap)
        elif isinstance(pixmap, str) and os.path.isfile(pixmap):
            self.pixmap = QPixmap(pixmap)
        else:
            return
        self._item.setPixmap(self.pixmap)
        self._item.update()
        self.setSceneDims()
        posisi = self._item.pos()
        ukuran = self.pixmap.size()
        # print('[app.imageutils#setPixmap] ukuran:', ukuran, 'posisi:', (posisi.x(), posisi.y()))
        if fitIn:
            self.fitInView(QRectF(posisi, QSizeF(ukuran)), Qt.KeepAspectRatio)
        self.update()

    def setSceneDims(self):
        if not self.pixmap:
            return
        self.setSceneRect(QRectF(QPointF(0, 0), QPointF(self.pixmap.width(), self.pixmap.height())))

    def fitInView(self, rect, flags=Qt.IgnoreAspectRatio):
        if not self.scene() or rect.isNull():
            return
        unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        viewRect = self.viewport().rect()
        sceneRect = self.transform().mapRect(rect)
        layarw, layarh = sceneRect.width(), sceneRect.height()
        vieww, viewh = viewRect.width(), viewRect.height()
        x_ratio = vieww / layarw
        y_ratio = viewh / layarh
        if flags == Qt.KeepAspectRatio:
            x_ratio = y_ratio = min(x_ratio, y_ratio)
        elif flags == Qt.KeepAspectRatioByExpanding:
            x_ratio = y_ratio = max(x_ratio, y_ratio)

        # print('rasio:', x_ratio, y_ratio)
        # print('layar:', layarw, layarh)
        # print('view:', vieww, viewh)
        pengali=2
        self.scale(x_ratio*pengali, y_ratio*pengali)
        self.centerOn(rect.center())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def zoomIn(self):
        self.zoom(1 + self._delta)

    def zoomOut(self):
        self.zoom(1 - self._delta)

    def zoom(self, factor):
        _factor = self.transform().scale(
            factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            return
        self.scale(factor, factor)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            if self.quit_mode:
                self.close()
            else:
                self.hide()

def tampilkan_acdsee(gambar = 'C:/fr/belum-coded/love-samping01.jpg'):
    app = QApplication([])
    w = ImageView(image=gambar, background=Qt.black)
    w.show()
    app.aboutToQuit.connect(app.deleteLater)  # delete the app instance when the image view is closed
    app.exec_()

def tampilkan_gif_animation(gif_path = "C:/Users/usef/dwhelper/out-of-the-way.gif", window_label="Press Esc or 'q' to exit"):
    # Load the GIF animation
    gif = cv2.VideoCapture(gif_path)

    # Create a window to display the animation
    cv2.namedWindow(window_label, cv2.WINDOW_NORMAL)

    # Set the window dimensions to the size of the GIF frames
    width = int(gif.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(gif.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.resizeWindow(window_label, width, height)

    # Display the animation
    while True:
        ret, frame = gif.read()
        if not ret:
            break
        cv2.imshow(window_label, frame)
        key = cv2.waitKey(100)
        if key == 27 or key == ord('q'): # Press 'ESC' to exit
            break

    # Release the resources
    gif.release()
    cv2.destroyAllWindows()

# tampilkan_gif_animation()

def write_text_on_gif_animation_single(text = "Hello, world!", gif_input='c:/users/usef/dwhelper/trump.gif', gif_output=None, pengalivertikal=0.8, huruf='arial.ttf', ukuranhuruf=40):
    if not gif_output:
        from schnell.app.dirutils import suffix_filename
        gif_output = suffix_filename(gif_input, '_with_text')
    # Open the GIF animation
    animation = imageio.mimread(gif_input)
    # Get the font and set the size
    font = ImageFont.truetype(huruf, ukuranhuruf)
    # Define the text and its size
    text_width, text_height = font.getsize(text)
    # Calculate the position for the text
    x_pos = int((animation[0].shape[1] - text_width) / 2)
    y_pos = int(animation[0].shape[0] * pengalivertikal - text_height)
    # Modify each frame of the animation
    modified_frames = []
    for frame in animation:
        # Create a PIL image from the current frame
        pil_image = Image.fromarray(frame)
        # Create a drawing context
        draw = ImageDraw.Draw(pil_image)
        # Add text to the image
        draw.text((x_pos, y_pos), text, font=font, fill=(255,255,255))
        # Append the modified frame to the list of modified frames
        modified_frames.append(pil_image)

    # Save the modified animation
    imageio.mimsave(gif_output, modified_frames, duration=0.1)
    tampilkan_gif_animation(gif_output)

def windows_photo_viewer(photo_path = r'C:\fr\381.JPG', viewer_path = r'C:\Program Files\Windows Photo Viewer\PhotoViewer.dll'):
    os.system(f'rundll32 "{viewer_path}", ImageView_Fullscreen "{photo_path}"')


# juga cek
# https://github.com/djentleman/imgrender
# https://github.com/stefanhaustein/TerminalImageViewer
# https://github.com/PerBothner/DomTerm

# pip install --user ascii_art climage

# # https://www.tutorialspoint.com/display-images-on-terminal-using-python
# # pip install ascii_art
# from ascii_art import ascii_art
# def print_image_ascii(image_path):
#     print('print_image_ascii')
#     with open(image_path, "rb") as f:
#         image_data = f.read()
#     # Convert the image to ASCII art
#     ascii_data = ascii_art(image_data)
#     # Display the ASCII art in the terminal
#     print(ascii_data)

# https://www.geeksforgeeks.org/display-images-on-terminal-using-python/
# pip install climage
# climage [-h] [-v] [–unicode | –ascii] [–truecolor | –256color | –16color | –8color] [–palette {default,xterm,linuxconsole,solarized,rxvt,tango,gruvbox,gruvboxdark}] [-w width] [-o outfile] inputfile

# convert(filename, is_unicode=False, is_truecolor=False, is_256color=True, is_16color=False, is_8color=False, width=80, palette=”default”)
# Parameters:
# filename : Name of image file.
# is_unicode :  If true, conversion is done in unicode format, otherwise ASCII characters will be used.
# is_truecolor :  Whether to use RGB colors in generation, if supported by terminal. Defaults False.
# is_256color : Whether to use 256 colors encoding. Defaults True.
# is_16color : Whether to use 16 colors encoding. Defaults False.
# is_8color : Whether to use first 8 System colors. Defaults False.
# width : Number of blocks of console to be used. Defaults to 80.
# palette : Sets mapping of RGB colors scheme to system colors. 
# Options are : [“default”, “xterm”, “linuxconsole”, “solarized”, “rxvt”, “tango”, “gruvbox”, “gruvboxdark”]. Default is “default”.
import climage

def print_image_climage(image_path):
    # print('print_image_climage')
    # inform of ANSI Escape codes
    output = climage.convert(image_path)
    # converts the image to print in terminal
    # with 8 color encoding and palette tango
    try:
        output = climage.convert(image_path,
            is_truecolor=True,
            # is_256color=True,
            # is_8color=True,
            palette='tango',
        )
    except:
        output = climage.convert(image_path,
            # is_truecolor=True,
            is_256color=True,
            # is_8color=True,
            palette='tango',
        )
    # prints output on console.
    print(output)


# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     # gambar = 'C:/fr/belum-coded/malu-manis01.jpg'
#     gambar = 'C:/fr/belum-coded/love-samping01.jpg'
#     if len(sys.argv)==2 and sys.argv[1]:
#         gambar = sys.argv[1]
#     w = ImageView(image=gambar, background=Qt.black, quit_mode=True)
#     w.show()
#     sys.exit(app.exec_())

if __name__ == '__main__':
    # draw1()
  	# draw2()
    print_image_climage('pic1.png')
