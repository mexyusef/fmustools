# https://www.thepythoncode.com/article/optical-character-recognition-pytesseract-python
# pip install pytesseract
# pip install numpy matplotlib opencv-python pillow

# pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH.
# See README file for more information.
# https://github.com/UB-Mannheim/tesseract/wiki (binary)
# https://github.com/tesseract-ocr/tesseract/releases (source)
# https://cygwin.com/cgi-bin2/package-grep.cgi?grep=tesseract&arch=x86_64

"""
https://stackoverflow.com/questions/49101270/move-to-searched-text-on-active-screen-with-pyautogui

Yes, you can do that, but you additionally need Tesseract (and the Python-module pytesseract) for text recognition and PIL for taking screenshots.

Then perform the following steps:

    Open the page
    Open and perform the search (ctrl+f with pyautogui) - the view changes to the first result
    Take a screenshot (with PIL)
    Convert the image to text and data (with Tesseract) and find the text and the position
    Use pyautogui to move the mouse and click on it

Here is the needed code for getting the image and the related data:

import time
from PIL import ImageGrab  # screenshot

import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = (r"C:\...\AppData\Local\Programs\Tesseract-OCR\tesseract") # needed for Windows as OS

screen =  ImageGrab.grab()  # screenshot
cap = screen.convert('L')   # make grayscale

data=pytesseract.image_to_boxes(cap,output_type=Output.DICT)

print(data)

In data you find all required information you need to move the mouse and click on the text.

The downside of this approach is the ressource consuming OCR part which takes a few seconds on slower machines.

https://stackoverflow.com/questions/60413634/is-there-a-possibility-to-select-text-by-mouse-double-click-and-drag-the-selecte
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("your site")

source = driver.find_element_by_xpath('your element to drag')
destination = driver.find_element_by_xpath('element to drag to')

ActionChains(driver).drag_and_drop(source= source, target= destination).perform()

https://stackoverflow.com/questions/74282908/pyautogui-scroll-and-dragto-are-inconsistent-depending-on-the-size-of-the-scroll
"""

import cv2
import datetime
import os
import time
import pytesseract
from PIL import Image

from schnell.app.autoutils import alert
from schnell.app.mediautils import capture_gambar
from schnell.app.dirutils import (
  joiner,
  isfile,
  ayah,
  here,
  normy,
)
from schnell.app.envvalues import datadir_
from schnell.app.printutils import indah3, indah4
from schnell.app.fileutils import file_append, file_remove
from schnell.app.utils import env_get, env_exist
from schnell.app.datetimeutils import timestamp_for_file


def image_cv2(filepath):
    return cv2.imread(filepath)


def image_pil(filepath):
    return Image.open(filepath)


def pil_image(filepath):
    return Image.open(filepath)


def image_to_string(pil_image):
    res = pytesseract.image_to_string(pil_image)
    return res


i2s = image_to_string
DATADIR = r'C:\Users\usef\Desktop\Screenshots\ocr-data'


def surround_text(pil_image, text):
    """
    https://www.thepythoncode.com/article/optical-character-recognition-pytesseract-python
    """
    import matplotlib.pyplot as plt
    
    # make a copy of this image to draw in
    image_copy = pil_image.copy()
    # the target word to search for
    target_word = text
    # get all data from the image
    data = pytesseract.image_to_data(pil_image, output_type=pytesseract.Output.DICT)
    # get all occurences of the that word
    word_occurences = [ i for i, word in enumerate(data["text"]) if word.lower() == target_word ]
    for occ in word_occurences:
        # extract the width, height, top and left position for that detected word
        w = data["width"][occ]
        h = data["height"][occ]
        l = data["left"][occ]
        t = data["top"][occ]
        # define all the surrounding box points
        p1 = (l, t)
        p2 = (l + w, t)
        p3 = (l + w, t + h)
        p4 = (l, t + h)
        # draw the 4 lines (rectangular)
        image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=2)
        image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=2)
        image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=2)
        image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=2)
    plt.imsave("all_dog_words.png", image_copy)
    plt.imshow(image_copy)
    plt.show()


def capture_text(output_file=None, DATADIR=DATADIR):
    if not output_file:
        output_file = DATADIR + f"ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        output_file = normy(output_file)
    # ternyata gambar jadi menyatu...
    # hapus dulu sblm capture
    file_remove(output_file)
    print('[schnell.app.ocrutils][capture_text] saved screenshot:', output_file)
    # sblm capture, kita minimize dulu current window (misal repl terminal)
    # minimize_current_window()
    # err not working...
    capture_gambar(output_file)
    return output_file


def ocr_screenshot(output_file=None, DATADIR=DATADIR, delay=1.0):
    # filepath = capture_text(output_file)
    if not DATADIR:
        if env_exist('ULIBPY_MEMO_DATADIR'):
            DATADIR = env_get('ULIBPY_MEMO_DATADIR')
        else:
            DATADIR = os.getcwd()
    if not isinstance(delay, float):
        delay = float(delay)
    if not output_file:
        output_file = DATADIR + f"ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        output_file = normy(output_file)
    # ternyata gambar jadi menyatu...
    # hapus dulu sblm capture
    file_remove(output_file)
    indah4(f"""[schnell.app.ocrutils][ocr_screenshot] saved screenshot
    output_file = {output_file}
    DATADIR = {DATADIR}
    delay = {delay}""", warna='magenta')
    # sblm capture, kita minimize dulu current window (misal repl terminal)
    # minimize_current_window()
    # err not working...
    capture_gambar(output_file)

    filepath = output_file

    time.sleep(delay)  # kasih waktu dari capture ke ekstrak teks

    result = 'NO CAPTURE'
    if isfile(filepath):
        img = image_cv2(filepath)
        result = image_to_string(img)
        indah4('='*40 + ' ' + output_file, warna='green')
        indah3(result, warna='white')
        indah4('='*40, warna='green')
        ocrtext_filepath = joiner(DATADIR, 'ocr-data', 'ocr.txt')
        file_append(ocrtext_filepath, f"\n{timestamp_for_file()}\n{result}\n")
    else:
        alert(f'No file {filepath}', 'OCR')

    return result


def copy_image_to_clipboard(output_file):
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QClipboard, QImage
    print('[schnell.app.ocrutils][copy_image_to_clipboard] copying...')
    with open(output_file, 'rb') as f:
        image_data = f.read()
    image = QImage.fromData(image_data)
    clipboard = QApplication.clipboard()
    clipboard.setImage(image)
    print('[schnell.app.ocrutils][copy_image_to_clipboard] clipboard copied')


def clipboard_screenshot(output_file=None, DATADIR=DATADIR, delay=1.0):
    from .clipboardutils import image_to_clipboard2
    if not output_file:
        output_file = DATADIR + f"ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        output_file = normy(output_file)
    # ternyata gambar jadi menyatu...
    # hapus dulu sblm capture
    file_remove(output_file)
    print('[schnell.app.ocrutils][clipboard_screenshot] saved screenshot:', output_file)
    # sblm capture, kita minimize dulu current window (misal repl terminal)
    # minimize_current_window()
    # err not working...
    capture_gambar(output_file)
    print('[schnell.app.ocrutils][clipboard_screenshot] saving...')
    time.sleep(delay)  # kasih waktu dari capture ke ekstrak teks
    print('[schnell.app.ocrutils][clipboard_screenshot] really saving...')
    image_to_clipboard2(output_file)
    print('[schnell.app.ocrutils][clipboard_screenshot] clipboard copied')


def clipboard_screenshot2(output_file=None, DATADIR=DATADIR, delay=1.0):
    from PIL import ImageGrab
    import win32clipboard
    import pyperclip, io
    if not output_file:
        output_file = DATADIR + f"ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        output_file = normy(output_file)
    # ternyata gambar jadi menyatu...
    # hapus dulu sblm capture
    file_remove(output_file)
    print('[schnell.app.ocrutils][clipboard_screenshot2] saved screenshot:', output_file)

    capture_gambar(output_file)
    time.sleep(delay)
    # # Grab the image
    # image = ImageGrab.grab()

    # # Convert the image to a format that can be copied to the clipboard (e.g. BMP)
    # image.convert('RGB').save('temp.bmp')

    # # Open the temporary file and read its contents
    # with open('temp.bmp', 'rb') as f:
    #     data = f.read()

    # # Copy the image data to the clipboard
    # win32clipboard.OpenClipboard()
    # win32clipboard.EmptyClipboard()
    # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    # win32clipboard.CloseClipboard()
    print('[schnell.app.ocrutils][clipboard_screenshot2] copying...')

    # with open(output_file, 'rb') as image_file:
    #     image_data = image_file.read()
    #     pyperclip.copy(image_data)

    with Image.open(output_file) as image:
        with io.BytesIO() as output:
            image.convert('RGB').save(output, format='BMP')
            data = output.getvalue()[14:]
            pyperclip.copy(data)
    print('[schnell.app.ocrutils][clipboard_screenshot2] clipboard copied')


def clipboard_screenshot3(output_file=None, DATADIR=DATADIR, delay=1.0):
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QClipboard, QImage

    if not output_file:
        output_file = DATADIR + f"ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        output_file = normy(output_file)
    # ternyata gambar jadi menyatu...
    # hapus dulu sblm capture
    file_remove(output_file)
    print('[schnell.app.ocrutils][clipboard_screenshot3] saved screenshot:', output_file)

    capture_gambar(output_file)
    time.sleep(delay)
    # # Grab the image
    # image = ImageGrab.grab()

    # # Convert the image to a format that can be copied to the clipboard (e.g. BMP)
    # image.convert('RGB').save('temp.bmp')

    # # Open the temporary file and read its contents
    # with open('temp.bmp', 'rb') as f:
    #     data = f.read()

    # # Copy the image data to the clipboard
    # win32clipboard.OpenClipboard()
    # win32clipboard.EmptyClipboard()
    # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    # win32clipboard.CloseClipboard()
    print('[schnell.app.ocrutils][clipboard_screenshot3] copying...')

    with open(output_file, 'rb') as f:
        image_data = f.read()

    image = QImage.fromData(image_data)

    clipboard = QApplication.clipboard()
    clipboard.setImage(image)

    print('[schnell.app.ocrutils][clipboard_screenshot3] clipboard copied')


def take_screenshot(output_file=None, output_dir=None):
    # kita bisa:
    # take_screenshot(None, r'c:\tmp')
    if not output_file:  # gak kasih filename, maka generate filename
        if not output_dir:  # jk tdk specify dirname, baru simpan di default folder
            output_dir = DATADIR
        # else: simpan generated filename di specified dirname
        output_file = os.path.join(output_dir, f"ss_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        output_file = normy(output_file)
    elif output_dir:  # jk kasih filename+dirname, gunakan
        output_file = os.path.join(output_dir, output_file)
        output_file = normy(output_file)
    # else: hanya filename, simpan di cwd

    # ternyata gambar jadi menyatu, hrs hapus dulu sblm capture
    file_remove(output_file)
    print('[schnell.app.ocrutils][take_screenshot] saved to', output_file)
    capture_gambar(output_file)
    return output_file
