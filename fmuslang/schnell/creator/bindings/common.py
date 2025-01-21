from prompt_toolkit.application import run_in_terminal
from schnell.app.fileutils import (
	get_definition_by_key_permissive_start, 	
)
from schnell.app.printutils import indah3
from schnell.app.utils import (
	env_get,	
)
from schnell.app.fmus import Fmus


def process_fmus(sumber, entry_title, Debug=True):
	# print('process_fmus:', sumber, 'dan:', entry_title)
	debug_level = int(env_get('ULIBPY_FMUS_DEBUG'))
	fmus = Fmus(debug_level)
	fmus.set_file_dir_template(sumber)
	program = get_definition_by_key_permissive_start(sumber, entry_title)
	if debug_level:
		indah3(f'FMUS: mau oprek program: [{program}]')
	if not program.strip():
		indah3(f"entry {entry_title} tidak ditemukan di {sumber}...", warna='red')
		input('*'*80 + '\nERR...ERR...ERR...\n' + '*'*80 + '\n')
	fmus.process(program)


def run_fmus(sumber, entry_title='index/fm.us'):
	"""
	utk jalankan dari repl prompt
	"""
	jalankan = lambda: process_fmus(sumber, entry_title)
	run_in_terminal(jalankan)
