from schnell.app.printutils import (
	Debug,
	dir_w,
	filter_print_latest_files,
	indah, 
	indah0, 
	indah4,
)
from schnell.app.utils import (
	# trycopy,
	# trypaste,
	# yesno,
	env_set,
	env_get, 
	env_int,
	env_exist,
	# env_expand,
	# perintahsp_outerr,
	# perintahsp_outerr_as_shell,
)
from ..common import Common, input_keyword
from ..treehelper import (
	get_all_tree_children,
	get_last_absolute_children,
)

def add_while_requirements_to_absolute_last_child(item, while_requirements):

	terakhir = get_last_absolute_children(item)

	if terakhir:
		terakhir.while_requirements = while_requirements

		for anak in get_all_tree_children(item):

			if env_int('ULIBPY_FMUS_DEBUG') > 1:
				indah4(f"""[helper.generator] while_requirements anak.original: {anak.original} => {anak}""", warna='white')

			if hasattr(anak, 'replacer'):
				if '__COUNTER__' in anak.replacer:
					anak.replacer['__COUNTER__'] += 1
				else:
					anak.replacer['__COUNTER__'] = 1
			else:
				anak.replacer = {
					'__COUNTER__' : 1,
				}

			# bbrp node gak bisa direcover misal yg berhub dg input_keyword
			# krn node dimodifikasi langsung sambil jalan
			# -----------------------------------------------
			# anak: input,d(/mk) => 
			# AnyNode(counter=4, level=2, 
			# name='tiga', old_name='input', operations=['create_dir'], 
			# original='input,d(/mk)', 
			# replacer={'__COUNTER__': 2}, type='dir', 
			# workdir='/tmp/sample/tiga')
			# bbrp kita recover manual
			recover_createdir_input = True
			if recover_createdir_input:
				if input_keyword in anak.original:
					if hasattr(anak, 'old_name') \
						and input_keyword == anak.old_name \
						and anak.name != anak.old_name:
						'''coba ganti workdir dan name kembali agar mengandung "input"'''
						# indah4(f'[generator/generate_iterate] ganti nama pada workdir dari [{anak.name}] ke [{anak.old_name}]', warna='red', layar='white')
						anak.workdir = anak.workdir.replace(anak.name, anak.old_name)
						anak.name = anak.old_name
					elif anak.type == 'simpan_temp_vars':
						'''
						node %... sudah berubah dari aslinya:
						AnyNode(counter=-1, level=3, 
						name='info', 
						original='%__modelname=input', 
						replacer={'__COUNTER__': 1}, 
						type='simpan_temp_vars', 
						variables={'__modelname': 'input'}, <- yg berubah cuma ini
						workdir='/tmp/hapus/django-starter1/apps')

						menjadi:
						AnyNode(counter=-1, level=3, 
						name='info', 
						original='%__modelname=input', 
						replacer={'__COUNTER__': 1}, 
						type='simpan_temp_vars', 
						variables={'__modelname': 'user'}, <- yg berubah cuma ini
						workdir='/tmp/hapus/django-starter1/apps')
						'''
						# dapatkan kata = '__modelname'
						original_varname = anak.original.split('=')[0].lstrip('%')
						if hasattr(anak, 'variables') and original_varname in anak.variables:
							anak.variables[original_varname] = input_keyword

		if env_int('ULIBPY_FMUS_DEBUG') > 1:
			indah4(f'*** [helper.generator] node ini berisi code utk diexec berulang: {terakhir}', warna='yellow')

	return item