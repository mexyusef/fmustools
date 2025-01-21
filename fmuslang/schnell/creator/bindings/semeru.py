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

def setup_bindings(bindings):
	@bindings.add("insert", "0")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/hajar.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "1")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/lamar.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "2")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/internet.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "a")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2021.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "b")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2020.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "c")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2015.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "d")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2013.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "e")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2012.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "f")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2009.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "g")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2008.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "h")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/2001.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)

	@bindings.add("insert", "i")
	def _(event):
		sumber = joiner(env_get('ULIBPY_ZLAUNCHER_DIR'), '2021/past/semeru/summary.mk')
		entry_title = 'index/fm.us'
		jalankan = lambda: process_fmus(sumber, entry_title)
		run_in_terminal(jalankan)
