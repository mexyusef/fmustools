# import os, sys
from pprint import pprint as pp
from uuid import uuid4 as u4
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([schnelldir, '..'])
import sys
from pathlib import Path
sidoarjodir = Path(__file__).resolve().parent.parent.parent.parent.parent
#                              file     langs quick app     sch   sid
sys.path.append(sidoarjodir)

# print(schnelldir)
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
from schnell.app.dirutils import joiner
from schnell.app.fileutils import file_write
from schnell.app.utils import env_get


kode_chart = """
import matplotlib
# matplotlib.use('agg')
# matplotlib.use('TkAgg')
import os
os.environ['QT_API'] = 'PyQt5'

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
plt.rcParams["figure.autolayout"] = True
warna_untuk_piechart = sns.color_palette('pastel')[0:5]

__TEMPLATE_CODE__


"""

output = {}

def reset():
    global output
    output.clear()

def intercept(value):
    # {'attrs': ['x=1,2,3,4,5', 'y=10,20,30,40,50'], 'type': 'barchart'}}}
    # x=1/2/3/4/5 (bahasa)
    # x=1,2,3,4,5 (bahasa2)
    if '..' in value:
        start, end = map(int, value.split(".."))
        lst = list(range(start, end+1))
        value = ','.join(map(str, lst))
    # kita mau variasi x=1..5, x=rnd:i:3 utk 2,4,9, rnd:s:5 utk F,C,K,U,B
    return value

def charthandler(tree, parent=''):
    namaparent = ''
    itemid = ''
    for item in anak(tree):
        jenis = data(item)
        print(jenis)
        if jenis == 'element_name':
            nama = token(item)
            # print('  ', nama, f'berortu [{parent}]')
            namaparent = token(item) # agar bisa diakses dari element_config di bawah
            itemid = str(u4())
            if nama == 'canvas':
                print('canvas')
                output['canvas'] = {}
            elif nama == 'piechart':
                print('  pie')
            elif nama == 'barchart':
                print('  bar')
            elif nama == 'linechart':
                print('  line')
            elif nama == 'donutchart':
                print('  donut')
            elif nama == 'map':
                print('  map')
        elif jenis == 'element_children':
            for bagian in anak(item):
                for bagianlagi in bagian:
                    #print('  ', type(bagianlagi), '=>', bagianlagi, '=>', data(bagianlagi))
                    if data(bagianlagi) == 'declarative_element':
                        charthandler(bagianlagi)
        elif jenis == 'element_config':
            for tupleitem in anak(item):
                jenis2 = data(tupleitem)
                if jenis2 == 'item_key_value':
                    k,v='',''
                    for anaktupleitem in anak(tupleitem):
                        jenis3 = data(anaktupleitem)
                        if jenis3 == 'item_key':
                            k = token(anaktupleitem)
                        elif jenis3 == 'item_value':
                            # x=1/2/3/4/5 (bahasa)
                            # x=1,2,3,4,5 (bahasa2)
                            # kita mau variasi x=1..5, x=rnd:i:3 utk 2,4,9, rnd:s:5 utk F,C,K,U,B
                            v = token(anaktupleitem)

                    # attr barchart/5ecd6411-4b86-4f96-8c1a-e71b9737859f k=v => x=1,2,3,4,5
                    # attr barchart/5ecd6411-4b86-4f96-8c1a-e71b9737859f k=v => y=10,20,30,40,50
                    print(f'  attr {namaparent}/{itemid} k=v => {k}={v}')

                    if namaparent=='canvas':
                        pass
                    else:
                        # {'attrs': ['x=1,2,3,4,5', 'y=10,20,30,40,50'], 'type': 'barchart'}}}
                        # intercept v...
                        v = intercept(v)
                        if not itemid in output['canvas']:
                            output['canvas'][itemid] = {'type':namaparent, 'attrs': [f"{k}={v}"]}
                        else:
                            output['canvas'][itemid]['attrs'].append(f"{k}={v}")


def process_output(output, returning=False, pemisah_values='/'):
    templatecodes = []

    if 'canvas' in output:
        for _id, kamus in output['canvas'].items():
            if kamus['type'] in ['barchart','linechart','piechart','donutchart']:
                mode = 'B'
                chartname = 'chartname = "bar1.png"'
                chartfunction = 'sns.barplot(x=x, y=y)'
                if kamus['type']=='linechart':
                    mode = 'L'
                    chartname = 'chartname = "line1.png"'
                    chartfunction = 'sns.lineplot(x=x, y=y)'
                elif kamus['type']=='piechart':
                    mode = 'P'
                    chartname = 'chartname = "pie1.png"'
                    chartfunction = "plt.pie(y, labels = x, colors = warna_untuk_piechart, autopct='%.0f%%')"
                elif kamus['type']=='donutchart':
                    mode = 'D'
                    chartname = 'chartname = "donut1.png"'
                    chartfunction = "plt.pie(y, labels = x, autopct='%.0f%%', wedgeprops={'width': 0.5})"

                attrs = kamus['attrs']
                xlabels = []
                ylabels = []
                for attr in attrs:
                    if attr.startswith('x='):
                        attr = attr.removeprefix('x=')
                        x = attr.split(pemisah_values)
                        x = [f'"{item}"' if not item.isdigit() else item for item in x]
                        xlabels = x
                        x = '[' + ', '.join(x) + ']'
                        templatecodes.append(f"x = {x}")
                    elif attr.startswith('y='):
                        attr = attr.removeprefix('y=')
                        y = attr.split(pemisah_values)
                        y = [f'"{item}"' if not item.isdigit() else item for item in y]
                        ylabels = y
                        y = '[' + ', '.join(y) + ']'
                        templatecodes.append(f"y = {y}")

                # # Find the length of the longer list
                # max_len = max(len(xlabels), len(ylabels))
                # # Pad the shorter list with zeros or empty strings, depending on the type of the elements
                # if len(xlabels) < max_len:
                #     xlabels += [0 if isinstance(xlabels[0], int) else '']*(max_len-len(xlabels))
                # if len(ylabels) < max_len:
                #     ylabels += [0 if isinstance(ylabels[0], int) else '']*(max_len-len(ylabels))

                #templatecodes.append(f"sns.{tipechart}(x=x, y=y)")
                templatecodes.append(chartname)
                templatecodes.append(chartfunction)
                templatecodes.append(f"plt.title(chartname)")
                templatecodes.append(f"plt.savefig(chartname)")
                templatecodes.append(f"plt.show()")
                templatecodes.append(f"\n\n")

    print('[app.quick.languages.chartlang] templatecodes:', templatecodes)
    a = '\n'.join(templatecodes)
    content = kode_chart.replace('__TEMPLATE_CODE__', a)
    # print(content)
    # file_output = joiner(env_get('ULIBPY_DATA_FOLDER_ABS'), 'chart.py')
    # indah4(f'{file_output}',warna='cyan')
    # file_write(file_output, content)
    if returning:
        return content
    exec(content)
    # import matplotlib.pyplot as plt
    # plt.show()



# TODO:
# ganti bentuk ke x=A,B,C,D,E|y=70,40,90,20,50 juga x=1:5 utk range
# masalahnya ini bagian dari decl language
chartlang = """
<canvas[cols=5](
    <piechart[x=A/B/C/D/E,y=70/40/90/20/50]
    <barchart[x=1/2/3/4/5,y=10/20/30/40/50]
    <linechart[x=1/2/3/4/5,y=10/20/30/40/50]
    <donutchart[x=A/B/C/D/E,y=70/40/90/20/50]
    <map
)
"""

# C:/Users/usef/work/sidoarjo/schnell/app/transpiler/frontend/bahasa2.py
# [a,b,c/1,2,3] alih2 [a/b/c,1/2/3]
from schnell.app.transpiler.frontend.bahasa2 import bahasa as decl_grammar

def chartlang(code=chartlang, returning=False, bahasa2=False):
    reset()
    if bahasa2:
        process_language(code, current_handler=charthandler, language_grammar=decl_grammar)
        pp(output)
        content = process_output(output, returning=returning, pemisah_values=',')
    else:
        process_language(code, current_handler=charthandler)
        pp(output)
        content = process_output(output, returning=returning)
    
    if returning:
        return content
