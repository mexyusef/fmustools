
# main
		for insn in instructions:
			hasil = handler(insn)
			results.append(hasil)
		hasil = '\n'.join(results)
		if returning:
			return hasil
		indah4(hasil, warna='yellow')

# handler

def declarative_element(tree):  
  kembali = ''
  name, attrs, children, text = '','','', ''
  for item in anak(tree):
    jenis = data(item)
    if jenis == 'element_name':
      name = element_name(item)
    elif jenis == 'element_config':
      attrs = element_config(item)
    elif jenis == 'element_children':
      children = element_children(item)
    elif jenis == 'cdata_text':
      text = token(item)
  kembali += f'<{name}'
  if attrs:
    kembali += ' ' + attrs
  kembali += '>\n'
  if text:
    inc()
    content = tabify_content(text, tab())
    kembali += content
    dec()
    kembali += '\n'
  if children:
    inc()
    content = tabify_content(children, tab())
    kembali += content
    dec()
    kembali += '\n'
  kembali += f'</{name}>'
  return kembali

def handler(tree):
  kembali = declarative_element(tree)
  return kembali

# bahasa
`<satu<dua<tiga/config/(children)`
declarative_program: declarative_element (declarative_element)*
declarative_element: "<" element_name element_config? cdata_text? element_children?

/..something../ atau $..something..$
element_config: "/" element_config_item (element_config_separator element_config_item)* "/"
  | "$" element_config_item_berslash (element_config_separator element_config_item_berslash)* "$"

element_children: "(" declarative_program ")"
cdata_text: HURUF_CDATA

bgm jk: <elem diikuti cdata_text ??? pemisahnya apa?
harusnya:
cdata_text: "%" HURUF_CDATA
sementara ini: cdata_text hanya bisa muncul jk ada config, otherwise kemakan oleh "element_name"

# log pakai
<a<b(<c<d<e/nilai=kuda/sampurasun(<f<g))
<a>
</a>
<b>
  <c>
  </c>
  <d>
  </d>
  <e nilai=kuda>
    sampurasun
    <f>
    </f>
    <g>
    </g>
  </e>
</b>

<a<b(<c/disabled/<d<e/nilai=kuda/sampurasun(<f<g))
<a>
</a>
<b>
  <c disabled>
  </c>
  <d>
  </d>
  <e nilai=kuda>
    sampurasun
    <f>
    </f>
    <g>
    </g>
  </e>
</b>

