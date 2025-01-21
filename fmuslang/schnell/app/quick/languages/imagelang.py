######### biar exec bisa sukses
import cv2
from urllib.request import urlopen
import numpy as np
mapwarna = {
    'blue': (255,0,0),
    'green': (0,255,0),
    'red': (0,0,255),

    'cyan': (255,255,0),
    'magenta': (255,0,255),
    'yellow': (0,255,255),

    'white': (255,255,255),
    'black': (0,0,0),
}

# enum HersheyFonts {
#     FONT_HERSHEY_SIMPLEX        = 0, //!< normal size sans-serif font
#     FONT_HERSHEY_PLAIN          = 1, //!< small size sans-serif font
#     FONT_HERSHEY_DUPLEX         = 2, //!< normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)
#     FONT_HERSHEY_COMPLEX        = 3, //!< normal size serif font
#     FONT_HERSHEY_TRIPLEX        = 4, //!< normal size serif font (more complex than FONT_HERSHEY_COMPLEX)
#     FONT_HERSHEY_COMPLEX_SMALL  = 5, //!< smaller version of FONT_HERSHEY_COMPLEX
#     FONT_HERSHEY_SCRIPT_SIMPLEX = 6, //!< hand-writing style font
#     FONT_HERSHEY_SCRIPT_COMPLEX = 7, //!< more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX
#     FONT_ITALIC                 = 16 //!< flag for italic font
# };

font = cv2.FONT_HERSHEY_PLAIN
#########

# import os, sys
from pprint import pprint as pp
from uuid import uuid4 as u4
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([schnelldir, '..'])
# # print(schnelldir)
import sys
from pathlib import Path
sidoarjodir = Path(__file__).resolve().parent.parent.parent.parent.parent
#                              file     langs quick app     sch   sid
sys.path.append(sidoarjodir)

from schnell.app.transpiler.frontend.main import process_language
from schnell.app.dirutils import joiner, joinhere
from schnell.app.fileutils import file_write, file_content
from schnell.app.printutils import indah4
from schnell.app.stringutils import sanitize_chars
from schnell.app.treeutils import (
    anak,
    data,
    token,
    child1,
    child2,
    child3,
    child4,
    child,
    chdata,
    chtoken,
    ispohon, istoken,
    beranak,
    sebanyak,
    jumlahanak,
)
from schnell.app.utils import env_get


imgoutput = {}

def reset():
    global imgoutput
    imgoutput.clear()

def imghandler(tree, parent=''):
    kembali = ''
    name, attrs, children, text = '','','', ''
    namaparent = ''
    itemid = ''
    for item in anak(tree):
        jenis = data(item)        
        if jenis == 'element_name':
            namaparent = token(item)
            itemid = str(u4())
            print('elem:', namaparent)
            if namaparent == 'canvas':
                print('tag canvas')
                imgoutput['canvas'] = {}
            elif namaparent == 'img':
                print('tag img', 'parent:', parent)
            elif namaparent == 'text':
                print('tag text', 'parent:', parent)
        elif jenis == 'element_config':
            for tupleitem in anak(item):
                jenis2 = data(tupleitem)
                if jenis2 == 'item_key_value':
                    k,v='',''
                    for anaktupleitem in anak(tupleitem):
                        jenis3 = data(anaktupleitem)
                        if jenis3 == 'item_key':
                            k = token(anaktupleitem)
                        elif jenis3 == 'item_value':
                            v = token(anaktupleitem)
                    print(f'  attr {namaparent}/{itemid} k=v => {k}={v}')
                    if namaparent=='canvas':
                        if k=='w':
                            imgoutput['width'] = v
                        elif k == 'h':
                            imgoutput['height'] = v
                        elif k == 'color':
                            imgoutput['color'] = v
                    else:
                        print(f'adding {k}={v}',end='')
                        if not itemid in imgoutput['canvas']:
                            print(f' to new {namaparent}')
                            imgoutput['canvas'][itemid] = {'type':namaparent, 'attrs': [f"{k}={v}"]}
                        else:
                            print(f' to existing {namaparent}')
                            #attrs = imgoutput['canvas'][itemid]['attrs'].append(f"{k}={v}")
                            #imgoutput['canvas'][itemid]['attrs'] = attrs
                            imgoutput['canvas'][itemid]['attrs'].append(f"{k}={v}")
                elif jenis2 == 'item_key_value_boolean':
                    nilai = token(tupleitem)
                    print(f'  attr {namaparent}/{itemid} bool => {nilai}')
        elif jenis == 'element_children':
            for tupleitem in anak(item):
                for anaktupleitem in tupleitem:
                    res = imghandler(anaktupleitem, parent=namaparent)
        elif jenis == 'cdata_text':
            text = token(item)
            print(f'  cdata {namaparent}/{itemid}:', text)
            if itemid not in imgoutput['canvas']:
                # ini jk kita tdk specify config [], hanya cdata
                # tapi masih gagal nih
                # ../img)<canvas(<img[src=U//bali]<text|this is my first journey)
                # oh ternyata muncul, tapi kepotong, ada di atas...
                # create_text(0,0,"hello world","black")
                imgoutput['canvas'][itemid] = {'attrs': [], 'type': 'text'}
            imgoutput['canvas'][itemid]['attrs'].append(f'text={text}')


# cv::HersheyFonts {
#   cv::FONT_HERSHEY_SIMPLEX = 0,
#   cv::FONT_HERSHEY_PLAIN = 1,
#   cv::FONT_HERSHEY_DUPLEX = 2,
#   cv::FONT_HERSHEY_COMPLEX = 3,
#   cv::FONT_HERSHEY_TRIPLEX = 4,
#   cv::FONT_HERSHEY_COMPLEX_SMALL = 5,
#   cv::FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
#   cv::FONT_HERSHEY_SCRIPT_COMPLEX = 7,
#   cv::FONT_ITALIC = 16
# }

kode_output_image = file_content(joinhere(__file__, 'imagelang_template.py'))
# kode_output_image = """
# import numpy as np
# import cv2
# import random
# import requests
# from urllib.request import urlopen

# mapwarna = {
#     'blue': (255,0,0),
#     'green': (0,255,0),
#     'red': (0,0,255),

#     'cyan': (255,255,0),
#     'magenta': (255,0,255),
#     'yellow': (0,255,255),

#     'white': (255,255,255),
#     'black': (0,0,0),
# }

# font = cv2.FONT_HERSHEY_SIMPLEX
# default_font_scale = 1
# thickness = 2

# img = np.zeros((__TINGGI__, __LEBAR__, 3), dtype=np.uint8)
# #img.fill(__WARNA__) # or img[:] = 255
# img[:] = __WARNA__


# def put_text_on_image(img, text, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=default_font_scale, thickness=thickness, color='white'):

#     def get_text_width(text, font, font_scale, thickness):
#         (width, _) = cv2.getTextSize(text, font, font_scale, thickness)[0]
#         return width

#     def get_text_height(text, font, font_scale, thickness):
#         (_, height) = cv2.getTextSize(text, font, font_scale, thickness)[0]
#         return height

#     # Get image dimensions
#     height, width = img.shape[:2]
#     warna = mapwarna[color]

#     # Set spacing between lines of text
#     v_spacing = int(1.5 * get_text_height(text, font, font_scale, thickness))

#     # Split the text into lines based on newlines
#     lines = text.splitlines()

#     # Initialize variables for drawing text
#     x = 0
#     y = get_text_height(text, font, font_scale, thickness)

#     # Draw the text onto the image
#     for line in lines:
#         # Split the line into parts based on the image width
#         while get_text_width(line, font, font_scale, thickness) > width:
#             i = 1
#             while get_text_width(line[:i], font, font_scale, thickness) < width:
#                 i += 1
#             part = line[:i-1]
#             line = line[i-1:]
#             cv2.putText(img, part, (x, y), font, font_scale, warna, thickness)
#             y += v_spacing

#         # Draw the line onto the image
#         cv2.putText(img, line, (x, y), font, font_scale, warna, thickness)
#         y += v_spacing

#     return img

# def create_rect(x,y,w,h,warna='red'):
#     # global img
#     x,y,w,h = int(x),int(y),int(w),int(h)
#     cv2.rectangle(img, (x,y), (x+w,y+h), mapwarna[warna], -1)

# def create_circle(x,y,w,h,warna='red'):
#     # global img
#     center = (x+(w//2), y+(h//2))
#     radius = min(w,h)//2
#     cv2.circle(img, center, radius, mapwarna[warna], -1)

# def create_eclipse(x,y,w,h,warna='red'):
#     # global img
#     center = (x+(w//2), y+(h//2))
#     radius = min(w,h)//2
#     ax1 = w//2
#     ax2 = h//2
#     angle = 0
#     startangle = 0
#     endangle = 360
#     cv2.eclipse(img, center, (ax1,ax2), angle, startangle, endangle, mapwarna[warna], -1)

# def create_image2(alamat, x,y,w,h, alpha=0.5):
#     global img
#     x,y,w,h = int(x),int(y),int(w),int(h)
#     req = urlopen(alamat)
#     #print(alamat, ':', req)
#     image = np.asarray(bytearray(req.read()), dtype=np.uint8)
#     #image = cv2.imdecode(image, -1)
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     if w==0 or h==0:
#         h,w,_=image.shape
#     else:
#         image = cv2.resize(image.copy(), (w,h))

#     #img = np.uint8(img*alpha + image*(1-alpha))

#     #print(f'''
#     #x = {x}
#     #y = {y}
#     #w = {w}
#     #    x+w = {x+w}
#     #h = {h}
#     #    y+h = {y+h}
#     #shape 1 = {img.shape}
#     #shape 2 = {image.shape}
#     #''')

#     #https://stackoverflow.com/questions/56002672/display-an-image-over-another-image-at-a-particular-co-ordinates-in-opencv
#     #img[x:x+w,y:y+h,:] = image[0:w,0:h,:]
#     img[y:y+image.shape[0], x:x+image.shape[1]] = image

# def create_image(alamat, x, y, w, h, alpha=0.5):
#     global img
#     x, y, w, h = int(x), int(y), int(w), int(h)
#     req = urlopen(alamat)

#     image = np.asarray(bytearray(req.read()), dtype=np.uint8)

#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     if w == 0 or h == 0:
#         h, w, _ = image.shape
#     else:
#         image = cv2.resize(image.copy(), (w, h))

#     overlay = image.copy()
#     alpha = max(0, min(1, alpha))  # Make sure alpha is in the range [0,1]
#     cv2.addWeighted(overlay, alpha, img[y:y + h, x:x + w], 1 - alpha, 0, img[y:y + h, x:x + w])

# def write_on_rectangle(text, x, y, w, h, color='blue', font_scale=default_font_scale, thickness=thickness, warna_rectangle = (255,255,255), alpha=0.5):
#     '''
#     ini masih gagal
#     '''
    
#     global img, put_text_on_image
#     x,y,w,h = int(x),int(y),int(w),int(h)
#     warna_tulisan = mapwarna[color]    
#     black = np.zeros((h, w, 3), np.uint8)  # Create a black image with the specified size

#     # Convert the color from a string to a tuple of BGR values
#     #if isinstance(color, str):
#     #    color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))[::-1]

#     overlay = black.copy()
#     cv2.rectangle(overlay, (0, 0), (w, h), warna_rectangle, -1)
#     alpha = max(0, min(1, alpha))
#     cv2.addWeighted(overlay, alpha, black, 1 - alpha, 0, black)

#     gabung = put_text_on_image(overlay, text, color=color, font_scale=font_scale, thickness=thickness)

#     # Set the position of the rectangle within the image
#     #x, y = int(x), int(y)
#     #img = np.zeros((y + h, x + w, 3), np.uint8)
#     #img[:, :] = (255, 255, 255) # background putih, harusnya sesuai dg main color
#     img[y:y+h, x:x+w] = gabung

#     #return img_with_rect

# def create_line():
#     pass

# def create_text(x, y, tulisan, warna='black', scale=1.5, thick=2):
#     # (image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
#     x,y = int(x),int(y)
#     if y == 0:
#         y = 25 # biar keliatan
#     cv2.putText(img, tulisan, (x,y), font, scale, mapwarna[warna], thick)

# __TEMPLATE_CODE__

# cv2.imshow(r'__FILEPATH__', img)
# __TEMPLATE_TULIS_FILEPATH__
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# """


#unsplash
#unsplash/w,h
#unsplash/w,h/wallpaper,landscape
#picsum -> 640x480
#picsum/w,h
#https://source.unsplash.com/random/1920x1080/?wallpaper,landscape
#https://source.unsplash.com/random/1920x1080
#https://source.unsplash.com/random
#https://picsum.photos/1920/1080

def process_output(imgoutput, filepath=None, returning=False):
    template_codes = []
    # pastikan background size > ukuran image yg akan didownload
    screen_width = '2000'
    screen_height = '2000' # 1920x1080, 1920 kenapa jadi tinggi?
    screen_background = 'white'

    if 'width' in imgoutput:
        screen_width = imgoutput['width']
    if 'height' in imgoutput:
        screen_height = imgoutput['height']
    if 'color' in imgoutput:
        screen_background = imgoutput['color']

    for k,v in imgoutput.items():
        if k=='canvas':
            for _uuid,dict_attrs in imgoutput['canvas'].items():

                # oprek 1a708259-1955-485b-82bd-18b1363bb545 
                # dan {'type': 'img', 'attrs': ['x=10', 'y=150', 'w=500', 'h=600', 'src=https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Seal_of_ASEAN.svg/500px-Seal_of_ASEAN.svg.png']}
                # /<class 'dict'>
                # oprek 80e5b3a8-89d4-4b6a-958b-29a69a13ce02 
                # dan {'type': 'text', 'attrs': ['x=750', 'y=300', 'w=500', 'h=400', 'sz=0.75', 'color=red', 'text=ini baris pertama__NLini baris kedua__NLini baris ketiga']}
                # /<class 'dict'>
                print(f'oprek {_uuid} dan {dict_attrs}/{type(dict_attrs)}')

                # handle <img
                if dict_attrs['type'] == 'img':
                    x,y,width,height,alpha=0,0,0,0,.9
                    fungsi = 'create_rect'
                    alamat = ''
                    warna = 'red'
                    # print(f'sekali lagi, w adlh: {w} jenis {type(w)}')
                    # print(f'sekali lagi, w adlh: {w} dan attrs nya adlh {w["attrs"]}')
                    for anaklaki in dict_attrs['attrs']:
                        # print(f'oprek anaklaki {anaklaki}')
                        kunci,nilai=anaklaki.split('=',1)
                        if kunci == 'x':
                            x = float(nilai)
                            if nilai.startswith('.'):
                                x = float(nilai)*float(screen_width)
                                # print(f"bangsat float(nilai)*float(screen_width) = float(nilai)*float(screen_width) = ")
                            indah4(f'nilai {nilai}, x {x}, sw = {screen_width}', warna='blue')
                        elif kunci == 'y':
                            if nilai.startswith('.'):
                                y = float(nilai)*float(screen_height)
                            else:
                                y = float(nilai)
                            indah4(f'nilai {nilai}, y {y}, sh = {screen_height}', warna='blue')
                        elif kunci == 'w':
                            if nilai.startswith('.'):
                                width = float(nilai)*float(screen_width)
                            else:
                                width = int(nilai)
                            indah4(f'nilai {nilai}, width {width}, sw = {screen_width}', warna='blue')
                        elif kunci == 'h':
                            if nilai.startswith('.'):
                                height = float(nilai)*float(screen_height) # .25 => 25% height
                            else:
                                height = int(nilai)
                            indah4(f'nilai {nilai}, height {height}, sh = {screen_height}', warna='blue')
                        elif kunci == 'alpha':
                            if nilai.startswith('.') or nilai.startswith('0.'):
                                alpha = float(nilai)
                            else:
                                alpha = float(nilai)/100 # 80 -> 0.8
                        elif kunci == 'color':
                            warna = nilai
                        elif kunci == 'src':
                            if nilai.startswith('http') or nilai.startswith('U') or nilai.startswith('P'):
                                fungsi = 'create_image'
                                alamat = nilai
                            elif nilai in ['rect', 'circle', 'ellipse', 'line']:
                                fungsi = 'create_' + nilai
                    # generate
                    if fungsi == 'create_image':
                        if alamat.startswith('U'):  # unsplash
                            alamat = alamat.removeprefix('U')
                            if not alamat:
                                alamat = 'https://source.unsplash.com/random'
                            elif alamat.count('/')==2:
                                # U/1920x1080/wallpaper,landscape <- gak bisa comma
                                # U//wallpaper,landscape <- gak bisa comma
                                # https://source.unsplash.com/random/1920x1080/?wallpaper,landscape <- gak bisa comma
                                _,size,topic = alamat.split('/')
                                if not size:
                                    width = 640
                                    height = 480
                                else:
                                    # gak bisa comma, krn jadi item config yg berbeda dalam decl-lang
                                    width,height = size.split('x')
                                if topic:
                                    alamat = f'https://source.unsplash.com/random/{width}x{height}/?{topic}'
                                else:
                                    alamat = f'https://source.unsplash.com/random/{width}x{height}'
                            else:
                                # https://source.unsplash.com/random/1920x1080
                                if not width:
                                    width = 640
                                if not height:
                                    height = 480
                                alamat = f'https://source.unsplash.com/random/{width}x{height}'
                        elif alamat.startswith('P'):  # picsum
                            alamat = alamat.removeprefix('P')
                            # P
                            # P/1920x1080
                            if not alamat:
                                width=640
                                height=480
                            else:
                                _,alamat = alamat.split('/',1)
                                width, height = alamat.split('x')
                            alamat = f'https://picsum.photos/{width}/{height}'
                        # else: not unsplash or picsum, just get it
                        kode = f'{fungsi}("{alamat}", {x},{y},{width},{height}, {alpha})'
                    else:
                        kode = f'{fungsi}({x},{y},{width},{height},"{warna}")'
                    # indah4(kode, warna='green')

                elif dict_attrs['type'] == 'text':
                    x,y=0,0
                    w,h=0,0  # utk nulis pake koordinate di rectangle
                    init_rectangle=False
                    init_xy=False
                    init_scale=False
                    init_color=False
                    scale=1.0
                    thick=2
                    init_thickness=False
                    warna='black'
                    warna_rect='white'
                    init_warna_rect=False
                    content = ''
                    nilai_alpha=0.9
                    init_alpha=False

                    for anaklaki in dict_attrs['attrs']:
                        kunci,nilai=anaklaki.split('=')
                        if kunci == 'x':
                            init_xy=True
                            x = float(nilai)
                            if nilai.startswith('.'):
                                x = float(nilai)*float(screen_width)
                        elif kunci == 'y':
                            init_xy=True
                            if nilai.startswith('.'):
                                y = float(nilai)*float(screen_height)
                            else:
                                y = float(nilai)

                        # utk nulis di rectangle
                        elif kunci == 'w':
                            init_rectangle=True
                            w = float(nilai)
                            if nilai.startswith('.'):
                                w = float(nilai)*float(screen_width)
                        elif kunci == 'h':
                            init_rectangle=True
                            if nilai.startswith('.'):
                                h = float(nilai)*float(screen_height)
                            else:
                                h = float(nilai)
                        elif kunci == 'rect':
                            warna_rect = nilai
                            init_warna_rect=True
                        elif kunci == 'alpha':
                            init_alpha=True
                            if nilai.startswith('.') or nilai.startswith('0.'):
                                nilai_alpha = float(nilai)
                            else:
                                nilai_alpha = float(nilai)/100 # 80 -> 0.8

                        elif kunci == 'color':
                            warna = nilai
                            init_color=True
                        elif kunci == 'thick':
                            thick = nilai
                            init_thickness=True
                        elif kunci == 'text':
                            content = sanitize_chars(nilai)
                        elif kunci == 'size' or kunci == 'sz' or kunci == 'z':
                            scale=nilai
                            init_scale=True

                    if init_xy and init_scale and not init_rectangle:
                        # jk specify: x,y,sz but not w,h
                        kode = f'create_text({x},{y},"""{content}""","{warna}",{scale})'
                    elif init_scale and not init_rectangle:
                        # jk specify: sz, but not w,h
                        if init_color:
                            kode = f'put_text_on_image(img, """{content}""", font_scale={scale}, color="{warna}")'
                        else:
                            kode = f'put_text_on_image(img, """{content}""", font_scale={scale})'
                    elif init_rectangle and init_xy:
                        # jk specify: x,y,w,h maka write in a box
                        # write_on_rectangle(text, x, y, w, h, color='blue', alpha=0.5):

                        args = [f'"""{content}""", {x}, {y}, {w}, {h}']
                        if init_scale:
                            args.append(f'font_scale={scale}')
                        if init_thickness:
                            args.append(f'thickness={thick}')
                        if init_color:
                            args.append(f'color="{warna}"')
                        if init_warna_rect:
                            args.append(f'warna_rectangle=mapwarna["{warna_rect}"]')
                        if init_alpha:
                            args.append(f'alpha={nilai_alpha}')

                        # if init_color:
                        #     if init_scale:
                        #         if init_thickness:
                        #             kode = f'write_on_rectangle("""{content}""", {x}, {y}, {w}, {h}, font_scale={scale}, thickness={thick}, color="{warna}")'
                        #         else:
                        #             kode = f'write_on_rectangle("""{content}""", {x}, {y}, {w}, {h}, font_scale={scale}, color="{warna}")'
                        #     else:
                        #         if init_thickness:
                        #             kode = f'write_on_rectangle("""{content}""", {x}, {y}, {w}, {h}, thickness={thick}, color="{warna}")'
                        #         else:
                        #             kode = f'write_on_rectangle("""{content}""", {x}, {y}, {w}, {h}, color="{warna}")'
                        # else:
                        #     if init_scale:
                        #         kode = f'write_on_rectangle("""{content}""", {x}, {y}, {w}, {h}, font_scale={scale})'
                        #     else:
                        #         kode = f'write_on_rectangle("""{content}""", {x}, {y}, {w}, {h})'
                        kode = f'write_on_rectangle({", ".join(args)})'
                    else:
                        # jk hanya specify warna
                        if init_color:
                            kode = f'put_text_on_image(img, """{content}""", color="{warna}")'
                        else:
                            kode = f'put_text_on_image(img, """{content}""")'

                    indah4(f"""
                    init_xy = {init_xy}
                    init_scale = {init_scale}
                    init_rectangle = {init_rectangle}
                    screen_background = {screen_background}
                    """, warna='cyan')
                    indah4(kode, warna='yellow')

                template_codes.append(kode)

    content = kode_output_image.replace('__TEMPLATE_CODE__', '\n\n'.join(template_codes))
    content = content.replace('__TINGGI__', screen_height).replace('__LEBAR__',screen_width)
    content = content.replace('__WARNA__', f'mapwarna["{screen_background}"]')
    if not filepath:
        content = content.replace('__FILEPATH__', f'RESULT').replace('__TEMPLATE_TULIS_FILEPATH__', '')
    else:
        content = content.replace('__FILEPATH__', filepath).replace('__TEMPLATE_TULIS_FILEPATH__', f"cv2.imwrite(r'{filepath}', img)")
    # file_output = joiner(env_get('ULIBPY_DATA_FOLDER_ABS'), 'gambar.py')
    # indah4(f'{file_output}',warna='cyan')
    # file_write(file_output, content)
    if returning:
        return content
    indah4(f"kita mau exec [{content}]", warna='red')
    exec(content)


# image harus rectangular...
imgcode = """
<canvas[w=1000,h=800,color=red](
    <img[x=100,y=500,w=.25,h=.25,rotateccw=45,grayscale=50,alpha=80,src=rect,color=yellow]
    <img[x=10,y=150,w=500,h=600,src=https://media.gettyimages.com/photos/bella-thorne-attends-the-los-angeles-premiere-midnight-sun-at-on-picture-id932666434?s=2048x2048]
    <text[x=10,y=250,sz=14,color=blue]|hello mama mia di tinggi 250
    <text[x=10,y=500,sz=14,color=green]|ini di tinggi 500
)
"""


def imagelang(code=imgcode, filepath=None, returning=False):
    reset()
    # C:\Users\usef\work\sidoarjo\schnell\app\quick\__init__.py:957
    # C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\editor_fmus.py:423
    code = code.replace('__ASK_NEWLINE__', '\n').replace('__ASK_TAB__', '\t')
    # code = sanitize_chars(code)
    process_language(code, current_handler=imghandler)
    pp(imgoutput)
    if returning:
        return process_output(imgoutput, filepath=filepath, returning=True)
    process_output(imgoutput, filepath=filepath, returning=False)
