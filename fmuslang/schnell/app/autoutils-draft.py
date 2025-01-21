# https://python.plainenglish.io/10-python-automation-scripts-for-everyday-problems-3ca0f2011282
# https://python.plainenglish.io/10-automation-scripts-for-your-daily-python-projects-892a82be3f75
# Excellent. I would expand on pandas. 
# Reading Excel is great. But what if you have to make 5, 10, 50 Excel workbooks? 
# pd.ExcelWriter to the rescue! 
# You can explain how to loop through your dataset and create an instance of writer, workbook, possibly workbook.add_worksheet 
# (or df.to_excel() etc), save and close. 
# How to use this? product marketing and sales report, sales person report, automate internal purchas orders, customer reports, department reports.... 
# If you have groups of things that need individual reports you can use this. 
# Couple it with an emailer function and you can automate sending them out when the python code has everything ironed out.

# 10 Python Automation Scripts for Everyday Problems
# 👉 Photo Editing

# Edit your photos with this awesome automation script that uses the Pillow module. 
# Below I made a list of image editing functions that you can use in your Python project or solve any daily life problem.
# This script is a handful of snippet codes for programmers who need to programmatically edit their images.

# Photo Editing 
# pip install pillow
from PIL import Image, ImageFilter
# Resize an image
img = Image.open('img.jpg')
resize = img.resize((200, 300))
resize.save('output.jpg')

# Blur Image
img = Image.open('img.jpg')
blur = img.filter(ImageFilter.BLUR)
blur.save('output.jpg')

# Sharp Image
img = Image.open('img.jpg')
sharp = img.filter(ImageFilter.SHARPEN)
sharp.save('output.jpg')

# Crop Image
img = Image.open('img.jpg')
crop = img.crop((0, 0, 50, 50))
crop.save('output.jpg')

# Rotate Image
img = Image.open('img.jpg')
rotate = img.rotate(90)
rotate.save('output.jpg')

# Flip Image
img = Image.open('img.jpg')
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('output.jpg')

# Transpose Image
img = Image.open('img.jpg')
transpose = img.transpose(Image.TRANSPOSE)
transpose.save('output.jpg')

# Convert Image to GreyScale
img = Image.open('img.jpg')
convert = img.convert('L')
convert.save('output.jpg')

# 👉 PDF Watermarker
# This automation script will simply help you Watermark your PDF page by page. 
# This script uses the PyPDF4 module to read and add watermark. 
# Check out the code below:

# Watermark PDF files
# pip install PyPDF4
import PyPDF4
def Watermark():
	pdf_file= "test.pdf"
	output_pdf= "output.pdf"
	watermark= "watermark.pdf"
	watermark_read = PyPDF4.PdfFileReader(watermark)
	watermark_page = watermark_read.getPage(0)
	pdf_reader = PyPDF4.PdfFileReader(pdf_file)
	pdf_writer = PyPDF4.PdfFileWriter()
	for page in range(pdf_reader.getNumPages()):
		page = pdf_reader.getPage(page)
		page.mergePage(watermark_page)
		pdf_writer.addPage(page)

	# writing output pdf file
	with open(output_pdf, 'wb') as pdf:
		pdf_writer.write(pdf)

Watermark()


# WaterMark Your Photos
# pip install Pillow
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
def Apply_Watermark(input, output, text):
	image = Image.open(input)
	font = ImageFont.truetype("arial.ttf", 120)
	w, h = image.size
	draw = ImageDraw.Draw(image)
	
	text_w, text_h = draw.textsize(text, font)   
	pos = w - text_w, (h - text_h) - 50
	watermark_text = Image.new('RGB', (text_w, (text_h)))
	draw = ImageDraw.Draw(watermark_text)
	
	draw.text((0,0), text, font=font)
	watermark_text.putalpha(100)
   
	image.paste(watermark_text, pos, watermark_text)
	image.save(output)

Apply_Watermark('img.jpg', 'watermark.jpg', 'WaterMark')


# 👉 Video Editing
# Now edit your video programmatically with this automation script. 
# It uses the Moviepy module to edit the video. 
# The below script is a handy bit of code to trim videos, add VFX and add audio to specific parts of the video. 
# You can explore the Moviepy more for further functions.

# Video Editing
# pip install moviepy
from moviepy.editor import *
# Triming the video
clip_1 = VideoFileClip("sample_video.mp4").subclip(40, 50)
clip_2 = VideoFileClip("sample_video.mp4").subclip(68, 91)
final_clip = concatenate_videoclips([clip_1, clip_2])
final_clip.write_videofile("output.mp4")

# Adding VFX
clip_1 = (VideoFileClip("sample_video.mp4").subclip(40, 50).fx(vfx.colorx, 1.2).fx(vfx.lum_contrast, 0, 30, 100))
clip_2 = (VideoFileClip("sample_video.mp4").subclip(68, 91).fx(vfx.invert_colors))
final_clip = concatenate_videoclips([clip_1, clip_2])
final_clip.write_videofile("output.mp4")

# Add Audio to Video
clip = VideoFileClip("sample_video.mp4")
# Add audio to only first 5 sec
clip = clip.subclip(0, 5)
audioclip = AudioFileClip("audio.mp3").subclip(0, 5)
videoclip = clip.set_audio(audioclip)
final_clip.write_videofile("output.mp4")

# 👉 Speech to Text AI
# You saw my code about converting Text to Speech But do you know we can convert speech to text in Python too. 
# This awesome code will show you how to do it. Check the code below:

# Convert Speech to Text
#pip install SpeechRecognition
import speech_recognition as sr
def SpeechToText():
	Ai = sr.Recognizer()
	with sr.Microphone() as source:
		listening = Ai.listen(source, phrase_time_limit = 6)  
	try:
		command = Ai.recognize_google(listening).lower()
		print("You said: " + command)
		
	except sr.UnknownValueError:
		print("Sorry Can't understand, Try again")
		SpeechToText()

# 👉 Request API
# Need to call an API request then try the below script. 
# The script uses the Beautiful request module that can get/post data on any API call. 
# The below code has two parts one is getting the HTML source code and the second is logging in to the site.

# Request Api 
# pip install requests
import requests
# Get Data
headers = {
	"Connection": "keep-alive",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
r = requests.get('https://api.example.com', headers=headers)
print(r.status_code) # 200
print(r.headers['content-type'])
print(r.content) # HTML Data
# Login Site
payload = {'username': 'USERNAME', 'userpass': 'PASSWORD'}
r = requests.post('https://example.com/login', data=payload)
print(r.status_code) # 200

# 👉 Python GUI
# This script will let you a hand to create Graphical User-Interface Python programs. 
# It uses the latest PyQt6 module and I coded most of the important widgets below:

# Python GUI
# pip install PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit
def Application():
	app = QApplication(sys.argv)
	win = QWidget()
	win.resize(300, 300)
	win.move(200, 200)
	win.setWindowTitle('Medium Article')
	# Create Buttons
	btn = QPushButton('Quit', win)
	# Message Box
	QMessageBox.question(win, 'Message',"Are you sure to quit?")
	# Label Text
	lbl = QLabel('Hello World', win)
	# Button Clicked
	btn.clicked.connect(lambda: QMessageBox.question(win, 'Message',"Are you sure to quit?"))
	# Entry Box
	entry = QLineEdit(win)win.show()
	sys.exit(app.exec())
if __name__ == '__main__':
	Application()

# 👉 Spell Checker
# Have a lot of documents and huge text and if you want to check the spelling then this Python script will help you solve your problem. 
# It uses the Pyspellchecker module to check spells and give correction suggestions.

# Spell Checker in Python 
# pip install pyspellchecker
from spellchecker import SpellChecker as spell
Words = spell.unknown(['Python'  , 'is' , 'a' , 'good' , 'lantyguage'])
for w in Words:
	print(spell.correction(w)) #language
	print(spell.candidates(w)) #{ language }

# 👉 Grammar Checker

# Inspired by Grammarly then why not try to create your own grammar checker in Python. 
# The below script will help you check your grammar it uses the Gingerit module which is an API-based module.

# Grammer Checker in Python
# pip install gingerit
from gingerit.gingerit import GingerIt
text = "Welcm Progammer to Python"
Grammer = GingerIt()
Correction = Grammer.parse(text)
print(Correction["result"]) # Welcome, Programmer to Python
print(Correction['corrections'])


# Spell and Grammer Checker
# pip install textblob
# pip install language-tool-python
from textblob import TextBlob
import language_tool_python
# Spell Checker
def spell_checker(text):
	text = TextBlob(text)
	print(text.correct())
# Grammer Checker
def grammer_checker(text):
	tool = language_tool_python.LanguageTool('en-US')
	checker = tool.check(text)
	print("Issue: ", checker[0].ruleIssueType)
	print("Corrected Text:", checker[0].replacements)
grammer_checker("I Stackoverflow love")
spell_checker("The Smell of Fliwers")

# 👉 Automate Win, Mac, and Linux
# We have automated web apps and smartphones then why not the Operating Systems. 
# This automation script will automate Win, Mac, and Linux using the PyautoGui module in Python. 

# Automate Win, Mac and Linux
# pip install PyAutoGUI
import pyautogui as py

# Mouse Movements
py.moveTo(100, 100)
py.moveTo(200, 200, duration=1)
py.click(100, 100)
py.doubleClick(200, 200)

# Keyboard Inputs
py.write('Hello World!', interval=0.25)
py.press('enter')
py.hotkey('ctrl', 'c')
py.keyDown('shift')
py.keyUp('shift')

# Screen Automation
img = py.screenshot('screenshot.jpg')
img.save('screenshot.jpg')

loc = py.locationsOnScreen('icon.jpg')
print(loc)

# 👉 Read Excel
# You probably use Pandas for reading CSV files but do you know you can read excel files too. 
# Take a look at the following script to know how it works:
# Read Excel
# pip install pandas
import pandas as pd
df = pd.read_excel('test.xlsx', sheet_name='Sheet1')
# Read Columns
name = df['Name'].to_list()
Id  = df['Id'].to_list()
print(name) # ["haider", "Dustin, "Tadashi"]
print(Id) # [245, 552, 892]

# Generate and Decode QrCode
# pip install qrcode
# pip install qrtools
# pip install Pillow
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def generate_qrcode(data):
	qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
	qr.add_data(data)
	qr.make(fit=True)
	image = qr.make_image(fill_color="black", back_color="white")
	image.save("qrcode.png")

def Decode_Qrcode(file_name):
	result = decode(Image.open(file_name))
	print("Data:", result[0][0].decode())

generate_qrcode("This is Medium Article By Haider")
Decode_Qrcode("qrcode.png")

# Read Excel Files
# pip install openpyxl



# urllib3
# pip install urllib3
import urllib3
import urllib.request
# Get HTML or API Call
r = urllib3.PoolManager()
response = r.request('GET', 'http://www.example.com')
print(response.status)
print(response.data)
# Mutliple API Call
r = urllib3.PoolManager(num_pools=2)
response1 = r.request('GET', 'http://www.example1.com')
response2 = r.request('GET', 'http://www.example2.com')
# Download Images/videos and Files
r = urllib.request.urlretrieve("video url", 'video_name.mp4')



# 👉Recognize Handwriting
# Did you ever imagine your computer can recognize your handwriting? 
# This amazing automation script will help you to do so. 
# It uses the Pytesseract module to detect and recognize the handwriting using a machine learning support in the backend.

# Recognized Handwritting
# pip install pytesseract
import pytesseract
from PIL import Image
# Recognize Handwritting
img  = Image.open('test.png')
text = pytesseract.image_to_string(img)
print(text)
# Recognize by Language
pytesseract.image_to_string(img, lang='spa')
# config for Detection
text = pytesseract.image_to_string(img,  lang='eng',  config='--psm 6')
# Page segmentation modes (--psm num):
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR.
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.



# 👉Automate Websites and WebApps
# We have automated Windows and mobile phones then why not web and web apps. 
# This awesome script will help you to do it by using the Selenium module. 
# Below I mention the example code with most of the useful functions need in web automation.

# Automate WebApps 
# pip install Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.example.com/")
# Finding Elements
driver.find_element_by_id("id")
driver.find_element_by_name("name")
driver.find_element_by_class_name("class name")
driver.find_element_by_tag_name("tag")
driver.find_element_by_link_text("link text")
driver.find_element_by_xpath("xpath")
driver.find_element_by_css_selector("css")
# Finding Elements with Wait
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id")))
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "xpath")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id")))
# Click on Element
driver.find_element_by_id("id").click()
# Send keys or Type
driver.find_element_by_id("id").send_keys("Keys")
# Press Enter or Keys
driver.find_element_by_id("id").send_keys(Keys.ENTER)
# Mouse Hover
ActionChains(driver).move_to_element(driver.find_element_by_id("id")).perform()

# # Quit Browser
# driver.quit()
# # Refresh Browser
# driver.refresh()

# 👉Python GUI with Tkinter
# This automation script will be handy for you to create GUI programs in Python using the Tkinter module. 
# Below example code is a complete handmade tool for Gui maker in Python check out the code now.

#Python GUI with Tkinter
import tkinter as tk
root = tk.Tk()
root.title("Medium Article")
# Button
btn = tk.Button(root, text="Click Me!", command=lambda: print("Welcome Pythoneer!"))
btn.pack()
# Entry
entry = tk.Entry(root)
entry.pack()
# Label
label = tk.Label(root, text="Medium")
label.pack()
# Text
text = tk.Text(root, height=2, width=30)
text.pack()
# Listbox
listbox = tk.Listbox(root, height=2, width=30)
listbox.pack()
# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# messagebox
tk.messagebox.showinfo("Title", "Your Message")
# Radio Button
var = tk.IntVar()
radio = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
radio.pack()
radio = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
radio.pack()
# Check Button
var = tk.IntVar()
check = tk.Checkbutton(root, text="Option 1", variable=var)
check.pack()
check = tk.Checkbutton(root, text="Option 2", variable=var)
check.pack()
# Dropdown
var = tk.StringVar()
dropdown = tk.OptionMenu(root, var, "Option 1", "Option 2", "Option 3")
dropdown.pack()
# Status Bar
status = tk.Label(root, text="Preparing to do Something...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)
# File Input
def open_file():
	file = tk.filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
	if file != None:
		contents = file.read()
		file.close()
		text.insert(tk.END, contents)
# Folder Input
def folder():
	folder = tk.filedialog.askdirectory(parent=root, title='Select a folder')
	label.config(text=folder)

root.mainloop()
# 👉Multi-Processing
# Do you need to run your program or python project run parallel at the same time then this script will be handy for you? 
# It uses a Multiprocessing module that let you run different functions in the same timeframe. 
# This automation script is handy for leveraging the processing time.

# Multi-processing
import multiprocessing
def worker(num):
	print('Worker:', num)
if __name__ == '__main__':
	jobs = []
	for i in range(5):
		p = multiprocessing.Process(target=worker, args=(i,))
		jobs.append(p)
		p.start()
	for i in jobs:
		i.join()
print('Done')


# https://python.plainenglish.io/10-killer-automation-scripts-for-your-python-projects-61284d265844
# 👉 Photo Compressor
# This is an awesome Automation Script that will Compress your Photos into lower Sizes by keeping the Quality the same.

import PIL
from tkinter.filedialog import *
from PIL import Image
file_loc=askopenfilenames()
img = Image.open(file_loc[0])
img.save("Compressed.jpg", "JPEG", optimize = True, quality = 10)
print("Image is Compressed")
# 👉Image Watermarker
# You had Probbally used different Photo Editing software to watermark your photos. This simple python script using the PIL module will watermark any image. You can set the Text, location, and even Font.

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
def watermark_Image(img_path,output_path, text, pos):
	img = Image.open(img_path)
	drawing = ImageDraw.Draw(img)
	black = (10, 5, 12)
	drawing.text(pos, text, fill=black)
	img.show()
	img.save(output_path)
img = '1.jpg'
watermark_Image(img, 'watermarked.jpg','Python', pos=(0, 0))
# 👉 InstaDpViewer
# This Python automation script will help you to view the DP of any Instagram User. Script use module instaloader which will take username as input and download the DP as an output.

#pip install instaloader
import instaloader
 
ig = instaloader.Instaloader()
DP = input("Enter Insta username : ")
 
ig.download_profile(dp , profile_pic_only=True)
print("Your Image is Downloaded")
# 👉 Plagiarism Checker
# This is an awesome script that will help you to check the Plagiarism between two files. Now you don’t longer need any software or a web app for Plagiarism checking. This will do your work in a second.

from difflib import SequenceMatcher
def Plagerism_checker(f1, f2):
	with open(f1,errors="ignore") as file1,open(f2,errors="ignore") as file2:
		f1_data=file1.read()
		f2_data=file2.read()
		checking=SequenceMatcher(None, f1_data, f2_data).ratio()
		print(f"These files are {checking*100} % similar")
file_1=input("Enter file 1 path: ")
file_2=input("Enter file 2 path: ")
Plagerism_checker(file_1, file_2)
# 👉 YT Video Downloader
# This is another simple automation script to download Youtube videos. Now you don’t need any web app or software, just use the below code to download any video.

# pip install pytube
import pytube
link = input('Enter Youtube Video URL')
yt = pytube.Youtube(link)
yt.streams.first().download()
print('downloaded', link)

# 👉 Convert PDF to CSV
# Sometimes we need to convert our PDF data into CSV format, So for that kind of work, this Python script will be handy for you. I had mentioned the two methods to do this work.

import tabula
import camelot
# Method 1
filename = input("Enter File Path: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')
df.to_csv('output.csv')
# Method 2
tables = camelot.read_pdf('file.pdf')
tables.export('file.csv', f='csv', compress=True)

# 👉 File Encrypt and Decrypt
# Want to lock your File then this script will be handy for you. Below I mention Encryption and decryption code that can work on any file.

# pip install cryptography
from cryptography.fernet import Fernet
def encrypt(filename, key):
	fernet = Fernet(key)
	
	with open(filename, 'rb') as file:
		original = file.read()
		
	encrypted = fernet.encrypt(original)
	
	with open(filename, 'wb') as enc_file:
		enc_file.write(encrypted)
def decrypt(filename, key):
	fernet = Fernet(key)
	with open(filename, 'rb') as enc_file:
		encrypted = enc_file.read()
		decrypted = fernet.decrypt(encrypted)
	with open(filename, 'wb') as dec_file:
		dec_file.write(decrypted)
# Generate Key
key = Fernet.generate_key()
filename = input("Enter Your filename: ")
encrypt(filename, key)
decrypt(filename, key)
# 👉 Battery Notification
# You had seen a battery notification on your Mobile Phone. So what if your Laptop also notifies you about your Battery status. This Python Script will do the exact same work by using 3 modules it can be Battery Notifier. Check out the code below.

# pip install win10toast
# pip install pywin32
# pip install pyttsx3
import psutil
import time
import pyttsx3
import threading
from win10toast import ToastNotifier
bot=pyttsx3.init()
bot.setProperty('rate',110)
bot.setProperty('volume',3)
toaster = ToastNotifier()

def display_notification(text):
	toaster.show_toast(text, duration=8)
	while toaster.notification_active():
		time.sleep(0.003)

def Battery_Notification():
	while (True):
		time.sleep(2)
		battery = psutil.sensors_battery()
		plugged = battery.power_plugged
		percent = int(battery.percent)
		if percent < 15:
			if plugged == False:
				processThread = threading.Thread(target=display_notification, args=("Your Battery at "+str(percent)+"% Please Plug the charger",))
				processThread.start()
				bot.say("Your battery is getting low so plug your charger")
				bot.runAndWait()
		elif percent >= 99:
			if plugged == True:
				processThread = threading.Thread(target=display_notification, args=("Charging is getting complete",))
				processThread.start()
				bot.say("Charging is Completed")
				bot.runAndWait()
		# elif percent >= 99:
		# 	if plugged == True:
		# 		processThread = threading.Thread(target=display_notification, args=("Charging is getting complete",))
		# 		processThread.start()
		# 		bot.say("Charging is Completed")
		# 		bot.runAndWait()
Battery_Notification()

# 👉 Convert Images to PDF
# If you had a lot of images and looking for converting them into a single Pdf then this automation script will be handy for you.

import os
import img2pdf
#Method 1
with open("Output.pdf", "wb") as file:
	file.write(img2pdf.convert([i for i in os.listdir('Path of image_Directory') if i.endswith(".jpg")]))
#Method 2
from fpdf import FPDF
Pdf = FPDF()
list_of_images = ["1.jpg", "2.jpg"]
for i in list_of_images: # list of images with filename
	Pdf.add_page()
	Pdf.image(i,x,y,w,h)
Pdf.output("yourfile.pdf", "F")

# 👉 Text to Speech AI Bot
# If you had known about the Jarvis AI then this script will work similarly.
# It uses google Text to Speech API to convert your written Text to AI bot voice.
# checkout the code below.

# pip install gTTS
from pygame import mixer
from gtts import gTTS

def main():
  tts = gTTS('Learn Python from Medium')
  tts.save('python.mp3')
  mixer.init()
  mixer.music.load('python.mp3')
  mixer.music.play()
  
if __name__ == "__main__":
  main()

# 
# https://python.plainenglish.io/20-extremely-useful-python-one-liners-you-must-know-6c5f3d9c875a
