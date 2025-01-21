import tkinter as tk
import sys
from os.path import abspath
from PIL import Image, ImageTk, ImageGrab


class ScreenCapture(tk.Tk):
    def __init__(self, filename='screenshot.png'):
        super().__init__()

        self.filename = abspath(filename)
        self.img = None

        # Capture the entire screen, including all monitors
        image = ImageGrab.grab(all_screens=True)
        self.image = ImageTk.PhotoImage(image, master=self)
        
        # Get the screen width and height for full-screen mode
        screen_width = self.image.width()
        screen_height = self.image.height()

        self.withdraw()
        self.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height)
        self.canvas.pack(fill="both", expand=True)

        self.photo = self.canvas.create_image(0, 0, image=self.image, anchor="nw")

        self.x, self.y = 0, 0
        self.rect, self.start_x, self.start_y = None, None, None
        self.deiconify()

        self.canvas.tag_bind(self.photo, "<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.photo, "<B1-Motion>", self.on_move_press)
        self.canvas.tag_bind(self.photo, "<ButtonRelease-1>", self.on_button_release)

        self.stay_on_top()

    def stay_on_top(self):
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
        img = ImageGrab.grab(bbox)
        img.save(self.filename, "PNG")
        self.img = img.copy()
        img.close()

        self.canvas.destroy()
        self.quit()

    def get_image(self):
        assert self.img is not None, "No image captured"
        return self.img

# import tkinter as tk
# import sys
# from os.path import abspath

# try:
#     from PIL import Image, ImageTk, ImageGrab
# except ImportError as ie:
#     pass

# class ScreenCapture(tk.Tk):
#     def __init__(self, filename='screenshot.png'):
#         super().__init__()

#         self.filename = abspath(filename)
#         self.img = None

#         self.withdraw()
#         self.attributes('-fullscreen', True)

#         self.canvas = tk.Canvas(self)
#         self.canvas.pack(fill="both", expand=True)

#         image = ImageGrab.grab()
#         self.image = ImageTk.PhotoImage(image, master=self)
#         self.photo = self.canvas.create_image(0, 0, image=self.image, anchor="nw")

#         self.x, self.y = 0, 0
#         self.rect, self.start_x, self.start_y = None, None, None
#         self.deiconify()

#         self.canvas.tag_bind(self.photo, "<ButtonPress-1>", self.on_button_press)
#         self.canvas.tag_bind(self.photo, "<B1-Motion>", self.on_move_press)
#         self.canvas.tag_bind(self.photo, "<ButtonRelease-1>", self.on_button_release)

#         self.stay_on_top()

#     def stay_on_top(self):
#         self.lift()
#         self.after(2000, self.stay_on_top)

#     def on_button_press(self, event):
#         self.start_x = event.x
#         self.start_y = event.y
#         self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

#     def on_move_press(self, event):
#         curX, curY = (event.x, event.y)
#         self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

#     def on_button_release(self, event):
#         bbox = self.canvas.bbox(self.rect)
#         self.withdraw()
#         img = ImageGrab.grab(bbox)
#         img.save(self.filename, "PNG")
#         self.img = img.copy()
#         img.close()

#         self.canvas.destroy()
#         self.quit()

#     def get_image(self):
#         assert self.img is not None, "No image captured"
#         return self.img

# Usage:
# from this_module import ScreenCapture
# ScreenCapture(filename='screenshot.png').mainloop()
