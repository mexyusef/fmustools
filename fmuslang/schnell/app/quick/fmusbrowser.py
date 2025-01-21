from schnell.app.dirutils import sfiles, files_filter, isabsolute, joiner
from schnell.app.fmusutils import run_fmus_for_file
from schnell.app.printutils import print_list_warna, indah4
from .common import folder_expand

"""
fmusbrowser
"""

def fmusbrowser(request):
    """
    terima request=filepath
    """
    filepath = request
    if not request:
        filepath = '@c/appgen'
    if not isabsolute(filepath):
        filepath = folder_expand(filepath, prefix_with_rootdir=True)
    daftar_file = files_filter(filepath, ['.fmus', '.mk'])
    yn = 1
    while yn:
        print_list_warna(daftar_file, 'white', 'cyan', start=1)
        indah4('Masukkan pilihan, Enter utk keluar:', newline=False)
        yn = input(' ')
        if yn:
            nilai = int(yn)
            if 1 <= nilai <= len(daftar_file):
                akses = joiner(filepath, daftar_file[nilai-1])
                print('run fmus utk', akses)
                run_fmus_for_file(akses)
