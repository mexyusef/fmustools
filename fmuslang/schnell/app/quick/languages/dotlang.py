import os, sys, traceback
from pprint import pprint as pp
from uuid import uuid4 as u4
import sys
from pathlib import Path
sidoarjodir = Path(__file__).resolve().parent.parent.parent.parent.parent
#                              file     langs quick app     sch   sid
sys.path.append(sidoarjodir)

# from schnell.app.fileutils import file_write
# from schnell.app.printutils import indah4
# from schnell.app.transpiler.frontend.main import process_language
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
    ispohon,
    istoken,
    beranak,
    sebanyak,
    jumlahanak,
)
from schnell.langs import base_grammar

import schnell.vendor.lark as lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)
from schnell.vendor.lark.indenter import Indenter
import click
import graphviz


class TheProcessor(InlineTransformer):
	def dot_program(self, *item_lines):
		return item_lines


dot_language = f"""
dot_program: program_config? statement ("|" statement)*
//statement: walk ("." walk)*
//walk: source "." targets
statement: source "." destination
destination: targets
    | target ("." target)* 
targets: target ("," target)*
source: node
target: node
node: name node_config?
node_config: "[" config_item ("," config_item)* "]"
//program_config: node_config
program_config: "/" config_item ("," config_item)* "/"
config_item: HURUF_CONFIG_ITEM
name: HURUF_DIGIT_SPACE_NONDOT
HURUF_DIGIT_SPACE_NONDOT: ("_"|LETTER|DIGIT|"\\"") ("_"|LETTER|DIGIT|" "|"\\"")*
HURUF_CONFIG_ITEM: ("_"|LETTER|DIGIT|"\\"") ("_"|LETTER|DIGIT|" "|"="|"\\"")*

{base_grammar}
"""
# https://click.palletsprojects.com/en/7.x/utils/

def p(*text, **kwargs):
    text = ' '.join([str(item) for item in text])
    if 'fg' not in kwargs:
        kwargs['fg'] = 'green'
    click.echo(click.style(text, **kwargs))

run_config = {
    'panah': '->', # -> atau --
    'graph': 'digraph', # digraph atau graph
}

dot_output = {}
dot_config = {}

def reset():
    global dot_output, dot_config
    dot_output.clear()
    dot_config.clear()

def handle_node_config(node, dstname):
    if len(anak(node))==2:
        node_config = anak(node)[1]

        for configitem in anak(node_config):
            #configitem = anak(node_config)[0]
            nilai = token(configitem)
            destname_suffix=''
            if nilai.startswith('fill'):
                p('node fill',fg='yellow')
                if nilai.count('=')==1:
                    p('node fill, 1 =',fg='yellow')
                    # fill=blue
                    _,warna = nilai.split('=')
                    sisa=''
                else:
                    p('node fill, multiple =',fg='yellow')
                    # fill=blue,shape=Mdiamond,fontsize=10
                    fillwarna, sisa = nilai.split(',',1)
                    _,warna=fillwarna.split('=')
                destname_suffix = f"{dstname} [style=filled, fillcolor={warna}{sisa}]"
                if not destname_suffix in dot_config:
                    dot_config[destname_suffix] = []
                else:
                    original = dot_config[destname_suffix]
                    original = original.replace(']', f", style=filled, fillcolor={warna}]")
                    #del dot_config[destname_suffix]
                    dot_config[original] = []
            else:
                p('node NON fill',fg='yellow')
                if not destname_suffix in dot_config:
                    dot_config[f"{dstname} [{nilai}]"] = []
                else:
                    original = dot_config[destname_suffix]
                    original = original.replace(']', f", {nilai}]")
                    #del dot_config[destname_suffix]
                    dot_config[original] = []

def dot_handler(tree):
    currentsource = ''

    p('[dot_handler]', data(tree), fg='red')

    if data(tree) == 'program_config':
        for dahan in anak(tree):
            # if data(dahan) == 'node_config':
            for daun in anak(dahan):
                if istoken(daun):
                    daun = str(daun)
                    # if '=' in daun:
                    #     k,v = daun.split('=',1)
                    #     dot_config[k]=[v]
                    dot_config[daun]=[]
                elif data(daun)=='config_item':
                    nilai = token(daun)
                    if nilai.startswith('fill'):
                        _,warna=nilai.split('=')
                        kunci = f'node[style=filled, fillcolor={warna}]'
                        dot_config[kunci]=[]
                    else:
                        kunci = f'node[{nilai}]'
                        if nilai.startswith('rankdir'):
                            '''
                            utk berbagai config utk non-node (global) spt 
                            rankdir="TB" atau rankdir="LR"
                            rankdir="BT" dan "RL"
                            '''
                            kunci = f'{nilai}'
                        dot_config[kunci]=[]
        return

    for item in anak(tree):
        jenis = data(item)
        p(jenis, fg='blue')
        if jenis == 'source':
            '''
            source
                node
                    name      indonesia
                    node_config
                        config_item     fill=red
            '''
            node = anak(item)[0] # anak selalu berikan list
            nama = anak(node)[0]
            currentsource = token(nama)
            p(' src:', currentsource)
            handle_node_config(node, currentsource)
        elif jenis == 'destination':
            destinations = [] # utk a->b->c->d kita kumpulkan dulu
            for tujuan in anak(item):
                jenistujuan = data(tujuan)
                # utk target masih salah...harusnya src -> dst -> dst -> dst
                if jenistujuan == 'target':
                    node = anak(tujuan)[0]
                    nama = anak(node)[0]
                    dstname = token(nama)
                    p(f' tujuan {jenistujuan}:', dstname, f'output: {currentsource} -> {dstname}')
                    destinations.append(dstname)
                    handle_node_config(node, dstname)
                elif jenistujuan == 'targets':
                    '''
                      destination
                        targets <- tujuan
                          target <- cucu
                            node <- node
                              name	d <- nama + dstname
                              node_config
                                config_item	fill=blue
                                config_item	k=v
                    '''
                    for cucu in anak(tujuan):
                        node = anak(cucu)[0]
                        nama = anak(node)[0]
                        dstname = token(nama)
                        p(f' tujuan {jenistujuan}:', dstname, f'output: {currentsource} -> {dstname}')
                        handle_node_config(node, dstname)
                        key = f'{currentsource} -> {dstname}'
                        # if len(anak(node))==2:
                        #     node_config = anak(node)[1]
                        #     for configitem in anak(node_config):
                        #         #configitem = anak(node_config)[0]
                        #         nilai = token(configitem)
                        #         destname_suffix=''
                        #         if nilai.startswith('fill'):
                        #             # p('node fill',fg='yellow')
                        #             if nilai.count('=')==1:
                        #                 p('node fill, 1 =',fg='yellow')
                        #                 # fill=blue
                        #                 _,warna = nilai.split('=')
                        #                 sisa=''
                        #             else:
                        #                 # p('node fill, multiple =',fg='yellow')
                        #                 # fill=blue,shape=Mdiamond,fontsize=10
                        #                 fillwarna, sisa = nilai.split(',',1)
                        #                 _,warna=fillwarna.split('=')
                        #             destname_suffix = f"{dstname} [style=filled, fillcolor={warna}{sisa}]"
                        #             if not destname_suffix in dot_config:
                        #                 dot_config[destname_suffix] = []
                        #             else:
                        #                 original = dot_config[destname_suffix]
                        #                 original = original.replace(']', f", style=filled, fillcolor={warna}]")
                        #                 #del dot_config[destname_suffix]
                        #                 dot_config[original] = []
                        #         else:
                        #             # p('node NON fill',fg='yellow')
                        #             if not destname_suffix in dot_config:
                        #                 dot_config[f"{dstname} [{nilai}]"] = []
                        #             else:
                        #                 original = dot_config[destname_suffix]
                        #                 original = original.replace(']', f", {nilai}]")
                        #                 #del dot_config[destname_suffix]
                        #                 dot_config[original] = []

                        if key not in dot_output:
                            dot_output[key] = []
                        else:
                            pass
            if destinations:
                dsts = ' -> '.join(destinations)
                key = f'{currentsource} -> {dsts}'
                if key not in dot_output:
                    dot_output[key] = []

def process_dot_language(code):
    try:
        pre_parser = Lark(dot_language, start='dot_program')
        parser = pre_parser.parse
        parsed_tree = parser(code)
        instructions = TheProcessor().transform(parsed_tree)
        for insn in instructions:
            print(insn.pretty())
            dot_handler(insn)
    except Exception as err:
        print(err)
        trace = traceback.format_exc()
        print(trace)

kode_sumber = '''
graphviz.Source("""
digraph MyGraph {
  rankdir=LR
__TEMPLATE_CONFIG__
__TEMPLATE_CODE__
}
""")
'''

kode_sumber_text = """
digraph MyGraph {
  rankdir=LR
__TEMPLATE_CONFIG__
__TEMPLATE_CODE__
}
"""

def opreks():
    templatecodes = []
    for line in dot_output.keys():
        templatecodes.append(line)
    content = '\n'.join(templatecodes)
    hasil = kode_sumber.replace('__TEMPLATE_CODE__',content)
    config = ''
    templateconfs = []
    for item in dot_config.keys():
        templateconfs.append(item)
    config = '\n'.join(templateconfs)
    hasil = hasil.replace('__TEMPLATE_CONFIG__', config)
    return hasil

dot_code = """[shape=box,color=red,fill=yellow,fontsize=24]
a.b.c[shape=triangle].d.e[shape=oval]
|
b.d[fill=blue,shape=Mdiamond]
|
k.telor[shape=egg],bintang[shape=star],terakhir
"""

# https://www.programcreek.com/python/example/104477/graphviz.Source
def contoh():
    process_dot_language(dot_code)
    # process_dot_language("""a.b.c.d.e|b.d|k.l,m,n""")
    pp(dot_output)
    print('*'*40)
    pp(dot_config)
    res = opreks()
    pp(res)
    eval(res)

def dotlang(code=dot_code, filepath=None):
    reset()
    process_dot_language(code)

    # process output
    templatecodes = []
    for line in dot_output.keys():
        templatecodes.append(line)
    content = '\n'.join(templatecodes)
    hasil = kode_sumber_text.replace('__TEMPLATE_CODE__', content)
    config = ''
    templateconfs = []
    for item in dot_config.keys():
        templateconfs.append(item)
    config = '\n'.join(templateconfs)
    hasil = hasil.replace('__TEMPLATE_CONFIG__', config)

    print('*'*80)
    pp(dot_output)
    print('*'*40)
    pp(dot_config)
    print('*'*40, hasil)
    print(hasil)

    graph = graphviz.Source(hasil)
    graph.format = 'png' # ext[1:]
    graph.view('dotlang', cleanup = True)
    if filepath:
        graph.render(filepath)


kode_output_image = """
import graphviz
def mydotlang(hasil, filepath=None):
    graph = graphviz.Source(hasil)
    graph.format = 'png' # ext[1:]
    graph.view('dotlang', cleanup = True)
    if filepath:
        graph.render(filepath)

hasil = '''
__HASIL__
'''
mydotlang(hasil)
"""
# def process_dotlang2(dout_output, filepath=None, returning=False):
#     # process output
#     templatecodes = []
#     for line in dot_output.keys():
#         templatecodes.append(line)
#     content = '\n'.join(templatecodes)
#     hasil = kode_output_image.replace('__TEMPLATE_CODE__', content)
#     config = ''
#     templateconfs = []
#     for item in dot_config.keys():
#         templateconfs.append(item)
#     config = '\n'.join(templateconfs)
#     hasil = hasil.replace('__TEMPLATE_CONFIG__', config)

#     print('*'*80)
#     pp(dot_output)
#     print('*'*40)
#     pp(dot_config)
#     print('*'*40, hasil)
#     print(hasil)

def dot_program():
    templatecodes = []
    for line in dot_output.keys():
        templatecodes.append(line)
    content = '\n'.join(templatecodes)
    hasil = kode_sumber_text.replace('__TEMPLATE_CODE__',content)
    config = ''
    templateconfs = []
    for item in dot_config.keys():
        templateconfs.append(item)
    config = '\n'.join(templateconfs)
    hasil = hasil.replace('__TEMPLATE_CONFIG__', config)
    return hasil


def process_dotlang2(code=dot_code, returning=False):
    reset()
    process_dot_language(code)
    # pp(imgoutput)
    # if returning:
    #     return process_dotlang2(imgoutput, filepath=filepath, returning=True)
    # process_dotlang2(imgoutput, filepath=filepath, returning=False)
    hasil = dot_program()
    program = kode_output_image.replace('__HASIL__', hasil)
    if returning:
        return program
    print(f'\n\n{"*"*20}\n')
    print(program)


"""TODO:
digraph MyGraph {
  rankdir=LR
shape=box
a -> b -> c
}

utk shape=box, ini adlh yg hrs diapply ke semua node.
jadi harus ada
a [shape=box]
...
c [shape=box]
"""
