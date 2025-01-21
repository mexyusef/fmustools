import sys, time
import win32api, win32con, win32gui


def to_top(hwnd):
    win32gui.BringWindowToTop(hwnd)


def set_topmost(hwnd, not_topmost=False):
    '''https://stackoverflow.com/questions/19425038/hide-window-from-ms-windows-taskbar
    https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
    root = Tk()
    root.wm_attributes("-topmost", 1)

    https://github.com/flashwave/topmostfriend
    https://github.com/Bluegrams/PinWin
    https://github.com/progrium/topframe

    '''
    try:
        if not_topmost:
            win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        else:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    except win32gui.error:
        print ("[s.g.s.s.windowshelper:set_topmost] Error while moving window to top")

# C:\Users\usef\work\sidoarjo\schnell\app\windowsutils.py
# def set_topmost(hwnd, reverse=False)
# win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
