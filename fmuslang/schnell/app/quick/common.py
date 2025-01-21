from schnell.app.dirutils import joiner, pemisah_direktori
from schnell.app.utils import platform, env_get


rootdir = env_get('ULIBPY_ROOTDIR')
schnelldir = env_get('ULIBPY_BASEDIR')
pohon = 'tree'
filepath = 'index-input.mk'
barisentry = 'index/fmus'


program_config = {
}


path_mapping = {
    '@c'        : 'coords',
    '@d'        : 'codes',
    '@D'        : 'data',
    '@DB'       : 'database',
    '@s'        : 'schnell',
    '@sa'       : joiner('schnell', 'app'),
    '@saq'      : joiner('schnell', 'app', 'quick'),
    '@saqb'     : joiner('schnell', 'app', 'quick', 'blitz'),
    '@saqbdo'   : joiner('schnell', 'app', 'quick', 'blitz', 'do'),
    '@saqbdj'   : joiner('schnell', 'app', 'quick', 'blitz', 'dj'),
    '@saqbpy'   : joiner('schnell', 'app', 'quick', 'blitz', 'py'),
    '@saqbr'    : joiner('schnell', 'app', 'quick', 'blitz', 'r'),
    '@saqbts'   : joiner('schnell', 'app', 'quick', 'blitz', 'ts'),
    '@saqd'     : joiner('schnell', 'app', 'quick', 'dahsyat'),
    '@sat'      : joiner('schnell', 'app', 'transpiler'),
    '@satf'     : joiner('schnell', 'app', 'transpiler', 'frontend'),
    '@satff'    : joiner('schnell', 'app', 'transpiler', 'frontend', 'fslang'),
    '@satfff'   : joiner('schnell', 'app', 'transpiler', 'frontend', 'fslang', 'fullstack'),
    '@satffm'   : joiner('schnell', 'app', 'transpiler', 'frontend', 'fslang', 'misc'),
    '@satffu'   : joiner('schnell', 'app', 'transpiler', 'frontend', 'fslang', 'utils'),
    '@satffz'   : joiner('schnell', 'app', 'transpiler', 'frontend', 'fslang', 'z'),
    '@satffzq'  : joiner('schnell', 'app', 'transpiler', 'frontend', 'fslang', 'z', 'quick'),
    '@sd'       : joiner('schnell', 'db'),
    '@sdb'      : joiner('schnell', 'db', 'bantuan'),
    '@l'        : joiner('schnell', 'langs'),
}


if platform() in ['win32', 'windows']:
    pohon = 'wsl tree'


def map_folder(relative_folder):
    """
    path bs berisi komponen @... di atas
    kita expand dan kembalikan bentuk terexpanded
    """
    pemisah_input = pemisah_direktori()

    if pemisah_direktori() not in relative_folder:
        if '\\' not in relative_folder and '/' in relative_folder:
            pemisah_input = '/'
        elif '/' not in relative_folder and '\\' in relative_folder:
            pemisah_input = '\\'

    pemisah_direktori().join([
        path_mapping.get(item, item) for item in relative_folder.split(pemisah_input)
    ])


def folder_expand(relative_folder, force_pemisah='', prefix_with_rootdir=False):
    """
    reqs: terima input dan hasilkan output hanya utk di dalam git folder "sidoarjo"
    misal
    @satff\moleculer
    maka hrs jadi
    schnell\app\transpiler\frontend\fslang\moleculer
    ini gak ditambah dg basefolder
    """
    if force_pemisah:
        pemisah_input = force_pemisah
        hasil = pemisah_input.join([
            path_mapping.get(item, item) for item in relative_folder.split(pemisah_input)
        ])
    else:
        pemisah_input = pemisah_direktori()
        if pemisah_direktori() not in relative_folder:
            # jk system default separator gak ada dari user input relative_folder
            # berarti user input specify separator yg berbeda
            # kita perlukan utk bisa split path-entry dg benar
            # tapi hasil akhirnya dipaksa sesuai platform
            if '\\' not in relative_folder and '/' in relative_folder:
                pemisah_input = '/'
            elif '/' not in relative_folder and '\\' in relative_folder:
                pemisah_input = '\\'

        hasil = pemisah_direktori().join([
            path_mapping.get(item, item) for item in relative_folder.split(pemisah_input)
        ])

    if prefix_with_rootdir:
        if not hasil.startswith(rootdir):
            hasil = joiner(rootdir, hasil)

    return hasil


file_instruction = """
    touch new file
        /file>touch|filename.txt
    write/replace content from string
        /file>content/content|file.txt
    write/replace content from fmuscontent
        /file>CONTENT/filepath=barisentry|file.txt
    join lines from line#
        /file>j/17|__PWD/contoh.txt
            join baris no 17 sebanyak 1 (dg next line)
        /file>j/17/5|__PWD/contoh.txt
            join baris no 17 sebanyak 5 baris
        /file>j/72/6|__PWD/s_users.sql
            join_lines c:\work/s_users.sql OK
    join lines from line containing pattern
        /file>J/find me|filepath
        /file>J/find me/2|filepath
                        ^ how many lines
    commenting line#
        /file>c/10/-- |file.txt
        /file>c/2,3/'-- '|__PWD/contoh.txt"
        /file>c/1,4-6/'-- '|__PWD/contoh.txt"
                ^^^^^ line expression
    commenting lines started with prefix - C tidak terima leading space
        /file>C/TEXT/'-- '|__PWD/s_users.sql
        /file>C/SET/'-- '|__PWD/s_users.sql
            comment_file_by_prefix c:\work/s_users.sql OK
        /file>C/ALTER TABLE/'-- '|__PWD/s_users.sql
            comment_file_by_prefix c:\work/s_users.sql OK
        /file>C/ALTER SEQUENCE/'-- '|__PWD/s_users.sql
            comment_file_by_prefix c:\work/s_users.sql OK
        /file>C/SELECT /'-- '|__PWD/s_users.sql
            comment_file_by_prefix c:\work/s_users.sql OK
    commenting lines started with \s*prefix - C2 bisa leading space
        /file>C2/ADD CONSTRAINT /'-- '|__PWD/s_users.sql
            comment_file_by_prefix c:\work/s_users.sql OK

    insert (at) string as line at line#
        /file>i/3/DISALLOW HOST|settings.py
    insert (at) string as line from fmuscontent
        /file>I/3/filepath=barisentry|settings.py
    insert (after) string after line containing pattern
        /file>ia/baris cari/isi tulisan|settings.py
    insert (after) fmuscontent after line containing pattern
        /file>IA/baris cari/filepath=barisentry|settings.py
    insert (before) string before line containing pattern
        /file>ib/baris cari/isi tulisan|settings.py
    insert (before) fmuscontent before line containing pattern        
        /file>IB/baris cari/filepath=barisentry|settings.py

    append string at line#
        /file>a/10/isi komentar|file.txt
            10 adlh line expression
    replace old string to new string in file
        /file>repl/yang_mau_dihapus/nilai_pengganti|filetarget
    replace old string to fmuscontent in file
        /file>REPL/yang_mau_dihapus/filepath=barisentry|filetarget
    replace line at line# with string
        /file>repline/3/ini baris pengganti
    replace line at line# with fmuscontent
        /file>REPLINE/filepath=entry/ini baris pengganti

    replace line from... (not yet)
        def replace_from(filepath, baris_cari, content_to_insert):
        /file>replF/text-baris-cari/text-content
    replace line until... (not yet)
        def replace_until(filepath, baris_cari, content_to_insert):
        /file>replU/text-baris-cari/text-content
    replace line between... (not yet)
        def replace_between(filepath, baris_cari_start, baris_cari_end, content_to_insert):
        /file>replB/text-baris-cari-start/text-baris-cari-end/text-content
    remove prefix by regex (not yet)
        def remove_prefix_by_regex(filepath, regex_expression):
        suka lihat 01. pertama, next line: 02. kedua, pengen hapus "^(\d+\.\s*)" pada tiap baris
        /file>^-/ekspresi-regex
    sort lines between
        def sort_lines(filepath, start, end):
        /file>@/start,end
        /file>@/, (default 0 sampai -1)

    rx operation (not really used)
        di-regex kan...tiap baris...tapi gak disimpan, hanya utk ngeprint
        /file>re/fileregex|__PWD/filetarget
        /file>re/fileregex|filetarget
        disini kita bikin versi 'us' file, jadi gak pake entry
    remove line(s) at line# dg -
        /file>-/SELECT /3|__PWD/s_users.sql"
            -/<pola prefix>/<jumlah hapus>|<target "
    remove line(s) containing pattern in file dg --
        u -e"/file>--/table_name|target.txt"
            remove line ybs
        u -e"/file>--/table_name/2|target.txt"
            remove 2 lines (plus line berikutnya) stlh ketemu line berisi table_name
    indent lineexpr pada filepath with tab or space
        /file>>lineexpr,t|filepath
        /file>>lineexpr,t,1|filepath
            indent pada line nos = lineexpr, gunakan tab sebanyak 1
        /file>>lineexpr,s|filepath
            indent pada line nos = lineexpr, gunakan space sebanyak 1 (default) dg space size = 2 (default)
        /file>>lineexpr,s,1,4|filepath
            indent pada line nos = lineexpr, gunakan space sebanyak 1 dg space size = 4
    dedent lineexpr pada filepath with tab or space
        /file><lineexpr,t,1|filepath
        /file><lineexpr,s,1,4|filepath
    indent searchpattern yg ketemu pada filepath with tab or space
        /file>^>pattern-cari/t|filepath
        /file>^>pattern-cari/t/1|filepath
        /file>^>pattern-cari/s|filepath
        /file>^>pattern-cari/s/3|filepath
        /file>^>pattern-cari/s/3/4|filepath
            3 space dg space size = 4
        /file>^>root "tasks#index"/s/1/2|routes.rb
              ^>/ <- jangan / sebelum cari...
    dedent searchpattern yg ketemu pada filepath with tab or space
        /file>^<pattern-cari/t|filepath
        /file>^<pattern-cari/t/1|filepath
        /file>^<pattern-cari/s|filepath
        /file>^<pattern-cari/s/3|filepath
        /file>^<pattern-cari/s/3/4|filepath

    insert fmuscontent to line# and tabify with tab or space (I>)
        /file>I>/3/filepath=barisentry/t|settings.py
            tabify dg 1 tab
        /file>I>/3/filepath=barisentry/t/2|settings.py
            tabify dg 2 tab
        /file>I>/3/filepath=barisentry/s|settings.py
        /file>I>/3/filepath=barisentry/s/3|settings.py
            tabify dg 3 space
        /file>I>/3/filepath=barisentry/s/3/4|settings.py
            tabify dg 3 space berukuran 4
    insert text to line# and tabify with tab or space (i>)
        spt I> tapi alih2 filepath=barisentry, langsung content_to_insert
        # misal dari # root "articles#index"
        # ini butuh insert before dan insert after!
    tab to space
        /file>ts|filepath
        /file>ts/4|filepath
    space to tab
        /file>st|filepath
        /file>st/4|filepath
"""


scraper_instruction = """
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
"""


search_instruction = """
    basefolder bisa @s, @c, @d, @satff, __PWD, dst
    stlh /s> bisa 
        text langsung (grep), 
        ~ (walkdir+pattern-antipattern) dulu 
        dan # (find) dulu.

    search content/text dalam tiap file dalam folder menggunakan linux grep command
    u -e"/s>package main|__PWD"

    search menggunakan pattern /s>~ dg 3 varian ~file, file/ dan file
        masing2 utk file saja, dir saja, file+dir
    u -e"/s>~~main.go|__PWD"
    u -e"/s>~src/|__PWD"
    u -e"/s>~main|__PWD"

    search menggunakan linux find command, setara -name "*main*"
    u -e"/s>#main|__PWD"
"""


launcher_instruction = """
    l)alamat
    l)f/alamat
        new tab
    l)f+/alamat
        new window
    l)c/alamat
        chrome
    l)o/alamat
        opera
harus bisa: google search, google translate, search youtube...
"""


cloudia_instruction = """
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
"""


compressor_instruction = """
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
"""
