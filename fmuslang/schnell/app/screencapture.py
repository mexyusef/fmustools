import tkinter as tk
import sys
try:
	from PIL import (
		Image,
		ImageTk
	)
except ImportError as ie:
	pass

if sys.platform != 'linux':
	from PIL import ImageGrab

class ScreenCapture(tk.Tk):

	def __init__(self, filename = 'screenshot.png'):
		super().__init__()

		self.withdraw()
		self.attributes('-fullscreen', True)

		self.canvas = tk.Canvas(self)
		self.canvas.pack(fill="both",expand=True)

		self.filename = filename

		self.img = None
		image = ImageGrab.grab()
		# https://stackoverflow.com/questions/45668895/tkinter-tclerror-image-doesnt-exist
		# master = Tk()
		self.image = ImageTk.PhotoImage(image, master=self)
		self.photo = self.canvas.create_image(0, 0, image=self.image, anchor="nw")
		# https://stackoverflow.com/questions/45668895/tkinter-tclerror-image-doesnt-exist
		# self.photo.image = self.image

		self.x, self.y = 0, 0
		self.rect, self.start_x, self.start_y = None, None, None
		self.deiconify()

		self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press)
		self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press)
		self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release)

		self.stay_on_top()

	def stay_on_top(self):
		"""
		https://www.tutorialspoint.com/forcing-tkinter-window-to-stay-on-top-of-fullscreen-in-windows-10
		"""
		self.lift()
		self.after(2000, self.stay_on_top)

	def on_button_press(self, event):
		self.start_x = event.x
		self.start_y = event.y
		self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

	def on_move_press(self, event):
		curX, curY = (event.x, event.y)
		self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

	def on_button_release(self, event):
		bbox = self.canvas.bbox(self.rect)
		self.withdraw()
		# self.new_image = ImageTk.PhotoImage(ImageGrab.grab(bbox))
		# self.attributes('-fullscreen', False)
		# self.title("Image grabbed")
		# self.canvas.destroy()
		# self.deiconify()
		# tk.Label(self,image=self.new_image).pack()
		# langsung tulis ke file...abis itu OCR...

		# filepath = self.filename # kita bikin dah abspath agar sama dg versi linux
		# filepath = joiner(datadir, self.filename)
		# img = Image.open(self.new_image) # .convert('RGB')
		img = ImageGrab.grab(bbox)
		img.save(self.filename, "PNG")
		self.img = img.copy()
		img.close()

		self.canvas.destroy()
		# self.deiconify()

		self.quit()

	def get_image(self) -> Image:
		"""
		kembalikan self.img hasil ImageGrab.grab(bbox)
		"""
		assert self.img != None, "self.img == None"
		return self.img

"""
cara pake:
from schnell.app.screencapture import ScreenCapture
ScreenCapture(filename).mainloop()
"""
