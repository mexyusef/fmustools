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


################################## desktop
def setup_bindings(bindings):
  @bindings.add("pageup", "a")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/csgtk/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "c")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/cppgtk/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "g")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/pygame/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "j")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/javafx/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "i")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/javaswing/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "p")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/pyqt5/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "q")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/qt/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "s")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/scalafx/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "t")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/tkinter/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "u")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/rustqt/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "x")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/wxpython/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("pageup", "w")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/desktop/wpf/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)
