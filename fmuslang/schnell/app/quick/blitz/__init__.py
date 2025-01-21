
"""
kita bikin spt apa:
b>cpp/operasi|kode
operasi:
	- cmake onefiler
		b>cpp/cm1|source.cpp
		b>cpp/cm1|source.cpp,output.exe
		- onefiler: bikin cmake cepat, input nama file cpp (atau specify)
"""

from creator.helper import CODE
from app.dirutils import joinhere, sfiles
from app.fmusutils import run_fmus_from_coordinator, get_rootnode
from app.printutils import indah4, print_list_warna
from app.quick.blitz.py import Coordinator as py_coordinator
from app.utils import perintah_shell, trycopy
from app.fakerutils import getfakers
from app.quick.blitz.a import Coordinator as all_coordinator
from app.quick.blitz.cpp import Coordinator as cpp_coordinator
from app.quick.blitz.do import Coordinator as devops_coordinator
from app.quick.blitz.go import Coordinator as go_coordinator
from app.quick.blitz.goog import Coordinator as google_coordinator
from app.quick.blitz.hc import Coordinator as html_css_coordinator
from app.quick.blitz.java import Coordinator as java_coordinator
from app.quick.blitz.js import Coordinator as js_coordinator
from app.quick.blitz.k import Coordinator as karya_coordinator
from app.quick.blitz.m import Coordinator as mobile_coordinator
from app.quick.blitz.ml import Coordinator as machinelearning_datascience_coordinator
from app.quick.blitz.n import Coordinator as n_coordinator
from app.quick.blitz.pr import Coordinator as parser_coordinator
from app.quick.blitz.r import Coordinator as react_coordinator
from app.quick.blitz.rs import Coordinator as rust_coordinator
from app.quick.blitz.tdd import Coordinator as tdd_coordinator
from app.quick.blitz.ts import Coordinator as ts_coordinator


language_to_handler = {
	'a'			: all_coordinator,
	'all'		: all_coordinator,
	'cpp'		: cpp_coordinator,
	'do'		: devops_coordinator,
	'go'		: go_coordinator,
	'goog'		: google_coordinator,
	'hc'		: html_css_coordinator,
	'java'		: java_coordinator,
	'js'		: js_coordinator,
	'k'			: karya_coordinator,
	'm'			: mobile_coordinator,
	'ml'		: machinelearning_datascience_coordinator,
	'n'			: n_coordinator,
	'pr'		: parser_coordinator,
	'py'		: py_coordinator,
	'r'			: react_coordinator,
	'react'		: react_coordinator,
	'rs'		: rust_coordinator,
	'tdd'		: tdd_coordinator,
	'ts'		: ts_coordinator,
}

blog_header = """---
title: 
date: __DATE
description: 
tag: 
author: Yusef
---

content
"""


def blog(code):
	"""
	b>blog/pages
	b>blog/pages=judul-baru
	u -e"/b>blog/pages=stream-foreach"
	"""
	filename = ''
	if '=' in code:
		_, filename = code.split('=',1)
	if not filename:
		indah4('''Masukkan filename:''', warna='green', newline=False)
		filename = input(' ')
	if not filename:
		# u -e"/b>blog/pages"
		print_list_warna(sfiles(joinhere(__file__, '../dahsyat/nxblog/pages')))
		return
	filename += '.md'
	targetdir = joinhere(__file__, '../dahsyat/nxblog/pages', filename)
	
	kwfuncargs = {'end_date':'now', 'start_date':'-5y'} # 2017, 2018, 2019, 2020, 2021, 2022
	get_date = getfakers('date_between', kwfuncargs=kwfuncargs)
	header = blog_header.replace('__DATE', get_date.strftime('%Y/%m/%d'))
	trycopy(header)

	indah4(f'''memproses file: {targetdir}
	in clipboard:
	{header}
		''', warna='white')	
	perintah_shell(f'{CODE} {targetdir}')


def blitz(request):
	"""
	/b> language/filename|csvcode
	"""
	csvcode = '[/dummy]{@Dummy}dummy,s' # dummy

	# indah4('blitz!', warna='white')

	if not request:
		return

	language, fmus_filename = request.split('/',1) # b>py/fa1.fmus

	if not language or not fmus_filename:
		return

	if language == 'blog' and fmus_filename.startswith('pages'):
		blog(fmus_filename)
		return

	if '|' in fmus_filename:
		fmus_filename, csvcode = fmus_filename.split('|',1)

	if not fmus_filename.endswith('.fmus') and not '.' in fmus_filename:
		'''
		bisa gunakan filename.mk selain filename.fmus dan filename
		'''
		fmus_filename += '.fmus'

	if language in language_to_handler:
		RootNode = get_rootnode(csvcode)
		run_fmus_from_coordinator(language_to_handler[language], [RootNode, fmus_filename])
