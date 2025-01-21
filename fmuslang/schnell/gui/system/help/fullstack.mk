--% cara execute fmus
```
from app.fileutils import get_definition_by_key_permissive_start

filepath = program_config['filepath']
baris_entry = program_config['baris_entry']
program = get_definition_by_key_permissive_start(filepath, baris_entry)

from app.fmus import Fmus
fmus = Fmus(False)
fmus.set_file_dir_template(filepath)
fmus.process(program)

input('[fullstack] Press any key to continue... ')
program_config = {
	'config': {
		'fe': 'react-light',
	}
}
```
--#

--% program dan examples
cara akses:
../F. utk fullstack-repl
../f. kode utk akses dari kbrepl

code C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fullstack.py

# ini fullstack
app/transpiler/frontend/fullstack.py

# ini frontend
app/transpiler/frontend/main.py

# cara kerja:
- iterate instruksi dari statement
- handle tiap instruksi
salah satunya dihandle di:
from app.transpiler.frontend.fslang.csv_statement import csv_statement
kita lihat proses yg terjadi:
```

generator_by_backend = {
	'django': django_generator,
	'django_mongo': django_mongo_generator,
	'dropwizard': dropwizard_generator,
	'dropwizard_mongo': dropwizard_mongo_generator,
	'fastapi': fastapi_generator,
	'fastapi_mongo': fastapi_mongo_generator,
	'flask': flask_generator,
	'flask_mongo': flask_mongo_generator,
	'micronaut': micronaut_generator,
	'micronaut_mongo': micronaut_mongo_generator,
	'moleculer': moleculer_generator,
	'moleculer_mongo': moleculer_mongo_generator,
	'nest': nest_generator,
	'nest_mongo': nest_mongo_generator,
	'node_antd': node_antd_generator,	
	'node_antd_mongo': node_antd_mongo_generator,	
	'node_apollo': node_apollo_generator,
	'node_apollo_mongo': node_apollo_mongo_generator,
	'quarkus': quarkus_generator,
	'quarkus_mongo': quarkus_mongo_generator,
	'springboot': springboot_generator,
	'springboot_mongo': springboot_mongo_generator,
	'fullstack': fullstack_generator,
}

konfigurasi_backend = get_konfigurasi_backend()
# bc = BackendCreator(RootNode, konfigurasi_backend)
# bc.generate()
generator = generator_by_backend[konfigurasi_backend] (RootNode)
generator.generate()

frontend_config.update({
	# 'filepath': bc.mkfile_output_filepath,
	'filepath': generator.output(),
	'baris_entry': 'index/fmus',
})
```
- update program_config
- cek program_config jk exec fmus maka ambildari program_config['filepath'] dan program_config['baris_entry']

program: statement+
statement: 
	| statement_config? csv_statement? backend_statement? frontend_statement?
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "i" 		-> info // info atau help, mengentai kode yg dioprek

  | "all" 	-> fullstack
	| "fs" 		-> fullstack

	| "dj" 		-> be_django
	| "djm" 	-> be_django_mongo
	| "sb" 		-> be_springboot
	| "sbm"		-> be_springboot_mongo
	| "fast" 	-> be_fastapi
	| "fastm" 	-> be_fastapi_mongo
	| "fl" 		-> be_flask
	| "flm" 	-> be_flask_mongo
	| "ns" 		-> be_nest
	| "nsm" 	-> be_nest_mongo
	| "dw" 		-> be_dropwizard
	| "dwm" 	-> be_dropwizard_mongo
	| "mn" 		-> be_micronaut
	| "mnm" 	-> be_micronaut_mongo
	| "q" 		-> be_quarkus
	| "qm" 		-> be_quarkus_mongo
	| "nda" 	-> be_node_antd
	| "ndam" 	-> be_node_antd_mongo
	| "ndp" 	-> be_node_apollo
	| "ml" 		-> be_moleculer
	| "mlm"		-> be_moleculer_mongo
	| "lt" 		-> fe_react_light
	| "ag" 		-> fe_react_argon
	| "af" 		-> fe_react_airframe
	| "vo" 		-> fe_react_volt
	| "nt" 		-> fe_react_notus
	| "now" 	-> fe_react_now
	| "ppr" 	-> fe_react_paper
	| "xt" 		-> fe_react_xtreme

  | "mqr"				-> misc_quickrepl
	| "msp"				-> misc_simplepython
	| "msut"			-> misc_simpleunittest
	| "mlang"			-> misc_langtemplate
	| "mtray"			-> misc_pytrayicon
	| "mcrajs"			-> misc_crajs
	| "mcrats"			-> misc_crats
	| "mrcli"			-> misc_rustcli
	| "mccli"			-> misc_cppcli
	| "mgcli"			-> misc_gocli
	| "mid"				-> misc_indon
	| "msfx"			-> misc_sfxso
	| "mjfx"			-> misc_jfxso
	| "mjupy"			-> misc_jupy
	| "mjuser"			-> misc_jupyuser
	| "mel"				-> misc_electron
	| "mbedj"			-> misc_be_django_corona
	| "mbeno"			-> misc_be_node_corona
	| "mqt"				-> misc_qtcmake
	| "mqt2"			-> misc_qtcmake2
	| "msel1"			-> misc_tselflutter1
	| "mrn1"			-> misc_reactnative1
	| "msun"			-> misc_androidkotlinbasesunflower
	| "mrural"			-> misc_rustwarpsimplerest
	| "mgseed"			-> misc_mongoseeder
// insert new misc app
	| "urlr"			-> utils_relight_routes
	| "upsr"			-> utils_proshop_routes
	| "upss"			-> utils_proshop_store
	| "upsb"			-> utils_proshop_backend 	// wm -e'***upsb,*/B^..^'
	| "uecommdj"		-> utils_ecommdj					// wm -e'***uecommdj,*/B^..^'
	| "upnode"			-> utils_proshop_node
	| "uhcx"			-> utils_htmlcss
	| "uvsb"			-> utils_vertxspringboot		// lebih mirip misc: wm -e '***uvsb,*/B'
	| "upmern"			-> utils_proshop_mern

nda/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
dj/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
fl/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
ns/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
sb/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
fast/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
ndp/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
ml/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
seingakut: * ini fmus...jadi index.mk stlh dihasilkan, diexec...
*,dj/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Corona=#5}id,i,pk,ai;country,s;cases,i;deaths,i;date,dt:d|{@Todo=#5}done,b,df=false;content,s,len=5000;category,s^
*,nda/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Corona=#5}id,i,pk,ai;country,s;cases,i;deaths,i;date,dt:d|{@Todo=#5}done,b,df=false;content,s,len=5000;category,s^

all/C^[usef:rahasia@localhost:5432/tempdb]{@ShippingAddress=#10}order,11/Order/d=cascade,n,b;address,s,len=200,n,b;city,s,len=200,n,b;postalCode,s,len=200,n,b;country,s,len=200,n,b;shippingPrice,dec,digits=7,places=2,n,b;_id,auto,pk,E | {@OrderItem=#10}product,fk/Product/d=setnull,n;order,fk/Order/d=setnull,n;name,s,len=200,n,b;qty,i,n,b,df=0;price,dec,digits=7,places=2,n,b;image,s,len=200,n,b;_id,auto,pk,E | {@Order=#10,ts}user,fk/User/d=setnull,n;paymentMethod,s,len=200,n,b;taxPrice,dec,digits=7,places=2,n,b;shippingPrice,dec,digits=7,places=2,n,b;totalPrice,dec,digits=7,places=2,n,b;isPaid,b,df=False;paidAt,ts,ana,n,b;isDelivered,b,df=False;deliveredAt,ts,ana,n,b;_id,auto,pk,E | {@Product=#10,ts}_id,auto,pk,E;brand,s,len=200,n,b;category,s,len=200,n,b;countInStock,i,n,b,df=0;description,t,n,b;image,img,n,b;name,s,len=200,n,b;numReviews,i,n,b,df=0;price,dec,digits=7,places=2,n,b;rating,dec,digits=7,places=2,n,b;user,fk/User/d=setnull,n | {@Review=#10,ts}user,fk/User/d=setnull,n;product,fk/Product/d=setnull,n;name,s,len=200,n,b;rating,i,n,b,df=0;comment,t,n,b;_id,auto,pk,E | {@Cart=#10}product_id,i;user_id,i;shippingaddress_id,i | {@User=#10}username,s;name,s;first_name,s;last_name,s;email,s;phone,s;is_active,b;is_staff,b;roles,s,(admin,user,guest>user) ^

if jenis == 'statement_config':
    res = statement_config(item)
    program_config.update(res)
elif jenis == 'backend_statement':
    res = backend_statement(item)
    program_config.update(res)
elif jenis == 'csv_statement':
    res = csv_statement(item)
    program_config.update(res)
elif jenis == 'frontend_statement':
    res = frontend_statement(item)
    program_config.update(res)

kita kenal
backend lang
/B^^, u -e "***mrcli,*/B"
csv lang
/C^^
frontend lang
/F^^
# F<<layout(header(drop,profile),sidebar(menu(level1a(level2a,level2b),level1b)))>>
# F<<layout(header(drop,profile),sidebar(menu(level1a(level2a,level2b),level1b)),content,footer)>>
# F<<layout(header(drop,profile),sidebar(menu(level1a(level2a,level2b),level1b)),content,footer,floating)>>

--#

--% csv_statement, fullstack mycsv C
program: statement+
statement: 
	| statement_config? csv_statement? backend_statement? frontend_statement?

csv_statement			: "C^" program_csv "^"
--#

--% backend_statement, fullstack backend B
backend_statement		: "B^" program_backend "^"
B" // wm -e "***mrcli,*/B"
--#

--% frontend_statement, fullstack frontend F
frontend_statement		: "F^" program_frontend "^"
--#

--% i, info
--#

--% dj, be_django
program: statement+
statement: 
	| statement_config? csv_statement? backend_statement? frontend_statement?
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "i" 		-> info // info atau help, mengentai kode yg dioprek
	| "dj" 		-> be_django
	| "djm" 	-> be_django_mongo

dj/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
--#

--% djm, be_django_mongo
program: statement+
statement: 
	| statement_config? csv_statement? backend_statement? frontend_statement?
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "i" 		-> info // info atau help, mengentai kode yg dioprek
	| "dj" 		-> be_django
	| "djm" 	-> be_django_mongo

djm/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
--#

--% sb, be_springboot
--#

--% sbm, be_springboot_mongo
--#

--% fast, be_fastapi
--#

--% fastm, be_fastapi_mongo
--#

--% fl, be_flask
--#

--% flm, be_flask_mongo
--#

--% ns, be_nest
--#

--% nsm, be_nest_mongo
--#

--% dw, be_dropwizard
--#

--% dwm, be_dropwizard_mongo
--#

--% mn, be_micronaut
--#

--% mnm, be_micronaut_mongo
--#

--% q, be_quarkus
--#

--% qm, be_quarkus_mongo
--#

--% nda, be_node_antd
--#

--% ndam, be_node_antd_mongo
--#

--% ndp, be_node_apollo
--#

--% ml, be_moleculer
--#

--% mlm, be_moleculer_mongo
--#

--% lt, fe_react_light
--#

--% ag, fe_react_argon
--#

--% af, fe_react_airframe
--#

--% vo, fe_react_volt
--#

--% nt, fe_react_notus
--#

--% now, fe_react_now
--#

--% ppr, fe_react_paper
--#

--% xt, fe_react_xtreme
--#

--% all, fullstack
--#

--% fs, fullstack
--#

--% mqr, misc_quickrepl
--#

--% msp, misc_simplepython
--#

--% msut, misc_simpleunittest
--#

--% mlang, misc_langtemplate
--#

--% mtray, misc_pytrayicon
coba:
../f. mtray/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^

u -e"/f. mtray/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^"

{
"config": {
    "fe": "react-light"
},
"be": "pytrayicon"
}

'pytrayicon'
Traceback (most recent call last):
  File "C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fullstack.py", line 233, in process_language
    hasil = handler(insn)
  File "C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fullstack.py", line 201, in handler
    res = csv_statement(item)
  File "C:\Users\usef\work\sidoarjo\schnell\app\transpiler\frontend\fslang\csv_statement.py", line 323, in csv_statement
    generator = generator_by_backend[konfigurasi_backend] (RootNode)
KeyError: 'pytrayicon'

--#

--% mcrajs, misc_crajs
--#

--% mcrats, misc_crats
--#

--% mrcli, misc_rustcli
--#

--% mccli, misc_cppcli
--#

--% mgcli, misc_gocli
--#

--% mid, misc_indon
--#

--% msfx, misc_sfxso
--#

--% mjfx, misc_jfxso
--#

--% mjupy, misc_jupy
--#

--% mjuser, misc_jupyuser
--#

--% mel, misc_electron
--#

--% mbedj, misc_be_django_corona
--#

--% mbeno, misc_be_node_corona
--#

--% mqt, misc_qtcmake
--#

--% mqt2, misc_qtcmake2
--#

--% msel1, misc_tselflutter1
--#

--% mrn1, misc_reactnative1
--#

--% msun, misc_androidkotlinbasesunflower
--#

--% mrural, misc_rustwarpsimplerest
--#

--% mgseed, misc_mongoseeder
--#

--% urlr, utils_relight_routes
--#

--% upsr, utils_proshop_routes
--#

--% upss, utils_proshop_store
--#

--% upsb, utils_proshop_backend
// u -e'***upsb,*/B^..^'
--#

--% uecommdj, utils_ecommdj
// u -e'***uecommdj,*/B^..^'
--#

--% upnode, utils_proshop_node
--#

--% uhcx, utils_htmlcss
--#

--% uvsb, utils_vertxspringboot
// lebih mirip misc: u -e '***uvsb,*/B'
--#

--% upmern, utils_proshop_mern
--#
