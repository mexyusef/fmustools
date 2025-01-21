import json, os, time, pyautogui
from schnell.app.appconfig import command_prompt_data, command_prompt_data_extension, programming_data
from schnell.app.autoutils import (
	type_by_window_title, prompt, alert, confirm, password,
	q1, q2, q3, q4,
	bottom_pane, top_pane)
# from schnell.app.dirutils import bongkar
from schnell.app.printutils import indah4
from schnell.app.utils import env_get, env_replace_filepath, env_int
from schnell.app.windowsutils import (
	cmd_register_list as l,
	get_cmd_register_list as getlist,
	is_visible as is_window_visible,
	create_register_commandprompt as c,
	ketik as k,
	ketik as ketik_by_hwnd,
	ketik_by_index as ki,
	ketik_by_index,
	fill_in_hwnds as fill,
	hapus_by_id as hadi,
	get_command_prompt_data_index_from_uuidtitle,
	get_hwnd_from_uuidtitle,
	minimize_window, maximize_window,
	show_window, hide_window,
	restore_window, normal_window,
	close_window,
	bring_to_top, set_top, set_topmost, set_not_topmost,
	hapus_empty, hapus_by_id,
	hapus_iterate_by_title,
	minimize_terminal,
)
# from schnell.creator.context import context as creator_context


def get_last_console_data():
	values = list(command_prompt_data.values())
	if values:
		print(values)
		return values[-1]
	return None


def data_for_item(item):
	index = get_command_prompt_data_index_from_uuidtitle(item)
	data = command_prompt_data[index]
	data.update({
		'index': index,
	})
	return data


def get_items_for_combo():
	items = [v['id'] for v in command_prompt_data.values()]
	return items


def fill_set():
	"""
	iterate command_prompt_data, mengisi hwnd dan chwnd jk belum ada utk masing2 window
	"""
	# jk belum ada hwnd pada tiap command_prompt_data, maka coba isi berdasarkan title/uuid nya
	fill()
	# bentuk list of ids/uuids/titles dari masing2 window di command_prompt_data
	res = get_items_for_combo()
	# print('fill_set:', res)
	return res


def hapus_set_combo_items():
	hapus_iterate_by_title()
	return get_items_for_combo()


def create_fill_set(CURDIR=None):
	_id = c(CURDIR=CURDIR)
	items = fill_set()

	l() # print

	# cek id ada
	index_or_none = get_command_prompt_data_index_from_uuidtitle(_id)
	if not index_or_none:
		# TODO: loop + sleep utk fill automatic
		print(f'ERR...please fill "index" dari window title "{_id}" secara manual! karena masih kosong...')
	else:
		# cek hwnd sudah ada
		hwnd = get_hwnd_from_uuidtitle(_id)
		while not hwnd:
			fill_set()
			time.sleep(0.5)
			hwnd = get_hwnd_from_uuidtitle(_id)
	return items


def create_fill_set_with_id_index(CURDIR=None):
	# create
	hwnd = None
	if not CURDIR:
		CURDIR = os.getcwd()
	_id = c(CURDIR=CURDIR)
	# isi data
	items = fill_set()
	index_or_none = get_command_prompt_data_index_from_uuidtitle(_id)
	if not index_or_none:
		# TODO: loop + sleep utk fill automatic
		indah4(f'ERR...please fill "index" dari window title "{_id}" secara manual! karena masih kosong...', warna='red')
	else:
		# cek hwnd sudah ada
		hwnd = get_hwnd_from_uuidtitle(_id)
		while not hwnd:
			fill_set()
			time.sleep(0.5)
			hwnd = get_hwnd_from_uuidtitle(_id)

	# print(f"""create_fill_set_with_id_index
	# items = {items} 
	# title/_id = {_id}
	# index/none = {index_or_none}
	# hwnd = {hwnd}
	# command_prompt_data[index] = {command_prompt_data[index_or_none]}
	# """)

	return items, _id, index_or_none


def to_top(window_title, mode='topmost'):
	id_now = window_title
	hwnd = get_hwnd_from_uuidtitle(id_now)
	if mode == 'topmost':
		set_topmost(hwnd)
	elif mode == 'nottopmost':
		set_not_topmost(hwnd)
	elif mode == 'top':
		set_top(hwnd)
	elif mode == 'bringtop':
		bring_to_top(hwnd)


def to_top_by_hwnd(hwnd, mode='topmost'):
	# id_now = window_title
	# hwnd = get_hwnd_from_uuidtitle(id_now)
	if mode == 'topmost':
		set_topmost(hwnd)
	elif mode == 'nottopmost':
		set_not_topmost(hwnd)
	elif mode == 'top':
		set_top(hwnd)
	elif mode == 'bringtop':
		bring_to_top(hwnd)


def operate_on_windows(window_title, mode='hide'):
	id_now = window_title
	hwnd = get_hwnd_from_uuidtitle(id_now)
	if mode == 'hide':
		hide_window(hwnd)
	elif mode == 'show':
		show_window(hwnd)
	elif mode == 'normal':
		normal_window(hwnd)
	elif mode == 'restore':
		restore_window(hwnd)
	elif mode == 'min':
		minimize_window(hwnd)
	elif mode == 'max':
		maximize_window(hwnd)
	elif mode == 'close':
		close_window(hwnd)


def operate_on_windows_by_hwnd(hwnd, mode='hide'):
	# id_now = window_title
	# hwnd = get_hwnd_from_uuidtitle(id_now)
	if mode == 'hide':
		hide_window(hwnd)
	elif mode == 'show':
		show_window(hwnd)
	elif mode == 'normal':
		normal_window(hwnd)
	elif mode == 'restore':
		restore_window(hwnd)
	elif mode == 'min':
		minimize_window(hwnd)
	elif mode == 'max':
		maximize_window(hwnd)
	elif mode == 'close':
		close_window(hwnd)


def button_ketik_handler(window_title, text):
	# if not text:
	#     text = line_ketik.text()
	id_now = window_title
	index = get_command_prompt_data_index_from_uuidtitle(id_now)
	print(f"send [{text}] to {id_now}, index={index}.")
	ki(index, text)


def create_cmd_and_type_away(CURDIR=None, ketikan=['wsl'], delay_antar_ketikan=0.0, console_name=None, console_target=None):
	"""
	mengetik menggunakan "ketik_by_index" dimana index adlh index pada command_prompt_data
	27/11/22 bisa handle pyautogui
	/ketik)auto:ctrl,d
	/ketik)dir|auto:ctrl,shift,t|pwd
	/ketik)min
	/ketik)pause
	"""
	posisi_console =programming_data['j']['schnell']['app']['wcmderutils']['reposition_console']
	if CURDIR and os.path.isfile(CURDIR):
		CURDIR = os.path.dirname(CURDIR)

	if not delay_antar_ketikan:
		delay_antar_ketikan = programming_data['j']['schnell']['app']['wcmderutils']['delay_antar_ketikan']
	if programming_data['debug']:
		print(f'create_cmd_and_type_away, CURDIR = {CURDIR}, ketikan = {ketikan}.')

	# bgm hubungan antara title dan index?
	# command_prompt_data[index] = {'id': title, ...}
	# proses mengetik tulisan adlh: ketik(command_prompt_data[index]['chwnd'], pesan, cpm=cpm)
	# ketik_by_index(index, pesan, cpm=4000)
	# ketik_by_window_title(title, pesan, cpm=4000)
	title = ''
	if console_target:
		if console_target in command_prompt_data_extension:
			# block ini seharusnya bisa utk mengetik ke gui editor, tanpa harus bikin console
			title = command_prompt_data_extension[console_target]['title']
			index = command_prompt_data_extension[console_target]['index']
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				print('console_target:', console_target)
		else:
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				print('no console_target:', console_target, 'in:', json.dumps(command_prompt_data_extension, indent=2))
			items, title, index = create_fill_set_with_id_index(CURDIR=CURDIR)
			if env_int('ULIBPY_FMUS_DEBUG')>1:
				print(f'title={title}, index={index}')
	elif console_name:
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('console_name:', console_name)
		_, title, index = create_fill_set_with_id_index(CURDIR=CURDIR)
		command_prompt_data_extension[console_name] = {
			'title': title,
			'index': index,
		}
	else:
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print('no console name or target')
		items, title, index = create_fill_set_with_id_index(CURDIR=CURDIR)
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print(f'title={title}, index={index}')

	# indah4(f"""[create_cmd_and_type_away]
	# CURDIR={CURDIR}
	# ketikan={ketikan}
	# delay_antar_ketikan={delay_antar_ketikan}
	# console_name={console_name}
	# console_target={console_target}
	# title={title}
	# index={index}
	# items={items}
	# """, warna='yellow')

	# /au) utk console yg dibuat
	if title and posisi_console and not console_target:
		if posisi_console=='bottom':
			wnds = pyautogui.getWindowsWithTitle(title)
			if wnds:
				hwnd = wnds[0]
				if hwnd:
					# 23/12/23, dukung 4 cmds
					if len(command_prompt_data)%4==0:
						# bottom_pane(hwnd, factor=7)
						q1(hwnd)
					elif len(command_prompt_data)%4==1:
						# top_pane(hwnd, factor=7)
						q2(hwnd)
					elif len(command_prompt_data)%4==2:
						q3(hwnd)
					else:
						q4(hwnd)

	# self.populate_flowwidget(items)
	for tulisan in ketikan:
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			indah4(f'tulisan [{tulisan}]', warna='yellow')

		press_enter = True

		tulisan = env_replace_filepath(tulisan) # agar bisa ULIBPY_
		# tulisan = tulisan.replace('ULIBPY_ROOTDIR', r'C:\Users\usef\work\sidoarjo')

		if tulisan.startswith('auto:'):
			# /ketik)dir|auto:ctrl,shift,t|pwd
			# kita tambah agar bisa handle wexpect
			# ...|auto:hope=SSD#[sudo] password for usef:#usef|...
			tulisan = tulisan.removeprefix('auto:')
			keys = [item.strip() for item in tulisan.split(',')]

			if tulisan.startswith('alert'):
				_, body = tulisan.split('=', 1)
				body = body.replace('\\n', '\n').replace('\\t', '\t')
				if '=' in body:
					_body, title = body.split('=', 1)
					alert(_body, title)
				else:
					alert(body)
			elif tulisan.startswith('confirm'):
				_, body = tulisan.split('=')
				body = body.replace('\\n', '\n').replace('\\t', '\t')
				confirm(body)
			elif tulisan.startswith('prompt'):
				_, body = tulisan.split('=')
				body = body.replace('\\n', '\n').replace('\\t', '\t')
				res = prompt(body)
				indah4(f'prompt resulting [{res}]', warna='green')
			elif tulisan.startswith('password'):
				_, body = tulisan.split('=')
				body = body.replace('\\n', '\n').replace('\\t', '\t')
				res = password(body)
				indah4(f'password resulting [{res}]', warna='green')
			elif tulisan.startswith('hope='):
				# err ternyata gagal, krn kita gunakan wexpect tapi command berikut (SSD, sudo service docker start) jalan di linux
				hope_statement = tulisan.removeprefix('hope=')
				from schnell.app.quick.crunner import harapw
				harapw(hope_statement.replace('#', '|'))
			else:
				# misal tekan ctrl+shift+d
				type_by_window_title(title, keys)

				if set(keys)==set(['ctrl','shift','t']):
					# ini hanya jk auto:ctrl,shift,t
					# perlu ganti title cmd prompt agar ctrl+shift+d berikutnya bisa jalan
					time.sleep(0.75)  # perlu waktu dari tab terbuat, dan ngetik ganti title
					indah4(f'sending title "{title}"...', warna='white')
					ketik_by_index(index, f'title {title}')

			if delay_antar_ketikan:
				time.sleep(delay_antar_ketikan)

		elif tulisan.startswith('wait:'):
			# wait:judul=tulisan
			# wait:tulisan
			# /ketik)wait:ini berjudul=tunggu sampai jalan|dir|wait:tunggu lagi yg kedua|pwd
			tulisan = tulisan.removeprefix('wait:')

			title = '(UNTITLED)'
			if '=' in tulisan:
				title, body = tulisan.split('=',1)
			else:
				body = tulisan
			body = body.replace('\\n', '\n').replace('\\t', '\t')
			alert(body, title)
			if delay_antar_ketikan:
				time.sleep(delay_antar_ketikan)

		elif tulisan == 'pause':
			# ini akibatkan, muncul Press any key di window creator, bukan window created yg kita inginkan.
			# os.system('''python -c"input('Press any key... ')"''')

			# hanya utk windows...
			# ternyata ini, malah dibantai oleh Enter berikutnya, tiap tulisan dipisah Enter soalnya
			# ketik_by_index(index, 'pause')
			# if delay_antar_ketikan:
			#     time.sleep(delay_antar_ketikan)
			input('Press any key... ')

		elif tulisan == 'min':
			minimize_terminal()

		else:
			# upd 6/5/23, bisa gak tekan enter: __NO_ENTER__|dua|tiga
			if tulisan.endswith('__NO_ENTER__'):
				tulisan = tulisan.removesuffix('__NO_ENTER__')
				press_enter=False

# 			print(f"""ketik_by_index
# 		index={index}
# 		tulisan={tulisan}
# 		press_enter={press_enter}
# """)
			# ketik_by_index(index, tulisan, cpm=creator_context['characters_per_minute'], press_enter=press_enter)
			ketik_by_index(index, tulisan, cpm=programming_data['j']['schnell']['app']['wcmderutils']['ULIBPY_TYPING_CPM'], press_enter=press_enter)
			if delay_antar_ketikan:
				time.sleep(delay_antar_ketikan)
