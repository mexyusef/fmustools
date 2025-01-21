import pyautogui
import pyautogui as P
pyautogui.FAILSAFE = False
from rich.pretty import pprint


# import os, sys
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([sidoarjodir, schnelldir])
import sys
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent.parent)
#                              file     app     sch   sid
sys.path.append(sidoarjodir)

from schnell.app.appconfig import programming_data
from schnell.app.greputils import pattern_search_list, pattern_search_list_keep_case
from schnell.app.printutils import indah4, print_list_warna
# from schnell.app.promptutils import combobox_listbox

# def alert(header,body,button='OK'):
#     P.alert(body,header,button)


def alert(body, header='(UNTITLED)'):
    P.alert(body, header)


def confirm(body):
    P.confirm(body)


def prompt(body):
    return P.prompt(body)


def password(body):
    return P.password(body)


def top_bringto(wnd):
    pass


def top_most(wnd):
    pass


def minimize_current_window():
    pyautogui.hotkey('winleft', 'down')


def maximize_current_window():
    pyautogui.hotkey('winleft', 'up')


def minimize_all_windows():
    pyautogui.hotkey('winleft', 'home')


def minimize_all_windows_except_current():
    pyautogui.hotkey('winleft', 'm')


def restore_all_minimized_windows():
    pyautogui.hotkey('winleft', 'shift', 'm')


def show_desktop():
    pyautogui.hotkey('winleft', 'd')

# https://stackoverflow.com/questions/43785927/python-pyautogui-window-handle
# pyautogui.getWindowsWithTitle("Stack Overflow")[0].maximize()
# pyautogui.getWindowsWithTitle("Stack Overflow")[0].minimize()
# pyautogui.getWindowsWithTitle("Stack Overflow")[0].activate()
# https://automatetheboringstuff.com/2e/chapter20/
def get_window_by_title(title):
    return pyautogui.getWindowsWithTitle(title)[0]


def type_by_window_title(title, ketik_list):
    try:
        wnd = get_window_by_title(title)
    except Exception as err:
        # wnd = choose_window_title(lambda: print(f'Handled {err}', False))
        wnd = activewindow()
    if wnd:
        wnd.activate()
        pyautogui.hotkey(*ketik_list)


docs = """https://automatetheboringstuff.com/2e/chapter20/

moveTo(x, y)
    Moves the mouse cursor to the given x and y coordinates.

move(xOffset, yOffset)
    Moves the mouse cursor relative to its current position.

dragTo(x, y)
    Moves the mouse cursor while the left button is held down.

drag(xOffset, yOffset)
    Moves the mouse cursor relative to its current position while the left button is held down.

click(x, y, button)
    Simulates a click (left button by default).

rightClick()
    Simulates a right-button click.

middleClick()
    Simulates a middle-button click.

doubleClick()
    Simulates a double left-button click.

mouseDown(x, y, button)
    Simulates pressing down the given button at the position x, y.

mouseUp(x, y, button)
    Simulates releasing the given button at the position x, y.

scroll(units)
    Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.

write(message)
    Types the characters in the given message string.

write([key1, key2, key3])
    Types the given keyboard key strings.

press(key)
    Presses the given keyboard key string.

keyDown(key)
    Simulates pressing down the given keyboard key.

keyUp(key)
    Simulates releasing the given keyboard key.

hotkey([key1, key2, key3])
    Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.

screenshot()
    Returns a screenshot as an Image object. (See Chapter 19 for information on Image objects.)

getActiveWindow(), getAllWindows(), getWindowsAt(), and getWindowsWithTitle()
    These functions return Window objects that can resize and reposition application windows on the desktop.

getAllTitles()
    Returns a list of strings of the title bar text of every window on the desktop.
"""


def setinggi(tinggi):
    """
    tinggi: 0.1, 0.2, ..., 0.9 dari h
    x gerak dari 100 ke 600 ke 100
    """
    w,h = P.size()
    x1 = (w*0.1*100)//100
    x2 = (w*0.9*100)//100
    P.moveTo(x1, (h*tinggi*100)//100, 1.0)
    P.moveTo(x2, (h*tinggi*100)//100, 2.0)
    P.moveTo(x1, (h*tinggi*100)//100, 2.0)


def wh():
    w,h = P.size()  # Size(), .w,.h
    return (w,h)


def mouse():
    x,y = P.position()  # Point(), .x,.y
    return (x,y)


def clickcenter(wnd):
    x = wnd.left + wnd.width//2
    y = wnd.top + wnd.height//2
    P.click(x,y)


def click14(wnd):
    x = wnd.left + wnd.width//4
    y = wnd.top + wnd.height//2
    P.click(x,y)


def click34(wnd):
    x = wnd.left + wnd.width*3//4
    y = wnd.top + wnd.height//2
    P.click(x,y)


def click14v(wnd):
    x = wnd.left + wnd.width//2
    y = wnd.top + wnd.height//4
    P.click(x,y)


def click34v(wnd):
    x = wnd.left + wnd.width//2
    y = wnd.top + wnd.height*3//4
    P.click(x,y)


def drag(dx,dy,dur=0.2,abs=True):
    if abs:
        P.dragTo(dx,dy,dur)
    else:
        P.drag(dx,dy,dur)


def move(x,y,dur=0.2,abs=True):
    if abs:
        P.moveTo(x,y,dur)
    else:
        P.move(x,y,dur)


def skroll(h, x, y):
    P.scroll(h, x, y)


def scroll(h):
    P.scroll(h)


def mouseinfo():
    P.mouseInfo()


def click(x,y):
    P.click(x,y)


def doubleclick():
    P.doubleClick()


def klikkanan():
    P.rightClick()


def klik(delay=0):
    if delay:
        P.sleep(delay)
    P.click()


def dragrel(dx=0, dy=0, duration=1):
    P.dragRel(dx, dy, duration=duration)


def dragrels(xylist=[], duration=1):
    """
    >>> eval('[(1,2),(3,4),(5,6)]')
    [(1, 2), (3, 4), (5, 6)]
    """
    for (x,y) in xylist:
        dragrel(x, y, duration=duration)


def dragtos(xylist=[], duration=1):
    for (x,y) in xylist:
        P.dragTo(x, y, duration=duration)


def dragto_from(x2=1700, duration=1):
    """
    mouse sama
    """
    x,y = mouse()
    P.dragTo(x2, y, duration=duration)
    return x,y


def dragto_from_and_scroll(amount=1000, x2=1700, duration=1):
    x,y = dragto_from(x2, duration)
    P.scroll(amount, x2, y)


def dragto_from_and_scroll_copy_switch(amount=1000, x2=1750, duration=1, delay=0.3):
    from schnell.app.clipboardutils import trypaste
    x,y = dragto_from(x2, duration)
    P.scroll(amount, x2, y)
    P.sleep(delay)
    P.hotkey('ctrl', 'c')
    P.alert(text=trypaste(), title='Finished Scrolling & Ctrl+C')
    P.hotkey('alt', 'tab')


def gpt_op1(tinggi=1/4):
    """
    cara pake:
    click:(judul)100,100\gpt:
    """
    w,h = P.size()
    P.click(600, (h*tinggi*100)//100)
    dragto_from_and_scroll_copy_switch()


def ss(filepath):
    im = P.screenshot()
    im.save(filepath)


def activewindow():
    wnd = P.getActiveWindow()
    print(f"""bisa set dg attribute berikut (misal .width dan .topleft):
    title = {wnd.title}
    size = {wnd.size}
    coords LTRB = {wnd.left, wnd.top, wnd.right, wnd.bottom}
    coords TL = {wnd.topleft}
    area = {wnd.area}
    L+10 T+20 (utk click) = {wnd.left+10, wnd.top+20}
    width = {wnd.width}
    isMaximized = {wnd.isMaximized}
    isMinimized = {wnd.isMinimized}
    isActive = {wnd.isActive}
    """)
    return wnd


def minactive():
    w = activewindow()
    w.minimize()


def maxactive():
    w = activewindow()
    w.maximize()


def allwindows():
    return P.getAllWindows()


def windowat(x,y):
    return P.getWindowsAt(x,y)


def windowstitled(title):
    return P.getWindowsWithTitle(title)


def windowtitles():
    # if lower:
    #     return [i.lower() for i in P.getAllTitles() if i.strip()]
    return [i for i in P.getAllTitles() if i.strip()]


def inwindowtitles(title):
    semua = [i.lower() for i in windowtitles()]
    # ketemu_title = [i for i in semua if title.lower() in i]
    ketemu_title = pattern_search_list(semua, title, aslist=True)
    indah4(f"""autoutils:inwindowtitles
        cari '{title}'
        dalam {semua}
        => {ketemu_title}
    """, warna='blue')
    if ketemu_title:
        return True, ketemu_title
    return False, None


def activate_wnd(wnd):
    try:
        wnd.activate()
    except:
        wnd.minimize()
        wnd.restore()


def title_to_wnd(title):
    wnds = P.getWindowsWithTitle(title)
    if wnds and len(wnds)==1:
        wnd = wnds[0]
        return wnd
    return None


def index_to_wnd(index):
    title = ''
    titles = [item for item in P.getAllTitles() if item.strip()]
    if titles:
        title = titles[index]
    if title:
        return title_to_wnd(title)
    return None


def activate_wnd(wnd, restore_minmax=False):
    try:
        wnd.activate()
    except:
        wnd.minimize()
        if restore_minmax:
            wnd.maximize()
        else:
            wnd.restore()


def activate_wnd_by_index(index):
    wnd = index_to_wnd(index)
    if wnd:
        activate_wnd(wnd)
    return wnd


def activate_wnd_by_title(title):
    wnd = title_to_wnd(title)
    if wnd:
        activate_wnd(wnd)
    return wnd


def get_inwindowtitles(title, choose_shortest_for_multiple_windows=False):
    """
    click(660,920)
    """
    print(f"[autoutils:get_inwindowtitles]1 /first/ => inwindowtitles(title) = {inwindowtitles(title)}")
    found, foundlist = inwindowtitles(title)
    if found:
        # judul = [i for i in P.getAllTitles() if i.strip() and title.lower() in i.lower()]
        judul = foundlist
        print(f"[autoutils:get_inwindowtitles]2 /second/ => judul = {judul}")
        if judul and len(judul)==1:
            cari_judul = judul[0]
            print(f"[autoutils:get_inwindowtitles]3 /if block, third-last/ => cari_judul {cari_judul}")
            hasil_cari_judul = P.getWindowsWithTitle(cari_judul)
            wnds = hasil_cari_judul
            print(f"[autoutils:get_inwindowtitles]4 /second-last/ => wnds {wnds}")
            if wnds and len(wnds)==1:
                wnd = wnds[0]
                print(f"[autoutils:get_inwindowtitles]5 /last/ => found {wnd}")
                # last_index = [i for i in P.getAllTitles() if i.strip()].index(cari_judul)
                last_index = pattern_search_list_keep_case(P.getAllTitles(), cari_judul, send_indices=True)
                # print('before sending:', selected, 'input:', all_lines, 'code:', code)
                # before sending: [9]
                # input: ['', '', '', '', '', '', '', 'WORK - repl', 'C:\\Users\\usef\\work\\sidoarjo\\schnell\\app\\greputils.py - sidoarjo - Visual Studio Code', 'ini judul baru', 'FM', 'Settings', 'Settings', 'Windows Input Experience', '', '', '', '', '', '', '', 'AvaloniaEdit', 'Total Commander (x64) 10.00 - NOT REGISTERED', 'Lara', 'Jan Blachowicz vs Luke Rockhold | FREE FIGHT | UFC 291 - YouTube — Mozilla Firefox', '', '', 'Program Manager'] 
                # code: ['ini', 'judul', 'baru']
                indah4('*'*20 + ' </autoutils:get_inwindowtitles>', warna='red')
                return wnd, last_index
        elif len(judul)>1:
            print(f"[autoutils:get_inwindowtitles]6 /else block/ => multiple windows")
            print_list_warna(judul, start=1)
            # get the shortest
            if choose_shortest_for_multiple_windows:
                cari_judul = sorted(judul, key=len)[0]
            else:
                from .promptutils import combobox_listbox
                masuk = combobox_listbox(judul)
                # masuk = input('Enter choice: ').strip()
                # while not masuk:
                #     masuk = input('Enter choice: ').strip()
                masuk = int(masuk)
                if 1<=masuk<=len(judul):
                    cari_judul = judul[masuk-1]
            if cari_judul:
                print(f"[autoutils:get_inwindowtitles]7 /third-last/\n=> cari_judul: {cari_judul}")
                hasil_cari_judul = P.getWindowsWithTitle(cari_judul)
                wnds = hasil_cari_judul
                print(f"[autoutils:get_inwindowtitles]8 /second-last/ => wnds {wnds}")
                if wnds and len(wnds)==1:
                    '''
                    <Win32Window 
                    left="-9", 
                    top="-9", 
                    width="1938", 
                    height="1038", 
                    title="The Rise of ChatGPT and the Fall of the Software Developer — Is This the Beginning of the End? | by Fernando Doglio | Geek Culture | Dec, 2022 | Medium — Mozilla Firefox Private Browsing">                    
                    'the rise of chatgpt and the fall of the software developer — is this the beginning of the end? | by fernando doglio | geek culture | dec, 2022 | medium — mozilla firefox private browsing' is not in list                    
                    '''
                    wnd = wnds[0]
                    indah4(f"[autoutils:get_inwindowtitles]9 /last/\n=> found wnd: {wnd}", warna='green')
                    # last_index = [i for i in P.getAllTitles() if i.strip()].index(cari_judul)
                    last_index = [i for i in P.getAllTitles() if i.strip()].index(wnd.title)
                    indah4('*'*20 + ' </autoutils:get_inwindowtitles>', warna='red')
                    return wnd, last_index
    print(f"[autoutils:get_inwindowtitles]10 /ultimate-last/ get None utk title {title} in {P.getAllTitles()}.")
    indah4('*'*20 + ' </autoutils:get_inwindowtitles>', warna='red')
    return None, None


def ismax(w):
    return w.isMaximized


def ismin(w):
    return w.isMinimized


def maxwnd(w):
    return w.maximize()


def minwnd(w):
    return w.minimize()


def reswnd(w):
    return w.restore()


def closewnd(w):
    return w.close()


def actwnd(w):
    return w.activate()


def clickwrite(x,y,msg):
    P.click(x,y)
    P.write(msg)


def mdown(x,y):
    P.mouseDown(x,y)


def mup(x,y):
    P.mouseUp(x,y)


def kdown(control):
    P.keyDown(control)


def kup(control):
    P.keyUp(control)


def dragwindow(wnd,x,y,l=100,t=10,dur=0.2):
    mdown(wnd.left+l, wnd.top+t)
    # drag(x,y,dur=dur)
    P.drag(x,y,duration=dur)
    P.mouseUp()


def dragtowindow(wnd,x,y,l=100,t=10,dur=0.2):
    mdown(wnd.left+l, wnd.top+t)
    # drag(x,y,dur=dur,abs=True)
    P.dragTo(x,y,duration=dur)
    P.mouseUp()


def movewindow(wnd,x,y,l=100,t=10,dur=0.2):
    # print('mouse down:', wnd.left+l, wnd.top+t)
    # activewindow()
    mdown(wnd.left+l, wnd.top+t)
    # click(wnd.left+l, wnd.top+t)
    # P.click()
    move(x,y,dur=dur)
    P.mouseUp()


def movetowindow(wnd,x,y,l=100,t=10,dur=0.2):
    # mdown(wnd.left+l, wnd.top+t)
    P.moveTo(wnd.left+l, wnd.top+t)
    P.mouseDown(button='left')
    # click(wnd.left+l, wnd.top+t)
    # P.click()
    # move(x,y,dur=dur,abs=True)
    P.moveTo(x,y,duration=dur)
    P.mouseUp()


def down_press_up(control, key):
    P.keyDown(control)
    P.press(key)
    P.keyUp(control)


def press(control='enter'):
    P.press(control)


def hotkey(keylist):
    P.hotkey(*keylist)


def sleep(dur):
    P.sleep(dur)


def count(counter,msg=''):
    if msg:
        print(msg, end='')
    P.countdown(counter)


def halfwidth(wnd):
    setengah = P.size().width // 2
    wnd.width = setengah
    # pastikan wnd dalam screen
    if wnd.left > setengah:
        wnd.left = setengah
    elif wnd.left < 5:
        wnd.left = 5


def halfheight(wnd, offset=-55):
    setengah = P.size().height // 2
    wnd.height = setengah + offset
    # pastikan wnd dalam screen
    if wnd.top > setengah:
        wnd.top = setengah + offset
    elif wnd.top < 5:
        wnd.top = 5


def halves(wnd):
    halfwidth(wnd)
    halfheight(wnd)


def fullwidth(wnd):
    wnd.width = P.size().width
    wnd.left = 5


# def fullheight(wnd, offset=programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]):
#     print('fullheight config:', programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"])
#     wnd.height = P.size().height + offset
def fullheight(wnd, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    print('fullheight config:', programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"])
    wnd.height = P.size().height + offset
    wnd.top = 5


def centerhorizontal(wnd):
    """
    w, h tetap hanya saja left berubah
    """
    wnd.left = (P.size().width//2) - (wnd.width//2)


def centervertical(wnd):
    """
    w, h tetap hanya saja top berubah
    """
    wnd.top = (P.size().height//2) - (wnd.height//2)


def centerhalf(wnd):
    """
    """
    wnd.left = P.size().width//4
    wnd.top = P.size().height//4
    halves(wnd)


def tengah(wnd, faktor=8):
    """
    faktor=8 = 80%
    faktor=7.5 = 75%
    """
    wnd.left = (P.size().width*(10-faktor)//10)//2
    wnd.top = (P.size().height*(10-faktor)//10)//2
    wnd.width = P.size().width*faktor//10
    wnd.height = P.size().height*faktor//10


def kanan(wnd):
    """
    """
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = P.size().width//2
    wnd.top = 5
    halfwidth(wnd)
    fullheight(wnd)


def kiri(wnd):
    """
    """
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = 5
    halfwidth(wnd)
    fullheight(wnd)


def atas(wnd):
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = 5
    fullwidth(wnd)
    halfheight(wnd)


def bawah(wnd):
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = P.size().height//2
    fullwidth(wnd)
    halfheight(wnd)


def touch_top(wnd):
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.top = 5


def touch_bottom(wnd, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.bottom = P.size().height - 5
    wnd.height = P.size().height + offset


def touch_left(wnd):
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5


def touch_right(wnd):
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.right = P.size().width - 5


def pojok1(wnd):
    """
    1,2,3,4 = top-left, top-right, bottom-right, bottom-left
    """
    wnd.left = 5
    wnd.top = 5
    wnd.width = P.size().width // 2
    wnd.height = P.size().height // 2


def pojok2(wnd):
    """
    1,2,3,4 = top-left, top-right, bottom-right, bottom-left
    """
    wnd.left = P.size().width // 2
    wnd.top = 5
    wnd.width = P.size().width // 2
    wnd.height = P.size().height // 2


def pojok3(wnd, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    wnd.left = P.size().width // 2
    wnd.top = P.size().height // 2
    wnd.width = P.size().width // 2
    wnd.height = P.size().height // 2 + offset


def pojok4(wnd, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    wnd.left = 5
    wnd.top = P.size().height // 2
    wnd.width = P.size().width // 2
    wnd.height = P.size().height // 2 + offset


def q1(wnd, factor=5):
    # top left
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = 5
    wnd.width = P.size().width * factor // 10
    wnd.height = P.size().height * factor // 10


def q2(wnd, factor=5):
    # top right
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = P.size().width * (10-factor)//10
    wnd.top = 5
    wnd.width = P.size().width * factor // 10
    wnd.height = P.size().height * factor // 10


def q3(wnd, factor=5, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = P.size().width * (10-factor)//10
    wnd.top = P.size().height * (10-factor)//10
    wnd.width = P.size().width * factor // 10
    wnd.height = P.size().height * factor // 10 + offset


def q4(wnd, factor=5, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = P.size().height * (10-factor)//10
    wnd.width = P.size().width * factor // 10
    wnd.height = P.size().height * factor // 10 + offset

# right adlh kanan dg factor
def right_pane(wnd, factor=7.5, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    # di sini kita kasih fullheight krn right dan left itu kan geser horizontal
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = P.size().width*(10-factor)//10
    wnd.top = 5
    wnd.width = P.size().width*factor//10
    wnd.height = P.size().height + offset

# left adlh kiri dg factor
def left_pane(wnd, factor=7.5, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    # di sini kita kasih fullheight krn right dan left itu kan geser horizontal
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = 5
    # wnd.right = P.size().width*(10-factor)//10
    wnd.width = P.size().width*factor//10
    wnd.height = P.size().height + offset

# top adlh atas dg factor
def top_pane(wnd, factor=7.5, offset=None):
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = 5
    wnd.width = P.size().width
    wnd.height = P.size().height*factor//10 + offset

# bottom adlh bawah dg factor
# perlu offset, krn bottom margin selalu kemakan taskbar
def bottom_pane(wnd, factor=7.5, offset=None):
    # normalize jk masukkan 0<factor<1 dan 0<factor<100
    if factor<1.0:
        factor *= 10.0
    elif factor>10:
        factor /= 10.0
    elif factor<0:
        factor = 0
    if offset is None:
        offset = programming_data['j']["schnell"]["app"]["autoutils"]["fullheight/offset"]
    if wnd.isMaximized or wnd.isMinimized:
        wnd.restore()
    wnd.left = 5
    wnd.top = P.size().height*(10-factor)//10
    wnd.width = P.size().width
    wnd.height = P.size().height*factor//10 + offset


def resize_op_internal(wnd, digit, operation, codes):
    # digit hrs sudah int
    digit = -1*digit if operation=='-' else digit
    w = wnd.width
    h = wnd.height
    for code in codes:
        if code=='l':
            # wnd.left += digit
            # namanya resize, jk kiri ditambah +digit
            # maka w yg bertambah (+), l justeru bertambah (-)
            # krn "left membesar" itu kekiri atau (-) secara coordinate
            wnd.left -= digit
            wnd.width = w + digit
        elif code =='t':
            # wnd.top += digit
            # namanya resize, jk atas ditambah +digit
            # maka h yg bertambah (+), t justeru bertambah (-)
            # krn "top membesar" itu ke atas atau (-) secara coordinate
            wnd.top -= digit
            wnd.height = h + digit
        elif code == 'r':
            wnd.right += digit
            wnd.width = w + digit
        elif code == 'b':
            wnd.bottom += digit
            wnd.height = h + digit


def move_op_internal(wnd, digit, operation, codes):
    digit = -1*digit if operation=='-' else digit
    w = wnd.width
    h = wnd.height
    for code in codes:
        if code=='l':
            wnd.left += digit
            wnd.width = w
        elif code =='t':
            wnd.top += digit
            wnd.height = h
        elif code == 'r':
            wnd.right += digit
            wnd.width = w
        elif code == 'b':
            wnd.bottom += digit
            wnd.height = h


def non_empty_all_titles():
    return [item for item in P.getAllTitles() if item.strip()]


def list_visible_window_titles():
    """
    pilih = input('Choose: ')
    pilih = int(pilih)
    if 1 <= pilih <= len(allwnds):
        t = allwnds[pilih-1]
    else:
        import sys
        print('keluar')
        sys.exit(0)

    wnds = P.getWindowsWithTitle(t)
    print('Choosing:', wnds)
    if len(wnds)==1:
        wnd = wnds[0]
        try:
            wnd.activate()
        except:
            wnd.minimize()
            # wnd.maximize()
            wnd.restore()
    """
    allwnds = non_empty_all_titles()
    pprint([f"{i+1}. {e}" for i, e in enumerate(allwnds)])
    return allwnds


window_history = {
    'last_index': -1,
    'last_title': '',
}


def index_window(idx):
    title = non_empty_all_titles() [idx-1]
    hasil_cari_judul = P.getWindowsWithTitle(title)
    wnds = hasil_cari_judul
    if wnds:
        if len(wnds)==1:
            wnd = wnds[0]
            return wnd, title
        else:
            print('Double windows:', wnd, 'returning None for wnd.')
            return None, title
    return None, None


def choose_window_title(callback, restore_minmax=True):
    from .promptutils import combobox_listbox
    allwnds = non_empty_all_titles()
    # pprint([f"{i+1}. {e}" for i, e in enumerate(allwnds)])
    # t = ''
    pilihan_wnds = [f"{i+1}. {e}" for i, e in enumerate(allwnds)]
    try:
        pilih = combobox_listbox(pilihan_wnds, title='[choose_window_title] Tekan angka untuk memilih window')
    except Exception as err:
        print(f"""[choose_window_title] exception => pilih = combobox_listbox, exc = {err}""")
        pilih = input('[choose_window_title] Due to exception => Choose: ')
    if not pilih:
        return
    pilih = int(pilih)
    if 1 <= pilih <= len(allwnds):
        t = allwnds[pilih-1]
    else:
        return
        # import sys
        # print('keluar')
        # sys.exit(0)

    wnd = None
    wnds = P.getWindowsWithTitle(t)
    print('[choose_window_title] Choosing:', wnds)
    if len(wnds)==1:
        wnd = wnds[0]
        try:
            wnd.activate()
        except:
            wnd.minimize()
            if restore_minmax:
                wnd.maximize()
            else:
                wnd.restore()
        window_history['last_index'] = pilih
        window_history['last_title'] = t
        callback()
    else:
        print('[choose_window_title] Double windows:', wnds)
    return wnd


DEFAULT_ALERT_TITLE = 'DEFAULT_ALERT_TITLE'
TYPING_INTERVAL_DEFAULT = 0.00  # biar langsung ceplok
NEWLINE_INTERVAL_DEFAULT = 0.01
current_typing_interval = TYPING_INTERVAL_DEFAULT
current_newline_interval = NEWLINE_INTERVAL_DEFAULT


def normal_type(line, current_typing_interval=TYPING_INTERVAL_DEFAULT, current_newline_interval=0.05):
    P.write(line, current_typing_interval)
    P.write('\n', current_newline_interval)


# '__BKSPC__' in line:
def type_with_backspace(line, current_typing_interval=TYPING_INTERVAL_DEFAULT, current_newline_interval=0.05):
    lines = line.split('__BKSPC__')
    for baris in lines:
        if baris:
            normal_type(baris, current_typing_interval)
        P.write(['backspace'], current_newline_interval)


sample_pandas_code = """
import numpy as np
__SLEEP__=1.0
import pandas as pd
__SLEEP__=1.0
__INTERVAL__=0.0
__NEWLINE_INTERVAL__=0.01

# ini paling penting spt nya
df2 = pd.DataFrame({"X": ["B", "B", "A", "A"], "Y": [1, 2, 3, 4]})
__SLEEP__=0.3
df2
__ALERT__=are you ready to go?=This is the content that needs to be displayed
# jk kita group berdasar kolom X, kita tau X gak all unique
df2.groupby(["X"]).sum()
__ALERT__=Kalau ini hanya body saja...tanpa title
# ini akan sama dg atas, tapi gak diurut A dan B nya
df2.groupby(["X"], sort=False).sum()

df3 = pd.DataFrame({"X": ["A", "B", "A", "B"], "Y": [1, 4, 3, 2]})
__SLEEP__=0.3
df3
df3.groupby(["X"]).get_group("A")
df3.groupby(["X"]).get_group("B")


df = pd.DataFrame(
[
("bird", "Falconiformes", 389.0),
("bird", "Psittaciformes", 24.0),
("mammal", "Carnivora", 80.2),
("mammal", "Primates", np.nan),
("mammal", "Carnivora", 58),
],
index=["falcon", "parrot", "lion", "monkey", "leopard"],
columns=("class", "order", "max_speed"),
)
__INTERVAL__=DEFAULT
__NEWLINE_INTERVAL__=DEFAULT
df

grouped = df.groupby("class")
__SLEEP__=0.2
grouped.sum()
grouped = df.groupby("order", axis="columns")
__SLEEP__=0.2
grouped
grouped = df.groupby(["class", "order"])
__SLEEP__=0.2
grouped.sum()



df = pd.DataFrame(
{
"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
"B": ["one", "one", "two", "three", "two", "two", "one", "three"],
"C": np.random.randn(8),
"D": np.random.randn(8),
}
)

df

grouped = df.groupby("A")
__SLEEP__=0.2
grouped.sum()

grouped = df.groupby(["A", "B"])
__SLEEP__=0.2
grouped.sum()

df2 = df.set_index(["A", "B"])

grouped = df2.groupby(level=df2.index.names.difference(["B"]))
__SLEEP__=0.2
grouped.sum()

def get_letter_type(letter):
if letter.lower() in 'aeiou':
return 'vowel'
__BKSPC__else:
\treturn 'consonant'

grouped = df.groupby(get_letter_type, axis=1)
__SLEEP__=0.2
grouped.sum()


lst = [1, 2, 3, 1, 2, 3]
s = pd.Series([1, 2, 3, 10, 20, 30], lst)
grouped = s.groupby(level=0)
__SLEEP__=0.2
grouped.first()
grouped.last()
grouped.sum()
"""


def gugu_type(pesan, current_typing_interval=TYPING_INTERVAL_DEFAULT, current_newline_interval=NEWLINE_INTERVAL_DEFAULT):
    r"""
    sample code
    sptnya ini digunakan utk qtconsole (jup.bat namafile.py)
    C:\tmp>cat \work\bin\jup.bat
    @echo off
    python C:\Users\usef\work\sidoarjo\schnell\jup.py %*
    """
    # global current_typing_interval, current_newline_interval
    pesan = pesan.replace('\\t', '\t').replace('\\n', '\n')

    for line in pesan.splitlines():

        if line.startswith('__SLEEP__'):
            detik=3.0
            if '=' in line:
                _, detik = line.split('=')
                detik = float(detik)
            P.sleep(detik)
        elif line.startswith('__ALERT__'):
            kode_title_body = line.split('=') # __ALERT__=header=body
            title = DEFAULT_ALERT_TITLE
            if len(kode_title_body)==2:
                _, body = kode_title_body
            elif len(kode_title_body)==3:
                _, title, body = kode_title_body
            P.alert(text=body, title=title, button='OK')
        elif line.startswith('__INTERVAL__'):
            _, interval = line.split('=')
            if interval == 'DEFAULT':
                current_typing_interval = TYPING_INTERVAL_DEFAULT
            else:
                current_typing_interval = float(interval)
        elif line.startswith('__NEWLINE_INTERVAL__'):
            _, interval = line.split('=')
            if interval == 'DEFAULT':
                current_newline_interval = NEWLINE_INTERVAL_DEFAULT
            else:
                current_newline_interval = float(interval)
        elif '__BKSPC__' in line:
            type_with_backspace(line, current_typing_interval)
        else:
            # P.write(line, current_typing_interval)
            P.write(line)
            P.write('\n', current_newline_interval)
