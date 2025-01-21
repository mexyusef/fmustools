import datetime
import os
import time
import base64
import requests
import re
import cv2
import pytesseract
from PIL import Image
# https://gist.github.com/nealcaren/4ba5f2624baaf5e3ba8fa26e7486f74f
from openai import OpenAI
from typing import List, Union

from schnell.app.utils import env_get, env_exist, platform
from schnell.app.printutils import indah3, indah4
from schnell.app.dirutils import joiner, isfile, normy
from schnell.app.fileutils import file_append, file_remove
from schnell.app.datetimeutils import timestamp_for_file
from schnell.app.autoutils import alert
from schnell.app.screencapture import ScreenCapture
from schnell.app.screencaptureutils import ScreenCapture as ScreenCaptureNew
import os
import time
import datetime
import cv2
import pytesseract
from PIL import Image


from schnell.app.mediautils import capture_gambar
from schnell.app.fileutils import file_append, file_remove
from schnell.app.dirutils import joiner, isfile, ayah, here, normy


DATADIR = r"C:\Users\usef\Desktop\Screenshots\ocr-data"
LLM_IMAGE_DIR = r"C:\Users\usef\Desktop\Screenshots\llms-vscode"


def capture_and_copy_screenshot(
    output_file=None,
    datadir=None,
    delay=1.0
    ):
    """
    Capture a screenshot, save it to a file, and copy it to the clipboard.
    
    Args:
        output_file (str): Path to save the screenshot. Defaults to a timestamped file in `datadir`.
        datadir (str): Directory to save the screenshot. Defaults to LLM_IMAGE_DIR.
        delay (float): Delay in seconds after capturing the screenshot. Defaults to 1.0.
    """
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QClipboard, QImage
    
    app = QApplication([])

    if not datadir:
        datadir = LLM_IMAGE_DIR
    if not output_file:
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(datadir, f"ocr_{timestamp}.png")
        output_file = os.path.normpath(output_file)
    # print('capture_and_copy_screenshot #2')
    os.makedirs(datadir, exist_ok=True)
    file_remove(output_file)
    indah4('[schnell.app.ocrutils][capture_and_copy_screenshot] Screenshot will be saved to: '+output_file)
    capture_gambar(output_file)
    time.sleep(delay)
    # # print('capture_and_copy_screenshot #3')
    # # indah4('[schnell.app.ocrutils_new][capture_and_copy_screenshot] Screenshot captured. Copying to clipboard...')
    # image = Image.open(output_file)
    # byte_array = image.tobytes("raw", "RGBA")
    # qimage = QImage(byte_array, image.width, image.height, QImage.Format_ARGB32)
    # try:
    #     app = QApplication.instance() or QApplication([])
    #     clipboard = app.clipboard()
    #     clipboard.setImage(qimage)
    #     indah4('[schnell.app.ocrutils_new][capture_and_copy_screenshot] Screenshot copied to clipboard successfully.')
    # except Exception as err:
    #     indah4(str(err), warna='red')
    #     import traceback
    #     traceback.format_exc()

    # filepath = output_file

    # time.sleep(delay)  # kasih waktu dari capture ke ekstrak teks

    print('[schnell.app.ocrutils_new][capture_and_copy_screenshot] copying...')
    with open(output_file, 'rb') as f:
        image_data = f.read()
    # print('image_data=>', image_data)
    image = QImage.fromData(image_data)
    clipboard = QApplication.clipboard()  # NoneType
    if not clipboard:
        print('GAGAL buat clipboard = QApplication.clipboard()')
    clipboard.setImage(image)
    print('[schnell.app.ocrutils_new][capture_and_copy_screenshot] clipboard copied')

    app.quit()
    return output_file


def capture_screen(filename="screenshot.png"):
    # ScreenCapture(filename).mainloop()
    ScreenCaptureNew(filename).mainloop()


def capture_image(filepath, delay=1):
    filepath = normy(filepath)
    if platform() == "linux":
        capture_command = f"gnome-screenshot -a -d {delay} -f {filepath}"
        os.system(capture_command)
    else:
        capture_screen(filepath)


def read_image(filepath):
    return cv2.imread(filepath)


def extract_text_from_image(pil_image):
    return pytesseract.image_to_string(pil_image)


def old_ocr_by_tesseract(
    output_file=None, datadir=r"C:\Users\usef\Desktop\Screenshots\ocr-data", delay=1.0
):
    if not datadir:
        # if env_exist("ULIBPY_MEMO_DATADIR"):
        #     datadir = env_get("ULIBPY_MEMO_DATADIR")
        # else:
        datadir = os.getcwd()

    delay = float(delay)

    if not output_file:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = normy(os.path.join(datadir, f"ocr_{timestamp}.jpg"))

    file_remove(output_file)

    indah4(
        f"[schnell.app.ocrutils_new][ocr_by_tesseract] Saving screenshot\n"
        f"Output file: {output_file}\n"
        f"Data directory: {datadir}\n"
        f"Delay: {delay}",
        warna="magenta",
    )

    capture_image(output_file, delay)
    time.sleep(delay)  # Allow time for capture before extracting text

    if isfile(output_file):
        img = read_image(output_file)
        result = extract_text_from_image(img)
        indah4("=" * 40 + " " + output_file, warna="green")
        indah3(result, warna="white")
        indah4("=" * 40, warna="green")
        # ocr_text_file = joiner(datadir, "ocr-data", "ocr-new.txt")
        # file_append(ocr_text_file, f"\n{timestamp_for_file()}\n{result}\n")
    else:
        result = "NO CAPTURE"
        alert(f"No file {output_file}", "OCR")

    return result



# from schnell.app.ocrutils_new import screenshot_here
# #reflect#schnell.app.ocrutils_new/screenshot_here
def screenshot_here(output_file=None, datadir=None, delay=1.0):
    if not datadir:
        datadir = os.getcwd()

    delay = float(delay)

    if not output_file:
        now = datetime.datetime.now()
        timestamp = now.strftime("%d_%B_%Y_%H_%M_%S")
        # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.normpath(os.path.join(datadir, f"screenshot_{timestamp}.jpg"))

    file_remove(output_file)
    capture_image(output_file, delay)


def print_token_cost(response):
    c = (
        response.usage.completion_tokens * 0.03 / 1000
        + response.usage.prompt_tokens * 0.01 / 1000
    )
    formatted_c = "${:.2f}".format(c)
    print(f"Cost: {formatted_c}")


def is_url(s):
    # Regular expression for checking if it's a URL
    url_pattern = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ...or ipv4
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # ...or ipv6
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    # Check if the string is a URL
    if re.match(url_pattern, s):
        return True
    # Check if the string is a file
    elif os.path.isfile(s):
        return False


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


instructions = """
Your role is to take images of text from books, convert them into markdown format enclosed within a markdown code block, and list any corrections made during the process.
When presenting the markdown-formatted text, it should always use triple backticks (```) at the start and end to encase the markdown content in a code block.
It should use '*' for italics, '#' and '##' for headers, avoid smart quotes, and use '---' with a space on each side for em dashes.
Combine texts if split across multiple columns or images, especially if it splits a word, sentence or paragarph.
You should also correct any likely errors in the text, emphasizing accuracy in text recognition and markdown formatting, and being cautious about altering the original meaning of the text. 
If you encounter any words that are not clear due to the quality of the image, make a best guess and annotate it with a question mark in brackets [?]
When converting headlines in all caps, it should replace them with title case. 
Review your work carefully.
You should communicate in a helpful and precise manner, effectively meeting the user's needs for text conversion, error correction, and providing a summary of any corrections made.
"""

from schnell.app.llmutils.wrapper import GPT4VisionJyw
from schnell.app.llmutils.wrapper import GPT4OmniJyw


def old_ocr_by_openai(
    urls_or_filename,
    user_prompt="Transcribe this article into Markdown.",
    # model="gpt-4-vision-preview",
    # max_tokens=2500,
):
    # if type(urls_or_filename) == str:
    #     print("Processing one image.")
    #     image_locations = [urls_or_filename]
    # else:
    #     print(f"Processing {len(urls_or_filename)} images.")
    #     image_locations = urls_or_filename

    # user_message = [{"type": "text", "text": user_prompt}]

    # for image_location in image_locations:
    #     if is_url(image_location) == True:
    #         iu = image_location
    #     else:
    #         base64_image = encode_image(image_location)
    #         iu = f"data:image/jpeg;base64,{base64_image}"
    #     d = {"type": "image_url", "image_url": iu}
    #     user_message.append(d)

    if not urls_or_filename:
        datadir=r"C:\Users\usef\Desktop\Screenshots\ocr-data"
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = normy(os.path.join(datadir, f"ocr_{timestamp}.jpg"))
        file_remove(output_file)
        image_locations = [output_file]
    elif isinstance(urls_or_filename, str):
        print("Processing one image.")
        image_locations = [urls_or_filename]
    else:
        print(f"Processing {len(urls_or_filename)} images.")
        image_locations = urls_or_filename

    user_message = [{"type": "text", "text": user_prompt}]

    for image_location in image_locations:
        if is_url(image_location):
            image_url = image_location
        else:
            base64_image = encode_image(image_location)
            image_url = f"data:image/jpeg;base64,{base64_image}"
        image_message = {"type": "image_url", "image_url": image_url}
        user_message.append(image_message)

    # client = OpenAI(max_retries=3)
    # response = client.chat.completions.create(
    #     model=model,
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": instructions
    #         },
    #         {
    #             "role": "user",
    #             "content": user_message,
    #         },
    #     ],
    #     max_tokens=max_tokens,
    # )
    # print_token_cost(response)
    # return response.choices[0].message.content

    client = GPT4VisionJyw()
    return client.generate(instructions, user_message)

# md = ocr_by_openai(determination_url)
# print(md)

# from schnell.app.ocrutils_new import ocr_by_tesseract
def ocr_by_tesseract(output_file=None, datadir=r"C:\Users\usef\Desktop\Screenshots\ocr-data", delay=1.0):
    if not datadir:
        datadir = os.getcwd()

    delay = float(delay)

    if not output_file:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.normpath(os.path.join(datadir, f"ocr_{timestamp}.jpg"))

    file_remove(output_file)
    capture_image(output_file, delay)
    time.sleep(delay)  # Allow time for capture before extracting text

    if os.path.isfile(output_file):
        img = read_image(output_file)
        result = extract_text_from_image(img)
    else:
        result = "NO CAPTURE"

    return result


# from schnell.app.ocrutils_new import ocr_by_tesseract_from_file
# #reflect#schnell.app.ocrutils_new/ocr_by_tesseract_from_file/input_file=
# #reflect#schnell.app.ocrutils_new/ocr_by_tesseract_from_file/input_file=c:/users/usef/downloads/3js.jpg
def ocr_by_tesseract_from_file(input_file):
    # if not datadir:
    #     datadir = os.getcwd()
    # delay = float(delay)
    # if not output_file:
    #     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    #     output_file = os.path.normpath(os.path.join(datadir, f"ocr_{timestamp}.jpg"))
    # file_remove(output_file)
    # capture_image(output_file, delay)
    # time.sleep(delay)  # Allow time for capture before extracting text
    if os.path.isfile(input_file):
        img = read_image(input_file)
        result = extract_text_from_image(img)
    else:
        result = "NO CAPTURE"

    return result


# #reflect#schnell.app.ocrutils_new/test_ocr_by_tesseract_from_file/input_file=c:/users/usef/downloads/3js.jpg
def test_ocr_by_tesseract_from_file(input_file):
    result = ocr_by_tesseract_from_file(input_file)
    indah3(result)


# from schnell.app.ocrutils_new import ocr_by_openai
def ocr_by_openai(
    urls_or_filename: Union[str, List[str], None] = None,
    user_prompt: str = "Transcribe this article into Markdown.",
    system_message: str = instructions,
    gpt4vision_over_gpt4o = False,
):
    if not urls_or_filename:  # if file/url not given, use screen capture
        datadir = r"C:\Users\usef\Desktop\Screenshots\ocr-data"
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.normpath(os.path.join(datadir, f"ocr_{timestamp}.jpg"))
        file_remove(output_file)
        capture_image(output_file, 1.0)
        image_locations = [output_file]
    elif isinstance(urls_or_filename, str):  # filename
        image_locations = [urls_or_filename]
    else:  # list of urls
        image_locations = urls_or_filename

    user_message = [{"type": "text", "text": user_prompt}]

    for image_location in image_locations:
        if is_url(image_location):
            image_url = image_location
        else:
            base64_image = encode_image(image_location)
            image_url = f"data:image/jpeg;base64,{base64_image}"
        image_message = {"type": "image_url", "image_url": image_url}
        user_message.append(image_message)

    if gpt4vision_over_gpt4o:
        client = GPT4VisionJyw()  # Placeholder for actual OpenAI client instantiation
    else:
        client = GPT4OmniJyw()
    return client.generate(system_message, user_message)
