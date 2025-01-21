
from app.printutils import print_json
from anytree import RenderTree
from app.treeutils import (
	data, 
	token, 
	child1, 
	child2, 
	child3, 
	child4,
	child,
	chdata,
	chtoken,
	anak, 
	ispohon, istoken,
	beranak,
	sebanyak,
	jumlahanak, 
)

from app.transpiler.frontend.fslang.common import program_config
from .misc import (
	quickrepl_generator,
	simplepython_generator,
	crajs_generator,
	crats_generator,
	simpleunittest_generator,
	pytrayicon_generator,
	langtemplate_generator,
	rustcli_generator,
	cppcli_generator,
	gocli_generator,
	indon_generator,
	sfxso_generator,
	jupy_generator,
	jupyuser_generator,
	electron_generator,
	be_django_corona_generator,
	be_node_corona_generator,
	qtcmake_generator,
	qtcmake2_generator,
	# new misc imports
	mongoseeder_generator,
	rustwarpsimplerest_generator,
	androidkotlinbasesunflower_generator,
	jfxso_generator,
	reactnative1_generator,
	tselflutter1_generator,
	htmlcss_generator,
)
from .utils import (
	proshop_routes_generator,
	relight_routes_generator,
	proshop_store_generator,
	proshop_backend_generator,
	ecommdj_generator,
	# new utils imports
	proshop_mern_generator,
	vertxspringboot_generator,
	proshop_node_generator,
)

generator_utils = {
	## utils
	'proshop_routes': proshop_routes_generator,
	'relight_routes': relight_routes_generator,
	'proshop_store': proshop_store_generator,
	'proshop_backend': proshop_backend_generator,
	'ecommdj': ecommdj_generator,
	# new gen utils entry
	'proshop_mern': proshop_mern_generator,
	'vertxspringboot': vertxspringboot_generator,
	'proshop_node': proshop_node_generator,
}
generator_by_backend = {

	## misc
	'quickrepl': quickrepl_generator,
	'simplepython': simplepython_generator,
	'crajs': crajs_generator,
	'crats': crats_generator,
	'simpleunittest': simpleunittest_generator,
	'pytrayicon': pytrayicon_generator,
	'langtemplate': langtemplate_generator,
	'rustcli': rustcli_generator,
	'cppcli': cppcli_generator,
	'gocli': gocli_generator,
	'indon': indon_generator,
	'sfxso': sfxso_generator,
	'jupy': jupy_generator,
	'jupyuser': jupyuser_generator,
	'electron': electron_generator,
	'be_django_corona': be_django_corona_generator,
	'be_node_corona': be_node_corona_generator,
	'qtcmake': qtcmake_generator,
	'qtcmake2': qtcmake2_generator,
	# new gen misc entry
	'mongoseeder': mongoseeder_generator,
	'rustwarpsimplerest': rustwarpsimplerest_generator,
	'androidkotlinbasesunflower': androidkotlinbasesunflower_generator,
	'jfxso': jfxso_generator,
	'reactnative1': reactnative1_generator,
	'tselflutter1': tselflutter1_generator,
	'htmlcss': htmlcss_generator,
}

backend_config = {}
generator_by_backend.update(generator_utils)

def get_konfigurasi_backend():
	hasil = None
	try:
		hasil = program_config['config']['be']
	except Exception as e:
		print('Gagal get_konfigurasi_backend() / Exception: '+str(e) + '\nprogram_config:')
		print_json(program_config)
		hasil = program_config["be"]
	return hasil


def backend_statement(tree):
	print('backend_statement:', data(tree))
	dummy_argument = tree
	if program_config['config']['be'] in generator_utils.keys():
		print(f'lihat struktur tree hrs berisi csv program:')
		print('jenis adlh:', type(tree))
		print('jk dia adlh token:', tree)
		if data(tree) == 'backend_statement':
			if chdata(tree) == 'program_backend':
				program = chtoken(tree)
				print('\n\nharusnya oprek program:', program)
				from langs.ucsv import processor
				RootNode = processor(program, print)
				dummy_argument = RootNode
		# jk dia adlh token:
		# Tree('backend_statement', [Tree('program_backend', [Token('HURUF_PROGRAM_BACKEND', '{@Product}name,s;price,n')])])
		# print(RenderTree(tree))
		# input('Press any routes key to continue')
	konfigurasi_backend = get_konfigurasi_backend()
	generator = generator_by_backend[konfigurasi_backend] (dummy_argument)
	generator.generate()
	backend_config.update({
		'filepath': generator.output(),
		'baris_entry': 'index/fmus',
	})
	return backend_config
