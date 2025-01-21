import sys, time
from prompt_toolkit.shortcuts import (
	button_dialog,
	checkboxlist_dialog,
	input_dialog,
	message_dialog,
	radiolist_dialog,
	yes_no_dialog,
)
from prompt_toolkit.styles import Style
from .autoutils import prompt, password

"""
https://python-prompt-toolkit.readthedocs.io/en/master/pages/dialogs.html
radio = single selection
check = multi selection
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox


mystyle=Style.from_dict({
	'dialog': 'bg:#cdbbb3',
	'button': 'bg:#bf99a4',
	'checkbox': '#e8612c',
	'dialog.body': 'bg:#a9cfd0',
	'dialog shadow': 'bg:#c98982',
	'frame.label': '#fcaca3',
	'dialog.body label': '#fd8bb6',
})


class MessageBoxApplication(tk.Frame):
	def __init__(self, master=None, title="Clock and Text Body", body="This is a paragraph of text."):
		super().__init__(master)
		self.body = body
		self.master = master
		self.master.title(title)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.text_body = tk.Text(self, height=10, wrap=tk.WORD)
		self.text_body.insert(tk.END, self.body)
		self.text_body.pack()

		self.clock_label = tk.Label(self, font=('calibri', 40, 'bold'), background='black', foreground='green')
		self.clock_label.pack(fill=tk.BOTH, expand=True)
		self.update_clock()

	def update_clock(self):
		current_time = time.strftime('%H:%M:%S')
		self.clock_label.config(text=current_time)
		self.clock_label.after(1000, self.update_clock)


def message_box_application(title='(UNTITLED)', body='NO MESSAGE'):
	root = tk.Tk()
	# root = tk.Toplevel()
	root.withdraw()
	root.attributes("-topmost", True)
	app = MessageBoxApplication(master=root, title=title, body=body)
	app.mainloop()


def get_yes_or_no(prompt, judul="Confirmation"):
	"""Usage example:
	result = get_yes_or_no("Do you want to proceed?")
	print(result)
	"""
	root = tk.Tk()
	root.withdraw()  # Hide the main window
	result = messagebox.askyesno(judul, prompt)
	root.destroy()  # Close the window after obtaining the result
	return result


def radio(judul, isi, pilihan=['a','b','c'], default_checked=None):
	"""
	pilihan bisa list of strings atau list of tuples (value-displayedvalue)
	"""
	if pilihan and isinstance(pilihan[0], str): # jk list of strings, convert ke list of tuples dulu
		values = list(map(lambda x: (x,x), pilihan))
	else:
		values = pilihan

	kwargs = {
		'title'		: judul,
		'text'		: isi,
		'values'	: values,
	}
	if default_checked:
		kwargs['default'] = default_checked
	result = radiolist_dialog(
		**kwargs
		# title=judul,
		# text=isi,
		# values=values
	).run()
	return result


def check(judul, isi, pilihan=['a','b','c'], default_checked=[]):
	"""
	pilihan bisa list of strings atau list of tuples (value-displayedvalue)
	list of tuples: [(value, label)]
		("eggs", "Eggs"),
		("bacon", "Bacon"),
		("croissants", "20 Croissants"),
		("daily", "The breakfast of the day")

	semua_keys = list(invoke_all.keys())
	semua_keys_selected = [item for item in invoke_all.keys() if invoke_all[item]==1]
	print('semua_keys:', semua_keys, 'semua_keys_selected:', semua_keys_selected)
	"""
	if pilihan and isinstance(pilihan[0], str):
		values = list(map(lambda x: (x,x), pilihan))
	else:
		values = pilihan

	kwargs = {
		'title'		: judul,
		'text'		: isi,
		'values'	: values,
	}
	if default_checked:
		kwargs['default_values'] = default_checked


	# print(f"""check
	# pilihan				= {pilihan}
	# default_checked		= {default_checked}
	# values				= {values}
	# kwargs				= {kwargs}
	# """)

	result = checkboxlist_dialog(
		**kwargs
		# title=judul,
		# text=isi,
		# values=values,
	).run()

	# print('hasil:', result)
	return result


def masuk(judul, isi):
	result = input_dialog(
		title=judul,
		text=isi).run()
	return result


def tombol(judul, isi, pilihan=[('Yes', True), ('No', False), ('Maybe...', None)]):
	"""
	asumsi: pertama label, kedua nilai
	"""
	result = button_dialog(
		title=judul,
		text=isi,
		buttons=pilihan,
	).run()
	return result


def yesno(judul, isi):
	result = yes_no_dialog(
		title=judul,
		text=isi).run()
	return result


def message(judul, isi):
	message_dialog(
		title=judul,
		text=isi).run()
	return None


def choose_one_file(dirpath, judul='Choose one file', isi='Choose one file'):
	from .dirutils import sfiles
	daftar_file = sfiles(dirpath=dirpath)
	return radio(judul, isi, daftar_file)


def choose_multiple_files(dirpath, judul='Choose several files', isi='Choose multiple files'):
	from .dirutils import sfiles
	daftar_file = sfiles(dirpath=dirpath)
	return check(judul, isi, daftar_file)


def tkopendir(judul='Buka direktori', initial_directory=None):
	"""
	# Usage example:
	directory = opendir('Select Directory', initial_directory='C:/Users')
	print("Selected Directory:", directory)

	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	root.withdraw()  # Hide the main Tkinter window
	root.attributes("-topmost", True)

	# Configure file dialog options
	file_options = {}
	if initial_directory:
		file_options['initialdir'] = initial_directory

	selected_directory = filedialog.askdirectory(title=judul, **file_options)

	if selected_directory:
		print(f"[tkopendir][hasil input]\nfileName = {selected_directory}")
	root.destroy()
	return selected_directory


def tkopenfile(judul='Buka file', initial_directory=None):
	"""
	# Example usage:
	selected_file = tkopenfile(judul='Select a file', initial_directory='/path/to/initial/directory')
	if selected_file:
		print("Selected file:", selected_file)
	else:
		print("No file selected.")

	"""
	root = tk.Tk()
	root.withdraw()  # Hide the main window
	root.attributes("-topmost", True)

	file_path = filedialog.askopenfilename(
		title=judul,
		initialdir=initial_directory,
		filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")]
	)
	root.destroy()
	return file_path


def tkopenfiles(judul='Buka beberapa file', initial_directory=None):
	"""
	# Example usage:
	selected_files = tkopenfiles(judul='Select multiple files', initial_directory='/path/to/initial/directory')
	if selected_files:
		print("Selected files:", selected_files)
	else:
		print("No files selected.")

	"""
	root = tk.Tk()
	root.withdraw()  # Hide the main window
	root.attributes("-topmost", True)

	file_paths = filedialog.askopenfilenames(
		title=judul,
		initialdir=initial_directory,
		filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")]
	)
	root.destroy()
	return file_paths


def tksavefile(judul='Simpan file', initial_directory=None, default_extension=".txt"):
	"""
	# Example usage:
	saved_file = tksavefile(judul='Save as', initial_directory='/path/to/initial/directory', default_extension=".txt")
	if saved_file:
		print("Selected file:", saved_file)
	else:
		print("No file selected.")
	"""
	root = tk.Tk()
	root.withdraw()  # Hide the main window
	root.attributes("-topmost", True)

	file_path = filedialog.asksaveasfilename(
		title=judul,
		initialdir=initial_directory,
		defaultextension=default_extension,
		filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")]
	)
	root.destroy()
	return file_path


def opendir(judul='Buka direktori', initial_directory=None):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)

	options = QtWidgets.QFileDialog.Options()
	options |= QtWidgets.QFileDialog.DontUseNativeDialog
	if initial_directory:
		selected_directory = QtWidgets.QFileDialog.getExistingDirectory(None, judul, directory=initial_directory, options=options)
	else:
		selected_directory = QtWidgets.QFileDialog.getExistingDirectory(None, judul, options=options)
	if selected_directory:
		print(f"""[opendir][hasil input]
		selected_directory = {selected_directory}
		""")
	app.quit()
	return selected_directory
opendirdialog = opendir
gui_dialog_open_dir = opendir


def openfile(judul="openfile", isi="Pilih file", berkas="All Files (*);;Python Files (*.py)"):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)

	options = QtWidgets.QFileDialog.Options()
	options |= QtWidgets.QFileDialog.DontUseNativeDialog
	nama_file, jenis_file = QtWidgets.QFileDialog.getOpenFileName(None, judul, isi, berkas, options=options)
	if nama_file:
		print(f"""[openfile][hasil input]
		nama_file = {nama_file}
		jenis_file = {jenis_file}
		""")
	app.quit()
	return nama_file
openfiledialog = openfile
gui_dialog_open_file = openfile


def openfiles(judul="gui_dialog_open_files", isi="badan", berkas="All Files (*);;Python Files (*.py)"):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)

	options = QtWidgets.QFileDialog.Options()
	options |= QtWidgets.QFileDialog.DontUseNativeDialog
	nama_file, jenis_file = QtWidgets.QFileDialog.getOpenFileNames(None, judul, isi, berkas, options=options)
	if nama_file:
		print(f"""[gui_dialog_open_files][hasil input]
		nama_file = {nama_file}
		jenis_file = {jenis_file}
		""")
	app.quit()
	# sys.exit(app.exec_())
	return nama_file
openfilesdialog = openfiles
gui_dialog_open_files = openfiles


def savefile(judul="gui_dialog_save_file", isi="badan", berkas="All Files (*);;Python Files (*.py);;Text Files (*.txt)"):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)

	options = QtWidgets.QFileDialog.Options()
	options |= QtWidgets.QFileDialog.DontUseNativeDialog
	nama_file, jenis_file = QtWidgets.QFileDialog.getSaveFileName(None, judul, isi, berkas, options=options)
	if nama_file:
		print(f"""[gui_dialog_save_file][hasil input]
		nama_file = {nama_file}
		jenis_file = {jenis_file}
		""")
	app.quit()
	return nama_file
savefiledialog = savefile
gui_dialog_save_file = savefile


def gui_single_select_radio():
	pass


def gui_single_select_combo():
	pass


def gui_multi_select_check():
	pass


def gui_masuk(judul='Masukkan', isi='Masukkan nama:'):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getText(None, judul, isi)
	print(f"""[gui_masuk][hasil input]
	name = {name}
	done = {done}
	""")
	# QtWidgets.qApp.quit()
	# MainWindow = QtWidgets.QMainWindow()
	# ui = Ui_MainWindow()
	# ui.setupUi(MainWindow)
	# MainWindow.show()
	# app.exec_()
	app.quit()
	# sys.exit(app.exec_())
	return name
gm = gui_masuk


def gui_masuk_int(judul='Masukkan', isi='Masukkan integer:'):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getInt(None, judul, isi)
	print(f"""[gui_masuk_int][hasil input]
	name = {name}
	done = {done}
	""")
	# QtWidgets.qApp.quit()
	# MainWindow = QtWidgets.QMainWindow()
	# ui = Ui_MainWindow()
	# ui.setupUi(MainWindow)
	# MainWindow.show()
	# app.exec_()
	app.quit()
	# sys.exit(app.exec_())
	return name
gmi = gui_masuk_int


def gui_masuk_double(judul='Masukkan', isi='Masukkan double:'):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getDouble(None, judul, isi)
	print(f"""[gui_masuk_double][hasil input]
	name = {name}
	done = {done}
	""")
	# QtWidgets.qApp.quit()
	# MainWindow = QtWidgets.QMainWindow()
	# ui = Ui_MainWindow()
	# ui.setupUi(MainWindow)
	# MainWindow.show()
	# app.exec_()
	app.quit()
	# sys.exit(app.exec_())
	return name
gmd = gui_masuk_double


def gui_pilih(pilihan=['C', 'C++', 'Java', 'Python', 'Javascript'], judul='Masukkan pilihan', isi='Pilih bahasa:'):
	from PyQt5 import QtCore, QtGui, QtWidgets
	app = QtWidgets.QApplication(sys.argv)
	name, done = QtWidgets.QInputDialog.getItem(None, judul, isi, pilihan)
	name = str(name)
	print(f"""[gui_pilih][hasil input]
	name = {name}
	done = {done}
	""")
	# QtWidgets.qApp.quit()
	# MainWindow = QtWidgets.QMainWindow()
	# ui = Ui_MainWindow()
	# ui.setupUi(MainWindow)
	# MainWindow.show()
	# app.exec_()
	app.quit()
	# sys.exit(app.exec_())
	return name
gp = gui_pilih


def critical(judul, isi):
	# QWidget: Must construct a QApplication before a QWidget
	from PyQt5.QtWidgets import QMessageBox, QApplication, qApp
	app = QApplication(sys.argv)
	result = QMessageBox.critical(
		None,
		judul,
		isi,
		buttons=QMessageBox.Yes | QMessageBox.No,
		defaultButton=QMessageBox.Yes,
	)
	if result == QMessageBox.Yes:
		print('Yay!')
		return True
	return False
	# sys.exit(app.exec())


def warning(judul, isi):
	from PyQt5.QtWidgets import QMessageBox, QApplication, qApp
	app = QApplication(sys.argv)
	result = QMessageBox.warning(
		None,
		judul,
		isi,
		buttons=QMessageBox.Yes | QMessageBox.No,
		defaultButton=QMessageBox.Yes,
	)
	if result == QMessageBox.Yes:
		print('Yay!')
		return True
	return False


def information(judul, isi):
	from PyQt5.QtWidgets import QMessageBox, QApplication, qApp
	app = QApplication(sys.argv)
	result = QMessageBox.information(
		None,
		judul,
		isi,
		buttons=QMessageBox.Yes | QMessageBox.No,
		defaultButton=QMessageBox.Yes,
	)
	if result == QMessageBox.Yes:
		print('Yay!')
		return True
	return False


def question(judul, isi):
	from PyQt5.QtWidgets import QMessageBox, QApplication, qApp
	app = QApplication(sys.argv)
	result = QMessageBox.question(
		None,
		judul,
		isi,
		buttons=QMessageBox.Yes | QMessageBox.No,
		defaultButton=QMessageBox.Yes,
	)
	if result == QMessageBox.Yes:
		print('Yay!')
		return True
	return False


def autoprompt(hint='Masukkan info:'):
	from schnell.creator.context import context
	data = prompt(hint)
	context['pyautogui_input'] = data
	return data


def autopassword(hint='Masukkan info:'):
	from schnell.creator.context import context
	data = password(hint)
	context['pyautogui_input'] = data
	return data


def combobox(lst):
	"""
	selection = combobox(["apple", "banana", "cherry"])
	print("Selected item:", selection)
	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	# root.withdraw()
	root.title("Select from List")

   # Set the window to be always on top
	root.attributes("-topmost", True)

	# create combobox
	selected_item = tk.StringVar(value=lst[0])
	combo = ttk.Combobox(root, textvariable=selected_item, values=lst, state="readonly")
	combo.pack(padx=10, pady=10)
	combo.focus() # set focus to the combobox on load

	# allow user to select using arrow keys
	combo.bind("<Down>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Up>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Return>", lambda event: root.destroy())

	# create OK button to close the window
	ok_button = tk.Button(root, text="OK", command=root.destroy)
	ok_button.pack(padx=10, pady=10)

	# run the GUI
	root.mainloop()
	# root.wait_window()

	# return the selected item
	return selected_item.get()

# selection = combobox(["apple", "banana", "cherry"])
# print("Selected item:", selection)


def combobox_escape(lst):
	"""
	selection = combobox(["apple", "banana", "cherry"])
	print("Selected item:", selection)
	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	# root.withdraw()
	root.title("Select from List")

	# Set the window to be always on top
	root.attributes("-topmost", True)

	# create combobox
	selected_item = tk.StringVar(value=lst[0])
	combo = ttk.Combobox(root, textvariable=selected_item, values=lst, state="readonly")
	combo.pack(padx=10, pady=10)
	combo.focus()  # set focus to the combobox on load

	# allow user to select using arrow keys
	combo.bind("<Down>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Up>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Return>", lambda event: root.destroy())

	def on_escape(event):
		root.destroy()

	# bind the escape key to return None
	root.bind("<Escape>", on_escape)

	# create OK button to close the window
	ok_button = tk.Button(root, text="OK", command=root.destroy)
	ok_button.pack(padx=10, pady=10)

	# run the GUI
	root.mainloop()
	# root.wait_window()

	# return the selected item, or None if escape was pressed
	return selected_item.get() if selected_item.get() != "" else None


def combobox_listbox2(lst, title="Select from List"):
	"""
	selection = combobox(["apple", "banana", "cherry"])
	print("Selected item:", selection)
	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	# root.withdraw()
	root.title(title)

	# Set the window to be always on top
	root.attributes("-topmost", True)

	# Create a listbox to display the items
	listbox = tk.Listbox(root, selectmode=tk.SINGLE)
	for item in lst[:10]:
		listbox.insert(tk.END, item)
	if len(lst) > 10:
		listbox.insert(tk.END, "...")
	listbox.pack(padx=10, pady=5)

	# create combobox
	selected_item = tk.StringVar(value=lst[0])
	combo = ttk.Combobox(root, textvariable=selected_item, values=lst, state="readonly")
	combo.pack(padx=10, pady=5)
	combo.focus()  # set focus to the combobox on load

	# allow user to select using arrow keys
	combo.bind("<Down>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Up>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Return>", lambda event: root.destroy())

	def on_escape(event):
		root.destroy()

	# bind the escape key to return None
	root.bind("<Escape>", on_escape)

	# create OK button to close the window
	ok_button = tk.Button(root, text="OK", command=root.destroy)
	ok_button.pack(padx=10, pady=5)

	# run the GUI
	root.mainloop()
	# root.wait_window()

	# return the selected item, or None if escape was pressed
	# return selected_item.get() if selected_item.get() != "" else None
	# kembalikan index dari 1
	return lst.index(selected_item.get())+1 if selected_item.get() != "" else 1


def combobox_listbox(lst, title="Select from List", return_index=True, starting_index=1):
	"""
	selection = combobox(["apple", "banana", "cherry"])
	print("Selected item:", selection)
	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	# root.withdraw()
	root.title(title)

	# Set the window to be always on top
	root.attributes("-topmost", True)

	# Get the width of the screen
	screen_width = root.winfo_screenwidth()

	# Calculate the initial width of the window (half of the screen width)
	initial_width = screen_width // 3

	# Set the initial width and height of the window
	root.geometry(f"{initial_width}x300")  # You can adjust the height as needed

	# Create a listbox to display the items
	listbox = tk.Listbox(root, selectmode=tk.SINGLE)
	for item in lst[:10]:
		listbox.insert(tk.END, item)
	if len(lst) > 10:
		listbox.insert(tk.END, "...")
	listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)  # Expand to fill the available space

	# create combobox
	selected_item = tk.StringVar(value=lst[0])
	combo = ttk.Combobox(root, textvariable=selected_item, values=lst, state="readonly")
	combo.pack(fill=tk.X, padx=10, pady=5)  # Expand horizontally

	combo.focus()  # set focus to the combobox on load

	# allow user to select using arrow keys
	combo.bind("<Down>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Up>", lambda event: combo.event_generate("<Button-1>", x=0, y=0))
	combo.bind("<Return>", lambda event: root.destroy())

	def on_escape(event):
		root.destroy()

	# bind the escape key to return None
	root.bind("<Escape>", on_escape)

	# create OK button to close the window
	ok_button = tk.Button(root, text="OK", command=root.destroy)
	ok_button.pack(padx=10, pady=5)

	# run the GUI
	root.mainloop()
	# root.wait_window()

	# return the selected item, or None if escape was pressed
	# return selected_item.get() if selected_item.get() != "" else None
	# kembalikan index dari 1
	if return_index:
		return lst.index(selected_item.get()) + starting_index if selected_item.get() != "" else starting_index
	else:
		return selected_item.get()


def checkbox_select2(lst, instruction="Select items:", title="Select from List"):
	"""
	selected_indexes = checkbox_select(["apple", "banana", "cherry"])
	print("Selected indexes:", selected_indexes)
	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	# root.withdraw()
	root.title(title)

	# Set the window to be always on top
	root.attributes("-topmost", True)

	# Create a list to store the selected indexes
	selected_indexes = []

	# Add instructions above the checkboxes
	instructions_label = tk.Label(root, text=instruction)
	instructions_label.pack(padx=10, pady=5)

	def on_checkbox_click(index):
		if index in selected_indexes:
			selected_indexes.remove(index)
		else:
			selected_indexes.append(index)

	def focus_next(event):
		event.widget.tk_focusNext().focus()
		return "break"

	first_checkbox = None

	# Create checkboxes for each item in the list
	for i, item in enumerate(lst, start=1):
		checkbox = tk.Checkbutton(root, text=item, command=lambda idx=i: on_checkbox_click(idx))
		checkbox.pack(anchor="w")
		checkbox.bind("<Down>", focus_next)
		checkbox.bind("<Up>", lambda event, c=checkbox: c.tk_focusPrev().focus())

		if not first_checkbox:
			first_checkbox = checkbox

	# Set initial focus on the first checkbox
	if first_checkbox:
		first_checkbox.focus()

	def on_ok_click():
		root.destroy()

	# Create OK button to close the window
	ok_button = tk.Button(root, text="OK", command=on_ok_click)
	ok_button.pack(pady=10)

	def on_escape(event):
		root.destroy()

	def on_enter(event):
		on_ok_click()

	# Bind the escape key to return an empty list
	root.bind("<Escape>", on_escape)
	root.bind("<Return>", on_enter)

	# Run the GUI
	root.mainloop()
	# root.wait_window()

	return selected_indexes


def checkbox_select(lst, instruction="Select items:", title="Select from List"):
	"""
	selected_indexes = checkbox_select(["apple", "banana", "cherry"])
	print("Selected indexes:", selected_indexes)
	"""
	root = tk.Tk()
	# root = tk.Toplevel()
	# root.withdraw()
	root.title(title)

	# ini setting w dan h, tapi belum x0,y0
	# Set the window to be always on top
	root.attributes("-topmost", True)
	# Get the width of the screen
	screen_width = root.winfo_screenwidth()
	# Calculate the initial width of the window (half of the screen width)
	initial_width = screen_width // 2
	# Set the initial width and height of the window
	root.geometry(f"{initial_width}x800")  # You can adjust the height as needed


	# Create a list to store the selected indexes
	selected_indexes = []

	# Add instructions above the checkboxes
	instructions_label = tk.Label(root, text=instruction)
	instructions_label.pack(padx=10, pady=5)
	################# START: tambah scrollbar
	canvas = tk.Canvas(root)
	scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
	checkbox_frame = tk.Frame(canvas)

	checkbox_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
	canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")

	canvas.pack(side="left", fill="both", expand=True)
	scrollbar.pack(side="right", fill="y")

	canvas.configure(yscrollcommand=scrollbar.set)
	################# END: tambah scrollbar

	def on_checkbox_click(index):
		if index in selected_indexes:
			selected_indexes.remove(index)
		else:
			selected_indexes.append(index)

	def focus_next(event):
		event.widget.tk_focusNext().focus()
		return "break"

	first_checkbox = None

	# Create checkboxes for each item in the list
	for i, item in enumerate(lst, start=1):
		# checkbox = tk.Checkbutton(root, text=item, command=lambda idx=i: on_checkbox_click(idx))
		checkbox = tk.Checkbutton(checkbox_frame, text=item, command=lambda idx=i: on_checkbox_click(idx))
		checkbox.pack(anchor="w")
		checkbox.bind("<Down>", focus_next)
		checkbox.bind("<Up>", lambda event, c=checkbox: c.tk_focusPrev().focus())

		if not first_checkbox:
			first_checkbox = checkbox

	# Set initial focus on the first checkbox
	if first_checkbox:
		first_checkbox.focus()

	def on_ok_click():
		root.destroy()

	# Create OK button to close the window
	ok_button = tk.Button(root, text="OK", command=on_ok_click)
	ok_button.pack(pady=10)

	def on_escape(event):
		root.destroy()

	def on_enter(event):
		on_ok_click()

	# Bind the escape key to return an empty list
	root.bind("<Escape>", on_escape)
	root.bind("<Return>", on_enter)

	# Run the GUI
	root.mainloop()
	# root.wait_window()

	return selected_indexes
