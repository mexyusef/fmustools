from schnell.app.dirutils import joinhere
from schnell.app.fileutils import file_content
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
    FILE_DECLANG,
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
    FILE_MOBILE,
    FILE_MULTIMEDIA,
    FILE_PENJELASAN,
    FILE_PROJECTS,
    FILE_SEMERU,
    FILE_TDD,
    FILE_URLS,
    FILE_TEMPLATES,
    FILE_TWITTER,
    FILE_UPWORK,
    FILE_YOUTUBE,
)

editor_fmus_mapper4 = {
    "u": {
        'desc': 'daftar alamat/urls',
        'content':   file_content(FILE_URLS)+ '\n' +FILE_URLS,
    },
    "U": {
        'desc': 'daftar alamat/urls',
        'content':   file_content(FILE_URLS)+ '\n' +FILE_URLS,
    },
    "urls": {
        'desc': 'daftar alamat/urls',
        'content':   file_content(FILE_URLS)+ '\n' +FILE_URLS,
    },
    "alamat": {
        'desc': 'daftar alamat',
        'content':   file_content(FILE_URLS)+ '\n' +FILE_URLS,
    },

#     "docker": {
#         'desc': 'all docker command',
#         'content': """
# cara build
# cara run container
# cara bikin docker-compose
# generate docker compose here
# """
#     },

    "mem": { 'desc': 'memorize, hafal', 'content':   file_content(FILE_MEMORY)+ '\n' +FILE_MEMORY, },

    "rn": {
        'desc': 'editor_fmus_mobile.txt',
        'content':   file_content(FILE_MOBILE)+ '\n' +FILE_MOBILE,
    },
    "mob": {
        'desc': 'editor_fmus_mobile.txt',
        'content':   file_content(FILE_MOBILE)+ '\n' +FILE_MOBILE,
    },
    "mobile": {
        'desc': 'editor_fmus_mobile.txt',
        'content':   file_content(FILE_MOBILE)+ '\n' +FILE_MOBILE,
    },
    "ketik": {
        'desc': 'operasi /ketik)',
        'content':   file_content(FILE_KETIK)+ '\n' +FILE_KETIK,
    },
    "/ketik)": {
        'desc': 'operasi /ketik)',
        'content':   file_content(FILE_KETIK)+ '\n' +FILE_KETIK,
    },

    "decl": { 'desc': 'editor_fmus_declang.txt', 'content': file_content(FILE_DECLANG) + '\n' + FILE_DECLANG, },

    "file": {
        'desc': 'fileops',
        'content': file_content(FILE_KARYA_FILES) + '\n' + FILE_KARYA_FILES,
    },
    "files": {
        'desc': 'fileops',
        'content': file_content(FILE_KARYA_FILES) + '\n' + FILE_KARYA_FILES,
    },
    "/files>": {
        'desc': 'fileops',
        'content': file_content(FILE_KARYA_FILES) + '\n' + FILE_KARYA_FILES,
    },
    "/files)": {
        'desc': 'fileops',
        'content': file_content(FILE_KARYA_FILES) + '\n' + FILE_KARYA_FILES,
    },


    "prj": {
        'desc': 'start projects',
        'content': file_content(FILE_PROJECTS) +'\n'+ FILE_PROJECTS,
    },
    "P": {
        'desc': 'start projects',
        'content': file_content(FILE_PROJECTS) +'\n'+ FILE_PROJECTS,
    },

    "jelas": {
        'desc': 'penjelasan semua karya2 kita dg kalimat sederhana dan kknize agar bisa pengkondisian awal',
        'content': file_content(FILE_PENJELASAN) +'\n'+ FILE_PENJELASAN,
    },
    "penjelasan": {
        'desc': 'penjelasan semua karya2 kita dg kalimat sederhana dan kknize agar bisa pengkondisian awal',
        'content': file_content(FILE_PENJELASAN) +'\n'+ FILE_PENJELASAN,
    },
    "x": {
        'desc': 'penjelasan semua karya2 kita dg kalimat sederhana dan kknize agar bisa pengkondisian awal',
        'content': file_content(FILE_PENJELASAN) +'\n'+ FILE_PENJELASAN,
    },
    "exp": {
        'desc': 'penjelasan semua karya2 kita dg kalimat sederhana dan kknize agar bisa pengkondisian awal',
        'content': file_content(FILE_PENJELASAN) +'\n'+ FILE_PENJELASAN,
    },
    "explain": {
        'desc': 'penjelasan semua karya2 kita dg kalimat sederhana dan kknize agar bisa pengkondisian awal',
        'content': file_content(FILE_PENJELASAN) +'\n'+ FILE_PENJELASAN,
    },

    "db": {
        'desc': 'all about db',
        'content': file_content(FILE_DB)+ '\n' +FILE_DB,
    },

    "ls": { 'desc': '/ls), /exec), /find), /grep)', 'content': file_content(FILE_LS)+ '\n' +FILE_LS, },
    "exec": {
        'desc': '/ls), /exec), /find), /grep)',
        'content': file_content(FILE_LS)+ '\n' +FILE_LS,
    },
    "find": {
        'desc': '/ls), /exec), /find), /grep)',
        'content': file_content(FILE_LS)+ '\n' +FILE_LS,
    },
    "grep": {
        'desc': '/ls), /exec), /find), /grep)',
        'content': file_content(FILE_LS)+ '\n' +FILE_LS,
    },

    "conf": {
        'desc': 'config: ssl, java, etc',
        'content': file_content(FILE_CONFIG)+ '\n' +FILE_CONFIG,
    },
    "config": {
        'desc': 'config: ssl, java, etc',
        'content': file_content(FILE_CONFIG)+ '\n' +FILE_CONFIG,
    },
    "ssl": {
        'desc': 'config: ssl, java, etc',
        'content': file_content(FILE_CONFIG)+ '\n' +FILE_CONFIG,
    },


    "api": { 'desc': 'all about api', 'content': file_content(FILE_API) + '\n' + FILE_API, },

    "cloud": { 'desc': 'all about cloud', 'content':  file_content(FILE_CLOUD) + '\n' +FILE_CLOUD, },

    "do": { 'desc': 'all about devops', 'content': file_content(FILE_DEVOPS) + '\n' + FILE_DEVOPS, },

    "git": { 'desc': 'perintah2 penting utk git', 'content': file_content(FILE_GIT) +'\n'+ FILE_GIT, },

    "tdd": { 'desc': 'all about tdd', 'content': file_content(FILE_TDD) + '\n' + FILE_TDD, },

    "ai": { 'desc': 'all about ML/AI', 'content': file_content(FILE_ML_AI) + '\n' + FILE_ML_AI, },
    "ml": { 'desc': 'all about ML/AI', 'content': file_content(FILE_ML_AI) + '\n' + FILE_ML_AI, },


    "gh": {
        'desc': 'all about github',
        'content': file_content(FILE_GITHUB) +'\n'+ FILE_GITHUB,
    },
    "tw": {
        'desc': 'all about twitter',
        'content': file_content(FILE_TWITTER) +'\n'+ FILE_TWITTER,
    },
    "yt": {
        'desc': 'all about youtube',
        'content': file_content(FILE_YOUTUBE) +'\n'+ FILE_YOUTUBE,
    },

    "F": {
        'desc': 'all about folders etc',
        'content':   file_content(FILE_FOLDERS)+'\n'+FILE_FOLDERS,
    },
    "f": {
        'desc': 'all about folders etc',
        'content':   file_content(FILE_FOLDERS)+'\n'+FILE_FOLDERS,
    },
    "folders": {
        'desc': 'all about folders etc',
        'content':   file_content(FILE_FOLDERS)+'\n'+FILE_FOLDERS,
    },

    "gawe": { 'desc': 'daftar alamat gawe', 'content':   file_content(FILE_JOBS)+ '\n' +FILE_JOBS, },
    "jobs": { 'desc': 'daftar alamat gawe', 'content':   file_content(FILE_JOBS)+ '\n' +FILE_JOBS, },

    "debate": { 'desc': 'bantuan utk berdebat', 'content': file_content(FILE_DEBATE) +'\n'+ FILE_DEBATE, },
    "dbt": { 'desc': 'bantuan utk berdebat', 'content': file_content(FILE_DEBATE) +'\n'+ FILE_DEBATE, },

    "hack": { 'desc': 'bantuan utk hackathon', 'content': file_content(FILE_HACK) +'\n'+ FILE_HACK, },

    "karya": {
        'desc': 'bantuan utk karya tmsk upw',
        'content':   file_content(FILE_KARYA)+'\n'+FILE_KARYA,
    },
    "K": {
        'desc': 'bantuan utk karya tmsk upw',
        'content':   file_content(FILE_KARYA)+'\n'+FILE_KARYA,
    },
    "k": {
        'desc': 'bantuan utk karya tmsk upw',
        'content':   file_content(FILE_KARYA)+'\n'+FILE_KARYA,
    },

    "d": {
        'desc': 'bantuan utk demo fmuslang dsb',
        'content':   file_content(FILE_DEMO)+'\n'+FILE_DEMO,
    },
    "D": {
        'desc': 'bantuan utk demo fmuslang dsb',
        'content':   file_content(FILE_DEMO)+'\n'+FILE_DEMO,
    },
    "demo": {
        'desc': 'bantuan utk demo fmuslang dsb',
        'content':   file_content(FILE_DEMO)+'\n'+FILE_DEMO,
    },


    "sem": { 'desc': 'perintah2 penting utk semeru', 'content': file_content(FILE_SEMERU) +'\n'+ FILE_SEMERU, },
    "semeru": { 'desc': 'perintah2 penting utk semeru', 'content': file_content(FILE_SEMERU) +'\n'+ FILE_SEMERU, },

    "AG": { 'desc': 'appgen mania', 'content': file_content(FILE_APPGEN) +'\n'+ FILE_APPGEN, },
    "ag": { 'desc': 'appgen mania', 'content': file_content(FILE_APPGEN) +'\n'+ FILE_APPGEN, },
    "appgen": {
        'desc': 'appgen mania',
        'content': file_content(FILE_APPGEN) +'\n'+ FILE_APPGEN,
    },

    "bez": { 'desc': 'appgen mania', 'content': file_content(FILE_BEZ) +'\n'+ FILE_BEZ, },

    "bat": { 'desc': 'batchers', 'content': file_content(FILE_BATCHERS) +'\n'+ FILE_BATCHERS, },

    "courses": { 'desc': 'batchers', 'content': file_content(FILE_COURSES) +'\n'+ FILE_COURSES, },
    "course": { 'desc': 'batchers', 'content': file_content(FILE_COURSES) +'\n'+ FILE_COURSES, },
    "co": { 'desc': 'batchers', 'content': file_content(FILE_COURSES) +'\n'+ FILE_COURSES, },
    "learn": { 'desc': 'kuliah, knowledge learning', 'content': file_content(FILE_COURSES) +'\n'+ FILE_COURSES, },
    "kul": { 'desc': 'batchers', 'content': file_content(FILE_COURSES) +'\n'+ FILE_COURSES, },
    "kuliah": { 'desc': 'batchers', 'content': file_content(FILE_COURSES) +'\n'+ FILE_COURSES, },

    "upw": { 'desc': 'napaktilas upwork', 'content': file_content(FILE_UPWORK) +'\n'+ FILE_UPWORK, },

    "mm": { 'desc': 'multimedia', 'content': file_content(FILE_MULTIMEDIA) +'\n'+ FILE_MULTIMEDIA, },
    "gif": { 'desc': 'multimedia', 'content': file_content(FILE_MULTIMEDIA) +'\n'+ FILE_MULTIMEDIA, },
    "img": { 'desc': 'multimedia', 'content': file_content(FILE_MULTIMEDIA) +'\n'+ FILE_MULTIMEDIA, },
    "vid": { 'desc': 'multimedia', 'content': file_content(FILE_MULTIMEDIA) +'\n'+ FILE_MULTIMEDIA, },
    "meme": { 'desc': 'multimedia', 'content': file_content(FILE_MULTIMEDIA) +'\n'+ FILE_MULTIMEDIA, },


    "T": {
        'desc': 'templates utk bikin berbagai fmuslang file',
        'content': file_content(FILE_TEMPLATES)+'\n'+FILE_TEMPLATES,
    },
    "tpl": {
        'desc': 'templates utk bikin berbagai fmuslang file',
        'content': file_content(FILE_TEMPLATES)+'\n'+FILE_TEMPLATES,
    },
    "template": {
        'desc': 'templates utk bikin berbagai fmuslang file',
        'content': file_content(FILE_TEMPLATES)+'\n'+FILE_TEMPLATES,
    },


    "cpp": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\cpp-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\cpp-boot.txt'),
    },
    "cs": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\cs-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\cs-boot.txt'),
    },
    "go": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\go-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\go-boot.txt'),
    },
    "java": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\java-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\java-boot.txt'),
    },
    "js": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\js-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\js-boot.txt'),
    },
    "py": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\py-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\py-boot.txt'),
    },
    "rb": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\rb-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\rb-boot.txt'),
    },
    "rs": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\rs-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\rs-boot.txt'),
    },
    "scala": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\scala-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\scala-boot.txt'),
    },
    "ts": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\ts-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\ts-boot.txt'),
    },
    "zig": {
        'desc': 'memorize, hafal',
        'content': r'C:\work\ciledug\ciledug\cepat\data\zig-boot.txt' + '\n' + file_content(r'C:\work\ciledug\ciledug\cepat\data\zig-boot.txt'),
    },


}
