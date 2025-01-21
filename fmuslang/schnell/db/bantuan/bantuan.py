import re, sys
from anytree import RenderTree
from schnell.app.dirutils import joiner, here, isdir
from schnell.app.envvalues import bylangs_relative
from schnell.app.fileutils import file_content, lines_skip_lines_from_string
from schnell.app.printutils import indah3
from schnell.app.utils import env_get, env_int, env_exist
from schnell.langs.ucsv import processor
from .category import category_map, frontend_map


# if not env_exist('ULIBPY_BYLANGSDIR'):
# 	bylangsdir = bylangsdir_func()
# else:
# 	bylangsdir = env_get('ULIBPY_BYLANGSDIR')
bylangsdir = bylangs_relative

class Bantuan:

	# pindah
	# helpfile = joiner(here(__file__), 'HELP.txt')
	helpfile = joiner(bylangsdir, 'mapper', 'HELP.txt')


	def __init__(self):
		self.output = ''
		self.metaresult = {}


	def help(self, code=None):
		"""
		help|filtering words
		help|+5|
		help|-5|
		help|=5|
		update:
		kita tambah bisa konteks -A, -B, -C    
		"""
		content = file_content(self.helpfile)
		if code .startswith('|'):
			filtercode = code.removeprefix('|')			
			m = re.match(r'^(\+|\-|=)(\d+)\|(.*)$', filtercode)
			if m is None:
				'''
				help|angka|word
				atau
				help|word
				'''
				m = re.match(r'^(.*)$', filtercode)
				if m is None:
					return "Tidak ditemukan"
				filterword = m.group(1)
				content = lines_skip_lines_from_string(content, filterword, isFiltering=True)
				return content

			print('filtercode:', filtercode, 'm:', m.groups())
			if m and m.group(1) and m.group(2) and m.group(3):
				print('terima:', m.groups())
				tanda = m.group(1)
				jumlah = int(m.group(2))
				filterword = m.group(3)
				print(f'tanda: {tanda}, jumlah = {jumlah}, kata = {filterword}')
				if tanda == '+':
					content = lines_skip_lines_from_string(content, filterword, isFiltering=True, after=jumlah)
					print('after:', content)
				elif tanda == '-':
					content = lines_skip_lines_from_string(content, filterword, isFiltering=True, before=jumlah)
					print('before:', content)
				elif tanda == '=':
					content = lines_skip_lines_from_string(content, filterword, isFiltering=True, after=jumlah, before=jumlah)
					print('context:', content)
				return content
			elif filtercode:
				content = lines_skip_lines_from_string(content, filtercode, isFiltering=True)
				print('lines_skip_lines_from_string content:', content, 'dari filter:', filtercode)
		indah3(content, warna='white')
		return content


	def frontend(self, code, frontend_category):
		if frontend_category in frontend_map:
			self.output = frontend_map.get(frontend_category, lambda x:'') (code)

		return self.output, self.metaresult


	def new_generate(self, category, config, program):
		"""
		result, meta = bantupeople.new_generate(category, config, program)
		config
			__TEMPLATE_PROJECT_DIR__ -> lokasi basedir atau input
			__TEMPLATE_MTS_DIR__ -> lokasi source react
			__TEMPLATE_WEBPACK_NAME__ -> nama webpack...dg default
		"""
		from schnell.db.bantuan.frontend.bantu_react.bantu_react import bantu_react
		return bantu_react(category, config, program)


	def generate(self, code, category):
		"""
		category: django, fake, etc
		RootNode digeneate dari langs.ucsv
		"""
		RootNode = processor(code, print)
		print(RenderTree(RootNode))
		if category in category_map:
			# self.output = category_map[category] (RootNode)
			self.output = category_map.get(category, lambda x:'') (RootNode)

		return self.output, self.metaresult


	def dahsyat(self, text):
		"""
		semua digenerate.
		replservice.py:
		*!dahsyat:/tmp/hapus/whatever|codes
		*!dahsyat:/tmp/hapus/whatever:1,2,3,4,5|codes
		bantuan.py:
		/tmp/hapus/whatever|codes
		"""
		from .dahsyat.config import project_names
		project_terpilih = project_names
		print('dahsyat:', text)
		folder, code = text.split('|', 1) # hanya 1 krn code bisa berisi |
		if ':' in folder:
			'''
			*!dahsyat:/tmp/hapus/whatever:1,2,3,4,5|codes
			/tmp/hapus/whatever:1,2,3,4,5|codes
			^folder             ^saring
			but:
			c:/tmp/hapus1:1,2,3,4,5|codes
			c:/tmp/hapus1
									 :
									  1,2,3,4,5|codes
			'''
			if sys.platform == 'win32':
				folder, saring = folder.rsplit(':', 1)
			else:
				folder, saring = folder.split(':')
			if ',' in saring:
				project_pilihan = [int(angka) for angka in saring.split(',')]
				# ini hasilkan: django, flask, fastapi, dll
				project_terpilih = [item for item in project_terpilih if project_terpilih[item]['id'] in project_pilihan]
			else:
				project_terpilih = [item for item in project_terpilih if project_terpilih[item]['id'] == int(saring)]
		# else:
		# 	input(f'tidak terdeteksi : dari dalam {folder} dari sumber: {text}')
		
		# input(f'folder skrg yg mau dibuat adlh: {folder}')

		if not isdir(folder):
			from schnell.app.dirutils import first_part, create_dir_with_parent
			if first_part(folder) and isdir(first_part(folder)):
				create_dir_with_parent(folder)

		if isdir(folder) and code:
			from schnell.app.appconfig import bantuan_data
			from schnell.app.fmus import Fmus

			bantuan_data['bantuan_basedir'] = folder
			RootNode = processor(code, print)
			print(RenderTree(RootNode))

			fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))

			for project in project_terpilih:
				# input(f'kerjakan {project} dari total {project_terpilih}')
				projectname = project
				# projectitem = project_names[project]
				self.output += f'siap2 generate {projectname}...\n'
				theproject = project_names[projectname]
				project_base = theproject['project_dir']
				project_dir = joiner(folder, project_base)
				handler = theproject['handler']
				output_mkfile = handler(RootNode, project_dir, need_program_output=True)
				self.output += f'selesai generate {projectname} mkfile {output_mkfile}\n'
				baris_entry = 'program/fmus'
				cek_program_ketemu = fmus.process_mkfile(output_mkfile, baris_entry=baris_entry)
				if not cek_program_ketemu:
					self.output += f'Aborting process karena {baris_entry} tidak ditemukan di {output_mkfile}'
				else:
					self.output += f'selesai execute fmus utk django {output_mkfile}\n'
			return self.output, self.metaresult


bantupeople = Bantuan()
