from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

import os, sys, functools, shutil, threading, pyperclip, time
envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
from dotenv import load_dotenv
load_dotenv(envfile)
sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([sidoarjodir, schnelldir])
sys.path.insert(0, sidoarjodir)

if __name__ == '__main__':
	from startup import initialize_programming_data
	initialize_programming_data()

from schnell.app.executor import FileExecutor
from schnell.app.wcmderutils import (
	getlist, button_ketik_handler, operate_on_windows, to_top,
	create_fill_set, fill_set,
	create_fill_set_with_id_index,
	ketik_by_hwnd, ketik_by_index,
	get_items_for_combo,
	hapus_set_combo_items,
	data_for_item,
	is_window_visible,
	operate_on_windows_by_hwnd,
	to_top_by_hwnd,
	get_last_console_data,
)
from schnell.app.utils import env_get
from schnell.app.dirutils import normy, explore, joiner, files_filter
from schnell.app.fileutils import get_daftar, get_definition_by_key_permissive_start, file_content, not_binary, get_extension
from schnell.app.fmusutils import run_fmus_for_file, run_fmus_for_content, run_fmus_for_file_in_folder_in_thread
from schnell.app.systemutils import execute_command_in_dir, execute_command_in_dir_in_thread
from schnell.gui.system.searcher.widgets.flowwidget import FlowWidget
from schnell.gui.system.searcher.widgets.editor_standard import EditorStandard
from schnell.gui.system.searcher.widgets.common import get_icon, BlueButton
from schnell.gui.system.searcher.widgets.dahsyatmenu import DashsyatMenu
from schnell.gui.system.searcher.widgets.common import (
	context_menu_stylesheet,
	resize_screen_ratio_wrapper,
	bahasa_filepaths,
	context_menu_for_dirs_with_entries,
	context_menu_for_files_with_entries,
	predefined_commands,
	yarn_add_packages_dev,
	yarn_add_packages,
)
from schnell.gui.system.searcher.widgets.colorwidget import ColorWidget
from schnell.gui.system.searcher.widgets.buttonwidget import ButtonWidget
from schnell.gui.system.searcher.widgets.tkeditor import tkeditor
from schnell.gui.system.searcher.widgets.windower import WindowerWidget
from schnell.gui.system.searcher.widgets.lalangwidget import LalangWidget
from schnell.gui.system.searcher.widgets.showedit import ShowEditWindow
from schnell.gui.system.searcher.widgets.packagewidget import PackageWidget
from schnell.gui.system.searcher.widgets.creator import CreatorWidget
from schnell.gui.system.searcher.widgets.quickviewer import QuickViewerWidget
from schnell.gui.system.searcher.widgets.filemanip import filemanip

from schnell.gui.system.searcher.widgets.config import preset_directories


class CmderWidget(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def set_input_completer(self):
		model = self.completer.model()
		model.setStringList(self.history)

	def initUI(self):
		self.main_layout = QVBoxLayout(self)
		self.flower = FlowWidget()
		self.history = []
		self.completer = QCompleter(self.history)
		self.completer.setCompletionMode(QCompleter.PopupCompletion)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.editor = QLineEdit()
		self.editor.setCompleter(self.completer)
		self.editor.setFont(QFont("Consolas", 16))
		self.editor.setStyleSheet('background-color: oldlace; height: 48px;')
		self.editor.returnPressed.connect(self.tekan_enter)

		# from schnell.app.wcmderutils import getlist, button_ketik_handler, operate_on_windows, to_top, create_fill_set, fill_set, hapus_set_combo_items
		self.button_menu = QMenu('Button')
		self.button_menu.setIcon(get_icon())
		self.button_menu.addAction('Create+fill+set', self.create_cmd)
		self.button_menu.addAction('Fill+set', self.isi_ulang)
		self.button_menu.addAction('Hapus kosong', self.hapus_kosong)
		self.button_menu.addAction('List', self.list_consoles)
		# TODO:
		# utk operasi berikut, baiknya, hapus kosong dulu
		self.button_menu.addAction('Show all')
		self.button_menu.addAction('Hide all')

		# editor_layout => 6 = linedit, 4 = main button
		# main_layout => 2 = editor_layout, 8 = flow widget
		editor_layout = QVBoxLayout()
		self.main_layout.addLayout(editor_layout, 2)
		self.main_layout.addWidget(self.flower, 8)

		self.main_button = BlueButton(self.button_menu, "Menu")
		# self.exit_button = BlueButton(None, "Exit")
		# self.exit_button.clicked.connect(lambda: qApp.quit())
		button_layout = QHBoxLayout()
		button_layout.addWidget(self.main_button)
		button_layout.addStretch(1)
		editor_layout.addLayout(button_layout, 4)
		editor_layout.addWidget(self.editor, 6) # line edit biar dekat dg flow widget

		# b = QPushButton('')
		# b.setProperty('datastr', value_any)
		# for i in range(100):
		#     b = BlueButton(self.button_menu, f"Btn {i}")
		#     self.flower.add_item(b)
		for item in get_items_for_combo():
			# buat menu masing2
			button_menu = QMenu('Button')
			button_menu.setIcon(get_icon())
			button_menu.addAction('Toggle', self.toggle_button_visibility)
			b = BlueButton(button_menu, item)
			button_menu.setProperty('button', b)  # <menu>.property('button')
			b.setProperty('information', data_for_item(item))
			self.flower.add_item(b)

	def tekan_enter(self):
		tulisan = self.editor.text().strip()
		if tulisan:
			console = get_last_console_data()
			if console:
				console_hwnd = console['chwnd'] # utk ngetik pake chwnd.
				ketik_by_hwnd(console_hwnd, tulisan)
				if tulisan not in self.history:
					self.history.append(tulisan)
					self.set_input_completer()

	def populate_flowwidget(self, items):
		widgets = []
		for item in items:
			button_menu = QMenu('Button')
			button_menu.setIcon(get_icon())
			button_menu.addAction('Toggle', self.toggle_button_visibility)
			button_menu.addAction('Ketik', self.type_on_console)
			button_menu.addAction('Minimize', self.minimize_window)
			button_menu.addAction('Maximize', self.maximize_window)
			button_menu.addAction('Restore', self.restore_window)
			button_menu.addAction('Normal', self.normal_window)
			button_menu.addAction('Close', self.close_window)

			button_menu.addAction('Set topmost', self.topmost_yes)
			button_menu.addAction('Set not topmost', self.topmost_no)
			button_menu.addAction('Set top', self.top_set)
			button_menu.addAction('Bring to top', self.top_bring)
			b = BlueButton(button_menu, item)
			button_menu.setProperty('button', b)  # <menu>.property('button')
			b.setProperty('information', data_for_item(item))
			widgets.append(b)
			# self.flower.add_item(b)
		self.flower.clear_add_items(widgets)

	def list_consoles(self):
		data = getlist()
		from rich.pretty import pprint
		pprint(data)

	def create_cmd(self, CURDIR=None):
		if os.path.isfile(CURDIR):
			CURDIR = os.path.dirname(CURDIR)
		items = create_fill_set(CURDIR=CURDIR)
		self.populate_flowwidget(items)

	def create_cmd_and_type_away(self, CURDIR=None, ketikan=['wsl'], delay_antar_ketikan=0.2):
		if os.path.isfile(CURDIR):
			CURDIR = os.path.dirname(CURDIR)
		items, title, index = create_fill_set_with_id_index(CURDIR=CURDIR)
		self.populate_flowwidget(items)
		for tulisan in ketikan:
			ketik_by_index(index, tulisan)
			if delay_antar_ketikan:
				time.sleep(delay_antar_ketikan)

	def action_to_button(self, pengirim):
		"""
		not really to button, tapi to button info yg berisi hwnd dan chwnd
		hwnd utk operasi2 window
		chwnd utk mengetik
		action punya parent() = menu, menu punya property 'button' = button.
		"""
		menu = pengirim.parent()
		button = menu.property('button')
		# buttontext = button.text()
		buttoninfo = button.property('information')
		return buttoninfo

	def hapus_kosong(self):
		items = hapus_set_combo_items()
		self.populate_flowwidget(items)

	def isi_ulang(self):
		items = fill_set()
		self.populate_flowwidget(items)
		self.list_consoles()

	def type_on_console(self):
		text = self.editor.text().strip()
		if text:
			pengirim = self.sender()
			buttoninfo = self.action_to_button(pengirim)
			console_hwnd = buttoninfo['chwnd'] # utk ngetik pake chwnd.
			ketik_by_hwnd(console_hwnd, text)
			if text not in self.history:
				self.history.append(text)
			self.set_input_completer()

	def toggle_button_visibility(self):
		pengirim = self.sender()
		# teks = pengirim.text() # teks dari menu item
		# menu = pengirim.parent()
		# button = menu.property('button')
		# buttontext = button.text()
		# buttoninfo = button.property('information')
		# # gimana dapatkan text dari button pemilik menu yg menu itemnya diclick?
		# # akses parent: <PyQt5.QtWidgets.QMenu object at 0x00000232D7EEEB00>, jenis <class 'PyQt5.QtWidgets.QMenu'>
		# # parent widget: <PyQt5.QtWidgets.QMenu object at 0x00000232D7EEEB00>, jenis <class 'PyQt5.QtWidgets.QMenu'>
		# # button = 1ebb33661c6211ed902c201e886a9090
		# # informasi dari button = {
		# # 'chwnd': 7406884, 
		# # 'chwnds': [7866208, 30213646, 6031400, 7406884], 
		# # 'cmd': 'cmd /k "title 1ebb33661c6211ed902c201e886a9090"', 
		# # 'hprocess': <PyHANDLE:1444>, 
		# # 'hthread': <PyHANDLE:1636>, 
		# # 'hwnd': 40765404, 
		# # 'id': '1ebb33661c6211ed902c201e886a9090', 
		# # 'pid': 11632, 
		# # 'tid': 10196}
		# print(f"""pengirim {pengirim} dg text: {teks}, jenis pengirim adlh {type(pengirim)}, 
		# akses parent: {pengirim.parent()}, jenis {type(pengirim.parent())}
		# parent widget: {pengirim.parentWidget()}, jenis {type(pengirim.parentWidget())}
		# button = {buttontext}
		# informasi dari button = {buttoninfo}
		# """)
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		if is_window_visible(console_hwnd):
			operate_on_windows_by_hwnd(console_hwnd, 'hide')
		else:
			operate_on_windows_by_hwnd(console_hwnd, 'show')

	def topmost_yes(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		to_top_by_hwnd(console_hwnd, 'topmost')

	def topmost_no(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		to_top_by_hwnd(console_hwnd, 'nottopmost')

	def top_set(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		to_top_by_hwnd(console_hwnd, 'top')

	def top_bring(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		to_top_by_hwnd(console_hwnd, 'bringtop')

	def minimize_window(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		operate_on_windows_by_hwnd(console_hwnd, 'min')

	def maximize_window(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		operate_on_windows_by_hwnd(console_hwnd, 'max')

	def restore_window(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		operate_on_windows_by_hwnd(console_hwnd, 'restore')

	def normal_window(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		operate_on_windows_by_hwnd(console_hwnd, 'normal')

	def close_window(self):
		pengirim = self.sender()
		buttoninfo = self.action_to_button(pengirim)
		console_hwnd = buttoninfo['hwnd']
		operate_on_windows_by_hwnd(console_hwnd, 'close')

# def main():
	# # self.tab_cmder = QWidget(self)
	# # self.tab_cmder.setStyleSheet('background-color: tan;')
	# # layout_for_tab_cmder = QVBoxLayout(self.tab_cmder) # utk content tab 2
	# # layout_for_tab_cmder.addWidget(self.cmder)
	# self.color_widget = ColorWidget()
	# self.button_widget = ButtonWidget()
	# self.cmder = CmderWidget()
	# cmder_color = QSplitter(Qt.Horizontal)
	# cmder_color.addWidget(self.cmder)
	# cmder_color.addWidget(self.color_widget)
	# cmder_color_button = QSplitter(Qt.Vertical)
	# cmder_color_button.addWidget(cmder_color)
	# cmder_color_button.addWidget(self.button_widget)
	# self.main_tab.addTab(cmder_color_button, 'Cmder')


def main():
	app = QApplication([])
	# set_theme(app)
	w = CmderWidget()
	# w.setStyleSheet(background_image_stylesheet)
	w.setStyleSheet("background-color: #ffffff;")
	w.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

