--% cara execute fmus
```
from app.fmusutils import run_fmus_from_coordinator, get_rootnode

language_to_handler = {
	'a'			: all_coordinator,
	'all'		: all_coordinator,
	'cpp'		: cpp_coordinator,
	'do'		: devops_coordinator,
	'go'		: go_coordinator,
	'goog'		: google_coordinator,
	'hc'		: html_css_coordinator,
	'java'		: java_coordinator,
	'js'		: js_coordinator,
	'k'			: karya_coordinator,
	'm'			: mobile_coordinator,
	'ml'		: machinelearning_datascience_coordinator,
	'n'			: n_coordinator,
	'pr'		: parser_coordinator,
	'py'		: py_coordinator,
	'r'			: react_coordinator,
	'react'		: react_coordinator,
	'rs'		: rust_coordinator,
	'tdd'		: tdd_coordinator,
	'ts'		: ts_coordinator,
}

csvcode = '[/dummy]{@Dummy}dummy,s'

if '|' in fmus_filename:
    fmus_filename, csvcode = fmus_filename.split('|',1)
if language in language_to_handler:
    RootNode = get_rootnode(csvcode)
    run_fmus_from_coordinator(language_to_handler[language], [RootNode, fmus_filename])

# lihat fmusutils.py
fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))

def run_fmus_from_coordinator(coordinator, coordinator_param_list=None, baris_entry = 'index/fmus', coordinator_kwargs=None):
	if coordinator_param_list:
		generator = coordinator (*coordinator_param_list)
	elif coordinator_kwargs:
		generator = coordinator (**coordinator_kwargs)
	generator.generate()
	filepath = generator.output()	
	program = get_definition_by_key_permissive_start(filepath, baris_entry)
	fmus.set_file_dir_template(filepath)
	fmus.process(program)
```
--#

--% cara kerja level code

app/grammar.py:
```
keseluruhan: insn+

// instruction start
insn: filename "," filetype fileoperation?
| "/" quick_command
| "/" -> empty_quick_command
```

app/fmus/generator.py:
```
elif item.type == 'quick_command' or item.type == 'empty_quick_command':
    from .quick_command import quick_command
    quick_command(root_tree, item, self.run_configuration['replacer'], self.run_configuration)
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
        u -e/b)
            blitz
            request = code.removeprefix(BLITZ_PREFIX)
            from .blitz import blitz
            blitz(request)
            return
        u -e/file>
        u -e/sc>
        u -e/sel>
        u -e/nb>
        u -e/ref>
        u -e/s>
        u -e/run>
        u -e/hope>
        u -e/fmb>
        u -e/gz)
        u -e/bz)
        u -e/zip)
        u -e/T)
        u -e/l)
        u -e/aws)
        u -e/dot)
        u -e/img)
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

```from .blitz import blitz
blitz(request)```

diproses di sini:

app/quick/blitz/__init__.py:
```
def blitz(request):
	"""
	/b> language/filename|csvcode
	"""
	csvcode = '[/dummy]{@Dummy}dummy,s' # dummy

	# indah4('blitz!', warna='white')

	if not request:
		return

	language, fmus_filename = request.split('/',1) # b>py/fa1.fmus

	if not language or not fmus_filename:
		return

	if language == 'blog' and fmus_filename.startswith('pages'):
		blog(fmus_filename)
		return

	if '|' in fmus_filename:
		fmus_filename, csvcode = fmus_filename.split('|',1)

	if not fmus_filename.endswith('.fmus') and not '.' in fmus_filename:
		'''
		bisa gunakan filename.mk selain filename.fmus dan filename
		'''
		fmus_filename += '.fmus'

	if language in language_to_handler:
		RootNode = get_rootnode(csvcode)
		run_fmus_from_coordinator(language_to_handler[language], [RootNode, fmus_filename])
```

--#

--% getting started
ide blitz adlh:
ada file fmus di app/quick/blitz/*
kita bisa execute index/fmus nya dg:
u -e/b)folder/filename
u -e/b)folder/filename|csvcode

ini berbeda dg dahsyater:
u -e/D>dj|csvcode


penjelasan konsep coordinator, bgm dia bisa output kan index.mk atau output.fmus
lalu bisa jalankan fmus nya.
bedakan:
fullstack
dahsyater
blitz
adakah bedanya?

misal kita lihat dulu utk blitz
| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1

fslang_z_quick_django = fslang/z/quick/django
seingatku, sekepercayaanku, ini dioprek oleh quick_statement
dg process_language dan handler dari app.quick.__init__
bentuk /DJ/1 ini diakses paling akhir, stlh condition lain gak masuk (chart lang, img lang, dot lang, aws lang, etc)

handler -> statement_config
        -> quick_statement

proses utama quick_statement adlh:
(dlm handler)
res = quick_statement(item)
program_config.update(res)

(dlm statement_config)
elif jenis .startswith ('fslang_'):
folder = jenis.replace('_','/')
parent = 'app/transpiler/frontend'
absdir = joiner(env_get('ULIBPY_BASEDIR'), parent)
workabsdir = joiner(absdir, folder)
# generator = schnelldir/app/transpiler/frontend/ + fslang/z/quick/django + __init__.py
# ini artinya hanya bisa 1 fe sekali invocation
kembali.update({
  'work': folder, # fslang/path/to/target
  'modulename': jenis, # fslang_path_to_target, fslang_z_quick_django
  'generator': joiner(workabsdir, '__init__.py'),
  'fmusfile': joiner(workabsdir, 'index-input.mk'),
  'workabs': workabsdir,
})

(dlm quick_statement)
Q: siapa yg memberi program_config['generator'] ??? ternyata sblm masuk quick_statement, masuk dulu statement_config!

generator_module = import_module(program_config['modulename'], program_config['generator'])
generator = generator_module.Coordinator(RootNode)
generator.generate()
kembalian quick_statement adlh:
backend_config.update({
    'filepath': generator.output(),
    'baris_entry': 'index/fmus',
})

kembalian di atas diproses selanjutnya dlm process_language (stlh diprocess quick_statement):
hasil = handler(insn)

# jk melist spt /ls/ atau /i/
if 'operation' in program_config:
    ...
# now jk memang minta eksekusi...
else:
    if 'filepath' in program_config:
        filepath = program_config['filepath']
        baris_entry = program_config['baris_entry']
        program = get_definition_by_key_permissive_start(filepath, baris_entry)
        fmus.set_file_dir_template(filepath)
        fmus.process(program)
        input('[app.quick] Press any key to continue... ')
        program_config = {}

jd utk
| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1
fslang_z_quick_django = fslang/z/quick/django
berarti quick_statement memanggil Coordinator.generate() pada
fslang/z/quick/django/__init__.py
--#

--% i, info
../i/
u -e/i/
--#

--% ls, toc
../ls/
u -e/ls/
--#

--% android textinput, Atxt, fslang_z_quick_android_textinput
../Atxt/1
// u -e/Atxt/1

perlu juga utk menjalankan apa saja yg dibutuhkan
termasuk settings SDK HOME utk ini itu
--#

--% react chakra ui, Rch, fslang_z_quick_campur_react_tschakraui
// u -e/Rch/1
--#

--% react grid layout, Rgl, fslang_z_quick_campur_react_reactgridlayout
// u -e/Rgl/1
schnell/app/transpiler/frontend/fslang/z/quick/campur/react/reactgridlayout/index-input.mk
--#

--% menu react: wp, wp+ts, sanity, R, fslang_z_quick_react
// u -e/R/1
ini keluarkan menu...
tp yg baru ke-isi
@project: crajs, webpack react-js*
?pick
    wp5react,d(/load=__CURDIR/wp5-reactjs.mk=index/fmus*)
    wp5react-ts,d(/load=__CURDIR/wp5-reactts.mk=index/fmus*)
    sanity,d(/load=__CURDIR/sanity.mk=index/fmus*)
--#

--% DJ, fslang_z_quick_django
// u -e/DJ/1

hasil mkfile    : C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\z\quick\django\index.mk
hasil model     : C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\z\quick\django\index.mk
hasil save file : C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\z\quick\django\index.mk
ini ternyata menu...
1. @new route*
2. @new model*
3. @new controller*
4. @class based view*
5. @function based view*
6. @new orm*
7. @new env*
8. @new index/app*
9. @new config*
10. @new app*
11. @new complete*
--#

--% N, fslang_z_quick_node
// u -e/N/1
--#

--% ST, fslang_z_quick_nest
// u -e/ST/1
--#

--% XT, fslang_z_quick_next
// u -e/XT/1
--#

--% A, fslang_z_quick_mobile
// u -e/A/1
--#

--% DO, fslang_z_quick_devops
// u -e/DO/1
--#

--% BE, fslang_z_quick_backend
// u -e/BE/1
--#

--% FE, fslang_z_quick_frontend
// u -e/FE/1
--#

--% K, fslang_z_quick_karya
// u -e/K/1
--#

--% algo, fslang_z_quick_algos
// u -e/algo/1
--#

--% tdd, fslang_z_quick_tdd
// u -e/tdd/1
--#

--% PR, fslang_z_quick_parser
// u -e/PR/1
--#

--% crajs, fslang_misc_crajs
// u -e/crajs/1
--#

--% crats, fslang_misc_crats
// u -e/crats/1
--#

--% aws, fslang_z_quick_campur_aws
// u -e/aws/1
--#

--% books, fslang_z_quick_campur_books
// u -e/books/1
--#

--% gomi, fslang_z_quick_campur_gomisc
// u -e/gomi/1
--#

--% hasura, fslang_z_quick_campur_hasura
// u -e/hasura/1
--#

--% html, fslang_z_quick_campur_htmltemplates
// u -e/html/1
--#

--% H, fslang_z_quick_campur_htmltemplates
// u -e/H/1
--#

--% jfx, fslang_z_quick_campur_javafx
// u -e/jfx/1
--#

--% netlify, fslang_z_quick_campur_netlify
// u -e/netlify/1
--#

--% prisma, fslang_z_quick_campur_prisma
// u -e/prisma/1
--#

--% rr, fslang_z_quick_campur_rubyrails
// u -e/rr/1
--#

--% tddjava, fslang_z_quick_campur_tdd_tddjava
// u -e/tddjava/1
--#

--% tddjs, fslang_z_quick_campur_tdd_tddjs
// u -e/tddjs/1
--#

--% tddpy, fslang_z_quick_campur_tdd_tddpy
// u -e/tddpy/1
--#

--% twrds, fslang_z_quick_campur_onefilers_pytwitterredis
// u -e/twrds/1
--#

--% w3, fslang_z_quick_campur_web30
// u -e/w3/1
--#

--% webext, fslang_z_quick_campur_webext
// u -e/webext/1
--#

--% wp53, fslang_z_quick_campur_wp5_wd3
// u -e/wp53/1
--#

--% wp54, fslang_z_quick_campur_wp5_wd4
// u -e/wp54/1
--#

--% wp5ts, fslang_z_quick_campur_wp5_ts
// u -e/wp5ts/1
--#
