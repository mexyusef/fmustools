--% window
# TODO
- DONE key utk keluar (keysequence)
- DONE background color, background image
- DONE add context menu: about qt dan quit
- add tray icon support
- DONE as qmainwindow + menu, toolbar, statusbar

<w[main,title=judul2an,w=800,h=600,trans,top](
    <l[type=v,name=main_layout](
        ...
    )
)
qmainwindow = ada background
top = stay on top
dark = dark theme
trans = translucent

<w[main,qmainwindow,title=kuda,top,dark,trans]
--#

--% ball
--#

--% button
--#

--% cal
--#

--% casio
--#

--% chartarea, chartbar, chartbarhorizontal, chartbarpercent, chartbarstack, chartcpu, chartcustomaxis, chartline, chartlinestack, chartpie, chartscatter, chartspline, chartsplinedynamic
../G)
<w[main,title=myapp] ( 
    <l[type=v,name=mainlayout] (
        <split(
            <page(<chartsplinedynamic<chartscatter<chartspline)
            <page(<chartline<chartarea<chartpie)
            <page(<chartcpu<chartlinestack<chartbarstack)
            <page(<chartbar<chartbarhorizontal<chartbarpercent)
            <page(<chartcustomaxis)
        )
    )
)
--#

--% check
--#

--% clock
--#

--% colorinput
<w[main,name=kcharles klausmayer](
<l[type=v,name=main_layout](
<colorinput[label=button utk colorinput]
)
)
--#

--% combo
--#

--% date
<w[main,title=judul2an](
    <l[type=v,name=main_layout](
        <date
    )
)
--#

--% datetime
<w[main,title=judul2an](
    <l[type=v,name=main_layout](
        <datetime
    )
)
--#

--% devto
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](
        <devto[label=devto]
    ) 
)
--#

--% dial
--#

--% draw
lumayan bisa painting dg ubah color dan thickness dari pen
pengennya bisa lanjut ke bikin diagram.
--#

--% edit
--#

--% editmulti
--#

--% editor_standard
--#

--% fileinput
--#

--% filetree
--#

--% filetree2
--#

--% flow
--#

--% font
--#

--% fontinput
--#

--% form
--#

--% frame
<w[main,title=kuda](
    <l[type=v,name=main](
        <frame(
            <b[label=satu]
            <b[label=dua]
        )
    )
)
<w[main,qmainwindow,title=kuda,top,dark](
    <l[type=v,name=main](
        <group[label=balada group bukan frame](
            <b[label=tiga]
            <b[label=empat]
        )
        <frame(
            <label[label=ini di dalam group]
            <b[label=satu]
            <b[label=dua]
            <label[label=ini juga di dalam group]
        )
    )
)
<w[main,title=kuda](
    <l[type=v,name=main](
        <group(
            <b[label=satu]
            <b[label=dua]
        )
    )
)
--#

--% group
masih bugs utk:
<w[main,title=kuda](
<l[type=v,name=main](
    <group(
        <split(
            <page(<b[label=satu])
            <page(<b[label=dua])
        )
    )
)
)

sudah jalan utk:

<w[main,title=kuda](
<l[type=v,name=main](
    <group[label=ini adalah group, sayangku](
        <b[label=satu]
        <b[label=dua]
    )
)
)
--#

--% input
--#

--% label
--#

--% layout
--#

--% lcd
--#

--% list
--#

--% listfold
<listfold(
    <page[label=lihat analog](<clock)
    <page[label=lihat digital](<casio)
)
--#


--% lr, logrocket
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](
        <lr[label=mylogrocket]
    ) 
)
--#

--% medium
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](
        <med[label=medium]
    ) 
)
--#

--% message
--#

--% note
--#

--% notification_anim
--#

--% notification_button
--#

--% notification_clock
--#

--% notification_content
<w[main,name=kcharles klausmayer](
<l[type=v,name=main_layout](
<notification_content[label=label utk pushbutton,w=0.2,h=0.5](
    <label[label=kuda lumping luh]
)
)
)

<w[main,name=kcharles klausmayer](
<l[type=v,name=main_layout](
<notification_content[label=label utk pushbutton,w=0.5,h=0.5](
    <label[label=kuda lumping luh]
)
)
)
--#

--% pageswitch
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](      
        <pageswitch( 
            <page[label=plotter](<plot_rt)  
            <page[label=clock](<plot_plotter) 
            <page(<plot_static)
        )
    )
)
--#

--% pdf
--#

--% plain
--#


--% plot_plotter
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](      
        <split( 
            <page[label=realtime](<plot_rt)  
            <page[label=clickable](<plot_plotter) 
            <page[label=static](<plot_static)
        )          
    )
)
--#

--% plot_race
--#

--% plot_rt
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](      
        <split( 
            <page[label=realtime](<plot_rt)  
            <page[label=clickable](<plot_plotter) 
            <page[label=static](<plot_static)
        )          
    )
)
--#

--% plot_static
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](      
        <split( 
            <page[label=realtime](<plot_rt)  
            <page[label=clickable](<plot_plotter) 
            <page[label=static](<plot_static)
        )          
    )
)
--#

--% progress
--#

--% radio
--#

--% radios
--#

--% scrollbar
--#

--% slider
--#

--% spin
--#

--% spinfloat
--#

--% split
<split[](
    <page
)
--#

--% stacked
<stacked[](
    page[label=sebuah tulisan, control=control]
)
--#

--% so, stackoverflow
../G)
<w[main,title=gila] ( 
    <l[type=h,name=tool_layout](
        <so[label=stackorama]
    )
)
--#

--% tab
<tab[](
    <page[label=sebuah tulisan]
)
--#

--% table
--#

--% tableview
--#

--% tetris
--#

--% time
<w[main,title=judul2an](
    <l[type=v,name=main_layout](
        <time
    )
)
--#

--% windowbrowser, browser
<w[main,title=judul2an](
    <l[type=v,name=main_layout](
        <windowbrowser[label=klik untuk buka browser]
    )
)
--#
