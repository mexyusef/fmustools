# utk replang
replang_active_languages = ['ts','py','java','go','rs','kt','dart','rb']
# utk csvlang

sample_data_csvlang = {
    'city': '{@City} country,s; id,n; name,s; populationDensity,n',
    'product': '{@Product} id,s; name,s; price,n',
    'todo': '{@Todo} title,s; description,t; completed,b; createdAt,dt',
    'user': '{@User} username,s; email,s',
}

# template table
template_tbl_todo = """[@Todo]
title,s;
description,t;
completed,b;
createdAt,dt:dt
"""

# template db
template_db_default = """[/dummy]{@Dummy}dummy,s"""

template_db_todo = f"""[/todo]{template_tbl_todo}"""

# model utk database
system_template_dict = {
    'default': template_db_default,
    'arsip': """ok""",
    'blog': """ok""",
    'rockit': """ok""",
    'sitarang': """ok""",
    'sop': """ok""",
    'spor': """ok""",
    'sucor': """ok""",
    'todo': template_db_todo,
    'whosedoc': """ok""",
}
system_template = list(system_template_dict.keys())

# model utk table

# model utk fields/columns


# preset location
preset_directories = [
    'C:',
    'C:\\src',
    'C:\\tmp',
    'C:\\tmp\\deleteme',
    'C:\\verwijderen\\hapus',
    'C:\\work',
    'C:\\work\\github',
    'C:\\work\\github\\go',
    'C:\\work\\github\\java',
    'C:\\work\\github\\typescript',
    'C:\\Users\\usef\\Downloads',
    'C:\\Users\\usef\\Documents',
]

default_websites = [
    'https://translate.google.com/',
    'https://github.com/PacktPublishing/',

    'https://myflixer.pw/country/gb?page=137',
    'https://myflixer.pw/genre/horror?page=150',
    'https://myflixer.pw/cast/martin-landau',
    'https://myflixer.pw/cast/val-kilmer?page=3',
    'https://myflixer.pw/movie/the-river-157',

    'https://myflixer.pw/movie/deep-in-the-darkness-54879',
    'https://myflixer.pw/movie/devil-in-the-dark-56363',
    'https://myflixer.pw/movie/the-whisperer-in-darkness-56099',

    'http://m4ufree.life/search/danielle-ouimet-m4ufree.html',
    'https://www.google.com/search?q=best+vampire+movies',
    'https://www.reddit.com/r/Python',
]


bahasa = [
    'akka',
    'algods',
    'android',
    'angular',
    'aspnetcore',
    'bahasa',
    'buku',
    'bun',
    'compete',
    'cppweb',
    'crack',
    'data',
    'database',
    'deno',
    'devops',
    'django',
    'fastapi',
    'fintech',
    'flask',
    'flutter',
    'gawe',
    'goweb',
    'guilang',
    'html_css_js',
    'karya',
    'laravel',
    'mapper',
    'medium',
    'ml',
    'mmm',
    'nest',
    'next',
    'node',
    'parser',
    'pattern',
    'phoenix',
    'proto',
    'rails',
    'react',
    'reactnative',
    'rustweb',
    'scraper',
    'springboot',
    'systems',
    'telco',
    'vscode',
    'vue',
    'workup',
]
