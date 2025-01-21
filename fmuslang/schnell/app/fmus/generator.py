# pylint: disable=W0105
import pathlib, copy, json, os, re, shutil, sys, traceback
from rich.pretty import pprint
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter

# from schnell.app.objectutils import hapus_salin_node_dalam
from schnell.app.datetimeutils import epoch
from schnell.app.dirutils import (
	abs_dir,
	ayah,
	ayahbasename, basename,
	bongkar,
	create_dir,
	# find_patterns,
	here,
	isdir, isfile,
	# does_exist,
	joiner,
	normy,
	# tempdir,
	# file_under_tempdir,
	# exists_in_dir,
)
from schnell.app.fileutils import (
	get_daftar,
	get_extension,
	get_filename,
	get_lastpath_and_filename,
	check_replace_if_contain_links,
	fmusfile_entry,
	get_definition_fmusfile_barisentry,
	file_content,
)
from schnell.app.inpututils import give_me
from schnell.app.printutils import (
	Debug,
	dir_w,
	filter_print_latest_files,
	indah,
	indah0,
	indah4,
	print_copy,
	print_copy_enumerate,
	print_copy_enumerate_list,
	print_copy_file,
	print_list_warna,
)
from schnell.app.promptutils import checkbox_select
from schnell.app.urlutils import get_content as get_url_content
from schnell.app.utils import (
	env_set,
	env_get,
	env_int,
	env_exist,
)
# from schnell.app.communication import start_client
# from schnell.app.configuration import Configuration as Konfigurasi
# from schnell.app.punctuation import Punctuation
# from schnell.app.specialcmd import SpecialCommand
# from schnell.app.autoutils import confirm as autogui_confirm
from .common import Common, input_keyword
from .treehelper import (
	get_all_tree_children,
	get_last_absolute_children,
	get_direct_children,
	get_last_direct_children,
	set_attr_direct_children,
	set_attr_direct_children_cond,
	print_ready_children,
	get_root,
	get_siblings_all,
	get_siblings_before,
	get_siblings_after,
)


is_debugging = env_int('ULIBPY_FMUS_DEBUG') > 1
# is_debugging = 2

class Generator:


	def __init__(self, run_configuration, parent=None):
		self.run_configuration = run_configuration
		self.debug = Debug(env_int('ULIBPY_FMUS_DEBUG')>0)
		self.parent_fmus = parent


	def update_config_replacer(self, new_replacer):

		if is_debugging:
			indah0(f'[generator][update_config_replacer] Updating __FILE__ dari {self.run_configuration["replacer"]["__FILE__"]} ke {new_replacer["__FILE__"]}.', newline=True, warna='yellow', layar='blue', bold=True)
		self.run_configuration['replacer'].update(new_replacer)


	def create_and_chdir_projectdir(self):
		projectdir = normy(self.run_configuration['projectdir'])

		if is_debugging:
			indah4(f"""[generator][create_and_chdir_projectdir]
			self.run_configuration['projectdir'] = {self.run_configuration['projectdir']}
			projectdir = {projectdir}
			""", warna='magenta')
		if '__INPUT__' in projectdir:
			'''
			belum bisa buat projectdir krn masih butuh input dari user
			jangan sampai dir bernama __INPUT__ dibuat
			'''
			return projectdir
		if not os.path.exists(projectdir):
			indah4(f'''[generator][create_and_chdir_projectdir]
			creating
			projectdir = {projectdir}
			self.run_configuration['projectdir'] = {self.run_configuration['projectdir']}
			''', warna='magenta')
			try:
				os.makedirs(projectdir)
			except Exception as err:
				indah4(f'''[generator][create_and_chdir_projectdir] Exception os.makedirs({projectdir}).
				mau buat projectdir = {projectdir}
				exception = {err}
				''',
				warna='cyan')
		os.chdir(projectdir)
		return projectdir


	def generator_replace_me(self, line):
		for k, v in self.run_configuration['replacer'].items():
			line = line.replace(k, v)
		return line


	def get_content(self, node):
		if hasattr(node, 'original'):
			return node.original
		elif hasattr(node, 'content'):
			return node.content
		elif hasattr(node, 'command'):
			return node.command
		elif hasattr(node, 'operations'):
			return str(node.operations)
		else:
			return ""


	def generate(self, root_tree, projectdir=None, banner=True, capture_outerr=False):

		if is_debugging:
			indah(f'''***** GENERATOR *****
			self.run_configuration replacer = {self.run_configuration['replacer']}
			projectdir = {projectdir}
			rendertree = {str(RenderTree(root_tree))}
			''', warna='magenta', layar='black', newline=True, bold=True, blink=True)


		if '__PWD__' in self.run_configuration['replacer'] and not env_exist('ULIBPY__PWD__'):
			'''TODO:
			cek apakah ini lokasi yg tepat utk memberikan ULIBPY__PWD__
			ataukah bisa lebih early?
			fmus
			processor
			generator
				generate
					here
			'''
			# indah4(f'''[generator]
			# 	setting PWD ke env dari config!
			# 	{self.run_configuration['replacer']['__PWD__']}
			# 	''', warna='cyan')
			env_set('ULIBPY__PWD__', self.run_configuration['replacer']['__PWD__'])
			# input(' ...press... ')

		root_tree.epoch = epoch()

		if banner:
			if is_debugging:
				indah4(f"""[generator] self.run_configuration =\n{json.dumps(self.run_configuration, indent=2)}""", warna='magenta')

		# autogui_confirm('generate #2')
		if not projectdir:
			projectdir = self.create_and_chdir_projectdir()
			# if is_debugging:
			# 	indah4(f"""[app.fmus.generator][generate] no projectdir, after calling create_and_chdir_projectdir
			# 	projectdir = {projectdir}
			# 	""", warna='green')
			if is_debugging:
				indah4(f"[generator] => create projectdir: {projectdir}", warna='magenta')

		if 'initial_rootvars' in self.run_configuration:
			'''
			ini agar bisa passing root variables ke child program dari parent program
			'''
			root_tree.variables = self.run_configuration['initial_rootvars']

		self.generate_iterate(root_tree, projectdir, capture_outerr=capture_outerr)


	def generate_iterate(self, root_tree, projectdir, capture_outerr=False):

		counter = 1

		for item in PreOrderIter(root_tree):

			# autogui_confirm(f'generate_iterate {counter} => {item}')

			if is_debugging:
				# item2 = salin(item)
				# del item2['replacer']
				# item2 = hapus_salin_node_dalam(item, 'replacer')
				indah4(f'''👀 [generator][generate_iterate][{item.original}]
	item: {re.sub(r'replacer={[^}]+},', '', str(item))}''', warna='yellow', layar='blue')

			# warning jk original = input,d name input type dir tapi gak ada operations=['create_dir']
			# maka gak ada proses minta input dari user.
			if item.name == input_keyword and item.type == 'dir' and item.workdir.endswith(input_keyword) \
				and not hasattr(item, 'operations'):
				pesan = f'warning: terdeteksi {item.original} tetapi tidak ada directory operations\n'
				pesan += f'ini akan sebabkan {item.workdir} dibuat tanpa minta ganti dari user\n'				
				pesan += 'Tekan "y" atau "yes" jk ditambahkan operations sehingga akan diminta buat direktori'
				indah0(pesan, warna='white', bold=True, newline=True)
				yesno = input('=> ')
				if yesno == 'y' or yesno == 'yes':
					item.forced_operation = True # utk nandakan bahwa anak cucu perlu ganti workdir
					item.operations = ['create_dir']

			counter += 1

			# di sini tempat pas utk intercept jk workdir berakhir dg __INPUT__ dan gak ada nilai
			# item:
			# workdir='C:\\work\\hapus\\kerja\\hapus\\coba\\hulk\\__INPUT__'
			# workdir='C:\\work\\hapus\\kerja\\hapus\\coba\\hulk\\__INPUT__'
			# parent:
			# workdir='C:\\work\\hapus\\kerja\\hapus\\coba\\hulk\\hulk'
			if input_keyword in item.workdir \
				and (hasattr(item.parent, 'workdir') and not input_keyword in item.parent.workdir) \
				and item.parent.type == 'dir' and item.parent.workdir != item.workdir:
				if is_debugging:
					indah4(f'''😭 [generator] ada __INPUT__ di workdir, tapi gak ada di parent yg type=dir
					item {item}
					parent {item.parent}
					root {root_tree}
					''', warna='yellow', layar='cyan')

				if item.type == 'file':
					'''
					item
						type='file'
						workdir='C:\\work\\hapus\\kerja\\hapus\\coba\\hulk\\__INPUT__\\mengenai_settings.txt'
					parent 
						name='__INPUT__', 
						old_name='__TEMPLATE_SCRAPYPROJECT'
						original='__TEMPLATE_SCRAPYPROJECT,d(/mk)'
						type='dir'
						workdir='C:\\work\\hapus\\kerja\\hapus\\coba\\hulk'
					root
						input_keys=['__TEMPLATE_DJANGOPROJECT', '__TEMPLATE_SCRAPYPROJECT'], 
						input_keys_index=1
						variables={'__TEMPLATE_DJANGOPROJECT': 'coba', '__TEMPLATE_SCRAPYPROJECT': 'hulk'}
					'''
					old_workdir = item.workdir
					filename = os.path.basename(old_workdir)
					workdir_tanpa_file = os.path.dirname(old_workdir)
					if input_keyword in workdir_tanpa_file and workdir_tanpa_file != item.parent.workdir:
						if item.parent.name == input_keyword:
							kunci_index = item.parent.old_name # __TEMPLATE_SCRAPYPROJECT
							if kunci_index in root_tree.variables:
								nilai_input = root_tree.variables[kunci_index] # hulk
								new_workdir = normy(item.workdir.replace(input_keyword, nilai_input))
								item.workdir = new_workdir
						else:
							new_basedir = item.parent.workdir
							new_workdir = normy(os.path.join(item.parent.workdir, filename))
							item.workdir = new_workdir

						if is_debugging:
							indah4(f'''🤩🤩🤩 [generator] {old_workdir} => {new_workdir} utk file {filename}
						item = {item}
						''', warna='yellow', layar='green')
				else:
					if item.parent.name == input_keyword:
						kunci_index = item.parent.old_name # __TEMPLATE_SCRAPYPROJECT
						if kunci_index in root_tree.variables:
							nilai_input = root_tree.variables[kunci_index] # hulk
							new_workdir = normy(item.workdir.replace(input_keyword, nilai_input))
							item.workdir = new_workdir
					else:
						# ini jika bukan file
						item.workdir = item.parent.workdir

				# di sini mestinya, semua following-sibling juga ganti workdir utk yg non-file
				if is_debugging:
					indah4(f'''🙂 [generator] {input_keyword} in item.workdir sudah dibenerin skrg jd:
					item = {item}
					item.workdir = {item.workdir}
					parent = {item.parent}
					''', warna='yellow', layar='green')

			# # kadang item.workdir baru diassign oleh % simpan-temp-vars dari user input
			# # tapi belum ada/terbuat
			# # maka operasi file ,f(e=) bisa gagal
			# if not isdir(item.workdir):
			# 	if is_debugging:
			# 		indah4(f'''[generator][generate_iterate] buat folder item.workdir karena belum ada
			# 		item.workdir = {item.workdir}
			# 		apakah sudah ada = {isdir(item.workdir)}
			# 		''', warna='magenta', layar='green')
			# 	create_dir(item.workdir)

			# skip utk node skip = True dan bukan branching
			# TODO: check apa ini sebabkan masalah jk branching/looping anak item lain
			if is_debugging:
				indah4('>>before check branching/looping/skip', warna='cyan')

			if item.type != 'branching' \
				and item.type != 'looping' \
				and hasattr(item, 'skip') \
				and item.skip == True:
				continue

			if is_debugging:
				indah4('>>after check branching/looping/skip', warna='cyan')

			if hasattr(item, 'operations'):

				for oper in item.operations:

					if is_debugging:
						indah4(f"[generator] operations => oper = [{oper}] in item:\n\t[{item}].\n", warna='magenta')

					if oper == 'create_dir':
						if is_debugging:
							indah4("""[generator][create_dir]
							masuk if oper == 'create_dir':
							""", warna='magenta')
						# cek ada pwd atau tidak
						# AnyNode(counter=0, epoch=1647048283, level=0, name='C:\\Users\\user\\AppData\\Local\\Temp\\sample\\crajs', old_name='__PWD/crajs'
						if hasattr(item, 'old_name') and '__PWD' in item.old_name:
							indah4(f'''[generator][create_dir]
								deteksi __PWD di {item.old_name}
								cek apakah environ memberikan __PWD: {env_exist('__PWD__')}
								jika ya: {env_get('__PWD__')}
								pwd dari self.config: {self.run_configuration['replacer']['__PWD__']}
								''', warna='magenta')
							# input(' ... press ... ')
						from .create_dir import create_dir as create_dir_fmus
						create_dir_fmus(root_tree, item, projectdir, self.debug, self_run_configuration=self.run_configuration)

					elif oper == 'remove_dir':
						targetdir = os.path.join(projectdir, item.workdir)
						yes = input(f'Press "y" to remove [{targetdir}]')
						if yes == 'y':
							shutil.rmtree(targetdir)

					elif oper .startswith ('copy_dir_from'):
						'''
						# ini utk operasi file f,(f=lokasi-relatif-terhadap-cwd) <- don't use
						# don't use krn kita sudah gak pake ini template dir
						# dan cwd juga gak rujuk ke folder yg kita gunakan sekarang

						"templates": "templates", <- filemanager/templates
						templates = os.path.join(workdir, run_configuration['templates'])
						TODO:
						ganti templatedir ke lokasi yg diconfigure dan absolute atau yg digunakan
						'''
						from .copy_dir_from import copy_dir_from
						copy_dir_from(oper, item, self.debug, self.run_configuration)

					elif oper .startswith ('copy_absolute_dir_from'):
						from .copy_absolute_dir_from import copy_absolute_dir_from
						copy_absolute_dir_from(oper, item, self.debug)

					elif oper.startswith ('load_program_from'):
						'''
						%tempate_anak=__CURDIR/file_anak.mk
						somedir,d(/load=__CURDIR/file.mk=cari-program/fm.us)
						somedir,d(/load=tempate_anak=cari-program/fm.us)

						for k,v in self.run_configuration['replacer'].items():
							template_file = root_tree.variables[kunci]

						harusnya bisa temukan cara shg gak perlu __CHILD*
						misal dg save dulu replacer parent...
						stlh proses child selesai maka balikkan replacer nya.
						sptnya yg perlu disave
						replacer
						projectdir
						initial_rootvars
						'''
						from .load_program_from import load_program_from
						load_program_from(root_tree, oper, item, self.debug, self.run_configuration)

					elif oper.startswith('grep='):
						query = oper.removeprefix('grep=')
						print(f'start grepping query={query} di {item.workdir}')
						# input('[generator] Press any key to process grep_within_directory')
						os.system(f'grep -r -n -H -I "{query}" {item.workdir}')

					elif oper.startswith('find='):
						query = oper.removeprefix('find=')
						print(f'start finding query={query} di {item.workdir}')
						# C:\hapus\nov22>\work\usr\local\wbin\find . -type d ( -name *rai* -or -name *phoe* ) -maxdepth 1
						if ',' in query:
							# queries = [f"-iname \"*{item.strip()}*\"" for item in query.split(',')]
							# kita bikin "raw", agar user bisa *.exe daripada cuma exe => peroleh execute, dsb
							queries = [f"-iname \"{item.strip()}\"" for item in query.split(',')]
							if queries:
								new_query = ' -or '.join(queries)
								# os.system(f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" ( {new_query} )')
								perintahnya = f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" ( {new_query} )'
								print(perintahnya)
								os.system(perintahnya)
						else:
							os.system(f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" -iname "*{query}*"')

					elif oper.startswith('rm='):
						query = oper.removeprefix('rm=')
						print(f'start rm-ing query={query} di {item.workdir}')
						# C:\hapus\nov22>\work\usr\local\wbin\find . -type d ( -name *rai* -or -name *phoe* ) -maxdepth 1
						if ',' in query:
							queries = [f"-iname \"*{item.strip()}*\"" for item in query.split(',')]
							if queries:
								new_query = ' -or '.join(queries)
								# os.system(f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" ( {new_query} )')
								perintahnya = f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" ( {new_query} ) -type d -print | C:\\work\\usr\\local\\wbin\\xargs.exe -0 rm -r --'
								print(perintahnya)
								os.system(perintahnya)
						else:
							# os.system(f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" -iname "*{query}*" -type d -print | C:\\work\\usr\\local\\wbin\\xargs.exe -0 rm -r --')
							perintahnya = f'C:\\work\\usr\\local\\wbin\\find.exe "{item.workdir}" -iname "*{query}*" -type d -print | C:\\work\\usr\\local\\wbin\\xargs.exe -0 rm -r --'
							print(perintahnya)
							os.system(perintahnya)

					elif oper == 'input_from_user_with_prompt':
						from .input_from_user_with_prompt import input_from_user_with_prompt
						input_from_user_with_prompt(item, self.debug)

					elif oper == 'touch_file':
						# indah4(f'''
						# PRE
						# item.workdir			= {item.workdir}
						# item.parent.workdir	= {item.parent.workdir}
						# item					= {item}
						# item.parent			= {item.parent}
						# ''', warna='white')
						from schnell.app.fmusutils import replace_input_workdir
						replace_input_workdir(item)
						# indah4(f'''
						# POST
						# item.workdir			= {item.workdir}
						# item.parent.workdir	= {item.parent.workdir}
						# item					= {item}
						# item.parent			= {item.parent}
						# ''', warna='yellow')
						# input(' ... lanjut ... ')
						pathlib.Path(item.workdir).touch()

					elif oper .startswith ('content_file'):
						from .content_file import content_file
						item.replacer = self.run_configuration['replacer']
						# content_file(oper, item, self.debug, self.run_configuration)
						content_file(oper, item, root_tree, self.run_configuration)



					elif oper .startswith ('query_active_llm_for_code'):
						from .query_active_llm_for_code import query_active_llm_for_code
						item.replacer = self.run_configuration['replacer']
						query_active_llm_for_code(oper, item, root_tree, self.run_configuration)

					elif oper .startswith ('query_specific_llm_for_code'):
						from .query_specific_llm_for_code import query_specific_llm_for_code
						item.replacer = self.run_configuration['replacer']
						query_specific_llm_for_code(oper, item, root_tree, self.run_configuration)

					elif oper .startswith ('query_active_llm_from_fmus'):
						from .query_active_llm_from_fmus import query_active_llm_from_fmus
						item.replacer = self.run_configuration['replacer']
						query_active_llm_from_fmus(oper, item, root_tree, self.debug, self.run_configuration)

					elif oper .startswith ('query_specific_llm_from_fmus'):
						from .query_specific_llm_from_fmus import query_specific_llm_from_fmus
						item.replacer = self.run_configuration['replacer']
						query_specific_llm_from_fmus(oper, item, root_tree, self.debug, self.run_configuration)

					# bahaya, startswith bisa kemakan di atas...
					elif oper .startswith ('query_active_llm'):
						from .query_active_llm import query_active_llm
						item.replacer = self.run_configuration['replacer']
						query_active_llm(oper, item, root_tree, self.run_configuration)

					elif oper .startswith ('query_specific_llm'):
						from .query_specific_llm import query_specific_llm
						item.replacer = self.run_configuration['replacer']
						# print(f"""[generator] oper, item, root_tree, self.run_configuration
						# oper: {oper}
						# item: {item}
						# root: {root_tree}
						# dummy: self.run_configuration
						# """)
						query_specific_llm(oper, item, root_tree, self.run_configuration)


					elif oper .startswith ('load_from_file') and not oper.startswith('load_from_file_absolute'):
						'''
						TODO:
						- perbaiki ambil sumber templates
						- utk insert before misanya baru bisa gini
						monyong.txt,f(f=huckleberry.txt,@ib=line_pengganti=Release Date)
						Release Date terlalu sederhana, pengen bisa ada ' koma, dst
						krn jk isi file panjang maka perlu spesifik line indicator nya.
						Release Date diambil dari HURUF_FOLDER_LAMA
						coba kita ganti ke MENGANDUNG_AMPERSAND_DAN_TANDASERU
						| "ib" "=" singkat "=" MENGANDUNG_AMPERSAND_DAN_TANDASERU -> insert_before
						kita coba dg line_indicator:
						Release Date: August, 1993 [eBook #76]
						'''
						from .load_from_file import load_from_file
						load_from_file(oper, item, self.debug, self.run_configuration, self.generator_replace_me)

					elif oper .startswith ('load_from_file_absolute'):
						from .load_from_file_absolute import load_from_file_absolute
						load_from_file_absolute(oper, item, root_tree, self.run_configuration)

					elif oper .startswith ('load_from_dir_with_filter'):
						from .load_from_dir_with_filter import load_from_dir_with_filter
						load_from_dir_with_filter(oper, item, root_tree, self.run_configuration)

					elif oper .startswith('ambil_entry_dari_file_template'):
						'''
						oper: ambil_entry_dari_file_template={'template': 'cari1024'}
							di sini, dict_file_baris.items() hanya satu tentunya
						template -> src, utama, main, dll
						cari1024: program/001/fm.us dll

						kita pengen stlh dapat entry dari template::cari1024, kita oprek replacer.
						write_file_with_variable_expansion

						update:
						kita tambah 4 operasi insert before/after/replace at/from
						dg 2 kunci:
						insert_replace = 1/2/3/4
						line_indicator = baris utk jadi indicator to insert/replace
						'''
						from .ambil_entry_dari_file_template import ambil_entry_dari_file_template
						try:
							ambil_entry_dari_file_template(oper, item, root_tree, self.debug, self.run_configuration)
						except Exception as err:
							'''
							kita lagi lupa dimana 
							%TEMPLATE_THIS=input 
							%TEMPLATE_THAT=input
							diassign ke item.workdir
							yg ternyata jk item anak dari TEMPLATE_THIS tetapi ngambil "item ayah basename" dari yg terakhir
							yakni TEMPLATE_THAT
							ini salah
							'''
							item_ayah_basename = ayahbasename(item.workdir)
							item_parent_basename = basename(item.parent.workdir)
							indah4(f"""😭 [generator] [{item.original}]
							ambil_entry_dari_file_template error: {err}
							item: {item}
							item ayah basename: {item_ayah_basename}
							item.parent: {item.parent}
							item.parent basename: {item_parent_basename}
							""")
							indah4(traceback.format_exc(), warna='red')
							# cek jika basename dari item.ayah berbeda dg basename dari item.parent
							if item_ayah_basename != item_parent_basename:
								item.workdir = normy(item.workdir.replace(item_ayah_basename, item_parent_basename))
								# indah4(f'item.workdir baru = {item.workdir}', warna='yellow')
								if isdir(ayah(item.workdir,1)):
									indah4(f'[generator] ketemu item.workdir baru dari info parent [{item.workdir}], kita coba ulang', warna='yellow', layar='blue')
									ambil_entry_dari_file_template(oper, item, root_tree, self.debug, self.run_configuration)

					elif oper .startswith('ambil_entry_codegen'):
						'''
						'''
						from .ambil_entry_codegen import ambil_entry_codegen
						ambil_entry_codegen(oper, item, root_tree, self.debug, self.run_configuration)

					elif oper .startswith('ambil_replify_here'):
						'''
						'''
						from .helper.ambil_replify_here import ambil_replify_here
						ambil_replify_here(oper, item, root_tree, self.debug, self.run_configuration)

					elif oper .startswith('ambil_terdekod_dari_file_template'):
						'''
						'''
						from .ambil_terdekod_dari_file_template import ambil_terdekod_dari_file_template
						ambil_terdekod_dari_file_template(oper, item, root_tree, self.debug, self.run_configuration)

					elif oper == 'paste_from_clipboard_with_pause':
						from .paste_from_clipboard_with_pause import paste_from_clipboard_with_pause
						paste_from_clipboard_with_pause(item, self.debug)

					elif oper == 'paste_from_clipboard_without_pause':
						from .paste_from_clipboard_with_pause import paste_from_clipboard_with_pause
						paste_from_clipboard_with_pause(item, self.debug, pause=False)

					elif oper .startswith ('url_file'):
						from .url_file import url_file
						url_file(oper, item, self.debug)

					elif oper .startswith ('generate_image'):
						# operations => oper = [generate_image=avarandom] in item:
						_, namaoperasi = oper.split('=')

						if namaoperasi == 'ava1':
							'''
							filename.png,f(img=ava1)
							'''
							indah4(f"random-avatar => {item.workdir}", warna='blue', layar='green')
							from schnell.app.mediautils import generate_avatar
							generate_avatar(item.workdir)

						elif namaoperasi .startswith('art1'):
							'''
							filename.png,f(img=art1)
							'''
							spec = namaoperasi.removeprefix('art1')
							indah4(f"random-geometric-art => {item.workdir}", warna='blue', layar='green')
							from schnell.app.imageart import image_art_save
							# art1,300x300
							if spec and spec.startswith(','):
								spec = spec.removeprefix(',')
								w,h = spec.split('x')
								image_art_save(item.workdir,int(w),int(h))
							else:
								image_art_save(item.workdir)

						elif namaoperasi.startswith('random'):
							from schnell.app.fakerutils import palsu
							from schnell.app.urlutils import save_image
							image_url = palsu.faker.image_url()
							indah4(f"{image_url} => {item.workdir}", warna='blue', layar='green')
							save_image(image_url, item.workdir)

					else:
						indah4(f"operation [{oper}] not processed", warna='red', layar='white')

					if hasattr(item, 'fileops_operation'):
						from schnell.app.fmus.fileops import replace_left_of_query, replace_right_of_query, replace_query
						from schnell.app.fmus.fileops import insert_at_lines, insert_after_query
						from schnell.app.fmus.fileops import insert_after_regex, insert_between_queries, replace_between_queries
						from schnell.app.fmus.fileops import inclusive_replace_between_queries_inclusive
						indah4(f"""[generator] oper [{oper}], found fileops_operation => {item.fileops_operation}
	fileops_attributes = {item.fileops_attributes}
	filepath = {item.workdir}
	item = {item}
	isi file:
	""", warna='black', layar='red')
						print('------------START')
						os.system(f'head -50 {item.workdir}')  # jangan cat...
						print('\n------------END')

						fileops_data_type = item.fileops_attributes['data_type']
						processing_data = item.fileops_attributes['line_data']

						if fileops_data_type in ['line_data_literal', 'string_data_literal']:
							pass
						elif fileops_data_type in ['line_data_filepath', 'string_data_filepath']:
							processing_data = file_content(processing_data)
						elif fileops_data_type in ['line_data_fmus', 'string_data_fmus']:
							processing_data = get_definition_fmusfile_barisentry(processing_data)
						elif fileops_data_type in ['line_data_input', 'string_data_input']:
							processing_data = give_me(prompt=f'Masukkan data untuk {processing_data}', default_value='')
						elif fileops_data_type in ['line_data_url', 'string_data_url']:
							processing_data = get_url_content(processing_data)

						if item.fileops_operation == 'fileops_line_expression':
							'''
							contoh.txt,f(t=,@line=1,2,3|i+|(aku cuma))
							fileops_operation => fileops_line_expression
							fileops_attributes = {
								'line_operation': 'line_insert_after', 
								'line_data': 'aku cuma', 
								'line_query': ['1', '2', '3']
							}
							'''
							# sptnya operasi i+ atau i- akan jadi insert_at
							# karena kita specify lines to insert
							# if item.fileops_attributes['line_operation'] = line_insert_after
							# jk line query adlh [] maka minta insert at
							if isinstance(item.fileops_attributes['line_query'], list):
								string_to_insert = processing_data # item.fileops_attributes['line_data']
								lines_to_insert_at = item.fileops_attributes['line_query']
								lines_to_insert_at = [int(i) for i in lines_to_insert_at]
								# insert_at_lines(filepath, string_to_insert, lines_to_insert_at, encoding='utf-8')
								insert_at_lines(item.workdir, string_to_insert, lines_to_insert_at)

						elif item.fileops_operation == 'fileops_line_contains':
							'''
							found fileops_operation => fileops_line_contains
							fileops_attributes = {
								'line_operation': 'line_insert_after', 
								'line_data': 'aku cuma', 
								'line_query': 'find me goose'
							}
							'''
							if item.fileops_attributes['line_operation'] == 'line_insert_after':
								query = item.fileops_attributes['line_query']
								string_to_insert = processing_data # item.fileops_attributes['line_data']
								insert_after_query(query, item.workdir, string_to_insert, encoding='utf-8')

						elif item.fileops_operation == 'fileops_line_matches':
							if item.fileops_attributes['line_operation'] == 'line_insert_after':
								# g "fileops_line_matches.txt,f(@line~(find me goose)|i+|(aku cuma), n=baris1__NL__fake info for you__NL__rather find me goose rather long__NL__baris4__NL__baris5)"
								regex_pattern = item.fileops_attributes['line_query']
								string_to_insert = processing_data # item.fileops_attributes['line_data']
								insert_after_regex(regex_pattern, item.workdir, string_to_insert, encoding='utf-8')
							# elif item.fileops_attributes['line_operation'] == 'line_replace_at':
							# 	pass
							print('------------result: START')
							os.system(f'cat {item.workdir}')
							print('\n------------result: END')

						elif item.fileops_operation == 'fileops_line_between_contains':
							if item.fileops_attributes['line_operation'] == 'line_insert_after':
								# g "fileops_line_between_contains.txt,f(@btw>(start contains)(end contains)|i+|(aku cuma), n=baris1__NL__baris2__NL__pertama start contains__NL__baris3__NL__baris4__NL__kedua end contains__NL__baris5__NL__baris6)"
								query1 = item.fileops_attributes['line_query_start']
								query2 = item.fileops_attributes['line_query_end']
								string_to_insert = processing_data # item.fileops_attributes['line_data']
								insert_between_queries(query1, query2, item.workdir, string_to_insert, encoding='utf-8')
							print('------------result: START')
							os.system(f'cat {item.workdir}')
							print('\n------------result: END')

						elif item.fileops_operation == 'fileops_line_between_matches':
							if item.fileops_attributes['line_operation'] == 'line_replace_at':
								# g "fileops_line_between_matches.txt,f(@btw~(start contains)(end contains)|r|(aku cuma), n=baris1__NL__baris2__NL__pertama start contains__NL__baris3__NL__baris4__NL__kedua end contains__NL__baris5__NL__baris6)"
								query1 = item.fileops_attributes['line_query_start']
								query2 = item.fileops_attributes['line_query_end']
								string_to_replace = processing_data # item.fileops_attributes['line_data']
								replace_between_queries(query1, query2, item.workdir, string_to_replace, encoding='utf-8')
							elif item.fileops_attributes['line_operation'] == 'line_replace_at_inclusive':
								# g "fileops_line_between_matches.txt,f(@btw~(start contains)(end contains)|ri|(aku cuma), n=baris1__NL__baris2__NL__pertama start contains__NL__baris3__NL__baris4__NL__kedua end contains__NL__baris5__NL__baris6)"
								query1 = item.fileops_attributes['line_query_start']
								query2 = item.fileops_attributes['line_query_end']
								string_to_replace = processing_data # item.fileops_attributes['line_data']
								inclusive_replace_between_queries_inclusive(query1, query2, item.workdir, string_to_replace, encoding='utf-8')
							print('------------result: START')
							os.system(f'cat {item.workdir}')
							print('\n------------result: END')

						elif item.fileops_operation == 'fileops_string_before':
							# if fileops_data_type == 'string_data_literal':
							# 	# string_to_insert sudah ok
							# 	pass
							# elif fileops_data_type == 'string_data_filepath':
							# 	pass
							# elif fileops_data_type == 'string_data_fmus':
							# 	pass
							# elif fileops_data_type == 'string_data_input':
							# 	pass
							# elif fileops_data_type == 'string_data_url':
							# 	pass
							if item.fileops_attributes['string_operation'] == 'string_replace':
								# g "fileops_string_before.txt,f(@str-(LOOK TO THE LEFT)|r|(aku ganti semua string di belakangmu), n=ini isi file ...LOOK TO THE LEFT... bohongan3)"
								replace_left_of_query(item.fileops_attributes['string_query'], item.workdir, processing_data)
							print('------------result: START')
							os.system(f'cat {item.workdir}')
							print('\n------------result: END')

						elif item.fileops_operation == 'fileops_string_after':
							# if fileops_data_type == 'string_data_literal':
							# 	# string_to_insert sudah ok
							# 	pass
							# elif fileops_data_type == 'string_data_filepath':
							# 	pass
							# elif fileops_data_type == 'string_data_fmus':
							# 	pass
							# elif fileops_data_type == 'string_data_input':
							# 	pass
							# elif fileops_data_type == 'string_data_url':
							# 	pass
							if item.fileops_attributes['string_operation'] == 'string_replace':
								# g "fileops_string_after.txt,f(@str+(ALLOWED_HOSTS)|r|(aku ganti semua string setelah mu dalam barismu), n=ini isi file bohongan2__NL__ini baris2__NL__nilai ALLOWED_HOSTS=gak tau__NL__ini baris3)"
								replace_right_of_query(item.fileops_attributes['string_query'], item.workdir, processing_data)
							print('------------result: START')
							os.system(f'cat {item.workdir}')
							print('\n------------result: END')

						elif item.fileops_operation == 'fileops_string_at':
							# if fileops_data_type == 'string_data_literal':
							# 	# string_to_insert sudah ok
							# 	pass
							# elif fileops_data_type == 'string_data_filepath':
							# 	pass
							# elif fileops_data_type == 'string_data_fmus':
							# 	pass
							# elif fileops_data_type == 'string_data_input':
							# 	pass
							# elif fileops_data_type == 'string_data_url':
							# 	pass
							if item.fileops_attributes['string_operation'] == 'string_replace':
								# g "fileops_string_at.txt,f(@str=(GANTI AKU DONG)|r|(aku ganti dirimu yang jelek itu), n=ini isi file bohongan1 isinya juga bohongan /GANTI AKU DONG/ tapi jangan bilang siapa2)"
								replace_query(item.fileops_attributes['string_query'], item.workdir, processing_data)
							print('------------result: START')
							os.system(f'cat {item.workdir}')
							print('\n------------result: END')

					else:

						if env_int('ULIBPY_FMUS_DEBUG')>1:
							indah4(f"[generator] oper [{oper}], no fileops_operation in {item}", warna='red')

			elif item.type == 'dir':
				"""
				name='coba', old_name='__TEMPLATE_DJANGOPROJECT'
				jk name dan old_name berbeda, berarti hasil __INPUT__
				hrs rubah workdir utk tiap anak
				%__TEMPLATE_DJANGOPROJECT=__INPUT__ <- ini dimana sih diubahnya?
				__TEMPLATE_DJANGOPROJECT,d <- ini dimana diubahnya...
				"""
				if is_debugging:
					indah4(f"""[generator|dir] [item.original={item.original}]
					item = {item}
					""", warna='magenta')

				# coba 24/7/23 bisa opendir
				if '__OPENDIR__' in item.workdir:
					'''contoh:
					__OPENDIR__,d
						/ketik)dir
					'''
					from schnell.app.promptutils import opendirdialog as notused, tkopendir as opendirdialog
					direktori_baru = opendirdialog(initial_directory=os.getcwd())
					# ternyata survey bermasalah, bisa dicek g "__OPENDIR__,d"
					# if not env_get('__USE_TK_FOR_FMUS_BACKEND__'):  # sekedar bikin False krn __USE_TK_FOR_FMUS_BACKEND__ memang belum ada
					# 	from schnell.app.promptutils import opendirdialog as notused, tkopendir as opendirdialog
					# 	direktori_baru = opendirdialog(initial_directory=os.getcwd())
					# else:
					# 	from schnell.app.filemanager.survey_browser import folder_browser
					# 	direktori_baru = folder_browser(item.workdir.replace('__OPENDIR__', '.'))  # jgn lupa hapus dulu __OPENDIR__

					# @TODO:
					# ubah __PWD__ atau __CURDIR__ utk masuk ke direktori_baru?
					direktori_lama = item.workdir
					item.workdir = normy(direktori_baru)
					print(f"[generator|dir] pindah ke direktori_baru = {direktori_baru}. item = {item}.")
					# skrg yg hrs dilakukan adlh ganti semua direktori_lama dg direktori_baru pada setiap anak
					# untung sudah ada di sysop_command contohnya
					# berkat: /ketik)grep -r -n -s -H -I "get_all_tree_children" ULIBPY_ROOTDIR/schnell/app
					for anak in get_all_tree_children(item):
						anak.workdir = normy(anak.workdir.replace(direktori_lama, item.workdir))

				if hasattr(root_tree, 'variables'):
					butuh_reworkdir_siblings_dan_children = False
					nama_lama_yang_harus_diganti = item.name
					nama_baru_sebagai_pengganti = item.name
					if item.name in root_tree.variables:
						indah4(f"""[generator|dir] jika root_tree punya variables, cek item.name jk ada di situ
						root_tree.variables = {root_tree.variables}
						item.name = {item.name}
						item.workdir = {item.workdir}
						""", warna='magenta')
						nama_lama_yang_harus_diganti = item.name
						nama_baru_sebagai_pengganti = root_tree.variables[nama_lama_yang_harus_diganti]
						item.name = nama_baru_sebagai_pengganti
						item.workdir = normy(item.workdir.replace(nama_lama_yang_harus_diganti, nama_baru_sebagai_pengganti))
						if item.name != nama_lama_yang_harus_diganti:
							butuh_reworkdir_siblings_dan_children = True
					else:
						nama_lama_yang_harus_diganti = item.name
						# bisa saja item.name+workdir berbentuk dir1/dir2/kuncirootitem, bukan kuncirootitem saja.
						# contoh kuncirootitem adlh NAMAFOLDER dan nilairootitem adlh de/fulgent/oefening
						# shg item.name = dir1/dir2/NAMAFOLDER
						# hrs menjadi = dir1/dir2/de/fulgent/oefening
						# nama_baru_sebagai_pengganti harus memegang "de/fulgent/oefening"
						# dan bukannya "dir1/dir2/de/fulgent/oefening"
						for kuncirootitem,nilairootitem in root_tree.variables.items():
							nama_baru_sebagai_pengganti = nilairootitem
							item.name = item.name.replace(kuncirootitem, nilairootitem)
							item.workdir = normy(item.workdir.replace(kuncirootitem, nilairootitem))
						if item.name != nama_lama_yang_harus_diganti:
							butuh_reworkdir_siblings_dan_children = True
					if butuh_reworkdir_siblings_dan_children:
						from .treehelper import recursive_callback_for_bawahan
						# item.workdir sodara diubah
						# item.workdir children diubah
						def panggil_balik(benda):
							benda.workdir = normy(benda.workdir.replace(nama_lama_yang_harus_diganti, nama_baru_sebagai_pengganti))
						recursive_callback_for_bawahan(item, panggil_balik)

				if not isdir(item.workdir):
					if is_debugging:
						indah4(f'''[generator|dir] [create_dir] name={item.name}, workdir={item.workdir}
						nama folder utk dibuat: {item.name}
						create dir	: {item.workdir}
						item 		: {item}
						cek di bawah ini utk root_tree.variables.
						root 		: {root_tree}
						''', warna='magenta')
						input('Press any key... ')
					create_dir(item.workdir)
				# else:
				# 	if is_debugging:
				# 		indah4(f'''[generator] item.type == 'dir' / not create_dir
				# 		item.type == 'dir'
				# 		item.workdir {item.workdir} is dir? => {isdir(item.workdir)}
				# 		''', warna='cyan')

				if is_debugging:
					indah4(f'''[generator|dir] after create or not create_dir
					item.type == dir (dari: nama,d)
					workdir		: {item.workdir}
					item 		: {item}
					os.chdir(item.workdir): os.chdir({item.workdir})
					''', warna='black', layar='white')
				os.chdir(item.workdir)

			elif item.type == 'sysop_command':
				'''
				kok bisa belum masuk direktori item.workdir ???
				lihat pemrosesan generate
				for item in tree
					proses jk item.operations
					proses jk type=dir
						create if dont exist
						chdir
					proses jk type=$
					proses jk type=&
					proses jk type=%%%
					proses jk type=@
					proses jk type=#
					proses jk type=%
				'''
				from .sysop_command import sysop_command
				sysop_command(root_tree, item, capture_outerr, self.debug, self.parent_fmus, self.run_configuration)

			elif item.type == 'special_command':
				'''
				kita bikin di sini case dimana gak perlu nanya apa mau diexec:
				diawali dg * <- pastikan special_command bs handle char *
					&*showtext
				env var ULIBPY_FORCEABLE_YES == 1
				jawab yes pd prompt
				'''
				from .special_command import special_command
				special_command(root_tree, item, self.debug)

			elif item.type == 'quick_command' or item.type == 'empty_quick_command':
				# quick_command /something
				from .quick_command import quick_command
				try:
					if is_debugging:
						indah4('>>before quick command', warna='cyan')
					quick_command(root_tree, item, self.run_configuration['replacer'], self.run_configuration)
					# if is_debugging:
					# 	indah4('>>after quick command', warna='cyan')
				except Exception as err:
					indah4(f"""😭😭😭 [generator][exception pada quick_command/empty_quick_command][{item.original}]
					err = {err}
					item = {item}
					parent = {item.parent}
					root = {root_tree}
					trace:
					{traceback.format_exc()}
					""", warna='red', layar='black')

			elif item.type == 'user_command':
				from .user_command import user_command
				user_command()

			elif item.type == 'pesan_instruksi':
				from .pesan_instruksi import pesan_instruksi
				# utk bisa __FILE, __IF_ETH0 di @...pesan instruksi...
				# indah4('sebelum pemanggilan pesan_instruksi, item adlh: ' + item, warna='yellow', layar='blue')
				item.replacer = self.run_configuration['replacer']
				pesan_instruksi(item, self.run_configuration, is_debugging)

			elif item.type == 'komentar_untuk_instruksi_selanjutnya':
				'''ini dari #(file=baris)
				item.content adlh hasil get definition di BaseDefinitor
				'''
				from .komentar_untuk_instruksi_selanjutnya import komentar_untuk_instruksi_selanjutnya
				komentar_untuk_instruksi_selanjutnya(item)

			elif item.type == 'pesan_instruksi_selanjutnya':
				'''dari @(file=baris)
				'''
				from .pesan_instruksi_selanjutnya import pesan_instruksi_selanjutnya
				pesan_instruksi_selanjutnya(item)

			elif item.type == 'simpan_temp_vars':
				# kita bikin item.variables bisa terima input dari user
				from .simpan_temp_vars import simpan_temp_vars
				simpan_temp_vars(root_tree, item, is_debugging, self.run_configuration)

			elif item.type == 'branching':
				from .branching import branching
				branching(root_tree, item)

			elif item.type == 'looping':
				if is_debugging:
					indah4(f"[generator] looping (while or unless)\n", warna='blue')
				execute = item.execute
				if hasattr(item, 'branch_condition') and len(item.branch_condition)>0:
					'''
					konsep
					a
						b
							c
								d <- while
									1
									2
									3
									4
									5
									<- stlh 5 kita hrs bisa masuk lagi ke d
								e <- hrs punya handle ke e
									^ e bisa satu parent dg while atau beda!
									sebaiknya cantol/handle ke 5...lebih deterministik
									but how...
								f
							g
						h
					i
					strategi 1:
					kita cantol ke 5 = while_requirements (parent dari 5 = while loop)
					di akhir generate_iterate cek jk item punya while_requirements
					maka recursive panggil itu dulu (while_requirements = while_loop = parent)
					cantolan adlh deepcopy terhadap while loop (dan anak2nya)
					'''
					if is_debugging:
						indah4(f'[generator] condition: {item.branch_condition}.', warna='blue')
					default_while = item.branch_condition
					default_unless = item.branch_condition
				else:
					default_while = ['y', 'yes']
					default_unless = ['x', 'q']

				lanjut = False

				if item.loop_type == 'while':

					list_item = '\n'.join([f'  {idx}. '+i.original for (idx,i) in enumerate(item.children,1)])

					if is_debugging:
						indah4('[while loop] extra info ' + json.dumps(item.branch_extra_info,indent=2), warna='cyan')

					if item.branch_extra_info:
						if '__PROCESS_FILES' in item.branch_extra_info:
							if item.branch_extra_info['__PROCESS_FILES']:
								nilai_pertama = item.branch_extra_info['__PROCESS_FILES'][0]
								# ambil file pertama dan jadikan sbg __CURFILE__ dalam replacer
								# yg sudah bisa handle replacer: @, $, dst.
								self.run_configuration['replacer']['__CURFILE__'] = nilai_pertama
								# pastikan yg sudah diambil, dibuang utk visit berikutnya
								item.branch_extra_info['__PROCESS_FILES'].pop(0)
								lanjut = True
						elif '__PROCESS_STRINGS' in item.branch_extra_info:
							if item.branch_extra_info['__PROCESS_STRINGS']:
								nilai_pertama = item.branch_extra_info['__PROCESS_STRINGS'][0]
								self.run_configuration['replacer']['__CURSTR__'] = nilai_pertama
								item.branch_extra_info['__PROCESS_STRINGS'].pop(0)
								lanjut = True
						elif '__PROCESS_COMMAS' in item.branch_extra_info:
							if item.branch_extra_info['__PROCESS_COMMAS']:
								nilai_pertama = item.branch_extra_info['__PROCESS_COMMAS'][0]
								self.run_configuration['replacer']['__CURCOMMA__'] = nilai_pertama
								# pastikan yg sudah diambil, dibuang utk visit berikutnya
								item.branch_extra_info['__PROCESS_COMMAS'].pop(0)
								lanjut = True
					else:
						# indah4(f"""[{item.workdir}:while] Masukkan {default_while} untuk execute ('Enter' untuk quit)\n{list_item}\n=>""", warna='green', newline=False)
						indah4(f"""[while] Masukkan {default_while} untuk execute ('Enter' untuk quit)\n{list_item}\n=>""", warna='cyan', newline=False)
						terima = input(' ')
						if terima in default_while:
							# jk yg dimasukkan ada dalam item.branch_condition
							# maka ulang terus
							lanjut = True
				else:
					# terima = input(f"[{item.workdir}:unless] Masukkan {default_unless} untuk mengakhiri: ")
					indah4(f"""[unless] Masukkan {default_unless} untuk mengakhiri:""", warna='cyan', newline=False)
					terima = input(' ')
					if terima not in default_unless: # not in...
						lanjut = True
					else:
						lanjut = False
						# indah0('Quitting unless loop', warna='red', bold=True)
						# input(' ')

				if lanjut:
					if env_int('ULIBPY_FMUS_DEBUG') > 1:
						indah4('[generator] looping: kita masuk lanjut...', warna='blue')

					while_requirements = copy.deepcopy(item)

					# terakhir = get_last_direct_children(item)
					# dari sebuah loop, anak terakhir kasih cantolan while_requirements 
					# agar bisa balik ke while_loop di awal

					# get last absolute ini hanya jk direct child bukan ?pick
					# jk ?pick maka cukup pick saja...
					if len(item.children)==1 and item.children[0].original == '?pick':
						terakhir = item.children[0]
						terakhir.please_bestow_while_requirements_to_executed_children = while_requirements
						if env_int('ULIBPY_FMUS_DEBUG') > 1:
							indah4(f'''[generator]
								hooray, ?pick jadi anak tunggal dg while_requirements
								{terakhir}
								''', warna='cyan')

						# jk ~unless punya direct dan 1 anak = ~pick
						# problem: dari ~unless ke ~pick tapi anak ~pick gak sempat diexec
						# krn keburu loop lagi ke ~unless

					else:
						from .helper.generator import add_while_requirements_to_absolute_last_child
						item = add_while_requirements_to_absolute_last_child(item, while_requirements)

				else: # not lanjut/execute badan while/unless
					# skip semua...
					# set_attr_direct_children(item, 'skip', True)
					for cabang in get_all_tree_children(item):
						cabang.skip = True

			elif item.type == 'pickone_ormore':

				direct_children = [node for node in item.children]
				indexes = [n+1 for n in range(len(direct_children))]

				if is_debugging:
					indah(f"""\n[generator] pickone_ormore: {item.replacer['__FILE__']}
						item = {item}

						parent = {item.parent}
						""", warna='red', layar='white', reverse=True, newline=True)
					# indah0(f"\n[generator] pickone_ormore: {item}\n", warna='yellow', reverse=True, newline=True)

				# kita gak oprek 999 = input
				if hasattr(item, 'pickone_condition'): # ?pick[#,i,dst]
					# statically pick children yg dispecified di [choose_number, choose_number]
					condition = item.pickone_condition
					# condition ini berisi angka item/child atau 999 utk minta input
					# jadi len(condition) <= len(direct children)
					last_executed_children_index = 0
					last_executed_children_node = None
					for index, node in enumerate(direct_children, 1):
						if index in condition:
							node.skip = False
							last_executed_children_index = index
							last_executed_children_node = node
						else:
							node.skip = True

					if last_executed_children_index > 0 and last_executed_children_node:
						if hasattr(item, 'please_bestow_while_requirements_to_executed_children'):
							# abs children dari node bukan item (?pick) krn ada node lain yg gak kexec
							terakhir = get_last_absolute_children(last_executed_children_node)
							if terakhir:
								terakhir.while_requirements = item.please_bestow_while_requirements_to_executed_children

					if is_debugging:
						print_ready = [f"Execute {idx}. {self.get_content(node)} = {'No' if node.skip else '<<Yes>>'} " for idx,node in enumerate(direct_children)]
						indah0(json.dumps(print_ready, indent=4), warna='white', bold=True, newline=True)
				else: # ?pick
					# ini agar visibility luas
					if is_debugging:
						indah0(get_root(item).source_code, warna='green', layar='white', bold=True, newline=True)

					# verbose = int(env_get('ULIBPY_VERBOSITY'))
					# if verbose == 1:
					# 	indah0(json.dumps([f"{angka}. {self.get_content(node)}" \
					# 		for angka,node in enumerate(direct_children, 1)], \
					# 		indent=4), warna='white', bold=True, newline=True)
					# elif verbose == 2:
					# 	indah0(json.dumps([f"{angka}. {node.name}/{node.type}{self.get_content(node)}" \
					# 		for angka,node in enumerate(direct_children, 1)], \
					# 		indent=4), warna='white', bold=True, newline=True)
					# elif verbose == 3:
					# 	indah0(json.dumps([f"{angka}. {node.name}/{node.type}{self.get_content(node)} => {node}" \
					# 		for angka,node in enumerate(direct_children, 1)], \
					# 		indent=4), warna='white', bold=True, newline=True)

					# print_list_warna(the_list, genap='yellow', ganjil='green', bold=True, berwarna=True, special_ends=None, start=0, extra_warna={})
					the_list = [f"{self.get_content(node)}" for angka,node in enumerate(direct_children, 1)]
					# print_list_warna(the_list, genap='green', ganjil='white', start=1, prefix='  ')

					# else:
					'''
					ada masalah dg direct_children ternyata...
					jk berindent spt ini
					a
						b
							c
					b sbg direct children tdk diexec, tapi c jadi diexec
					UPDATE:
					a
						b
						c
							d
					ternyata ini harus di awal sebelum minta masukan
					why?
					krn jk kita pilih b stlh prompt,
					ternyata d jadi diminta, padahal kita pengen bypass
					'''
					# for index, node in enumerate(direct_children, 1):
					for index, node in enumerate(get_all_tree_children(item), 1):
						node.skip = True

					message = f'[{item.workdir}]\nEnter your choice:'
					# indah4(message, warna='yellow', newline=False)
					# masukan = input(f' ')
					masukan_list = checkbox_select(the_list, message)
					masukan = ','.join([str(e) for e in masukan_list])
					# validasi
					if masukan:
						# berarti ini bisa pick lebih dari satu
						pecah = [bersih.strip() for bersih in masukan.split(',')]
						condition = []
						for cond in pecah:
							if cond.isdigit() and int(cond) in indexes:
								nilai = int(cond)
								condition.append(nilai)
							else:
								indah0(f'Skipping invalid [{cond}] from [{indexes}]...', warna='red', reverse=True, newline=True)
						if condition:
							'''
							UPDATE:
							utk child yg skip = False maka hrs dilakukan utk semua child nya.
							krn kasus ini:
							?pick
								a
									b
									c
								d
									e
									f
								jk kita pilih a dan a adlh dir, maka b dan c gak exec.
							'''
							for index, node in enumerate(direct_children, 1):

								if index in condition:

									node.skip = False
									# tambah utk semua anak, jadi ikut terexecuted
									for index2, node2 in enumerate(get_all_tree_children(node), 1):
										node2.skip = False

									if hasattr(item, 'please_bestow_while_requirements_to_executed_children'):
										# abs children dari node bukan item (?pick) krn ada node lain yg gak kexec
										terakhir = get_last_absolute_children(node)
										if terakhir:
											terakhir.while_requirements = item.please_bestow_while_requirements_to_executed_children

								else:
									node.skip = True

							if is_debugging:
								print_ready = [f"{'skipping' if node.skip else '***'} {idx}. {self.get_content(node)} = {'No' if node.skip else '<<Yes>>'} " for idx,node in enumerate(direct_children)]
								indah0(json.dumps(print_ready, indent=4), warna='white', bold=True, newline=True)

			if hasattr(item, 'while_requirements'):

				# which_parent = item.parent
				# while which_parent.type != 'looping':
				# 	which_parent = which_parent.parent

				# indah0(f"[generator] ************* LOOPING {item.while_requirements} *************\noleh item: {item}\n", warna='red', layar='white', bold=True, reverse=True, newline=True)

				self.generate_iterate(item.while_requirements, projectdir)
