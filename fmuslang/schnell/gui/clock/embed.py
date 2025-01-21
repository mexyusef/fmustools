# -*- coding: utf-8 -*-

# import win32con
# import win32gui

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
# from win32com.shell.shell import ShellExecuteEx
# from win32com.shell import shellcon
# from win32com.shell import shell
# import win32security
import time, os, sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QApplication


kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32
# user32 = ctypes.WinDLL('user32', use_last_error=True)
# _winlib = win32api.LoadLibrary("user32")
shell = win32com.client.Dispatch('WScript.Shell')

def MakeProcessStd(cmd, creaf=win32process.CREATE_NEW_CONSOLE, hide=False):
    return MakeProcess(CMD=cmd, CREAF=creaf, hide=hide)

# https://www.programcreek.com/python/?code=turingsec%2Fmarsnake%2Fmarsnake-master%2Fcore%2Fwinpty.py
def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        # if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
        # print hwnd
        if found_pid == pid:
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

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

def MakeProcess(NAME=None, CMD=None, PATTRS=None, TATTRS=None, INHER=0, CREAF=None, NEWENV=None, CURDIR=None, INFO=win32process.STARTUPINFO(), hide=False):
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


def get_hwnd_focus():
    return win32gui.GetFocus()

def get_hwnd_foreground():
    return win32gui.GetForegroundWindow()


def get_child_windows(hwnd):
    child_windows = []
    try:
        win32gui.EnumChildWindows(hwnd, lambda hwnd, container: container.append(hwnd), child_windows)
    except Exception as e:
        # print str(e)
        return []
    return child_windows



def post_enter(hwnd):
    '''
    kita gunakan post-enter di keyboard module utk ngetik type-interval-chars
    '''
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def post_char(hwnd, char):
    win32gui.PostMessage(hwnd, win32con.WM_CHAR, ord(char), 0) 

def post_chars(hwnd, chars, interval=0):
    for c in chars:
        if c == "\n":
            post_enter(hwnd)
        else:
            post_char(hwnd, c)

        if interval > 0:
            time.sleep(interval)

def calculate_typing_speed(isi_tulisan, cpm):
    harus_selesai_dlm_berapa_detik = float ( len(isi_tulisan) * 60 / float(cpm) )
    interval_ngetik = float ( 1 / (len(isi_tulisan) / harus_selesai_dlm_berapa_detik) )
    return interval_ngetik

def post_cmd_cpm(hwnd, chars, cpm=4000):
    '''
    '''
    post_chars(hwnd, chars, calculate_typing_speed(chars, cpm))
    post_enter(hwnd)
    # time.sleep(interval if interval else SLEEP_CREATION_TIME)
    time.sleep(1) # entah kenapa hrs gini

def create_command_and_get_last_child_hwnd(command, tidur=1.0):
    _,_,pid,tid = MakeProcessStd(command)
    time.sleep(tidur)
    hwnd = get_hwnd_from_pid(pid)
    if hwnd == 0:
        hwnd = get_hwnd_foreground()
        if hwnd:
            child_hwnds = get_child_windows(hwnd)
            hwnd = child_hwnds[-1]
    return hwnd


def create_command_and_get_own_hwnd_and_last_child_hwnd(command, tidur=1.0, hide=False):
    _,_,pid,tid = MakeProcessStd(command, hide=hide)
    time.sleep(tidur)
    hwnd = 0
    chwnd = 0
    hwnd = get_hwnd_from_pid(pid)
    if hwnd == 0:
        hwnd = get_hwnd_foreground()
        if hwnd:
            child_hwnds = get_child_windows(hwnd)
            if child_hwnds:
                chwnd = child_hwnds[-1]
    return hwnd, chwnd


def send_message_to_last_created_child_hwnd(pesan, command='cmd', tidur=1.0):
    hwnd = create_command_and_get_last_child_hwnd(command, tidur)
    post_cmd_cpm(hwnd, pesan)


class WindowEmbedder(QWidget):

    def __init__(self, *args, **kwargs):
        super(WindowEmbedder, self).__init__(*args, **kwargs)
        self.resize(800, 600)

        layout = QVBoxLayout(self)
        self.myhwnd = int(self.winId())

        QTimer.singleShot(1000, self.buat)

    def buat(self):
        hwnd, chwnd = create_command_and_get_own_hwnd_and_last_child_hwnd('cmd')
        # hwnd, chwnd = create_command_and_get_own_hwnd_and_last_child_hwnd('cmd', hide=True)
        phwnd = 0

        # perlu hwnd dan phwnd
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        wrect = win32gui.GetWindowRect(hwnd)[:2] + win32gui.GetClientRect(hwnd)[2:]
        # print('[embed] save (hwnd, style, exstyle, wrect):', hwnd, style, exstyle, wrect)

        widget = QWidget.createWindowContainer(QWindow.fromWinId(hwnd))
        widget.hwnd = hwnd  # 窗口句柄
        widget.phwnd = phwnd  # 父窗口句柄
        widget.style = style  # 窗口样式
        widget.exstyle = exstyle  # 窗口额外样式
        widget.wrect = wrect  # 窗口位置
        self.layout().addWidget(widget)

        # jk belum keluar maka restore_window(hwnd)
        # restore_window(hwnd)
        # time.sleep(3.0)

        widget.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        win32gui.SetParent(hwnd, int(self.winId()))

        if chwnd:
            post_cmd_cpm(chwnd, 'repl')

    def restore(self):
        """归还窗口"""
        # 有bug，归还后窗口没有了WS_VISIBLE样式，不可见
        index_control_window = 0
        widget = self.layout().itemAt(index_control_window).widget()
        hwnd, phwnd, style, exstyle, wrect = widget.hwnd, widget.phwnd, widget.style, widget.exstyle, widget.wrect
        print('restore', hwnd, phwnd, style, exstyle, wrect)
        widget.close()
        self.layout().removeWidget(widget)  # 从布局中移出
        widget.deleteLater()

        win32gui.SetParent(hwnd, phwnd)  # 让它返回它的父窗口
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style | win32con.WS_VISIBLE)  # 恢复样式
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, exstyle)  # 恢复样式
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)  # 显示窗口
        win32gui.SetWindowPos(hwnd, 0, wrect[0], wrect[1], wrect[2], wrect[3], win32con.SWP_NOACTIVATE)


if __name__ == '__main__':
    import sys
    # import cgitb
    # cgitb.enable(format='text')

    app = QApplication(sys.argv)
    w = WindowEmbedder()
    w.show()
    sys.exit(app.exec_())

