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


################################## languages
def setup_bindings(bindings):
  @bindings.add("delete", "0")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/polyglot/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "1")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/julia/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "a")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/cs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "b")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/bash/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "c")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/cpp/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "d")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/dart/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "e")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/erlang/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "f")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/css/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "g")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/go/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "h")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/html/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "i")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/js/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "j")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/java/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "k")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/kt/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "l")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/hs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "m")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/elm/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "n")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/nim/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "o")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/clj/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "p")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/py/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "q")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/rb/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "r")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/r/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "s")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/scala/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "t")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/ts/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "u")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/rs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "v")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/groovy/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "w")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/swift/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "x")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/elixir/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "y")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/php/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("delete", "z")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/languages/pl/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)
