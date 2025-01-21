--% cli/terminal repl
vars                                      : "V"
class                                     : "@c"
more_classes                              : "@C"
constructor                               : "@t"
field                                     : "@f"
method                                    : "@e"
module                                    : "@m"
struct                                    : "@s"
access_modifier                           : "am"
args                                      : "args"
assign                                    : "A"
async                                     : "as"
block                                     : "B"
byte                                      : "byte"
check                                     : "check"
cli                                       : "cli"
clipboard                                 : "cb"
collection                                : ".coll"
comment                                   : "C"
const                                     : "c"
convert                                   : "v"
csv                                       : ".csv"
dataframe                                 : "dataframe"
datetime                                  : "D"
db                                        : ".db"
docker                                    : ".D"
decorator                                 : "@d"
dict                                      : "d"
email                                     : ".email"
enum                                      : "e"
enumerate                                 : "rate"
env                                       : "E"
errors                                    : ".err"
excel                                     : ".xls"
exception                                 : "x"
extension                                 : "X"
filter                                    : ".Fi"
fold                                      : ".Fo"
for                                       : "4"
for_each                                  : "5"
for_of                                    : "6"
function                                  : "f"
functools                                 : ".ft"
generator                                 : "G"
generic                                   : "g"
grammar                                   : ".g"
gui                                       : "gui"
html                                      : "html"
http                                      : "http"
if                                        : "if"
import                                    : "P"
import_ask                                : "P~"
import_filter                             : "P!"
install                                   : "install"
interface                                 : "@i"
interop                                   : "interop"
invoke                                    : ".iv"
ipc                                       : "ipc"
io_stdout                                 : ".o"
io_stdin                                  : ".i"
io_stderr                                 : ".z"
io_file                                   : ".f"
io_dir                                    : ".d"
iterator                                  : "I"
itertools                                 : ".I"
json                                      : "json"
keyword                                   : "kw"
lambda                                    : "/l"
library                                   : "lib"
list                                      : "l"
lock                                      : ".l"
log                                       : ".L"
loop                                      : "L"
macro                                     : "mac"
main                                      : "M"
main_ask                                  : "M~"
math                                      : "math"
map                                       : ".Ma"
media                                     : "media"
memory                                    : "mem"
msword                                    : ".doc"
network                                   : ".net"
null                                      : "U"
number                                    : "n"
object                                    : "o"
oneliner                                  : "1l"
operator                                  : "Op"
option                                    : ",o"
result                                    : ",r"
package                                   : "p"
parallel                                  : "par"
pdf                                       : ".pdf"
projects                                  : "J"
random                                    : "r"
range                                     : "R"
rx_reactive                               : ".Rx"
recursion                                 : "q"
reduce                                    : ".Re"
reference                                 : ".ref"
reflection                                : ".rel"
regex                                     : ".rx"
repl                                      : ".repl"
rss                                       : ".rss"
selenium                                  : ".sel"
simple_type                               : ".smp1"
simple_typename                           : ".smp2"
serializer                                : ".ser"
sleep                                     : ".sleep"
stream                                    : ".st"
string                                    : "s"
switch                                    : "|"
system                                    : "S"
task                                      : "k"
test                                      : "T"
set                                       : ".set"
tuple                                     : ".tup"
timer                                     : "tmr"
thread                                    : "t"
type                                      : "y"
uuid                                      : "uuid"
version                                   : ".ver"
web                                       : "W"
while                                     : "w"
xml                                       : "xml"
yaml                                      : ".yaml"
threed                                    : "3d"
deque                                     : "deque"
queue                                     : "queue"
stack                                     : "stack"
compare                                   : "2"
karya                                     : ":karya"
oefening                                  : "7"
regrammar                                 : "8"
only_toc          : "#"
show_content      : "*"
--#

--% elif handled_by_repl(text):
elif handled_by_repl(text):
--#

--% repl_service, schnell.db.ReplService
repl_service = schnell.db.ReplService()

myredis memanggil dg berbagai macam cara:
from .replservice import repl_service
hasil, meta = repl_service.fastmapper(code, meta_input=metacontent)
hasil, meta = repl_service.process(content, meta_input=metacontent)
repl_service.process(code)
--#

--% /something, db.myredis.redis_repl, vscode/redis service/myredis repl
db.redis_repl(code)

if code == '.conn' or code == '.C':
elif code == '.load' or code == '.L':
elif code == '.CLR':
elif code .startswith('.clearload') or code == '.reboot' or code == '.restart':
elif code .startswith('.D'):
elif code .startswith('.K '):
elif code .startswith('.V '):
elif code .startswith('.K2 '):
elif code .startswith('.V2 '):
elif code .startswith('.K3 '):
elif code .startswith('.V3 '):
elif code .startswith(SubKey) or code == 'S' or code .startswith('S ') or code .startswith(PubKey):
  jk /S namakanal atau /Sub namakanal dan /Pub namakanal|data
  maka dihandle di sini
  handlePubsub(code)
    if code.startswith(SubKey) or code == 'S' or code.startswith('S '):
      redis_subscribe(channel)
        pubsub = r.pubsub()
        pubsub.subscribe(channel)
        for message in pubsub.listen():
          # ada 6 jenis: subscribe, unsubscribe, psubscribe, punsubscribe, message, pmessage.
          if message.get('type') == 'message':
            if isinstance(data, (bytes, bytearray, str)):
            else:
              redis_publish(data, redis_config['from_server'])
            if message_callback: message_callback(data, message)
    elif code.startswith(PubKey):
      redis_publish(message, channel)
elif code .startswith('@') or code .endswith('@'):
elif code .startswith('#') or code .endswith('#'):
elif code .startswith('repl:'):
else:
--#

--% vscode extension, mengirim dan menerima data dari redis pubsub
const data = {
  content: 'fastmapper:' + wordText,
  meta: {
    metaWorkspacesFspath,
    metaWorkspacesPath,
    metaDocument,
  }
}
redis_publish(data);

const data = {
  content: word,
  meta: {
    metaWorkspacesFspath,
    metaWorkspacesPath,
    metaDocument,
  }
}
redis_publish(data);

function redis_publish(data: object, channel: string = channel_name) {
  const message = JSON.stringify(data);
  publisher_connection.publish(
    channel, 
    message, 
    function() {
      console.log(`     
        ******
        [2/3] Publishing: [${message}].
        HOST = ${HOST}
        ******
      `);
    }
  );
}
--#

--% [code utk scraping
from app.scrape.scraper import process(code)
--#

--% backend language: ,?
backend language: ,?

Thu 23/174 01:21:21 [^✔]py: ,?
BE 2022-06-22T18:23:32.003755 >>

dari app/transpiler/backend/bahasa.py:
```
program: statement+
ROUTE_TERMINATOR = ";;"
statement: route_statement "{ROUTE_TERMINATOR}"
  | "m>" model_statement
  | "r>" response_statement
  | "h>" method_handler_statement // get(), post(), put(), delete(), patch()

.

////////////////////////////// route_statement
route_statement: backend_config? endpoint_path verbs? middlewares? path_handler?

backend_config: serverconfig? dbconfig? backend_items
backend_items: backend_item ("," backend_item)*
backend_item: "nd" -> express  
  | "dj" -> django
  | "fa" -> fastapi
  | "fl" -> flask
  | "mn" -> micronaut
  | "mux" -> mux
  | "ns" -> nest
  | "nx" -> next
  | "qk" -> quarkus
  | "sb" -> springboot

// minimal :8000
serverconfig: "[" hostport "]" -> konfigurasi_server

// minimal: /tablename
dbconfig						: "[" userpass? hostport? dbspec "]" -> konfigurasi_database
dbspec							: "/" dbname
userpass						: user ":" pass "@"
hostport						: host? ":" port
user								: HURUF
pass								: HURUF_PASSWORD
host								: HURUF_HOST
port								: BILBUL
dbname							: HURUF

//group_path: "/" rest_path
endpoint_path: "#" rest_path
rest_path: HURUF_DIGIT_PATH

verbs: "@" verb+
verb: "g" -> get                              // default
  | "p" -> post
  | "d" -> delete
  | "u" -> put
  | "a" -> patch
  | "h" -> head
  | "o" -> options

middlewares: "#" middleware ("," middleware)*
middleware: "custom" -> mw_custom
  | "body" -> mw_bodyparser
  | "cors" -> mw_cors
  | "fileupload" -> mw_fileupload
  | "helmet" -> mw_helmet
  | "morgan" -> mw_morgan
  | "ratelimit" -> mw_ratelimit
  | "session" -> mw_session

// ada default response: text = "ok"

path_handler: path_handler_status? path_handler_response
path_handler_status: "/" response_code
response_code: HURUF_DIGIT

path_handler_response: "|" HURUF_DIGIT_RESPONSE -> response_text
  | "|{{" HURUF_DIGIT_OBJECT "}}" -> response_json
  | "|>" HURUF_DIGIT_OBJECT ("|{{" HURUF_DIGIT_OBJECT "}}")? -> response_template // |>filename|jsonlikecontext
  | "{CODE_STARTER}" HURUF_DIGIT_CODE -> path_handler_code // apa ini butuh masuk lalang?
```
--#

--% csslang: ,< dan frontend lang: ,>
elif text .startswith (','):

,<
from app.transpiler.css.main import myrepl
,<code
from app.transpiler.css.main import process_language(code)

,>
from app.transpiler.frontend.main import myrepl
,>code
from app.transpiler.frontend.main import process_language(code)

,$
lokasi = '\\\\\\\\wsl$\\\\Ubuntu-20.04\\\\home\\\\usef\\\\work\\\\ulibs\\\\schnell\\\\app\\\\transpiler\\\\frontend'
perintah_shell(f'cmd.exe /c wt.exe -d "{lokasi}"')

,#
lokasi = env_get('ULIBPY_DAHSYATDIR')
perintah_shell(f'cmd.exe /c wt.exe -d "{lokasi}"')

,github
lokasi = 'c:/work/github'
perintah_shell(f'cmd.exe /c wt.exe -d "{lokasi}"')

,`pola-file
cari pola-file pada schnell/app, jk ketemu dan ada 1 file maka edit,
jk ketemu dan ada bbrp file, print list warna

--#

--% csvlang: ,.
,.
from app.transpiler.mycsv.main import myrepl()

,.code
from app.transpiler.mycsv.main import process_language(code)
--#

--% lalang: ,, dan ,/
,,
from app.transpiler.main import myrepl()
,,code
from app.transpiler.lalang import process_language(code)

,/
from app.transpiler.refactor import myrepl()
,/code
from app.transpiler.refactor import process_language(code)

,/py/for$i/..0,1000${}
,/py/for$item/anak_tree${} if(data(item)){}
,/py/for$item/anak_tree${}if(data(item)){}

,/rs/@Database{inner:Di,s | new(){}}
--#

--% DF declarative language
creator.declarative.handler
	DF...code...
	DF[yaml]...code...
	insn: insn
		declarative_program
			fileconfig  yaml
			declaratives___
				element
					element_name    apiVersion
					cdata_text      v1
    DF<a<b(<c[disabled=true,className=monyong]<d)<e
    DF<div[className=search](<div[className=searchInputs](<input[type=text]<div[className=searchIcon])<div[className=dataResult])
    DF<d[cn=search](<d[cn=searchInputs](<i[t=text]<d[cn=searchIcon])<d[cn=dataResult])
    DF[yaml]<d[cn=search](<d[cn=searchInputs](<i[t=text]<d[cn=searchIcon])<d[cn=dataResult])
    DF<d[cn=search](<d[cn=searchInputs](<i[disabled,t=text]<d[cn=searchIcon](<SearchIcon))<d[cn=dataResult](<a(<p)))
--#

--% #flutter-code
langs.flutter.main...
##code
  langs.flutter.main.process_langiage(code or default_program)
  default_program adlh:
  ma(tit:txt("monyet",slv:/icsearch),dbg:scaf(body:row(ch:dtab),fab:csv(txt:txt("hello boyz"))),thm:thmd(pmc:/tsfz,ab:sbui),hm:/mqw)
#E
  code schnelldir/langs/flutter/main.py
#att
  langs.flutter.main.show_attrs(code)
#con
  langs.flutter.main.show_const(code)
#wid
  langs.flutter.main.show_widgets(code)
#all something
  langs.flutter.main.show_all(code)
#flu
  langs.flutter.flumain.repl()
else
  langs.flutter.main.process_language(code)
--#

--% sched. (app.schedulerutils.py:handle_scheduler, data.scheduler.scheduler.py)

# main code
```
elif text.startswith('sched.'):
from app.schedulerutils import handle_scheduler
code = text.removeprefix('sched.').strip()
if code:
  handle_scheduler(code)
```

# internal handling
```
if request.startswith('+1'):
elif request.startswith('+i'):
elif request.startswith('+c'):
elif request in ['start', 'S']:
elif request in ['stop', '/S', 'shut', 'end']:
elif request in ['ls', 'list', 'dir', 'cetak', 'print']:
elif request.startswith('tick'):
elif request in ['block', 'sync']:
elif request in ['baru', 'async']:
elif request.startswith('rm') or request.startswith('hapus'):
elif request in ['del']:
```

kita hampir gak butuh/pake block/blocking/sync, krn kita pengen bisa gunakan lagi repl.

baru secara default hasilkan: 
scheduler = BackgroundScheduler()
tick<angka> hasilkan:
interval_ = int(code)
detik(tick, detik=interval_)
dimana kita punya:
````
def tick():
  print('Tick! The time is: %s' % datetime.now())
```

# setTimeout, one time schedule
+1(func)
+1(func),1m30s
+1(func),1m30s|id-of-job
+1(func*),1m30s|id-of-job
kita cek jk func ada di @data/module/... jk belum maka "micro" buat baru

# setInterval, periodical schedule
+i(func)

# cron scheduler
+c(func)
cron(func, h=None, m=None, s=None, d=None, w=None, month=None, year=None, dow=None, **kwargs):
+c(func),m=*/15|id=someid

# typical flow
- baru    
- tick10 atau tick 10 utk demo
- start
- ls
- del atau rm <id>
  del utk hapus pilih
  rm <id> utk hapus id atau all
- ls

# contoh pake:
Wed 15/166 07:56:25 [^✖]py: sched.ls
Wed 15/166 07:56:26 [^✖]py: sched.baru
Wed 15/166 07:56:35 [^✖]py: sched.ls
Wed 15/166 07:56:36 [^✖]py: sched.tick10
Wed 15/166 07:56:49 [^✖]py: sched.ls
278d5e23a7564113b2f962a7335ff7ea => tick (trigger: interval[0:00:10], pending)
Wed 15/166 07:56:51 [^✖]py: sched.start
Wed 15/166 07:57:04 [^✖]py: sched.ls
278d5e23a7564113b2f962a7335ff7ea => tick (trigger: interval[0:00:10], next run at: 2022-06-15 07:57:19 +07)
Tick! The time is: 2022-06-15 07:57:29.779624

# contoh lain:
sched.baru
sched.+1(print_wieke),30s|calling_wieke
sched.start

secara default kita punya:
```scheduler = BackgroundScheduler()```
yg setara dg ```sched.baru```
sched.start memanggil: scheduler.start()
sched.stop memanggil: scheduler.shutdown()

kita juga bisa edit
+1(nama_fungsi_asal*),1s
di sini akan edit file data/scheduler/scheduler.py
contoh:
```sched.+1(asal*),1s```
--#

--% dockerlang: .Dcode
from .repl_docker import repl_docker(code)
perlu lihat bisa ngapain aja nih...
--#

--% elif text in ['diary', 'own', 'sh'] or any([text.startswith('!'), text.startswith('pypkg')]):
elif text in ['diary', 'own', 'sh'] or any([text.startswith('!'), text.startswith('pypkg')]):
--#

--% elif text and text[0] in puncs_map.keys():
elif text and text[0] in puncs_map.keys():
--#

--% |code, |10, |100
creator.repl_help.latest_file_handler(text)
--#

--% @code utk ocr dan sort clipboard
creator.repl_language.ocr.ocr
@sort
  print app.collutils.sort_lines(clipboard)
@
  creator.repl_language.ocr.ocr()
  ocr print saja
@@
  creator.repl_language.ocr.ocr(True)
  ocr + search di google
@code
  ai.autolib.auto_process(code)
--#

--% wmc<something>
creator.repl_help.wmc_handler(code)
--#

--% reload
app.utils.env_reload()
--#

--% c | cls | clear
clear
--#

--% translate tr#code
bahasa = "es+fr+de+nl+ru+id"
sp.run(f"""trans -b :{bahasa} "{code}" """, shell=True)
--#

--% ?L/?lang, ?decl, ?u ganti envi, ?gui, ?out, ?wf, ?
self.config.change_configuration(code)
?L atau ?lang
?decl
?u<something>
?gui
?out
?wf
? = print config

?u
Pilih salah satu: ULIBPY_FMUS_DEBUG
  <di sini ada opsi utk milih yg mana>
Nilai lama = 0. Masukkan nilai baru untuk ULIBPY_FMUS_DEBUG: 2
{
    "current_chart": "highchart",
    "current_gui": "pyqt5",
    "current_language": "py",
    "current_mobile": "android",
    "current_declarative": "react",
    "cwd": "C:\\Users\\usef\\work\\sidoarjo\\schnell\\creator",
    "print_after_process": 1,
    "verbose": 0,
    "working_folder": "/tmp"
}
--#

--% \py, \rs
ganti bahasa
--#

--% lang<something>
creator.repl_help.lang_helper(text)
--#

--% repl<something>
creator.repl_help.repl_handler(text)
--#

--% ai
ai.ai_repl.run()
--#

--% comm
from commlib import comm_repl.run()
--#

--% env code
print env+value berisi code
--#

--% status
print repl status (last file+lineno)
--#

--% package.json, package.json*, package.json|pkgv1,pkgv2,pkgv3
from creator.package_json import process_packagejson
--#

--% ulib<something>
creator.repl_help import ulib_helper(text)
--#

--% fm/FMUS CODE
elif text .startswith('fm/'):
--#

--% ..FMUS CODE
elif text .startswith('..'):
--#

--% img<something>
creator.imghandler.imghandler(text)
--#

--% l code
app.utils.Launcher.launch(code)
--#

--% g/keyword
app.utils.buka(google search keyword)
--#

--% :py, :scala, dst.
app.executor.FileExecutor().exec(lang)
--#

--% help | history | h
elif text .startswith('h ') or text == 'h' or text == 'h*' or text == 'history':
--#

--% dimulai dg petik: elif text .startswith ('H') or text .startswith('`'):
``    default
`#    gunakan (unused)
`r    close, newline, open
`##   gunakan + default (unused)
```   contoh index/fmus
`1    $$link utk entry yg terlalu panjang
`8    utf-8 python code
`@    dari clipboard
`whatever   bahasa

if text == '``': print_copy(template_default_entry)
elif text == '`#': print_copy(template_use_entry) <-- ini entry "gunakan" yg gak lg dipake
elif text == '`r': print_copy(template_reverse_entry) <-- ini close lalu open+spasi
elif text == '`##': print_copy(template_use_entry + '\n' + template_default_entry) <-- hell, ngapain gak guna nih..
elif text == '```': print_copy(template_index_mk) <-- sample index/fmus
elif text == '`1': print_copy(template_link) <-- buat $$link=ULIBPY_SNIPPETS/ utk isi di tempat lain (jk entry panjang)
elif text == '`8':
  '''
  `8 akan print:
  # -*- coding: utf-8 -*-
  tapi ini masih dari repl, belum dari vscode/replservice
  jd hrs ada usaha utk gabungkan dalam satu service
  antara vscode dan repl
  mungkin replservice dlm folder sendiri?
  '''
  print_copy(template_python_utf8)
elif text == '`@':
  ''' kita entryfy isi clipboard '''
  # cek jk multiline
  clip = trypaste()
  if '\n' in clip:
    entrified = [template_entrify.replace('__TITLE__', item) for item in clip.splitlines() if item]
    print_copy('\n'.join(entrified))
  else:
    print_copy(template_entrify.replace('__TITLE__', clip))
else: <-- handle `reference dsb...
  prefix = 'H' if text .startswith ('H') else '`'
  from .grammar import bahasa
  baris = [item for item in bahasa.splitlines() if item and ':' in item and 'HURUF' not in item and item.endswith('"')]
  if text .startswith (f'{prefix}*'):
    '''
    jika berbentuk berikut, maka minta disort dulu
    `*tailwind
    H*tailwind
    '''
    baris = sorted(baris)
    code = text.replace(f'{prefix}*', '', 1).strip()
  else:
    '''
    `tailwind
    Htailwind
    '''
    code = text.replace(f'{prefix}', '', 1).strip()

  if code:
    baris = [item for item in baris if code in item]
  print('\n'.join(baris))
--#

--% else: ff, f@c, dst
kita bikin daftar (spt halnya press ` di repl)
--#

--% UNUSED text in self.session.completer.words:
text = get_definition_by_key_permissive_start(self.current_completer_source, text)
that's it gak ngapa2in
--#

--% UNUSED after<code>
elif text .startswith('after'):
--#

--% UNUSED print#
print(RenderTree(self.pohon))
--#

--% UNUSED modify#code
self.modify(code)
--#

--% UNUSED elif text == 'gen' or text == 'generate':
self.generate_file()
--#

--% UNUSED elif text == 'out' or text == 'output':
self.generate_file(False)
--#

--% UNUSED elif text == 'decl':
self.generate_declarative_program(self.pohon)
--#
