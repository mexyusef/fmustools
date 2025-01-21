import re
from .greputils import (
	system_grep_limitchars,
	system_grep,
)
from .utils import (
	env_int,
	perintah,
	perintahsp_outerr_as_shell,
)

# https://github.com/search?l=Python&q=fuzzy+search&type=Repositories
# https://github.com/topics/fuzzy-search
# https://github.com/seatgeek/thefuzz
# https://github.com/taleinat/fuzzysearch

def content_search(searchfolder,
	pattern,
	case_sensitive=False,
	horizontal_context_limit=0,
	before=0,
	after=0,
	suppress_longfoldername=True,
	no_color=False):
	"""
	kembalian, err = content_search(basefolder, pattern, case_sensitive=True)

	system_grep(basedir, pattern, case_sensitive=False, context=0, before=0, after=0, capture=False):
	system_grep_limitchars(basedir, pattern, limit=10, case_sensitive=False, capture=False):

	horizontal_context_limit, misal nilai 10
	maksudnya mungkin /terutama
	kalau kita terutama sekali makan ayam
		 <-----|       |-----> sebanyak 10 chars ke kiri dan kanan
	krn "context" itu "vertical"

	capture: kembalikan string output, krn mau kita lempar ke vscode
	"""
	# mmm_zau_folder
	if horizontal_context_limit:
		out, err = system_grep_limitchars(searchfolder, pattern, case_sensitive=case_sensitive, limit=horizontal_context_limit, capture=True, no_color=no_color)
	else:
		out, err = system_grep(searchfolder, pattern, case_sensitive=case_sensitive, capture=True, no_color=no_color, before=before, after=after)

	if suppress_longfoldername and out:
		out = out.replace(searchfolder, '')

	return out, err


def word_content_search(basefolder, code):
	"""
	* menyatakan case sensitive (dari default insensitive)
	angka/cari          -> limit chars di sekitar found
	angka,angka/cari    -> context before/after

	cari
	*cari-case
	10/cari		    grep limit: grep  -I -ro -P ".{0,10}naik.{0,10}" ..
	10*/cari-case	grep limit: grep  -I -ro -P ".{0,10}naik.{0,10}" ..
	3,0/cari		before=3 lines, after=0 lines
	"""
	if code.startswith('*'):
		'''
		*cari-case-sensitive
		'''
		pattern = code.removeprefix('*').strip()
		kembalian, err = content_search(basefolder, pattern, case_sensitive=True)
	elif re.match(r'^(\d+)/(.*)', code):
		'''
		10/cari			grep limit: grep  -I -ro -P ".{0,10}naik.{0,10}" ..
		'''
		m = re.match(r'^/(\d+)/(.*)', code)
		context = int(m.group(1))
		pattern = m.group(2)
		kembalian, err = content_search(basefolder, pattern, case_sensitive=False, horizontal_context_limit=context)
	elif re.match(r'^(\d+)\*/(.*)', code):
		'''
		10*/cari-case		grep limit: grep  -I -ro -P ".{0,10}naik.{0,10}" ..
		'''
		m = re.match(r'^(\d+)\*/(.*)', code)
		context = int(m.group(1))
		pattern = m.group(2)
		kembalian, err = content_search(basefolder, pattern, case_sensitive=True, horizontal_context_limit=context)
	elif re.match(r'^(\d+),(\d+)/(.*)', code):
		'''
		3,0/cari			before=3 lines, after=0 lines
		'''
		m = re.match(r'^/(\d+),(\d+)/(.*)', code)
		before = int(m.group(1))
		after = int(m.group(2))
		pattern = m.group(3)
		kembalian, err = content_search(basefolder, pattern, case_sensitive=True, before=before, after=after)
	else:
		'''
		cari
		default gak sensitive, context default 0, no limit horizontal (bisa rame)
		'''
		pattern = code.strip()
		kembalian, err = content_search(basefolder, pattern)

	if not kembalian and err:
		kembalian = err

	return kembalian


def system_find(basedir, pattern, capture=False, find_cmd='find', case_insensitive=True, suppress_longfoldername=True,):
	"""
	find filename dg pola: *cari*
	"""
	case_sensitive = 'name'
	if case_insensitive:
		case_sensitive = 'iname'
	all_opts = f'{find_cmd} {basedir} -{case_sensitive} "*{pattern}*"'
	if capture:
		kembali, err = perintahsp_outerr_as_shell(all_opts)
		if err:
			kembali = err
		elif suppress_longfoldername and kembali:
			kembali = kembali.replace(basedir + '/', '') # hati2, hardcode /
		return kembali
	else:
		perintah(all_opts)
	return None


def pattern_search_list(all_lines, code, aslist=False):
	from .greputils import pattern_search_list
	return pattern_search_list(all_lines=all_lines, code=code, aslist=aslist)

