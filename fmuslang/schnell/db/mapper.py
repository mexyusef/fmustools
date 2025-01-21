import re

# input_mapper digunakan hanya jk dia kosong...empty result...
# bisa juga digunakan
# stlh dapat result []
# sblm proses cari sekalian
input_mapper = {
    "ab": "appbar",
    "ax1": "mainaxis",
    "ax2": "crossaxis",
    "c": "column",
    "r": "row",
    "cls": "class",
    "kelas": "class",
    "clr": "color",
    "ctr": "center",
    "ctl": "control",
    "cnt": "container",
    "dvd": "divider",
    "ei": "edgeinsets",
    # terpanjang dulu
    # jangan masukkan fun
    # misal fungsi -> func
    # selanjutnya ketemu fun=>func -> menjadi (fun)c => (func)c => funcc
    "fn": "func",
    "fungsi": "func",
    # jangan h saja, nanti semua h* diubah
    # skrg dah bener dg re.sub, alih2 .replace
    "h": "height",
    "w": "width",
    "icb": "iconbutton",
    "img": "image",
    "iw": "inkwell",
    "mq": "mediaquery",
    "nw": "network",
    # panjang duluan dari pendek
    # agar pendek gak memakan sub dari panjang
    "szb": "sizedbox",
    "sz": "size",
    "scsv": "singlechildscrollview",
    "sctv": "singlechildscrollview",
    "stba": "slivertoboxadapter",
    # jangan sesuai sequence, style jangan st atau sty tapi hrs stl dll
    # yg gak berurut
    "sts": "status",
    "stl": "style",  # bs bentrok dg c++ stl
    "txt": "text",
    "xp": "expanded",
    "xt": "extended",
}


def map_input(code):
    for k, v in input_mapper.items():
        # code = code.replace(k, v)
        # print('result now:', code)
        code = re.sub(rf"\b{k}\b", v, code)

    return code
