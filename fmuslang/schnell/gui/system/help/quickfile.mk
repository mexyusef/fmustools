
--% touch, write
/file>touch|filepath

/file>content/isi untuk filepath|filepath           ini both content = replace isi file
/file>CONTENT/fileentry=barisentry|filepath         ini both content = replace isi file

--#

--% join lines
join lines:
/file>j/nobaris|filepath                            join lines at nobaris with next
/file>j/nobaris/howmanylines|filepath               join lines at nobaris + next howmanylines
/file>J/search_in_lines|filepath                    join lines at "line containing search_in_lines"
/file>J/search_in_lines/howmanylines|filepath

--#

--% comment

comment by baris expression or pattern search
/file>c/nobaris_expression/bentuk_komen|filepath    /file>c/10-15/# |filepath
/file>C/search_in_lines/bentuk_komen|filepath       spt c tapi berbasis pola dalam baris
/file>C/search_in_lines/bentuk_komen|filepath       spt C tapi pola = ^\s+pola

--#

--% uncomment

uncomment by pattern search
/file>U/pola-cari/komen-to-remove/5|filepath        hapus 5 baris mulai dari baris berisi komen-to-remove\s*pola-cari
  /file>U/CONCURRENT_REQUESTS_PER_DOMAIN/# /2|coba.cfg

remove prefix
/file>^-/regex-expr|target.txt                      remove_prefix_by_regex utk semua baris pada target.txt, bisa utk uncomment

--#

--% insert

insert after by pattern search
/file>ia/search_in_lines/content_to_insert|filepath     insert-after
/file>IA/search_in_lines/fileentry=barisentry|filepath

insert before by pattern search
/file>ib/search_in_lines/content_to_insert|filepath     insert-before
/file>IB/search_in_lines/fileentry=barisentry|filepath

/file>IA>/search_in_lines/fileentry=barisentry/s_or_t/num_tab/space_size|filepath insert-after+tabify
/file>IB>/search_in_lines/fileentry=barisentry/s_or_t/num_tab/space_size|filepath insert-before+tabify

insert+tabify by string
/file>i>/3/content to insert/t|settings.py        insert at line 3, lalu tabify dg tab
/file>i>/3/content to insert/t/2|settings.py
/file>i>/3/content to insert/s|settings.py
/file>i>/3/content to insert/s/3|settings.py
/file>i>/3/content to insert/s/3/2|settings.py
/file>i>/3/content to inserti/s/3/4|settings.py

insert+tabify by file
/file>I>/3/filepath=barisentry/t|settings.py
/file>I>/3/filepath=barisentry/t/2|settings.py
/file>I>/3/filepath=barisentry/s|settings.py
/file>I>/3/filepath=barisentry/s/3|settings.py
/file>I>/3/filepath=barisentry/s/3/2|settings.py
/file>I>/3/filepath=barisentry/s/3/4|settings.py

--#

--% append
append string at line no
/file>a/nobaris/content_to_append|filepath              append content at nobaris
--#

--% remove string
remove substring (bs utk remove suffix)
/file>#-/line-expr/regex-expr|target.txt            hapus substring regex pada baris2 line-expr
  ini bs dipake utk removesuffix tiap baris
    u -e"/file>#-/69-110/,$|pyqt5_references.mk"

insert at lineno
/file>i/nobaris/content_to_insert|filepath              /file>i/-1/ini di akhir file|filepath
/file>I/nobaris/fileentry=barisentry|filepath
--#

--% remove line
remove lines
/file>-/34|target.txt                 hapus 1 baris pada line no 34, remove_lines_by_no
/file>-/34/4|target.txt               hapus baris no 34 sebanyak 4
/file>--/table_name|target.txt        hapus 1 baris berisi table_name
/file>--/table_name/3|target.txt      hapus 3 baris dari baris berisi table_name + 2
--#

--% replace string
replace string
/file>repl/yang_mau_dihapus/nilai_pengganti|filetarget
/file>REPL/yang_mau_dihapus/filepath=barisentry|filetarget
--#

--% replace line
replace line
/file>repline/nobaris/ini baris pengganti|filepath
/file>REPLINE/filepath=entry/ini baris pengganti|filepath

replace from, until, between
/file>replF/text-baris-cari/text-content|file-target         replace content dari temukan pola sampai akhir
/file>replU/text-baris-cari/text-content|file-target         replace content dari awal sampai ditemukan pola
/file>replB/cari-awal/cari-akhir/text-content|file-target    replace between awal dan akhir
/file>replinefrom
/file>replinebetween
--#

--% indent dan dedent
indent
/file>>lineexpr/t|filepath            indent with tab, sebanyak 1
/file>>lineexpr/t/1|filepath
/file>>lineexpr/s|filepath
/file>>lineexpr/s/3|filepath
/file>>lineexpr/s/3/4|filepath        indent with space, sebanyak 3, space size=4

indent
/file>^>pattern-cari/t|filepath       indent dg pattern, bukan line expression
/file>^>pattern-cari/t/1|filepath
/file>^>pattern-cari/s|filepath
/file>^>pattern-cari/s/3|filepath
/file>^>pattern-cari/s/3/4|filepath

dedent
/file><lineexpr/t|filepath            dedent with tab, sebanyak 1
/file><lineexpr/t/1|filepath
/file><lineexpr/s|filepath
/file><lineexpr/s/3|filepath
/file><lineexpr/s/3/4|filepath        dedent with space, sebanyak 3, space size=4

dedent
/file>^<pattern-cari/t|filepath       dedent dg pattern, bukan line expression
/file>^<pattern-cari/t/1|filepath
/file>^<pattern-cari/s|filepath
/file>^<pattern-cari/s/3|filepath
/file>^<pattern-cari/s/3/4|filepath
--#

--% sort line
/file>@baris-awal,baris-akhir   sort_lines(filepath, start, end), bisa juga /file>@, utk 0 sampai -1 (akhir file)
--#

--% tab to space, space to tab
/file>ts|filepath         tab to space
/file>ts/4|filepath       space size = 4
/file>st|filepath         space to tab
/file>st/4|filepath       space size = 4
--#

--% app.quick.bahasa
app.quick.bahasa:	u -e/i/
app.quick.bahasa:	u -e/ls/
app.quick.bahasa:	u -e/Atxt/...
app.quick.bahasa:	u -e/Rch/...
app.quick.bahasa:	u -e/Rgl/...
app.quick.bahasa:	u -e/R/...
app.quick.bahasa:	u -e/DJ/...
app.quick.bahasa:	u -e/N/...
app.quick.bahasa: u -e/ST/...
app.quick.bahasa: u -e/XT/...
app.quick.bahasa: u -e/A/...
app.quick.bahasa: u -e/DO/...
app.quick.bahasa: u -e/BE/...
app.quick.bahasa: u -e/FE/...
app.quick.bahasa: u -e/K/...
app.quick.bahasa: u -e/algo/...
app.quick.bahasa: u -e/tdd/...
app.quick.bahasa: u -e/PR/...
app.quick.bahasa: u -e/crajs/1
app.quick.bahasa: u -e/crats/1
app.quick.bahasa: u -e/aws/1
app.quick.bahasa: u -e/books/1
app.quick.bahasa: u -e/gomi/1
app.quick.bahasa: u -e/hasura/1
app.quick.bahasa: u -e/html/1
app.quick.bahasa: u -e/H/1
app.quick.bahasa: u -e/jfx/1
app.quick.bahasa: u -e/netlify/1
app.quick.bahasa: u -e/prisma/1
app.quick.bahasa: u -e/rr/1
app.quick.bahasa: u -e/tddjava/1
app.quick.bahasa: u -e/tddjs/1
app.quick.bahasa: u -e/tddpy/1
app.quick.bahasa: u -e/twrds/1
app.quick.bahasa: u -e/w3/1
app.quick.bahasa: u -e/webext/1
app.quick.bahasa: u -e/wp53/1
app.quick.bahasa: u -e/wp54/1
app.quick.bahasa: u -e/wp5ts/1
--#

--% file manipulation
butuh apalagi?
--#
