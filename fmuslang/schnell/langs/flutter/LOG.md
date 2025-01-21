Column(padding=edge_insets_symmetric,onTap=Icons,onPressed=FlatButton,children=[Expanded(nama_attribute_asal=edge_insets_only),Container(backgroundColor=edge_insets_all)])
==================== Column(padding=edge_insets_symmetric,onTap=Icons,onPressed=FlatButton,children=[Expanded(nama_attribute_asal=edge_insets_only),Container(backgroundColor=edge_insets_all)]) 

widgets
  widget
    widget_name Column
    widget_content
      attr_widgets
        attr_widget
          attr_name     padding
          widget_or_constant
            const_name  edge_insets_symmetric
        attr_widget
          attr_name     onTap
          widget_or_constant
            const_name  Icons
        attr_widget
          attr_name     onPressed
          widget_or_constant
            const_name  FlatButton
        attr_widget
          attr_name     children
          widget_or_constant
            widgets
              widget_list
                widget
                  widget_name   Expanded
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_name       nama_attribute_asal
                        widget_or_constant
                          const_name    edge_insets_only
                widget
                  widget_name   Container
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_name       backgroundColor
                        widget_or_constant
                          const_name    edge_insets_all



w1(k1=c1,k2=w2,k3=w3,k4=[w4(k1=c3),w5(k3=c3)])
Column(k1=c1,k2=w2,k3=w3,k4=[w4(k1=c3),w5(k3=c3)])
==================== w1(k1=c1,k2=w2,k3=w3,k4=[w4(k1=c3),w5(k3=c3)]) 

widgets
  widget
    widget_1
    widget_content
      attr_widgets
        attr_widget
          attr_1
          widget_or_constant
            constant_1
        attr_widget
          attr_2
          widget_or_constant
            widgets
              widget
                widget_2
        attr_widget
          attr_3
          widget_or_constant
            widgets
              widget
                widget_3
        attr_widget
          attr_4
          widget_or_constant
            widgets
              widget_list
                widget
                  widget_4
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_1
                        widget_or_constant
                          constant_3
                widget
                  widget_5
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_3
                        widget_or_constant
                          constant_3

Column(k1=c1,k2=w2,k3=w3,k4=[Expanded(k1=c3),Container(k3=c3)])
==================== Column(k1=c1,k2=w2,k3=w3,k4=[Expanded(k1=c3),Container(k3=c3)]) 

widgets
  widget
    widget_name Column
    widget_content
      attr_widgets
        attr_widget
          attr_1
          widget_or_constant
            constant_1
        attr_widget
          attr_2
          widget_or_constant
            widgets
              widget
                widget_2
        attr_widget
          attr_3
          widget_or_constant
            widgets
              widget
                widget_3
        attr_widget
          attr_4
          widget_or_constant
            widgets
              widget_list
                widget
                  widget_name   Expanded
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_1
                        widget_or_constant
                          constant_3
                widget
                  widget_name   Container
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_3
                        widget_or_constant
                          constant_3

Column(padding=c1,onTap=w2,onPressed=w3,children=[Expanded(k1=c3),Container(backgroundColor=c3)])
==================== Column(padding=c1,onTap=w2,onPressed=w3,children=[Expanded(k1=c3),Container(backgroundColor=c3)]) 

widgets
  widget
    widget_name Column
    widget_content
      attr_widgets
        attr_widget
          attr_name     padding
          widget_or_constant
            constant_1
        attr_widget
          attr_name     onTap
          widget_or_constant
            widgets
              widget
                widget_2
        attr_widget
          attr_name     onPressed
          widget_or_constant
            widgets
              widget
                widget_3
        attr_widget
          attr_name     children
          widget_or_constant
            widgets
              widget_list
                widget
                  widget_name   Expanded
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_1
                        widget_or_constant
                          constant_3
                widget
                  widget_name   Container
                  widget_content
                    attr_widgets
                      attr_widget
                        attr_name       backgroundColor
                        widget_or_constant
                          constant_3

Column(padding=edge_insets_symmetric,onTap=Icons,onPressed=FlatButton,children=[Expanded(nama_attribute_asal=edge_insets_only),Container(backgroundColor=edge_insets_all)])


MaterialApp(title=anytext,debugShowCheckedModeBanner=F,theme=ThemeData(primaryColor=red),home=HomeScreen)
==================== MaterialApp(title=anytext,debugShowCheckedModeBanner=F,theme=ThemeData(primaryColor=red),home=HomeScreen) 

widgets
  widget
    widget_name MaterialApp
    widget_content
      attr_widgets
        attr_widget
          attr_name     title
          widget_or_constant
            const_name  anytext
        attr_widget
          attr_name     debugShowCheckedModeBanner
          widget_or_constant
            const_name  F
        attr_widget
          attr_name     theme
          widget_or_constant
            widgets
              widget
                widget_name     ThemeData
                widget_content
                  attr_widgets
                    attr_widget
                      attr_name primaryColor
                      widget_or_constant
                        const_name      red
        attr_widget
          attr_name     home
          widget_or_constant
            const_name  HomeScreen

ma(title=anytext,debugShowCheckedModeBanner=scaf,theme=thmd(primaryColor=red),home=HomeScreen)

ma(title=anytext,debugShowCheckedModeBanner=scaf,theme=thmd(primaryColor=/myconst),home=HomeScreen)
==================== ma(title=anytext,debugShowCheckedModeBanner=scaf,theme=thmd(primaryColor=/myconst),home=HomeScreen) 

widgets
  widget
    widget_name ma
    widget_content
      attr_widgets
        attr_widget
          attr_name     title
          widget_or_constant
            widgets
              widget
                widget_name     anytext
        attr_widget
          attr_name     debugShowCheckedModeBanner
          widget_or_constant
            widgets
              widget
                widget_name     scaf
        attr_widget
          attr_name     theme
          widget_or_constant
            widgets
              widget
                widget_name     thmd
                widget_content
                  attr_widgets
                    attr_widget
                      attr_name primaryColor
                      widget_or_constant
                        const_name      myconst
        attr_widget
          attr_name     home
          widget_or_constant
            widgets
              widget
                widget_name     HomeScreen


ma(title=anytext,debugShowCheckedModeBanner=scaf,theme=thmd(primaryColor=/myconst),home=/someconst)

ma(tit=txt,dbg=scaf,thm=thmd(pmc=/myconst),hm=/someconst)
ma(tit=txt,dbg=scaf,thm=thmd(pmc=/myconst,ab=sbui),hm=/someconst)


ma(tit=txt,dbg=scaf,thm=thmd(pmc=/myconst,ab=sbui),hm=/someconst)
MaterialApp(
  home: someconst, 
  title: Text(), 
  debugShowCheckedModeBanner: Scaffold(), 
  theme: ThemeData(
    primaryColor: myconst, 
    appBar: StreamBuilder()
  )
)

ma(tit=txt,dbg=scaf(body=row(ch=dtab),fab=csv),thm=thmd(pmc=/myconst,ab=sbui),hm=/someconst)
MaterialApp(
  home: someconst, 
  title: Text(), 
  debugShowCheckedModeBanner: Scaffold(
    body: Row(
      child: DataTable()
    ), 
    floatingActionButton: CustomScrollView()
  ), 
  theme: ThemeData(
    primaryColor: myconst, 
    appBar: StreamBuilder()
  )
)


ma(tit=txt,dbg=scaf(body=row(ch=dtab),fab=csv(txt=txt)),thm=thmd(pmc=/myconst,ab=sbui),hm=/someconst)

ma(tit=txt,dbg=scaf(body=row(ch=dtab),fab=csv(txt=txt("hello boyz"))),thm=thmd(pmc=/myconst,ab=sbui),hm=/someconst)

------------------------------------------------
ma(tit=txt,dbg=scaf(body=row(ch=dtab),fab=csv(txt=txt("hello boyz"))),thm=thmd(pmc=/myconst,ab=sbui),hm=/someconst)
MaterialApp(home: someconst, title: Text(), debugShowCheckedModeBanner: Scaffold(body: Row(child: DataTable()), floatingActionButton: CustomScrollView(txt: Text("hello boyz"))), theme: ThemeData(primaryColor: myconst, appBar: StreamBuilder()))

------------------------------------------------
ma(tit=txt,dbg=scaf(body=row(ch=dtab),fab=csv(txt=txt("hello boyz"))),thm=thmd(pmc=/tsfz,ab=sbui),hm=/mqw)
MaterialApp(home: MediaQuery.of(context).size.width, title: Text(), debugShowCheckedModeBanner: Scaffold(body: Row(child: DataTable()), floatingActionButton: CustomScrollView(txt: Text("hello boyz"))), theme: ThemeData(primaryColor: TextStyle(fontSize: 20.0), appBar: StreamBuilder()))

ma(tit=txt("monyet",slv=/icsearch),dbg=scaf(body=row(ch=dtab),fab=csv(txt=txt("hello boyz"))),thm=thmd(pmc=/tsfz,ab=sbui),hm=/mqw)

MaterialApp(
  home: MediaQuery.of(context).size.width, 
  title: Text(monyet", sliver: Icons.search), 
  debugShowCheckedModeBanner: Scaffold(
    body: Row(
      child: DataTable()
    ), 
    floatingActionButton: CustomScrollView(
      txt: Text("hello boyz")
    )
  ), 
  theme: ThemeData(
    primaryColor: TextStyle(fontSize: 20.0), 
    appBar: StreamBuilder()
  )
)
-- cobain widget_list
#scaf(ab=ab(tit=txt(title)),body=ce(ch=col(mxa=/mxac,chs=[txt("satu"),txt("dua
")])),fab=fab(onp=/fprint,too=/fprint,ch=/icadd))
    │   └── AnyNode(anchors={'chs': '__TEMPLATE__chs'}, attributes={'mxa': 'mxac'}, cantol='ch', level=3, name='col', type='widget')
    │       ├── AnyNode(cantol='chs', level=4, name='txt', text_content='satu', type='widget')
    │       └── AnyNode(cantol='chs', level=4, name='txt', text_content='dua', type='widget')

Scaffold(
  appBar: Appbar(title: Text(title)), 
  body: Center(
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center, 
      children: Text("satu")
    )
  ), 
  floatingActionButton: FloatingActionButton(
    onPressed: () => print('ok'), 
    tooltip: () => print('ok'), 
    child: Icons.add
  )
)
#scaf(ab=ab(tit=txt(title)),body=ce(ch=col(mxa=/mxac,chs=[txt("satu"),txt("dua
")])),fab=fab(onp=/fprint,too=/fprint,ch=/icadd))


Scaffold(
  appBar: Appbar(title: Text(title)), 
  body: Center(
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center, 
      children: [Text("satu"), Text("dua")]
    )
  ), 
  floatingActionButton: FloatingActionButton(
    onPressed: () => print('ok'), 
    tooltip: () => print('ok'), 
    child: Icons.add
  )
)

scaf(
  bc=/clrw,
  ab=ab(
    bc=/clw,
    ld=pad(
      pad=/insonl,
      ch=ir(
        ont=/fprint,
        ch=ic(/icmenu, sz=/30.0,clr=/clblk)
      )
    ),
    tit=im(im=aimg,h=/30.0),
    cT: /true,
    act:[
      stk(
        chs:[
          pad(
            pad=/insonr,
            ch=ir(
              ont=/fprint,
              ch=ic(
                ic(/icbasket,sz=/30.0,clr=/clblk),
              )
            )
          ),
          pos(
            bottom=/8.0,
            right=/16.0,
            ch=con(
              h=/20.0,
              w=/20.0,
              clr=corange,
              ch=ce(
                ch=txt("5"),
                sy=/tschz
              )
            )
          )
        ]
      ),

      pad(
        pad=/insonr,
        ch=ir(
          ont=/fprint,
          ch=ic(
            ic(/icsearch,sz=/30.0,clr=/clblk),
          )
        )
      ),
    ]
  )
)


#scaf(bc=/clrw,ab=ab(bc=/clw,ld=pad(pad=/insonl,ch=ir(ont=/fprint,ch=icmenu),tit=im(im=aimg,h=/30.0),cT=/true,act=[stk(chs=[pad(pad=/insonr,ch=ir(ont=/fprint,ch=icmenu,))),pos(bottom=/8.0,right=/16.0,ch=con(h=/20.0,w=/20.0,clr=corange,ch=ce(ch=txt("5"),sy=/tschz)))]),pad(pad=/insonr,ch=ir(ont=/fprint,ch=ic(ic(/icsearch,sz=/30.0,clr=/clblk),))),]))


-- calon utk process programs



