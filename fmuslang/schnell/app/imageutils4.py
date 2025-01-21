# berbagai effect di sini
# contrast
# brightness
# to grayscale

import pyperclip
import os
import re
from PIL import Image, ImageTk
import tkinter as tk

def display_images_in_grid(image_paths, thumbsize=(300,300)):
    root = tk.Tk()
    root.title(image_paths[0])

    # Calculate the number of rows and columns for the grid
    num_images = len(image_paths)

    if num_images == 1:
        # If there's only one image, display it as is
        img = Image.open(image_paths[0])
        img = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=img)
        label.image = img  # Keep a reference to avoid garbage collection
        label.pack()
    else:
        cols = int(num_images ** 0.5)
        rows = (num_images // cols) + (1 if num_images % cols > 0 else 0)

        for i, image_path in enumerate(image_paths):
            img = Image.open(image_path)
            img.thumbnail(thumbsize)  # Resize to fit in the grid
            img = ImageTk.PhotoImage(img)
            label = tk.Label(root, image=img)
            label.image = img  # Keep a reference to avoid garbage collection
            label.grid(row=i // cols, column=i % cols)

    # Center the window on the screen
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'+{x}+{y}')

    root.mainloop()

def display_images_from_clipboard():
    # Get clipboard content
    clipboard_content = pyperclip.paste()

    # Regular expression to find file paths
    path_regex = r'\b(?:[a-zA-Z]:\\|/)?(?:[^\\/:*?"<>|\r\n]+\\|/)*[^\\/:*?"<>|\r\n]+\.(?:png|jpg|jpeg|gif|bmp)\b'
    
    # Find all image paths in the clipboard content
    image_paths = re.findall(path_regex, clipboard_content, re.IGNORECASE)

    # Filter out non-existent files
    valid_image_paths = [path for path in image_paths if os.path.isfile(path)]

    if valid_image_paths:
        display_images_in_grid(valid_image_paths)
    else:
        print("No valid image paths found in clipboard.")

def test_display_images_from_clipboard():
    display_images_from_clipboard()
