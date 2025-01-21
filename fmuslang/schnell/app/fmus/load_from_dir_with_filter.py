from schnell.app.dirutils import (
	abs_dir,
	ayah, bongkar,
	create_dir,
	find_patterns,
	here,
	isdir, isfile, isdir_simple,
	basename,
    dirname,
	joiner,
	normy,	
	tempdir, file_under_tempdir,
	exists_in_dir,
    walk_fullpath,
    walk_fullpath_with_filters,
    make_folder_absolute,
)
from schnell.app.fileutils import (
	replace_from, 
	replace_at, 
	insert_after, 
	insert_before, 
	remove_lines,
	replace_entry,
	replace_between,
	replace_string_in_file,
	tab_to_space_start,
    copy_file, copy_file_list,
)
from schnell.app.printutils import (
  indah, indah0, indah3, indah4,
)
from schnell.app.utils import env_int
from schnell.app.fmus.common import Common


def load_from_dir_with_filter(oper, item, root_tree, self_run_configuration):
    """
    root_tree berguna jk siblings punya % variables dan perlu kita pake di sini waktu decode 
    namadir,f(D=...path dg variable...)
    """
    source = oper.split('=') [1]
    if env_int('ULIBPY_FMUS_DEBUG')>1:
        indah4(f"""[load_from_dir_with_filter] namadirektori,f(D=direktorisumber)
item:
    oper = {oper}
    item = {item}
config:
    self_run_configuration = {self_run_configuration}
params:
    source = {source}
    dirname = {dirname(source)}
    basename = {basename(source)}
""", warna='white')

    nama_file = basename(source)
    cek_ada_bintang = '.' in nama_file
    filter_extension = []
    skip_list = ['.git', '__pycache__', 'node_mdules']
    if cek_ada_bintang:
        source = dirname(source)
        # def walk_fullpath(basedir, skip_ends=None, filtered_ends=None):
        # filter_extension = '.' + nama_file.split('.')[1]
        filter_extension = ['.'+nama.split('.')[1] for nama in nama_file.split(',')] # *.js,*.css,*.png atau .js,.css,.png

    # jk sourcedir (D=sourcedir) punya variables, replace dari root_tree
    if root_tree is not None and hasattr(root_tree, 'variables'):
        for k,v in root_tree.variables.items():
            source = source.replace(k, v)
            if env_int('ULIBPY_FMUS_DEBUG')>1:
                indah4(f"[load_from_file_absolute] replacing {k} with {v} in {source}.", warna='magenta')

    source_atau_false = isdir(source) # ini bisa jadi boolean jk source di awal bukan dirpath/filepath benar
    # handle jk source_atau_false False atau source bukan dirpath
    if not source_atau_false: # isdir(source):
        indah4(f"[load_from_dir_with_filter] file/dir tidak ditemukan = [{source}]", warna='red')
    else:
        source = source_atau_false
        hasil = walk_fullpath_with_filters(source, keep_list=filter_extension, skip_list=skip_list)
        if env_int('ULIBPY_FMUS_DEBUG')>1:
            indah4(f"""[load_from_dir_with_filter] #2
oper = {oper}
item = {item}

source = {source}
dirname = {dirname(source)}
basename = {basename(source)}

hasil = skip dulu
panjang hasil = {len(hasil)}
item.workdir = {item.workdir}
""")
        targetdir = item.workdir
        if not isdir_simple(targetdir):
            make_folder_absolute(targetdir)
        copy_file_list(hasil, source, targetdir)
