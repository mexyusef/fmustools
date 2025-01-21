
*****
qt.he
*****

kita bikin dokumentasi

fullstack

system
    bikin sistem dengan cepat

handbook

juga riset:
mengenai graphqp, websocket, webrtc.

== memahami searcher

searcher            plugin              worker
Window
    (window)
LineEdit
ListWidget
    (popup)

popup punya signal activated
jk popup/done() dipanggil maka activated di emit.

window hubungkan activated dengan own select()
own select() akan panggil plugin select().

= Q: krn "kehidupan" mulai dg user milih item di popup
kapan popup itu sendiri muncul?

== hubungan window ke plugin ke worker
window panggil plugin lit(), plugin lit() panggil worker do()
(dg berikan: cmd + arg/query)

window panggil plugin lit() dg berikan arg/query, cmd digunakan olehnya utk memilih plugin yg mana.
plugin stlh nerima query, manggil worker.do(), yg membuat model list/content

= worker
utk make_word, etc
Make terima: impl, finished...
impl adlh: ...
    dari: make=lambda: WindowModel(self.data_callback_for_select(query, python_files)[:upper_bound])
    adlh fungsi yg mengembalikan/membungkus model dg contentnya...
finished adlh: try_popup...

jadi terlihat sudah: gimana kita bentuk model, abis itu keluarkan popup...
ini adlh "kehidupan" pertama
"kehidupan" kedua adlh wkt user milih item, dst.

jd misal mau bikin plugin yg self-sufficient...gak perlu ini itu (gak perlu worker, task, etc)
kita gak perlu "try_popup"/finished...
cukup terima arg/query = ff, fl, dst.
    lalu panggil replservice.process(...)
    err:
    redis_subscribe ke 'response_kanal' : "replservice_response",
        jk terima data, maka tampilkan di console lalu "note"/viewer
        wait up...
        subscribe ini bisa dilakukan di searcher...
        jd note akan keluar wkt terima...
    ini mestinya jalan di QThread...

    redis_publish   ke 'request_kanal' : "replservice_request",
    sementara kbrepl hrs dengar di kanal 'request_kanal' : "replservice_request",

lalu hasilnya gimana? kita keluarkan "note"/viewer.
