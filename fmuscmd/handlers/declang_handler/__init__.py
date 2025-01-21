from .declang_new import handle_declang
from schnell.app.clipboardutils import trycopy, trypaste
from schnell.app.dirutils import isfile
from schnell.app.fileutils import file_content
from schnell.app.printutils import indah4
from schnell.creator.declarative.mapper import (
	elem_mapper,
	attr_mapper,
	cdata_mapper,
	value_mapper)


def add_mapper_keys(toadddict, which=0):
	"""

	0 = element/tag
	1 = attribute
	2 = cdata/text
	3 = value dari attribute
	"""
	kembali = None
	indah4(f'add_mapper_keys, which: {which}, toadddict={toadddict}', warna='magenta')
	if which in [0, 'e', 'elem']:
		elem_mapper.update(toadddict)
		kembali = elem_mapper
		indah4('elem add mapper now', warna='yellow')
	elif which in [1, 'a', 'attr']:
		attr_mapper.update(toadddict)
		kembali = attr_mapper
		indah4('attr add mapper now', warna='yellow')
	elif which in [2, 'c', 'cdata']:
		cdata_mapper.update(toadddict)
		kembali = cdata_mapper
		indah4('cdata add mapper now', warna='yellow')
	elif which in [3, 'v', 'value']:
		value_mapper.update(toadddict)
		kembali = value_mapper
		indah4('value add mapper now', warna='yellow')
	return kembali


def load_from_ini(content, which=0):
	baris = [line for line in content.splitlines() if line.count('=')==1]
	if baris:
		dictify = {}
		for b in baris:
			k,v = b.split('=',1)
			dictify[k]=v

		return add_mapper_keys(dictify, which=which)

	return None


def load_from_ini_file(filepath, which=0):
	if isfile(filepath):
		load_from_ini(file_content(filepath), which=which)
		indah4(f'{filepath} reload...', warna='green')
	else:
		indah4(f'{filepath} not found', warna='red')


def load_from_clipboard(which=0):
	load_from_ini(trypaste(), which=which)
	indah4('clipboard reload...', warna='green')


def reset_mapper():
	global elem_mapper, attr_mapper, cdata_mapper, value_mapper
	elem_mapper = {}
	attr_mapper = {}
	cdata_mapper = {}
	value_mapper = {}
