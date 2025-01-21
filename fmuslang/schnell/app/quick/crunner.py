"""
ini adlh coordinator runner

paling sering kita gunakan
from schnell.app.fmusutils import fmus
from schnell.app.fmusutils import run_fmus_from_coordinator, get_rootnode
	RootNode = get_rootnode(csvcode)
	generator = provider_to_location[provider] (RootNode)
	generator.generate()
	filepath = generator.output()
	baris_entry = 'index/fmus'
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	fmus.set_file_dir_template(filepath)
	fmus.process(program)
perlu manfaatkan
from schnell.app.utils import import_module

ah ini di blitz
		RootNode = get_rootnode(csvcode)
		run_fmus_from_coordinator(language_to_handler[language], [RootNode, fmus_filename])
def run_fmus_from_coordinator(coordinator, coordinator_param_list, baris_entry = 'index/fmus'):
	generator = coordinator (*coordinator_param_list)
	generator.generate()
	filepath = generator.output()	
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	fmus.set_file_dir_template(filepath)
	fmus.process(program)

that's it kita dah punya...
ternyata sudah kasih info di info.txt

from schnell.app.utils import import_module
generator_module = import_module(program_config['modulename'], program_config['generator'])
generator = generator_module.Coordinator(RootNode)
generator.generate()

==========================
mending spt ini:
user diminta masukkan csvcode
RootNode = get_rootnode(csvcode)
coordinator = import_module('fslang/path/to/folder', joiner(basedir, 'fslang/path/to/folder'))
run_fmus_from_coordinator(coordinator, [RootNode, 'index-input.mk'], 'index/fmus')
==========================
kita klasifikasikan juga:
- yg masih minta csvcode dummy
- 

dari grammar:
	| "R" 			-> fslang_z_quick_react		// u -e/R/1
	| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1
	| "N" 			-> fslang_z_quick_node		// u -e/N/1
	...
if jenis .startswith ('fslang_'):
    kembali.update({
        'modulename'  : jenis,                                # fslang_path_to_target
        'generator'   : joiner(workabsdir, '__init__.py'),    # lokasi Coordinator        
    })
import_module(fslang_path_to_target, lokasi Coordinator)
"""
from schnell.app.dirutils import joiner, pemisah_direktori, isdir, isfile, sdirs, sfiles
from schnell.app.fmusutils import run_fmus_from_coordinator, get_rootnode, fmus
from schnell.app.printutils import indah4, print_list_warna
from schnell.app.stringutils import replace_non_alpha, newlinify
from schnell.app.utils import import_module, env_get, perintahsp_simple, platform, linuxify, perintah
from schnell.app.fileutils import file_content
from constants import sidoarjodir as rootdir
from .common import folder_expand as expand, pohon, filepath, barisentry



def crunner(rawcode):
    r"""
    /run>path|csvcode
    schnell\app\transpiler\frontend\fslang
    @s
    @sa
    @sat
    @satf
    @satff

    __PWD,d
        /run>@satff\flask
    """
    abspath_or_relpath, csvcode = rawcode.split('|', 1)

    indah4(f'''[crunner]
    rawcode = {rawcode}
    csvcode = {csvcode}
    path = {abspath_or_relpath}
    ''', warna='cyan')

    RootNode = get_rootnode(csvcode)
    # print('crunner, relpath:', abspath_or_relpath)
    absolute_path = expand(abspath_or_relpath)
    absolute_path = joiner(absolute_path, '__init__.py')
    # print('crunner, abspath:', absolute_path)
    module_name = replace_non_alpha(absolute_path).lower()
    if not absolute_path.startswith(rootdir):
        absolute_path = joiner(rootdir, absolute_path)

    indah4(f'''[crunner]
    abspath_or_relpath = {abspath_or_relpath}
    absolute_path   = {absolute_path}
    csvcode         = {csvcode}
    module_name     = {module_name}
    ''', warna='magenta')
    
    coordinatormodule = import_module(module_name, absolute_path)
    kwargs = {
        'RootNode': RootNode,
        'project_dir': '__PWD/__INPUT__',
        # 'filename': 'index-input.mk',
    }
    # run_fmus_from_coordinator(coordinatormodule.Coordinator, [RootNode, filepath], baris_entry=barisentry)
    run_fmus_from_coordinator(coordinatormodule.Coordinator, baris_entry=barisentry, coordinator_kwargs=kwargs)
    # import importlib
    # coordinator = importlib.import_module(coordinatormodule)
    # coordinatorclass = getattr(coordinator, 'Coordinator')
    # run_fmus_from_coordinator(coordinatorclass, [RootNode, filepath], barisentry)


def lister(code):
    dirpath = expand(code)
    if not dirpath.startswith(rootdir):
        dirpath = joiner(rootdir, dirpath)
    if isdir(dirpath):
        lihat = sdirs(dirpath)
        print_list_warna(lihat)


def filers(code):
    dirpath = expand(code)
    if not dirpath.startswith(rootdir):
        dirpath = joiner(rootdir, dirpath)
    print('filers:', dirpath)
    if isdir(dirpath):
        lihat = sfiles(dirpath)
        print_list_warna(lihat)


def treelers(code):
    dirpath = expand(code)
    if not dirpath.startswith(rootdir):
        dirpath = joiner(rootdir, dirpath)
    if isdir(dirpath):
        dirpath = linuxify(dirpath)
        perintahsp_simple(f'''{pohon} -C -P '*.mk|*.py|*.fmus' -I '*.pyc|__pycache__' {dirpath}''')


def fmusrunner(code):
    """
    /run>*  filename.fmus
    /run>*  filename.fmus|index/loop
    /run>*  *content.fm

    ada run fmus file dan fm file
    fmus file itu berisi barisentry
        fmus.process_mkfile(filepath, args.baris, os.getcwd())
    fm file hanya content
        fmus.process(content)
    barisentry default adlh index/fmus

    cuma set dir template nya ikutin lokasi tentunya

    fm//run>*@c/simple.fmus
    """
    fmus_not_fm_mode = True
    edit_mode = False
    entrybaris = barisentry

    if code.startswith('*'): # jk fm file = content
        # /run>**simple.fm
        fmus_not_fm_mode = False
        code = code.removeprefix('*').lstrip()
        dirpath = expand(code)
    else:
        # /run>*lengkap.fmus
        # /run>*lengkap.fmus|index/fmus
        if '|' in code:
            rawdirpath, entrybaris = code.split('|',1)
            dirpath = expand(rawdirpath)
        else:
            dirpath = expand(code)
    if not dirpath.startswith(rootdir):
        dirpath = joiner(rootdir, dirpath)

    if dirpath.endswith('*'):
        dirpath = dirpath.removesuffix('*').strip()
        indah4(f'edit {dirpath}', warna='green')
        perintah(f'code {dirpath}')
        return

    if not isfile(dirpath):
        if not dirpath.endswith('.fmus') \
            and not dirpath.endswith('.mk') \
            and not dirpath.endswith('.fm'):
            dirpath += '.fmus' # default ext
    if isfile(dirpath):
        fmus.set_file_dir_template(dirpath)
        if fmus_not_fm_mode:
            # fm//run>*@c/simple.fmus
            fmus.process_mkfile(dirpath, baris_entry=entrybaris)
        else:
            program = newlinify(file_content(dirpath))
            fmus.process(program)
    else:
        indah4(f'{dirpath} not found', warna='red')


expect_mapper = {
    'scp1': 'ssh -p 8022 u0_a194@192.168.0.102 ls -al',
    'scp2': 'ssh -p 8022 u0_a194@192.168.0.102 pwd',

    # 'scp -P 8022 upload.txt u0_a194@192.168.0.102:/data/data/com.termux/files/usef/work/uploads'
    'u1': 'u0_a194@192.168.0.102:/data/data/com.termux/files/usef/work/uploads',
    'files1': 'u0_a194@192.168.0.102:/data/data/com.termux/files/',
    'term1': 'u0_a194@192.168.0.102:/data/data/com.termux/',
    'ip1': 'u0_a194@192.168.0.102',
}


def harapw(code):
    """
    /hope>cmd|harapan|kirim|harapan|kirim|harapan|kirim|...
    kita bisa kirim yg sudah terkirim pada tahap 1 2 3 dst dg \1, \2, \3
    """
    import wexpect # https://github.com/raczben/wexpect

    cmd, harapkirims = code.split('|',1) # cmd|harapan|kirim|harapan|kirim|harapan|kirim|...
    cmd = expect_mapper.get(cmd, cmd) # utk singkat cmd/perintah, kita masukkan ke daftar perintah
    pecah = harapkirims.split('|') # harapan|kirim|harapan|kirim|harapan|kirim|...
    if cmd and pecah:
        w = wexpect.spawn(cmd)
        for i in range(0, len(pecah), 2):
            harap, kirim = pecah[i], pecah[i+1]
            indah4(f'''[wexpect] {cmd}
            harap   = [{harap}]
            kirim   = [{kirim}]
            ''', warna='white')
            w.expect(harap)
            w.sendline(kirim)
            print(w.read())


def harapl(code):
    import pexpect # https://pexpect.readthedocs.io/en/stable/overview.html

    cmd, harapkirims = code.split('|',1)
    cmd = expect_mapper.get(cmd, cmd)
    pecah = harapkirims.split('|')
    if cmd and pecah:
        w = pexpect.spawn(cmd)
        for i in range(0, len(pecah), 2):
            harap, kirim = pecah[i], pecah[i+1]
            indah4(f'''[pexpect] {cmd}
            harap   = [{harap}]
            kirim   = [{kirim}]
            ''', warna='white')
            w.expect(harap)
            w.sendline(kirim)
            print(w.read())


def harap(code):
    """
    fm//hope>scp2|.*password:|usef
    """
    if platform() in ['win32', 'windows']:
        harapw(code)
    else:
        harapl(code)
