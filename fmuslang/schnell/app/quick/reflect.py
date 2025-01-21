# utk reflect state dari fmus
# agar bisa diakses dari fmus itu sendir, misal dg fm//fmus>...
# utk bisa gawe, kita mau masukkan semua ke @d/1stop, exec dg fm//run>* @d/1stop
# change __PWD
# change __CURDIR/__FILE
import importlib as IL
from schnell.app.fmusutils import fmus
from schnell.app.printutils import indah4


def change__pwd():
    """
    ini bisa dg os.chdir()?
    """
    pass


def change__curdir():
    """
    ini bisa dg set_dir_template()?
    """
    pass


def change__file():
    """
    ini bisa dg set_file_dir_template()?
    """
    pass


def status():
    pass


# module_prefix = 'app.'
module_prefix = ''  # harus app.windowsutils dsb
def panggil(filename, functionname, *args, **kwargs):
    """
    /ref)schnell.app.githubutils/get_repos_from_githubusername/app-generator
    
    bisa panggil
    misal dari app.notifutils pengen panggil notifpy(judul, isi)

    ternyata ada 3 tempat utk *args: panggil, params, internal
    tp utk kwargs blm dicoba
    """

    # indah4(f'''[reflect]
    # args = {args}, jenis {type(args)}
    # kwargs = {kwargs}, jenis {type(kwargs)}
    # ''', warna='cyan')

    module = IL.import_module(f'{module_prefix}{filename}')
    if args:
        getattr(module, functionname)(*args)
    elif kwargs:
        getattr(module, functionname)(**kwargs)
    else:
        getattr(module, functionname)()
