--% ../ atau u -e/ = jalankan choice.fmus
../         = di repl
u -e/       = di cli
schnell/app/quick/choice.fmus
harusnya daripada ../run>*@d/1s mending ../ ini saja langsung ke kerjaan yg sering kita lakukan.
--#

--% ..//searchterm atau u -e//searchterm
```mulai dg search, terutama cari yg epmus, jk ada hasil, maka otomatis langsung masuk clipboard```
C:\Users\usef\work>u -e//geura
0. C:\Users\usef\work\sidoarjo\database\geura\devop.emus.mk:git config --global user.name/user.email/epmus
---------- C | \Users\usef\work\sidoarjo\database\geura\devop.emus.mk:git config --global user.name/user.email/epmus
.,d
    $* git config --global user.name "__INPUT__"
    $* git config --global user.email "__INPUT__"

```sekarang sudah masuk clipboard, tinggal u utk jalankan```
C:\Users\usef\work>u
[C:\Users\usef\work] clipboard: [.,d
    $* git config --global user.name "__INPUT__"
    $* git config --global user.email "__INPUT__"...]
Press [y] jk pengen execute clipboard: y
--#

--% ../%<something>, find+edit file
u -e'/%specialcmd.py'
u -e'/%$specialcmd.py'
u -e'/%$*specialcmd.py'

from .quick_statement import peek_file
peek_file(code)
--#

--% ../@<something>, csvlang
u -e'/@code'
from app.transpiler.mycsv.process import process_language
process_language(request)

jadi ../@ adlh csv lang...ini sama dg apa? <koma dot>

ada 4 cara panggil csvlang:
,.          kode
../@        kode
../C.       kode (atau ../c. ???)
**@         kode
12345
--#

--% ../><something>, generate json,docker-compose
u -e'/>json|json2|csv|sql,namafile|csvcode'
u -e'/>dc,pg|mg|my|ma|ms|redis'

from app.special import genfile
genfile(request)
--#

--% ../tar><something>
u -e'/tar>foldername|node_modules'		foldername.tar
u -e'/tar>foldername*|node_modules'		foldername.tgz
--#

--% ../D><something>, dahsyater
u -e'/D>dj|[/tempdb]{@Todo}title,s;description,t;done,b'
u -e'/D>=filepath=barisentry'
from .dahsyater import dahsyater
dahsyater(request)
--#

--% ../b), blitzkrieg
/b) language/filename|csvcode
u -e'/b)cpp/cm1|recipe05.cpp'
u -e'/b)cpp/cm1|recipe05.cpp,output.exe'
from .blitz import blitz
blitz(request)

```
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

mari kita bahas?
--#

--% ../sc><something>
../sc>colly/.article__title//|https://www.scmp.com/

lihat juga app.scrape

fm//sc>c/.article__title//|https://www.scmp.com/
fm//sc>c/a[data-testid=__BS"article-link__BS"]//|https://www.smh.com.au/
fm//sc>c/h2.titleNews//|https://www.thejakartapost.com/
fm//sc>c/div.article.article-tri-headline h2 a//|https://www.dailymail.co.uk/auhome/index.html

bloomberg bs deteksi auto
fm//sc>c/a.story-list-story__info__headline-link//|https://www.bloomberg.com/asia/
fm//sc>c/h3.story-package-module__story__headline//|https://www.bloomberg.com/asia
scrapy shell
fm//sc>https://medium.com/tag/data-science
response.xpath("//a[@class='au av aw ax ay az ba bb bc bd be bf bg bh bi']/@href").extract()
response.xpath("//a[@class='au av aw ax ay az ba bb bc bd be bf bg bh bi']/div[1]/h2/text()").extract()

versi goquery
fm//sc>gq/.article__title//|https://www.scmp.com/
fm//sc>gq/.s-post-summary--content@h3@.s-post-summary--content-excerpt//|https://stackoverflow.com/questions/tagged/python
tag: xpath, scrapy, web-scraping
fm//run>*@d/so.fmus

fm//sc>gq/.bn.fw.kl.km.kn.ko.ga.kp.kq.kr.ks.ge.kt.ku.kv.kw.gi.kx.ky.kz.la.gm.lb.lc.ld.le.gq.gr.gs.gt.gv.gw.fu//|https://medium.com/tag/programming
fm//sc>gq/.bn.fw.ko.kp.kq.kr.ga.ks.kt.ku.kv.ge.kw.kx.ky.kz.gi.la.lb.lc.ld.gm.le.lf.lg.lh.gq.gr.gs.gt.gv.gw.fu//|https://medium.com/tag/data-science

fm//sc>gq/.crayons-story__title//|https://dev.to/
fm//sc>gq/.crayons-story__title//|https://dev.to/t/appwritehack

medium data science
fm//sc>s///|https://medium.com/tag/data-science/
fm//sc>s///|https://medium.com/tag/programming/
fm//sc>s///|https://medium.com/
--#

--% ../sel><something>
/sel>config|find|oper|find|oper|...|url

Rp. 2.405,8600 19 April 2022
<span class="normal ng-binding">Rp.</span> 2.405,8600
<span class="date ng-binding">19 April 2022</span>

nop/wt=css=span.normal.ng-binding

../sel>hless,chr|css=span.normal.ng-binding/txt|https://pasardana.id/fund/2789
../sel>hless,chr|css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt|https://pasardana.id/fund/2789
../sel>hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt|https://pasardana.id/fund/2789
../sel>hless,chr|nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt/css=a.btn.btn-signin/c|https://pasardana.id/fund/2789

../sel>hless,chr| nop/wt=css=span.normal.ng-binding/   nop/wi/css=span.normal.ng-binding/txt/css=span.date.ng-binding/txt / css=a.btn.btn-signin/c|https://pasardana.id/fund/2789
--#

--% ../nb><something>
../nb>content/content/content/content|filepath

--#

--% ../ref><something>, reflection...sudah gak berguna sejak bisa pake upy
../ref>file/fungsi/args
--#

--% ../s><something>
search
../s>  ...search code...

u -e"/s>package main|__PWD"
u -e"/s>~~main.go|__PWD"
u -e"/s>~src/|__PWD"
u -e"/s>~main|__PWD"
u -e"/s>#main|__PWD"

word_content_search(basefolder, code)
system_find(basedir, pattern, capture=False, find_cmd='find', case_insensitive=True)
    pattern adlh filename yg akan menjadi: *filename*
s>cari_string|file
s>#cari_namafile|file
s>~cari_namafile_dg_pattern|file
files = walk_fullpath_skipdirs(basedir, skipdirs=['.git', '__pycache__'])
dirs = walk_fulldirs(basedir, skipdirs=['.git', '__pycache__'])
--#

--% ../run><something>, ../run>*@d/1s
../run>>
@s lihat dirs di @s				
../run>#
@s lihat files di @s
../run>^
@s tree di @s
../run>*					run file
filename.fmus
filename.fmus | index/loop
*content.fm
semua di atas bisa diakhiri * (kecuali yg diakhiri index/loop) 
    utk edit, contoh ../run>*@d/1stop.fmus*
../run>*@satff/flask
    berarti coba jalankan flask.fmus di @satff
    utk jalankan coordinator:
    ../run>@satff/flask
    (tanpa *)
../run>					run coordinator
@satff/flask
    input csvcode utk buat flask
@satff/flask|csvcode
    buat flask dg given csvcode
--#

--% ../hope><something>
hope>perintah|harap|kirim|harap|kirim
../hope>scp2|.*password:|usef

from .crunner import harap(request)
--#

--% ../fmb><something>, fmus browser
from .fmusbrowser import fmusbrowser
fmusbrowser(dirpath)
browse dirpath, execute fmus sampai user tekan empty/enter.
--#

--% ../gz)<something>
--#

--% ../bz)<something>
--#

--% ../zip)<something>
compress
    /gz)input>output
    /gz)input>

    /bz)input>output
    /bz)input>

uncompress
    uncompress, bisa juga terima ext yg mau/perlu diremove

    /gz)output<input
    /gz)output<input,ext to remove
    /gz)<input,ext to remove

    /bz)fileuncompress<filecompressed
    /bz)output<input,ext to remove
    /bz)<input,ext to remove

    /zip)<python.zip*
        extract
    /zip)<python.zip*
        test
--#

--% ../T)<something>
from app.concurrentutils import nantisystem
delayed launch...in 5 seconds...

u -e"/T)5|cmd /k start"
../T)5|python -m webbrowser -t https://youtube.com/
--#

--% ../l)<something>
from .launcher import launcher
l)alamat
ini launch chrome:
../l)google.com
--#

--% ../aws)<something>
/aws)gw
/aws)ath
/aws)cf
/aws)cw
/aws)ddb
/aws)eb
    versi aws eb cli
/aws)ebs
    versi boto3
    /aws)ebs/list
    /aws)ebs/list/my-env
/aws)ec2
/aws)ecs
/aws)eks
/aws)ev
    eventbridge
/aws)glue
/aws)iam
/aws)k
    kinesis
/aws)kafka
    /aws)kafka/list
    /aws)kafka/detail/clusterarn
    /aws)kafka/delete/clusterarn
    /aws)kafka/+/name=...,subnets=sn1|sn2,num=1
        num = jumlah broker per subnet
        jumlah broker nodes = num * len(subnets)
    /aws)kafka/+/name=wieka-1,subnets=subnet-01df53a9ffcbbe21f|subnet-0dd6c6f0b1d6c14f3
    /aws)kafka/public/clusterarn
    /aws)kafka/status/clusterarn
/aws)l
/aws)rds
    /aws)rds/all
    /aws)rds/list (kosong)
/aws)s3
/aws)ses
/aws)sns
/aws)sqs
/aws)sts
/aws)step
/aws)subnet
    /aws)subnet/list
    /aws)subnet/list2
    /aws)subnet/list/vpcid
    /aws)subnet/+/vpcid/cidrsubnet
    /aws)subnet/+/cidrvpc,cidrsubnet
    /aws)subnet/-/subnetid
    /aws)subnet/detail/subnetid
    /aws)subnet/cidr/cidrprefix
/aws)vpc
    /aws)vpc/list
--#

--% ../dot)<something>
[shape=box,color=red,fill=yellow,fontsize=24]
a.b.c[shape=triangle].d.e[shape=oval]
|
b.d[fill=blue,shape=Mdiamond]
|
k.telor[shape=egg],bintang[shape=star],terakhir

from .languages.dotlang import dotlang
no code: dotlang()
@: dotlang(clipboard)
dotlang(something)

# references
label="something"
color=warna keliling
color="#333399"
color="#ff000055"
shape=
    box
    diamond
    Mdiamond
    Mrecord
    Msquare
    octagon
    oval
    polygon,side=6
    polygon,sides=4,skew=.5 = jajaran genjang
    polygon,sides=4,distortion=.5 = funnel
    invtriangle
    triangle
fontcolor=Red,red,darkblue,green,blue,yellow,dodgerblue,colar4,crimson
peripheries=4
fontsize=24
style=filled, fillcolor=green
style=dashed
style=striped
    fillcolor="red:green:blue"
style=wedged
penwidth=3
--#

--% ../img)<something>
<canvas[w=1000,h=800,color=red](
    <img[x=100,y=500,w=.25,h=.25,rotateccw=45,grayscale=50,alpha=80,src=rect,color=yellow]
    <img[x=10,y=150,w=500,h=600,src=https://media.gettyimages.com/photos/bella-thorne-attends-the-los-angeles-premiere-midnight-sun-at-on-picture-id932666434?s=2048x2048]
    <text[x=10,y=250,sz=14,color=blue]|hello mama mia di tinggi 250
    <text[x=10,y=500,sz=14,color=green]|ini di tinggi 500
)

from .languages.imagelang import imagelang
no code: imagelang()
@: imagelang(clipboard)
imagelang(something)
--#

--% ../chart)<something>
<canvas[cols=5](
    <piechart[x=A/B/C/D/E,y=70/40/90/20/50]
    <barchart[x=1/2/3/4/5,y=10/20/30/40/50]
    <linechart[x=1/2/3/4/5,y=10/20/30/40/50]
    <donutchart[x=A/B/C/D/E,y=70/40/90/20/50]
    <map
)

from .languages.chartlang import chartlang
no code: chartlang()
@: chartlang(clipboard)
chartlang(something)
--#

--% ../file><something>
lihat quicklang...quickfile...
--#

--% else: blitz...
b)py/fa1.fmus

app/quick/blitz/ a,cpp,do,go,goog,....rwe,tdd,ts
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
if language in language_to_handler:
    RootNode = get_rootnode(csvcode)
    run_fmus_from_coordinator(language_to_handler[language], [RootNode, fmus_filename])
--#
