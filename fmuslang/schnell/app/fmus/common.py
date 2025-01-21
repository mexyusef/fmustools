import re
from schnell.app.definitor import BaseDefinitor
from schnell.app.fileutils import get_definition_by_key_permissive_start
from schnell.app.printutils import indah4
from schnell.app.utils import env_int, env_get

from .treehelper import get_all_tree_children

code_prefix = """Please edit the code following these instructions:
---------------------------------------------------------
"""

code_suffix = """
---------------------------------------------------------
If you make a change, rewrite the entire file."""

input_keyword = env_get('ULIBPY_FMUS_INPUT_KEYWORD')
if not input_keyword:
	input_keyword = '__INPUT__'
input_keyword_gui = '__INPUTGUI__'


LISTDIR = '__LS' # ~while[__LS=*], ~while[__LS=.txt] => __CURFILE__ masuk 'replacer'
# update bisa iterate over whitespace-delimited string atau comma-delimited string
LISTSTR = '__STR' # pkg1 pkg2 pkg3
LISTCMA = '__COMMA' # pkg1, pkg2, pkg3 (ignore whitespace)


def replace_inputgui_in_item_command_return_itemcommand(item, root_tree=None):
	if not root_tree:
		root_tree = item.parent

	if input_keyword_gui in item.command \
		and hasattr(root_tree, 'input_keys') \
		and hasattr(root_tree, 'input_keys_index') \
		and hasattr(root_tree, 'variables'):

		terindeks = root_tree.input_keys[root_tree.input_keys_index]

		if terindeks in root_tree.variables:
			pengganti = root_tree.variables[terindeks]

			item.command = item.command.replace(input_keyword_gui, pengganti)

	return item.command


def replace_input_in_item_command_return_itemcommand(item, root_tree=None):
	if not root_tree:
		root_tree = item.parent

	if input_keyword in item.command \
		and hasattr(root_tree, 'input_keys') \
		and hasattr(root_tree, 'input_keys_index') \
		and hasattr(root_tree, 'variables'):

		terindeks = root_tree.input_keys[root_tree.input_keys_index]

		if terindeks in root_tree.variables:
			pengganti = root_tree.variables[terindeks]

			item.command = item.command.replace(input_keyword, pengganti)

	return item.command


def replace_input_in_item_command(item, root_tree=None, change_item_workdir=True, change_children_workdir=True):
	"""
	root_dir = item.parent
	"""
	if not root_tree:
		root_tree = item.parent

	if (input_keyword in item.command or input_keyword in item.workdir) \
		and hasattr(root_tree, 'input_keys') \
		and hasattr(root_tree, 'input_keys_index') \
		and hasattr(root_tree, 'variables'):

		terindeks = root_tree.input_keys[root_tree.input_keys_index]

		if terindeks in root_tree.variables:
			pengganti = root_tree.variables[terindeks]

			if env_int('ULIBPY_FMUS_DEBUG')>=1:
				indah4(f"[app.fmus.common] Ganti '{input_keyword}' menjadi '{pengganti}'.", warna='white')
			
			# item.command dulu
			item.command = item.command.replace(input_keyword, pengganti)
			
			# juga item.workdir
			if change_item_workdir:
				item.workdir = item.workdir.replace(input_keyword, pengganti)
			
			if env_int('ULIBPY_FMUS_DEBUG')>=1:
				indah4(f"[app.fmus.common] item.command = '{item.command}' di workdir {item.workdir}.", warna='white')

			# di sini misalnya dari $flutter create __nameproyek
			# harusnya di sini semua children ganti 'input' ke name baru
			# file(e=) berhasil diubah, tapi file(f=) blm terubah

			if change_children_workdir:
				for node in get_all_tree_children(item):
					node.workdir = node.workdir.replace(input_keyword, pengganti)
	
	return item


class Common:
	TAB = '  '
	keywords = [
		'ancestors',
		'anchestors',
		'children',
		'depth',
		'descendants',
		'height',
		'is_leaf',
		'is_root',
		'iter_path_reverse',
		'leaves',
		'parent',
		'path',
		'root',
		'separator',
		'siblings'
	]
	temporary_dict = {}

	@staticmethod
	def definisi(baris, filepath):
		"""
		Common.definisi()
		kita bikin format baru yg didukung vscode: .mk file
		--% start
		--# end
		^ ini bikin masalah: gak dimulai dg ^
		utk content: 
		baris = '''"folding": {"markers": {"start": "^--%\\s*","end": "^--#"}},'''
		krn ada --# di tengah
		"""
		# if filepath.endswith('.mk'):
		# 	kunci_start = '^--%'
		# 	kunci_end = '^--#'
		# 	return BaseDefinitor.manual_definisi(baris, filepath, kunci_start, kunci_end)
		# else:
		# 	return BaseDefinitor.manual_definisi(baris, filepath, '--')
		from schnell.app.dirutils import bongkar_if_not_file
		filepath = bongkar_if_not_file(filepath)
		# kunci_start = '^--%'
		# kunci_end = '^--#'
		# content = BaseDefinitor.manual_definisi(baris, filepath, kunci_start, kunci_end)
		content = get_definition_by_key_permissive_start(filepath, baris)
		# if not content and '[' in baris and ']' in baris:
		# 	# def get_definition_by_key_permissive_start(filepath, baris, kunci_start='^--%', kunci_end='^--#', debug=False):
		# 	content = get_definition_by_key_permissive_start(filepath, baris)
		# 	indah4(f'[common/Common/definisi] nextjs baris style => file [{filepath}] baris [{baris}] hasil [{content}]', warna='yellow', layar='blue')
		return content


	@staticmethod
	# entries = BaseDefinitor.manual_list_grep(nilai, template_file, kunci='--')
	def list_grep(baris, filepath):
		"""
		harus gunakan:
		get_definition_double_entry_aware
		get_definition_double_entry_aware(filepath, baris, kunci_start='^--%', kunci_end='^--#')
		"""
		from schnell.app.dirutils import bongkar_if_not_file
		is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
		filepath = bongkar_if_not_file(filepath)
		if is_debugging:
			indah4(f"""[list_grep] baris = {baris}, filepath = {filepath}
			=> {filepath}
			""", warna='magenta', layar='green')
		return BaseDefinitor.manual_list_grep(baris, filepath)
		# if filepath.endswith('.mk'):
		# 	kunci_start = '--%'
		# 	kunci_end = '--#'
		# 	return BaseDefinitor.manual_list_grep(baris, filepath, kunci_start, kunci_end)
		# else:
		# 	return BaseDefinitor.manual_list_grep(baris, filepath, '--')

	@staticmethod
	def replace_me(line):
		is_debugging = env_int('ULIBPY_FMUS_DEBUG')>1
		for k, v in Common.temporary_dict.items():
			# |basename adlh fungsi khusus
			if k in line and not line.endswith('|basename') and not v in ['__OPENFILE__', '__OPENDIR__', '__SAVEFILE__']:
				if is_debugging:
					indah4(f'[schnell/app/fmus/common|Common.replace_me] from: [{k}] to [{v}] in [{line}]', warna='yellow', layar='blue')
				# if is_debugging:
				# 	indah4(f'[Common.replace_me] old: [{k}] new [{v}]', warna='yellow', layar='blue')
				# save_variables bisa execute shell dll
				check_executor = re.match(r'^/(sh|bash|py)/.*', v)
				if check_executor:
					handler = check_executor.group(1)
					if handler in ['bash', 'sh']:
						code = v.removeprefix('/' + handler + '/')
						from schnell.app.executor import handle_bash
						masukan = handle_bash(code)
						if is_debugging:
							indah4('[Common/replace_me], executing code: '+ code + ' => ' + masukan, warna='blue', layar='white')
						v = masukan
						# print('item vars bernilai skrg:', item.variables[k])
			line = line.replace(k, v)

		return line
