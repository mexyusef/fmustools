guilang_items = [
    'window/wnd/w/W',
    'ball',
    'button/btn/b/B',
    'cal',
    'chartarea',
    'chartbar',
    'chartbarhorizontal',
    'chartbarpercent',
    'chartbarstack',
    'chartlinestack',
    'chartcpu',
    'chartcustomaxis',
    'chartline',
    'chartpie',
    'chartscatter',
    'chartspline',
    'chartsplinedynamic',
    'casio',
    'check',
    'clock',
    'colorinput',
    'combo',
    'combofont',
    'date',
    'datetime',
    'dial',
    'draw',
    'edit',
    'editor_standard',
    'editmulti',
    'flow',
    'form',
    'font',
    'fontinput',
    'fileinput',
    'filetree',
    'filetree2',
    'frame/frm',
    'group/grp',
    'input/inp/i/I',
    'label/lbl/l', # l label
    'layout/lyt/lay/L', # L layout
    'lcd',
    'list',
    'listfold',
    'message/msg/m/M',
    'note',
    'notification_button',
    'notification_anim',
    'notification_clock',
    'notification_content',
    'page',
    'pageswitch',
    'pdf',
    'plain',
    'plot_rt',
    'plot_plotter',
    'plot_static',
    'plot_race',
    'progress',
    'radio',
    'radios',
    'row',
    'scrollbar',
    'slider',
    'split',
    'spin',
    'spinfloat',
    'stacked',
    'stackoverflow/so','medium/med','logrocket/lr','devto',
    'tab',
    'table',
    'tableview',
    'tetris',
    'time',
    'windowbrowser/browser',
]

fmdata = {
    'window/wnd/w/W': [
        {'label': 'main,title', 'content': """<w[main,title=judul2an](
    <L[type=v,name=main_layout](



    )
)
"""},
        {'label': 'main,title,qmainwindow', 'content': """<w[main,title=judul2an,qmainwindow](
    <L[type=v,name=main_layout](



    )
)
"""},
        {'label': 'main,title,w,h', 'content': """<w[main,title=judul2an,w=1200,h=800](
    <L[type=v,name=main_layout](



    )
)
"""},
        {'label': 'main,title,w,h,qmainwindow', 'content': """<w[main,title=judul2an,w=1200,h=800,qmainwindow](
    <L[type=v,name=main_layout](



    )
)
"""},
        {'label': 'lengkap', 'content': """<w[main,title=judul2an,w=1200,h=800,qmainwindow,top,dark,trans](
    <L[type=v,name=main_layout](



    )
)
"""},
        {'label': 'lengkap-top,trans', 'content': """<w[main,title=judul2an,w=1200,h=800,qmainwindow,dark](
    <L[type=v,name=main_layout](



    )
)
"""}
],
    'ball': """<ball""",
    'button/btn/b/B': """<b[label=tulisan]""",
    'cal': """<cal""",
    'chartarea': """<chartarea""",
    'chartbar': """<chartbar""",
    'chartbarhorizontal': """<chartbarhorizontal""",
    'chartbarpercent': """<chartbarpercent""",
    'chartbarstack': """<chartbarstack""",
    'chartlinestack': """<chartlinestack""",
    'chartcpu': """<chartcpu""",
    'chartcustomaxis': """<chartcustomaxis""",
    'chartline': """<chartline""",
    'chartpie': """<chartpie""",
    'chartscatter': """<chartscatter""",
    'chartspline': """<chartspline""",
    'chartsplinedynamic': """<chartsplinedynamic""",
    'clock': """<clock""",
    'casio': """<casio""",
    'check': """<check[label=Checkmate]""",
    'colorinput': """<colorinput""",
    'combo': [{'label':"bare", 'content':"""<combo"""}, {'label':"items", 'content':"""<combo[items=item 1/item 2/item 3]"""},],
    'combofont': """<combofont""",
    'date': """<date""",
    'datetime': """<datetime""",
    'devto': """<devto""",
    'dial': """<dial""",
    'draw': """<draw""",
    'edit': """<edit""",
    'editor_standard': """<editor_standard""",
    'editmulti': """<editmulti""",
    'flow': """<flow""",
    'form': """<form[label=myform](
    <row[label=sebuah tulisan, control=control]
    <row[label=sebuah tulisan 2, control=control]
    <row[label=sebuah tulisan 3, control=control]
)""",
    'font': """<font""",
    'fontinput': """<fontinput[label=Klik untuk buka]""",
    'fileinput': """<fileinput[label=Klik untuk buka]""",
    'filetree': """<filetree""",
    'filetree2': """<filetree2""",
    'frame/frm': """<frame(
    <b[label=satu]
    <b[label=dua]
)""",
    'group/grp': """<group[label=nama groupbox](
    <split(
        <page(<b[label=satu])
        <page(<b[label=dua])
    )
)""",
    'input/inp/i/I': """<i[label=Klik untuk buka]""",
    'label/lbl/l': """<l[label=tulisan]""",
    'layout/lyt/lay/L': """<L[type=v,name=mylayout](



)""", # L layout, l label
    'lcd': """<lcd""",
    'list': """<list""",
    'listfold': """<listfold(
    <page[label=lihat analog](<clock)
    <page[label=lihat digital](<casio)
)
""",
    'logrocket/lr': """<lr[label=mylogrocket]""",
    'medium/med': """<med[label=medium]""",
    'message/msg/m/M': """<message[label=mymessage]""",
    'note': """<note""",
    'notification_button': """<notification_button[label=notification_button]""",
    'notification_anim': """<notification_anim[label=notification_anim]""",
    'notification_clock': """<notification_clock[label=notification_clock]""",
    'notification_content': """<notification_content[label=label utk pushbutton,w=0.5,h=0.5](
    <label[label=kuda lumping luh]
)""",
    'page': """<page""",
    'pageswitch': """<pageswitch(
    <page[label=plotter](<plot_rt)  
    <page[label=clock](<plot_plotter) 
    <page(<plot_static)
)""",
    'pdf': """<pdf""",
    'plain': """<plain[label=initial content]""",
    
    'plot_plotter': """<plot_plotter""",
    'plot_race': """<plot_race""",
    'plot_rt': """<plot_rt""",
    'plot_static': """<plot_static""",
    
    'progress': """<progress""",
    'radio': """<radio""",
    'radios': """<radios(
    <b[label=radio 1]
    <b[label=radio 2]
    <b[label=radio 3]
)""",
    'row': """<row""",
    'scrollbar': """<scrollbar""",
    'slider': """<slider""",
    'split': """<split[type=v](
    <page[label=input]()
    <page[label=output]()
    <page[label=helper]()
)""",
    'spin': """<spin""",
    'spinfloat': """<spinfloat""",
    'stacked': """<stacked[label=stackerz](
    <page[label=sebuah tulisan, control=control]
)""",
    'stackoverflow/so': """<so[label=stackorama]""",
    'tab': """<tab[label=Tab1](
    <page[label=sebuah tulisan]
)""",
    'table': """<table""",
    'tableview': """<tableview""",
    'tetris': """<tetris""",
    'time': """<time""",
    'windowbrowser/browser': """<windowbrowser[label=klik untuk buka browser]""",
}