from schnell.app.dirutils import joinhere
from schnell.app.fileutils import file_content
from schnell.app.printutils import indah4


editor_fmus_mapper = {

    "l": {
    'desc': 'list of localhost urls',
    'content': r"""http://localhost:3000
http://localhost:3001
http://localhost:3344
http://localhost:1420
http://localhost:4000
http://localhost:4200
http://localhost:5000
http://localhost:5173
http://localhost:6000
http://localhost:7000
http://localhost:8000
http://localhost:8080
http://localhost:8888
http://localhost:9000

C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\editor_fmus_mapper.py
"""},


    "ss": {
    'desc': 'screenshot b64=ocr dan filepath utk ctrl+2',
    'content': """C:/work/kenza/resources/images/screenshots,d
    __FILENAME__.jpg,f(b64=OCR=whatever)
C:/work/kenza/resources/images/screenshots/__FILENAME__.jpg
"""},


    # ini utk replace input dg ctrl 9
    "$$": {
    'desc': 'screenshot b64=ocr dg $01 filename pake ctrl+9 dan filepath utk ctrl+2',
    'content': """C:/work/kenza/resources/images/screenshots,d
    $01.jpg,f(b64=OCR=whatever)
C:/work/kenza/resources/images/screenshots/$01.jpg
"""},


    "$dir": {
    'desc': 'screenshot to dir/images/screenshots',
    'content': r"""__DIR__\images\screenshots,d
    $01.jpg,f(b64=OCR=whatever)
__DIR__\images\screenshots\$01.jpg
"""},


    "$p": {
    'desc': 'screenshot to C:/work/kenza/resources/images/portfolio,d',
    'content': r"""C:/work/kenza/resources/images/portfolio,d
    $01.jpg,f(b64=OCR=whatever)
C:/work/kenza/resources/images/portfolio/$01.jpg
"""},


    "$fun": {
    'desc': 'screenshot to C:/work/kenza/resources/images/fun',
    'content': """C:/work/kenza/resources/images/fun,d
    $01.jpg,f(b64=OCR=whatever)
C:/work/kenza/resources/images/fun/$01.jpg
"""},


    "cl": {
    'desc': 'git clone full url with /ketik)pnpm i di c:/hapus',
    'content': """c:/hapus,d
    $* git clone __FILENAME__
    __FILENAME__,d
        /ketik)pnpm i
"""},


    "clsrc": {
    'desc': 'git clone user/repo with /ketik)pnpm i di c:/hapus',
    'content': """c:/hapus,d
    $* git clone https://github.com/__USERNAME__/__FILENAME__
    __FILENAME__,d
        /ketik)pnpm i
"""},


    # clsrc + ss
    "clss":{
    'desc': 'clone + c:/work/kenza/resources/images/screenshots',
    'content': """c:/hapus,d
    $* git clone https://github.com/__USERNAME__/__FILENAME__
    __FILENAME__,d
        /ketik)pnpm i

C:/work/kenza/resources/images/screenshots,d
    __FILENAME__.jpg,f(b64=OCR=whatever)
C:/work/kenza/resources/images/screenshots/__FILENAME__.jpg
"""},


    "cldir": {
    'desc': 'git clone https://github.com/__USERNAME__/__FILENAME__',
    'content': """__DIR__,d
    $* git clone https://github.com/__USERNAME__/__FILENAME__
    __FILENAME__,d
        /ketik)pnpm i

__DIR__/screenshots,d
    __FILENAME__.jpg,f(b64=OCR=whatever)
__DIR__/screenshots/__FILENAME__.jpg
"""},




}

from .editor_fmus_mapper2 import editor_fmus_mapper2
from .editor_fmus_mapper3 import editor_fmus_mapper3
from .editor_fmus_mapper4 import editor_fmus_mapper4
from .editor_fmus_folders import best_practice_folders

editor_fmus_mapper.update(best_practice_folders)
editor_fmus_mapper.update(editor_fmus_mapper2)
editor_fmus_mapper.update(editor_fmus_mapper3)
editor_fmus_mapper.update(editor_fmus_mapper4)


from .widgetsconstants import (
    FILE_API,
    FILE_APPGEN,
    FILE_BATCHERS,
    FILE_BEZ,
    FILE_CLOUD,
    FILE_CONFIG,
    FILE_COURSES,
    FILE_DB,
    FILE_DEBATE,
    FILE_DEVOPS,
    FILE_DEMO,
    FILE_FOLDERS,
    FILE_GIT,
    FILE_GITHUB,
    FILE_HACK,
    FILE_JOBS,
    FILE_KARYA,
    FILE_KARYA_FILES,
    FILE_KETIK,
    # FILE_LEARN,
    FILE_LS,
    FILE_MEMORY,
    FILE_ML_AI,
    FILE_MULTIMEDIA,
    FILE_PENJELASAN,
    FILE_PROJECTS,
    FILE_SEMERU,
    FILE_TDD,
    FILE_UPWORK,
    FILE_URLS,
)



def reload_folder(keyname):
    """
    kita bikin keyname hanya yg pasti saja,
    jadi misal /files) dan /files> sama, jk hanya berikan /files) maka hanya key tsb yg direload
    """
    kembali = ''
    if keyname in editor_fmus_mapper:
        if keyname=='/dj':
            # C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\editor_fmus_mapper.py
            # C:\Users\usef\work\sidoarjo\schnell\gui\system\searcher\widgets\folders\django.txt
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/django.txt'))
        elif keyname=='/nd':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/node.txt'))
        elif keyname=='/nx':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/next.txt'))
        elif keyname=='/ns':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/nest.txt'))
        elif keyname=='/android':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/android.txt'))
        elif keyname=='/react':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/react.txt'))
        elif keyname=='/vue':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/vue.txt'))
        elif keyname=='/flask':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/flask.txt'))
        elif keyname=='/fastapi':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/fastapi.txt'))
        elif keyname=='/sb':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/springboot.txt'))
        elif keyname=='/jee':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/jakarta-ee.txt'))
        elif keyname=='/flu':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/flutter.txt'))
        elif keyname=='/rn':
            editor_fmus_mapper[keyname]['content'] = file_content(joinhere(__file__, 'folders/react-native.txt'))


        elif keyname=='/go':
            filepath = r'C:\work\ciledug\ciledug\cepat\data\go-boot.txt'
            editor_fmus_mapper[keyname]['content'] = file_content(filepath)+'\n'+filepath


        elif keyname in ['ag', 'AG', 'appgen']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_APPGEN)+'\n'+FILE_APPGEN
        elif keyname in ['bez']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_BEZ)+'\n'+FILE_BEZ
        elif keyname in ['co', 'course', 'courses', 'learn', 'kul', 'kuliah']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_COURSES)+'\n'+FILE_COURSES
        elif keyname in ['dbt', 'debate']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_DEBATE)+'\n'+FILE_DEBATE
        elif keyname in ['demo', 'D', 'd']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_DEMO)+'\n'+FILE_DEMO
        elif keyname in ['folders', 'F', 'f']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_FOLDERS)+'\n'+FILE_FOLDERS
        elif keyname in ['gh', 'github']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_GITHUB)+'\n'+FILE_GITHUB
        elif keyname in ['git']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_GIT)+'\n'+FILE_GIT
        elif keyname in ['hack', 'hackathon']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_HACK)+'\n'+FILE_HACK
        elif keyname in ['karya', 'K', 'k']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_KARYA)+'\n'+FILE_KARYA
        elif keyname in ['ls', '/ls)', '/exec)', '/grep)', '/find)', 'exec', 'find', 'grep']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_LS)+'\n'+FILE_LS
        # elif keyname in ['learn']:
        #     editor_fmus_mapper[keyname]['content'] = file_content(FILE_LEARN)+'\n'+FILE_LEARN
        elif keyname in ['ml', 'ai']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_ML_AI)+'\n'+FILE_ML_AI
        elif keyname in ['mm', 'img', 'gif', 'meme', 'vid']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_MULTIMEDIA)+'\n'+FILE_MULTIMEDIA
        elif keyname in ['exp', 'jelas', 'explain', 'penjelasan', 'x']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_PENJELASAN)+'\n'+FILE_PENJELASAN
        elif keyname in ['alamat', 'urls', 'U', 'u']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_URLS)+'\n'+FILE_URLS
        elif keyname in ['ssl', 'conf', 'config']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_CONFIG)+'\n'+FILE_CONFIG
        elif keyname in ['upw']:
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_UPWORK)+'\n'+FILE_UPWORK
        elif keyname=='ketik':
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_KETIK)+'\n'+FILE_KETIK
        elif keyname=='cloud':
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_CLOUD)+'\n'+FILE_CLOUD
        elif keyname=='db':
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_DB)+'\n'+FILE_DB
        elif keyname=='git':
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_GIT)+'\n'+FILE_GIT
        elif keyname=='gh':
            editor_fmus_mapper[keyname]['content'] = file_content(FILE_GITHUB)+'\n'+FILE_GITHUB
        else:
            kembali = f"not handling [{keyname}] for now"
            indah4(kembali)
            return kembali

        indah4(f"reload_folder => handling [{keyname}]...")
    elif keyname == 'config.txt':
        from startup import read_txt_config
        read_txt_config()
    else:
        kembali = f"[{keyname}] not in {editor_fmus_mapper.keys()}."
        indah4(kembali)

    return kembali
