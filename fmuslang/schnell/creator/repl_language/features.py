# from schnell.app.dirutils import joiner
from schnell.app.fileutils import file_lines
from schnell.app.printutils import print_list_warna
# from schnell.app.utils import env_get
# from schnell.app.envvalues import sidoarjo_relative_normalized
from constants import FEATUREFILE, LALANGFILE


def features(filter=None):
    thelist = file_lines(FEATUREFILE, skip_emptylines=True)
    if filter:
        thelist = [item for item in thelist if filter.lower() in item.lower()]
    print_list_warna(thelist, ganjil='white', genap='cyan', start=1, extra_suffix='\n')


def lalang(filter=None):
    thelist = file_lines(LALANGFILE, skip_emptylines=True)
    if filter:
        thelist = [item for item in thelist if filter.lower() in item.lower()]
    print_list_warna(thelist, ganjil='white', genap='cyan', start=1, extra_suffix='\n', no_index=True)
