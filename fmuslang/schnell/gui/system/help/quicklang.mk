
--% app/quick/__init__.py dan app/quick/bahasa.py
jadi, dari app/quick/__init__ kita bercabang ke:
- blitz
- dahsyater
- "bahasa"
melalui handling 
```
def process_language(code, root_tree=None, item=None, self_run_configuration_replacer=None):
  ...
  elif code.startswith('D>'):
  elif code.startswith(BLITZ_PREFIX):
  try: # else
    pre_parser = Lark(quick_bahasa, start='program')
```

kita lihat dulu cabang no 3, "bahasa":
di sini kita banyak handle coords di fslang/z/quick/: 
`from app.quick.bahasa import bahasa as quick_bahasa`

```
try:
  pre_parser = Lark(quick_bahasa, start='program')
  parser = pre_parser.parse

  if env_int('ULIBPY_FMUS_DEBUG')>=1:
    indah4('='*20 + ' ' + code + '\n', warna='red')

  parsed_tree = parser(code)
  instructions = TheProcessor().transform(parsed_tree)

  for insn in instructions:
    indah4(insn.pretty(), warna='green', layar='black')
    hasil = handler(insn) <- ini adlh kunci

    if env_int('ULIBPY_FMUS_DEBUG')>=1:
      indah4(f'[app.quick] res: [{hasil}], config: {program_config}', warna='yellow')

    if 'operation' in program_config:
      if program_config['operation'] == 'list_statement_config_items':
        '''
        u -e/ls/
        '''
        from app.special import view_file
        basedir = env_get('ULIBPY_BASEDIR')					
        daftarfile = walk_fullpath(basedir)
        filepath = 'app/quick/bahasa.py'
        if platform() in ['win32', 'windows', 'desktop']:
          filepath = 'app\\quick\\bahasa.py'
        view_file(daftarfile, filepath, '// statement config item start', '// statement config item end')
      elif program_config['operation'] == 'info_quick':
        '''
        u -e/i/
        '''
        disini = ayah(__file__, 1)
        filepath = joiner(disini, 'info.txt')					
        filecontent = file_content(filepath)
        indah4(filecontent, warna='white')
    else:
      if 'filepath' in program_config:
        '''
        index.mk sudah digenerate dari index-input.mk
        '''
        filepath = program_config['filepath']
        baris_entry = program_config['baris_entry']
        program = get_definition_by_key_permissive_start(filepath, baris_entry)
        fmus.set_file_dir_template(filepath)
        fmus.process(program)
        input('[app.quick] Press any key to continue... ')
        program_config = {}

except Exception as err:
  print(err)
  trace = traceback.format_exc()
  print(trace)
```

perhatikan bentuk:
```| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1```
fslang_z_quick_django ini mengkodekan lokasi.
dimana diprosesnya?
di app/quick/statement_config.py:
```
elif jenis .startswith ('fslang_'):
folder = jenis.replace('_','/')
parent = 'app/transpiler/frontend'
absdir = joiner(env_get('ULIBPY_BASEDIR'), parent)
workabsdir = joiner(absdir, folder)
# ini artinya hanya bisa 1 fe sekali invocation
kembali.update({
  'work': folder, # fslang/path/to/target
  'modulename': jenis, # fslang_path_to_target, fslang_z_quick_django
  'generator': joiner(workabsdir, '__init__.py'),
  'fmusfile': joiner(workabsdir, 'index-input.mk'),
  'workabs': workabsdir,
})
```

dari ```pre_parser = Lark(quick_bahasa, start='program')```, quick_bahasa adlh spt berikut di bawah:

bahasa/quick_bahasa:
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

```
class TheProcessor(InlineTransformer):
	def program(self, *item_lines):
		return item_lines
```

kita juga lihat:
hasil = handler(insn) <- ini adlh kunci
--#

--% app/quick/__init__/handler
dari bentuk:
```
| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1

u -e/DJ/1
        ^ quick_statement
     ^ statement_config dipetakan ke fslang_z_quick_django
```
ingat handler di bawah ini dipanggil dg cara berikut:
(perhatikan bhw 'filepath' dan 'baris_entry' diassign dari dalam quick_statement)

```
for insn in instructions:
  indah4(insn.pretty(), warna='green', layar='black')
  hasil = handler(insn) <- ini adlh kunci
  if ...
  else:
    if 'filepath' in program_config:
      '''
      index.mk sudah digenerate dari index-input.mk
      '''
      filepath = program_config['filepath']
      baris_entry = program_config['baris_entry']
      program = get_definition_by_key_permissive_start(filepath, baris_entry)
      fmus.set_file_dir_template(filepath)
      fmus.process(program)
      input('[app.quick] Press any key to continue... ')
      program_config = {}
```

```
def handler(tree):
	"""
	statement
		statement_config
			statement_config_list
				fe_react_light
		quick_statement
			program_backend     satu
	"""

	kembali = ''	
	for item in anak(tree):
		jenis = data(item)
		if jenis == 'statement_config':
			res = statement_config(item)
			program_config.update(res)
		elif jenis == 'quick_statement':
			res = quick_statement(item)
			program_config.update(res)

	return kembali
```
--#

--% app/quick/statement_config
utk bentuk:
dari bentuk:
```
| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1

u -e/DJ/1
        ^ quick_statement
     ^ statement_config dipetakan ke fslang_z_quick_django
```
di sini kita petakan "fslang_z_quick_django" ke lokasi yg dibutuhkan...
dg cara:
```
elif jenis .startswith ('fslang_'):
  folder = jenis.replace('_','/')
  parent = 'app/transpiler/frontend'
  absdir = joiner(env_get('ULIBPY_BASEDIR'), parent) // schnelldir
  workabsdir = joiner(absdir, folder) // schnell/app/transpiler/frontend/fslang/z/quick/django
```
artinya kita bisa juga memetakan lokasi lain di dalam "sidoarjodir" spt di data/, coords/, dsb.
kita tinggal tambahkan saja kode di sini.

kita juga lihat
statement_config_list mengembalikan {} ke statement_config yg mengembalikan {} ke ???
lihat handler di atas yg:
```
if jenis == 'statement_config':
res = statement_config(item)
program_config.update(res)
```
from .common import program_config
jadi datanya ada di app/quick/common.py
siapa pihak lain yg membaca program_config tersebut? tentu dlm satu file yg sama, hanya di berbeda fungsi.

```
def statement_config_list(tree):  
  kembali = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'run_fmus':
      # kembali = 'run_fmus nih ye|'
      kembali.update({
        'fmus': 'execute'
      })
    elif jenis == 'info':
      kembali.update({
        'operation': 'info_quick'
      })
    elif jenis == 'toc':
      kembali.update({
        'operation': 'list_statement_config_items'
      })
    elif jenis .startswith ('fslang_'):
      folder = jenis.replace('_','/')
      parent = 'app/transpiler/frontend'
      absdir = joiner(env_get('ULIBPY_BASEDIR'), parent)
      workabsdir = joiner(absdir, folder)
      # ini artinya hanya bisa 1 fe sekali invocation
      kembali.update({
        'work': folder, # fslang/path/to/target
        'modulename': jenis, # fslang_path_to_target, fslang_z_quick_django
        'generator': joiner(workabsdir, '__init__.py'),
        'fmusfile': joiner(workabsdir, 'index-input.mk'),
        'workabs': workabsdir,
      })

  return kembali


def statement_config(tree):
  # print('statement_config')
  kembali = {}
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'statement_config_list':
      res = statement_config_list(item)
      # print('hasil statement_config_list', res)
      kembali.update(res)
    elif jenis == '':
      pass

  return kembali
```
--#

--% app/quick/quick_statement
setelah ```generator.generate()``` maka output.fmus atau index.mk sudah digenerate dari index-input.mk.
akibatnya apa? kita hrs assign filepath dan baris_entry agar bisa:
```
program = get_definition_by_key_permissive_start(filepath, baris_entry)
fmus.set_file_dir_template(filepath)
fmus.process(program)
```

```
def quick_statement(tree):
	program = chtoken(tree)
	if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
		print('\n\n[quick_statement] program:', program)

	if program:
		if len(program)==1:
			'''
			u -e/H/1 -> 1 adlh dummy csvcode, len(program)==1
			'''
			if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
				print('[quick_statement] dummy ucsv program')
			RootNode = tree

		else:
			indah4(f'ucsv for: {program}', warna='cyan')
			from langs.ucsv import processor
			RootNode = processor(program, print)

		generator_module = import_module(program_config['modulename'], program_config['generator'])
		generator = generator_module.Coordinator(RootNode)
		generator.generate()

		if env_int('ULIBPY_FMUS_DEBUGLEVEL')>1:
			print('[quick_statement] program_config:', program_config)

	backend_config.update({
		'filepath': generator.output(),
		'baris_entry': 'index/fmus',
	})
	return backend_config

```
--#

--% app/fmus/quick_command/__init__.py, kita sebut "DS"
urutan pemanggilan:
app/grammar.py
app/fmus/generator.py
app/fmus/quick_command/__init__.py <- ini sebut saja "DS", tempat dimana kita mau masuk "perapatan"

app/quick/__init__.py <- ini kita sebut saja "perapatan"
- app/quick/blitz/__init__.py
- app/quick/dahsyater.py
- app/quick/bahasa.py = quicklang

def quick_command(root_tree, item, self_run_configuration_replacer=None, self_run_configuration=None):
# skip jk __INPUT__ dari template yg akan diproses dg new_replacer_input
if not (hasattr(root_tree, 'input_keys') and len(root_tree.input_keys)):
request = get_input_generic(request)

if request == '/': # ..//

elif request == ')':

elif request .startswith('))'):

elif request.startswith('('):

elif request.startswith('/'):

elif request.startswith('f.'):

elif request.startswith('c.'):

elif request.startswith('l.'):

elif request.startswith('d.'):

elif request.startswith('b.'):

elif request.startswith('y.'):

elif request == 'F.':

elif request == 'C.':

elif request == 'L.':

elif request == 'D.':

elif request == 'B.':

elif request.startswith('git/'):

else:
from app.quick import process_language as quick_process_language
quick_process_language(request, root_tree, item, self_run_configuration_replacer)
--#

--% ../ choose.fmus, ..// info
../ choose.fmus, ..// info
--#

--% ../), find txt files in schnell/app/quick, choose to print
../)

files = files_filter(quick_folder, extension=['.txt'])
print_list_warna(files)
indah4('Masukkan nomer utk file:', warna='cyan', newline=False)
masuk = input(' ')
if masuk:
--#

--% ../))py, ../))react
../))
../))/
../))//
../))///

if request == '/':
elif request == '//':
elif request .startswith ('///'):
elif request: # ../))something
else: # ../))
--#

--% ../( fakerer
../( fakerer
from app.quick.fakerer import handle_faker
handle_faker(request)

u -e"/(s/{word,paragraph,text,phone,citydll}"
s/{word,paragraph,text,phone,citydll}

u -e"/(type/params"

u -e/(ts
u -e/(dt
u -e/(s
u -e/(i
u -e/(f
u -e/(T
u -e/([]
u -e/({}

u -e"/(s/{word,paragraph,text,phone,citydll}"
u -e"/(dt/<format>,between,in year,from-to-now,quote-item/single-quote-item"
u -e"/(ts/<format>,between,in year,from-to-now,quote-item/single-quote-item"
u -e"/([]/num=5,types=[i,s],quote-items/single-quote-items"
u -e"/([[]]/num=5,types=[i,s]"    2d/matrix
u -e"/({}/num=5,types=[i,s]"
u -e"/(i/between,num-digits,max=...,min=..."
u -e"/(f/between,num-digits,max=...,min=...,digits=...,places=..."

objective

u -e/>type/params

u -e/>s/{word,paragraph,text,phone,citydll}
u -e/>dt/<format>,between,in year,from-to-now,quote-item/single-quote-item
u -e/>ts/<format>,between,in year,from-to-now,quote-item/single-quote-item
u -e/>[]/num=5,types=[i,s],quote-items/single-quote-items
u -e/>[[]]/num=5,types=[i,s]    2d/matrix
u -e/>{}/num=5,types=[i,s]
u -e/>i/between,num-digits,max=...,min=...
u -e/>f/between,num-digits,max=...,min=...,places=...

random_digit
random_number

u -e/(s/fn

u -e/([]/10,s,fn
u -e/([]/10,s,ln
u -e/([]/10,s,city
u -e/([]/10,s,country
u -e/([]/3,s,phone_number
u -e/([]/3,s,name_male

u -e/([]/10,i,0-100
u -e/([]/20,i,100-1000

u -e/([]/5,['satu','dua','tiga','enam','tujuh']
u -e/([]/15,[1,2,3,4]

u -e/([]/5,s,fn
['Mary', 'Brian', 'David', 'James', 'Daniel']

u -e/([]/5,i,10-50
['38', '43', '33', '19', '19']

cara handle:
-e/([]/5
-e/([]/5,i
-e/([]/10,s
-e/([]/10,i
-e/([]/10,F
-e/([]/10,si

# random.choice: ../([]/jumlah,[anggota]

../([]/10,[1,10] => [10, 1, 1, 1, 1, 1, 10, 1, 10, 10]
hanya 1 atau 10 krn kita gunakan random.choice
../([]/10,[1,2,3,4,5] => [3, 1, 3, 1, 4, 1, 3, 3, 4, 3]
either 1..5
elif kedua.startswith('[') and pecah[-1].endswith(']'):
'''
random_element([])
'''
kedua = ','.join(pecah[1:])
# print('kedua:', kedua, type(kedua)) # str
import ast, random
args = ast.literal_eval(kedua)
# print('args:', args, type(args)) # list
# res = [getfakers('random_element',funcargs=args) for _ in range(int(pertama))]
res = [random.choice(args) for _ in range(int(pertama))]
indah3(str(res), warna='white')
return

-e/([]/5,i,10-50
-e/([]/10,s,fn
-e/([]/10,s,ln
-e/([]/10,s,country
-e/([]/10,i,0-100
-e/([]/20,i,100-1000
--#

--% ..// search
..//
from db import redis_repl
redis_repl(request, None)
--#

--% ../f. fullstack lang
mending gini, ada 4 bahasa: fs, mycsv, lalang, frontend/declarative

from app.transpiler.frontend.fullstack import process_language as fullstack_process_language
filepath, barisentry = fullstack_process_language(request, returning=True)

indah4(f'''
filepath    = {filepath}
barisentry  = {barisentry}
''', warna='cyan')

from app.transpiler.frontend.fullstack import process_language
-e/f. <kode fullstack-process-language>

biasanya kita bisa
u -e/crajs/1
ini tapi dari bahasa quick

gimana lakukan hal yg sama di sini?
u -e"/f. nda/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^"
u -e"/f. mrcli/B"
  statement
    statement_config
      statement_config_list
        misc_rustcli
    backend_statement

  handler: statement
  hasil statement_config_list {'be': 'rustcli'}
  backend_statement: backend_statement
  'be'
  Traceback (most recent call last):
    File fullstack.py, line 233, in process_language
      hasil = handler(insn)
    File fullstack.py", line 198, in handler
      res = backend_statement(item)
    File backend_statement.py, line 124, in backend_statement
      if program_config['config']['be'] in generator_utils.keys():
  KeyError: 'be'
u -e"/f. mrcli,*/B"
--#

--% ../c. csv lang
from app.transpiler.mycsv.process import process_language as mycsv_process_language
hasil = mycsv_process_language(request, returning=True)

u -e"/c. go/{@User}username,s;email,s"
u -e"/c. pris/{@User}username,s;email,s"
u -e"/c. ts/{@User}username,s;email,s"

u -e"/c. [i/0/@@@|main.go] go/{@User}username,s;email,s"

bentuk [i/0/@@@|main.go]
ini adlh file manip ops
--#

--% ../l. lalang
from app.transpiler.lalang import process_language as lalang_process_language
hasil = lalang_process_language(request, returning=True)

u -e"/l. go/Pmynewpackage"
u -e"/l. [i/0/@@@|pkg.go] go/Pmynewpackage"

bentuk [i/0/@@@|pkg.go]
ini adlh file manip ops
--#

--% ../d. declarative lang
from app.transpiler.frontend.main import process_language as declarative_process_language
hasil = declarative_process_language(request, returning=True)

u -e"/d. <a<b(<c/disabled/<d<e/nilai=kuda/sampurasun(<f<g))"
u -e"/d. [i/0/@@@|main.html] <a<b(<c/disabled/<d<e/nilai=kuda/sampurasun(<f<g))"

bentuk [i/0/@@@|main.html]
ini adlh file manip ops
--#

--% ../b. backend lang (backend language yg kita cari2)
from app.transpiler.backend.main import process_language as backend_process_language
backend_process_language(request)

../b.
../b. #api/users@gp#cors|hello, boyz!;
../b. #api/users@gp#cors/200|huruf text bahasa;
../b. #api/users@gp#cors/200|{1=satu,2=dua,3=tiga};
../b. #api/users@gp#cors/200|@ts/%name='usef';
../b. dj#api/users@gp#cors/200|@ts/$name='wieke';
../b. [:8000][/tempdb]dj#api/users@gp#cors/200|@ts/%name='usef';
../b. [:8000][usef:rahasia@localhost:6379/tempdb]dj#api/users@gp#cors/200|@ts/%name='usef';
../b. [0.0.0.0:8000][usef:rahasia@localhost:6379/tempdb]dj#api/users@gp#cors/200|@ts/%name='usef';

../b. nd#/api/users@g |@ts/||/sc/{?+'hello'; ?+'wieke'; ?+'monyong'; res.send('kuda')} ;;
../b. nd#/api/users@g |@ts/||{?+'hello'; ?+'wieke'; ?+'monyong'; res.send('kuda')} ;;
--#

--% ../y.
from db.generator.curly import process_language as curly_process_language
hasil, err = curly_process_language(request, force=True)

../y. localhost:9000/items p json {user=name}
../y. localhost:9001/rest/books p raw <{allBooks{isn;title}}>
../y. localhost:9222/users/update_password p json {identitas=Wiranto,password=rahasia}
../y. https://www.upwork.com/nx/jobs/search/?q=fullstack&from_recent_search=true&sort=recency
../y. https://www.upwork.com/Ss13U803/captcha/PXSs13U803/captcha.js?a=c&m=0&u=5c889419-c1f3-11ec-a7d9-5845654c7671&v=

--#

--% ../F.
from app.transpiler.frontend.fullstack import quick_repl
quick_repl()
--#

--% ../C.
from app.transpiler.mycsv.process import quick_repl
quick_repl()
--#

--% ../L.
from app.transpiler.lalang import quick_repl
quick_repl()
--#

--% ../D.
from app.transpiler.frontend.main import quick_repl
quick_repl()
--#

--% ../B.
from app.transpiler.backend.main import quick_repl
quick_repl()
--#

--% ../git/ (forget this)
../git/ perintah
import app.gitutils as gitter

res = getattr(gitter, fungsi)(args)
res = getattr(gitter, fungsi)()
--#
