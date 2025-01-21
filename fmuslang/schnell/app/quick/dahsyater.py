# dahsyater
from schnell.app.dirutils import joiner, get_cwd
from schnell.app.printutils import indah4
from schnell.app.utils import import_module, env_get, env_int
from schnell.app.fileutils import get_definition_by_key_permissive_start, file_content
from schnell.app.fmusutils import get_rootnode

from schnell.app.transpiler.frontend.fslang.django import Coordinator as dj_coordinator
from schnell.app.transpiler.frontend.fslang.dropwizard import Coordinator as dropwizard_coordinator
from schnell.app.transpiler.frontend.fslang.fastapi import Coordinator as fastapi_coordinator
from schnell.app.transpiler.frontend.fslang.flask import Coordinator as flask_coordinator
from schnell.app.transpiler.frontend.fslang.micronaut import Coordinator as micronaut_coordinator
from schnell.app.transpiler.frontend.fslang.nest import Coordinator as nest_coordinator
from schnell.app.transpiler.frontend.fslang.node_antd import Coordinator as noda_coordinator
from schnell.app.transpiler.frontend.fslang.springboot import Coordinator as sb_coordinator
from schnell.app.transpiler.frontend.fslang.quarkus import Coordinator as quarkus_coordinator

from schnell.app.transpiler.frontend.fslang.fullstack.assistance import Coordinator as assist_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.gin_gonic import Coordinator as gg_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.gin_gonic_simple import Coordinator as gingonic_simple_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.go_echo import Coordinator as echo_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.go_mux import Coordinator as mux_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_argon import Coordinator as nxargon_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_mkit import Coordinator as nxmkit_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_mui import Coordinator as nxmui_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_notus import Coordinator as nxnotus_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_tailwind import Coordinator as nxtw_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_ts1 import Coordinator as nxts1_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.next_ts2 import Coordinator as nxts2_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.node_next import Coordinator as nodenext_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.node_ts1_mg import Coordinator as nodetsmg_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_airframe import Coordinator as rair_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_argon import Coordinator as rargon_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_iot import Coordinator as riot_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_light import Coordinator as rlight_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_mkit import Coordinator as rmkit_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_mui import Coordinator as rmui_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_notus import Coordinator as rnotus_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_now import Coordinator as rnow_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_paper import Coordinator as rpaper_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_ts1 import Coordinator as rts1_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_volt import Coordinator as rvolt_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.react_xtreme import Coordinator as rxt_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.tokyo_white import Coordinator as tokyo_coordinator
from schnell.app.transpiler.frontend.fslang.fullstack.vue_materio import Coordinator as vue_coordinator

from schnell.app.transpiler.frontend.fslang.misc.androidkotlinbasesunflower import Coordinator as android_sunflower_coordinator
from schnell.app.transpiler.frontend.fslang.misc.be_django_corona import Coordinator as djcorona_coordinator
from schnell.app.transpiler.frontend.fslang.misc.be_node_corona import Coordinator as nodecorona_coordinator

from schnell.app.transpiler.frontend.fslang.misc.cppcli import Coordinator as cppcli_coordinator
from schnell.app.transpiler.frontend.fslang.misc.gocli import Coordinator as gocli_coordinator
from schnell.app.transpiler.frontend.fslang.misc.rustcli import Coordinator as rscli_coordinator

from schnell.app.transpiler.frontend.fslang.misc.crajs import Coordinator as crajs_coordinator
from schnell.app.transpiler.frontend.fslang.misc.crats import Coordinator as crats_coordinator
from schnell.app.transpiler.frontend.fslang.misc.cnxjs import Coordinator as cnxjs_coordinator
from schnell.app.transpiler.frontend.fslang.misc.cnxts import Coordinator as cnxts_coordinator

from schnell.app.transpiler.frontend.fslang.misc.electron import Coordinator as electron_coordinator

from schnell.app.transpiler.frontend.fslang.misc.htmlcss import Coordinator as htmlcss_coordinator
from schnell.app.transpiler.frontend.fslang.misc.indon import Coordinator as indon_coordinator

from schnell.app.transpiler.frontend.fslang.misc.jfxso import Coordinator as jfxso_coordinator
from schnell.app.transpiler.frontend.fslang.misc.jfxso2 import Coordinator as jfxso2_coordinator
from schnell.app.transpiler.frontend.fslang.misc.sfxso import Coordinator as sfxso_coordinator

from schnell.app.transpiler.frontend.fslang.misc.langtemplate import Coordinator as tplang_coordinator
from schnell.app.transpiler.frontend.fslang.misc.quickrepl import Coordinator as tprepl_coordinator

from schnell.app.transpiler.frontend.fslang.misc.mongoseeder import Coordinator as mgseed_coordinator
from schnell.app.transpiler.frontend.fslang.misc.pytrayicon import Coordinator as pytray_coordinator
from schnell.app.transpiler.frontend.fslang.misc.qtcmake import Coordinator as qtcm1_coordinator
from schnell.app.transpiler.frontend.fslang.misc.qtcmake2 import Coordinator as qtcm2_coordinator
from schnell.app.transpiler.frontend.fslang.misc.reactnative1 import Coordinator as rn1_coordinator

from schnell.app.transpiler.frontend.fslang.misc.rustwarpsimplerest import Coordinator as rswarp_coordinator
from schnell.app.transpiler.frontend.fslang.misc.simplepython import Coordinator as simplepy_coordinator
from schnell.app.transpiler.frontend.fslang.misc.simpleunittest import Coordinator as simpleunittest_coordinator
from schnell.app.transpiler.frontend.fslang.misc.tselflutter1 import Coordinator as tselflutter1_coordinator

from schnell.app.transpiler.frontend.fslang.utils.ecommdj import Coordinator as ecommdj_coordinator
from schnell.app.transpiler.frontend.fslang.utils.proshop_backend import Coordinator as probedj_coordinator
from schnell.app.transpiler.frontend.fslang.utils.proshop_mern import Coordinator as promern_coordinator
from schnell.app.transpiler.frontend.fslang.utils.proshop_node import Coordinator as probend_coordinator
from schnell.app.transpiler.frontend.fslang.utils.proshop_routes import Coordinator as proroutes_coordinator
from schnell.app.transpiler.frontend.fslang.utils.proshop_store import Coordinator as prostore_coordinator
from schnell.app.transpiler.frontend.fslang.utils.relight_routes import Coordinator as relightroutes_coordinator
from schnell.app.transpiler.frontend.fslang.utils.vertxspringboot import Coordinator as vertxsb_coordinator

from schnell.app.quick.dahsyat.adminator import Coordinator as adminator_coordinator
from schnell.app.quick.dahsyat.assistance import Coordinator as quickassist_coordinator
from schnell.app.quick.dahsyat.nextblog import Coordinator as nextblog_coordinator
from schnell.app.quick.dahsyat.nxblog import Coordinator as nxblog_coordinator
from schnell.app.quick.dahsyat.sblite import Coordinator as springboot_sqlite_coordinator


# parent = 'app/transpiler/frontend'
# absdir = joiner(env_get('ULIBPY_BASEDIR'), parent)

# def get_rootnode(program):
# 	from langs.ucsv import processor
# 	RootNode = processor(program, print)
# 	return RootNode

# class Coordinator:
# 	def __init__(self, RootNode, project_dir='input'):

provider_to_location_old = {
	# 'dj': {
	# 	'coord_obj': dj_coordinator,
	# 	'coord_container': joiner(absdir, 'fslang/django/__init__.py'),
	# 	'module_name': 'fslang_django',
	# },

	# utils
	'ecommdj'	: ecommdj_coordinator,
	'Uprobe'	: probedj_coordinator,
	'Uprome'	: promern_coordinator,
	'Uprond'	: probend_coordinator,
	'Uprort'	: proroutes_coordinator,
	'Uprost'	: prostore_coordinator,
	'Uroutes'	: relightroutes_coordinator,
	'Uvertx'	: vertxsb_coordinator,

	# misc
	'MA'		: android_sunflower_coordinator,
	'djcorona'	: djcorona_coordinator,
	'ndcorona'	: nodecorona_coordinator,

	'cppcli'	: cppcli_coordinator,
	'gocli'		: gocli_coordinator,
	'rscli'		: rscli_coordinator,

	'crajs'		: crajs_coordinator,
	'crats'		: crats_coordinator,
	'cnxjs'		: cnxjs_coordinator,
	'cnxts'		: cnxts_coordinator,

	# app.quick.dahsyat
	'adminator'	: adminator_coordinator,
	'qass' 		: quickassist_coordinator,
	'nextblog'	: nextblog_coordinator,
	'nxblog'	: nxblog_coordinator,
	'sblite'	: springboot_sqlite_coordinator,

	'Melec'		: electron_coordinator,
	'Mhtml'		: htmlcss_coordinator,
	'Mindon'	: indon_coordinator,
	'Mjfx1'		: jfxso_coordinator,
	'Mjfx2'		: jfxso2_coordinator,

	'Mlangtpl'	: tplang_coordinator,
	'Mqrepl'	: tprepl_coordinator,

	'Mmgseed'	: mgseed_coordinator,
	'Mtray'		: pytray_coordinator,
	'Mqt1'		: qtcm1_coordinator,
	'Mqt2'		: qtcm2_coordinator,	
	'Mrn'		: rn1_coordinator,

	'Mwarp'		: rswarp_coordinator,
	'Msfx'		: sfxso_coordinator,
	'Mpy'		: simplepy_coordinator,
	'Mut'		: simpleunittest_coordinator,
	'Mtsel'		: tselflutter1_coordinator,

	# original fslang
	'dj'		: dj_coordinator,
	'dw'		: dropwizard_coordinator,
	'fa'		: fastapi_coordinator,
	'fl'		: flask_coordinator,
	'noda'		: noda_coordinator,
	'nest'		: nest_coordinator,
	'sb'		: sb_coordinator,
	'mn'		: micronaut_coordinator,
	'qk'		: quarkus_coordinator,

	# fullstack
	'assist' 	: assist_coordinator,
	'gin1' 		: gg_coordinator,
	'gin2' 		: gingonic_simple_coordinator,
	'echo' 		: echo_coordinator,
	'mux' 		: mux_coordinator,
	'nxarg' 	: nxargon_coordinator,
	'nxmkit' 	: nxmkit_coordinator,
	'nxmui' 	: nxmui_coordinator,
	'nxnotus' 	: nxnotus_coordinator,
	'nxtw' 		: nxtw_coordinator,
	'nxts1' 	: nxts1_coordinator,
	'nxts2' 	: nxts2_coordinator,

	'nn' 		: nodenext_coordinator,
	'nts1'		: nodetsmg_coordinator,
	'rair'		: rair_coordinator,
	'rargon'	: rargon_coordinator,
	'riot'		: riot_coordinator,
	'rlight'	: rlight_coordinator,
	'rmkit'		: rmkit_coordinator,
	'rmui'		: rmui_coordinator,
	'rnotus'	: rnotus_coordinator,
	'rnow'		: rnow_coordinator,
	'rpaper'	: rpaper_coordinator,
	'rts1'		: rts1_coordinator,
	'rvolt'		: rvolt_coordinator,
	'rxt'		: rxt_coordinator,
	'tok'		: tokyo_coordinator,
	'vue'		: vue_coordinator,
}

provider_to_location = {}

from coords.fullstack import providers as fullstack_providers
for provider in fullstack_providers:
	provider_to_location.update(provider)

# fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))
from schnell.app.fmusutils import fmus
import anytree
from anytree import RenderTree
# from rich.pretty import pprint


def dahsyater(code): # , initial_dir=None):
	"""
	UPDATE 17-8-2022 tambah initial_dir utk dicantol ke RootNode
	app.quick.__init__ sudah request = code.removeprefix('D>')
	jadi yg diterima di sini adlh dj, dj|csvcode, dst
	D>dj|csvcode
	D>dj
	"""
	provider = code
	csvcode = '[/dummy]{@Dummy}dummy,s' # dummy
	if '|' in code:
		provider, csvcode = code.split('|', 1)

	provider = provider.strip()

	if not provider in provider_to_location:
		indah4(f'''[dahsyater]
			{provider} not found in {provider_to_location.keys()}
			''', warna='green')
		return

	# if provider and csvcode:
	RootNode = get_rootnode(csvcode)
	# if initial_dir:
	# 	RootNode.initial_dir = initial_dir
	# 	RootNode.workdir = initial_dir

	# module_name = provider_to_location[provider]['module_name']
	# containing_coordinator_object = provider_to_location[provider]['coord_container']
	# generator_module = import_module(module_name, containing_coordinator_object)
	# generator = generator_module.Coordinator(RootNode)
	if isinstance(RootNode, anytree.node.anynode.AnyNode):
		# pprint(RenderTree(RootNode))
		print(RenderTree(RootNode))

	indah4(f'''[dahsyater]
	RootNode adlh {RootNode}
	jenisnya adlh {type(RootNode)}
	''', warna='white')

	generator = provider_to_location[provider] (RootNode)
	generator.generate()
	filepath = generator.output()
	baris_entry = 'index/fmus' if not hasattr(generator, 'baris_output') else generator.baris_output()
	# baris_entry = generator.baris_output()
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	indah4(f'''[dahsyater]
	get_cwd = {get_cwd()}
	fmusing {filepath}/{baris_entry} = [{program:1000}...]
	''')
	fmus.set_file_dir_template(filepath, start_fresh=True)
	fmus.process(program)
	# input('[app.dahsyater] Press any key to continue... ')
