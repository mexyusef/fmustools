from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

import datetime, os, json, re, requests, sys
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# gak perlu reload env kan sudah ada yg ngeload?
import sys
from pathlib import Path
current_file_path = Path(__file__).resolve()
sidoarjodir = current_file_path.parent
# sys.path.append(rootdir)
ciledugdir = r'c:\work\ciledug'
# sys.path.extend([sidoarjodir, schnelldir])
sys.path.extend([sidoarjodir, ciledugdir])

from ciledug.cepat.cepat import processor_mycsv
from ciledug.palsu.palsu import process_palsu_language
# new declang
# C:\work\ciledug\ciledug\ceklang\ceklang.py
from ciledug.ceklang.ceklang import process_new_declanguage

from schnell.app.appconfig import programming_data
from schnell.app.autoutils import alert
# from schnell.app.autoutils import type_by_window_title, prompt, alert, confirm, password
from schnell.app.clipboardutils import trycopy, replace_keyword, indent_convert
from schnell.app.dirutils import joiner, exists_in_dir, joinhere, dirname, bongkar, isfile, isdir, capture_ls, is_valid_path
from schnell.app.fileutils import append_entry_tofile, file_content, get_definition_by_key_permissive_start, get_daftar, is_file_binary
from schnell.app.gptutils import process12_chatgpt, copy_answer_chatgpt
from schnell.app.googleutils import cari_google
from schnell.app.imageutils import show_image_mpl, show_image, show_image_cv, show_image_pygame, microsoft_photos, tampilkan_acdsee
from schnell.app.imageutils import show_image_url_cv, show_image_url_mpl, show_image_url_pygame, show_image_url_tk, microsoft_photos_from_url
from schnell.app.mediautils import internal_image_viewer, internal_image_viewer_from_url, internal_video_viewer
from schnell.app.printutils import indah4
from schnell.app.promptutils import combobox
from schnell.app.stringutils import multi_to_single_line, single_to_multi_line
from schnell.app.systemutils import execute_command

from schnell.creator.context import context as global_context
from schnell.db.replservice import repl_service


# from schnell.gui.system.editor.tkeditor import tkeditor
from schnell.gui.system.editor.vieweditor import open_editor as tkeditor
# C:\Users\usef\work\sidoarjo\schnell\gui\system\editor\editor.py
from schnell.gui.system.editor.editor import editor_nonmain
from schnell.gui.system.searcher.widgets.editor_fmus_mapper import editor_fmus_mapper

from .editor_fmus_helper import execute_code
from .editor_fmus_zpt import process_zpt
from startup import buka as buka_internet
from constants import vscode

zapatafolder = joiner(sidoarjodir, 'database/zpt')
editor_fmus_text_file = joinhere(__file__, 'editor_fmus.txt')
editor_fmus_file = joinhere(__file__, 'editor_fmus_mapper.py')
editor_fmus_help_content = file_content(editor_fmus_file)
# editor_fmus_help = '\n'.join(editor_fmus_mapper.keys())
editor_fmus_help = '\n'.join(f'{k}\n\t{v["desc"]}' for k,v in editor_fmus_mapper.items())
editor_fmus_mapper_local = editor_fmus_mapper

show_image_by = [
	'opencv',
	'pygame',
	'matplotlib',
	# 'ms photos', # 'buggy tk',
	'internal viewer',
]
tab_space_list = [
	'tab => 2 space', # 1
	'tab => 4 space', # 2
	'2 space => tab', # 3
	'4 space => tab', # 4
	'2 space => 4 space', # 5
	'4 space => 2 space', # 6
	'1 backslash => 2 backslash', # 7
	'2 backslash => 1 backslash', # 8
	'\' to "', #9
	'" to \'', #10
	'= to :', #11
	'filepath (content) to base64', #12
	'strip double/single quotes', #13
]


# from PyQt5.Qsci import QsciLexerPython
class SepiaPythonLexer(QsciLexerPython):
	def __init__(self, parent=None, warna=None):
		super().__init__(parent)
		if warna:
			self.warna = warna
		else:
			# https://htmlcolorcodes.com/
			self.warna = "#D2B48C"

	def defaultPaper(self, style):
		# return QColor("#F5DEB3")
		return QColor(self.warna)

class EditorFmus(QsciScintilla):

	save_file = pyqtSignal(bool)
	line_numbers_request = pyqtSignal(tuple)

	# ctrl+k, process_word, 1 baris
	replrequest = pyqtSignal(tuple)
	# ctrl+m, process_fmus, multi baris
	fmusrequest = pyqtSignal(str, int, int, int, int)
	fmus_repl_request = pyqtSignal(str)

	englishrequest = pyqtSignal(str)
	insert_at_top = pyqtSignal(str)
	publishrequest = pyqtSignal(str)


	def currentLine(self):
		# Get the current line number
		current_line = self.SendScintilla(self.SCI_LINEFROMPOSITION, self.SendScintilla(self.SCI_GETCURRENTPOS))

		return current_line

	def goToTop(self):
		# Scroll the current line to the top of the view
		self.SendScintilla(self.SCI_SCROLLCARET)
		# Set the first visible line to the current line
		self.setFirstVisibleLine(self.currentLine())

	def keyPressEvent(self, event):
		"""
		https://www.programcreek.com/python/example/101683/PyQt5.QtCore.Qt.Key_Backspace
		https://www.programcreek.com/python/example/101657/PyQt5.QtCore.Qt.Key_Up
		https://stackoverflow.com/questions/6647970/how-can-i-capture-qkeysequence-from-qkeyevent-depending-on-current-keyboard-layo        
		https://doc.qt.io/qtforpython-5/PySide2/QtCore/Qt.html
		"""
		key = event.key()
		key_modifiers = QApplication.keyboardModifiers()
		event.handled = False

		if (key == Qt.Key_K and key_modifiers == Qt.ControlModifier): # ctrl+k, fmuslang
			# if (key == Qt.Key_Semicolon and key_modifiers == Qt.ControlModifier):
			# self.process_word()
			self.combine_process_fmus_process_word()
			event.handled = True

		elif (key == Qt.Key_K and key_modifiers == (Qt.ControlModifier|Qt.ShiftModifier)): # ctrl+shift+k, ceklang=new declang
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				try:
					hasil = process_new_declanguage(bariskalimat, returning=True)
					self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
				except Exception as err:
					indah4(str(err), warna='red')
			event.handled = True

		elif key == Qt.Key_D and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+d, multiline to single line (collapse)
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:				
				hasil = multi_to_single_line(bariskalimat)
				self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_D and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+d, single line to multiline (expand)
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:				
				hasil = single_to_multi_line(bariskalimat)
				self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_E and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+e, editor_fmus_endpoints
			filepath = joinhere(__file__, 'editor_fmus_endpoints.txt')
			print(filepath)
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			event.handled = True

		elif (key == Qt.Key_G and key_modifiers == Qt.ControlModifier): # ctrl+g, google search
			# kita matikan gpt sialan, ganti dg googler
			self.googler()
			event.handled = True

		elif key == Qt.Key_G and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+g process github
			# TODO: issues, pull requests
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Redis search query is empty [{bariskalimat}].")
			else:
				from .editor_fmus_helper import process_github
				hasil = process_github(bariskalimat)
				if hasil:
					self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
				else:
					print('"hasil = process_github(bariskalimat)" is None. Please cek.')
			event.handled = True

		elif (key == Qt.Key_H and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier)): # ctrl+shift+h, editor_fmus_help
			filepath = joinhere(__file__, 'editor_fmus_help.txt')
			self.insert_and_move_at_cursor(f'\n{filepath}\n' + file_content(filepath) + f'\n{filepath}', next_line=1, column_at_start_line=True)
			event.handled = True

		elif (key == Qt.Key_H and key_modifiers == (Qt.ControlModifier | Qt.AltModifier)): # ctrl+alt+h, dup line
			self.duplicate_line()
			event.handled = True

		elif (key == Qt.Key_I and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier)): # ctrl+shift+i insert filecontent at cursor
			'''
			insert content of current file at line to next line
			'''
			# indah4('ctrl+shift+i', warna='green')			
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				if bariskalimat.count('=')==1:
					filepath, barisentry = [e.strip() for e in bariskalimat.split('=')]
					if isfile(filepath) and not is_file_binary(filepath):
						if barisentry:
							content = get_definition_by_key_permissive_start(filepath, barisentry)
						else: # jk filepath.mk/fmus= tanpa barisentry maka list semua barisentry pd file mk/fmus tsb
							content = get_daftar(filepath, stringified=True)
						self.insert_and_move_at_cursor(content, next_line=1, column_at_start_line=True)
					else:
						alert(f'Unknown file {filepath}', 'Can not read file')
				else:
					filepath = bariskalimat
					if isfile(filepath) and not is_file_binary(filepath):
						content = file_content(filepath)
						self.insert_and_move_at_cursor(content, next_line=1, column_at_start_line=True)
			# self.insert_file_content_at_cursor()
			self.goToTop()
			event.handled = True

		elif (key == Qt.Key_J and key_modifiers == Qt.ControlModifier): # ctrl+j, replify
			# Ctrl+J spt Ctrl+K tetapi prefix dg /R), agar bisa ff, dsb.
			# utk search repl dan tampilkan di yellownote
			self.process_word(prefix='/R)')
			event.handled = True

		elif key == Qt.Key_M and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+m, editor_fmus_models
			filepath = joinhere(__file__, 'editor_fmus_models.txt')
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_M and key_modifiers == (Qt.ControlModifier | Qt.AltModifier | Qt.ShiftModifier): # ctrl+alt+m, editor_fmus_mem
			filepath = joinhere(__file__, 'editor_fmus_mem.txt')
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		# elif key == Qt.Key_M and key_modifiers == (Qt.ControlModifier | Qt.AltModifier | Qt.ShiftModifier): # ctrl+shift+alt+m
		# 	self.process_mapper()
		# 	event.handled = True

		elif key == Qt.Key_P and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+p, editor_fmus_portfolio.txt
			filepath = joinhere(__file__, 'editor_fmus_portfolio.txt')
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_P and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+p run program
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Program to execute is empty [{bariskalimat}].")
			else:
				# execute_code(bariskalimat, language=context['current_active_language'])
				execute_code(bariskalimat, language=programming_data['language'])
			event.handled = True

		elif key == Qt.Key_S and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+s read paragraph
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Paragraph to speak is empty [{bariskalimat}].")
			else:
				from .editor_fmus_helper import read_paragraph
				read_paragraph(bariskalimat)
			event.handled = True

		elif key == Qt.Key_T and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+t, editor_fmus_todo
			filepath = joinhere(__file__, 'editor_fmus_todo.txt')
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_U and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+u url shorteners
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"url shorteners is empty [{bariskalimat}].")
			else:
				from schnell.app.shortenerutils import bitly, clickru, dagd, isgd, osdb, tinyurl
				res = None
				if '|' in bariskalimat:
					provider, url = [e.strip() for e in bariskalimat.split('|',1)]
					if provider in ['b', 'bitly']:
						res = bitly(url)
					elif provider in ['c', 'clickru']:
						res = clickru(url)
					elif provider in ['d', 'dagd']:
						res = dagd(url)
					elif provider in ['i', 'isgd']:
						res = isgd(url)
					elif provider in ['o', 'osdb']:
						res = osdb(url)
					elif provider in ['t', 'tiny', 'tinyurl']:
						res = tinyurl(url)
				else:
					res = bitly(bariskalimat)
				if res:
					self.insert_and_move_at_cursor('\n' + res, next_line=1, column_at_start_line=True)
			event.handled = True

		elif (key == Qt.Key_W and key_modifiers == Qt.ControlModifier): # ctrl+w, englisch
			self.process_english()

		elif key == Qt.Key_W and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+w process twitter
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Query for process_twitter is empty [{bariskalimat}].")
			else:
				from .editor_fmus_helper import process_twitter
				sisipkan = lambda content: self.insert_and_move_at_cursor(content, next_line=1, column_at_start_line=True)
				process_twitter(bariskalimat, sisipkan, num_tweets=25)
			event.handled = True

		elif (key == Qt.Key_X and key_modifiers == (Qt.ControlModifier|Qt.AltModifier)): # ctrl+alt+x utk explorer
			# self.process_translate() # ini gagal, mari kita ubah ke: code ... filepath
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				bariskalimat = bongkar(bariskalimat)
				# execute_command(f'{vscode} {bariskalimat}')
				# err...ini jadi bikin hanya proses yg sudah ada file/dir, justeru pengen bisa yg belum ada
				# hanya perlu detek jk bentuk itu bener berbentuk filepath atau tidak
				if is_valid_path(bariskalimat):
					# execute_command(f'{vscode} {bariskalimat}')
					os.system(f'explorer {bariskalimat}')
				else:
					alert(f'{bariskalimat} is not serious', 'Error opening file')
			event.handled = True

		elif key == Qt.Key_Z and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+z search redis
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Redis search query is empty [{bariskalimat}].")
			else:
				from .editor_fmus_helper import zpt_redis_search
				zpt_redis_search(bariskalimat)
			event.handled = True

		elif (key == Qt.Key_Z and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier)): # ctrl+shift+z, editor-fmus-1.txt
			perbandingan = joinhere(__file__, 'editor_fmus_1.txt')
			# print('harusnya load isi', perbandingan)
			hasil = file_content(perbandingan) + '\n' + perbandingan
			self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif (key == Qt.Key_1 and key_modifiers == Qt.ControlModifier): # ctrl+1, ctrl+shift+1==! (decode)
			self.insert_time()
			event.handled = True

		elif (key == Qt.Key_2 and key_modifiers == Qt.ControlModifier): # ctrl+2, show image+text
			# skip selection, langsung pake internal viewer
			# got = combobox(show_image_by)
			# if got == show_image_by[0]:
			#     self.show_image_at_line(4)
			# elif got == show_image_by[1]:
			#     self.show_image_at_line(5)
			# elif got == show_image_by[2]:
			#     self.show_image_at_line()
			# elif got == show_image_by[3]:
			#     self.show_image_at_line(3)
			self.show_image_at_line(3)
			event.handled = True

		# sementara kita matikan ini, lebih baik gunakan tkinter app yg milih tab space choice
		# elif key == Qt.Key_Exclam and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
		#     self.convert_space_tab(which=1)
		#     event.handled = True
		# elif key == Qt.Key_At and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
		elif key == Qt.Key_3 and event.modifiers() == (Qt.ControlModifier): # ctrl+3, tab-space
			got = combobox(tab_space_list)
			if got == tab_space_list[0]:
				self.convert_space_tab(which=1)
			elif got == tab_space_list[1]:
				self.convert_space_tab(which=2)
			elif got == tab_space_list[2]:
				self.convert_space_tab(which=3)
			elif got == tab_space_list[3]:
				self.convert_space_tab(which=4)
			elif got == tab_space_list[4]:
				self.convert_space_tab(which=5)
			elif got == tab_space_list[5]:
				self.convert_space_tab(which=6)
			elif got == tab_space_list[6]:
				# replace_single_backslash_with_double
				self.single_double_backslash()
			elif got == tab_space_list[7]:
				self.single_double_backslash(False)

			elif got == tab_space_list[8]:
				self.single_double_quote()
			elif got == tab_space_list[9]:
				self.single_double_quote(False)
			elif got == tab_space_list[10]:
				self.char_to_char(src='=', dst=':')
			elif got == tab_space_list[11]:
				self.insert_encode_filepath()
			elif got == tab_space_list[12]:
				bariskalimat = self.get_line_or_selected_text().strip()
				if bariskalimat:
					result = bariskalimat.strip('"').strip("'")
					self.replace_selection_in_editor(result)
			event.handled = True

		elif key == Qt.Key_4 and event.modifiers() == (Qt.ControlModifier): # ctrl+4, bard
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				from .editor_fmus_zpt import bard_prompt
				result = bard_prompt(bariskalimat)
				self.insert_and_move_at_cursor('\n' + result, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_Dollar and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+$ (cs4) ls folder
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Ctrl+4 capture_ls is empty [{bariskalimat}].")
			else:
				bariskalimat = bongkar(bariskalimat)
				if isdir(bariskalimat):
					content = capture_ls(bariskalimat)
					self.insert_and_move_at_cursor('\n' + content, next_line=1, column_at_start_line=True)
			event.handled = True

		# elif key == Qt.Key_NumberSign and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
		#     self.convert_space_tab(which=3)
		#     event.handled = True
		# elif key == Qt.Key_Percent and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
		#     self.convert_space_tab(which=5)
		#     event.handled = True

		elif (key == Qt.Key_5 and key_modifiers == Qt.ControlModifier): # ctrl+5, zpt
			bariskalimat = self.get_line_or_selected_text().strip()
			# print(f'zpt: {bariskalimat}.')
			result = process_zpt(bariskalimat)
			self.insert_and_move_at_cursor(result, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_Percent and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+% (cs5) zpt image
			'''
			default:
				n=1
				filepath_or_dirpath=filepath
				sz=256
				n<16
				sz>16
			n,sz/prompt|filepath_or_dirpath
			n,sz/image_input|filepath_or_dirpath
			'''
			from .editor_fmus_zpt import wrap_process_zpt_image, wrap_process_zpt_image_variation
			# wrap_process_zpt_image(filepath_or_dirpath, prompt, n=1, size='512x512')
			# wrap_process_zpt_image_variation(filepath_or_dirpath, image_input, n=1, size='512x512')
			bariskalimat = self.get_line_or_selected_text().strip()
			if '|' in bariskalimat:
				prompt, filepath_or_dirpath = [e.strip() for e in bariskalimat.split('|')]
				if '/' in prompt:
					n = 1
					sz = '256x256'
					for item in [e.strip() for e in prompt.split(',')]:
						if int(item)<16:
							n = int(item)
						else:
							sz = f'{item}x{item}'
					if isfile(prompt):
						# request variation
						wrap_process_zpt_image_variation(filepath_or_dirpath, prompt, n=n, size=sz)
					else:
						# request generation/create
						print(f'wrap_process_zpt_image with n={n}, size={sz} to {filepath_or_dirpath}')
						wrap_process_zpt_image(filepath_or_dirpath, prompt, n=n, size=sz)
				else:
					if isfile(prompt):
						# request variation, ctrl+shift+%
						# C:\fr\belum-coded\tidurkaty10.jpg|C:\fr\hasil-dari-ai.jpg
						wrap_process_zpt_image_variation(filepath_or_dirpath, prompt)
					else:
						# request generation/create
						print(f'wrap_process_zpt_image with default n and size to {filepath_or_dirpath}')
						wrap_process_zpt_image(filepath_or_dirpath, prompt)
			event.handled = True

		elif (key == Qt.Key_6 and key_modifiers == Qt.ControlModifier): # ctrl+6, open file in transed/tkeditor/np++
			# self.show_image_at_line(6)
			from schnell.app.threadutils import mulai
			from schnell.app.systemutils import noteplusplus, transeditor
			bariskalimat = self.get_line_or_selected_text().strip()
			editor_choices = programming_data['j']["schnell"]["gui"]["system"]["searcher"]["widgets"]["editor_fmus"]["ctrl+6:choices"]
			editor_trans = programming_data['j']["editors"]['TRANS']
			got = combobox(editor_choices).lower()
			if 'trans' in got:
				mulai(transeditor, (f"--filepath bariskalimat",))
			elif 'tkedit' in got:
				if not is_file_binary(bariskalimat):
					tkeditor(bariskalimat)
			elif 'notepad++' in got:				
				mulai(noteplusplus, (bariskalimat,))
			event.handled = True

		elif key == Qt.Key_AsciiCircum  and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # c+s+^ = c+s+6 = T:...(lara) ... utk zpt
			from schnell.autolang import handle_typing
			zpt_choice = programming_data['zpt']
			zpt_title = 'lara 01031995' if zpt_choice=='lara' else ('gaia 01031997' if zpt_choice=='gaia' else 'wieke 01031999')
			bariskalimat = self.get_line_or_selected_text().strip()
			# hilangkan newline agar chat input gak dipotong, ganti jd space utk "join"
			bariskalimat = bariskalimat.replace('\n', ' ')
			if bariskalimat:
				handle_typing(f'T:({zpt_title})~1000,900/~1000,900|'+bariskalimat)
			event.handled = True

		elif (key == Qt.Key_7 and key_modifiers == Qt.ControlModifier): # ctrl+7 open file in vscode => /au)
			# krn open di vscode tinggal pake ctrl+/, kita ganti saja ke /au)
			# self.show_image_at_line(7)
			bariskalimat = '/au)' + self.get_line_or_selected_text().lstrip()  #.strip()
			self.fmus_repl_request.emit(bariskalimat)
			event.handled = True

		elif (key == Qt.Key_7 and key_modifiers == (Qt.ControlModifier|Qt.AltModifier)): # ctrl+alt+7 open file in notepad++
			bariskalimat = self.get_line_or_selected_text().strip()
			print(f'proses [{bariskalimat}] di notepad++')
			from schnell.app.systemutils import noteplusplus
			from schnell.app.threadutils import mulai
			# noteplusplus(bariskalimat)
			mulai(noteplusplus, (bariskalimat,))
			event.handled = True

		elif key == Qt.Key_Ampersand and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+& (cs7) publish filecontent to yellow
			'''
			if key == Qt.Key_Ampersand and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
			insert to yellow note
			'''
			indah4('ctrl+shift+&', warna='green')
			self.insert_file_content_at_cursor(publish_to_yellow=True)
			event.handled = True

		elif (key == Qt.Key_8 and key_modifiers == Qt.ControlModifier): # ctrl+8 open url
			# self.show_image_at_line(8)
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				self.open_url(bariskalimat)
			event.handled = True

		elif (key == Qt.Key_8 and key_modifiers == (Qt.ControlModifier|Qt.AltModifier)): # ctrl++alt+8 utk click:()x,y/x,y utk "new chat" di zpt
			from schnell.autolang import process_language
			zpt_choice = programming_data['zpt']
			zpt_title = 'lara 01031995' if zpt_choice=='lara' else ('gaia 01031997' if zpt_choice=='gaia' else 'wieke 01031999')
			# self.show_image_at_line(8)
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				alert('Percobaan ctrl+shift+8 sebelum click:()x,y/x,y =>', bariskalimat)
				process_language(f'click:({zpt_title})100,125/100,125')
			event.handled = True

		elif (key == Qt.Key_9 and key_modifiers == Qt.ControlModifier): # ctrl+9 replace $01 $02 etc dari input
			self.replace_keyword_from_userinput()
			event.handled = True

		elif key == Qt.Key_ParenLeft and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+( (cs9) create file in curdir
			self.create_new_file_at_curdir()
			event.handled = True

		elif (key == Qt.Key_0 and key_modifiers == Qt.ControlModifier): # ctrl+0, speech to text (jangan kebalik dg cs0 yg copy to clipboard)
			from schnell.app.speechutils import record_audio_timed, record_audio_timed_threaded
			# jangan next line, dan jangan dari kolom 0
			sisipkan = lambda content: self.insert_and_move_at_cursor(content, next_line=0, column_at_start_line=False)
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat and bariskalimat.isdigit():
				lama = int(bariskalimat)
				# record_audio_timed(lama, print_callback=sisipkan)
				record_audio_timed_threaded(lama, print_callback=sisipkan)
			else:
				# record_audio_timed(print_callback=sisipkan)
				record_audio_timed_threaded(print_callback=sisipkan)
			event.handled = True

		elif key == Qt.Key_ParenRight and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+) (cs0) copy to clipboard
			self.copy_to_clipboard()
			event.handled = True

		elif key == Qt.Key_Underscore and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+_ editor_fmus_proglang
			# entah kenapa ) Key_ParenRight gak bisa jalan.
			# kita masih punya Key_Minus, Key_Plus, Key_Equal
			#bikin_meme_dong()
			# kita load isi dari editor_fmus
			perbandingan = joinhere(__file__, 'editor_fmus_proglang.txt')
			# print('harusnya load isi', perbandingan)
			hasil = file_content(perbandingan) + '\n' + perbandingan
			self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_Plus and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift++ utk info bikin proyek baru
			perbandingan = joinhere(__file__, 'editor_fmus_projects.txt')
			hasil = file_content(perbandingan)
			self.insert_and_move_at_cursor(perbandingan + '\n' + hasil + '\n' + perbandingan, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_BraceLeft and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+{ hapus atas
			self.remove_above_selection()
			event.handled = True

		elif key == Qt.Key_BraceRight and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+} hapus bawah
			self.remove_below_selection()
			event.handled = True

		elif key == Qt.Key_QuoteDbl and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+" command_prompt_data/extension+(global) context
			from .editor_fmus_ketik import process_ketik
			bariskalimat = self.get_line_or_selected_text().strip()
			result = ''
			if bariskalimat:
				result = process_ketik(bariskalimat)
			else:
				result = process_ketik()
			if result:
				if isinstance(result, (list, dict)):
					result = json.dumps(result, indent=2)
				elif isinstance(result, (int, float, datetime.datetime)):
					result = str(result)
				self.insert_and_move_at_cursor(result, next_line=1, column_at_start_line=True)
			event.handled = True

		elif (key_modifiers == Qt.ControlModifier and key == Qt.Key_Apostrophe): # ctrl+' dictionary
			self.process_dictionary()
			event.handled = True

		elif key == Qt.Key_Apostrophe and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+' toggle ' dan "
			self.process_quote()
			event.handled = True

		elif (key == Qt.Key_Semicolon and key_modifiers == Qt.ControlModifier): # ctrl+; github list repos
			self.list_github_repos()
			event.handled = True

		elif key == Qt.Key_Semicolon and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+; open github, krn ctrl+shift+: gak bisa
			# self.list_github_repos()
			bariskalimat = self.get_line_or_selected_text().strip()
			
			if bariskalimat:
				urlpath = bariskalimat
				if urlpath.startswith('https://github'):
					self.open_url(urlpath)
				else:
					urlpath = urlpath.removeprefix('/')
					if urlpath.count('/')==0:
						urlpath += '?tab=repositories'
					urlpath = 'https://github.com/' + urlpath
					self.open_url(urlpath)
			event.handled = True

		elif key == Qt.Key_Less and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+< fold
			# from schnell.creator.context import context
			self.foldAll()
			# global_context['fmus_editor_folding'] = not global_context['fmus_editor_folding']
			# if global_context['fmus_editor_folding']:
			#     self.foldAll()
			# else:
			#     self.clearFolds()
			event.handled = True

		elif key == Qt.Key_Less and event.modifiers() == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+< unfold
			# from schnell.creator.context import context
			self.clearFolds()
			# global_context['fmus_editor_folding'] = not global_context['fmus_editor_folding']
			# if global_context['fmus_editor_folding']:
			#     self.foldAll()
			# else:
			#     self.clearFolds()
			event.handled = True

		elif key == Qt.Key_Greater and event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+> actor
			self.process_actor()
			event.handled = True

		elif (key == Qt.Key_Slash and key_modifiers == Qt.ControlModifier): # ctrl+/ google translate => ubah ke code <filepath>
			# self.process_translate() # ini gagal, mari kita ubah ke: code ... filepath
			bariskalimat = self.get_line_or_selected_text().strip()
			if bariskalimat:
				bariskalimat = bongkar(bariskalimat)
				# execute_command(f'{vscode} {bariskalimat}')
				# err...ini jadi bikin hanya proses yg sudah ada file/dir, justeru pengen bisa yg belum ada
				# hanya perlu detek jk bentuk itu bener berbentuk filepath atau tidak
				if is_valid_path(bariskalimat):
					execute_command(f'{vscode} {bariskalimat}')
				else:
					alert(f'{bariskalimat} is not serious', 'Error opening file')
			event.handled = True

		elif (key == Qt.Key_Backslash and key_modifiers == Qt.ControlModifier): # ctrl+\ hapus atas dan bawah
			# # elif (key == Qt.Key_BracketLeft and key_modifiers == Qt.ControlModifier):
			# # self.process_english()
			# global_context['fmus_expansion_mode'] = not global_context['fmus_expansion_mode']
			# self.mkhelp.toggle_expansion_button.setChecked(global_context['fmus_expansion_mode'])
			# self.mkhelp.reopen_last_file()
			# self.remove_below_selection()
			# self.remove_above_selection()
			self.remove_context_selection()
			event.handled = True

		elif key == Qt.Key_Backslash and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+\ toggle \ dan /
			self.process_backslash()
			event.handled = True

		elif key == Qt.Key_Bar and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+\ = ctrl+shift+| tambah wsl tree + wsl path
			# print('self.process_backslash(wsl_tree=True)')
			self.process_backslash(wsl_tree=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_Backtab and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+tab sama dg c-s-a-m mapper, agar lebih cepat
			# dari shift+tab kita ubah ke ctrl+tab soalnya shift+tab dipake utk mundurkan indented text
			# ctrl+tab gak jalan, coba ctrl+shift+tab
			self.process_mapper()
			event.handled = True

		elif key == Qt.Key_PageDown and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+pgdn, fakerlang, palsulang
			# self.process_mapper()
			# kita ganti saja ke /palsu)...
			bariskalimat = self.get_line_or_selected_text().strip()
			try:
				result = process_palsu_language(bariskalimat, returning=True)
			except Exception as err:
				result = str(err)
			if result:
				if isinstance(result, list):
					result = '\n'.join(result)
				self.insert_and_move_at_cursor(result, next_line=1, column_at_start_line=True)
			else:
				self.insert_and_move_at_cursor('NO RESULT!', next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_PageDown and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+pgdn desanitize selection
			# sanitize
			self.desanitize_current_selection()
			event.handled = True

		elif key == Qt.Key_PageUp and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+pgup: cepat
			bariskalimat = self.get_line_or_selected_text().strip()
			result = processor_mycsv(bariskalimat, returning=True)
			if result:
				if isinstance(result, list):
					result = '\n'.join(result)
				self.insert_and_move_at_cursor(result, next_line=1, column_at_start_line=True)
			else:
				self.insert_and_move_at_cursor('NO RESULT!', next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_Left and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+left csvlang ke yellow
			self.process_csvlang()
			event.handled = True

		elif key == Qt.Key_Right and key_modifiers == (Qt.ControlModifier | Qt.AltModifier): # ctrl+alt+right lalang ke yellow
			self.process_lalang()
			event.handled = True

		elif key == Qt.Key_Question and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+? file reference.txt, jangan cs-right yg dipake utk pindah cursor
			filepath = joinhere(__file__, 'editor_fmus_reference.txt')
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_Up and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+up replservice, insert here
			self.process_replservice()
			event.handled = True

		elif key == Qt.Key_Down and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+down, daftar keys
			filepath = joinhere(__file__, 'editor_fmus.txt')
			self.insert_and_move_at_cursor(file_content(filepath) + '\n' + filepath, next_line=1, column_at_start_line=True)
			event.handled = True

		elif key == Qt.Key_AsciiTilde and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+~ encrypt
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Codec query is empty [{bariskalimat}].")
			else:
				from .editor_fmus_helper import wieke
				# hasil = process_github(bariskalimat)
				# self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
				# self.publishrequest.emit(f"ENCRYPTING [{bariskalimat}].")
				sisipkan = lambda content: self.insert_and_move_at_cursor('\n' + content, next_line=1, column_at_start_line=True)
				publishkan = lambda content: self.publishrequest.emit(content)
				wieke(bariskalimat, sisipkan, publishkan)
			event.handled = True

		elif key == Qt.Key_Exclam and key_modifiers == (Qt.ControlModifier | Qt.ShiftModifier): # ctrl+shift+! decrypt
			bariskalimat = self.get_line_or_selected_text().strip()
			if not bariskalimat:
				self.publishrequest.emit(f"Codec query is empty [{bariskalimat}].")
			else:
				from .editor_fmus_helper import gaia
				# hasil = process_github(bariskalimat)
				# self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
				# self.publishrequest.emit(f"DECRYPTING [{bariskalimat}].")
				sisipkan = lambda content: self.insert_and_move_at_cursor('\n' + content, next_line=1, column_at_start_line=True)
				publishkan = lambda content: self.publishrequest.emit(content)
				gaia(bariskalimat, sisipkan, publishkan)
			event.handled = True

		elif key == Qt.Key_F7:  # ctrl+f7 = parse python file
			from schnell.app.ivyutils import file_to_parsetree
			from schnell.app.redisutils import handle_publish_to_redis
			code = self.get_line_or_selected_text().strip()
			print(f'Getting [{code}]')
			if code:
				publish_to_yellownote = False
				if code.startswith('*'):
					code = code.removeprefix('*').strip()
					publish_to_yellownote = True
				code = bongkar(code)
				if code and isfile(code):
					print(f'Processing [{code}]')
					result = file_to_parsetree(code)
					if publish_to_yellownote:
						handle_publish_to_redis(result)
					else:
						self.insert_and_move_at_cursor(result, next_line=1, column_at_start_line=True)
			else:
				handle_publish_to_redis("No code")
			event.handled = True

		elif key == Qt.Key_F3:  # ctrl+f3, spiff.txt
			perbandingan = r'C:\work\kenza\editor_fmus\spiff.txt'
			hasil = file_content(perbandingan) + '\n' + perbandingan
			self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_F8:  # ctrl+f8 = list of commands, editor_fmus_2.txt
			perbandingan = joinhere(__file__, 'editor_fmus_2.txt')
			hasil = file_content(perbandingan) + '\n' + perbandingan
			self.insert_and_move_at_cursor(hasil, next_line=1, column_at_start_line=True)
			self.goToTop()
			event.handled = True

		elif key == Qt.Key_F12:  # ctrl+f12, edit last file
			self.handle_f12()
			event.handled = True

		if not event.handled:
			super().keyPressEvent(event)

	def insert_at_top_handler(self, content):
		if not content.endswith('\n'):
			content += '\n'
		self.insertAt(content, 0, 0)

	def insert_at_newline(self, content, baris, kolom):
		if not content.endswith('\n'):
			content += '\n'
		self.insertAt(content, baris, kolom)

	def insert_and_move_at_cursor(self, content, next_line=0, column_at_start_line=False):
		current_line, current_column = self.getCursorPosition()
		insert_start_row = current_line+next_line
		insert_start_col = 0 if column_at_start_line else current_column
		self.insertAt(content, insert_start_row, insert_start_col)
		# setCursorPosition(self, line: int, index: int)
		self.setCursorPosition(insert_start_row, insert_start_col+len(content))
		if programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['editor_fmus']['fold_after_insert']:
			self.foldAll() # biar lebih rapi

	def show_image_at_line(self, viewer=2):
		"""
		2 = mpl
		3 = tk
		4 = cv
		5 = pygame
		"""
		text, _, _ = self.get_current_line_text()
		text = text.strip()
		print(f"show_image_at_line, text = [{text}], viewer = {viewer}.")
		if text:
			# cek jk ada $$link=, maka ctrl+6 bisa lihat file ybs (biasanya ada #$$link=)
			# ini agar bisa view tentunya

			ask_url = text.startswith('http') or text.startswith('localhost') or re.match(
	r"(?i)\b((?:(?:https?|ftp)://)|(?:www\.))"
	r"[-a-z0-9+&@#/%?=~_|!:,.;]*[-a-z0-9+&@#/%=~_|]"
	, text
)

			if not ask_url:
				filepath = bongkar(text)
				# ask_file = isfile(filepath)
			else:
				# ask_file = isfile(text)
				filepath = text

			print(f"text = [{text}], filepath = [{filepath}]")

			# utk hadapi
			# text = # $$link=ULIBPY_ROOTDIR/database/quicks/languages/c++/-boot.txt=default,
			# filepath = # $link=C:\Users\usef\work\sidoarjo\database\quicks\languages\c++\-boot.txt=default
			# entah kenapa stlh env replace, $$Link jadi $link
			dua = '$$link=' in filepath
			satu = '$link=' in filepath
			if dua or satu:
				if dua:
					filepath = filepath.split('$$link=')[1]
				elif satu:
					filepath = filepath.split('$link=')[1]
				print('relinking $$/$link #1:', filepath)
				if '=' in filepath:
					# filepath=barisentry
					filepath = filepath.split('=')[0]
					print('relinking $$/$link #2:', filepath)

			ask_file = isfile(filepath)

			if ask_file or ask_url or isdir(filepath):
				if ask_file and filepath.endswith('.mp4'):
					internal_video_viewer(filepath)
				elif viewer == 2:
					if ask_url:
						try:
							show_image_url_mpl(filepath)
						except Exception as err:
							print(err)
					else:
						show_image_mpl(filepath)
				elif viewer == 3:
					if ask_url:
						try:
							# show_image_url_tk(filepath)
							# microsoft_photos_from_url(filepath)
							# self.mkhelp.filemanager.show_image_from_url(filepath)
							internal_image_viewer_from_url(filepath, show_text_file=self.sisipkan)
						except Exception as err:
							print(err)
					else:
						# show_image(filepath)
						# microsoft_photos(filepath)
						# tampilkan_acdsee(filepath)
						# self.mkhelp.filemanager.show_image(filepath)
						internal_image_viewer(filepath)
				elif viewer == 4:
					if ask_url:
						try:
							show_image_url_cv(filepath)
						except Exception as err:
							print(err)
					else:
						show_image_cv(filepath)
				elif viewer == 5:
					if ask_url:
						try:
							show_image_url_pygame(filepath)
						except Exception as err:
							print(err)
					else:
						show_image_pygame(filepath)
				elif viewer == 6:
					print('ctrl 6, filepath:', filepath)
					# filepath = bongkar(filepath)
					if not is_file_binary(filepath):
						print(f"viewing file {filepath}")
						tkeditor(filepath)
						# editor_nonmain(filepath)
					else:
						print(f'file {filepath} is binary')
				elif viewer == 7 and (ask_file or isdir(filepath)):
					print('ctrl 7, filepath:', filepath)
					if isdir(filepath) or (not is_file_binary(filepath)):
						if ' ' in filepath:
							os.system(f'{vscode} "{filepath}"')
						else:
							os.system(f'{vscode} {filepath}')
				elif viewer == 8 and ask_url:
					from schnell.app.browserutils import buka
					print('opening url:', filepath)
					buka(filepath)
			else:
				from schnell.app.promptutils import information, message_box_application
				print(f'{filepath} is not ask_file={ask_file}')
				# information('NOT FOUND', f'{filepath} NOT FOUND')
				message_box_application('NOT FOUND', f'{filepath} NOT FOUND')

	def open_url(self, urlpath):
		from schnell.app.systemutils import firefox_profiles, open_url_with_firefox
		# from schnell.app.browserutils import buka		
		if '|' in urlpath:
			firefox_profiles_ = firefox_profiles()
			firefox_profile, url = [e.strip() for e in urlpath.split("|")]
			if firefox_profile == '*':  # *|url utk list profile
				content = '\n'.join(firefox_profiles_)
				self.insert_and_move_at_cursor(content, next_line=0, column_at_start_line=False)
			else:
				wanted = firefox_profile.lower()
				if wanted in firefox_profiles_:
					open_url_with_firefox(url, wanted)
				else:
					found = [item for item in firefox_profiles_ if wanted in item]
					if found:
						wanted = found[0]
						open_url_with_firefox(url, wanted)
		else:
			buka_internet(urlpath)

	def insert_time(self):
		from schnell.app.timeutils import diary_time
		bariskalimat = diary_time()
		current_line, current_column = self.getCursorPosition()
		self.insertAt(bariskalimat, current_line, current_column)
		# setCursorPosition(self, line: int, index: int)
		self.setCursorPosition(current_line, current_column+len(bariskalimat))

	def gpt_activate_and_prompt(self):
		# process12_chatgpt(prompt, title_query='chatgpt mozilla firefox -visual -wasp', x=660,y=920)
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		trycopy(bariskalimat)
		process12_chatgpt(bariskalimat)

	def gpt_copy(self):
		copy_answer_chatgpt(tinggi_untuk_select_copy=1/4)

	def ctrl9_to_zapata(self):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		# alert(bariskalimat)
		lineskalimat = bariskalimat.splitlines()
		# jk header pertama adlh spesifikasi file mk utk memasukkan data
		if lineskalimat[0].startswith(':'):
			print('masuk :filename')
			mkfilename = lineskalimat[0].removeprefix(':') + ('.mk' if not lineskalimat[0].endswith('.mk') else '')
			mkfilepath = joiner(zapatafolder, mkfilename)
			print('filepath jadinya:', mkfilepath)
			baris_entry = lineskalimat[1]
			isi_entry = '\n'.join(lineskalimat[2:])
			print(f"title = {baris_entry}, content = {isi_entry}")
			append_entry_tofile(mkfilepath, baris_entry, isi_entry)
		else:
			mkfilename = 'history.mk'
			mkfilepath = joiner(zapatafolder, mkfilename)
			baris_entry = lineskalimat[0]
			isi_entry = '\n'.join(lineskalimat[1:])
			append_entry_tofile(mkfilepath, baris_entry, isi_entry)
		alert(isi_entry, f'{mkfilepath}:{baris_entry}')

	def get_current_line_text(self):
		current_line, current_column = self.getCursorPosition()
		panjang_baris = self.lineLength(current_line)
		# baris, kolom, barisakhir, kolomakhir = self.get_first_selection_only()
		start = self.positionFromLineIndex(current_line, 0)  # dari awal baris
		end = self.positionFromLineIndex(current_line, panjang_baris)  # termasuk newline
		bariskalimat = self.text(start, end)  # JANGAN strip newline
		return bariskalimat, current_line, current_column

	def gpt_printer(self, bariskalimat):
		current_line, current_column = self.getCursorPosition()
		self.insertAt(bariskalimat, current_line + 1, 0)
		# setCursorPosition(self, line: int, index: int)
		self.setCursorPosition(current_line + 1, 0)

	def get_selections(self):
		# Get the selection and store them in a list
		selections = []
		for i in range(self.SendScintilla(self.SCI_GETSELECTIONS)):
			selection = (
				self.SendScintilla(self.SCI_GETSELECTIONNSTART, i),
				self.SendScintilla(self.SCI_GETSELECTIONNEND, i)
			)
			# Add selection to list
			from_line, from_index = self.lineIndexFromPosition(selection[0])
			to_line, to_index = self.lineIndexFromPosition(selection[1])
			# selections.append((from_line, to_line))
			selections.append((from_line, from_index, to_line, to_index))

			# https://docs.huihoo.com/pyqt/QScintilla2/functions_w.html
			# self.wordAtLineIndex(from_line, from_index)
			# self.wordAtLineIndex(from_line, 0) # dari awal baris

		selections.sort()
		# Return selection list
		return selections

	def get_first_selection_only(self):
		selections = self.get_selections()
		if selections == None:
			return None
		return selections[0]  # nilai (x,y) dimana kita hanya pake x = from_line, krn y pasti sama dg x utk no-selection

	def duplicate_line(self):
		"""
		"""
		current_line, current_column = self.getCursorPosition()
		panjang_baris = self.lineLength(current_line)
		# baris, kolom, barisakhir, kolomakhir = self.get_first_selection_only()
		start = self.positionFromLineIndex(current_line, 0)  # dari awal baris
		end = self.positionFromLineIndex(current_line, panjang_baris)  # termasuk newline
		bariskalimat = self.text(start, end)  # JANGAN strip newline
		if not bariskalimat.endswith('\n'):
			bariskalimat += '\n'
		if not self.text().endswith('\n'):
			self.append('\n')
		self.insertAt(bariskalimat, current_line + 1, 0)  # duplicate di next line at col 0

	def process_word(self, prefix=''):
		"""
		TODO:
		sementara kita hanya proses dari awal baris ke akhir baris
		perlu juga bisa multiple line dari fromline ke toline
		krn agar bisa run fmus
		jadi hrs terima fromline dan toline selain fromindex dan toindex
		jadi mestinya bisa:
		barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()

		masih belum tau cara get current line text
		ide #1: setSelectionToEol(True), lalu get_first_selection_only
		ide #2:
		https://github.com/jacobslusser/ScintillaNET/issues/512
		string blah = scintilla.Lines[scintilla.CurrentLine].Text;

		ide baru:
		ternyata ada yg namanya lineLength(line)
		"""
		# self.setSelectionToEol(True)  # ini gagal
		# ide dari: https://stackoverflow.com/questions/69291478/move-text-cursor-of-qsciscintilla-to-the-left-or-right-in-pyqt5
		current_line, current_column = self.getCursorPosition()
		panjang_baris = self.lineLength(current_line)
		baris, kolom, barisakhir, kolomakhir = self.get_first_selection_only()
		bariskata = self.wordAtLineIndex(baris, kolom)  # kata under cursor gak berguna krn skip puncs
		start = self.positionFromLineIndex(baris, 0)  # dari awal baris
		# end = self.positionFromLineIndex(baris, kolom)  # sampai cursor di baris yg sama
		# end = self.positionFromLineIndex(baris, kolomakhir)  # sampai kolom akhir pada baris sama, utk selek 1 baris
		end = self.positionFromLineIndex(baris, panjang_baris)  # termasuk newline
		bariskalimat = prefix + self.text(start, end).strip()  # strip newline
		self.replrequest.emit((bariskalimat, baris))

	def handle_f12(self):
		# /R)f12 ini masuk ke fmus.process() masuk ke /quick lang, lalu replify.py
		self.replrequest.emit((f'/R)f12', 0))  # baris ini dummy, jadi masukkan saja 0

	def process_fmus(self):
		"""
		"""
		bariskalimat, barismulai, kolommulai, barisakhir, kolomakhir = self.get_selected_text()
		self.fmusrequest.emit(bariskalimat, barismulai, kolommulai, barisakhir, kolomakhir)

	def replace_keyword_from_userinput(self):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
			# bariskalimat, baris, start, end = self.get_line_text(return_line_start_end=True)
			baris, current_column = self.getCursorPosition()
			start = 0
			end = self.lineLength(baris)
			# set selection utk current line
			# virtual void setSelection (int lineFrom, int indexFrom, int lineTo, int indexTo)
			# bariskalimat, baris, start, end
			self.setSelection(baris, start, baris, end)

		if bariskalimat.strip():
			# input from user
			content = replace_keyword(bariskalimat)
			# replace text if input valid
			if content:
				self.replaceSelectedText(content)

	def select_current_line_where_cursor_is(self):
		baris, current_column = self.getCursorPosition()
		start = 0
		end = self.lineLength(baris)
		self.setSelection(baris, start, baris, end)

	def replace_selection_in_editor(self, content):
		if self.hasSelectedText():
			# jika sudah diselect (multiline) maka that's it, kita akan timpa
			# cek self.selectedText() jk kosong atau tidak
			pass
		else:
			# jk gak ada, kita select baris...
			self.select_current_line_where_cursor_is()
		self.replaceSelectedText(content)
		if programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['editor_fmus']['fold_after_insert']:
			self.foldAll()

	def remove_above_selection(self):
		if self.hasSelectedText():
			barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()
			if barismulai>0:
				sebelum=barismulai-1
				panjang_baris = self.lineLength(sebelum)
				self.setSelection(0, 0, sebelum, panjang_baris)
				self.removeSelectedText()
		else:
			baris, current_column = self.getCursorPosition()
			if baris>0:
				sebelum=baris-1
				panjang_baris = self.lineLength(sebelum)
				self.setSelection(0, 0, sebelum, panjang_baris)
				self.removeSelectedText()

	def remove_below_selection(self):
		total_lines = self.lines()
		if self.hasSelectedText():
			barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()
			if barismulai<total_lines-1:
				setelah=barismulai+1
				panjang_baris = self.lineLength(total_lines-1)
				self.setSelection(setelah, 0, total_lines-1, panjang_baris)
				self.removeSelectedText()
		else:
			baris, current_column = self.getCursorPosition()
			if baris<total_lines-1:
				setelah=baris+1
				panjang_baris = self.lineLength(total_lines-1)
				self.setSelection(setelah, 0, total_lines-1, panjang_baris)
				self.removeSelectedText()

	def remove_context_selection(self):
		total_lines = self.lines()
		if self.hasSelectedText():
			barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()
			delta = barisakhir-barismulai
			# hapus before
			if barismulai>0:
				sebelum=barismulai-1
				panjang_baris = self.lineLength(sebelum)
				self.setSelection(0, 0, sebelum, panjang_baris)
				self.removeSelectedText()
			else:
				pass # before gak perlu hapus jk sudah di awal baris

			# skrg current line pindah ke baris 0, akhir seleksi ada di baris "delta"
			barisakhir = delta

			# hapus after
			if barisakhir<total_lines-1:
				setelah=barisakhir+1
				panjang_baris = self.lineLength(total_lines-1)
				self.setSelection(setelah, 0, total_lines-1, panjang_baris)
				self.removeSelectedText()
			else:
				pass # after gak perlu hapus jika sudah di akhir baris
			
		else:
			baris, current_column = self.getCursorPosition()
			barismulai=baris
			
			# hapus before
			if barismulai>0:
				sebelum=barismulai-1
				panjang_baris = self.lineLength(sebelum)
				self.setSelection(0, 0, sebelum, panjang_baris)
				self.removeSelectedText()

			# skrg current line sudah pindah ke baris 0
			barisakhir=0

			# hapus after
			if barisakhir<total_lines-1:
				setelah=barisakhir+1
				panjang_baris = self.lineLength(total_lines-1)
				self.setSelection(setelah, 0, total_lines-1, panjang_baris)
				self.removeSelectedText()

	def combine_process_fmus_process_word(self):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		
		if not bariskalimat.strip():
			print('ctrl+k, combine_process_fmus_process_word, empty:', bariskalimat)
			alert('EMPTY COMMAND FOR CTRL+K')
			return

		# UGLY: khusus utk /img)...gak bisa terima \n dan \t
		# mungkin juga /dot)?
		if bariskalimat.startswith('/img)'):
			# sengaja kita bedakan dg sanitize_chars
			bariskalimat = bariskalimat.replace('\n', '__ASK_NEWLINE__').replace('\t', '__ASK_TAB__')
			# bariskalimat = bariskalimat.replace('\n', '__NL').replace('\t', '__TAB')

		# add: handle /gif), /meme) dll, newline direplace dg empty
		hilangkan_newline = ['/gif)', '/meme)', '/video)']
		if any([item for item in hilangkan_newline if bariskalimat.startswith(item)]):
			bariskalimat = bariskalimat.replace('\n', '')
		self.fmus_repl_request.emit(bariskalimat)

	def process_dictionary(self):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		from schnell.app.translatorutils import kamus
		bariskalimat = bariskalimat.strip()
		result = kamus(bariskalimat)
		# self.publishrequest.emit(result)
		self.insert_and_move_at_cursor('\n' + result, next_line=1, column_at_start_line=True)

	def process_translate(self):
		"""
		en,fr/sentence
		sentence = en,id
		"""
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		from schnell.app.translatorutils import translate, coded_translate
		bariskalimat = bariskalimat.strip()
		src = 'en'
		dest = 'id'
		m = re.match(r'^(\w{2},\w{2})/(.*)', bariskalimat)
		if m:
			src, dest = m.group(1).split(',')
			bariskalimat = f'{src},{dest}/' + m.group(2)
		else:
			bariskalimat = f'{src},{dest}/' + bariskalimat
		result = coded_translate(bariskalimat)
		# self.publishrequest.emit(result)
		self.insert_and_move_at_cursor('\n' + result, next_line=1, column_at_start_line=True)

	def process_english(self):
		current_line, current_column = self.getCursorPosition()
		panjang_baris = self.lineLength(current_line)
		baris, kolom, barisakhir, kolomakhir = self.get_first_selection_only()
		# bariskata = self.wordAtLineIndex(baris, kolom)  # kata under cursor gak berguna krn skip puncs
		start = self.positionFromLineIndex(baris, 0)  # dari awal baris
		end = self.positionFromLineIndex(baris, panjang_baris)
		bariskalimat = self.text(start, end).strip()
		self.englishrequest.emit(bariskalimat)

	def get_line_text(self):
		"""
		ambil baris pada letak kursor
		"""
		current_line, current_column = self.getCursorPosition()
		panjang_baris = self.lineLength(current_line)
		baris, kolom, barisakhir, kolomakhir = self.get_first_selection_only()
		# bariskata = self.wordAtLineIndex(baris, kolom)  # kata under cursor gak berguna krn skip puncs
		start = self.positionFromLineIndex(baris, 0)  # dari awal baris
		end = self.positionFromLineIndex(baris, panjang_baris)
		bariskalimat = self.text(start, end)  # default non strip
		return bariskalimat

	def get_selected_text(self):
		"""
		ambil teks pada selection
		seperti self.get_first_selection_only() tapi ditambah teks yang dipilih
		"""
		barismulai, kolommulai, barisakhir, kolomakhir = self.get_first_selection_only()
		start = self.positionFromLineIndex(barismulai, kolommulai)
		end = self.positionFromLineIndex(barisakhir, kolomakhir)
		bariskalimat = self.text(start, end)
		return bariskalimat, barismulai, kolommulai, barisakhir, kolomakhir

	def get_line_or_selected_text(self, select_if_line=False):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
			if select_if_line:
				self.select_current_line_where_cursor_is()
		return bariskalimat

	def get_line_text_with_line_column(self):
		current_line, current_column = self.getCursorPosition()
		panjang_baris = self.lineLength(current_line)
		baris, kolom, barisakhir, kolomakhir = self.get_first_selection_only()
		# bariskata = self.wordAtLineIndex(baris, kolom)  # kata under cursor gak berguna krn skip puncs
		start = self.positionFromLineIndex(baris, 0)  # dari awal baris
		end = self.positionFromLineIndex(baris, panjang_baris)
		bariskalimat = self.text(start, end)  # default non strip
		return bariskalimat, current_line, panjang_baris

	def get_line_or_selected_text_with_line_column(self):
		"""
		jika multiline, kembalikan last line+last col (r2, c2)
		jika singleline, kembalikan current line+jumlah kolom pada current baris
		"""
		if self.hasSelectedText():
			bariskalimat, _, _, r2, c2 = self.get_selected_text()
		else:
			bariskalimat, r2, c2 = self.get_line_text_with_line_column()
		return bariskalimat, r2, c2

	def process_csvlang(self):
		"""
		{@Todo}title,s
		/c. all/{@Todo}title,s
		"""
		# prefix_csvlang = "/c. all/"
		prefix_csvlang = "/c. "
		bariskalimat = self.get_line_or_selected_text()
		bariskalimat = bariskalimat.strip()
		if bariskalimat:
			self.fmus_repl_request.emit(prefix_csvlang + bariskalimat)

	def process_lalang(self):
		"""
		/l. go/Pmynewpackage
		/l. [i/0/@@@|pkg.go] go/Pmynewpackage
		"""
		prefix_lalang = "/l. "
		bariskalimat = self.get_line_or_selected_text()
		bariskalimat = bariskalimat.strip()
		if bariskalimat:
			self.fmus_repl_request.emit(prefix_lalang + bariskalimat)

	def process_backslash(self, wsl_tree=False):
		"""
		toggle forward dan back slash.

		jk selection atau baris berisi / maka toggle ke \\ dan sebaliknya.
		di sini panggil get_line_or_selected_text dengan select_if_line=True
		karena kita mau "replace selection"
		walaupun sebetulnya gak perlu dong?
		kan replace_selection_in_editor sudah pasti akan select baris jk gak ada selection.
		"""
		bariskalimat = self.get_line_or_selected_text(select_if_line=True)
		bariskalimat = bariskalimat.strip()
		if bariskalimat:
			if wsl_tree: # c+s+\
				# hasil_proses_wsl_tree = re.sub(r'^([A-Z]):\\|([A-Z]):/', r'/mnt/\1/', bariskalimat, flags=re.IGNORECASE).lower()
				hasil_proses_wsl_tree = re.sub(r'^([A-Z]):\\|([A-Z]):/', r'/mnt/\1/', bariskalimat, flags=re.IGNORECASE)
				hasil_proses_wsl_tree = hasil_proses_wsl_tree.replace('\\', '/').lower()
				# hasil_proses_wsl_tree = bariskalimat.replace('\\', '/').replace('')
				hasil_proses_wsl_tree = '/exec)wsl tree  -I "node_modules__PP__pycache__" ' + hasil_proses_wsl_tree
				self.replace_selection_in_editor(hasil_proses_wsl_tree)
			else: # c+a+\
				if '/' in bariskalimat:
					self.replace_selection_in_editor(bariskalimat.replace('/', '\\'))
				elif '\\' in bariskalimat:
					self.replace_selection_in_editor(bariskalimat.replace('\\', '/'))

	def process_quote(self):
		"""
		toggle single dan double quote.
		spt process_backslash tapi utk ' dan ".
		"""
		bariskalimat = self.get_line_or_selected_text(select_if_line=True)
		bariskalimat = bariskalimat.strip()
		if bariskalimat:
			if '"' in bariskalimat:
				# ‘
				# ’
				self.replace_selection_in_editor(bariskalimat.replace('"', "'").replace('‘', "'").replace('’', "'"))
			elif "'" in bariskalimat:
				self.replace_selection_in_editor(bariskalimat.replace("'", '"'))

	def desanitize_current_selection(self):
		bariskalimat = self.get_line_or_selected_text()
		# sementara hanya newline...
		newcontent = bariskalimat.replace('\n', '__NL')
		self.replace_selection_in_editor(newcontent)

	def process_mapper_list(self):
		instruksi = editor_fmus_help
		instruksi += '\n'
		instruksi += __file__
		instruksi += '\n'
		instruksi += 'ULIBPY_ROOTDIR/schnell/gui/system/searcher/widgets/editor_fmus_mapper.py'
		instruksi += '\n'
		instruksi += 'ULIBPY_ROOTDIR/schnell/gui/system/searcher/widgets/editor_fmus_helper.py'
		instruksi += '\n'
		instruksi += 'ULIBPY_ROOTDIR/schnell/gui/system/searcher/widgets/editor_fmus_folders.py'
		instruksi += '\n'
		self.insert_and_move_at_cursor(instruksi)

	def process_mapper(self):
		bariskalimat = self.get_line_or_selected_text().strip()
		if not bariskalimat:
			# self.publishrequest.emit(editor_fmus_help)
			self.process_mapper_list()
			# self.select_current_line_where_cursor_is()
			# self.replace_selection_in_editor(bariskalimat)
		elif bariskalimat in editor_fmus_mapper:
			replacer = editor_fmus_mapper[bariskalimat]['content']
			if '__DIR__' in replacer and hasattr(self.mkhelp, 'last_file') and self.mkhelp.last_file:
				replacer = replacer.replace('__DIR__', dirname(self.mkhelp.last_file))
			#self.insert_at_newline(replacer, baris, kolom)
			self.replace_selection_in_editor(replacer)
		elif bariskalimat in ['file', 'dir', 'keys']:
			if hasattr(self.mkhelp, 'last_file') and self.mkhelp.last_file:
				if bariskalimat == 'file':
					bariskalimat = bariskalimat.replace('file', self.mkhelp.last_file)
				elif bariskalimat == 'dir':
					bariskalimat = bariskalimat.replace('dir', dirname(self.mkhelp.last_file))
				self.replace_selection_in_editor(bariskalimat)
			elif bariskalimat == 'keys':
				# tampilkan editor_fmus.txt
				bariskalimat = file_content(editor_fmus_text_file)
				self.replace_selection_in_editor(bariskalimat)
		elif bariskalimat.startswith('reload=') or bariskalimat.startswith('R='): # reload=/dj
			from .editor_fmus_mapper import reload_folder
			kunci = bariskalimat.removeprefix('reload=' if bariskalimat.startswith('reload=') else 'R=').strip()
			kembali = reload_folder(kunci)
			if kembali:
				self.insert_and_move_at_cursor(kembali, next_line=1, column_at_start_line=True)
			self.process_mapper_list()

	def process_replservice(self):
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			# spt C:\Users\usef\work\sidoarjo\schnell\creator\repl_language\replify.py
			answer, _ = repl_service.process(bariskalimat)
			self.replace_selection_in_editor(answer)

	def insert_file_content_at_cursor(self, publish_to_yellow=False):
		"""
		dipanggil dg ctrl+shift+&
		insert file content pada next line
		"""
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			filepath = bongkar(bariskalimat)
			print('insert_file_content_at_cursor => filepath:', filepath)
			if isfile(filepath) and not is_file_binary(filepath):
				content = file_content(filepath)
				if not publish_to_yellow:
					self.insert_and_move_at_cursor(content, next_line=1, column_at_start_line=True)
				else:
					self.publishrequest.emit(content)

	def process_actor(self, publish_to_yellow=False):
		"""
		b -> ctrl+shift+> keluarkan blok b
		650 -> ctrl+shift+> keluarkan blok 650
		tambah:
		~ariya -> tampilkan any actor containing ariya.
		"""
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			from schnell.gui.system.searcher.widgets.actorhandler import actor_handler
			content = actor_handler(bariskalimat, debug=False)
			if not publish_to_yellow:
				self.insert_and_move_at_cursor(content, next_line=1, column_at_start_line=True)
			else:
				self.publishrequest.emit(content)

	def create_new_file_at_curdir(self):
		if hasattr(self.mkhelp, 'last_file') and self.mkhelp.last_file:
			from schnell.app.autoutils import prompt
			# from schnell.app.fileutils import touch_file
			from schnell.app.systemutils import run_code_file
			foldername = dirname(self.mkhelp.last_file)
			namafile = prompt('Masukkan nama file utk dibuat di {foldername}')
			if namafile:
				filepath = joiner(foldername, namafile)
				# touch_file(filepath)
				run_code_file(filepath)
				self.mkhelp.recreate_buttons()
			else:
				indah4('No input file', warna='red')
		else:
			indah4('No last file at mkhelp', warna='red')

	def convert_space_tab(self, which=1):
		"""
		which
		! dan @
			1   tab to 2s
			2   tab to 4s
		# dan $
			3   2s to tab
			4   4s to tab
		% dan ^
			5   2 to 4
			6   4 to 2
		"""
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			source='t'
			target=2
			if which==2:
				source='t'
				target=4
			elif which==3:
				source=2
				target='t'
			elif which==4:
				source=4
				target='t'
			elif which==5:
				source=2
				target=4
			elif which==6:
				source=4
				target=2
			answer = indent_convert(bariskalimat, source, target)
			self.replace_selection_in_editor(answer)

	def char_to_char(self, src='=', dst=':'):
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			answer = bariskalimat.replace(src, dst)
			self.replace_selection_in_editor(answer)

	def insert_encode_filepath(self):
		from schnell.app.mediautils import entrify_encode_file_content
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			result = entrify_encode_file_content(bariskalimat)
			self.insert_and_move_at_cursor(result, next_line=1, column_at_start_line=True)
			trycopy(result)

	def single_double_quote(self, single_to_double=True):
		"""
		'\' to "', #9
		'" to \'', #10		
		'= to :', #11
		"""
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			if single_to_double:
				answer = bariskalimat.replace('\'', '"')
			else:
				answer = bariskalimat.replace('"', '\'')
			self.replace_selection_in_editor(answer)

	def single_double_backslash(self, single_to_double=True):
		from schnell.app.stringutils import replace_single_backslash_with_double, replace_double_backslash_with_single
		bariskalimat = self.get_line_or_selected_text().strip()
		if bariskalimat:
			if single_to_double:
				answer = replace_single_backslash_with_double(bariskalimat)
			else:
				answer = replace_double_backslash_with_single(bariskalimat)
			self.replace_selection_in_editor(answer)

	def googler(self):
		# if self.hasSelectedText():
		#     bariskalimat, _,_,_,_ = self.get_selected_text()
		# else:
		#     bariskalimat = self.get_line_text()        
		bariskalimat = self.get_line_or_selected_text().strip()
		# alert(bariskalimat)
		cari_google(bariskalimat)

	def copy_to_clipboard(self):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		# pyperclip.copy(bariskalimat)
		self.publishrequest.emit(bariskalimat)

	def list_github_repos(self):
		if self.hasSelectedText():
			bariskalimat, _,_,_,_ = self.get_selected_text()
		else:
			bariskalimat = self.get_line_text()
		url = bariskalimat.strip()
		page = 1
		# bezkoder#100
		m = re.match(r'([A-Za-z0-9_\-]+)#(\d+)', url)
		if m:
			url = m.group(1)
			page = int(m.group(2))
		API_START = 'https://api.github.com/users/'
		if not url.startswith(API_START) and url.startswith('https://github.com'):
			from schnell.app.urlutils import first_path
			username = first_path(url)
			url = API_START + username + '/repos?sort=updated'
		elif re.match(r'[A-Za-z0-9_\-]+', bariskalimat):
			url = API_START + url + '/repos?sort=updated'
		url += f'&per_page=1000&page={page}'
		r = requests.get(url)
		print('list_github_repos for:', url, 'hasilkan:', r)
		if 200 <= r.status_code < 300:
			repos = '\n'.join([item['html_url'] for item in r.json()])
			self.publishrequest.emit(repos)
		else:
			from schnell.app.promptutils import message_box_application
			message_box_application(f'{url} not found.')

	# def toggle_fold(self, dont_toggle=False):
	#     if not dont_toggle: # initial sesuai config...jangan ubah nilai config
	#         global_context['fmus_editor_folding'] = not global_context['fmus_editor_folding']
	#     if global_context['fmus_editor_folding']:
	#         self.foldAll()
	#     else:
	#         self.clearFolds()

	def signalHandlers(self):
		self.linesChanged.connect(self.onLinesChanged)
		self.insert_at_top.connect(self.insert_at_top_handler)

	def onLinesChanged(self):
		self.setMarginWidth(0, self.fontMetrics().width(str(self.lines())) + self.margin)

	def setContent(self, content):
		self.setText(content)
		if programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['editor_fmus']['fold_after_insert']:
			self.foldAll()

	def init(self):
		self.setUtf8(True)

		# lexer = QsciLexerPython(self)
		lexer = SepiaPythonLexer(self, warna=self.warna)
		if self.lexer=='md':
			lexer = QsciLexerMarkdown(self)
		self.setLexer(lexer)
		self.setEolMode(QsciScintilla.EolUnix)
		self.setAutoCompletionCaseSensitivity(False)  # ignore case
		self.setAutoCompletionSource(self.AcsAll)
		self.setAutoCompletionThreshold(1)  # One character pops up completion
		self.setAutoIndent(True)  # auto indent
		self.setBackspaceUnindents(True)
		self.setBraceMatching(self.StrictBraceMatch)
		self.setIndentationGuides(True)
		self.setIndentationsUseTabs(False)
		self.setIndentationWidth(4)
		self.setTabIndents(True)
		self.setTabWidth(4)
		self.setWhitespaceSize(1)
		self.setWhitespaceVisibility(self.WsVisible)
		self.setWhitespaceForegroundColor(Qt.gray)
		self.setWrapIndentMode(self.WrapIndentFixed)
		self.setWrapMode(self.WrapWord)

		# fold
		# https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
		self.setFolding(self.BoxedTreeFoldStyle, 2)
		self.setFoldMarginColors(QColor("#676A6C"), QColor("#676A6D"))
		font = self.font() or QFont()
		font.setFamily("Hack")
		font.setFixedPitch(True)
		font.setPointSize(12)
		self.setFont(font)
		self.setMarginsFont(font)
		self.fontmetrics = QFontMetrics(font)
		lexer.setFont(font)
		self.textHeight(24)
		self.setCaretLineVisible(True)
		self.setCaretLineBackgroundColor(QColor("gold"))

		self.setMarginWidth(0, self.fontmetrics.width(str(self.lines())) + self.margin)
		self.setMarginLineNumbers(0, True)
		self.setMarginsBackgroundColor(QColor("gainsboro"))
		self.setMarginWidth(1, 0)
		self.setMarginWidth(2, 14) # folded area

		# Bind autocompletion hotkey Alt+/
		completeKey = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Slash), self)
		completeKey.setContext(Qt.WidgetShortcut)
		completeKey.activated.connect(self.autoCompleteFromAll)

		# QShortcut(QKeySequence("Ctrl+Q"), self, activated=lambda: qApp.quit())
		# https://docs.huihoo.com/pyqt/QScintilla2/classQsciScintilla.html
		# self.foldAll()
		# QShortcut(QKeySequence("Ctrl+L"), self, activated=lambda: self.foldAll)
		QShortcut(QKeySequence("Ctrl+S"), self, activated=lambda: self.save_file.emit(True))

	def __init__(self, parent=None, warna=None, lexer='py', *args, **kwargs):
		super(EditorFmus, self).__init__(parent, *args, **kwargs)
		self.mkhelp = parent
		self.margin = 24
		self.lexer = lexer
		self.warna = warna
		self.init()
		self.signalHandlers()
		self.sisipkan = lambda content: self.insert_and_move_at_cursor(content, next_line=1, column_at_start_line=True)
		# self.toggle_fold()
		self.foldAll()
