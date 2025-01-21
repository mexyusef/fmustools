# bantu selenium di quick
from schnell.app.dirutils import file_under_tempdir, under_tempdir, joiner
from schnell.app.fileutils import file_write
from schnell.app.fmusutils import run_fmus_for_content
# from schnell.app.printutils import indah3
from schnell.app.stringutils import splitstrip
from schnell.app.printutils import indah4
import re

__TEMPLATE__IMPORTS = """
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as chrome_options
# chrome_options.binary_location = exec1
# chrome_options.headless = True
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")

from selenium.webdriver.firefox.options import Options as ff_options
# ff_options.binary_location = exec1
# ff_options.headless = True

from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

import time
"""

__TEMPLATE_DRIVER_FF = """
gecko_driver = 'c:/work/bin/geckodriver.exe'
ff_options = webdriver.FirefoxOptions() # ini nebak
# ff_options.headless = True
# ff_options.add_argument("--headless")
# ff_options.add_argument("--incognito")
driver1 = webdriver.Firefox(executable_path=gecko_driver, options=ff_options)
"""

__TEMPLATE_DRIVER_CHR = """
chrome_driver = 'c:/work/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
# https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec/53040904#53040904
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#import requests
#user_agent = requests.get('https://httpbin.org/user-agent').json()['user-agent']
#chrome_options.add_argument(f'user-agent={user_agent}')

driver1 = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
"""

__TEMPLATE_START = f"""
{__TEMPLATE__IMPORTS}

{__TEMPLATE_DRIVER_CHR}

driver1.get('__URL__')
driver1.maximize_window()

__OPERATIONS__

"""

__TEMPLATE_SELENA_FMUS = """
__PRC__TEMP__PRC__/__PROJECTNAME__,d
	$* python __FILENAME__
"""

first = {
	'nop': 'nop',
	'ec': 'ec',
	'cls': 'byclass',
	'css': 'bycss',
	'id': 'byid',
	'link': 'bylinktext',
	'name': 'byname',
	'part': 'bypartiallinktext',
	'tag': 'bytag',
	'xp': 'byxpath',
}

second = {
	'txt': ['text', '.text'],
	# bisa tambahkan [0] etc utk ambil item #1
	# sblm split bisa removeprefix atau removesuffix
	'ws': ['textsplitspace', '.text.strip().split(maxsplit=1)'],
	# bisa tambahkan [0] etc utk ambil item #1
	'line': ['textsplitline', '.text.strip().splitlines(maxsplit=1)'],
	'ihtml': ['innerhtml', '.get_attribute("innerHTML")'],
	'ohtml': ['outerhtml', '.get_attribute("outerHTML")'],
	'itxt': ['innertext', '.get_attribute("innerText")'],
	'txtc': ['textcontent', '.get_attribute("textContent")'],
	'c': ['click', '.click()'],
	'sk': ['sendkey', '.send_keys(__KEYS__)'],
	'scy': ['scrolly', '.execute_script("window.scrollTo(0, __TINGGI_SCROLL__)")'],
	'sc': ['scoll', '.execute_script("window.scrollTo(0, document.body.scrollHeight);")'],
	'sub': ['submit', '.submit()'],
	'q': ['quit', '.quit()'],
	'ps': ['pagesource', '''pagesource := __DRIVERNAME__.page_source.encode("utf-8")
	\nfmt.Println(pagesource)
	'''],
	'wi': ['wait_implicit', '''__DRIVERNAME__.implicitly_wait(__LAMATUNGGU__)'''],
	'wv': ['wait_visible', '''WebDriverWait(__DRIVERNAME__, __LAMATUNGGU__).until(
		EC.visibility_of_element_located((__BYTYPE__, '__BYVALUE__'))
	)
	'''],
	'wt': ['wait_textpresent', '''WebDriverWait(__DRIVERNAME__, __LAMATUNGGU__).until(
		EC.text_to_be_present_in_element((__BYTYPE__, '__BYVALUE__'), '__BYTEXT__')
	)
	'''],
	'wc': ['wait_clickable', '''WebDriverWait(__DRIVERNAME__, __LAMATUNGGU__).until(
		EC.element_to_be_clickable((__BYTYPE__, '__BYVALUE__'))
	)
	'''],
}

third = {
	'bs': 'Keys.BACKSPACE',
	'end': 'Keys.END',
	'home': 'Keys.HOME',
	'c': 'Keys.CONTROL',
	'cd': 'Keys.CONTROL + "d"',
	'ct': 'Keys.CONTROL + "t"',
}

jenismap = {
	'cls': 'By.CLASSNAME',
	'css': 'By.CSS_SELECTOR',
	'id': 'By.ID',
	'lnk': 'By.LINK_TEXT',
	'nm': 'By.NAME',
	'pln': 'By.PARTIAL_LINK_TEXT',
	'tag': 'By.TAG_NAME',
	'xp': 'By.XPATH',
}

url_map = {
	'up1'	: 'https://www.upwork.com/nx/jobs/search/?q=python&sort=recency',
	'up2' 	: 'https://www.upwork.com/nx/jobs/search/?q=python&sort=recency&page=2',
}

def selena(code):
	"""
	/sel>config|find|oper|find|oper|...|url
	contoh config:
	gunakan ff atau chrome
	headless atau tidak
	ff, chr, hless

	find: (ada 8 utk sekarang)
		By.CLASS_NAME
		By.CSS_SELECTOR
		By.ID
		By.LINK_TEXT
		By.NAME
		By.PARTIAL_LINK_TEXT
		By.TAG_NAME
		By.XPATH
		kita sebut saja: cls, css, id, lnk, nm, pln, tag, xp = ...
	oper: (ada 10 utk sekarang)
		.text
		.text split whitespaces, get # item, strip all items
		.text split lines, get # item, strip all items     
		.get_attribute('innerHTML')
		.get_attribute('outerHTML')
		.get_attribute('innerText')
		.get_attribute('textContent')
		.click()
		.send_keys(...)
		.submit()
		kita sebut saja, txt, ws#, line#, ithml, ohtml, itxt, txtc, c, sk, sub

	juga perlu:
	wait until voel: visibility of element located, by xpath, css-selector, class-name...
		(By, value dari by)
	ada berbagai wait...ini termasuk dlm "oper" dg "find"/elem = ec atau driver.
		voel, ini butuh locator dg type-value
		implicit
		text_to_be_present_in_element, ini butuh locator dg type-value
		element_to_be_clickable, ini jg butuh locatr dg type-value

	bentuk:
	css=span.normal.ng-binding/txt
	/
	css=span.date.ng-binding/txt
	/
	...
	UPD:
	bikin shortcut dari: config|...|url
	menjadi cuma:
	fm//sel>url
	"""
	if '|' not in code or code.startswith('http'):
		code = '|nop/wi|' + code
	config, rest = code.split('|',1)
	findopers, url = rest.rsplit('|',1)
	url = url_map.get(url, url)

	if not url.startswith('http'):
		# coba cek
		m = re.search(r'^up(?P<pageno>\d+)', url)
		if m:
			url = 'https://www.upwork.com/nx/jobs/search/?q=python&sort=recency&page=' + m.group('pageno')
	elif url == 'up':
		url = 'https://www.upwork.com/nx/jobs/search/?q=python&sort=recency'
	operations = []
	drivername = 'driver1'
	lamatunggu = '30'
	kembali = __TEMPLATE_START
	__PROJECTNAME__ = 'selena'

	if findopers and url:
		pecah = findopers.split('/')
		for i in range(0, len(pecah), 2):
			harap, kirim = pecah[i].strip(), pecah[i+1].strip()
			# harap adlh operasi spt nop, find_element By.*
			# kirim adlh text, get_attribute, send_keys, dst

			# indah4(f'''{url}
			# harap   = [{harap}]
			# kirim   = [{kirim}]
			# findopers       = {findopers}
			# len findopers   = {len(findopers)}
			# ''', warna='green')

			oper = ''
			if harap == 'nop' or harap.startswith('css') or harap.startswith('xp') or harap.startswith('cls') or harap.startswith('id') or harap.startswith('tag') or harap.startswith('name') or harap.startswith('link') or harap.startswith('part'):
				info = f'{harap}|{kirim}:'
				if kirim in second or kirim.startswith('sk=') or kirim.startswith('wc') or kirim.startswith('wt') or kirim.startswith('wv'):
					if kirim in second:
						# c, sub, ...
						getter = second[kirim][1]
					elif kirim.startswith('sk='):
						getter = second['sk'][1]
					elif kirim.startswith('wc='):
						getter = second['wc'][1]
					elif kirim.startswith('wt='):
						getter = second['wt'][1]
					elif kirim.startswith('wv='):
						getter = second['wv'][1]

					if harap != 'nop':
						jenis, nilai = splitstrip(harap, '=')

					if kirim in ['txt', 'itxt', 'txtc', 'ihtml', 'ohtml', 'q', 'c', 'sub', 'ws', 'line']:						
						oper = f'for elem in __DRIVERNAME__.find_elements({jenismap[jenis]}, "{nilai}"):'
						if kirim in ['c', 'sub', 'q']:
							oper += '\n\t' + f'elem{getter}'
						else:
							oper += '\n\t' + f'print("{info}", elem{getter})'
					elif kirim.startswith('sk='):
						'''
						css=.../sk=sometext
						'''
						_, kunci = kirim.split('=')
						kunci = third.get(kunci, kunci)
						getter = getter.replace('__KEYS__', kunci)
						# indah4(f'''sk
						# getter: {getter}
						# kunci: {kunci}
						# ''', warna='yellow')
						oper = f'for elem in __DRIVERNAME__.find_elements({jenismap[jenis]}, "{nilai}"):'
						oper += '\n\t' + f'print("{info}", elem{getter})'                    
					elif kirim.startswith('wt=') or kirim.startswith('wv=') or kirim.startswith('wc='):
						# nop/wt=css=span.normal.ng-binding=text...
						# harap/kirim
						bytext = ''
						if kirim.startswith('wt='):
							_, bytype, byvalue, bytext = splitstrip(kirim, '=')
						else:
							_, bytype, byvalue = splitstrip(kirim, '=')
						bytype = jenismap.get(bytype, bytype)
						# indah4(f'''wc/wt/wv
						# getter: {getter}
						# bytype: {bytype}
						# byvalue: {byvalue}
						# bytext: {bytext}
						# ''', warna='yellow')
						oper = getter.replace('__BYTYPE__', bytype).replace('__BYVALUE__', byvalue).replace('__BYTEXT__', bytext)
					elif kirim in ['wi', 'ps']:
						oper = getter

			if oper:
				operations.append(oper)
	
	# print('[selena] operations:', operations)
	if operations:
		res = '\n\n'.join(operations)
		
		kembali = kembali.replace('__URL__', url)
		kembali = kembali.replace('__OPERATIONS__', res)
		kembali = kembali.replace('__DRIVERNAME__', drivername).replace('__LAMATUNGGU__', lamatunggu)

	indah4(f'''{kembali}
	''', warna='white')

	projdir = under_tempdir(__PROJECTNAME__)
	filename = 'main.py'
	filepath = joiner(projdir, filename)
	file_write(filepath, kembali)
	fmuscontent = __TEMPLATE_SELENA_FMUS.replace('__FILENAME__', filename).replace('__PROJECTNAME__', __PROJECTNAME__)
	run_fmus_for_content(fmuscontent)
	
