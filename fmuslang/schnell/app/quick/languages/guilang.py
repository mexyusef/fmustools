import os, pyperclip, sys
from pprint import pprint
from uuid import uuid4 as u4
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.path.join(schnelldir, os.pardir)
# sys.path.extend([schnelldir, '..'])
# # print(schnelldir)
import sys
from pathlib import Path
sidoarjodir = Path(__file__).resolve().parent.parent.parent.parent.parent
#                              file     langs quick app     sch   sid
sys.path.append(sidoarjodir)

from schnell.app.transpiler.frontend.main import process_language
from schnell.app.printutils import indah4
from schnell.app.treeutils import (
    anak,
    data,
    token,
    child1,
    child2,
    child3,
    child4,
    child,
    chdata,
    chtoken,
    ispohon, istoken,
    beranak,
    sebanyak,
    jumlahanak,
)
from schnell.app.dirutils import joiner, joinhere, copy_files_to_tempdir
from schnell.app.fileutils import file_write, file_content, prepend_folder_to_filelist
from schnell.app.utils import env_get


from schnell.app.stringutils import tabify_content_tab, tabify_content_space, tabify_contentlist_tab, tabify_contentlist_space

output = {}
hasil = []
layoutcode = ''
final_result = ''

from schnell.app.quick.languages.guilang_helper.template import kode_output

def reset():
    global output, hasil, layoutcode, final_result
    output.clear()
    hasil = []
    layoutcode = ''
    final_result = ''


def mygui_handler(tree, parent_name='', parent_id=''):
    namaparent = ''
    itemid = ''

    for item in anak(tree):
        jenis = data(item)
        #print('jenis:', jenis) # , 'parent:', parent)

        if jenis == 'element_name':
            namaparent = token(item)
            itemid = str(u4())

            if namaparent in ['window','wnd','w','W']:
                print('\t=>', f'window/{itemid}, parent={parent_name}/{parent_id}')
                output['window'] = { 'id': itemid }
                output['items'] = {
                    itemid: {
                        'name': namaparent,
                        'type': 'window',
                        'parent': None,
                        'id': itemid,
                        'children': [],
                        'attrs': { 'main': False },
                    }
                }

            elif namaparent in ['layout','lyt','lay','L']:
                print('\t=>', f'layout/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'layout',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'ball':
                print('\t=>', f'ball/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'ball',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['button','btn','b','B']:
                print('\t=>', f'button/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'button',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'cal':
                print('\t=>', f'cal/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'cal',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'chartarea':
                print('\t=>', f'chartarea/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartarea',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartbar':
                print('\t=>', f'chartbar/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartbar',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartbarhorizontal':
                print('\t=>', f'chartbarhorizontal/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartbarhorizontal',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartbarpercent':
                print('\t=>', f'chartbarpercent/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartbarpercent',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartbarstack':
                print('\t=>', f'chartbarstack/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartbarstack',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartlinestack':
                print('\t=>', f'chartlinestack/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartlinestack',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartcpu':
                print('\t=>', f'chartcpu/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartcpu',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartcustomaxis':
                print('\t=>', f'chartcustomaxis/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartcustomaxis',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartline':
                print('\t=>', f'chartline/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartline',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartpie':
                print('\t=>', f'chartpie/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartpie',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartscatter':
                print('\t=>', f'chartscatter/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartscatter',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartspline':
                print('\t=>', f'chartspline/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartspline',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'chartsplinedynamic':
                print('\t=>', f'chartsplinedynamic/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'chartsplinedynamic',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'clock':
                print('\t=>', f'clock/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'clock',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'casio':
                print('\t=>', f'casio/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'casio',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'check':
                print('\t=>', f'check/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'check',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'colorinput':
                print('\t=>', f'color/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'colorinput',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'combo':
                print('\t=>', f'combo/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'combo',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'combofont':
                print('\t=>', f'combofont/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'combofont',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'date':
                print('\t=>', f'date/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'date',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'datetime':
                print('\t=>', f'datetime/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'datetime',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['devto']:
                print('\t=>', f'devto/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'devto',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'dial':
                print('\t=>', f'dial/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'dial',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'draw':
                print('\t=>', f'draw/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'draw',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'edit':
                print('\t=>', f'edit/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'edit',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'editor_standard':
                print('\t=>', f'editor_standard/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'editor_standard',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'editmulti':
                print('\t=>', f'editmulti/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'editmulti',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'flow':
                print('\t=>', f'flow/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'flow',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'form':
                print('\t=>', f'form/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'form',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'font':
                print('\t=>', f'font/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'font',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'fontinput':
                print('\t=>', f'fontinput/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'fontinput',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'fileinput':
                print('\t=>', f'fileinput/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'fileinput',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'filetree':
                print('\t=>', f'filetree/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'filetree',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'filetree2':
                print('\t=>', f'filetree2/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'filetree2',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent in ['frame', 'frm']:
                print('\t=>', f'frame/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'frame',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent in ['group', 'grp']:
                print('\t=>', f'group/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'group',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent in ['input', 'inp', 'i', 'I']:
                print('\t=>', f'input/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'input',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['label', 'lbl', 'l']:
                print('\t=>', f'label/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'label',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'lcd':
                print('\t=>', f'lcd/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'lcd',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'list':
                print('\t=>', f'list/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'list',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'listfold':
                print('\t=>', f'listfold/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'listfold',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['logrocket', 'lr']:
                print('\t=>', f'logrocket/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'logrocket',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['medium', 'med']:
                print('\t=>', f'medium/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'medium',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['message','msg','m','M']:
                print('\t=>', f'message/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'message',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'note':
                print('\t=>', f'note/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'note',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'notification_button':
                print('\t=>', f'notification_button/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'notification_button',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'notification_anim':
                print('\t=>', f'notification_anim/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'notification_anim',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'notification_clock':
                print('\t=>', f'notification_clock/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'notification_clock',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)
            elif namaparent == 'notification_content':
                print('\t=>', f'notification_content/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'notification_content',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'page':
                print('\t=>', f'page/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'page',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'pageswitch':
                print('\t=>', f'pageswitch/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'pageswitch',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'pdf':
                print('\t=>', f'pdf/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'pdf',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'plain':
                print('\t=>', f'plain/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'plain',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['plot_rt']:
                print('\t=>', f'plot_rt/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'plot_rt',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['plot_plotter']:
                print('\t=>', f'plot_plotter/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'plot_plotter',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['plot_static']:
                print('\t=>', f'plot_static/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'plot_static',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['plot_race']:
                print('\t=>', f'plot_race/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'plot_race',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'progress':
                print('\t=>', f'progress/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'progress',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'radio':
                print('\t=>', f'radio/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'radio',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'radios':
                print('\t=>', f'radios/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'radios',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'row':
                print('\t=>', f'row/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'row',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'stacked':
                print('\t=>', f'stacked/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'stacked',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'split':
                print('\t=>', f'split/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'split',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'spin':
                print('\t=>', f'spin/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'spin',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'spinfloat':
                print('\t=>', f'spinfloat/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'spinfloat',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'scrollbar':
                print('\t=>', f'scrollbar/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'scrollbar',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'slider':
                print('\t=>', f'slider/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'slider',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['stackoverflow', 'so']:
                print('\t=>', f'stackoverflow/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'stackoverflow',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'tab':
                print('\t=>', f'tab/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'tab',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'table':
                print('\t=>', f'table/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'table',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'tableview':
                print('\t=>', f'tableview/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'tableview',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'tetris':
                print('\t=>', f'tetris/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'tetris',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent == 'time':
                print('\t=>', f'time/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'time',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

            elif namaparent in ['windowbrowser', 'browser']:
                print('\t=>', f'windowbrowser/{itemid}, parent={parent_name}/{parent_id}')
                item = {
                    'name': namaparent,
                    'type': 'windowbrowser',
                    'parent': parent_id,
                    'id': itemid,
                    'children': [],
                    'attrs': {},
                }
                output['items'][itemid] = item
                output['items'][parent_id]['children'].append(item)

        elif jenis == 'element_children':
            for bagian in anak(item):
                for bagianlagi in bagian:
                    if data(bagianlagi) == 'declarative_element':
                        mygui_handler(bagianlagi, parent_name=namaparent, parent_id=itemid)

        elif jenis == 'element_config':
            for tupleitem in anak(item):
                configitem = data(tupleitem)
                if configitem == 'item_key_value':
                    k,v='',''
                    for anaktupleitem in anak(tupleitem):
                        jenis3 = data(anaktupleitem)
                        if jenis3 == 'item_key':
                            k = token(anaktupleitem)
                        elif jenis3 == 'item_value':
                            v = token(anaktupleitem)
                    print(f'  \t\tattr {namaparent}/{itemid} k=v => {k}={v}')
                    output['items'][itemid]['attrs'][k]=v
                elif configitem == 'item_key_value_boolean':
                    nilai = token(tupleitem)
                    print(f'  \t\tattr {namaparent}/{itemid} bool => {nilai}')
                    output['items'][itemid]['attrs'][nilai]=True

def process_layout(output, anak, indent=True, provided_layout_name=None):
    hasil = []
    if provided_layout_name: # jk container dari template code, mungkin gak punya attrs.name
        layoutname = provided_layout_name
    else:
        layoutname = anak['attrs']['name']
    layouttype = anak['attrs'].get('type', 'h') # anak['attrs']['type'] # container dari template code gak bertype
    # cek apa main layout
    parent_dict = output['items'][anak['parent']]
    bapak = parent_dict['type']=='window' and parent_dict['attrs']['main']==True
    print(f'layout: {layoutname} => {layouttype}, apakah mainlayout: {bapak}')
    if bapak:
        layoutname = 'self.main_layout'

    layoutcode = 'QHBoxLayout()'
    if layouttype=='v':
        layoutcode = 'QVBoxLayout()'

    for index,item in enumerate(anak['children']):

        jenis = item['type']

        if jenis == 'button':
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            line = f'{objname} = QPushButton("{tulisan}")'
            hasil.append(line)
            hasil.append(f"{objname}.clicked.connect(lambda: print('{tulisan}'))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'ball':
            print(f'\titem: {jenis}')
            objname = f'ball{index}'
            hasil.append(f"{objname} = BouncingBall(self)")
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'bouncingball' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'bouncingball': file_content(joinhere(__file__, 'guilang_helper/bouncingball.py'))
                })

        elif jenis == 'cal':
            print(f'\titem: {jenis}')
            objname = f'cal{index}'
            line = f'{objname} = QCalendarWidget(self)'
            hasil.append(line)
            hasil.append(f'# tanggal = {objname}.selectedDate()')
            hasil.append(f'{objname}.clicked[QDate].connect(lambda tanggal: print(f"{objname} says {{tanggal.toString()}}"))')
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'casio':
            print(f'\titem: {jenis}')
            objname = f'casio{index}'
            hasil.append(f"{objname} = DigitalClock(self)")
            hasil.append(f"{objname}.setMinimumHeight(100)")
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'casiowidget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'casiowidget': file_content(joinhere(__file__, 'guilang_helper/casio.py'))
                })

        elif jenis == 'chartarea':
            print(f'\titem: {jenis}')
            objname = f'chartarea{index}'
            hasil.append(f'{objname} = ChartArea()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartarea_content = file_content(joinhere(__file__, 'guilang_helper/chartarea.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartarea_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartarea_content': chartarea_content
                })

        elif jenis == 'chartbar':
            print(f'\titem: {jenis}')
            objname = f'chartbar{index}'
            hasil.append(f'{objname} = ChartBar()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartbar_content = file_content(joinhere(__file__, 'guilang_helper/chartbar.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartbar_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartbar_content': chartbar_content
                })

        elif jenis == 'chartbarhorizontal':
            print(f'\titem: {jenis}')
            objname = f'chartbarhorizontal{index}'
            hasil.append(f'{objname} = ChartBarHorizontal()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartbarhorizontal_content = file_content(joinhere(__file__, 'guilang_helper/chartbarhorizontal.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartbarhorizontal_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartbarhorizontal_content': chartbarhorizontal_content
                })

        elif jenis == 'chartbarpercent':
            print(f'\titem: {jenis}')
            objname = f'chartbarpercent{index}'
            hasil.append(f'{objname} = ChartBarPercent()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartbarpercent_content = file_content(joinhere(__file__, 'guilang_helper/chartbarpercent.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartbarpercent_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartbarpercent_content': chartbarpercent_content
                })

        elif jenis == 'chartline':
            print(f'\titem: {jenis}')
            objname = f'chartline{index}'
            hasil.append(f'{objname} = ChartLine()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartline_content = file_content(joinhere(__file__, 'guilang_helper/chartline.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartline_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartline_content': chartline_content
                })

        elif jenis == 'chartbarstack':
            print(f'\titem: {jenis}')
            objname = f'chartbarstack{index}'
            hasil.append(f'{objname} = ChartBarStack()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            # barstack dan linestack bergantung pada GraphicsProxyWidget
            if not 'additional_classes' in output or not 'graphics_proxy_widget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'graphics_proxy_widget': file_content(joinhere(__file__, 'guilang_helper/graphics_proxy_widget.py'))
                })
            chartbarstack_content = file_content(joinhere(__file__, 'guilang_helper/chartbarstack.py'))
            if not 'additional_classes' in output or not 'chartbarstack_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartbarstack_content': chartbarstack_content
                })

        elif jenis == 'chartlinestack':
            print(f'\titem: {jenis}')
            objname = f'chartlinestack{index}'
            hasil.append(f'{objname} = ChartLineStack()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            # barstack dan linestack bergantung pada GraphicsProxyWidget
            if not 'additional_classes' in output or not 'graphics_proxy_widget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'graphics_proxy_widget': file_content(joinhere(__file__, 'guilang_helper/graphics_proxy_widget.py'))
                })
            chartlinestack_content = file_content(joinhere(__file__, 'guilang_helper/chartlinestack.py'))
            if not 'additional_classes' in output or not 'chartlinestack_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartlinestack_content': chartlinestack_content
                })

        elif jenis == 'chartpie':
            print(f'\titem: {jenis}')
            objname = f'chartpie{index}'
            hasil.append(f'{objname} = ChartPie()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartpie_content = file_content(joinhere(__file__, 'guilang_helper/chartpie.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartpie_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartpie_content': chartpie_content
                })

        elif jenis == 'chartscatter':
            print(f'\titem: {jenis}')
            objname = f'chartscatter{index}'
            hasil.append(f'{objname} = ChartScatter()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartscatter_content = file_content(joinhere(__file__, 'guilang_helper/chartscatter.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartscatter_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartscatter_content': chartscatter_content
                })

        elif jenis == 'chartspline':
            print(f'\titem: {jenis}')
            objname = f'chartspline{index}'
            hasil.append(f'{objname} = ChartSpline()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartspline_content = file_content(joinhere(__file__, 'guilang_helper/chartspline.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartspline_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartspline_content': chartspline_content
                })

        elif jenis == 'chartsplinedynamic':
            print(f'\titem: {jenis}')
            objname = f'chartsplinedynamic{index}'
            hasil.append(f'{objname} = ChartSplineDynamic()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartsplinedynamic_content = file_content(joinhere(__file__, 'guilang_helper/chartsplinedynamic.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartsplinedynamic_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartsplinedynamic_content': chartsplinedynamic_content
                })

        elif jenis == 'chartcpu':
            print(f'\titem: {jenis}')
            objname = f'chartcpu{index}'
            hasil.append(f'{objname} = ChartCpu()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartcpu_content = file_content(joinhere(__file__, 'guilang_helper/chartcpu.py'))
            # chartline_content = chartline_content.replace('__LEBAR__', nilai_lebar)
            # chartline_content = chartline_content.replace('__TINGGI__', nilai_tinggi)
            # chartline_content = chartline_content.replace('__JUDUL__', nilai_judul)
            if not 'additional_classes' in output or not 'chartcpu_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartcpu_content': chartcpu_content
                })

        elif jenis == 'chartcustomaxis':
            print(f'\titem: {jenis}')
            objname = f'chartcustomaxis{index}'
            hasil.append(f'{objname} = ChartCustomAxis()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            chartcustomaxis_content = file_content(joinhere(__file__, 'guilang_helper/chartcustomaxis.py'))
            if not 'additional_classes' in output or not 'chartcustomaxis_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'chartcustomaxis_content': chartcustomaxis_content
                })

        elif jenis == 'clock':
            print(f'\titem: {jenis}')
            objname = f'clock{index}'
            hasil.append(f"{objname} = ClockWidget(self)")
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'clockwidget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'clockwidget': file_content(joinhere(__file__, 'guilang_helper/clockwidget.py'))
                })

        elif jenis == 'check':
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'check{index}'
            hasil.append(f'{objname} = QCheckBox("{tulisan}")')
            # default handler
            hasil.append(f"{objname}.stateChanged.connect(lambda state: print('{tulisan} says yes' if state==Qt.Checked else '{tulisan} says no'))")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'colorinput':
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']

            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')

            def create_colorinput_handler(button_name):
                temp = []
                # buat body
                temp.append(f"color = QColorDialog.getColor()")
                temp.append(f"if color.isValid():")
                temp.append(f"    print('name:', color.name())")
                temp.append(f"    print('rgb:', color.rgb())")
                temp.append(f"    print('rgba:', color.rgba())")
                temp.append(f"    print('toRgb:', color.toRgb())")
                temp.append(f"    print('red:', color.red())")
                temp.append(f"    print('green:', color.green())")
                temp.append(f"    print('blue:', color.blue())")
                temp.append(f"    print('alpha:', color.alpha())")
                temp.append(f"    print('hue:', color.hue())")
                temp.append(f"    print('saturation:', color.saturation())")
                temp.append(f"    print('lightness:', color.lightness())\n")
                handler_body = tabify_contentlist_space(temp, num_tab=2, space_size=4)
                result = f'def colorinput_handler_for_{button_name}(self):\n' + handler_body
                if not 'methods' in output:
                    output['methods'] = [result]
                else:
                    output['methods'].append(result)

            hasil.append(f"{objname}.clicked.connect(self.colorinput_handler_for_{objname})")
            create_colorinput_handler(f'{objname}')
            hasil.append(f'{layoutname}.addWidget({objname})')
            
        elif jenis == 'combo':
            default_items = "'satu', 'dua', 'tiga', 'empat', 'lima'"
            if 'items' in item['attrs']:
                #default_items = item['attrs']['items']
                # gara2 config item, utk items harus dipisah /
                default_items = ', '.join(f"'{thing.strip()}'" for thing in item['attrs']['items'].split('/'))
            print(f'\titem: {jenis}', 'default_items:', default_items)
            objname = f'combo{index}'
            line = f'{objname} = QComboBox(self)'
            hasil.append(line)
            # default handler
            
            hasil.append(f"{objname}.addItems([{default_items}])")
            hasil.append(f"{objname}.currentTextChanged.connect(lambda value: print(value))")
            hasil.append(f"{objname}.currentIndexChanged.connect(lambda index: print(index))")
            hasil.append(f"# {objname}.textChanged.connect(lambda value: print(value))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'date':
            print(f'\titem: {jenis}')
            objname = f'date{index}'
            line = f'{objname} = QDateEdit(self)'
            hasil.append(line)
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'datetime':
            print(f'\titem: {jenis}')
            objname = f'datetime{index}'
            hasil.append(f'{objname} = QDateTimeEdit(self)')
            hasil.append(f'{objname}.setDateTime(QDateTime.currentDateTime())')
            hasil.append(f'{objname}.setDisplayFormat("yyyy/MM/dd hh:mm:ss")')
            hasil.append(f'{objname}.setCalendarPopup(True)')
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'devto':
            tulisan = 'DevTo'
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'logrocket{index}'
            hasil.append(f'{objname} = DevTo()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            # tambah dependencies ke BrowserWindow utk stackoverflow dan logrocket
            if not 'additional_classes' in output or not 'mainwindow_browser' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'mainwindow_browser': file_content(joinhere(__file__, 'guilang_helper/mainwindow_browser.py'))
                })
            if not 'additional_classes' in output or not 'devto_getdata' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'devto_getdata': file_content(joinhere(__file__, 'guilang_helper/devto_getdata.py'))
                })
            if not 'additional_classes' in output or not 'devto_control' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'devto_control': file_content(joinhere(__file__, 'guilang_helper/devto_control.py')).replace('__JUDUL__',tulisan)
                })

        elif jenis == 'dial':
            #tulisan = ''
            #if 'label' in item['attrs']:
            #    tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'dial{index}'
            line = f'{objname} = QDial()'
            hasil.append(line)
            # default handler
            hasil.append(f"{objname}.setRange(0,100)")
            hasil.append(f"{objname}.setSingleStep(1)")
            hasil.append(f"{objname}.valueChanged.connect(lambda value: print('val:', value))")
            hasil.append(f"{objname}.sliderMoved.connect(lambda value: print('pos', value))")
            hasil.append(f"{objname}.sliderPressed.connect(lambda: print('pressed'))")
            hasil.append(f"{objname}.sliderReleased.connect(lambda: print('released'))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'draw':
            '''
            '''
            print(f'\titem: {jenis}')
            objname = f'draw{index}'
            hasil.append(f"{objname} = DrawingWidget()")
            # for i,record in enumerate(item['children']):
            #     control = 'QLineEdit' # edit
            #     label = record['attrs']['label']
            #     hasil.append(f"{objname}.addRow('{label}', {control}())") # addRow bukan addWidget spt oleh layout
            #line = f'{objname} = QFontComboBox(self)'
            #hasil.append(line)
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'drawing_widget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'drawing_widget': file_content(joinhere(__file__, 'guilang_helper/drawing.py'))
                })

        elif jenis == 'edit':
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'edit{index}'
            line = f'{objname} = QLineEdit("{tulisan}")'
            hasil.append(line)
            hasil.append(f"{objname}.returnPressed.connect(lambda: print(f'Enter: {{{objname}.text()}}'))")
            hasil.append(f"# {objname}.selectionChanged.connect(lambda: print('selection changed'))")
            hasil.append(f"# {objname}.textChanged.connect(lambda value: print(value))")
            hasil.append(f"# {objname}.textEdited.connect(lambda value: print(value))")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'editmulti':
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'textedit{index}'
            line = f'{objname} = QTextEdit("{tulisan}")'
            hasil.append(line)
            hasil.append(f"# {objname}.returnPressed.connect(lambda: print('Enter'))")
            hasil.append(f"# {objname}.selectionChanged.connect(lambda: print('selection changed'))")
            hasil.append(f"# {objname}.textChanged.connect(lambda value: print(value))")
            hasil.append(f"# {objname}.textEdited.connect(lambda value: print(value))")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'editor_standard':
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'editor_standard{index}'
            hasil.append(f'{objname} = EditorStandard(self)')
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'editor_standard' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'editor_standard': file_content(joinhere(__file__, 'guilang_helper/editor_standard.py'))
                })

        elif jenis == 'fileinput':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            line = f'{objname} = QPushButton("{tulisan}")'
            hasil.append(line)

            def create_fileinput_handler(button_name):
                temp = []
                temp.append(f"filename, ok = QFileDialog.getOpenFileName(None, 'Open file:', '.', 'Text files (*.txt)')")
                temp.append(f"if ok: print(f'Anda milih filename: {{filename}}')\n\n")
                handler_body = tabify_contentlist_space(temp, num_tab=1, space_size=4)
                result = f'def fileinput_handler_for_{button_name}():\n' + handler_body
                if not 'functions' in output:
                    output['functions'] = [result]
                else:
                    output['functions'].append(result)

            hasil.append(f"{objname}.clicked.connect(fileinput_handler_for_{objname})")
            create_fileinput_handler(f'{objname}')
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'filetree':
            print(f'\titem: {jenis}')
            objname = f'filetree{index}'
            hasil.append(f"{objname} = FileTree()")
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'filetree' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'filetree': file_content(joinhere(__file__, 'guilang_helper/filetree.py'))
                })

        elif jenis == 'filetree2':
            print(f'\titem: {jenis}')
            objname = f'filetree2{index}'
            hasil.append(f"{objname} = FileTreeWidget()")
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'filetree2' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'filetree2': file_content(joinhere(__file__, 'guilang_helper/filetree2.py'))
                })

        elif jenis == 'form':
            '''
            <form[](
                row[label=sebuah tulisan, control=control]
            )
            '''
            print(f'\titem: {jenis}')
            objname = f'form{index}'
            hasil.append(f"{objname} = QFormLayout()")
            for i,record in enumerate(item['children']):
                control = 'QLineEdit' # edit
                label = record['attrs']['label']
                hasil.append(f"{objname}.addRow('{label}', {control}())") # addRow bukan addWidget spt oleh layout
            #line = f'{objname} = QFontComboBox(self)'
            #hasil.append(line)
            line = f'{layoutname}.addLayout({objname})'
            hasil.append(line)

        elif jenis == 'flow':
            '''
            <flow[](
                btn[label=sebuah tulisan, control=control]
            )
            '''
            print(f'\titem: {jenis}')
            objname = f'flow{index}'
            hasil.append(f"{objname} = FlowWidget()")
            hasil.append(f"widgets = []")
            # laycode, layname, laycontent = process_layout(output, item, indent=False, provided_layout_name='self.layout_main')
            for i,record in enumerate(item['children']):
                # sementara hanya QPushButton masuk flow layout widget
                # control = 'QPushButton' # edit
                label = record['attrs']['label']
                hasil.append(f"btn{index}_{i} = QPushButton('{label}')")
                hasil.append(f"widgets.append(btn{index}_{i})") # widgets.append bukan addWidget spt layout
                hasil.append(f"btn{index}_{i}.clicked.connect(lambda: print('{label}'))")
            hasil.append(f"{objname}.add_items(widgets)")
            hasil.append(f'{layoutname}.addWidget({objname})')

            if not 'additional_classes' in output or not 'flowwidget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'flowwidget': file_content(joinhere(__file__, 'guilang_helper/flowwidget.py'))
                })

        elif jenis == 'fontinput':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            line = f'{objname} = QPushButton("{tulisan}")'
            hasil.append(line)

            def create_fontinput_handler(button_name):
                temp = []
                temp.append(f"font, ok = QFontDialog.getFont()")
                temp.append(f"if ok: print(f'Anda milih font: {{font}}')\n\n")
                handler_body = tabify_contentlist_space(temp, num_tab=1, space_size=4)
                result = f'def fontinput_handler_for_{button_name}():\n' + handler_body
                if not 'functions' in output:
                    output['functions'] = [result]
                else:
                    output['functions'].append(result)

            hasil.append(f"{objname}.clicked.connect(fontinput_handler_for_{objname})")
            create_fontinput_handler(f'{objname}')
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'font':
            print(f'\titem: {jenis}')
            objname = f'font{index}'
            line = f'{objname} = QFontComboBox(self)'
            hasil.append(line)
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'frame':
            '''
            frame spt group?...group minta label, frame gak
            spt split dg tab...page di tab minta label, di split gak
            <frame(
                <b
                <label
                <edit
            )
            '''
            # tulisan = ''
            # if 'label' in item['attrs']:
            #     tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'frame{index}'
            hasil.append(f'{objname} = QFrame(self)')
            hasil.append(f'{objname}.setFrameShape(QFrame.NoFrame)')
            hasil.append(f'{objname}.setFrameShadow(QFrame.Raised)')
            hasil.append(f'{objname}.setStyleSheet("background-color: #d34db33f;")')
            hasil.append(f'{objname}.setObjectName("{objname}")')
            hasil.append(f'layout_for_{objname} = QVBoxLayout()')
            laycode, layname, laycontent = process_layout(output, item, indent=False, provided_layout_name=f'layout_for_{objname}')
            # hilangkan indent di kiri
            # hasil.append(f'# sblm lstrip: [{laycontent}]')
            laycontent = '\n' + laycontent # entah kenapa selalu ekstra indent 2 tab, terpaksa hrs tambah \n dulu
            formatted_content = tabify_content_space(laycontent, num_tab=2, space_size=4)
            hasil.append(f'{formatted_content}')
            hasil.append(f'# layout_for_{objname}.addStretch(1)')
            hasil.append(f'{objname}.setLayout(layout_for_{objname})')
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'group':
            '''
            <group[label=nama group](
                <b
                <label
                <edit
            )
            '''
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'group{index}'
            hasil.append(f'{objname} = QGroupBox("{tulisan}")')
            hasil.append(f'layout_for_{objname} = QVBoxLayout()')
            laycode, layname, laycontent = process_layout(output, item, indent=False, provided_layout_name=f'layout_for_{objname}')
            # hilangkan indent di kiri
            # hasil.append(f'# sblm lstrip: [{laycontent}]')
            laycontent = '\n' + laycontent # entah kenapa selalu ekstra indent 2 tab, terpaksa hrs tambah \n dulu
            formatted_content = tabify_content_space(laycontent, num_tab=2, space_size=4)
            hasil.append(f'{formatted_content}')
            hasil.append(f'# layout_for_{objname}.addStretch(1)')
            hasil.append(f'{objname}.setLayout(layout_for_{objname})')
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'input':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')

            def create_input_handler(button_name, content):
                temp = []
                temp.append(f"# getText/getInt/getDouble(parent, judul, isi), getItem(parent, judul, isi, list_pilihan)")
                temp.append(f"text, pressed = QInputDialog.getText(None, '{content}', '{content}', QLineEdit.Normal, '')")
                temp.append(f"if pressed: print(f'Anda memasukkan: {{text}}')\n\n")
                handler_body = tabify_contentlist_space(temp, num_tab=1, space_size=4)
                result = f'def input_handler_for_{button_name}():\n' + handler_body
                if not 'functions' in output:
                    output['functions'] = [result]
                else:
                    output['functions'].append(result)

            hasil.append(f"{objname}.clicked.connect(input_handler_for_{objname})")
            create_input_handler(f'{objname}', tulisan)
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'label':
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'lbl{index}'
            line = f'{objname} = QLabel("{tulisan}")'
            hasil.append(line)
            hasil.append(f'# font = {objname}.font()')
            hasil.append(f'# font.setPointSize(30)')
            hasil.append(f'# {objname}.setFont(font)')
            hasil.append(f'# {objname}.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)')
            # pixmap = QPixmap(16, 16)
            # pixmap.fill(Qt.transparent)
            # painter = QPainter()
            # painter.begin(pixmap)
            # painter.setFont(QFont('Webdings', 11))
            # painter.setPen(Qt.GlobalColor(random.randint(4, 18)))
            # painter.drawText(0, 0, 16, 16, Qt.AlignCenter, random.choice(string.ascii_letters))
            # painter.end()
            hasil.append(f'# {objname}.setPixmap(QPixmap(filepath))')
            hasil.append(f'# either label or icon')
            hasil.append(f'# {objname}.setPixmap(QApplication.style().standardIcon(QStyle.SP_VistaShield).pixmap(QSize(16,16)))')
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'layout':
            # first = init layout, second = layout content, third = add to parent layout
            laycode, layname, laycontent = process_layout(output, item, indent=False)
            first = f'{layname} = {laycode}'
            second = laycontent
            third = f'{layoutname}.addLayout({layname})'
            tempres = ['\n']
            tempres.append(first) # layoutname = QVBoxLayout()
            tempres += second.splitlines() # content = multiline string
            tempres.append(third) # currentlayout.addLayout(layoutname)
            tempres.append('\n')
            print(f'oprek layout => tempres 1+2+3:\n{tempres}')
            formatres = tabify_contentlist_space(tempres, num_tab=2, space_size=4)
            # formatres = tabify_contentlist_space(tempres, num_tab=1, space_size=4)
            hasil.append(formatres)

        elif jenis == 'lcd':
            print(f'\titem: {jenis}')
            objname = f'lcd{index}'
            line = f'{objname} = QLCDNumber(self)'
            hasil.append(line)
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
                if tulisan.isdigit():
                    hasil.append(f'{objname}.display({tulisan})')
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'list':
            objname = f'list{index}'
            hasil.append(f'{objname} = QListWidget(self)')
            # default handler
            default_items = "'satu', 'dua', 'tiga', 'empat', 'lima'"
            if 'items' in item['attrs']:
                #default_items = item['attrs']['items']
                # gara2 config item, utk items harus dipisah /
                default_items = ', '.join(f"'{thing.strip()}'" for thing in item['attrs']['items'].split('/'))
            print(f'\titem: {jenis}', 'default_items:', default_items)
            hasil.append(f"{objname}.addItems([{default_items}])")
            hasil.append(f"{objname}.currentItemChanged.connect(lambda listitem: print('item changed:', listitem.text()))")
            hasil.append(f"{objname}.currentTextChanged.connect(lambda value: print('text changed:', value))")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'listfold':
            '''
            <listfold(
                <page[label=lihat analog](<clock)
                <page[label=lihat digital](<casio)
            )
            '''
            objname = f'listfold{index}'            
            print(f'\titem: {jenis}')
            hasil.append(f'{objname} = FoldedListWidget(self)')

            listfold_content = file_content(joinhere(__file__, 'guilang_helper/listfold.py'))
            listfold_forloop_collect = []
            for i,record in enumerate(item['children']):
                listfold_forloop = file_content(joinhere(__file__, 'guilang_helper/listfold_iterate.py'))
                listfold_anak = file_content(joinhere(__file__, 'guilang_helper/listfold_anak.py'))
                tulisan = 'Fold me'
                if 'label' in record['attrs']:
                    tulisan = record['attrs']['label']
                content_per_anak = []
                content_per_anak.append(f"{objname}_pagelayout_{i} = QVBoxLayout(self)")
                laycode, layname, laycontent = process_layout(output, record, indent=False, provided_layout_name=f'{objname}_pagelayout_{i}')
                tempres = ['\n'] # jk gak di awali \n selalu terindent 2 tab
                tempres += laycontent.splitlines() # content = multiline string
                formatted_layoutcontent = tabify_contentlist_space(tempres, num_tab=2, space_size=4)
                content_per_anak.append(formatted_layoutcontent)
                # content_per_anak.append(f'# content per anak total [{len(item["children"])}] kita terima laycontent = [{laycontent}] utk i {i} dan record [{record}]')
                content_per_anak.append('\n')
                WIDGET_ANAK_NAME = f'WidgetAnak{i+1}'
                listfold_anak = listfold_anak.replace('__WIDGET_ANAK_NAME__', WIDGET_ANAK_NAME)
                # string_content_per_anak = '\n'.join(content_per_anak)
                string_content_per_anak = tabify_contentlist_space(content_per_anak, num_tab=2, space_size=4)
                listfold_anak = listfold_anak.replace('__TEMPLATE_CONTENT__', string_content_per_anak)
                listfold_anak_unique_name = f'listfold_anak_name_for_{objname}_{i}_{u4().hex}'
                if not 'additional_classes' in output or not f'{listfold_anak_unique_name}' in output['additional_classes']:
                    if not 'additional_classes' in output:
                        output['additional_classes'] = {}
                    output['additional_classes'].update({
                        f'{listfold_anak_unique_name}': listfold_anak
                    })

                listfold_forloop = listfold_forloop.replace('__FOLD_TITLE__', tulisan)
                listfold_forloop = listfold_forloop.replace('__LOOP_INDEX__', str(i))
                listfold_forloop = listfold_forloop.replace('__WIDGET_ANAK_NAME__', WIDGET_ANAK_NAME)
                listfold_forloop_collect.append(listfold_forloop)

            string_listfold_forloop_collect = '\n'.join(listfold_forloop_collect)
            listfold_content = listfold_content.replace('__TEMPLATE_WIDGET_ITEMS__', string_listfold_forloop_collect)
            # kode FoldedListWidget harus masuk additional_classes
            if not 'additional_classes' in output or not 'folded_list_widget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'folded_list_widget': listfold_content
                })
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'logrocket':
            tulisan = 'LogRocket'
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'logrocket{index}'
            hasil.append(f'{objname} = LogRocket()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            # tambah dependencies ke BrowserWindow utk stackoverflow dan logrocket
            if not 'additional_classes' in output or not 'mainwindow_browser' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'mainwindow_browser': file_content(joinhere(__file__, 'guilang_helper/mainwindow_browser.py'))
                })
            if not 'additional_classes' in output or not 'logrocket_getdata' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'logrocket_getdata': file_content(joinhere(__file__, 'guilang_helper/logrocket_getdata.py'))
                })
            if not 'additional_classes' in output or not 'logrocket_control' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'logrocket_control': file_content(joinhere(__file__, 'guilang_helper/logrocket_control.py')).replace('__JUDUL__',tulisan)
                })

        elif jenis == 'medium':
            tulisan = 'MediumWeb'
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'logrocket{index}'
            hasil.append(f'{objname} = MediumWeb()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            # tambah dependencies ke BrowserWindow utk stackoverflow dan logrocket
            if not 'additional_classes' in output or not 'mainwindow_browser' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'mainwindow_browser': file_content(joinhere(__file__, 'guilang_helper/mainwindow_browser.py'))
                })
            if not 'additional_classes' in output or not 'medium_getdata' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'medium_getdata': file_content(joinhere(__file__, 'guilang_helper/medium_getdata.py'))
                })
            if not 'additional_classes' in output or not 'medium_control' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'medium_control': file_content(joinhere(__file__, 'guilang_helper/medium_control.py')).replace('__JUDUL__',tulisan)
                })

        elif jenis == 'message':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            line = f'{objname} = QPushButton("{tulisan}")'
            hasil.append(line)

            def create_message_handler(button_name, content):
                temp = []
                temp.append(f"msg = QMessageBox(None)")
                temp.append(f"msg.setWindowTitle('{content}')")
                temp.append(f"msg.setText('{content}')")
                temp.append(f"msg.setIcon(QMessageBox.Question)")
                temp.append(f"msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)")
                temp.append(f"msg.setDefaultButton(QMessageBox.Ok)")
                temp.append(f"msg.setDetailedText('detail: {content}')")
                temp.append(f"msg.setInformativeText('informative: {content}')")
                temp.append(f"x = msg.exec_()")

                handler_body = tabify_contentlist_space(temp, num_tab=1, space_size=4)
                result = f'def message_handler_for_{button_name}():\n' + handler_body
                if not 'functions' in output:
                    output['functions'] = [result]
                else:
                    output['functions'].append(result)

            hasil.append(f"{objname}.clicked.connect(message_handler_for_{objname})")
            create_message_handler(f'{objname}', tulisan)
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'note':
            # tulisan = ''
            # if 'label' in item['attrs']:
            #     tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'note{index}'
            hasil.append(f'{objname} = StickyNote(self)')
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'sticky_note' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'sticky_note': file_content(joinhere(__file__, 'guilang_helper/sticky_note.py'))
                })

        elif jenis == 'notification_button':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            notification_type = 'info' # success, warning, error
            notification_title = 'Judul'
            notification_body = 'Badanku badanmu sama hitam...'
            
            if 'body' in item['attrs']:
                notification_body = item['attrs']['body']
            if 'title' in item['attrs']:
                notification_title = item['attrs']['title']
            if 'type' in item['attrs']:
                notification_type = item['attrs']['type']
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')
            notification_color = 'cyan'
            if notification_type == 'success':
                notification_color = 'green'
            elif notification_type == 'error':
                notification_color = 'red'
            elif notification_type == 'warning':
                notification_color = 'yellow'
            hasil.append(f'{objname}.setStyleSheet("background-color: {notification_color};")')
            # tambah kode browser di atas
            if not 'additional_classes' in output or not 'notification_kanan_atas' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'notification_kanan_atas': file_content(joinhere(__file__, 'guilang_helper/notification_kanan_atas.py'))
                })
            # jk button diclick, tampilkan browser
            hasil.append(f"{objname}.clicked.connect(lambda: NotificationWindow.{notification_type}('{notification_title}', '{notification_body}', callback=lambda: print('[{objname}/{tulisan}] says click')) )")
            # tambahkan button ke layout
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'notification_anim':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            notification_type = 'info' # success, warning, error
            notification_title = 'Judul'
            notification_body = 'Badanku badanmu sama hitam...'
            if 'body' in item['attrs']:
                notification_body = item['attrs']['body']
            if 'title' in item['attrs']:
                notification_title = item['attrs']['title']
            if 'type' in item['attrs']:
                notification_type = item['attrs']['type']
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')

            hasil.append(f'{objname}.setStyleSheet("background-color: #d34db33f;")')
            # tambah kode browser di atas
            if not 'additional_classes' in output or not 'notification_kanan_bawah' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'notification_kanan_bawah': file_content(joinhere(__file__, 'guilang_helper/notification_kanan_bawah.py'))
                })
            # jk button diclick, tampilkan browser
            hasil.append(f"{objname}.clicked.connect(lambda: NotificationKananBawah().show(content='{notification_body}').showAnimation() )")
            # tambahkan button ke layout
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'notification_clock':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            notification_type = 'info' # success, warning, error
            notification_title = 'Judul'
            notification_body = 'Badanku badanmu sama hitam...'
            if 'body' in item['attrs']:
                notification_body = item['attrs']['body']
            if 'title' in item['attrs']:
                notification_title = item['attrs']['title']
            if 'type' in item['attrs']:
                notification_type = item['attrs']['type']
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')

            hasil.append(f'{objname}.setStyleSheet("background-color: #d34db33f;")')

            # bergantung pd clockwidget, dimasukkan duluan
            if not 'additional_classes' in output or not 'clockwidget' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'clockwidget': file_content(joinhere(__file__, 'guilang_helper/clockwidget.py'))
                })
            if not 'additional_classes' in output or not 'clock_bottom' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'clock_bottom': file_content(joinhere(__file__, 'guilang_helper/clock_bottom.py'))
                })
            # jk button diclick, tampilkan animasi clock di bottom right
            hasil.append(f"{objname}.clicked.connect(lambda: ClockBottom().animate() )")
            # tambahkan button ke layout
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'notification_content':
            laycode, layname, laycontent = process_layout(output, item, indent=False, provided_layout_name='self.layout_main')
            tempres = ['\n'] # agar gak indent ekstra 2 tab
            tempres += laycontent.splitlines() # content = multiline string, jadikan list dulu
            tempres.append('\n')
            formatted_layoutcontent = tabify_contentlist_space(tempres, num_tab=2, space_size=4)

            tulisan = item['attrs']['label']
            tinggi_float = 0.75
            lebar_float = 0.25
            if 'h' in item['attrs']:
                tinggi_float = float(item['attrs']['h'])
            if 'w' in item['attrs']:
                lebar_float = float(item['attrs']['w'])
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')
            hasil.append(f'{objname}.setStyleSheet("background-color: #A5D56E;")')

            notification_bottom_content = file_content(joinhere(__file__, 'guilang_helper/notification_bottom.py'))
            notification_bottom_content = notification_bottom_content.replace('__TEMPLATE_CONTENT__', formatted_layoutcontent)
            notification_bottom_content = notification_bottom_content.replace('__LEBAR__', str(lebar_float))
            notification_bottom_content = notification_bottom_content.replace('__TINGGI__', str(tinggi_float))
            if not 'additional_classes' in output or not 'notification_bottom' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'notification_bottom': notification_bottom_content
                })
            hasil.append(f"{objname}.clicked.connect(lambda: NotificationBottom().animate() )")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'pageswitch':
            '''
            <pageswitch(
                <page[label=lihat analog](<clock)
                <page[label=lihat digital](<casio)
            )
            '''
            objname = f'pageswitch{index}'
            classname = f'PageSwitch{index}'
            print(f'\titem: {jenis}') 
            num_pages = len(item['children'])
            hasil.append(f'{objname} = {classname}(pages={num_pages})')
            pageswitcher_content = file_content(joinhere(__file__, 'guilang_helper/pageswitcher.py'))
            pageswitcher_content = pageswitcher_content.replace('__PAGE_SWITCHER_NAME__', classname)

            content_per_anak_collect = []
            for i,record in enumerate(item['children']):
                content_per_anak = []
                content_per_anak.append(f"        {objname}_page_{i} = QWidget(self)")
                content_per_anak.append(f"        {objname}_pagelayout_{i} = QVBoxLayout({objname}_page_{i})")
                laycode, layname, laycontent = process_layout(output, record, indent=False, provided_layout_name=f'{objname}_pagelayout_{i}')
                print(f"[pageswitch] cek indent, laycontent=[{laycontent}]")
                tempres = [] # jk gak di awali \n selalu terindent 2 tab
                tempres += laycontent.splitlines() # content = multiline string
                formatted_layoutcontent = tabify_contentlist_space(tempres, num_tab=2, space_size=4)
                content_per_anak.append(formatted_layoutcontent)
                content_per_anak.append(f"        self.stackedWidget.addWidget({objname}_page_{i})") # addTab bukan addWidget
                content_per_anak.append('\n')

                content_per_anak_collect += content_per_anak

            string_pageswitcher_collect = '\n'.join(content_per_anak_collect)
            pageswitcher_content = pageswitcher_content.replace('__TEMPLATE_WIDGET_ITEMS__', string_pageswitcher_collect)

            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'pageswitcher_stacked' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'pageswitcher_stacked': file_content(joinhere(__file__, 'guilang_helper/pageswitcher_stacked.py'))
                })
            if not 'additional_classes' in output or not f'{classname}' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    f'{classname}': pageswitcher_content
                })

        elif jenis == 'pdf':
            print(f'\titem: {jenis}')
            objname = f'pdf{index}'
            hasil.append(f"{objname} = PdfViewer(self)")
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'pdf_viewer' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'pdf_viewer': file_content(joinhere(__file__, 'guilang_helper/pdf_viewer.py'))
                })

        elif jenis == 'plain':
            tulisan = ''
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'plain{index}'
            line = f'{objname} = QPlainTextEdit("{tulisan}")'
            hasil.append(line)
            hasil.append(f"# {objname}.returnPressed.connect(lambda: print('Enter'))")
            hasil.append(f"# {objname}.selectionChanged.connect(lambda: print('selection changed'))")
            hasil.append(f"# {objname}.textChanged.connect(lambda value: print(value))")
            hasil.append(f"# {objname}.textEdited.connect(lambda value: print(value))")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'plot_plotter':
            print(f'\titem: {jenis}')
            objname = f'plot_rt{index}'
            hasil.append(f'{objname} = MatplotPlotter()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'matplot_canvas' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'matplot_canvas': file_content(joinhere(__file__, 'guilang_helper/matplot_canvas.py'))
                })
            if not 'additional_classes' in output or not 'matplot_plotter' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'matplot_plotter': file_content(joinhere(__file__, 'guilang_helper/matplot_plotter.py'))
                })

        elif jenis == 'plot_race':
            df = '1' # country population
            if 'df' in item['attrs']:
               df = item['attrs']['df']
            file_to_open = {
                'country_population'    : 'plot_race_country_population.py',
                '1'                     : 'plot_race_country_population.py',
                'city_population'       : 'plot_race_city_population.py',
                '2'                     : 'plot_race_city_population.py',
                '3'                     : 'plot_race_nonrace.py',
            }
            objname = f'plot_race{index}'
            hasil.append(f'{objname} = MatplotRace()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            matplotlib_race_content = file_content(joinhere(__file__, f'guilang_helper/{file_to_open[df]}'))
            if not 'additional_classes' in output or not 'plot_race_country_population' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'plot_race_country_population': matplotlib_race_content
                })

        elif jenis == 'plot_rt':
            print(f'\titem: {jenis}')
            objname = f'plot_rt{index}'
            hasil.append(f'{objname} = MatplotRealtimeInplace()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'matplot_canvas' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'matplot_canvas': file_content(joinhere(__file__, 'guilang_helper/matplot_canvas.py'))
                })
            if not 'additional_classes' in output or not 'matplot_realtime_inplace' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'matplot_realtime_inplace': file_content(joinhere(__file__, 'guilang_helper/matplot_realtime_inplace.py'))
                })

        elif jenis == 'plot_static':
            print(f'\titem: {jenis}')
            objname = f'plot_rt{index}'
            hasil.append(f'{objname} = MatplotStatic()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'matplot_canvas' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'matplot_canvas': file_content(joinhere(__file__, 'guilang_helper/matplot_canvas.py'))
                })
            if not 'additional_classes' in output or not 'matplot_static' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'matplot_static': file_content(joinhere(__file__, 'guilang_helper/matplot_static.py'))
                })

        elif jenis == 'progress':
            print(f'\titem: {jenis}')
            objname = f'progress{index}'
            line = f'self.{objname} = QProgressBar(self)'
            hasil.append(line)
            def create_progress_handler(timer_name, progressbar_name):
                temp = []
                # buat body
                temp.append(f"self.{progressbar_name}_count += 1")
                temp.append(f"{timer_name}.stop() if self.{progressbar_name}_count >= 100 else self.{progressbar_name}.setValue(self.{progressbar_name}_count)")
                handler_body = tabify_contentlist_space(temp, num_tab=2, space_size=4)
                result = f'def progress_handler_for_{progressbar_name}(self):\n' + handler_body
                if not 'methods' in output:
                    output['methods'] = [result]
                else:
                    output['methods'].append(result)
            hasil.append(f"self.{objname}_timer = QTimer()")
            hasil.append(f"self.{objname}_count = 0")
            hasil.append(f"self.{objname}_timer.setInterval(1000)")
            hasil.append(f"self.{objname}_timer.start()")
            hasil.append(f"self.{objname}_timer.timeout.connect(self.progress_handler_for_{objname})")
            create_progress_handler(f'self.{objname}_timer', f'{objname}')
            line = f'{layoutname}.addWidget(self.{objname})'
            hasil.append(line)

        elif jenis == 'radio':
            tulisan = ''
            if 'label' in item['attrs']:
               tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'radio{index}'
            line = f'{objname} = QRadioButton("{tulisan}")'
            hasil.append(line)
            # default handler
            # hasil.append(f"{objname}.addItems(['satu', 'dua', 'tiga', 'empat', 'lima'])")
            # hasil.append(f"{objname}.currentTextChanged.connect(lambda value: print(value))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'radios':
            '''
            <radios(
                <b[label=radio1] <- bisa b, label, dll dont matter krn kita hanya ambil attr labelnya
                <b[label=radio2]
            )
            '''
            print(f'\titem: {jenis}')
            objname = f'radios{index}'
            line = f'{objname} = QButtonGroup(self)'
            hasil.append(line)

            def create_radio_handler(objname):
                temp = []
                # buat body
                # temp.append(f"self.{progressbar_name}_count += 1")
                # temp.append(f"{timer_name}.stop() if self.{progressbar_name}_count >= 100 else self.{progressbar_name}.setValue(self.{progressbar_name}_count)")
                temp.append(f"toggled_radio = self.sender()")
                temp.append(f"print(f'{{toggled_radio.text()}} is {{\"ON\" if toggled_radio.isChecked() else \"OFF\"}}')")
                handler_body = tabify_contentlist_space(temp, num_tab=2, space_size=4)
                result = f'def radios_toggled_for_{objname}(self, value):\n' + handler_body
                if not 'methods' in output:
                    output['methods'] = [result]
                else:
                    output['methods'].append(result)

            for i,record in enumerate(item['children']): # iterate page
                # control = 'QLabel' # edit
                # label = record['attrs']['label']
                # # tiap page sementara hanya berisi QLabel yg sama tulisannya dg label = judul tab
                # hasil.append(f"{objname}.addWidget({control}('{label}'))")
                # hasil.append(f"{navig_objname}.insertItem({i}, '{label}')")
                tulisan = ''
                if 'label' in record['attrs']:
                    tulisan = record['attrs']['label']
                hasil.append(f"radio{i} = QRadioButton('{tulisan}')")
                hasil.append(f"radio{i}.toggled.connect(self.radios_toggled_for_{objname})")
                hasil.append(f"{objname}.addButton(radio{i})")
                hasil.append(f"{layoutname}.addWidget(radio{i})")
                create_radio_handler(objname)

        elif jenis == 'scrollbar':
            print(f'\titem: {jenis}')
            objname = f'scrollbar{index}'
            line = f'{objname} = QScrollBar(self)'
            hasil.append(line)
            maxvalue = 100
            if 'max' in item['attrs']:
                tulisan = item['attrs']['max']
                maxvalue = int(tulisan)
            hasil.append(f"{objname}.setMaximum({maxvalue})")
            hasil.append(f"# {objname}.valueChanged.connect(lambda val: print(val))")
            hasil.append(f"{objname}.sliderMoved.connect(lambda: print({objname}.value()))")
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'slider':
            #tulisan = ''
            #if 'label' in item['attrs']:
            #    tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'slider{index}'
            #line = f'{objname} = QSlider()'
            #line = f'{objname} = QSlider(Qt.Vertical)'
            # sementara hanya horiz slider
            line = f'{objname} = QSlider(Qt.Horizontal)'
            hasil.append(line)
            # default handler
            hasil.append(f"{objname}.setRange(0,100)")
            hasil.append(f"{objname}.setSingleStep(1)")
            hasil.append(f"{objname}.setTickPosition(QSlider.TicksBelow)")
            hasil.append(f"{objname}.setTickInterval(5)")
            hasil.append(f"{objname}.valueChanged.connect(lambda value: print('val:', value))")
            hasil.append(f"{objname}.sliderMoved.connect(lambda value: print('pos', value))")
            hasil.append(f"{objname}.sliderPressed.connect(lambda: print('pressed'))")
            hasil.append(f"{objname}.sliderReleased.connect(lambda: print('released'))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'spin':
            #tulisan = ''
            #if 'label' in item['attrs']:
            #    tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'spin{index}'
            line = f'{objname} = QSpinBox()'
            hasil.append(line)
            # default handler
            hasil.append(f"{objname}.setRange(0,100)")
            hasil.append(f"{objname}.setValue(75)")
            hasil.append(f"# {objname}.setDisplayIntegerBase(10)")
            hasil.append(f"# {objname}.setPrefix('IDR')")
            hasil.append(f"# {objname}.setPrefix('IDR')")
            hasil.append(f"# {objname}.setSuffix('Rupiah')")
            hasil.append(f"{objname}.valueChanged.connect(lambda value: print('val:', value))")
            hasil.append(f"{objname}.textChanged.connect(lambda value: print('text:', value))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'spinfloat':
            print(f'\titem: {jenis}')
            objname = f'spinfloat{index}'
            line = f'{objname} = QDoubleSpinBox()'
            hasil.append(line)
            # default handler
            hasil.append(f"{objname}.setRange(0,100)")
            hasil.append(f"{objname}.setSingleStep(1)")
            hasil.append(f"# {objname}.setPrefix('$')")
            hasil.append(f"# {objname}.setSuffix('c')")
            hasil.append(f"{objname}.valueChanged.connect(lambda value: print('val:', value))")
            hasil.append(f"{objname}.textChanged.connect(lambda value: print('text:', value))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'split':
            '''
            <split[](
                <page
            )
            utk split, page gak perlu label, gak spt tab
            '''
            print(f'\titem: {jenis}')
            objname = f'split{index}'
            orient = 'Qt.Horizontal'
            if 'type' in item['attrs']:
                if item['attrs'] == 'v':
                    orient = 'Qt.Vertical'
            hasil.append(f"{objname} = QSplitter({orient})")
            # for i,record in enumerate(item['children']):
            #     control = 'QLabel' # edit
            #     label = record['attrs']['label']
            #     # tiap page sementara hanya berisi QLabel yg sama tulisannya dg label = judul tab
            #     hasil.append(f"{objname}.addWidget({control}('{label}'))")
            for i,record in enumerate(item['children']):
                # label = record['attrs']['label']
                # kita coba bikin widget+layout utk mengisi tab di sini
                # item = tab, jadi record = page
                hasil.append(f"{objname}_page_{i} = QWidget(self)")
                hasil.append(f"{objname}_pagelayout_{i} = QVBoxLayout({objname}_page_{i})")
                laycode, layname, laycontent = process_layout(output, record, indent=False, provided_layout_name=f'{objname}_pagelayout_{i}')
                print(f"[split] cek indent, laycontent=[{laycontent}]")
                tempres = ['\n'] # jk gak di awali \n selalu terindent 2 tab
                tempres += laycontent.splitlines() # content = multiline string
                formatted_layoutcontent = tabify_contentlist_space(tempres, num_tab=2, space_size=4)
                hasil.append(formatted_layoutcontent)
                hasil.append(f"{objname}.addWidget({objname}_page_{i})") # addTab bukan addWidget
                hasil.append('\n')

            hasil.append(f"# {objname}.setOrientation(Qt.Horizontal)")
            hasil.append(f"# {objname}.setHandleWidth(8)")
            hasil.append(f"# {objname}.setStretchFactor(0, 5)")
            hasil.append(f"# {objname}.setStretchFactor(1, 5)")
            for i in range(len(item['children'])-1):
                hasil.append(f"{objname}.handle({i+1}).setStyleSheet('background: 3px blue;')")

            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'stacked':
            '''
            <stacked[](
                page[label=sebuah tulisan, control=control]
            )
            '''
            print(f'\titem: {jenis}')
            objname = f'stacked{index}'
            layout_objname = f"{objname}_layout"
            navig_objname = f"{objname}_navig"
            hasil.append(f"{objname} = QStackedWidget()")
            hasil.append(f"{layout_objname} = QHBoxLayout()")
            hasil.append(f"{navig_objname} = QListWidget()")
            hasil.append(f"{navig_objname}.currentRowChanged.connect(lambda idx: {objname}.setCurrentIndex(idx))")
            hasil.append(f"{layout_objname}.addWidget({navig_objname})") # kiri = list navigator
            hasil.append(f"{layout_objname}.addWidget({objname})") # kanan = stack
            for i,record in enumerate(item['children']): # iterate page
                control = 'QLabel' # edit
                label = record['attrs']['label']
                # tiap page sementara hanya berisi QLabel yg sama tulisannya dg label = judul tab
                hasil.append(f"{objname}.addWidget({control}('{label}'))")
                hasil.append(f"{navig_objname}.insertItem({i}, '{label}')")
            #hasil.append(f"{objname}.currentChanged.connect(lambda page: print(f'tab {objname} page {{page}}'))")
            #line = f'{layoutname}.addWidget({objname})'
            line = f'{layoutname}.addLayout({layout_objname})'
            hasil.append(line)

        elif jenis == 'stackoverflow':
            tulisan = 'Stackoverflow'
            if 'label' in item['attrs']:
                tulisan = item['attrs']['label']
            print(f'\titem: {jenis}')
            objname = f'stackoverflow{index}'
            hasil.append(f'{objname} = StackOverflow()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            # tambah dependencies ke BrowserWindow utk stackoverflow dan logrocket
            if not 'additional_classes' in output or not 'mainwindow_browser' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'mainwindow_browser': file_content(joinhere(__file__, 'guilang_helper/mainwindow_browser.py'))
                })
            if not 'additional_classes' in output or not 'stackoverflow_getdata' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'stackoverflow_getdata': file_content(joinhere(__file__, 'guilang_helper/stackoverflow_getdata.py'))
                })
            if not 'additional_classes' in output or not 'stackoverflow' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'stackoverflow': file_content(joinhere(__file__, 'guilang_helper/stackoverflow_control.py')).replace('__JUDUL__',tulisan)
                })

        elif jenis == 'tab':
            '''
            <tab[](
                <page[label=sebuah tulisan]
            )
            utk tab, page perlu label, gak spt split
            di sini 'page' tidak/belum diproses di process_layout
            tab hanya menggunakan atribut labelnya saja utk buat QLabel
            '''
            print(f'\titem: {jenis}')
            objname = f'tab{index}'
            hasil.append(f"{objname} = QTabWidget(self)")
            hasil.append(f"# {objname} = QTabWidget(self, tabPosition=QTabWidget.North/South/East/West)")
            for i,record in enumerate(item['children']):
                label = record['attrs']['label'] # label dari page
                # kita coba bikin widget+layout utk mengisi tab di sini
                # item = tab, jadi record = page
                hasil.append(f"{objname}_page_{i} = QWidget(self)")
                hasil.append(f"{objname}_pagelayout_{i} = QVBoxLayout({objname}_page_{i})")
                laycode, layname, laycontent = process_layout(output, record, indent=False, provided_layout_name=f'{objname}_pagelayout_{i}')
                print(f"cek indent, laycontent=[{laycontent}]")
                tempres = ['\n'] # jk gak di awali \n selalu terindent 2 tab
                tempres += laycontent.splitlines() # content = multiline string
                formatted_layoutcontent = tabify_contentlist_space(tempres, num_tab=2, space_size=4)
                hasil.append(formatted_layoutcontent)
                hasil.append(f"{objname}.addTab({objname}_page_{i}, '{label}')") # addTab bukan addWidget
                hasil.append('\n')
            hasil.append(f"{objname}.currentChanged.connect(lambda page: print(f'tab {objname} page {{page}}'))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'table':
            rows=5
            cols=2
            if 'rows' in item['attrs']:
               rows = int(item['attrs']['rows'])
            if 'cols' in item['attrs']:
               cols = int(item['attrs']['cols'])
            print(f'\titem: {jenis}')
            objname = f'table{index}'
            line = f'{objname} = QTableWidget(self)'
            hasil.append(line)

            hasil.append(f"{objname}.horizontalHeader().setStretchLastSection(True)")
            hasil.append(f"{objname}.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)")

            hasil.append(f"{objname}.setColumnWidth(0, 300)")
            hasil.append(f"{objname}.setRowHeight(0, 300)")
            hasil.append(f"{objname}.setColumnWidth(1, 150)")

            # default handler
            default_items = "'satu', 'dua', 'tiga', 'empat', 'lima'"
            if 'items' in item['attrs']:
                #default_items = item['attrs']['items']
                # gara2 config item, utk items harus dipisah /
                pecah_items = item['attrs']['items'].split('/')
                default_items = ', '.join(f"'{thing.strip()}'" for thing in pecah_items)
                rows = len(pecah_items) # ini override rows=... dan tanpa attr rows.
            print(f'\titem: {jenis}', 'default_items:', default_items)
            
            hasil.append(f"{objname}.setRowCount({rows})")
            hasil.append(f"{objname}.setColumnCount({cols})")
            col_labels = [f'"Col {n}"' for n in range(cols)]
            row_labels = [f'"Row {n}"' for n in range(rows)]
            hasil.append(f"{objname}.setHorizontalHeaderLabels([{', '.join(col_labels)}])")
            hasil.append(f"{objname}.setVerticalHeaderLabels([{', '.join(row_labels)}])")

            default_items_aslist = [thing.strip() for thing in default_items.split(',')]
            for i in range(rows):
                for j in range(cols):
                    '''
                    items=1-satu/2-dua/3-tiga
                    '''
                    if j==0:
                        # default_items sudah diapit '' utk masing2 itemnya
                        hasil.append(f"{objname}.setItem({i}, {j}, QTableWidgetItem({default_items_aslist[i]}))")
                    else:
                        hasil.append(f"{objname}.setItem({i}, {j}, QTableWidgetItem(''))")
                # hasil.append(f"{objname}.setItem({i}, {0}, QTableWidgetItem(''))")
                # hasil.append(f"{objname}.setItem({i}, {0}, QTableWidgetItem(''))")
            #hasil.append(f"{objname}.addItems(['satu', 'dua', 'tiga', 'empat', 'lima'])")
            #hasil.append(f"{objname}.currentItemChanged.connect(lambda listitem: print('item changed:', listitem.text()))")
            #hasil.append(f"{objname}.currentTextChanged.connect(lambda value: print('text changed:', value))")
            line = f'{layoutname}.addWidget({objname})'
            hasil.append(line)

        elif jenis == 'tableview':
            
            print(f'\titem: {jenis}')
            objname = f'tableview{index}'
            hasil.append(f'{objname} = TableViewData()')
            hasil.append(f'{layoutname}.addWidget({objname})')
            tableview_content = file_content(joinhere(__file__, 'guilang_helper/tableviewdata.py'))
            if not 'additional_classes' in output or not 'tableview_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'tableview_content': tableview_content
                })

        elif jenis == 'tetris':
            print(f'\titem: {jenis}')
            objname = f'tetris{index}'
            line = f'{objname} = TetrisControl()'
            hasil.append(line)
            hasil.append(f'{layoutname}.addWidget({objname})')
            if not 'additional_classes' in output or not 'tetris_content' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'tetris_content': file_content(joinhere(__file__, 'guilang_helper/tetris_content.py'))
                })

        elif jenis == 'time':
            print(f'\titem: {jenis}')
            objname = f'time{index}'
            line = f'{objname} = QTimeEdit(self)'
            hasil.append(line)
            hasil.append(f'{layoutname}.addWidget({objname})')

        elif jenis == 'windowbrowser':
            # sementara konten dari label=... dipake utk title, text, detailed, informative
            tulisan = item['attrs']['label']
            print(f'\titem: {jenis} => {tulisan}')
            objname = f'btn{index}'
            hasil.append(f'{objname} = QPushButton("{tulisan}")')
            # tambah kode browser di atas
            if not 'additional_classes' in output or not 'mainwindow_browser' in output['additional_classes']:
                if not 'additional_classes' in output:
                    output['additional_classes'] = {}
                output['additional_classes'].update({
                    'mainwindow_browser': file_content(joinhere(__file__, 'guilang_helper/mainwindow_browser.py'))
                })
            hasil.append(f'{objname}_browser = BrowserWindow()')
            # jk button diclick, tampilkan browser
            hasil.append(f"{objname}.clicked.connect(lambda: {objname}_browser.show())")
            # tambahkan button ke layout
            hasil.append(f'{layoutname}.addWidget({objname})')

    if indent:
        layoutcontent = tabify_contentlist_space(hasil, num_tab=2, space_size=4)
    else:
        layoutcontent = '\n'.join(hasil) # agar tidak list of list
    return layoutcode, layoutname, layoutcontent

def process_output(output):
    # layout_content_lines = []
    mainwindow_id = output['window']['id']
    mainwindow_dict = output['items'][mainwindow_id]
    judul = ''
    lebar, tinggi = 800, 600
    windows_attributes = []
    use_qmainwindow, use_dark = False, False
    if 'title' in mainwindow_dict['attrs']:
        judul = mainwindow_dict['attrs']['title']    
    if 'w' in mainwindow_dict['attrs']:
        lebar = mainwindow_dict['attrs']['w']
    if 'h' in mainwindow_dict['attrs']:
        tinggi = mainwindow_dict['attrs']['h']
    if 'trans' in mainwindow_dict['attrs']:
        windows_attributes.append('self.setAttribute(Qt.WA_TranslucentBackground, True)')
    if 'top' in mainwindow_dict['attrs']:
        # windows_attributes.append('self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)')
        windows_attributes.append('self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)')
    if 'qmainwindow' in mainwindow_dict['attrs']:
        use_qmainwindow = True
    if 'dark' in mainwindow_dict['attrs']:
        use_dark = True
    if 'context' in mainwindow_dict['attrs']:
        # tambah context menu
        result = file_content(joinhere(__file__, 'guilang_helper/contextmenu_method.py'))
        if not 'methods' in output:
            output['methods'] = [result]
        else:
            output['methods'].append(result)
        # output['methods'].append()
    for anak in mainwindow_dict['children']:
        if anak['type'] == 'layout':
            layoutcode, layoutname, layoutcontent = process_layout(output, anak)
            hasil.append(layoutcontent)

    print(layoutcode)
    pprint(hasil)

    final_result = kode_output.replace('__LAYOUT__', layoutcode)
    # background_image = 'https://images7.alphacoders.com/617/thumb-1920-617268.jpg'
    # final_result = final_result.replace('__FILEPATH_OR_URL__', background_image)
    
    
    if 'methods' in output:
        # print("ADA METHODS:")
        #methods = '\n'.join(output['methods'])
        methods = tabify_contentlist_space(output['methods'], num_tab=1, space_size=4)
        # print('methods:', methods)        
        final_result = final_result.replace('__METHODS__', methods)
    else:
        final_result = final_result.replace('__METHODS__', '')

    if 'functions' in output:
        print("ADA FUNCTIONS:")
        #methods = '\n'.join(output['methods'])
        methods = tabify_contentlist_space(output['functions'], num_tab=0, space_size=4)
        print('functions:', methods)
        
        final_result = final_result.replace('__FUNCTIONS__', methods)
    else:
        final_result = final_result.replace('__FUNCTIONS__', '')

    if 'additional_classes' in output:
        print("ADA CLASSES:")
        #methods = '\n'.join(output['methods'])
        # methods = tabify_contentlist_space(output['additional_classes'], num_tab=0, space_size=4)
        methods = ''
        for k,v in output['additional_classes'].items():
            methods += '\n' + v + '\n'        
        final_result = final_result.replace('__ADDITIONAL_CLASSES__', methods)
    else:
        final_result = final_result.replace('__ADDITIONAL_CLASSES__', '')

    if judul:
        final_result = final_result.replace('__JUDUL__', judul)
    final_result = final_result.replace('__LEBAR__', str(lebar))
    final_result = final_result.replace('__TINGGI__', str(tinggi))
    windows_attributes = tabify_contentlist_space(windows_attributes, num_tab=2, space_size=4)
    final_result = final_result.replace('__WINDOWS_ATTRIBUTES__', windows_attributes)
    content = '\n'.join(hasil)
    #content = tabify_contentlist_space(hasil, num_tab=2, space_size=4)
    final_result = final_result.replace('__LAYOUT_CONTENT__', content)

    main_layout_code = ['self.setLayout(self.main_layout)']
    if use_qmainwindow:
        main_layout_code = ['self.main_widget = QWidget()', 'self.main_widget.setLayout(self.main_layout)', 'self.setCentralWidget(self.main_widget)']
        # create statusbar
        main_layout_code.append('self.statusBar().showMessage("Status bar here...")')
        main_layout_code.append('self.statusBar().setStyleSheet("background-image : url(status.jpg); background-position: center; color: orange;")')
        # create menubar
        main_layout_code.append('editAct = QAction("&Edit", self)')
        main_layout_code.append('editAct.setShortcut("Ctrl+E")')
        main_layout_code.append('editAct.setStatusTip("Edit own file")')
        main_layout_code.append('editAct.triggered.connect(lambda: os.system(f"code {__file__}"))')        
        main_layout_code.append('editAct.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogDetailedView))')

        main_layout_code.append('exitAct = QAction("E&xit", self)')
        main_layout_code.append('exitAct.setShortcut("Ctrl+X")')
        main_layout_code.append('exitAct.setStatusTip("Exit application")')
        main_layout_code.append('exitAct.triggered.connect(qApp.quit)')
        main_layout_code.append('exitAct.setIcon(QApplication.style().standardIcon(QStyle.SP_BrowserStop))')

        main_layout_code.append('menubar = self.menuBar()')
        main_layout_code.append('file_menu = menubar.addMenu("&File")')

        main_layout_code.append('file_misc_menu = QMenu("&Misc", self)')
        main_layout_code.append('about_action = QAction("About Qt", self)')
        main_layout_code.append('about_action.setStatusTip("Display about Qt")')
        main_layout_code.append('about_action.triggered.connect(QApplication.instance().aboutQt)')
        main_layout_code.append('file_misc_menu.addAction(about_action)')

        main_layout_code.append('file_menu.addAction(editAct)')
        main_layout_code.append('file_menu.addMenu(file_misc_menu)')
        main_layout_code.append('file_menu.addAction(exitAct)')
        # create toolbar
        main_layout_code.append('toolbar = self.addToolBar("Main Toolbar")')
        main_layout_code.append('toolbar.addAction(editAct)')
        main_layout_code.append('toolbar.addAction(exitAct)')
        # copy files
        ocrdir = joiner(sidoarjodir, 'data/ocr-data/')
        filepathlist = prepend_folder_to_filelist(ocrdir, ['bg.jpg', 'bg2.jpg', 'bg3.jpg', 'bg4.jpg', 'bg5.jpg', 'bg6.jpg', 'status.jpg'])
        copy_files_to_tempdir(filepathlist)

    main_layout_code = tabify_contentlist_space(main_layout_code, num_tab=2, space_size=4)
    final_result = final_result.replace('__SET_MAIN_LAYOUT_CODE__', main_layout_code)
    
    dark_code = ['app = QApplication([])']
    if use_dark:
        dark_code.append('set_theme(app)')
    dark_code = tabify_contentlist_space(dark_code, num_tab=1, space_size=4)
    final_result = final_result.replace('__INVOKE_APPLICATION__', dark_code)

    final_result = final_result.replace('__PARENT_WINDOW__', 'QMainWindow' if use_qmainwindow else 'QWidget')

    # copy ke clipboard krn mau exec via clipboard
    pyperclip.copy(final_result)
    print('*'*40)
    print(final_result)
    return final_result

myguicode = """
<window[main, title=Si borokokok teh](
    <layout[type=v,name=mainlayout](
        <layout[type=h,name=forms](
            <form(
                <row[label=pertama,control=edit]
                <row[label=kedua,control=edit]
                <row[label=ketiga,control=edit]
            )
            <scrollbar[max=200]
        )
        <table[items=gaia/wieke/lara/katy]
        <radios(
            <radio[label=radio 1]
            <radio[label=radio 2]
            <radio[label=radio 3]
            <radio[label=radio 4]
            <radio[label=radio terakhir]
        )
        <layout[type=h,name=pages](
            <split[type=h](
                <page[label=pertama,control=edit]
                <page[label=kedua,control=edit]
                <page[label=ketiga,control=edit]
            )
        )
        <layout[type=h,name=pages](
            <tab(
                <page[label=pertama,control=edit]
                <page[label=kedua,control=edit]
                <page[label=ketiga,control=edit]
            )
        )
        <layout[type=h,name=pages](
            <stacked(
                <page[label=pertama,control=edit]
                <page[label=kedua,control=edit]
                <page[label=ketiga,control=edit]
            )
        )
        <cal[label=isi kalendar kah]
        <layout[type=h,name=buttons](
            <label[label=this is just a label]
            <button[label=hello 1]
            <button[label=hello 2]
            <button[label=hello 3]
        )
        <layout[type=h,name=editor](
            <edit[label=an editor for you bisa tekan enter]
            <editmulti[label=multiline editor gak bisa tekan enter]
        )
        
        <layout[type=h,name=waktu](
            <date[label=ignore date]
            <time[label=ignore time]
            <datetime[label=ignore datetime]
        )
        <layout[type=h, name=combien](
            <check[label=a chebox]
            <combo[label=ignore combo]
            <radio[label=radio 1]
            <radio[label=radio 2]
            <radio[label=radio 3]
        )
        <layout[type=h,name=gerak](
            <dial[label=ignore dial]
            <progress[label=ignore progress]
            <list[label=ignore list,items=gaia/wieke/lara/katy]
            <lcd[label=2024]
            <slider[label=ignore slider]
        )
        <layout[type=h,name=spiner](
            <spin[label=spin]
            <spinfloat[label=spinfloat]
        )
        <layout[type=h,name=horizle](
            <button[label=di dalam]
            <check[label=another checkbox]
            <button[label=di dalam 2]
            <button[label=di dalam 3]
            <message[label=ini pesan untuk keluar]
            <input[label=masukkan apa saja]
            <fontinput[label=input font]
            <fileinput[label=input file]
        )
    )
)
"""

def guilang_internal(code=myguicode):
    reset()
    process_language(code, current_handler=mygui_handler)
    #process_language(code)
    print('*'*40)
    pprint(output)

def guilang(code=myguicode, returning=False):
    guilang_internal(code)
    content = process_output(output)
    # input(f'ready to exec {content[:100]}...>> ')
    # exec(content)
    if returning:
        return content

"""
TODO:
sementara stacked/tab/form dll belum rekursif handle item...
sedangkan item baru dihandle di layout v/h.
jadi harus ada pemisahan item dg handle layout...kembalian item nanti di addWidget di layout
juga sama halnya utk stacked/tab/form
"""
