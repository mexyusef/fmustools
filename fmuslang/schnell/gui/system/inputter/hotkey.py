
import ctypes
from ctypes import CFUNCTYPE, c_int, POINTER, c_void_p, windll

import win32con
import timer



import time
from ctypes import *
import win32con, win32api, win32gui

class KeyboardHook_Old(object):
    """
    Written by: TwhK / Kheldar
    What do? Installs a global keyboard hook

    To install the hook, call the (gasp!) installHook() function.
    installHook() takes a pointer to the function that will be called
    after a keyboard event.  installHook() returns True if everything
    was successful, and False if it failed
    Note:  I've also provided a function to return a valid function pointer

    To make sure the hook is actually doing what you want, call the
    keepAlive() function
    Note:  keepAlive() doesn't return until kbHook is None, so it should
    be called from a separate thread

    To uninstall the hook, call uninstallHook()

    Note:  relies on modules provided by pywin32.
    http://sourceforge.net/projects/pywin32/
    """
    def __init__(self):
        self.user32     = windll.user32
        self.kernel32   = windll.kernel32
        self.kbHook     = None

    def installHook(self, pointer):
        """
        Traceback (most recent call last):
        File "C:/Users/usef/work/sidoarjo/schnell/gui/system/inputter/server.py", line 84, in run
            self.hotkey.start()
        File "C:/Users/usef/work/sidoarjo/schnell/gui/system/inputter/hotkey.py", line 151, in start
            if not self.keyboardHook.installHook(pointer):
        File "C:/Users/usef/work/sidoarjo/schnell/gui/system/inputter/hotkey.py", line 40, in installHook
            self.kbHook = self.user32.SetWindowsHookExA(
        ctypes.ArgumentError: argument 3: <class 'OverflowError'>: int too long to convert

        https://stackoverflow.com/questions/53732628/python-using-winapi-setwindowshookexa-on-windows-10
        """
        self.kbHook = self.user32.SetWindowsHookExA(
                              win32con.WH_KEYBOARD_LL,
                              pointer,
                              # win32api.GetModuleHandle(None),
                              self.kernel32.GetModuleHandleW(None),
                              0 # this specifies that the hook is pertinent to all threads
        )
        if not self.kbHook:
            return False
        return True

    def stop(self):
        self.uninstallHook()
        self.kbHook = None

    def keepAlive(self):
        if self.kbHook is None:
            return
        while self.kbHook is not None:
            win32gui.PumpWaitingMessages()
            #time.sleep(0.04)  # 25Hz
            time.sleep(0.001) # prevent delay when hold press

    def uninstallHook(self):
        if self.kbHook is None:
            return
        self.user32.UnhookWindowsHookEx(self.kbHook)
        self.kbHook = None

"""
https://stackoverflow.com/questions/53732628/python-using-winapi-setwindowshookexa-on-windows-10
"""

import win32con
import ctypes
from ctypes import *
from ctypes.wintypes import DWORD

user32 = windll.user32
kernel32 = windll.kernel32

class KBDLLHOOKSTRUCT(Structure): _fields_=[
    ('vkCode',DWORD),
    ('scanCode',DWORD),
    ('flags',DWORD),
    ('time',DWORD),
    ('dwExtraInfo',DWORD)]

HOOKPROC = WINFUNCTYPE(HRESULT, c_int, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM)

class KeyboardHook(object):
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None
    def installHookProc(self,pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(
            win32con.WH_KEYBOARD_LL,
            pointer,
            kernel32.GetModuleHandleW(None),
            0
        )
        if not self.hooked:
            return False
        return True
    def uninstalHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

def hookProc(nCode, wParam, lParam):
    if user32.GetKeyState(win32con.VK_CONTROL) & 0x8000:
        print("\nCtrl pressed, call uninstallHook()")
        KeyLogger.uninstalHookProc()
        return 0
    if nCode == win32con.HC_ACTION and wParam == win32con.WM_KEYDOWN:
        kb = KBDLLHOOKSTRUCT.from_address(lParam)
        user32.GetKeyState(win32con.VK_SHIFT)
        user32.GetKeyState(win32con.VK_MENU)
        state = (ctypes.c_char * 256)()
        user32.GetKeyboardState(byref(state))
        str = create_unicode_buffer(8)
        n = user32.ToUnicode(kb.vkCode, kb.scanCode, state, str, 8 - 1, 0)
        if n > 0:
            if kb.vkCode == win32con.VK_RETURN:
                print()
            else:
                print(ctypes.wstring_at(str), end = "", flush = True)
    return user32.CallNextHookEx(KeyLogger.hooked, nCode, wParam, lParam)

if __name__ == '__main__':
    KeyLogger = KeyboardHook()
    pointer = HOOKPROC(hookProc)
    KeyLogger.installHookProc(pointer)
    print("Hook installed")
    msg = ctypes.wintypes.MSG()
    user32.GetMessageA(byref(msg), 0, 0, 0) #wait for messages
##################################################
# returns a function pointer to the fn paramater #
# assumes the function takes three params:       #
# c_int, c_int, and POINTER(c_void_p)            #
##################################################
def getFunctionPointer(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)


modifiers = [
    ('control', 1 << 1, 0x11),
    ('win', 1 << 3, 0x5b),
    ('alt', 1 << 0, 0x12),
    ('shift', 1 << 2, 0x10)
]


def mods():
    windll.user32.GetKeyState(0)  # flush
    keyState = (ctypes.c_uint8 * 256)()  # Array of c_long
    windll.user32.GetKeyboardState(ctypes.byref(keyState))
    ms = []
    for mod in modifiers:
        if keyState[mod[2]] & 1 << 7:
            ms.append(mod[0])
        keyState[mod[2]] = 0
    return ms


class Hotkey(object):

    def __init__(self, fire):
        self.fire = fire
        self.presscount = 0
        self.delay = 300
        self.timer_id = None

        import win32com.client
        self.shell = win32com.client.Dispatch("WScript.Shell")

        self.keyboardHook = KeyboardHook()
        self.pending = False

    def go(self):
        if self.timer_id is not None:
            timer.kill_timer(self.timer_id)
            self.timer_id = None
        if self.presscount >= 2:
            self.presscount = 0
            self.fire()
        else:
            x = self.presscount
            if x > 0:
                self.presscount = 0
                self.pending = True
                try:
                    self.shell.SendKeys(';' * x)
                finally:
                    self.pending = False

    def timer_fn(self, id, time):
        self.go()

    def kbEvent(self, nCode, wParam, lParam):
        if nCode >= 0:
            # It just occured to me that I should aso be checking for WM_SYSKEYDOWN as well
            if wParam is win32con.WM_KEYDOWN:
                if not self.pending and lParam[0] == 0xBA and not mods():
                    if self.presscount >= 0:
                        if self.timer_id is None:
                            self.timer_id = timer.set_timer(self.delay, self.timer_fn)
                    self.presscount += 1
                    if self.presscount > 0:
                        # return a non-zero to prevent further processing
                        return 42
                else:
                    self.go()
        return windll.user32.CallNextHookEx(self.keyboardHook.kbHook, nCode, wParam, lParam)

    def start(self):
        pointer = getFunctionPointer(self.kbEvent)
        if not self.keyboardHook.installHook(pointer):
            raise RuntimeError('Install keyboard hook failed.')
        self.keyboardHook.keepAlive()

    def stop(self):
        self.keyboardHook.stop()
