--% repl ,?<kode> = backend lang
lokasi code di ???
akses dg??? repl: ,?<kode>

<framework> # endpoint @ verbs # middlewares | response text,json,template,code ;;
response 
  text          |   hello, world
  json          |{  1=satu,2=dua,3=tiga }
  template      |>  filename|{  1=satu,2=dua,3=tiga }
  code          |@  lalangcode

jadi lupa gimana cara aksesnya:
app/transpiler/backend/main.py
lalu di"share" di: app/quick/myback.py
```
from app.transpiler.backend.main import process_language

def myback(request):
    """
    config/route+handler/route+handler...
    wait up, bukannya dah bikin something similar???
    """
```

creator/repl.py:
elif text .startswith (','):
  elif code .startswith('?'):
    from app.transpiler.backend.main import myrepl
    myrepl()
ternyata ,? <kode backend>

program: statement+
statement: route_statement "{ROUTE_TERMINATOR}"

route_statement: backend_config? endpoint_path verbs? middlewares? path_handler?

ini bagian paling penting <framework> # endpoint @ verbs # middlewares | response text,json,template,code

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

CODE_STARTER = "|@"
CODE_ENDER = "=="
ROUTE_TERMINATOR = ";;"

path_handler_response: "|" HURUF_DIGIT_RESPONSE -> response_text
  | "|{{" HURUF_DIGIT_OBJECT "}}" -> response_json
  | "|>" HURUF_DIGIT_OBJECT ("|{{" HURUF_DIGIT_OBJECT "}}")? -> response_template // |>filename|jsonlikecontext
  | "{CODE_STARTER}" HURUF_DIGIT_CODE -> path_handler_code // apa ini butuh masuk lalang?

# nd#/satu@g|@ts/?+gaia ;; nd#/dua@g|@ ts/?+wieke ;; nd#/tiga@g |@ ts/?+hello ;;
# nd#/satu@g|@ts/?+gaia == ;; nd#/dua@g|@ ts/?+wieke == ;; nd#/tiga@g |@ ts/?+hello == ;;

# #api/users@gp#cors|huruf text bahasa
# #api/users@gp#cors/200|huruf text bahasa
# #api/users@gp#cors/200|{1=satu,2=dua,3=tiga}
# #api/users@gp#cors/200|@/ts/%name='usef'
# dj#api/users@gp#cors/200|@/ts/%name='usef'
# [:8000][/tempdb]dj#api/users@gp#cors/200|@/ts/%name='usef'
# [:8000][usef:rahasia@localhost:6379/tempdb]dj#api/users@gp#cors/200|@/ts/%name='usef'
# [0.0.0.0:8000][usef:rahasia@localhost:6379/tempdb]dj#api/users@gp#cors/200|@/ts/%name='usef'
--#

--% scraping lang
lokasi code di ???
app.quick:			/sc>...
--#

--% selenium lang
app.quick:			/sel>...

misal kita pengen buka upwork dg cepat...

[app.quick][sel>]
/sel>config|find|oper|find|oper|...|url

../sel>hless,chr|css=span.normal.ng-binding/txt/nop/q|https://pasardana.id/fund/2789
../sel>hless,chr|css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/nop/q|https://pasardana.id/fund/2789
../sel>hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/nop/q|https://pasardana.id/fund/2789
../sel>hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/css=a.btn.btn-signin/c/nop/q|https://pasardana.id/fund/2789
../sel>hless,chr|nop/wi/nop/wt=css=span.normal.ng-binding=Rp./css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt / css=a.btn.btn-signin/c /nop/q|https://pasardana.id/fund/2789

../sel>|nop/wi|up1
../sel>|nop/wi|https://www.upwork.com/nx/jobs/search/?q=python&sort=recency&page=2

--#

--% notebook lang, /nb>
app.quick:			/nb>...
  fm//nb>PV/2r/t=selamat datang pujaanku/sun/tree1/tree2/##
--#

--% dotlang, diagram lang, /dot)
app/quick/__init__.py:
```
elif code .startswith('dot)'):
  request = code.removeprefix('dot)').strip()
  from .languages.dotlang import dotlang
  if request:
    if request == '@': # ../dot)@
      dotlang(trypaste())
    else:
      dotlang(request)
  else:
    dotlang()
  return
```

[shape=box,color=red,fill=yellow,fontsize=24]
a.b.c[shape=triangle].d.e[shape=oval]
|
b.d[fill=blue,shape=Mdiamond]
|
k.telor[shape=egg],bintang[shape=star],terakhir
--#

--% imagelang, meme lang, /img)
app/quick/__init__.py:
```
elif code .startswith('img)'):
  request = code.removeprefix('img)').strip()
  from .languages.imagelang import imagelang
  if request:
    # bisa dari clipboard dg ../img)@
    if request == '@':
      imagelang(trypaste())
    else:
      imagelang(request)
  else:
    imagelang()
  return
```

<canvas[w=1000,h=800,color=red](
  <img[x=100,y=500,w=.25,h=.25,rotateccw=45,grayscale=50,alpha=80,src=rect,color=yellow]
  <img[x=10,y=150,w=500,h=600,src=https://media.gettyimages.com/photos/bella-thorne-attends-the-los-angeles-premiere-midnight-sun-at-on-picture-id932666434?s=2048x2048]
  <text[x=10,y=250,sz=14,color=blue]|hello mama mia di tinggi 250
  <text[x=10,y=500,sz=14,color=green]|ini di tinggi 500
)
--#

--% tviewlang, forms languages, go form lang, hasilkan tviewform.go
tinggal kita lengkapi:
go tui, pyqt5, web, mobile

<header<footer<sidebar<rightbar
<main(
  <form(
    <input[name=myinput]
    <pass[name=myarea]
    <check[Masukkan_yang_saya_minta,0]
    <combo[enam,tujuh,delapan,sembilan]
    <button[Tekan_aku]
  )
)
--#

--% guilang, gui language, /G), /G)@
<window[main, title=Si borokokok teh](
<layout[type=v,name=mainlayout](
  <layout[type=h,name=forms](
    <form(
      <row[label=pertama,control=edit]
      <row[label=kedua,control=edit]
      <row[label=ketiga,control=edit]
    )
    <scrollbar[max=200]
  )
  <layout[type=h,name=pages](
    <split[type=h](
      <page[label=pertama,control=edit]
      <page[label=kedua,control=edit]
      <page[label=ketiga,control=edit]
    )
  )
  <layout[type=h,name=pages](
    <tab(
      <page[label=pertama,control=edit]
      <page[label=kedua,control=edit]
      <page[label=ketiga,control=edit]
    )
  )
  <layout[type=h,name=pages](
    <stacked(
      <page[label=pertama,control=edit]
      <page[label=kedua,control=edit]
      <page[label=ketiga,control=edit]
    )
  )
  <cal[label=isi kalendar kah]
  <layout[type=h,name=buttons](
    <label[label=this is just a label]
    <button[label=hello 1]
    <button[label=hello 2]
    <button[label=hello 3]
  )
  <layout[type=h,name=editor](
    <edit[label=an editor for you bisa tekan enter]
    <editmulti[label=multiline editor gak bisa tekan enter]
  )
  
  <layout[type=h,name=waktu](
    <date[label=ignore date]
    <time[label=ignore time]
    <datetime[label=ignore datetime]
  )
  <layout[type=h, name=combien](
    <check[label=a chebox]
    <combo[label=ignore combo]
    <radio[label=radio 1]
    <radio[label=radio 2]
    <radio[label=radio 3]
  )
  <layout[type=h,name=gerak](
    <dial[label=ignore dial]
    <progress[label=ignore progress]
    <list[label=ignore list]
    <lcd[label=2024]
    <slider[label=ignore slider]
  )
  <layout[type=h,name=spiner](
    <spin[label=spin]
    <spinfloat[label=spinfloat]
  )
  <layout[type=h,name=horizle](
    <button[label=di dalam]
    <check[label=another checkbox]
    <button[label=di dalam 2]
    <button[label=di dalam 3]
    <message[label=ini pesan untuk keluar]
    <input[label=masukkan apa saja]
    <fontinput[label=input font]
    <fileinput[label=input file]
  )
)
)
```
if namaparent in ['window','wnd','w','W']:
elif namaparent in ['layout','lyt','lay','l','L']:
elif namaparent == 'flow':
elif namaparent == 'form':
elif namaparent == 'row':
elif namaparent == 'stacked':
elif namaparent == 'tab':
elif namaparent == 'split':
elif namaparent == 'page':
elif namaparent in ['button','btn','b','B']:
elif namaparent in ['message','msg','m','M']:
elif namaparent in ['input', 'inp', 'i', 'I']:
elif namaparent == 'label':
elif namaparent == 'edit':
elif namaparent == 'editmulti':
elif namaparent == 'plain':
elif namaparent == 'note':
elif namaparent == 'editor_standard':
elif namaparent == 'check':
elif namaparent == 'combo':
elif namaparent == 'radio':
elif namaparent == 'radios':
elif namaparent == 'date':
elif namaparent == 'time':
elif namaparent == 'datetime':
elif namaparent == 'spin':
elif namaparent == 'spinfloat':
elif namaparent == 'scrollbar':
elif namaparent == 'slider':
elif namaparent == 'progress':
elif namaparent == 'dial':
elif namaparent == 'combofont':
elif namaparent == 'lcd':
elif namaparent == 'clock':
elif namaparent == 'casio':
elif namaparent == 'font':
elif namaparent == 'fontinput':
elif namaparent == 'fileinput':
elif namaparent == 'filetree':
elif namaparent == 'windowbrowser':
elif namaparent == 'notification_button':
elif namaparent == 'notification_anim':
elif namaparent == 'notification_clock':
elif namaparent == 'list':
elif namaparent == 'table':
elif namaparent == 'cal':
```
--#

--% tuilang, rich console lang
<layout(
  <content(
    <row[fraction=1](
        <col[fraction=3]
        <col[fraction=7]
    )
    <row[fraction=6](
        <col
        <col
    )
    <row[fraction=2](
        <col
        <col
    )
    <row[fraction=1](
        <col
        <col
    )
  )
)
--#

--% chartlang, /chart)
```
elif code .startswith('chart)'):
  request = code.removeprefix('chart)').strip()
  from .languages.chartlang import chartlang
  if request:
    if request == '@': # ../chart)@
      chartlang(trypaste())
    else:
      chartlang(request)
  else:
    chartlang()
  return
```

tinggal lengkapi dg pyqt5 chart...
<canvas[cols=5](
  <piechart[x=A/B/C/D/E,y=70/40/90/20/50]
  <barchart[x=1/2/3/4/5,y=10/20/30/40/50]
  <linechart[x=1/2/3/4/5,y=10/20/30/40/50]
  <donutchart[x=A/B/C/D/E,y=70/40/90/20/50]
  <map
)
--#

--% curly lang
../y. https://detik.com [o=kuda.html]
--#

--% special command
languages dan specialcmd:
  **VF*
    VFS
    VFG
    VFGi
    VFGf
    VFGd
    VFGo
    VFGb
    VFC
    VFCG
    VFCG2
    VFCGS
    VFCGN
    VFCGD
  **term
  **term1
  **favico=filename.png
    u -e ".,d\n\tfilename.png,f(img=ava1)\n\t**favico=filename.png"
  **favgen=filename1.png
    u -e ".,d\n\tfilename1.png,f(img=ava1)\n\t**favgen=filename1.png"
  **favmake=filename2.png
    u -e ".,d\n\tfilename2.png,f(img=ava1)\n\t**favmake=filename2.png"
  **notif=judul=pesan
    u -e "**notif=judul=pesan"
  **notif2=judul=pesan
  **sccap=filepath
  **screc=filepath
    "**screc=rekam.mp4"
  **screc=filepath=long
    "**screc=rekam.mp4=10"
  **screc=filepath=long=br
    -e "**screc=rekam.mp4=10=3" (br=3 berarti 3fps)

  **picsum
  **picsum=tulisan
  **picsum=atas||bawah
  **unsplash
  **unsplash=tulisan
  **unsplash=atas||bawah
  **lalang, **lalang* (edit)
    from lalang.main import myrepl
  **decl, **decl* (edit)
    from app.transpiler.frontend.main import myrepl
  **css, **css*
    from app.transpiler.css.main import myrepl
  **be, **be*
    from app.transpiler.backend.main import myrepl
  **flu, **flu*
    from langs.flutter.main import myrepl
  **@
    from app.transpiler.csv.process import process_language
    u -e'/%$*csv/process.py'
      csv_item: 
        "mg"  -> mongoose
        | "sqlz"      -> sequelize
        | "pg"        -> sql_postgres
        | "ms"        -> sql_mssql
        | "my"        -> sql_mysql
        | "sqlt"      -> sql_sqlite
        | "torm"      -> nest_typeorm
        | "mg2"       -> nest_mongoose
        | "pris"      -> prisma
        | "hbr"       -> hibernate
        | "bts"       -> mybatis
        | "go"        -> struct_go
        | "rs"        -> struct_rs
        | "kt"        -> struct_kt
        | "ts"        -> struct_ts
        | "dj"        -> django_orm
        | "nsm"       -> help_nest_mongo
        | "nsp"       -> help_nest_postgres
        | "json1"     -> json1
        | "json2"     -> json2
        | "csv"       -> csv
    u -e'**@pris/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s'

ternyata csv lang bisa juga dari specialcmd...
--#

--% aws language
ini bisa dipamerkan di github, krn skrg gak berguna utk diri sendiri...


elif code .startswith('aws)'):
  request = code.removeprefix('aws)')
  if not request:
    from .common import cloudia_instruction
    indah4(f'''[app.quick][/:]\n{cloudia_instruction}''', warna='cyan')
    return
  from .cloudia import cloudia
  cloudia(request)
  return
--#

--% unsorted app.quick
app.quick:			/			      u -e/ = run choice.fmus
app.quick:			/%...       /%specialcmd.py, /%$specialcmd.py, /%$*specialcmd.py
app.quick:			/@...       /@code, app.transpiler.mycsv.process.process_language
app.quick:			/>...       />json|json2|csv|sql,namafile|csvcode, />dc,pg|mg|my|ma|ms|redis
app.quick:			/tar>...    /tar>foldername|node_modules (tar), /tar>foldername*|node_modules (tgz)
app.quick:			/D>...
app.quick:			/b)...
app.quick:			/ref>...
app.quick:			/s>...
app.quick:			/run>...
app.quick:			/hope>...
app.quick:			/fmb>...
app.quick:			/...		    app.quick.bahasa

app.quick.quick_statement: proses app.quick.bahasa, contoh: u -e/Atxt/1 -> len(chtoken(tree))=1, RootNode=1 else RootNode=langs.ucsv.processor(chtoken(tree))
--#

--% string, punctuation coding, sanitising
chars_to_sanitize_in_file_operation = {
  '__DQ': '"',
  '__SQ': "'",
  '__BT': '`',
  '__NL': "\n",
  '__SL': "/",
  '__BS': "\\",
  '__PP': "|",
  '__EQ': '=',

  '__DOLLAR__': '$',
  
  '__AT__': "@", # jangan lupa, yg panjang mendahului yg pendek
  '__AT': "@",
  
  '__PRC__': "%", # jangan lupa, yg panjang mendahului yg pendek
  '__PRC': "%", # ini krn %TEMP%,d dianggap sbg %TEMPLATE_SAVE_VAR etc
  

  '__CL': ":",
  '__SC': ";",
  
  '__LP': "(",
  '__RP': ")",

  '__LK__': "[", # jangan lupa, yg panjang mendahului yg pendek
  '__LK': "[",
  '__RK__': "]", # jangan lupa, yg panjang mendahului yg pendek
  '__RK': "]",

  '__LB': "{",
  '__RB': "}",

  '__LT': "<",
  '__GT': ">",

  '__TAB1': "\t",
  '__TAB2': "\t\t",
  '__TAB3': "\t\t\t",
  '__TAB4': "\t\t\t\t",
  '__SPC1': " ",
  '__SPC2': " "*2,
  '__SPC3': " "*3,
  '__SPC4': " "*4,
  '\\n': "\n",
  '\\t': "\t",
}
--#

--% tdd lang
mulai dg pytest, lanjut dg jest
lainnya menyusul. tetapi di rust dan go ini otomatis, di java perlu junit.

entry point bisa dari kerjaan rock_it
--#

--% faker lang/rencana baru
perlu utk nanti test...
kita pengen:

[5,-100:100|i]
list of ints sebanyak 5 dg nilai antara -100 dan 100

[s]
list of strings sebanyak 10
[5|s:name]
list of full names sebanyak 5

[f]
list of floats
[s:female_name]
list of female names sebanyak 10

[[]]
[[i]]
2D list 10x10 ints

default:
n = 10
range: 0 - 100
--#

--% faker lang so far, app.quick.fakerer
bbrp faker yg sudah dikerjakan...

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

dg quick: ../( kode...
--#
