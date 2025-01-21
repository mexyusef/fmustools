import redis
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkhtmlview import HTMLLabel
import markdown
from tkinter import filedialog
from tkinter import END


def my_application(keyword=None):

    class MarkdownViewer:
        def __init__(self, master):
            self.master = master
            self.html_label = HTMLLabel(self.master, html="<h1>Welcome to Markdown Viewer!</h1>")
            self.html_label.pack(fill="both", expand=True)
            self.scrollbar = tk.Scrollbar(self.master)
            self.scrollbar.pack(side="right", fill="y")
            self.html_label.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.configure(command=self.html_label.yview)
        def set_content(self, contents):
            html = markdown.markdown(contents)
            self.html_label.set_html(html)

    def load_value(key):
        value = redis_client.get(key)
        try:
            value_dict = json.loads(value)
            editor.set_content(value_dict['content'])
        except SyntaxError:
            print(f"Error parsing JSON for key {key}: unterminated string literal")
            editor.set_content(f"Error parsing JSON for key {key}: unterminated string literal")

    def search_redis(search_string=None):
        listbox.delete(0, tk.END)
        if not search_string:
            search_string = search_box.get()
        for key in redis_client.scan_iter():
            value = redis_client.get(key)
            try:
                value_dict = json.loads(value)
                if value_dict['content'] and search_string in value_dict['content']:
                    listbox.insert(tk.END, key.decode('utf8'))
            except SyntaxError:
                print(f"Error parsing JSON for key {key}: unterminated string literal")
        if listbox.size() == 0:
            editor.set_content("No matching keys found")

    def on_select(event=None):
        w = event.widget if event else listbox
        if w.curselection():
            index = int(w.curselection()[0])
            key = w.get(index)
            load_value(key)

    def bind_select(event):
        if event.keysym == 'Up':
            current_selection = listbox.curselection()
            if current_selection:
                index = int(current_selection[0])
                if index > 0:
                    listbox.selection_clear(0, END)
                    listbox.selection_set(index - 1)
                    on_select(event)
        elif event.keysym == 'Down':
            current_selection = listbox.curselection()
            if current_selection:
                index = int(current_selection[0])
                if index < listbox.size() - 1:
                    listbox.selection_clear(0, END)
                    listbox.selection_set(index + 1)
                    on_select(event)

    redis_client = redis.Redis(host='localhost', port=6380, db=10)
    root = tk.Tk()
    root.title("Redis Search")

    listbox_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
    listbox_frame.pack(side="left", fill="y")
    listbox_label = ttk.Label(listbox_frame, text="Matching Keys")
    listbox_label.pack(side="top", fill="x")
    listbox = tk.Listbox(listbox_frame, selectmode="SINGLE")
    listbox.pack(side="left", fill="y", expand=True)
    listbox_scroll = ttk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
    listbox_scroll.pack(side="right", fill="y")
    listbox.configure(yscrollcommand=listbox_scroll.set)
    search_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
    search_frame.pack(side="top", fill="x")
    search_label = ttk.Label(search_frame, text="Search:")
    search_label.pack(side="left")
    search_box = ttk.Entry(search_frame)
    search_box.pack(side="left", fill="x", expand=True)
    search_button = ttk.Button(search_frame, text="Search", command=search_redis)
    search_button.pack(side="right")
    search_box.bind("<Return>", lambda event: search_redis())
    editor_frame = ttk.Frame(root, padding=(0, 10, 10, 10))
    editor_frame.pack(side="left", fill="both", expand=True)

    editor_label = ttk.Label(editor_frame, text="Value")
    editor_label.pack(side="top", fill="x")
    editor = MarkdownViewer(editor_frame)
    listbox.bind("<<ListboxSelect>>", on_select)
    listbox.bind("<Up>", bind_select)
    listbox.bind("<Down>", bind_select)

    if keyword:
        search_redis(keyword)

    root.mainloop()


if __name__ == '__main__':
    my_application('scala')

