# try 1
import tkinter as tk
from tkinter import scrolledtext


def open_editor(filepath=None, content=None):
    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("800x600")

    # Create a scrolled text widget
    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12))
    text_widget.pack(expand=True, fill="both")

    # Load the contents of the file if filepath is specified
    if filepath is not None:
        with open(filepath, "r", encoding='utf-8') as f:
            text_widget.insert("1.0", f.read())
    # Load the text content if content is specified
    elif content is not None:
        text_widget.insert("1.0", content)

    # Bind the escape key to quit the editor
    root.bind("<Escape>", lambda event: root.destroy())

    root.mainloop()

if __name__ == '__main__':
    # Open a file in the text editor
    # open_editor(filepath="example.txt")
    # Open a new text content in the text editor
    open_editor(content="Hello, world!")
