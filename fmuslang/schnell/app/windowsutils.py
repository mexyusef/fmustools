import os
import subprocess
import sys
import threading
import time

import ctypes
import pywintypes

import win32api
# import win32clipboard
import win32com.client
import win32con
# import win32console
# import win32event
import win32gui
import win32gui_struct
import win32process
import win32ui
from win32com.shell import shell, shellcon

# from win32com.shell.shell import ShellExecuteEx
# from win32com.shell import shellcon
# from win32com.shell import shell
# import win32security
from uuid import uuid1

from .appconfig import command_prompt_data, command_prompt_data_extension
from .printutils import pp
# from app.appconfig import command_prompt_data


def env_int(kunci, default=0):
	if kunci in os.environ:
		return int(os.environ[kunci])
	return default


# tambahan
# https://stackoverflow.com/questions/2940858/kill-process-by-name
# https://stackoverflow.com/questions/48198/how-can-you-find-out-which-process-is-listening-on-a-port-on-windows?rq=1
# tasklist
# netstat -ano -nao -ona ona sutra -> netstat -ona | find /i "listening"
_all_proc_infos = []
_all_hwnd_0 = ['explorer']

kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32
# user32 = ctypes.WinDLL('user32', use_last_error=True)
# _winlib = win32api.LoadLibrary("user32")
shell = win32com.client.Dispatch('WScript.Shell')

CF_TEXT = 1
FAST_SLEEP = 0.1
WMI = win32com.client.GetObject('winmgmts:')
TH32CS_SNAPTHREAD = 0x00000004
mb_icons = [win32con.MB_ICONQUESTION, win32con.MB_ICONASTERISK, win32con.MB_ICONSTOP]
WINDOW_CREATION_TIME = 300
SLEEP_CREATION_TIME = float(WINDOW_CREATION_TIME/1000)

def is_clipboard_text():
	is_text = False
	user32.OpenClipboard(0)
	if user32.IsClipboardFormatAvailable(CF_TEXT):
		is_text = True
	user32.CloseClipboard()
	return is_text

class THREADENTRY32(ctypes.Structure): 
	_fields_ = [
		("dwSize", ctypes.c_ulong), 
		("cntUsage", ctypes.c_ulong), 
		("th32ThreadID", ctypes.c_ulong), 
		("th32OwnerProcessID", ctypes.c_ulong), 
		("tpBasePri", ctypes.c_long), 
		("tpDeltaPri", ctypes.c_long), 
		("dwFlags", ctypes.c_ulong)
	]

def EnumerateThreads(processId):
	threadEntry = THREADENTRY32()
	
	threadList = []
	threadSnap = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, processId)
	if threadSnap is not None:
		threadEntry.dwSize = ctypes.sizeof(threadEntry)
		success = kernel32.Thread32First(threadSnap, ctypes.byref(threadEntry))
		if not success:
			print ('Failed getting first process.')
		
		while success:
			if threadEntry.th32OwnerProcessID == processId:
				threadList.append(threadEntry.th32ThreadID)
			success = kernel32.Thread32Next(threadSnap, ctypes.byref(threadEntry))
		
		kernel32.CloseHandle(threadSnap)
	return threadList

def EnumerateProcesses(processName):
	processList = WMI.ExecQuery("SELECT * FROM Win32_Process where name = '%s'" % processName)
	return processList

def SearchWindowHandleIdIdByCaption(processName, caption):
	processList = EnumerateProcesses(processName)
	for process in processList:
		for thread in EnumerateThreads(process.Handle):
			windows = []
			win32gui.EnumThreadWindows(thread, lambda hwnd, resultList: resultList.append(hwnd), windows)
			for windowIdi in windows:
				text = win32gui.GetWindowText(windowIdi) 
				text = text.__str__()
				caption = caption.__str__()
				if caption in text:
					return [windowIdi, process.Handle]
	return [None, None]

def MakeProcess(NAME=None, CMD=None, PATTRS=None, TATTRS=None, INHER=0, CREAF=None, NEWENV=None, CURDIR=None, INFO=win32process.STARTUPINFO()):
	"""
	BOOL CreateProcess(
		LPCTSTR lpszImageName,
		LPCTSTR lpszCommandLine,
		LPSECURITY_ATTRIBUTES lpsaProcess,
		LPSECURITY_ATTRIBUTES lpsaThread,
		BOOL fInheritHandles,
		DWORD fdwCreate,
		LPVOID lpvEnvironment,
		LPTSTR lpszCurDir,
		LPSTARTUPINFO lpsiStartInfo,
		LPPROCESS_INFORMATION lppiProcInfo);

	When you call CreateProcess, the system creates a 4-GB virtual address space for the new process and 
	loads the specified process into this address space.
	The system then creates the primary thread for this process.
	This primary thread will begin by executing the C Runtime startup code, which will eventually call your WinMain function.

	cmd = "cmd"
	_, _, pid, tid = MakeProcess(CMD=cmd,CREAF=win32process.CREATE_NEW_CONSOLE)
	cmd_hwnd = GetNewlyCreatedWindow()
	for c in ('cd %s\r\n' % self.super_kamus['workdir']):
		win32api.PostMessage(cmd_hwnd, win32con.WM_CHAR, ord(c), 0)
	"""
	return win32process.CreateProcess(
		NAME,       # name
		CMD,        # command line
		PATTRS,     # process attributes
		TATTRS,     # thread attributes
		INHER,      # inheritance flag
		CREAF,      # creation flag
		NEWENV,     # new environment
		CURDIR,     # current directory
		INFO)

def MakeProcessStd(cmd, creaf=win32process.CREATE_NEW_CONSOLE):
	return MakeProcess(CMD=cmd, CREAF=creaf)

def long2word(lparam):
	x = win32api.LOWORD(lparam)
	y = win32api.HIWORD(lparam)
	return x,y

def move_window(hwnd, x, y, w, h):
	win32gui.MoveWindow(hwnd, x, y, w, h, True)

def slide_x(hwnd, increment=10):
	"""
	geser ke kanan/kiri sebanyak increment pixel
	"""
	x,y,w,h = window_rect(hwnd)
	# new pos, x+=10
	x += increment
	move_window(hwnd, x,y,w,h)

def resize_window(hwnd, value):
	"""
	h + value, jd y0 dikurangi value/2
	"""
	x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
	w = x1 - x0
	h = y1 - y0
	half = int(value/2)
	win32gui.MoveWindow(hwnd, x0-(half), y0-(half), w+value, h+value, True)

def resize_window_keep_topleft(hwnd, value):
	x,y,w,h = window_rect(hwnd)
	win32gui.MoveWindow(hwnd, x,y, w+value, h+value, True)

def resize_window_keep_bottomright(hwnd, value):
	x,y,w,h = window_rect(hwnd)
	win32gui.MoveWindow(hwnd, x-value,y-value, w+value, h+value, True)

def resize_window_keep_center(hwnd, value):
	x,y,w,h = window_rect(hwnd)
	half = int(value/2)
	win32gui.MoveWindow(hwnd, x-half,y-half, w+half, h+half, True)

def c2s(hwnd, x, y):
	'''
	'''
	return win32gui.ClientToScreen(hwnd, x, y)

def s2c(hwnd, x, y):
	'''
	return x,y di client coords
	'''
	return win32gui.ScreenToClient(hwnd, (x, y) )

def screen_size():
	'''
	w, h
	'''
	w = win32api.GetSystemMetrics(0)
	h = win32api.GetSystemMetrics(1)
	return w,h

def exec_program(filepath):
	win32api.ShellExecute(0, 'open', filepath, '', '', 1)

def send_alt_f():
	''' send to foreground hwnd '''
	win32api.Sleep(1000)
	win32api.keybd_event(18,0,0,0) # alt
	win32api.keybd_event(70,0,0,0) # f
	win32api.Sleep(1000)
	win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.Sleep(1000)

def send_o():
	''' send to fg hwnd '''
	win32api.keybd_event(79,0,0,0) # o
	win32api.Sleep(1000)
	win32api.keybd_event(79,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.Sleep(1000)

def window_rect(hwnd):
	"""
	https://stackoverflow.com/questions/7142342/get-window-position-size-with-python
	"""
	rect = win32gui.GetWindowRect(hwnd)
	x = rect[0]
	y = rect[1]
	w = rect[2] - x
	h = rect[3] - y
	return x, y, w, h

def window_rect2(hwnd):
	'''
	bbox = win32gui.GetWindowRect(hwnd)
	left, top, right, bottom = win32gui.GetWindowRect(hwnd)
	dapatkan tengah dg:
	(right - left) / 2
	(bottom - top) / 2
	'''
	return win32gui.GetWindowRect(hwnd)

def click_inside_hwnd(hwnd, x, y):
	'''
	https://www.programcreek.com/python/example/53239/win32gui.GetCursorPos
	'''
	left, top, right, bottom = window_rect(hwnd)
	width, height = right - left, bottom - top
	if x < 0 or x > width or y < 0 or y > height:
		return
	win32gui.SetForegroundWindow(hwnd)
	# pos = win32gui.GetCursorPos()
	win32api.SetCursorPos((left+x, top+y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	win_sleep(100)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	win_sleep(100)
	# win32api.SetCursorPos(pos) 

def win_sleep(sleep_time):
	'''
	satuan: millisecond
	'''
	win32api.Sleep(sleep_time)

def cur_thr():
	return win32api.GetCurrentThread()

def cur_proc():
	return win32api.GetCurrentProcess()

def cur_pid():
	return win32api.GetCurrentProcessId()

def cur_pid_os():
	import os
	return os.getpid()

def get_all_pids():
	return win32process.EnumProcesses()

def get_all_mids(proc_handle):
	return win32process.EnumProcessModules(proc_handle)

def terminate(pid):
	"""
	handle = win32api.OpenProcess(1, False, pid)
	win32api.TerminateProcess(handle, -1)
	"""
	handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, False, pid)
	win32api.TerminateProcess(handle, 0)
	win32api.CloseHandle(handle)

def kill(pid):
	try:
		import os, signal
		os.kill(pid, signal.SIGTERM)
	except (AttributeError, ImportError):
		print ('os.kill not found..')

def cursor():
	'''
	(x,y)
	'''
	return win32api.GetCursorPos()

def set_cursor(pos):
	win32api.SetCursorPos(pos) 

def cursorinfo():
	'''
	flag, handle, (x,y)
	flag = 1
	handle = 6553*
	'''
	return win32gui.GetCursorInfo()

def control_event(up=0, ext=0, shift=False):
	'''
	antara ctrl atau shift
	'''
	if up: 
		up = win32con.KEYEVENTF_KEYUP
	if ext:
		extended = win32con.KEYEVENTF_EXTENDEDKEY
	if shift:
		win32api.keybd_event(win32con.VK_SHIFT, 0, up | extended, 0)
	else:
		win32api.keybd_event(win32con.VK_CONTROL, 0, up | extended, 0)

def shift_type(hwnd, key_code):
	control_event(shift=True)
	win_sleep(FAST_SLEEP)
	post_char(hwnd, key_code)
	control_event(1, 1, shift=True)
	win_sleep(FAST_SLEEP)
	control_event(up=1, shift=True)

def control_type(hwnd, key_code):
	control_event()
	win_sleep(FAST_SLEEP)
	post_char(hwnd, key_code)
	control_event(1, 1)
	win_sleep(FAST_SLEEP)
	control_event(1)

def post_char(hwnd, char):
	win32gui.PostMessage(hwnd, win32con.WM_CHAR, ord(char), 0) 

def close_window(hwnd):
	win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def post_close(hwnd):
	win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def post_click(hwnd):
	win32gui.PostMessage(hwnd, win32con.BM_CLICK, 0, 0) 

def post_press(hwnd, code):
	win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, code, 0)

def post_release(hwnd, code):
	win32api.PostMessage(hwnd, win32con.WM_KEYUP, code, 0)

def post_type(hwnd, code):
	post_press(hwnd, code)
	post_release(hwnd, code)

def send_char(hwnd, char):
	win32gui.SendMessage(hwnd, win32con.WM_CHAR, ord(char), 0) 

def post_enter(hwnd):
	'''
	kita gunakan post-enter di keyboard module utk ngetik type-interval-chars
	'''
	win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def send_enter(hwnd):
	win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def post_tab(hwnd):
	'''
	kita gunakan post-tab over send-tab utk type-interval-chars
	'''
	win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_TAB, 0)
	win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_TAB, 0)

def send_tab(hwnd):
	win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_TAB, 0)
	win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_TAB, 0)

def post_backspace(hwnd):
	win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_BACK, 0)
	win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_BACK, 0)

def send_backspace(hwnd):
	win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_BACK, 0)
	win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_BACK, 0)

def post_home(hwnd):
	win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_HOME, 0)
	win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_HOME, 0)

def send_home(hwnd):
	win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_HOME, 0)
	win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_HOME, 0)

def calculate_typing_speed(isi_tulisan, cpm):
	panjang_tulisan = len(isi_tulisan)
	if not isi_tulisan or len(isi_tulisan) == 0:
		panjang_tulisan = 1
	harus_selesai_dlm_berapa_detik = float ( panjang_tulisan * 60 / float(cpm) )
	interval_ngetik = float ( 1 / (panjang_tulisan / harus_selesai_dlm_berapa_detik) )
	return interval_ngetik

def repeating(string):
	'''
	https://stackoverflow.com/questions/34212898/check-for-repeated-characters-letter-in-a-string
	'''
	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			return True, (i, i+1)
	return False, None

def exec_long_running_cmd(hwnd, text, judul, cpm=3000):
	'''
	krn kita lempar str 'title xxx' maka ini hanya jalan utk cmd
	'''
	while repeating(judul):
		_, x, y = repeating(judul)
		judul = judul[:x] + judul[y:]
	interval = calculate_typing_speed(text, cpm)
	post_chars(hwnd, text, interval)
	post_cmd(hwnd, 'title %s' % judul, interval)
	start = time.time()
	while judul not in get_window_title(hwnd):
		time.sleep(SLEEP_CREATION_TIME * 2.5)
	end = time.time()
	return (end - start)

def wait_for_other_cmd(master_hwnd, judul, slave_hwnd=None):
	'''
	called after long running command is invoked in master_hwnd
	'''
	post_cmd(master_hwnd, 'title %s' % judul)

	while judul not in get_window_title(master_hwnd):
		if slave_hwnd: post_chars(slave_hwnd, '.', SLEEP_CREATION_TIME * 2.5)
		# time.sleep(SLEEP_CREATION_TIME)
		time.sleep(1) # entah kenapa hrs gini

def post_chars_handling_double(hwnd, characters, interval=0):
	'''
	digunakan utk window yg gak bisa handle 2 consecutive repeated chars
	docker window, cmd prompt baru dll
	'''
	# SLEEP_TIME = {'cmd':0.25, 'np':1.0, 'typing':0.5, 'fast':0.1, 'fast_init':0.05}
	DOCKERTERMINAL_CANNOTHANDLE_REPEATEDCHARS_TIME = SLEEP_CREATION_TIME * 2.5 # 0.75s, 0.7s minimum
	for baris in characters.split('\n'):
		last = None
		for c in baris:
			if c == '\t':
				post_tab(hwnd)
			else:
				if last == c:
					time.sleep(DOCKERTERMINAL_CANNOTHANDLE_REPEATEDCHARS_TIME)
					post_char(hwnd, c)
				post_char(hwnd, c)
				last = c
			time.sleep(interval)
		post_enter(hwnd)
		# time.sleep(SLEEP_TIME['typing'])
		time.sleep(SLEEP_CREATION_TIME)

def post_cmd_handling_double(hwnd, chars, interval=0):
	post_chars_handling_double(hwnd, chars, interval)    
	post_enter(hwnd)
	# time.sleep(interval if interval else SLEEP_CREATION_TIME)
	time.sleep(1) # entah kenapa hrs gini

def post_cmd_cpm(hwnd, chars, cpm=4000, press_enter=True):
	'''
	'''
	interval = calculate_typing_speed(chars, cpm)
	# print(f'post_cmd_cpm, cpm {cpm}, typing interval {interval}')
	post_chars(hwnd, chars, interval)
	# time.sleep(0.5) # entah kenapa hrs gini
	# input('PRE')
	if press_enter:
		post_enter(hwnd)
	# time.sleep(interval if interval else SLEEP_CREATION_TIME)
	# time.sleep(1.0)
	# input('POST')

def post_cmd(hwnd, chars, interval=0):
	'''
	digunakan utk ganti title dari cmd misalnya
	post_cmd(cmdhwnd, 'title %s' % (new_title))
	tapi gagal dml handling repeated chars
	'''
	post_chars(hwnd, chars, interval)
	post_enter(hwnd)
	# time.sleep(interval if interval else SLEEP_CREATION_TIME)
	time.sleep(1) # entah kenapa hrs gini

def post_notepadpp(hwnd, chars, interval=0):
	for c in chars:
		if c == "\n":
			post_enter(hwnd)
			time.sleep(0.3) # kasih wkt sblm home...
			post_home(hwnd)
		elif c == "\t":
			post_tab(hwnd)
		else:
			post_char(hwnd, c)

		if interval > 0:
			time.sleep(interval)

def post_tab_chars(hwnd, chars, interval=0):
	for c in chars:
		if c == "\n":
			post_enter(hwnd)
		elif c == "\t":
			post_tab(hwnd)
		else:
			post_char(hwnd, c)

		if interval > 0:
			time.sleep(interval)

def post_chars(hwnd, chars, interval=0):
	for c in chars:
		if c == "\n":
			post_enter(hwnd)
		else:
			post_char(hwnd, c)

		if interval > 0:
			time.sleep(interval)

def send_chars(hwnd, chars):
	'''
	https://stackoverflow.com/questions/5080777/what-sendmessage-to-use-to-send-keys-directly-to-another-window
	pecah di newline
	perlu bikin versi post nya???
	'''
	for c in chars:
		if c == "\n":
			send_enter(hwnd)
		else:
			send_char(hwnd, c)

def send_click(hwnd):
	win32gui.SendMessage(hwnd, win32con.BM_CLICK, 0, 0) 

def send_press(hwnd, code):
	win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, code, 0)

def send_release(hwnd, code):
	win32api.SendMessage(hwnd, win32con.WM_KEYUP, code, 0)

def send_type(hwnd, code):
	send_press(hwnd, code)
	send_release(hwnd, code)

def type_keys(text, interval=0):
	for c in text:
		if c == "\n":
			shell.SendKeys('{ENTER}')
		else:
			shell.SendKeys(c)
		if interval > 0:
			time.sleep(interval)

def send_keys(text):
	"""
	shell.SendKeys('abc')
	shell.SendKeys('^v')  # Ctrl+V, gimana dg alt, shift?
	shell.SendKeys('{ENTER}')  # Enter key
	"""
	shell.SendKeys(text)

def find_window(window_name):
	'''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
	'''
	try:
		return win32gui.FindWindow(None, window_name)
	except win32gui.error:
		print("Error while finding the window")
		return None

def get_hwnd_by_window_name(window_name):
	'''
	win32gui.FindWindow(class_text, title_text)
	'''
	return win32gui.FindWindow(None, window_name)

def get_hwnd_by_class_name(class_name):
	'''
	win32gui.FindWindow(class_text, title_text)
	'''
	return win32gui.FindWindow(class_name, None) # None atau 0

def get_hwnd_by_class_name_ex(class_name):
	'''
	last_child = 0
	child_control = win32gui.FindWindowEx(parent_hwnd, last_child, class_text, None)
	child_control = win32gui.FindWindowEx(parent_hwnd, 0, class_text, title_text)

	edit_hwnd = win32gui.FindWindowEx(maineditor_hwnd, 0, edit_control, 0)
	'''
	return win32gui.FindWindowEx(None, None, class_name, None)

def get_hwnd_by_class_name_and_parent(parent_hwnd, class_name):
	'''
	args: parent hwnd, last child (?), class text, window/title text

	last_child = 0
	child_control = win32gui.FindWindowEx(parent_hwnd, last_child, class_text, None)
	child_control = win32gui.FindWindowEx(parent_hwnd, 0, class_text, title_text)

	edit_hwnd = win32gui.FindWindowEx(maineditor_hwnd, 0, edit_control, 0)
	'''
	return win32gui.FindWindowEx(parent_hwnd, None, class_name, None)

def get_child_windows(hwnd):
	child_windows = []
	try:
		win32gui.EnumChildWindows(hwnd, lambda hwnd, container: container.append(hwnd), child_windows)
	except Exception as e:
		# print str(e)
		return []
	return child_windows

def get_child_windows_with_names(hwnd):
	"""
	child_windows = []
	win32gui.EnumChildWindows(hwnd, lambda hwnd, container: container.append('%d - %s' % (hwnd, get_window_title(hwnd))), child_windows)
	return child_windows
	"""
	return ['%d - %s' % (window, get_window_title(window)) for window in get_child_windows(hwnd)]

def get_child_windows_with_title_and_class(hwnd):
	"""
	mencari child hwnd dari class name bukan dari title !!!
	"""
	return ['%10d - [%-25s] - [%-25s]' % (window, get_window_title(window), get_window_classname(window)) for window in get_child_windows(hwnd)]

def get_child_windows_with_paths(hwnd):
	return ['%d - %s' % (window, get_procname_from_hwnd(window)) for window in get_child_windows(hwnd)]

def get_parent_hwnd(hwnd):
	return win32gui.GetParent(hwnd)

def get_hwnd_by_name(window_name):
	'''
	beda enum windows dan enum child windows
	ew: cb, []
	ecw: hwnd, cb, []
	'''
	hwnd = get_hwnd_by_window_name(window_name)
	if hwnd == 0:
		def callback(hwnd, hwnds): # hwnds = lparam atau param saja = container (istilah kita)
			if window_name in get_window_title(hwnd): # win32gui.GetWindowText(hwnd):
				hwnds.append(hwnd)
			return True
		hwnds_of_name = []
		win32gui.EnumWindows(callback, hwnds_of_name)
		if not hwnds_of_name: 
			return 0
		if len(hwnds_of_name) == 1: 
			return hwnds_of_name[0]
		return hwnds_of_name
	return hwnd

def is_visible(hwnd):
	return win32gui.IsWindowVisible(hwnd)

def is_enabled(hwnd):
	return win32gui.IsWindowEnabled(hwnd)

def is_alive(hwnd):
	return win32gui.IsWindow(hwnd)

def is_always_on_top(hwnd):
	return win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST

def is_minimized(hwnd):
	"""
	https://stackoverflow.com/questions/60471477/using-python-how-can-i-detect-whether-a-program-is-minimized-or-maximized
	"""
	minimized = False
	tup = win32gui.GetWindowPlacement(hwnd)
	if tup[1] == win32con.SW_SHOWMAXIMIZED:
		minimized = False
	elif tup[1] == win32con.SW_SHOWMINIMIZED:
		minimized = True
	elif tup[1] == win32con.SW_SHOWNORMAL:
		normal = True
	return minimized

def hide_from_taskbar(hwnd):
	'''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
	'''
	try:
		win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
		win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TOOLWINDOW)
		win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
	except win32gui.error:
		print("Error while hiding the window")
		return None

def bring_to_top(hwnd, restore_if_minimized=True):
	if restore_if_minimized and is_minimized(hwnd):
		restore_window(hwnd)
	win32gui.BringWindowToTop(hwnd)

def set_top(hwnd):
	"""
	https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowpos
	HWND_BOTTOM
	HWND_NOTOPMOST
	HWND_TOP
	HWND_TOPMOST
	"""
	win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0,0,0,0, win32con.HWND_TOP | win32con.SWP_SHOWWINDOW)

def set_not_topmost(hwnd):
	'''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
	https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
	root = Tk()
	root.wm_attributes("-topmost", 1)
	'''
	try:
		win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
	except win32gui.error:
		print ("Error while moving window to top")

def set_topmost(hwnd, reverse=False):
	'''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
	https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
	root = Tk()
	root.wm_attributes("-topmost", 1)
	'''
	try:
		if reverse:
			set_not_topmost(hwnd)
		else:
			win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
	except win32gui.error:
		print ("Error while moving window to top")

def set_bottommost(hwnd):
	'''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
	https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
	https://stackoverflow.com/questions/812686/can-a-window-be-always-on-top-of-just-one-other-window
	'''
	try:
		win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0,0,0,0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
	except win32gui.error:
		print ("Error while moving window to bottom")

def set_topmost_size(hwnd, x,y, w,h):
	'''https://stackoverflow.com/questions/12439417/set-another-program-to-always-be-on-top
	'''
	return win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h, 0)

def make_parent_child(parent_hwnd, child_hwnd):
	'''https://stackoverflow.com/questions/812686/can-a-window-be-always-on-top-of-just-one-other-window
	agar child window di atas parent window
	'''
	win32gui.SetWindowLong(child_hwnd, win32con.GWL_HWNDPARENT, parent_hwnd)

class WINDOWPOS(ctypes.Structure):
	_fields_ = [
		('hwnd', ctypes.c_ulong),
		('hwndInsertAfter', ctypes.c_ulong),
		('x', ctypes.c_int),
		('y', ctypes.c_int),
		('cx', ctypes.c_int),
		('cy', ctypes.c_int),
		('flags', ctypes.c_ulong)
	]

def mywndproc(oldWndProc, hWnd, msg, wParam, lParam, parent_hwnd):
	'''https://stackoverflow.com/questions/812686/can-a-window-be-always-on-top-of-just-one-other-window
	'''
	if msg == win32con.WM_WINDOWPOSCHANGING:
		pos = WINDOWPOS.from_address(lParam)
		pos.hwndInsertAfter = parent_hwnd # win32con.HWND_BOTTOM
	elif msg == win32con.WM_DESTROY:
		win32gui.SetWindowLong(hWnd, win32con.GWL_WNDPROC, oldWndProc)
	return win32gui.CallWindowProc(oldWndProc, hWnd, msg, wParam, lParam)

def set_new_wndproc(hwnd, new_wndproc):
	'''https://www.programcreek.com/python/example/63320/win32con.GWL_WNDPROC
	bisa win32api atau win32gui
	'''
	old_wndproc = win32gui.SetWindowLong(hwnd, win32con.GWL_WNDPROC, new_wndproc)
	# old_wndproc = win32api.SetWindowLong(hwnd, win32con.GWL_WNDPROC, new_wndproc)
	return old_wndproc

def set_new_wndproc_mm(hwnd, message_map):
	'''https://www.programcreek.com/python/example/63320/win32con.GWL_WNDPROC
	message_map = {
		win32con.WM_COMMAND: self.OnCommand,
		win32con.WM_CONTEXTMENU: self.OnContextMenu,
		win32con.WM_DESTROY: self.OnDestroy,
		win32con.WM_NOTIFY:  self.OnNotify,
		win32con.WM_SIZE: self.OnSize,
	}
	'''
	old_wndproc = win32gui.SetWindowLong(hwnd, win32con.GWL_WNDPROC, message_map)
	return old_wndproc

def load_dll(dll_library): # "Scintilla.dll"
	try:
		win32api.GetModuleHandle(dll_library)
	except win32api.error:
		for p in sys.path:
			fname = os.path.join(p, dll_library)
			if not os.path.isfile(fname):
				fname = os.path.join(p, "Build", dll_library)
			if os.path.isfile(fname):
				win32api.LoadLibrary(fname)
				break
		else:
			raise RuntimeError("Can't find %s!" % dll_library)

def get_hwnd_focus():
	return win32gui.GetFocus()

def get_hwnd_foreground():
	return win32gui.GetForegroundWindow()

def set_focus(app_name):
	'''https://stackoverflow.com/questions/1080719/screenshot-an-application-in-python-regardless-of-whats-in-front-of-it
	'''
	shell = win32com.client.Dispatch("Wscript.Shell")
	return shell.AppActivate(app_name) # Returns true if focus given successfully.

def set_hwnd_foreground(hwnd):
	'''
	bisa juga sblm ini sendkeys dulu % spt di:
	https://stackoverflow.com/questions/30200381/python-win32gui-setasforegroundwindow-function-not-working-properly
	'''
	win32gui.SetForegroundWindow(hwnd)

def set_hwnd_top(hwnd):
	win32gui.BringWindowToTop(hwnd)

def set_hwnd_active(hwnd):
	win32gui.SetActiveWindow(hwnd)

# START: operasi2 pada window yg aktif
def get_hwnd_active():
	return get_hwnd_foreground()

def set_active_topmost(reverse=False):
	wnd = get_hwnd_active()
	if wnd:
		print(f"[app.windowsutils] set_topmost, hwnd: {wnd}, reverse: {reverse}")
		set_topmost(wnd, reverse=reverse)

def set_active_top():
	wnd = get_hwnd_active()
	if wnd:
		set_top(wnd)

def set_active_bringtotop():
	wnd = get_hwnd_active()
	if wnd:
		bring_to_top(wnd)
	
def set_active_title(title):
	wnd = get_hwnd_active()
	if wnd:
		print('[app.windowsutils:set_active_title] coba set title ke:', title)
		set_window_title(wnd, title)

def set_active_transparent(amount):
	wnd = get_hwnd_active()
	if wnd:
		make_transparent(wnd, amount=amount)
# END: operasi2 pada window yg aktif

def make_current_transparent(amount=200):
	make_transparent(get_hwnd_foreground(), amount)

def make_transparent(hwnd, amount):
	_winlib = win32api.LoadLibrary("user32")
	pSetLayeredWindowAttributes = win32api.GetProcAddress(_winlib, "SetLayeredWindowAttributes")
	if pSetLayeredWindowAttributes is None: return
	exstyle = win32api.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
	if 0 == (exstyle & 0x80000):
		exstyle |= win32con.WS_EX_LAYERED | win32con.WS_EX_TOOLWINDOW | win32con.WS_EX_TRANSPARENT
		win32api.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, exstyle)
	win32gui.SetLayeredWindowAttributes(hwnd, 0, amount, 2)

def set_transparent(hwnd, amount):
	'''https://stackoverflow.com/questions/29458775/tkinter-see-through-window-not-affected-by-mouse-clicks
	'''
	# hwnd = root.winfo_id() getting hwnd with Tkinter windows
	# hwnd = root.GetHandle() getting hwnd with wx windows
	lExStyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
	lExStyle |=  win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED 
	win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE , lExStyle )
	win32gui.SetLayeredWindowAttributes(hwnd, 0, amount, 2)

'''
https://www.programcreek.com/python/example/89840/win32gui.ShowWindow
https://www.programcreek.com/python/example/104595/win32api.SetWindowLong

# Set the WndProc to our function.
self.oldWndProc = win32gui.SetWindowLong (self.hwnd, win32con.GWL_WNDPROC, self.MyWndProc)
def MyWndProc (self, hWnd, msg, wParam, lParam):
	# Pass all messages (in this case, yours may be different) on to the original WndProc
	return win32gui.CallWindowProc (self.oldWndProc, hWnd, msg, wParam, lParam) 

# Restore the old WndProc
# Notice the use of win32api instead of win32gui here. 
# This is to avoid an error due to not passing a callable object.
win32api.SetWindowLong (self.hwnd, win32con.GWL_WNDPROC, self.oldWndProc)
'''

# from toastr import _DH

# def entry(text, title=None, placeholder=None):    
#     entry_run = _DH.entry_run
#     if title and placeholder:
#         entry_run(text, title, placeholder)
#     elif title:
#         entry_run(text, title)
#     elif placeholder:
#         entry_run(text, placeholder=placeholder)
#     else:
#         entry_run(text)

def message(text):
	win32ui.MessageBox(text)

def msgok(text, title='Message'):
	win32api.MessageBox(0, text, title, win32con.MB_OK) 
	# win32con.MB_ICONERROR win32con.MB_YESNO win32con.MB_YESNOCANCEL
	# win32con.IDYES

def msgyesno(text, title='Message'):
	win32api.MessageBox(0, text, title, win32con.MB_YESNO) 

def get_windows_messages():
	msgdict = dict()
	for name in dir(win32con):
		if name.startswith('WM_'):
			value = getattr(win32con, name)
			msgdict[value] = name
	return msgdict # print msg, '->', msgdict.get(msg)

def maximize_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def minimize_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_FORCEMINIMIZE)

def show_max_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)

def show_noact_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_SHOWNOACTIVATE)

def show_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

def hide_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_HIDE) # 0 ?

def normal_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)

def restore_window(hwnd):
	win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

def get_hwnd_desktop():
	return win32gui.GetDesktopWindow()

def get_monitors():
	'''
	[ (pyhandle, pyhandle, (x,y,w,h)), (..), (..), ... ]
	'''
	return win32api.EnumDisplayMonitors()

def get_window_classname(hwnd):
	return win32gui.GetClassName(hwnd)

def get_window_title(hwnd):
	return win32gui.GetWindowText(hwnd)

def set_window_title(hwnd, text):
	win32gui.SetWindowText(hwnd, text)

def get_procname_from_pid(pid): # procname = procpath
	"""
	exception:
	pywintypes.error: (5, 'OpenProcess', 'Access is denied.') wkt openprocess

	try:
		hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, pywintypes.FALSE, pid)
	except pywintypes.error, err:
		print str(err)

	hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, win32con.FALSE, pid)
	"""
	try:
		hproc = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
	except Exception as e1:
		# print 'Exc1:', e1.message
		try:
			hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
		except Exception as e2:
			# print 'Exc2:', e2.message
			return None
			# try:
			#     hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
			# except Exception as e3:
			#     print 'Exc3:', e3.message
	return get_procname_from_prochandle(hproc)
	# procname = win32process.GetModuleFileNameEx(hproc, 0)
	# return procname

def get_procname_from_prochandle(proc_handle, module_id=0):
	return str( win32process.GetModuleFileNameEx(proc_handle, module_id) )

def get_procpath_from_pid(pid):
	'''
	berikut ini salah: krn get_procpath_from_pid adlh instance, dia mengingat pid yg sblmnya
	get_procpath_from_pid = get_procname_from_pid
	'''
	return get_procname_from_pid(pid)

def get_procname_from_hwnd(hwnd):
	return get_procname_from_pid(get_pid_from_hwnd(hwnd))

def get_hwnd_from_pid(pid):
	'''
	https://www.programcreek.com/python/example/100815/win32gui.EnumWindows
	kita enumwindows di sistem
	utk tiap hwnd kita ambil tid, pid dari get window thread process id
	jk ketemu pid, masukkan ke container/holder/lparam/arg kedua dari callback
	'''
	def callback(hwnd, hwnds):
		if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
			_, _pid = win32process.GetWindowThreadProcessId(hwnd)
			if _pid == pid:
				hwnds.append(hwnd)
		return True
	hwnds_of_pid = []
	win32gui.EnumWindows(callback, hwnds_of_pid)
	if not hwnds_of_pid:
		return 0
	if len(hwnds_of_pid) == 1:
		return hwnds_of_pid[0]
	return hwnds_of_pid

def get_hwnd_from_pid2(pid):
	"""
	https://stackoverflow.com/questions/70618975/python-get-windowtitle-from-process-id-or-process-name
	"""
	def callback(hwnd, hwnds):
		#if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
		_, found_pid = win32process.GetWindowThreadProcessId(hwnd)

		if found_pid == pid:
			hwnds.append(hwnd)
		return True
	hwnds = []
	win32gui.EnumWindows(callback, hwnds)
	return hwnds 

def get_pid_from_hwnd(hwnd):
	_, pid = win32process.GetWindowThreadProcessId(hwnd)
	return pid

def netstat(filter='LISTENING'):
	p = subprocess.Popen(['netstat', '-ona'], stdout=subprocess.PIPE)
	out, _ = p.communicate()
	pecah = out.split('\n')
	return [item.strip() for item in pecah if filter in item]

def tasklist():
	'''
	https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
	any, all, bool
	'''
	p = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE)
	out, _ = p.communicate()
	pecah = out.splitlines() # out.split('\n') # gak nyisakan \r yg perlu distrip dulu
	return [item.replace(' K', 'K').replace(' M', 'M').replace(' G', 'G') for item in pecah if any(char.isdigit() for char in item)]

def tkill3(pid_or_name, verbose=True):
	task = ['TSKILL']
	task.append(pid_or_name)
	if verbose:
		task.append('/V')
	os.system(' '.join(task))

def tkill2(procname, children=True, force=True):
	task = ['TASKKILL']
	if force:
		task.append('/F')
	if children:
		task.append('/T')
	task.append('/IM')
	task.append(procname)
	os.system(' '.join(task))

def tkill(pid, children=True, force=True):
	'''
	https://stackoverflow.com/questions/2940858/kill-process-by-name
	bs gunakan psutil
	juga split('\n') ada juga namanya splitlines() mungkin lebih baik krn gak nyisakan \r
	'''
	task = ['TASKKILL']
	if force:
		task.append('/F')
	if children:
		task.append('/T')
	task.append('/PID')
	task.append(pid)
	os.system(' '.join(task))

def get_pid_from_name(proc_name):
	proc_name = proc_name.lower()
	for pid in get_all_pids():
		if pid == cur_pid():
			continue
		try:
			hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, pid)
			try:
				mids = win32process.EnumProcessModules(hproc)
				for mid in mids:
					proc_name_found = get_procname_from_prochandle(hproc, mid) # str(win32process.GetModuleFileNameEx(hproc, mid))
					if proc_name_found.lower().find(proc_name) != -1:
						return pid
			finally:
				win32api.CloseHandle(hproc)
		except:
			pass
	return None

def all_windows():
	'''
	hwnd = 0 memberikan semua windows yg visible dan invisible ?
	'''
	return get_child_windows(0)

def get_visible_windows():
	def callback(hwnd, hwnds):
		if is_visible(hwnd) and is_enabled(hwnd):
			hwnds.append(hwnd)
	hwnds = []
	win32gui.EnumWindows(callback, hwnds)
	return hwnds

def get_visible_title_hwnd():
	return map(lambda item: (get_window_title(item), item), get_visible_windows())

def get_invisible_windows():
	def callback(hwnd, hwnds):
		if not is_visible(hwnd):
			hwnds.append(hwnd)
	hwnds = []
	win32gui.EnumWindows(callback, hwnds)
	return hwnds

def get_procinfos_from_hwnds(hwnds):
	# return [process_info_hwnd(item) for item in hwnds]
	return [ProcInfo(item, allow_hwnd_0=True) for item in hwnds]

class ProcInfo:

	def __repr__(self):
		cetak = f"""
		hwnd = {self.hwnd}
		pid = {self.pid}

		path = {self.path}
		title = {self.title}
		cname = {self.classname}
		alive = {self.alive}
		"""
		return cetak

	def __init__(self, pid=None, hwnd=None, allow_hwnd_0=False):
		self.hwnd = hwnd
		self.pid = pid

		self.path = None
		self.title = None
		self.classname = None
		self.parent = None
		self.alive = False

		self.children = None
		self.allow_hwnd_0 = allow_hwnd_0
		# print('allow hwnd 0? %s' % allow_hwnd_0)

		self.initialize()

	def dump(self):
		self.short_refresh()
		for attr in self.__dict__:
			print ("obj.%s = %r" % (attr, getattr(self, attr)))

	def dump_list(self):
		self.short_refresh()
		return ["obj.%s = %r" % (attr, getattr(self, attr)) for attr in self.__dict__]

	def initialize(self):
		'''
		butuh either pid atau hwnd utk mengisi field2 lain
		'''

		if self.pid:
			if not self.hwnd:
				self.hwnd = get_hwnd_from_pid (self.pid)

		elif self.hwnd:
			if not self.pid:
				self.pid = get_pid_from_hwnd (self.hwnd)

		else:
			print ('not having pid or hwnd')
			return

		# print('ProcInfo: pid %d hwnd %d' % (self.pid, self.hwnd))
		if not self.allow_hwnd_0:
			while self.hwnd == 0:
				self.hwnd = get_hwnd_from_pid (self.pid)
				sys.stdout.write('.')
				win_sleep(100)
		else:
			win_sleep(WINDOW_CREATION_TIME)

		self.path = get_procpath_from_pid (self.pid)
		self.title = get_window_title ( self.hwnd )
		print('ProcInfo: pid %d hwnd %d title %s' % (self.pid, self.hwnd, self.title))
		try:
			self.classname = get_window_classname ( self.hwnd )
		except Exception as e:
			# print 'get class exc', str(e)
			self.classname = None
		try:
			self.parent = get_parent_hwnd ( self.hwnd )
		except Exception as e:
			# print 'get parent exc', str(e)
			self.parent = None
		self.alive = is_alive(self.hwnd)

	def short_refresh(self):
		self.alive = is_alive(self.hwnd)
		self.title = get_window_title ( self.hwnd )

	def refresh(self):
		self.hwnd = get_hwnd_from_pid (self.pid)
		while self.hwnd == 0:
			self.hwnd = get_hwnd_from_pid (self.pid)
			sys.stdout.write('.')
			win_sleep(100)

		self.path = get_procpath_from_pid (self.pid)
		self.title = get_window_title ( self.hwnd )
		self.classname = get_window_classname ( self.hwnd )
		self.parent = get_parent_hwnd ( self.hwnd )
		self.alive = is_alive(self.hwnd)
		
	def assign(self, path, title, classname, parent):
		self.path = path
		self.title = title
		self.classname = classname
		self.parent = parent

	# end class

def process_info_hwnd(hwnd):
	return ProcInfo(hwnd=hwnd)

def process_info_hwnd_whocares(hwnd, allow_hwnd_0=True):
	return ProcInfo(hwnd=hwnd, allow_hwnd_0=allow_hwnd_0)

def process_info(pid):
	return ProcInfo(pid)

def process_info_children(pid):
	# proc_info = get_process_info(pid)
	# proc_info['children'] = get_child_windows ( proc_info['hwnd'] )
	proc_info = ProcInfo(pid)
	proc_info.children = get_child_windows ( proc_info.hwnd )
	return proc_info

def create_process(command, allow_hwnd_0=False):
	'''
	kebalikan dari win32process createprocess:
	tid, pid = win32process.GetWindowThreadProcessId(hwnd)

	kembalian MakeProcess adlh:
	hproc, hthr, pid, tid
	CREATE_NEW_CONSOLE setara shell=True di subprocess
	'''
	_, _, pid, _ = MakeProcess(CMD=command, CREAF=win32process.CREATE_NEW_CONSOLE)
	_all_proc_infos.append(ProcInfo(pid=pid, allow_hwnd_0=allow_hwnd_0))
	return pid

def check_hwnd_0(command):
	program = command.split()[0].lower()
	print ('check_hwnd_0: cmd [%s] program [%s]' % (command, program))
	if program in _all_hwnd_0:
		return True
	return False

def create_process_info(command, wait_time=WINDOW_CREATION_TIME):
	pid = create_process(command, allow_hwnd_0=check_hwnd_0(command))
	win_sleep(wait_time)
	return process_info(pid)

def print_process_info(info):
	info.dump()
	# for k, v in info.iteritems():
	#     print '%s = [%s]' % (k, v)

def get_edit_window(npp=False): # np or npp
	"""
	https://stackoverflow.com/questions/21917965/send-keys-to-a-inactive-window-in-python
	arg kedua berarti win title
	notepad = win32gui.FindWindow("notepad", "prueba.txt: Bloc de notas")
	"""
	program = "notepad++" if npp else "notepad"
	edit_control = "Scintilla" if npp else "Edit"
	maineditor_hwnd = get_hwnd_by_class_name(program) # win32gui.FindWindow(program, 0)
	edit_hwnd = get_hwnd_by_class_name_and_parent(maineditor_hwnd, edit_control) # win32gui.FindWindowEx(maineditor_hwnd, 0, edit_control, 0)

	return edit_hwnd

def get_scintilla_hwnd(npp_hwnd):
	npp_scintilla = None

	for child_hwnd in get_child_windows(npp_hwnd):
		if get_window_classname(child_hwnd) == 'Scintilla':
			npp_scintilla = child_hwnd
			break
	return npp_scintilla

def test_windows():
	hwnds = get_visible_windows()
	pinfos = get_procinfos_from_hwnds(hwnds)
	for proc in sorted([item['path'] for item in pinfos]):
		print (proc)

	print ()
	print (".....................invisible.....................")
	print ()

	# for proc in sorted(get_procinfos_from_hwnds(get_invisible_windows()), keys=lambda item: item['path']):
	for proc in sorted(get_procinfos_from_hwnds(get_invisible_windows())):
		print (proc)

def refresh_icon(hwnd, myicon, notify_id, hover_text):
	'''
	https://www.programcreek.com/python/example/53226/win32gui.NIF_ICON
	'''
	# Try and find a custom icon
	hinst = win32gui.GetModuleHandle(None)
	if os.path.isfile(myicon):
		icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
		hicon = win32gui.LoadImage(hinst,
									myicon,
									win32con.IMAGE_ICON,
									0,
									0,
									icon_flags)
	else:
		print ("Can't find icon file - using default.")
		hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

	if notify_id: message = win32gui.NIM_MODIFY
	else: message = win32gui.NIM_ADD
	notify_id = (hwnd,
						0,
						win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP,
						win32con.WM_USER+20,
						hicon,
						hover_text)
	win32gui.Shell_NotifyIcon(message, notify_id)
#####################################
def choose_file(filename="catatan", extension=".txt", mask="Text Files (*.txt)|*.txt|All Files (*.*)|*.*|"):
	select_dlg = win32ui.CreateFileDialog(0, extension, filename, 0, mask)
	select_dlg.DoModal()
	selected_file = select_dlg.GetPathName()
	print (selected_file)

def choose_folder():
	'''
	http://timgolden.me.uk/python/win32_how_do_i/browse-for-a-folder.html
	https://stackoverflow.com/questions/277053/filechooser-to-select-a-directory-not-a-file
	https://stackoverflow.com/questions/16108503/how-to-open-folder-with-specified-items-selected-on-windows
	'''    
	desktop_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_DESKTOP, 0, 0)
	mydocs_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_PERSONAL, 0, 0)
	desktop = shell.SHGetDesktopFolder()
	temp_pidl = shell.SHILCreateFromPath (win32api.GetTempPath(), 0)[0]
	urepl_pidl = shell.SHILCreateFromPath (os.path.join(win32api.GetTempPath(), 'urepl'), 0)[0]
	shell_folder = desktop.BindToObject(temp_pidl, None, shell.IID_IShellFolder)
	# items = [item for item in shell_folder][:5]
	## print (items)
	# shell.SHOpenFolderAndSelectItems(folder_pidl, items, 0)
	# https://mail.python.org/pipermail/python-win32/2012-September/012533.html
	# name_to_item_mapping = dict([(desktop.GetDisplayNameOf(item, 0), item)
	# for item in shell_folder])
	#     to_show = []
	#     for file in files:
	#         if not name_to_item_mapping.has_key(file):
	#             raise Exception('File: "%s" not found in "%s"' % (file, path))
	#         to_show.append(name_to_item_mapping[file])
	#     shell.SHOpenFolderAndSelectItems(folder_pidl, to_show, 0)
	pidl, display_name, image_list = shell.SHBrowseForFolder (
		win32gui.GetDesktopWindow(),
		urepl_pidl,
		"Choose a folder",
		0, # shellcon.BIF_BROWSEINCLUDEFILES utk pilih folder dan/atau file, selanjutnya bs os.startfile(path)
		None,
		None
		)
	choice = shell.SHGetPathFromIDList (pidl)
	print ('Choosen dir [%s]' % choice)
	return choice

def make_process(NAME=None, CMD=None, PATTRS=None, TATTRS=None, INHER=0, CREAF=None, NEWENV=None, CURDIR=None, INFO=win32process.STARTUPINFO(), hide=False, desktop=None):
	"""
	BOOL CreateProcess(
		LPCTSTR lpszImageName,
		LPCTSTR lpszCommandLine,
		LPSECURITY_ATTRIBUTES lpsaProcess,
		LPSECURITY_ATTRIBUTES lpsaThread,
		BOOL fInheritHandles,
		DWORD fdwCreate,
		LPVOID lpvEnvironment,
		LPTSTR lpszCurDir,
		LPSTARTUPINFO lpsiStartInfo,
		LPPROCESS_INFORMATION lppiProcInfo);

	When you call CreateProcess, the system creates a 4-GB virtual address space for the new process and 
	loads the specified process into this address space.
	The system then creates the primary thread for this process.
	This primary thread will begin by executing the C Runtime startup code, which will eventually call your WinMain function.

	cmd = "cmd"
	_, _, pid, tid = MakeProcess(CMD=cmd,CREAF=win32process.CREATE_NEW_CONSOLE)
	hProcess, hThread, dwProcessID, dwThreadID = ...


	https://www.programcreek.com/python/?code=turingsec%2Fmarsnake%2Fmarsnake-master%2Fcore%2Fwinpty.py

	cmd_hwnd = GetNewlyCreatedWindow()
	for c in ('cd %s\r\n' % self.super_kamus['workdir']):
		win32api.PostMessage(cmd_hwnd, win32con.WM_CHAR, ord(c), 0)

	https://stackoverflow.com/questions/21434644/how-to-show-console-app-window-hidden-by-createprocess-function
	Instead of using the CREATE_NO_WINDOW flag, use the wShowWindow member of the STARTUPINFO struct instead. 
	Set it to SW_HIDE initially (and set the dwFlags member to STARTF_USESHOWWINDOW), then you can use ShowWindow() to show/hide the console window when needed. 
	To find the window that belongs to the new process, use EnumWindows() and GetWindowThreadProcessId() to find the window whose process/thread IDs match the IDs that CreateProcess() returns in the PROCESS_INFORMATION struct.

	PROCESS_INFORMATION pi;
	STARTUPINFO si;
	ZeroMemory(&si,sizeof(si));
	si.cb = sizeof(si);
	ZeroMemory(&pi, sizeof(pi);
	si.wShowWindow = SW_SHOW;
	si.dwFlags = STARTF_USESHOWWINDOW;
	si.lpTitle ="my_process_console";
	CreateProcess(null,"my.exe",null,null,false,CREATE_NEW__CONSOLE,null,null,&si,&pi);
				  1     2       3    4    5     6                   7    8    9   10
	https://www.programcreek.com/python/example/25659/win32con.SW_HIDE
	https://www.programcreek.com/python/example/8489/win32process.CreateProcess

	StartupInfo.hStdInput = win32api.GetStdHandle(win32api.STD_INPUT_HANDLE)
	StartupInfo.hStdOutput = win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE)
	StartupInfo.hStdError = win32api.GetStdHandle(win32api.STD_ERROR_HANDLE)
	StartupInfo.dwFlags = win32process.STARTF_USESHOWWINDOW | win32process.STARTF_USESTDHANDLES
	"""

	# https://stackoverflow.com/questions/6312627/windows-7-how-to-bring-a-window-to-the-front-no-matter-what-other-window-has-fo
	# win32gui.ShowWindow(HWND, win32con.SW_RESTORE)

	if hide:
		INFO.dwFlags = win32process.STARTF_USESHOWWINDOW | win32process.STARTF_USESTDHANDLES
		INFO.wShowWindow = win32con.SW_HIDE

	if desktop:
		import win32service
		# https://stackoverflow.com/questions/23694017/start-process-on-the-other-desktop-python-windows
		hDesktop = win32service.CreateDesktop(desktop, 0, win32con.GENERIC_ALL, None)
		win32api.Sleep(500)
		INFO.lpDesktop = desktop

	return win32process.CreateProcess(
		NAME,       # 1 name
		CMD,        # 2 command line
		PATTRS,     # 3 process attributes
		TATTRS,     # 4 thread attributes
		INHER,      # 5 inheritance flag
		CREAF,      # 6 creation flag, win32process.CREATE_NO_WINDOW, win32process.CREATE_NEW_CONSOLE, win32con|win32process.NORMAL_PRIORITY_CLASS
		NEWENV,     # 7 new environment, os.environ
		CURDIR,     # 8 current directory, os.path.dirname(__file__)
		INFO        # 9, StartupInfo = win32process.STARTUPINFO(), StartupInfo.dwFlags = win32process.STARTF_USESHOWWINDOW, StartupInfo.wShowWindow = win32con.SW_NORMAL|win32con.SW_HIDE
	)

def make_process_std(cmd, creaf=win32process.CREATE_NEW_CONSOLE, hide=False, desktop=None, CURDIR=None):
	return make_process(CMD=cmd, CREAF=creaf, hide=hide, desktop=desktop, CURDIR=CURDIR)

def fill_in_hwnds(tidur=0.5):
	"""
	dg modal window name yg berupa uuid
	iterate data cari yg belum ada 'hwnd'nya
	jk blm ada berarti dia jg blm ada 'chwnd'nya
	"""    
	# print('fill_in_hwnds start')
	for index, data in command_prompt_data.items():
		# print(f'fill_in_hwnds {index}')
		if 'hwnd' not in data:
			# pid = data['pid']
			# hwnd = get_hwnd_from_pid(pid)
			# hwnd = get_hwnd_from_pid2(pid)
			window_name = data['id']
			if window_name:
				# time.sleep(tidur)
				hwnd = get_hwnd_by_window_name(window_name)
			# print(f'fill_in_hwnds from title "{window_name}" hwnd {hwnd}.')
			# if hwnd == 0:
			#     time.sleep(tidur)
			#     # mungkin lebih baik, kasih title unik utk pid, abis itu get hwnd dari title
			#     hwnd = get_hwnd_foreground()
			if hwnd != 0:
				command_prompt_data[index]['hwnd'] = hwnd
				child_hwnds = get_child_windows(hwnd)
				if child_hwnds:
					command_prompt_data[index]['chwnd'] = child_hwnds[-1]
					command_prompt_data[index]['chwnds-title'] = {}
					command_prompt_data[index]['chwnds'] = []
					for chwnd in child_hwnds:
						command_prompt_data[index]['chwnds'].append(chwnd)
						judul_anak = get_window_title(chwnd)
						if not judul_anak:
							# utk cmd.exe
							# ternyata jk id gak ditemukan (misal title bar gak ada)
							# maka hwnd utk ngetik adlh chwnd yg gak ada title nya
							# 2 chwnd lain biasanya punya title DesktopWindowXamlSource
							command_prompt_data[index]['chwnd-ngetik'] = chwnd
						command_prompt_data[index]['chwnds-title'][chwnd] = judul_anak
			# get_window_title()
			# get_hwnd_by_window_name()

	# print('fill_in_hwnds end')

# def create_register_cmd(command=f'cmd /k start "{uuid1().hex}"', hide=False, desktop=None):
def create_register_cmd(command=f'cmd /k "title {uuid1().hex}"', identifier=None, hide=False, desktop=None, CURDIR=None):
	"""
	{
		1: {
			'hprocess': <PyHANDLE:1344>,
			'hthread': <PyHANDLE:1540>,
			'pid': 8532,
			'tid': 6620
		}
	}
	>>>
	"""
	# from app.appconfig import command_prompt_data
	hprocess,hthread,pid,tid = make_process_std(command, hide=hide, desktop=desktop, CURDIR=CURDIR)
	index = len(command_prompt_data) + 1
	command_prompt_data[index] = {
		'cmd': command, # command to create with passing window title
		'id': identifier, # window title
		'pid': pid,
		'tid': tid,
		'hprocess': hprocess,
		'hthread': hthread,
	}
	return identifier

def create_register_commandprompt(CURDIR=None):
	judul = uuid1().hex
	command=f'cmd /k "title {judul}"'
	identifier = create_register_cmd(command, identifier=judul, CURDIR=CURDIR)
	# step 2, tambahkan hwnd, biasanya gagal, mungkin perlu sleep cukup lama
	fill_in_hwnds()
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		print('create_register_commandprompt, id:', identifier)
	return identifier

def create_register_commandprompt_with_sleep(tidur=1.0):
	judul = uuid1().hex
	command=f'cmd /k "title {judul}"'
	identifier = create_register_cmd(command, identifier=judul)
	# step 2, tambahkan hwnd
	time.sleep(tidur)
	fill_in_hwnds()
	return identifier

def get_cmd_register_list():
	"""
	app.appconfig.get_cmd_register_list
	utk dipake digui
	"""
	# from app.appconfig import command_prompt_data
	return command_prompt_data

def cmd_register_list():
	"""
	kita lakukan ini dari dalam upy
	from app.windowsutils import (
		cmd_register_list as l,
		create_register_commandprompt as c,
		ketik as k,
		ketik_by_index as ki,
		fill_in_hwnds as fill,
		hapus_by_id as hadi,
	)
	c()
	l()
	fill()
	l()
	ki(1, 'hello')
	"""    
	# from app.richutils import console
	# from app.appconfig import command_prompt_data
	pp(command_prompt_data)

def get_command_prompt_data_index_from_uuidtitle(title):
	# from app.appconfig import command_prompt_data
	data = [k for k,v in command_prompt_data.items() if v['id']==title]
	if data and len(data)==1:
		return data[0]
	return None

def get_hwnd_from_uuidtitle(title):
	"""
	hwnd utk operasi window spt minimize, hide, dsb
	 3: {
		'chwnd': 3933604,
		'chwnds': [3868312, 394214, 4130472, 3933604],
		'cmd': 'cmd /k "title e148f8b112c511ed844c201e886a908d"',
		'hprocess': <PyHANDLE:1816>,
		'hthread': <PyHANDLE:1820>,
		'hwnd': 8521388, <- kita ambil ini
		'id': 'e148f8b112c511ed844c201e886a908d',
		'pid': 11224,
		'tid': 14604}}
	"""
	# from app.appconfig import command_prompt_data
	idx = get_command_prompt_data_index_from_uuidtitle(title)
	if idx:
		if 'hwnd' in command_prompt_data[idx]:
			return command_prompt_data[idx]['hwnd']
	return 0

def get_chwnd_from_uuidtitle(title):
	"""
	chwnd utk operasi ngetik dsb
	 3: {
		'chwnd': 3933604,
		'chwnds': [3868312, 394214, 4130472, 3933604],
		'cmd': 'cmd /k "title e148f8b112c511ed844c201e886a908d"',
		'hprocess': <PyHANDLE:1816>,
		'hthread': <PyHANDLE:1820>,
		'hwnd': 8521388, <- kita ambil ini
		'id': 'e148f8b112c511ed844c201e886a908d',
		'pid': 11224,
		'tid': 14604}}
	"""
	# from app.appconfig import command_prompt_data
	idx = get_command_prompt_data_index_from_uuidtitle(title)
	if idx:
		if 'chwnd' in command_prompt_data[idx]:
			return command_prompt_data[idx]['chwnd']
	return 0

def is_identifier_in_command_prompt_data(identifier):
	# from app.appconfig import command_prompt_data
	data = [k for k,v in command_prompt_data.items() if v['id']==identifier]
	if data and len(data)==1:
		return data[0]
	return False

def ketik(chwnd, pesan, cpm=4000, press_enter=True):
	post_cmd_cpm(chwnd, pesan, cpm=cpm, press_enter=press_enter)

def ketik_by_index(index, pesan, cpm=4000, press_enter=True):
	if index in command_prompt_data:
		if 'chwnd-ngetik' in command_prompt_data[index]:
			ketik(command_prompt_data[index]['chwnd-ngetik'], pesan, cpm=cpm, press_enter=press_enter)
		elif 'chwnd' in command_prompt_data[index]:
			ketik(command_prompt_data[index]['chwnd'], pesan, cpm=cpm, press_enter=press_enter)

def ketik_by_window_title(title, pesan, cpm=4000, press_enter=True):
	chwnd = get_chwnd_from_uuidtitle(title)
	if chwnd:
		ketik(chwnd, pesan, cpm=cpm, press_enter=press_enter)

def hapus_empty(window_name):
	"""
	hapus entry command_prompt_data dg id==window_name jk sudah tidak ada lagi (not find_window)
	kita bisa masukkan fragment dari id yg adlh title dari cmd, dari hasil cmd_register_list()
	'id': 'fbdeb88a129d11eda8bf201e886a908d',
	"""
	# from app.appconfig import command_prompt_data
	# find_window(window_name)
	cek = find_window(window_name)
	if not cek:
		# hapus
		for index, data in command_prompt_data.items():
			if data['id'] == window_name:
				del command_prompt_data[index]

def hapus_by_id(id):
	# from app.appconfig import command_prompt_data
	del command_prompt_data[id]

def hapus_iterate_by_title():
	"""
	Traceback (most recent call last):
	File "C:/Users/usef/work/sidoarjo/schnell/gui/system/searcher/cmder.py", line 226, in <lambda>
		btn1_4.clicked.connect(lambda: hapus_set_combo_items())
	File "C:/Users/usef/work/sidoarjo/schnell/gui/system/searcher/cmder.py", line 224, in hapus_set_combo_items
		hapus_iterate_by_title()
	File "C:/Users/usef/work/sidoarjo/schnell/app/windowsutils.py", line 1648, in hapus_iterate_by_title      
		for k,v in command_prompt_data.items():
	RuntimeError: dictionary changed size during iteration

	https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
	>>> a = {1:'satu',2:'dua',3:'tiga'}
	>>> list(a)
	[1, 2, 3]
	"""
	# from app.appconfig import command_prompt_data
	# for k,v in command_prompt_data.items():
	for k in list(command_prompt_data):
		v = command_prompt_data[k]
		window_name = v['id']
		cek = find_window(window_name)
		if not cek:
			del command_prompt_data[k]

# https://stackoverflow.com/questions/70965202/python-turn-screen-on-and-off-on-windows
def screen_off():
	ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

def screen_on():
	ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
	move_cursor()

def move_cursor():
	# for me on my laptop the code works perfectly as intended. 
	# The use of win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y) 
	# instead of pyautogui.move(1,1) seems to do the trick. 
	x, y = (0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)

# screen_off()
# time.sleep(3)
# screen_on()
soff = screen_off
son = screen_on

# move window to another desktop
# MoveWindowToDesktop
# https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ivirtualdesktopmanager-movewindowtodesktop
# https://www.qiniu.com/qfans/qnso-72232353
# https://www.autohotkey.com/boards/viewtopic.php?t=54202

# https://stackoverflow.com/questions/37009777/how-to-make-a-windows-10-computer-go-to-sleep-with-a-python-script
# need to have administrator permissions to run Powercfg -H *
# turn hibernation off:
# Powercfg -H OFF
# To turn hibernation mode back on:
# Powercfg -H ON
def computer_sleep():
	os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
	# os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
	# C:\Windows\System32\psshutdown.exe -d -t 0 

def application_icon():
	"""
	https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
	https://stackoverflow.com/questions/67599432/setting-the-same-icon-as-application-icon-in-task-bar-for-pyqt5-application
	"""

# from schnell.app.windowsutils import minimize_terminal
def minimize_terminal(pause=0.3):
	# import pyautogui
	# import win32gui
	# import win32con  # Import win32con
	# Get the handle of the Windows Terminal window
	terminal_window = win32gui.GetForegroundWindow()
	# Minimize the Windows Terminal window
	win32gui.ShowWindow(terminal_window, win32con.SW_MINIMIZE)
	if pause:
		time.sleep(pause)
