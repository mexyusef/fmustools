langkah:
*!antd|
di sini kasih informasi:
config webpack
  harus bisa namai webpack...
config babel
config eslint
yarn add/remove/
###
[...]
...bahasa spt biasa

__TEMPLATE_PROJECT_DIR__ => input
__TEMPLATE_WEBPACK_NAME__ => webpack-mts.js
__TEMPLATE_ADDITIONAL_IMPORTS__
const CopyWebPackPlugin = require('copy-webpack-plugin');
const Dotenv = require('dotenv-webpack');
__TEMPLATE_ADDITIONAL_PLUGINS__
new CopyWebPackPlugin({
  patterns: [
    { from: `./${sourcedir}/assets`, to: '/' },
  ],
}),
new Dotenv(),
new HtmlWebPackPlugin({
  template: path.resolve(process.cwd(), sourcedir, 'src', 'index.html'),
  filename: "./index.html",
  favicon: path.resolve(process.cwd(), sourcedir, 'assets', 'favicon.ico'),
  // excludeChunks: [ 'server' ]
}),

__TEMPLATE_MTS_DIR__
ini harus sama dg __TEMPLATE_PROJECT_DIR__
no...
__TEMPLATE_PROJECT_DIR__
  __TEMPLATE_MTS_DIR__=react-mts-ui/src


= bikin bahasa webpack
= juga nextjs

ada baiknya juga:
*!antd|
ngasih tau dimana lokasi utk bikinnya...
/home/usef/tmp/
/tmp/hapus/whatever
misalnya
dan kembalikan qterminal...jangan langsung install

berbagai gaya react
sop
anjab
arsip
spor
sucor
gothinkster redux
gothinkster mobx

elif text .startswith('*!'):
  '''
  *!<code data csv>
    <- default ini sementara blm support
  *!grpc/<code data csv>
  '''			
  code = text.removeprefix('*!').strip()
  if code .startswith('help'):
    code = code.removeprefix('help')
    self.output = bantupeople.help(code)
  elif code.count(category_delimiter) == 1:
    category, program = code.split(category_delimiter)
    if category and program:					
      result, meta = bantupeople.generate(program, category)
      self.output = result if result else ''
      self.metaresult.update({
        'bantu_meta': meta
      })
  else:
    result, meta = bantupeople.generate(code, 'default')
    self.output = result if result else ''
    self.metaresult.update({
      'bantu_meta': meta
    })

if category in category_map:
  self.output = category_map.get(category, lambda x:'') (RootNode)
pada dasarnya, bantupeople.generate itu akses mapper func
category_map = {
  'django'      : bantu_django,
  'fake'        : bantu_faker,
  'fastapi'     : bantu_fastapi,
  'flask'       : bantu_flask,  
  'grpc'        : bantu_grpc,
  'nest2'       : bantu_nest_old,
  'nest'        : bantu_nest,
  'nodeapo'     : bantu_nodeapollo,
  'nodereact'   : bantu_nodereact, 
  'sql'         : bantu_sql,
  'sbgql'       : bantu_sbgql,
  'sboot'       : bantu_springboot,
  'ts'          : bantu_ts,
}


langsung bikin antd, bs, dan webpack

bikin webpack utk tiap hasil...
nextjs gimana ya dg webpack?
utk next sementara belum ya...
ada 5 aplikasi:
react+antd+wp
react+bs+wp
react+mui+wp
react+mui+ts+wp
next

bikin package.json
bikin index+app
abis itu masuk:
routes
layout
sidebar menu...
header...
footer
content
  dashboard
  table
  list
  card
  forms
  chart
  map
...

*!help
#<d[cn=search](<d[cn=searchInputs](<i[disabled,t=text]<d[cn=searchIcon](<SearchIcon))<d[cn=dataResult](<a(<p)))
#+e{'p':'Provider','cr':'ConnectedRouter','s':'Switch','r':'Route'}
#+a{'s':'store'}
#+a{'h':'history','p':'path'}
#+a{'c':'component'}
#-e['unused']
#-a['removeme']
#<a<b<c*short<d[onClick=hajar''c'k]
#<a<b<c*short<d[onClick=short'''c]
	txf value: ', '', 'c, 'k, 'p

#+e{}
{'ar': 'article', 'b': 'button', 'd': 'div', 'fi': 'fieldset', 'f': 'form', 'i': 'input', 'm': 'main', 'n': 'nav', 's': 'section', 'ta': 'textarea'}
#+a{}
{'c': 'class', 'cn': 'className', 'oc': 'onClick', 'og': 'onChange', 'ph': 'placeholder', 't': 'type'}

#<ar(<b)<d[cn=Whatever,onClick=doMe](<f(<fi<i[og=doThat,ph=write me''])<m)
<article>
  <button>
  </button>
</article>
<div className=Whatever onClick=doMe>
  <form>
    <fieldset>
    </fieldset>
    <input onChange=doThat placeholder='write me'>
    </input>
  </form>
  <main>
  </main>
</div>

l o trans
%$1*

## favicon

/tmp/hapuslah/react-antd/assets/favicon.ico


## antd

*!antd|/tmp/hapuslah,react-antd,webpack-antd|dummycode
OK: /tmp/hapuslah,react-antd,webpack-antd

## bs

*!bs|/tmp/hapuslah,react-bs,webpack-bs|dummycode

## med

*!med|/tmp/hapuslah,react-med,webpack-med|dummycode
OK: /tmp/hapuslah,react-med,webpack-med

## mts
*!mts|/home/usef/tmp/retry-mts2,retry-mts2,webpack-retrymts2|dummycode

*!mts|/home/usef/tmp/,react-mts-01,webpack-whatever|dummycode

*!mts|/home/usef/common/working/_incub/oprek/,react-mts-01,webpack-whatever|dummycode

*!mts|/tmp/hapuslah,react-mts-01,webpack-mts|dummycode
OK: /tmp/hapuslah,react-mts-01,webpack-mts

## mts2
*!mts2|/home/usef/tmp/,react-mts-02,webpack-mts2|dummycode

*!mts2|/tmp/hapuslah,react-mts-02,webpack-mts2|dummycode

## mts3
*!mts3|/home/usef/tmp/,react-mts3,webpack-mts3|dummycode
OK: /home/usef/tmp/,react-mts3,webpack-mts3

## next1

## next2

## next3

## sop

## spor


## sucor

