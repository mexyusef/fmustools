from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.Qsci import QsciScintilla, QsciLexerPython


class SimpleQtEditor(QMainWindow):
    def __init__(self, content=None, filepath=None):
        super().__init__()
        self.editor = QsciScintilla()
        self.editor.setLexer(QsciLexerPython(self.editor))

        if content:
            self.editor.setText(content)
        elif filepath:
            with open(filepath, 'r') as f:
                self.editor.setText(f.read())

        self.setCentralWidget(self.editor)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        save_as_action = QAction('Save As', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        save_as_action.triggered.connect(self.save_as)

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open)

        line_numbers_action = QAction('Show Line Numbers', self)
        line_numbers_action.setCheckable(True)
        line_numbers_action.setChecked(True)
        line_numbers_action.triggered.connect(self.toggle_line_numbers)

        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(open_action)

        view_menu = menu.addMenu('View')
        view_menu.addAction(line_numbers_action)

    def save(self):
        if not self.filepath:
            self.save_as()
            return

        with open(self.filepath, 'w') as f:
            f.write(self.editor.text())

    def save_as(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save As')
        if file_path:
            self.filepath = file_path
            self.save()

    def open(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open')
        if file_path:
            self.filepath = file_path
            with open(file_path, 'r') as f:
                self.editor.setText(f.read())

    def toggle_line_numbers(self, checked):
        self.editor.setMarginWidth(0, 0 if checked else self.editor.fontMetrics().width('00000') + 5)


def simple_qt_editor(content=None, filepath=None):
    if not content and not filepath:
        return

    app = QApplication([])
    editor = SimpleQtEditor(content, filepath)
    editor.show()
    app.exec_()

# simple_qt_editor('hello brother')


import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class SimpleTkEditor:
    def __init__(self, content=None, filepath=None):
        self.filepath = filepath

        self.root = tk.Tk()
        self.root.title('Simple Editor')

        self.textbox = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.textbox.pack(expand=True, fill=tk.BOTH)

        if content:
            self.textbox.insert(tk.END, content)
        elif filepath:
            try:
                with open(filepath, 'r') as f:
                    self.textbox.insert(tk.END, f.read())
            except Exception as e:
                messagebox.showerror('Error', str(e))

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=self.new_file)
        filemenu.add_command(label='Open', accelerator='Ctrl+O', command=self.open_file)
        filemenu.add_command(label='Save', accelerator='Ctrl+S', command=self.save_file)
        filemenu.add_command(label='Save As', accelerator='Ctrl+Shift+S', command=self.save_file_as)
        menubar.add_cascade(label='File', menu=filemenu)

        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-S>', lambda e: self.save_file_as())

        self.root.config(menu=menubar)

    def run(self):
        self.root.mainloop()

    def new_file(self):
        self.textbox.delete('1.0', tk.END)
        self.filepath = None

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    self.textbox.delete('1.0', tk.END)
                    self.textbox.insert(tk.END, f.read())
                    self.filepath = file_path
            except Exception as e:
                messagebox.showerror('Error', str(e))

    def save_file(self):
        if self.filepath:
            try:
                with open(self.filepath, 'w') as f:
                    f.write(self.textbox.get('1.0', tk.END))
            except Exception as e:
                messagebox.showerror('Error', str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(self.textbox.get('1.0', tk.END))
                    self.filepath = file_path
            except Exception as e:
                messagebox.showerror('Error', str(e))


def simple_tk_editor(content=None, filepath=None):
    if not content and not filepath:
        return

    editor = SimpleTkEditor(content, filepath)
    editor.run()

# simple_tk_editor('hello brother')
