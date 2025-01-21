import time
from uuid import uuid1
from schnell.app.printutils import pp

"""
tujuan:
command_prompt_data menggunakan versi redis
"""

from schnell.app.windowsutils import (
    make_process_std,
    is_visible as is_window_visible,
    get_hwnd_by_window_name,
    get_child_windows,
    
    # cmd_register_list as l,
    # get_cmd_register_list as getlist,
    # create_register_commandprompt as c,
    ketik as k,
    ketik as ketik_by_hwnd,
    ketik_by_index as ki,
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
)

# from schnell.app.appconfig import command_prompt_data
from schnell.app.redisutils import ConsoleData
command_prompt_data = ConsoleData()


def cmd_register_list():
    pp(command_prompt_data())

def get_cmd_register_list():
    return command_prompt_data
getlist = get_cmd_register_list


# def create_register_cmd(command=f'cmd /k start "{uuid1().hex}"', hide=False, desktop=None):
def create_register_cmd(command=f'cmd /k "title {uuid1().hex}"', identifier=None, hide=False, desktop=None):
    hprocess,hthread,pid,tid = make_process_std(command, hide=hide, desktop=desktop)
    index = len(command_prompt_data) + 1
    command_prompt_data[index] = {
        'cmd': command,
        'pid': pid,
        'tid': tid,
        'id': identifier,
        'hprocess': hprocess,
        'hthread': hthread,
    }
    return identifier


def fill_in_hwnds(tidur=0.5):
    # from schnell.app.appconfig import command_prompt_data
    for index, data in command_prompt_data.items():
        if 'hwnd' not in data:
            window_name = data['id']
            if window_name:
                # time.sleep(tidur)
                hwnd = get_hwnd_by_window_name(window_name)

            if hwnd != 0:
                command_prompt_data[index]['hwnd'] = hwnd
                child_hwnds = get_child_windows(hwnd)
                if child_hwnds:
                    command_prompt_data[index]['chwnd'] = child_hwnds[-1]
                    command_prompt_data[index]['chwnds'] = []
                    for chwnd in child_hwnds:
                        command_prompt_data[index]['chwnds'].append(chwnd)


def create_register_commandprompt():
    judul = uuid1().hex
    command=f'cmd /k "title {judul}"'
    identifier = create_register_cmd(command, identifier=judul)
    # step 2, tambahkan hwnd, biasanya gagal, mungkin perlu sleep cukup lama
    fill_in_hwnds()
    return identifier
c = create_register_commandprompt


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
    fill()
    return get_items_for_combo()

def hapus_set_combo_items():
    hapus_iterate_by_title()
    return get_items_for_combo()

def create_fill_set():
    _id = c()
    items = fill_set()

    l() # print

    # cek id ada
    index_or_none = get_command_prompt_data_index_from_uuidtitle(_id)
    if not index_or_none:
        # TODO: loop + sleep utk fill automatic
        print('ERR...please fill secara manual! karena masih kosong...')
    else:
        # cek hwnd sudah ada
        hwnd = get_hwnd_from_uuidtitle(_id)
        while not hwnd:
            fill_set()
            time.sleep(0.5)
            hwnd = get_hwnd_from_uuidtitle(_id)
    return items

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
