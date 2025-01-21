from prompt_toolkit.application import run_in_terminal
from schnell.app.dirutils import (
	dirs, files, 
	files_noext,
	sdirs, sfiles, 
	joiner, 
	here, 
	isdir, isfile,
	abs_dir,
	ayah,
)
from schnell.app.fileutils import (
	file_lines, 
	line_contains,
	get_definition_by_key_permissive_start, 
	get_daftar,
)
from schnell.app.utils import (
	env_exist,
	env_get,
	perintah,
	python_package,
	trycopy, trypaste,
)
from schnell.app.printutils import (
	indah0,
	print_copy,
	print_copy_enumerate_list,
	print_file,
)

from .common import process_fmus

################################## android
def setup_bindings(bindings):
  @bindings.add("c-a", "3")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/mobile/_persiapan/expo-project.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-a", "a")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/mobile/android/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-a", "f")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/mobile/flutter/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-a", "k")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/mobile/android-kotlin/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-a", "n")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/mobile/react-native/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)
