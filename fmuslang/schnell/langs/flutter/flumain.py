import json, os, pyperclip, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
# schnell = os.path.join(os.pardir, os.pardir, 'app')
sidoarjodir = os.path.join(os.pardir, os.pardir, os.pardir)
sys.path += [sidoarjodir]

from schnell.app.dirutils import joiner, ayah
from schnell.app.fileutils import file_content
from schnell.app.printutils import print_copy

delimiter  = '###'
codes = joiner(ayah(__file__, 1), 'codes.txt')
isifile = file_content(codes)
codelist = [item.strip() for item in isifile.split(delimiter) if item.strip()]

# print(codelist)

def jsonize(daftar):
	if len(daftar) == 1:
		print_copy(daftar[0])
	elif len(daftar) > 1:
		print_copy(json.dumps(daftar, indent=4))

def saring(daftar, cari):
	return [item for item in daftar if cari.lower() in item.lower()]

def buang(daftar, cari):
	return [item for item in daftar if cari.lower() not in item.lower()]

def process_language(code):
	if ' ' in code:
		codes = code.split()
		if codes:
			negatives_minus = [item for item in codes if item.startswith('-')]
			negatives = [item.replace('-','',1) for item in negatives_minus]
			positives = list(set(codes) - set(negatives_minus))
			# print('codes:', codes)
			# print('pos:', positives)
			# print('neg:', negatives)
			terakhir = codelist
			# print('#1:', terakhir)
			for kode in positives:
				terakhir = saring(terakhir, kode)
			# print('#2:', terakhir)
			for kode in negatives:
				terakhir = buang(terakhir, kode)
			# print('#3:', terakhir)
			if terakhir:
				jsonize(terakhir)
	else:
		temu = [item for item in codelist if code.lower() in item.lower()]
		jsonize(temu)

def repl():
	code = 1
	while code != 'x':
		try:
			code = input('flumain>> ')
			code = code.strip()
			if code == 'help':
				print('no help')
			elif code == 'L':
				global codelist, isifile, codes
				isifile = file_content(codes)
				codelist = [item.strip() for item in isifile.split(delimiter) if item.strip()]
			elif code != '' and code != 'x':
				process_language(code)
		except EOFError as eof:
			print('Ctrl+D? Exiting...', eof)
			break
		except Exception as err:
			print(err)

if __name__ == '__main__':
	repl()
