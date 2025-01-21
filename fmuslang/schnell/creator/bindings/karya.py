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

prefix_key = "home"

def setup_bindings(bindings):
  @bindings.add(prefix_key, "0")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/current/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "a")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/arsip/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "b")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/broadphone/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "c")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/clarity/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "d")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/dahsyat/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "e")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/ecoss/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "i")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/ivideo/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "j")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/anjab/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "k")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/koperasi/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "l")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/lingkungan/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "m")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/mandiri-rapor/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "n")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/nrt/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "o")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/oss/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "p")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/pubsub/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "q")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/mincle/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "r")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/scheduler/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "s")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/sop/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "t")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/sitarang/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "x")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/streamsation/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "y")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/yate/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "f")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/npm/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add(prefix_key, "z")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/karya/kryedit/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)
