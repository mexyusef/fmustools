# https://stackoverflow.com/questions/63737476/screenshot-on-multiple-monitor-setup-pyautogui

# import mss
# import cv2
# import numpy as np

# with mss.mss() as sct:
    
#     # Get information of monitor 2
#     monitor_number = 2
#     mon = sct.monitors[monitor_number]

#     # The screen part to capture
#     monitor = {
#         "top": mon["top"],
#         "left": mon["left"],
#         "width": mon["width"],
#         "height": mon["height"],
#         "mon": monitor_number,
#     }
#     output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

#     # Grab the data
#     sct_img = sct.grab(monitor)
#     img = np.array(sct.grab(monitor)) # BGR Image
    
#     # Display the picture
#     cv2.imshow("OpenCV", img)
#     cv2.waitKey(0)

# import tkinter as tk
# import mss
# import mss.tools

# class ScreenCaptureGUI(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         # Initialize mss instance
#         self.sct = mss.mss()

#         # Get information of monitor 2
#         self.monitor_number = 2
#         self.mon = self.sct.monitors[self.monitor_number]

#         # Create a canvas to display the monitor content
#         self.canvas = tk.Canvas(self, width=self.mon["width"], height=self.mon["height"])
#         self.canvas.pack()

#         # Bind mouse events
#         self.canvas.bind("<ButtonPress-1>", self.on_button_press)
#         self.canvas.bind("<B1-Motion>", self.on_move_press)
#         self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

#         # Variables to track selection
#         self.start_x = None
#         self.start_y = None
#         self.rect = None

#     def on_button_press(self, event):
#         self.start_x = event.x
#         self.start_y = event.y
#         self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

#     def on_move_press(self, event):
#         curX, curY = event.x, event.y
#         self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

#     def on_button_release(self, event):
#         bbox = {
#             "top": min(self.start_y, event.y),
#             "left": min(self.start_x, event.x),
#             "width": abs(event.x - self.start_x),
#             "height": abs(event.y - self.start_y),
#             "mon": self.monitor_number
#         }

#         # Grab the data
#         sct_img = self.sct.grab(bbox)

#         # Save to a file (example: PNG)
#         output = "selected_area.png"
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         print(f"Saved to {output}")

#         # Close the GUI
#         self.destroy()

#     def start_capture(self):
#         # Set window position on the second monitor
#         self.geometry(f"{self.mon['width']}x{self.mon['height']}+{self.mon['left']}+{self.mon['top']}")
#         self.mainloop()

# # Usage:
# if __name__ == "__main__":
#     app = ScreenCaptureGUI()
#     app.start_capture()


# import mss
# import mss.tools


# with mss.mss() as sct:
#     # Get information of monitor 2
#     monitor_number = 2
#     mon = sct.monitors[monitor_number]

#     # The screen part to capture
#     monitor = {
#         "top": mon["top"],
#         "left": mon["left"],
#         "width": mon["width"],
#         "height": mon["height"],
#         "mon": monitor_number,
#     }
#     output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

#     # Grab the data
#     sct_img = sct.grab(monitor)

#     # Save to the picture file
#     mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#     print(output)









# import tkinter as tk
# import mss
# import mss.tools

# class ScreenCaptureGUI(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         # Initialize mss instance
#         self.sct = mss.mss()

#         # Get information of monitor 2
#         self.monitor_number = 2
#         self.mon = self.sct.monitors[self.monitor_number]

#         # Set window on the second monitor and make it transparent
#         self.geometry(f"{self.mon['width']}x{self.mon['height']}+{self.mon['left']}+{self.mon['top']}")
#         self.attributes('-alpha', 0.5)  # Adjust transparency as needed

#         # Create a canvas to display the monitor content
#         self.canvas = tk.Canvas(self, width=self.mon["width"], height=self.mon["height"], bg='white')
#         self.canvas.pack()

#         # Bind mouse events
#         self.canvas.bind("<ButtonPress-1>", self.on_button_press)
#         self.canvas.bind("<B1-Motion>", self.on_move_press)
#         self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

#         # Variables to track selection
#         self.start_x = None
#         self.start_y = None
#         self.rect = None

#     def on_button_press(self, event):
#         self.start_x = event.x
#         self.start_y = event.y
#         self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

#     def on_move_press(self, event):
#         curX, curY = event.x, event.y
#         self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

#     def on_button_release(self, event):
#         bbox = {
#             "top": min(self.start_y, event.y),
#             "left": min(self.start_x, event.x),
#             "width": abs(event.x - self.start_x),
#             "height": abs(event.y - self.start_y),
#             "mon": self.monitor_number
#         }

#         # Grab the data
#         sct_img = self.sct.grab(bbox)

#         # Save to a file (example: PNG)
#         output = "selected_area.png"
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         print(f"Saved to {output}")

#         # Close the GUI
#         self.destroy()

#     def start_capture(self):
#         self.mainloop()

# # Usage:
# if __name__ == "__main__":
#     app = ScreenCaptureGUI()
#     app.start_capture()



# import tkinter as tk
# import mss
# import mss.tools

# class ScreenCaptureGUI(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         # Initialize mss instance
#         self.sct = mss.mss()

#         # Get information of monitor 2
#         self.monitor_number = 2
#         self.mon = self.sct.monitors[self.monitor_number]

#         # Set window on the second monitor and make it transparent
#         self.geometry(f"{self.mon['width']}x{self.mon['height']}+{self.mon['left']}+{self.mon['top']}")
#         self.attributes('-alpha', 0.5)  # Adjust transparency as needed

#         # Create a canvas to display the monitor content
#         self.canvas = tk.Canvas(self, width=self.mon["width"], height=self.mon["height"], bg='white')
#         self.canvas.pack()

#         # Bind mouse events
#         self.canvas.bind("<ButtonPress-1>", self.on_button_press)
#         self.canvas.bind("<B1-Motion>", self.on_move_press)
#         self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

#         # Variables to track selection
#         self.start_x = None
#         self.start_y = None
#         self.rect = None

#     def on_button_press(self, event):
#         self.start_x = event.x
#         self.start_y = event.y
#         self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

#     def on_move_press(self, event):
#         curX, curY = event.x, event.y
#         self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

#     def on_button_release(self, event):
#         bbox = {
#             "top": min(self.start_y, event.y) + self.mon['top'],
#             "left": min(self.start_x, event.x) + self.mon['left'],
#             "width": abs(event.x - self.start_x),
#             "height": abs(event.y - self.start_y),
#             "mon": self.monitor_number
#         }

#         # Grab the data
#         sct_img = self.sct.grab(bbox)

#         # Save to a file (example: PNG)
#         output = "selected_area.png"
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         print(f"Saved to {output}")

#         # Close the GUI
#         self.destroy()

#     def start_capture(self):
#         self.mainloop()

# # Usage:
# if __name__ == "__main__":
#     app = ScreenCaptureGUI()
#     app.start_capture()



import tkinter as tk
import mss
import mss.tools

class ScreenCaptureChooseMonitor(tk.Tk):
    def __init__(self,
        monitor_number = 1,
        selection_size = 30,
        transparency=0.2,
        background='cyan',
        outline_color='white'
    ):
        super().__init__()

        # Initialize mss instance
        self.sct = mss.mss()

        # Get information of monitor 2
        self.monitor_number = monitor_number
        self.mon = self.sct.monitors[self.monitor_number]

        # Set window on the second monitor and make it transparent
        self.geometry(f"{self.mon['width']}x{self.mon['height']}+{self.mon['left']}+{self.mon['top']}")
        # self.attributes('-alpha', 0.5)  # Adjust transparency as needed
        self.attributes('-alpha', transparency)  # Adjust transparency as needed

        # Create a canvas to display the monitor content
        self.canvas = tk.Canvas(self, width=self.mon["width"], height=self.mon["height"], bg=background)
        # self.canvas = tk.Canvas(self, width=self.mon["width"], height=self.mon["height"])
        self.canvas.pack()

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        # Variables to track selection
        self.start_x = None
        self.start_y = None
        self.selection_size = selection_size
        self.outline_color = outline_color
        self.rect = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x + self.selection_size, self.start_y + self.selection_size,
            outline=self.outline_color
        )

    def on_move_press(self, event):
        curX, curY = event.x, event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        bbox = {
            "top": min(self.start_y, event.y) + self.mon['top'],
            "left": min(self.start_x, event.x) + self.mon['left'],
            "width": abs(event.x - self.start_x),
            "height": abs(event.y - self.start_y),
            "mon": self.monitor_number
        }

        # Adjust bbox to ensure it captures the entire selection area
        bbox["width"] = max(1, bbox["width"])
        bbox["height"] = max(1, bbox["height"])

        # Grab the data
        sct_img = self.sct.grab(bbox)

        # Save to a file (example: PNG)
        output = "selected_area.png"
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(f"Saved to {output}")

        # Close the GUI
        self.destroy()

    def start_capture(self):
        self.mainloop()

# from schnell.app.screencapture_monitor import start_capture
def start_capture(monitor_number=2, selection_size=30):
    application = ScreenCaptureChooseMonitor(monitor_number=monitor_number, selection_size=selection_size)  # Set selection_size to desired default (10 pixels)
    application.start_capture()

# Usage:
if __name__ == "__main__":
    app = ScreenCaptureChooseMonitor(monitor_number=2, selection_size=30)  # Set selection_size to desired default (10 pixels)
    app.start_capture()
