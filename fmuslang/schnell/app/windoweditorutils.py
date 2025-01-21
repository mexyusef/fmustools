from uuid import uuid1
import time
from .printutils import indah4
from .windowsutils import create_register_cmd, fill_in_hwnds, get_command_prompt_data_index_from_uuidtitle, get_hwnd_from_uuidtitle
from .wcmderutils import fill_set
from schnell.app.appconfig import command_prompt_data, command_prompt_data_extension, programming_data

# C:\work\kenza\zpt\AvaloniaEdit\src\AvaloniaEdit.Demo\bin\Debug\net6.0\AvaloniaEdit.Demo.exe --title "our history" --filepath c:\work\tmp\ulibpy.hist
AVALON_EDITOR=programming_data['j']['editors']['AVALON']
JUP_EDITOR=programming_data['j']['editors']['JUP']
NOTEPAD_EDITOR=programming_data['j']['editors']['NOTEPAD']
ALT_EDITOR=programming_data['j']['editors']['ALT']
PLAIN_EDITOR=programming_data['j']['editors']['PLAIN']
PAD_EDITOR=programming_data['j']['editors']['PAD']
YNOTE_EDITOR=programming_data['j']['editors']['YNOTE']
RSED_EDITOR=programming_data['j']['editors']['RSED']
RSNONE_EDITOR=programming_data['j']['editors']['RSNONE']
GOED_EDITOR=programming_data['j']['editors']['GOED']
GOMD_EDITOR=programming_data['j']['editors']['GOMD']
GOIDE_EDITOR=programming_data['j']['editors']['GOIDE']

ACCEPTABLE_EDITORS = ['avalon', 'jup', 'np', 'notepad', 'alt', 'plain', 'pad', 'ynote', 'rsed', 'rsnone', 'goed', 'gomd', 'goide']
editors_map = dict(zip(ACCEPTABLE_EDITORS, [
    AVALON_EDITOR, # no use
    JUP_EDITOR, # no use
    NOTEPAD_EDITOR, # no use
    NOTEPAD_EDITOR, # no use
    ALT_EDITOR,
    PLAIN_EDITOR,
    PAD_EDITOR,
    YNOTE_EDITOR,
    RSED_EDITOR,
    RSNONE_EDITOR,
    GOED_EDITOR,
    GOMD_EDITOR,
    GOIDE_EDITOR,
]))

def create_register_editor(editor='avalon', CURDIR=None):
    judul = uuid1().hex
    if not editor in ACCEPTABLE_EDITORS:
        return None
    if editor=='avalon':
        command=f'{AVALON_EDITOR} --title "{judul}"'
    elif editor=='jup':
        command=f'{JUP_EDITOR} --title "{judul}"'
    elif editor in ['np', 'notepad']:
        command=NOTEPAD_EDITOR
        judul = "Untitled - Notepad"
    elif editor in ['alt', 'plain', 'pad', 'ynote', 'rsed', 'rsone', 'goed', 'gomd', 'goide']:
        command = editors_map.get(editor, f'{AVALON_EDITOR} --title "{judul}"')
    #     command=ALT_EDITOR
    # elif editor in ['plain']:
    #     command=PLAIN_EDITOR
    # elif editor in ['pad']:
    #     command=PAD_EDITOR
    # elif editor in ['ynote']:
    #     command=YNOTE_EDITOR
    # step 1, stlh make_proces, akan fill in command_prompt_data
    identifier = create_register_cmd(command, identifier=judul, CURDIR=CURDIR)
    # step 2, tambahkan hwnd, biasanya gagal, mungkin perlu sleep cukup lama
    fill_in_hwnds()
    indah4(f'create_register_editor, title/id: {identifier}', warna='green')
    return identifier


def create_editor(editor, CURDIR=None, window_name=None):
    # create
    _id = create_register_editor(editor, CURDIR=CURDIR)
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

    if window_name:
        print('window_name:', window_name)
        # _, title, index = create_fill_set_with_id_index(CURDIR=CURDIR)
        command_prompt_data_extension[window_name] = {
            'title': _id,
            'index': index_or_none,
        }

    indah4(f"""create_editor
    items = {items} 
    title/_id = {_id}
    index/none = {index_or_none}
    """, warna='green')
    return items, _id, index_or_none


def get_window_name(code):
    console_name=None
    au_code=''
    # console_target=None
    # cek /ketik)[name=...] dan /ketik)[target=...]
    if code.startswith('[') and ']' in code:
        spec, code = code.split(']')
        spec = spec.removeprefix('[')
        for keyval in [kv.strip() for kv in spec.split(',')]:
            '''
            /edit:aval)[name=whatever]
            '''
            if '=' in keyval:
                k,v = [e.strip() for e in keyval.split('=')]
                if k == 'name':
                    console_name=v
                    indah4(f'get_window_name => window_name for editor: {console_name}', warna='magenta')
                elif k == 'au':
                    au_code=v
    return console_name, au_code
