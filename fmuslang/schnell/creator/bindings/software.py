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

# prefix_key = "s-delete"
# prefix_key = "s-escape"
prefix_key = "pagedown"

################################## software
def setup_bindings(bindings):
	@bindings.add(prefix_key, "1")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/compiler/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "2")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/competitive/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "a")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/architect/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "c")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/cicd/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "d")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/data/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "g")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/git/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "i")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/multimedia/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "k")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/kubernetes/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "l")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/cloud/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "m")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/ml/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "n")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/knowledge/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "o")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/tools/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "p")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/scraper/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "r")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/protocols/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "s")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/selenium/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "t")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/tdd/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "u")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/medium/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add(prefix_key, "y")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), 'zlauncher/software/system/index.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)
