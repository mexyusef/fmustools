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

################################## web frontend
def setup_bindings(bindings):
  @bindings.add("c-_")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/_persiapan/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "1")
  def _(event):
    # kalimat = "web no 1"
    # event.app.current_buffer.insert_text(kalimat)
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/_persiapan/draft_v0.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "a")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/react-antd/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "b")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/react-bs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "g")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/angular/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "m")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/react-mui/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "n")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/nextjs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "r")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/react/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "s")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/nestjs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "t")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/tailwindcss/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "u")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/nuxtjs/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "v")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/vue/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)

  @bindings.add("c-f", "y")
  def _(event):
    sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/web/storybook/index.mk')
    entry_title = 'index/fm.us'
    jalankan = lambda: process_fmus(sumber, entry_title)
    run_in_terminal(jalankan)
