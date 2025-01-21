--% cara execute fmus
```
# D>dj|csvcode
provider = code
csvcode = '[/dummy]{@Dummy}dummy,s' # dummy
if '|' in code:
    provider, csvcode = code.split('|', 1)

RootNode = get_rootnode(csvcode)

from app.transpiler.frontend.fslang.django import Coordinator as dj_coordinator
from app.transpiler.frontend.fslang.misc.crajs import Coordinator as crajs_coordinator

provider_to_location = {
    'crajs'		: crajs_coordinator,
	'crats'		: crats_coordinator,
	'cnxjs'		: cnxjs_coordinator,
	'cnxts'		: cnxts_coordinator,

	'dj'		: dj_coordinator,
	'dw'		: dropwizard_coordinator,
	'fa'		: fastapi_coordinator,
	'fl'		: flask_coordinator,
	'noda'		: noda_coordinator,
	'nest'		: nest_coordinator,
	'sb'		: sb_coordinator,
	'mn'		: micronaut_coordinator,
	'qk'		: quarkus_coordinator,
}
generator = provider_to_location[provider] (RootNode)
generator.generate()
filepath = generator.output()
baris_entry = 'index/fmus'
program = get_definition_by_key_permissive_start(filepath, baris_entry)

# fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))
from app.fmusutils import fmus
fmus.set_file_dir_template(filepath)
fmus.process(program)
```
--#

--% cara kerja level code
urutan pemanggilan:
app/grammar.py
app/fmus/generator.py
app/fmus/quick_command/__init__.py

app/quick/__init__.py
- app/quick/blitz/__init__.py
- app/quick/dahsyater.py
- app/quick/bahasa.py = quicklang

app/quick/dahsyater.py:
```
def dahsyater(code):
	"""
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


	# module_name = provider_to_location[provider]['module_name']
	# containing_coordinator_object = provider_to_location[provider]['coord_container']
	# generator_module = import_module(module_name, containing_coordinator_object)
	# generator = generator_module.Coordinator(RootNode)
	indah4(f'''[dahsyater]
		RootNode adlh {RootNode}
		jenisnya adlh {type(RootNode)}
		''', warna='white')

	generator = provider_to_location[provider] (RootNode)
	generator.generate()
	filepath = generator.output()
	baris_entry = 'index/fmus'
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	fmus.set_file_dir_template(filepath)
	fmus.process(program)
	# input('[app.dahsyater] Press any key to continue... ')
```

app/quick/__init__.py:
```
def process_language(code, root_tree=None, item=None, self_run_configuration_replacer=None):
    if ...
        handle if utk:
        u -e/
            choice.fmus
        u -e/%
            peek file
        u -e/@
            csvlang
        u -e/>
            gen file
        u -e/tar>
        u -e/D>
            dahsyater
			from .dahsyater import dahsyater
			request = code.removeprefix('D>')
			# handle /D>=filepath=barisentry
			if request.startswith('=') and request.count('=') == 2:
				request = request.removeprefix('=')
				request = filepath_samadengan_barisentry(request)
				indah4(f'''[app.quick]
				hasil filepath_samadengan_barisentry:
				request sudah menjadi [{request}]
				''', warna='blue')
				if not request:
					indah4('[app.quick] not processing for empty dahsyat request', warna='red')
					return	
			dahsyater(request)
			return
        u -e/b)
            blitz
            request = code.removeprefix(BLITZ_PREFIX)
            from .blitz import blitz
            blitz(request)
            return
        u -e/file>
        ...
        u -e/chart)
    else:
        pre_parser = Lark(quick_bahasa, start='program')
        parser = pre_parser.parse
        parsed_tree = parser(code)
        instructions = TheProcessor().transform(parsed_tree)
        for insn in instructions:
            indah4(insn.pretty(), warna='green', layar='black')
            hasil = handler(insn)

            if 'operation' in program_config: # jika /ls/ atau /i/
            else:
                # kita tertarik ini
                if 'filepath' in program_config:
                    filepath = program_config['filepath']
                    baris_entry = program_config['baris_entry']
                    program = get_definition_by_key_permissive_start(filepath, baris_entry)
                    fmus.set_file_dir_template(filepath)
                    fmus.process(program)
                    input('[app.quick] Press any key to continue... ')
                    program_config = {}
```

app/quick/bahasa.py:
```
program: statement+
statement: 
	| statement_config? quick_statement?

quick_statement: program_backend <- kode csv dan "1" masuk sini
program_backend: HURUF_PROGRAM_BACKEND

statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
// statement config item start
statement_config_item: "*" -> run_fmus
    | "i" 			-> info // info atau help, mengentai kode yg dioprek
    | "ls" 			-> toc
    | "Atxt" 		-> fslang_z_quick_android_textinput				// u -e/Atxt/1
    | "Rch" 		-> fslang_z_quick_campur_react_tschakraui		// u -e/Rch/1
    | "Rgl" 		-> fslang_z_quick_campur_react_reactgridlayout	// u -e/Rgl/1
    | "R" 			-> fslang_z_quick_react		// u -e/R/1
    | "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1
    | "N" 			-> fslang_z_quick_node		// u -e/N/1
    | "ST" 			-> fslang_z_quick_nest		// u -e/ST/1
    | "XT" 			-> fslang_z_quick_next		// u -e/XT/1
    | "A" 			-> fslang_z_quick_mobile	// u -e/A/1
    | "DO" 			-> fslang_z_quick_devops	// u -e/DO/1
    | "BE" 			-> fslang_z_quick_backend	// u -e/BE/1
    | "FE" 			-> fslang_z_quick_frontend	// u -e/FE/1
    | "K" 			-> fslang_z_quick_karya		// u -e/K/1
    | "algo" 		-> fslang_z_quick_algos		// u -e/algo/1
    | "tdd" 		-> fslang_z_quick_tdd		// u -e/tdd/1
    | "PR" 			-> fslang_z_quick_parser	// u -e/PR/1

    | "crajs" 		-> fslang_misc_crajs			// u -e/crajs/1
    | "crats" 		-> fslang_misc_crats			// u -e/crats/1
    | "aws" 		-> fslang_z_quick_campur_aws			// u -e/aws/1
    | "books" 		-> fslang_z_quick_campur_books			// u -e/books/1
    | "gomi" 		-> fslang_z_quick_campur_gomisc			// u -e/gomi/1
    | "hasura" 		-> fslang_z_quick_campur_hasura			// u -e/hasura/1
    | "html" 		-> fslang_z_quick_campur_htmltemplates	// u -e/html/1
    | "H" 			-> fslang_z_quick_campur_htmltemplates	// u -e/H/1
    | "jfx" 		-> fslang_z_quick_campur_javafx			// u -e/jfx/1
    | "netlify" 	-> fslang_z_quick_campur_netlify		// u -e/netlify/1
    | "prisma" 		-> fslang_z_quick_campur_prisma			// u -e/prisma/1
    | "rr" 			-> fslang_z_quick_campur_rubyrails		// u -e/rr/1
    | "tddjava"		-> fslang_z_quick_campur_tdd_tddjava	// u -e/tddjava/1
    | "tddjs" 		-> fslang_z_quick_campur_tdd_tddjs		// u -e/tddjs/1
    | "tddpy" 		-> fslang_z_quick_campur_tdd_tddpy		// u -e/tddpy/1
    | "twrds" 		-> fslang_z_quick_campur_onefilers_pytwitterredis		// u -e/twrds/1
    | "w3" 			-> fslang_z_quick_campur_web30			// u -e/w3/1
    | "webext" 		-> fslang_z_quick_campur_webext			// u -e/webext/1
    | "wp53" 		-> fslang_z_quick_campur_wp5_wd3		// u -e/wp53/1
    | "wp54" 		-> fslang_z_quick_campur_wp5_wd4		// u -e/wp54/1
    | "wp5ts" 		-> fslang_z_quick_campur_wp5_ts			// u -e/wp5ts/1
```

app/fmus/quick_command/__init__.py:
```
def quick_command(root_tree, item, self_run_configuration_replacer=None, self_run_configuration=None):
    os.chdir(item.workdir)
    request = item.command
    request = request.replace('__WORKDIR__', item.workdir) # sementara baru @ dan / yg dukung __WORKDIR__
    if ...
    handle if untuk
        u -e//
            print info.txt
            uniknya u -e/ dihandle di bawah di app/quick/__init__.py
        u -e/)
        u -e/))..
        u -e//..
            search
        u -e/f. atau c. atau l. atau d. atau b. atau y.
    else:
        quick_process_language(request, root_tree, item, self_run_configuration_replacer)
```

app/fmus/generator.py:
```
elif item.type == 'quick_command' or item.type == 'empty_quick_command':
    from .quick_command import quick_command
    quick_command(root_tree, item, self.run_configuration['replacer'], self.run_configuration)
```

app/grammar.py:
```
keseluruhan: insn+

// instruction start
insn: filename "," filetype fileoperation?
| "/" quick_command
| "/" -> empty_quick_command
```

--#

--% app/grammar.py
```
keseluruhan: insn+

// instruction start
insn: filename "," filetype fileoperation?
| "/" quick_command
| "/" -> empty_quick_command
```
awal mulanya dari sini utk bahasa fmus (famous)
--#

--% app/fmus/generator.py
```
elif item.type == 'quick_command' or item.type == 'empty_quick_command':
    from .quick_command import quick_command
    quick_command(root_tree, item, self.run_configuration['replacer'], self.run_configuration)
```
--#

--% app/fmus/quick_command/__init__.py
```
def quick_command(root_tree, item, self_run_configuration_replacer=None, self_run_configuration=None):
    os.chdir(item.workdir)
    request = item.command
    request = request.replace('__WORKDIR__', item.workdir) # sementara baru @ dan / yg dukung __WORKDIR__
    if ...
    handle if untuk
        u -e//
            print info.txt
            uniknya u -e/ dihandle di bawah di app/quick/__init__.py
        u -e/)
        u -e/))..
        u -e//..
            search
        u -e/f. atau c. atau l. atau d. atau b. atau y.
    else:
        quick_process_language(request, root_tree, item, self_run_configuration_replacer)
```
"quick handler" di app/fmus (yakni app/fmus/quick_command ini) "memanggil" quicklang yg ada di app/quick/bahasa dg quick_process_language().
--#

--% app/quick/__init__.py
di sini terjadi percabangan antara blitz dan dahsyater dan "quicklang" yg sesungguhnya.
```
def process_language(code, root_tree=None, item=None, self_run_configuration_replacer=None):
    if ...
        handle if utk:
        u -e/
            choice.fmus
        u -e/%
            peek file
        u -e/@
            csvlang
        u -e/>
            gen file
        u -e/tar>
        u -e/D> # handle dahsyater
            dahsyater
			from .dahsyater import dahsyater
			request = code.removeprefix('D>')
			# handle /D>=filepath=barisentry
			if request.startswith('=') and request.count('=') == 2:
				request = request.removeprefix('=')
				request = filepath_samadengan_barisentry(request)
				indah4(f'''[app.quick]
				hasil filepath_samadengan_barisentry:
				request sudah menjadi [{request}]
				''', warna='blue')
				if not request:
					indah4('[app.quick] not processing for empty dahsyat request', warna='red')
					return	
			dahsyater(request)
			return
        u -e/b) # handle blitz
            blitz
            request = code.removeprefix(BLITZ_PREFIX)
            from .blitz import blitz
            blitz(request)
            return
        u -e/file>
        ...
        u -e/chart)
    else: # handle quicklang/bahasa
        pre_parser = Lark(quick_bahasa, start='program')
        parser = pre_parser.parse
        parsed_tree = parser(code)
        instructions = TheProcessor().transform(parsed_tree)
        for insn in instructions:
            indah4(insn.pretty(), warna='green', layar='black')
            hasil = handler(insn)

            if 'operation' in program_config: # jika /ls/ atau /i/
            else:
                # kita tertarik ini
                if 'filepath' in program_config:
                    filepath = program_config['filepath']
                    baris_entry = program_config['baris_entry']
                    program = get_definition_by_key_permissive_start(filepath, baris_entry)
                    fmus.set_file_dir_template(filepath)
                    fmus.process(program)
                    input('[app.quick] Press any key to continue... ')
                    program_config = {}
```
yg belum "terjawab" adlh bagian else di ```pre_parser = Lark(quick_bahasa, start='program')```
tapi itu bukan fokus kita sekarang.
--#

--% app/quick/dahsyater.py
stlh masuk dahsyater, kita pecah bagian csv code, jk kosong kita sediakan sendiri.
utk bagian csv yg kosong ini krn kita punya template fmus yg "static", apa adanya.
kerennya dahsyater apa coba? ya tentu krn kita bisa specify bahasa csv lang di dalam fmus lang.
nah andaikan kita sudah bisa/selesai dg bahasa backend yg bisa specify middleware, validation, dst...
```
def dahsyater(code):
	"""
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

	# module_name = provider_to_location[provider]['module_name']
	# containing_coordinator_object = provider_to_location[provider]['coord_container']
	# generator_module = import_module(module_name, containing_coordinator_object)
	# generator = generator_module.Coordinator(RootNode)
	indah4(f'''[dahsyater]
		RootNode adlh {RootNode}
		jenisnya adlh {type(RootNode)}
		''', warna='white')

	generator = provider_to_location[provider] (RootNode)
	generator.generate()
	filepath = generator.output()
	baris_entry = 'index/fmus'
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	fmus.set_file_dir_template(filepath)
	fmus.process(program)
	# input('[app.dahsyater] Press any key to continue... ')
```
--#

--% app/quick/bahasa.py
jadi, dari app/quick/__init__ kita bercabang ke:
- blitz
- dahsyater
- "bahasa"

bagian ini harusnya dibahasa di "quicklang"

perhatikan bentuk:
```| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1```
fslang_z_quick_django ini mengkodekan lokasi.
dimana diprosesnya?

```
program: statement+
statement: 
	| statement_config? quick_statement?

quick_statement: program_backend <- kode csv dan "1" masuk sini
program_backend: HURUF_PROGRAM_BACKEND

statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
// statement config item start
statement_config_item: "*" -> run_fmus
    | "i" 			-> info // info atau help, mengentai kode yg dioprek
    | "ls" 			-> toc
    | "Atxt" 		-> fslang_z_quick_android_textinput				// u -e/Atxt/1
    | "Rch" 		-> fslang_z_quick_campur_react_tschakraui		// u -e/Rch/1
    | "Rgl" 		-> fslang_z_quick_campur_react_reactgridlayout	// u -e/Rgl/1
    | "R" 			-> fslang_z_quick_react		// u -e/R/1
    | "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1
    | "N" 			-> fslang_z_quick_node		// u -e/N/1
    | "ST" 			-> fslang_z_quick_nest		// u -e/ST/1
    | "XT" 			-> fslang_z_quick_next		// u -e/XT/1
    | "A" 			-> fslang_z_quick_mobile	// u -e/A/1
    | "DO" 			-> fslang_z_quick_devops	// u -e/DO/1
    | "BE" 			-> fslang_z_quick_backend	// u -e/BE/1
    | "FE" 			-> fslang_z_quick_frontend	// u -e/FE/1
    | "K" 			-> fslang_z_quick_karya		// u -e/K/1
    | "algo" 		-> fslang_z_quick_algos		// u -e/algo/1
    | "tdd" 		-> fslang_z_quick_tdd		// u -e/tdd/1
    | "PR" 			-> fslang_z_quick_parser	// u -e/PR/1

    | "crajs" 		-> fslang_misc_crajs			// u -e/crajs/1
    | "crats" 		-> fslang_misc_crats			// u -e/crats/1
    | "aws" 		-> fslang_z_quick_campur_aws			// u -e/aws/1
    | "books" 		-> fslang_z_quick_campur_books			// u -e/books/1
    | "gomi" 		-> fslang_z_quick_campur_gomisc			// u -e/gomi/1
    | "hasura" 		-> fslang_z_quick_campur_hasura			// u -e/hasura/1
    | "html" 		-> fslang_z_quick_campur_htmltemplates	// u -e/html/1
    | "H" 			-> fslang_z_quick_campur_htmltemplates	// u -e/H/1
    | "jfx" 		-> fslang_z_quick_campur_javafx			// u -e/jfx/1
    | "netlify" 	-> fslang_z_quick_campur_netlify		// u -e/netlify/1
    | "prisma" 		-> fslang_z_quick_campur_prisma			// u -e/prisma/1
    | "rr" 			-> fslang_z_quick_campur_rubyrails		// u -e/rr/1
    | "tddjava"		-> fslang_z_quick_campur_tdd_tddjava	// u -e/tddjava/1
    | "tddjs" 		-> fslang_z_quick_campur_tdd_tddjs		// u -e/tddjs/1
    | "tddpy" 		-> fslang_z_quick_campur_tdd_tddpy		// u -e/tddpy/1
    | "twrds" 		-> fslang_z_quick_campur_onefilers_pytwitterredis		// u -e/twrds/1
    | "w3" 			-> fslang_z_quick_campur_web30			// u -e/w3/1
    | "webext" 		-> fslang_z_quick_campur_webext			// u -e/webext/1
    | "wp53" 		-> fslang_z_quick_campur_wp5_wd3		// u -e/wp53/1
    | "wp54" 		-> fslang_z_quick_campur_wp5_wd4		// u -e/wp54/1
    | "wp5ts" 		-> fslang_z_quick_campur_wp5_ts			// u -e/wp5ts/1
```
--#

--% getting started
ingat tujuan awal di sini adlh?
bikin csvlang bisa terintegrasi dg fmus...kan keren jk bisa dari __INPUT__ atau input gui
--#

--% app.quick.dahsyater
app/quick/dahsyater.py
app.quick.dahsyater:

  u -e"/D>CHOOSE|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
.

provider_to_location = {
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

```
def dahsyater(code):
	"""
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

  indah4(f'''[dahsyater]
		RootNode adlh {RootNode}
		jenisnya adlh {type(RootNode)}
		''', warna='white')

  # from app.transpiler.frontend.fslang.django import Coordinator as dj_coordinator
	generator = provider_to_location[provider] (RootNode)
	generator.generate()
	filepath = generator.output()
	baris_entry = 'index/fmus'
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	fmus.set_file_dir_template(filepath)
	fmus.process(program)
```
.
--#

--% dj
D>dj
provider = dj
code = [/dummy]{@Dummy}dummy,s

u -e"/D>dj|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
        ^ provider
          | ^ csvcode

shit jd ngawur========== [processor] mk file = C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\django\index.mk
create_dir| Masukkan nilai untuk [C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\django\__INPUT__\main\helpers]: resto

--#

--% dw
u -e"/D>dw|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% fa
u -e"/D>fa|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% fl
u -e"/D>fl|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% noda
u -e"/D>noda|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nest
u -e"/D>nest|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% sb
u -e"/D>sb|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% mn
u -e"/D>mn|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% qk
u -e"/D>qk|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% ecommdj
u -e"/D>ecommdj|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uprobe
u -e"/D>Uprobe|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uprome
u -e"/D>Uprome|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uprond
u -e"/D>Uprond|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uprort
u -e"/D>Uprort|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uprost
u -e"/D>Uprost|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uroutes
u -e"/D>Uroutes|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Uvertx
u -e"/D>Uvertx|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% MA
u -e"/D>MA|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mrn
u -e"/D>Mrn|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mtsel
u -e"/D>Mtsel|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% djcorona
u -e"/D>djcorona|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% ndcorona
u -e"/D>ndcorona|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% cppcli
u -e"/D>cppcli|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% gocli
u -e"/D>gocli|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rscli
u -e"/D>rscli|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% crajs
u -e"/D>crajs|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% crats
u -e"/D>crats|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% cnxjs
u -e"/D>cnxjs|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% cnxts
u -e"/D>cnxts|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% adminator
u -e"/D>adminator|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% qass
u -e"/D>qass|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nextblog
u -e"/D>nextblog|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxblog
u -e"/D>nxblog|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% sblite
u -e"/D>sblite|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Melec
u -e"/D>Melec|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mhtml
u -e"/D>Mhtml|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mindon
u -e"/D>Mindon|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mjfx1
u -e"/D>Mjfx1|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mjfx2
u -e"/D>Mjfx2|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mlangtpl
u -e"/D>Mlangtpl|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mqrepl
u -e"/D>Mqrepl|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mmgseed
u -e"/D>Mmgseed|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mtray
u -e"/D>Mtray|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"

err = no library called "cairo-2" was found
no library called "cairo" was found
no library called "libcairo-2" was found
cannot load library 'libcairo.so.2': error 0x7e
cannot load library 'libcairo.2.dylib': error 0x7e
cannot load library 'libcairo-2.dll': error 0x7e
--#

--% Mqt1
u -e"/D>Mqt1|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mqt2
u -e"/D>Mqt2|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mwarp
u -e"/D>Mwarp|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Msfx
u -e"/D>Msfx|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mpy
u -e"/D>Mpy|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% Mut
u -e"/D>Mut|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% assist
u -e"/D>assist|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% gin1
u -e"/D>gin1|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% gin2
u -e"/D>gin2|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% echo
u -e"/D>echo|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% mux
u -e"/D>mux|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxarg
u -e"/D>nxarg|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxmkit
u -e"/D>nxmkit|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxmui
u -e"/D>nxmui|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxnotus
u -e"/D>nxnotus|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxtw
u -e"/D>nxtw|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxts1
u -e"/D>nxts1|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nxts2
u -e"/D>nxts2|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nn
u -e"/D>nn|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% nts1
u -e"/D>nts1|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rair
u -e"/D>rair|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rargon
u -e"/D>rargon|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% riot
u -e"/D>riot|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rlight
u -e"/D>rlight|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rmkit
u -e"/D>rmkit|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rmui
u -e"/D>rmui|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rnotus
u -e"/D>rnotus|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rnow
u -e"/D>rnow|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rpaper
u -e"/D>rpaper|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rts1
u -e"/D>rts1|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rvolt
u -e"/D>rvolt|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% rxt
u -e"/D>rxt|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% tok
u -e"/D>tok|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#

--% vue
u -e"/D>vue|[usef:rahasia@localhost:5432/tempdb#8000##9000]{@Todo}title,s,len=150;description,t,len=1000;done,b,df=False"
--#
