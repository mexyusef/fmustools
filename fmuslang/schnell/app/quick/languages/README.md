# rencana
tdd lang
form lang
faker lang

# guilang
kita sudah pernah bikin bhs flutter
bisa digunakan di sini utk bikin guilang
mulai saja dulu dari: flutter, lalu pyqt5
abis itu mungkin tkinter atau wxwidgets
selanjutnya java-fx, qt-go, qt-rs, dll

# tviewlang
baiknya kita jadikan library
harus juga dukung flex, grid, dst.

juga lihat rivo/tview postgresql sourcecode
terutama gunakan flex...dan distribute ukuran dsb.

# dotlang
utk tiap node

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

# cara kerja imagelang
/img)<canvas[w=1500,h=800,color=yellow](
    <img[x=10,y=150,w=800,h=600,alpha=0.95,src=https://everydaylifeinmaoschina.files.wordpress.com/2016/10/6608188028237558784.jpg?w=736]
    <text[x=250,y=100,w=330,h=100,sz=3.75,alpha=0.9,thick=10,rect=green,color=red]|LMAO
)

img = np.zeros((800, 1500, 3), dtype=np.uint8)
#img.fill(mapwarna["yellow"]) # or img[:] = 255
img[:] = mapwarna["yellow"]

create_image("https://everydaylifeinmaoschina.files.wordpress.com/2016/10/6608188028237558784.jpg?w=736", 10.0,150.0,800,600, 0.95)

write_on_rectangle("""LMAO""", 250.0, 100.0, 330.0, 100.0, font_scale=3.75, thickness=10, color="red", warna_rectangle=mapwarna["green"], alpha=0.9)

cv2.imshow(r'RESULT', img)

cv2.waitKey(0)
cv2.destroyAllWindows()]
