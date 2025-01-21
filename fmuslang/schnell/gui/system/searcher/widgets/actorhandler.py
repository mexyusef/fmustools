import os, sys
from dotenv import load_dotenv

# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sidoarjodir = os.environ['ULIBPY_ROOTDIR']
# sys.path.extend([sidoarjodir, schnelldir])
from pathlib import Path
sidoarjodir = str(Path(__file__).resolve().parent.parent)
sys.path.append(sidoarjodir)

# from actorwidget import actor_lines, ACTOR_FILE
from schnell.gui.system.searcher.widgets.actorwidget import actor_lines, ACTOR_FILE


def actor_handler(start='u', debug=True):
    kembali = []
    start = start.strip()
    # if debug:
    #     print(f"start: {start}.")
    if start=='edit':
        os.system(f"vscode {ACTOR_FILE}")
    elif start .startswith('~'):
        cari = start.removeprefix('~')
        kembali = [f'{i}. {item}' for (i,item) in enumerate(actor_lines) if cari in item]
        if not kembali:
            kembali = [f'"{cari}" not found.']
    elif start.startswith(':'):
        # print('=>', start)
        actor_no = start.removeprefix(':').strip()
        # print('=>', actor_no)
        if actor_no.isdigit():
            actor_no = int(actor_no)
            # print('=0=>', actor_no, 'panjang:', len(actor_lines))
            kembali = [actor_lines[actor_no]]
            # print('=1=>', kembali)
        else:
            kembali = [f'"{actor_no}" not a digit.']
            # print('=2=>', kembali)
        # print('==>', kembali)
    elif isinstance(start, str) and not start.isdigit() and len(start)==1: # hanya b, u, dsb
        angka = ord(start) - ord('a')
        #   print(angka * 25)
        mulai = angka*25
        for i in range(25):
            tabs = (i % 5)*'\t'
            bentuk = tabs + actor_lines[i+mulai].strip()
            if debug:
                print(bentuk)
            kembali.append(bentuk)
    else:
        if not start.isdigit():
            return f'[{start}] is not a digit'
        # jk misalnya 600, 675, dsb
        mulai = int(start)
        for i in range(25):
            tabs = (i % 5)*'\t'
            bentuk = tabs + actor_lines[i+mulai].strip()
            if debug:
                print(bentuk)
            kembali.append(bentuk)
    # if debug:
    #     print(f'kembali: {kembali}.')
    return '\n'.join(kembali)


if __name__ == '__main__':
    res = actor_handler('b', debug=False)
    print(res)
