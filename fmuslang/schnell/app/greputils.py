import os, re
from .appconfig import programming_data
from .dirutils import normy
from .utils import perintahsp_outerr_as_shell, platform


GREP_COMMAND = 'grep'
if platform() in ['win32', 'windows']:
	# GREP_COMMAND = 'wsl grep'
	GREP_COMMAND = 'C:/work/usr/local/wbin/grep.exe'


def curdir_grep(basedir, pattern, case_sensitive=False, context=0, before=0, after=0, capture=False, no_color=False):
	context_opts = ''
	if before:
		context_opts = f"-B {before}"
	if after:
		context_opts += f"{' ' if context_opts else ''}-A {after}"
	if context:
		context_opts = f"-C {context}"
	# print('A:', after, 'B:', before, 'C:', context, '=>', context_opts)
	basedir = normy(basedir)
	# basedir = basedir.replace('\\', '/')
	print(f'''[greputils]
	basedir = {basedir}
	''')
	skip_binary = "-I"
	color_opt = '' if no_color else ' --color=always -s'
	main_opts = f"-n {skip_binary}{color_opt}" # -s silent jk grep dir
	if ' ' in basedir:
		basedir = f'"{basedir}"'
	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_CASESENSITIVE_GREP"]:
		case_sensitive = True
	all_opts = f'{GREP_COMMAND} {"" if case_sensitive else "-i"} {main_opts} {context_opts} -e "{pattern}" {basedir}/*'
	# os.system('pwd')
	# print('curdir {GREP_COMMAND}', pattern, '->', all_opts)  
	if capture:
		return perintahsp_outerr_as_shell(all_opts)
	else:
		os.system(all_opts)
	return None


def system_grep(basedir,
	pattern,
	case_sensitive=False,
	context=0,
	before=0,
	after=0,
	capture=False,
	no_color=False):
	context_opts = ''
	if before:
		context_opts = f"-B {before}"
	if after:
		context_opts += f"{' ' if context_opts else ''}-A {after}"
	if context:
		context_opts = f"-C {context}"
	# print('A:', after, 'B:', before, 'C:', context, '=>', context_opts)
	basedir = normy(basedir)
	# basedir = basedir.replace('\\', '/')
	print(f'''[greputils]
	basedir = {basedir}
	''')
	skip_binary = "-I"
	color_opt = '' if no_color else ' --color=always'
	if platform() in ['win32', 'windows', 'desktop']:
		color_opt = ''
	main_opts = f"-n {skip_binary}{color_opt} -r"
	if ' ' in basedir:
		basedir = f'"{basedir}"'
	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_CASESENSITIVE_GREP"]:
		case_sensitive = True
	all_opts = f'{GREP_COMMAND} {"" if case_sensitive else "-i"} {main_opts} {context_opts} -e "{pattern}" {basedir}'
	# print(f'{GREP_COMMAND} system:', all_opts)
	if capture:
		return perintahsp_outerr_as_shell(all_opts)
	else:
		os.system(all_opts)
	return None


def system_grep_limitchars(basedir,
	pattern, 
	limit=10, 
	case_sensitive=False, 
	capture=False,
	no_color=False):
	"""
	N=10; grep -roP ".{0,$N}\Wactor.{0,$N}" .

	N=limit; grep -roP ".{0,$N}" +pattern+ ".{0,$N}" basedir
	-P adlh perl style dg .{0,$bilangan}

	di sini kita gunakan
	grep -i -I --color=always -ro -P ".{0,n}pattern.{0,n}" basedir
	"""
	skip_binary = "-I"
	color_opt = '' if no_color else ' --color=always'
	if platform() in ['win32', 'windows', 'desktop']:
		color_opt = ''
	main_opts = f"{skip_binary}{color_opt} -ro"
	# main_opts = f"{skip_binary} --color=always -ro"
	if ' ' in basedir:
		basedir = f'"{basedir}"'
	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_CASESENSITIVE_GREP"]:
		case_sensitive = True
	all_opts = f'{GREP_COMMAND} {"" if case_sensitive else "-i"} {main_opts} -P ".{{0,{limit}}}{pattern}.{{0,{limit}}}" {basedir}'
	# print(f'{GREP_COMMAND} limit:', all_opts)
	if capture:
		return perintahsp_outerr_as_shell(all_opts)
	else:
		os.system(all_opts)
	return None


def system_find(basedir, pattern, opts=None, capture=False):
	"""
	kita tambah sendiri *cari*
	"""
	case_sensitive = 'name'
	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_WMC_CASESENSITIVE_GREP"]:
		case_sensitive = 'iname'
	all_opts = f'find {basedir} -{case_sensitive} "*{pattern}*"'
	if capture:
		return perintahsp_outerr_as_shell(all_opts)
	else:
		os.system(all_opts)
	return None


def pattern_search(filepath, code):
	"""
	"""
	from .fileutils import file_lines
	all_lines = file_lines(filepath)

	# antipatterns = [item.replace('-','',1) for item in code if re.match(r'^-[\w\d]+', item)]
	# patterns = [item for item in code if not re.match(r'^-[\w\d]+', item)]

	# pre_selected = filter(lambda baris: all(
	# 	[item.lower() in baris.lower() for item in patterns]), all_lines)
	# selected = filter(lambda baris: all(
	# 	[item.lower() not in baris.lower() for item in antipatterns]), pre_selected)
	# selected = list(selected)
	# selected = '\n'.join(selected)
	# return selected
	return pattern_search_list(all_lines, code)


def pattern_search_list_keep_case(all_lines, code, aslist=False, send_indices=False):
	"""
	search code yg berisi + dan - dari dalam list all_lines
	[satu_pat1,dua_pat2,tiga_pat3,empat_pat4,lima_pat5]
	+pat1
	-pat2
	+pat3
	-pat4
	"""
	if isinstance(code, str):
		code = [item.strip() for item in code.split()]

	all_lines_with_indices = [(i, item) for i,item in enumerate(all_lines)]
	all_lines_with_indices_lower = [(i, item.lower()) for i,item in enumerate(all_lines)]

	# code di sini sudah jadi list of search terms
	antipatterns = [item.replace('-','',1) for item in code if re.match(r'^-[\w\d]+', item)]
	patterns = [item for item in code if not re.match(r'^-[\w\d]+', item)]

	# step 1: ambil dulu yg patterns (+) dari haystack all_lines
	pre_selected = filter(lambda baris: all(
		[item.lower() in baris.lower() for item in patterns]), all_lines)
	# step 2: filter out yg anti (-)
	selected = filter(lambda baris: all(
		[item.lower() not in baris.lower() for item in antipatterns]), pre_selected)
	# filter -> list
	selected = list(selected)
	selected_indices = [i for (i,t) in all_lines_with_indices_lower for u in selected if t==u]
	if send_indices:
		selected = [i for (i,t) in all_lines_with_indices for j in selected_indices if i==j]
	else:
		selected = [t for (i,t) in all_lines_with_indices for j in selected_indices if i==j]
	# return selected as list atau stringified
	if aslist:
		return selected

	# cek jk item int: start
	# print('before sending:', selected, 'input:', all_lines, 'code:', code)
	# if all([isinstance(i,int) for i in selected]):
	# 	# jika items adlh ints, gak bisa \n.join, hrs di str() kan dulu
	# 	return '\n'.join([str(i) for i in selected])
	# dipanggil dg last_index = pattern_search_list_keep_case(P.getAllTitles(), cari_judul, send_indices=True)
	# di C:\Users\usef\work\sidoarjo\schnell\app\autoutils.py:get_inwindowtitles
	if len(selected)==1 and isinstance(selected[0], int):
		return selected[0]
	# cek jk item int: end

	selected = '\n'.join(selected)
	return selected


def pattern_search_list(all_lines, code, aslist=False):
	"""
	search code yg berisi + dan - dari dalam list all_lines
	[satu_pat1,dua_pat2,tiga_pat3,empat_pat4,lima_pat5]
	+pat1
	-pat2
	+pat3
	-pat4
	"""
	if isinstance(code, str):
		code = [item.strip() for item in code.split()]

	# code di sini sudah jadi list of search terms
	antipatterns = [item.replace('-','',1) for item in code if re.match(r'^-[\w\d]+', item)]
	patterns = [item for item in code if not re.match(r'^-[\w\d]+', item)]

	# step 1: ambil dulu yg patterns (+) dari haystack all_lines
	pre_selected = filter(lambda baris: all(
		[item.lower() in baris.lower() for item in patterns]), all_lines)
	# step 2: filter out yg anti (-)
	selected = filter(lambda baris: all(
		[item.lower() not in baris.lower() for item in antipatterns]), pre_selected)
	# filter -> list
	selected = list(selected)
	# return selected as list atau stringified
	if aslist:
		return selected
	selected = '\n'.join(selected)
	return selected


def pattern_search_string(content, code, aslist=False):
	"""
	search code yg berisi + dan - dari dalam string content terpisah spasi
	"""
	return pattern_search_list(content.splitlines(), code, aslist=aslist)

# It looks like you've implemented a function in Python for searching patterns in a list of strings. 
# The pattern you're searching for includes terms that should be included and excluded. 
# Your code seems to be functional, but there are a few improvements that can be made for clarity and efficiency.

# Here's an enhanced version of your code with some improvements:

# ```python
# import re

def pattern_search_list_refactor(list_source, pattern_code, aslist=True):
	if isinstance(pattern_code, str):
		pattern_code = pattern_code.split()

	antipatterns = [item[1:] for item in pattern_code if item.startswith('-')]
	patterns = [item for item in pattern_code if not item.startswith('-')]

	pre_selected = [baris for baris in list_source if all(item.lower() in baris.lower() for item in patterns)]
	selected = [baris for baris in pre_selected if all(item.lower() not in baris.lower() for item in antipatterns)]

	if aslist:
		return selected

	selected = '\n'.join(selected)
	return selected

def pattern_search_string_refactor(string_source, pattern_code, aslist=False):
	return pattern_search_list_refactor(string_source.splitlines(), pattern_code, aslist=aslist)
# ```

# In this version, I made the following improvements:

# 1. **Removed unnecessary regular expressions:** 
# You can achieve the same functionality without using regular expressions, making the code simpler.

# 2. **Simplified pattern and antipattern extraction:** 
# The code now directly checks whether a term starts with '-' to identify antipatterns, making it more intuitive.

# 3. **List comprehensions:** I replaced the filter functions with list comprehensions for readability.

# 4. **Code readability:** Variable names have been kept meaningful for better understanding.

# Remember that the `pattern_search_list` function takes a list of strings as input and a pattern code (as a list of strings). 
# It then filters the input list based on the inclusion and exclusion criteria specified in the pattern code. 
# The `pattern_search_string` function splits the input string into lines and calls the `pattern_search_list` function.


def pattern_search_from_string_to_list(list_source, pattern_code):
	pattern_code = pattern_code.split()
	antipatterns = [item[1:] for item in pattern_code if item.startswith('-')]
	patterns = [item for item in pattern_code if not item.startswith('-')]

	pre_selected = [baris for baris in list_source if all(item.lower() in baris.lower() for item in patterns)]
	selected = [baris for baris in pre_selected if all(item.lower() not in baris.lower() for item in antipatterns)]

	return selected
