import re
from ..autoutils import alert, prompt
try:
	import pyperclip
except ImportError as err:
	pass

import os
import tempfile
from PIL import Image
import pyperclip
import win32clipboard
import io
import ctypes

from schnell.app.stringutils import (
	sort_and_remove_duplicates,
	replace_single_backslash_with_double,
	replace_double_backslash_with_single,
	replace_single_quote_with_double,
	replace_double_quote_with_single,
	replace_slash_with_backslash,
	replace_backslash_with_slash,
	prefix_suffix_multiline,
	tabify_content_tab,
	tabify_content_space,
)


def send_to_clipboard(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def image_to_clipboard4(image_path):
	# https://stackoverflow.com/questions/66845295/copy-image-to-clipboard-and-preserve-transparency
	import win32clipboard as clp
	# file_path = 'test.png'
	clp.OpenClipboard()
	clp.EmptyClipboard()
	# This works for Discord, but not for Paint.NET:
	wide_path = os.path.abspath(image_path).encode('utf-16-le') + b'\0'
	clp.SetClipboardData(clp.RegisterClipboardFormat('FileNameW'), wide_path)
	# This works for Paint.NET, but not for Discord:
	# file = open(image_path, 'rb')
	with open(image_path, 'rb') as file:
		clp.SetClipboardData(clp.RegisterClipboardFormat('image/png'), file.read())
		clp.CloseClipboard()


def image_to_clipboard3(image_path):
	image = Image.open(image_path)
	print('image_to_clipboard3:', image_path)
	# Convert the image to a byte stream
	with io.BytesIO() as buffer:
		image.save(buffer, format='PNG')
		image_bytes = buffer.getvalue()
	print('image_to_clipboard3, image_bytes ok')
	# Create a global memory object to hold the image bytes
	global_mem = ctypes.windll.kernel32.GlobalAlloc(0x0040, len(image_bytes))
	global_mem_ptr = ctypes.windll.kernel32.GlobalLock(global_mem)
	ctypes.memmove(global_mem_ptr, image_bytes, len(image_bytes))
	ctypes.windll.kernel32.GlobalUnlock(global_mem)
	print('image_to_clipboard3, ctype init 1/2')
	# Open the clipboard and set the image data
	ctypes.windll.user32.OpenClipboard(None)
	ctypes.windll.user32.EmptyClipboard()
	ctypes.windll.user32.SetClipboardData(17, global_mem)
	ctypes.windll.user32.CloseClipboard()
	print('image_to_clipboard3, ctype init 2/2')
	# Free the global memory object
	ctypes.windll.kernel32.GlobalFree(global_mem)
	print('image_to_clipboard3 END.')


def image_to_clipboard2(image_path):
	image = Image.open(image_path)
	print('image_to_clipboard2:', image_path)
	# Convert the image to a byte stream
	with io.BytesIO() as buffer:
		# image.save(buffer, format='PNG')
		image.convert("RGB").save(buffer, format='PNG')
		# image_bytes = buffer.getvalue()
		image_bytes = buffer.getvalue()[14:]
	print('image_to_clipboard2, image_bytes ok')
	# # Set the clipboard data to the image bytes
	# win32clipboard.OpenClipboard()
	# win32clipboard.EmptyClipboard()
	# win32clipboard.SetClipboardData(win32clipboard.CF_DIB, image_bytes)
	# win32clipboard.CloseClipboard()
	send_to_clipboard(image_bytes)
	print('image_to_clipboard2 END.')


def image_to_clipboard(image_path):
    # create a temporary file to save the image
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, 'clipboard.png')

    # open the image file
    try:
        with Image.open(image_path) as im:
            # convert the image to PNG format and save to temporary file
            im.convert('RGB').save(temp_file_path, 'PNG')
            with open(temp_file_path, 'rb') as f:
                # copy the image data to clipboard
                pyperclip.copy(f.read())
        print(f'{image_path} copied to clipboard')
    except IOError:
        print(f'{image_path} is not an image')


def trycopy(content):
	try:
		pyperclip.copy(content)
	except Exception as err:
		pass


def trypaste():
	try:
		content = pyperclip.paste()
		return content
	except Exception as err:
		return None


def try_copy(content):
	trycopy(content)


def try_paste():
	return trypaste()


def sort_strings(content, joiner='\n'):
	result = sorted(content.splitlines())
	return joiner.join(result)


def replace_string(content, old, new):
	content = content.replace(old, new)
	return content


def replace_keyword(content,
	# replacers,  # \one\two\three
	wieke_prefix='$',
	wieke_capper='^^',
	wiekeplural='^s',
	wiekesingular='^1',
	wiekesingularcap='^c',
	wiekelower='^l',
	wiekeupper='^u',
	# wieke_space='~',
	wieke_space=None,
	replacer_separator='|'):
	r"""
	misal
	const [$01, set$01^^] = useState...
	\monkey
	hasilkan:
	const [monkey, setMonkey] == useState...
	"""
	if not wieke_prefix+'01' in content:
		return content
	
	masuk = prompt(f'Masukkan replacers dipisah dg {replacer_separator}:')

	while not masuk:
		masuk = prompt(f'Masukkan replacers dipisah dg {replacer_separator}:')

	replacers = masuk.split(replacer_separator)
	templates = [wieke_prefix + str(angka).zfill(2) for angka in range(1,len(replacers)+1)]
	for index, wieke in enumerate(replacers):
		# careful: work from "most" to "least"
		content = content.replace(templates[index]+wieke_capper, wieke.capitalize()) # ^^
		content = content.replace(templates[index]+wiekeplural, wieke + 's') # ^s
		content = content.replace(templates[index]+wiekelower, wieke.lower()) # ^l
		content = content.replace(templates[index]+wiekeupper, wieke.upper()) # ^u
		# singular capitalize vs singular, Cat vs cat if input is cats
		content = content.replace(templates[index]+wiekesingularcap, wieke.removesuffix('s').capitalize()) # ^c
		content = content.replace(templates[index]+wiekesingular, wieke.removesuffix('s')) # ^1
		# last only $01
		content = content.replace(templates[index], wieke)
		# expand space di result
		if wieke_space is not None:
			content = content.replace(wieke_space, ' ')
	return content


def replace_input(content,
	input_keyword='__INPUT__',
	replacer_separator='|'):
	r"""
	misal
	ini adalah tulisan berisi __INPUT__ yang akan diganti
	hasilkan:
	ini adalah tulisan berisi <input-user> yang akan diganti
	"""
	jumlah_inputs = content.count(input_keyword)
	if not jumlah_inputs:
		return content
	line_inputs = [item for item in content if input_keyword in item]
	line_inputs = '\n'.join(line_inputs)
	MAXLINES_TAMPILKAN = 10
	prompt_body = content if len(content.splitlines()) <= MAXLINES_TAMPILKAN else line_inputs
	masuk = prompt(f'Masukkan replacers dipisah dg {replacer_separator}:\n\n{prompt_body}')
	replacers = masuk.split(replacer_separator)
	while len(replacers) != jumlah_inputs:
		masuk = prompt(f'Jumlah masukkan replacers {len(replacers)} != {jumlah_inputs}, ulang lagi dipisah dg {replacer_separator}:\n\n{prompt_body}')
		replacers = masuk.split(replacer_separator)

	for i in range(jumlah_inputs):
		content = content.replace(input_keyword, replacers[i], 1)
	return content


def suffix_string(content, suffix='', joiner='\n'):
	result = [baris+suffix for baris in content.splitlines()]
	return joiner.join(result)


def prefix_string(content, prefix='', joiner='\n'):
	if isinstance(prefix, int):
		# misal 5 -> 5, 6, 7, ...
		result = [str(prefix+i)+baris for i,baris in enumerate(content.splitlines())]
	elif prefix.isdigit():
		width = len(prefix)
		iszfill = width>1 and prefix.startswith('0')
		start = int(prefix)
		if iszfill:
			result = [str(start+i).zfill(width)+baris for i,baris in enumerate(content.splitlines())]
		else:
			result = [str(start+i)+baris for i,baris in enumerate(content.splitlines())]
	else:
		result = [prefix+baris for baris in content.splitlines()]
	return joiner.join(result)


def indent_string(content, tab='t', num=1, joiner='\n'):
	"""
	tab = t, digit utk tab dan space*digit
	"""
	tabber = ' '*int(tab)*num if (isinstance(tab, int) or tab.isdigit()) else '\t'*num
	result = [tabber+baris for baris in content.splitlines()]
	return joiner.join(result)


def indent_convert(content: str, source='t', target=2, joiner='\n'):
	if not content:
		return content
	if source == 't':
		source = '\t'
	elif isinstance(source, int):
		source = ' '*source
	if target == 't':
		target = '\t'
	elif isinstance(target, int):
		target = ' '*target
	result = []
	for line in content.splitlines():
		m = re.match(r'^(\s+)(\S.*)+', line)
		if m:
			ubah = m.group(1)
			isi = m.group(2)
			result.append(ubah.replace(source, target) + isi)
		else:
			result.append(line)

	result = joiner.join(result)
	return result


def convert_2_to_4(bariskalimat):
	return indent_convert(bariskalimat, source=2, target=4)


def convert_2_to_t(bariskalimat):
	return indent_convert(bariskalimat, source=2, target='t')


def convert_4_to_2(bariskalimat):
	return indent_convert(bariskalimat, source=4, target=2)


def convert_4_to_t(bariskalimat):
	return indent_convert(bariskalimat, source=4, target='t')


def convert_t_to_2(bariskalimat):
	return indent_convert(bariskalimat, source='t', target=2)


def convert_t_to_4(bariskalimat):
	return indent_convert(bariskalimat, source='t', target=4)


def process_clipboard(request, PEMISAH="$$$"):
	"""
	PEMISAH="|clip|"
	24	PEMISAH 	content
	2t	PEMISAH		content
	42	PEMISAH 	content
	4t	PEMISAH		content
	t2	PEMISAH 	content
	t4	PEMISAH		content
	@	PEMISAH		content
	q21	PEMISAH		content		double quote (") to single quote (')
	q12	PEMISAH		content
	s21	PEMISAH		content		double backslash to single backslash
	s12	PEMISAH		content
	sbs	PEMISAH		content		/ to \\
	bss	PEMISAH		content		\\ to /

	^ lstrip, $ rstrip, ^$ strip, - remove, + add
	^-word
	$-word
	^$-word
	^+
	$+
	^$+

	t=2		tabify dg 2 tab
	s2=2	tabify dg 2*space2
	s4=7	tabify dg 7*space4

	s^... spt atas tapi maintain prefix space
	"""
	content = request
	result = ''
	if not request:
		alert('Masukkan data ke clipboard sblm tekan Enter...')
		content = trypaste()
	elif request.endswith(PEMISAH):  # user provide code spt 2t||, content langsung ambil dari clipboard
		# user bisa 24|| dan content bisa minta dari clipboard
		content = request + trypaste()

	if PEMISAH in content:
		code, content = content.split(PEMISAH, 1)
		code = code.strip()
		content = content.lstrip()
		if code == '24':
			result = convert_2_to_4(content)
		elif code == '2t':
			result = convert_2_to_t(content)
		elif code == '42':
			result = convert_4_to_2(content)
		elif code == '4t':
			result = convert_4_to_t(content)
		elif code == 't2':
			result = convert_t_to_2(content)
		elif code == 't4':
			result = convert_t_to_4(content)
		elif code == '@':  # /clip)@ utk sort
			result = sort_and_remove_duplicates(content)
		elif code.startswith('t='):
			jumlah_tab = code.removeprefix('t=')
			if not jumlah_tab:
				jumlah_tab=1
			result = tabify_content_tab(content, num_tab=jumlah_tab)
		elif code.startswith('s2='):
			jumlah_tab = code.removeprefix('s2=')
			if not jumlah_tab:
				jumlah_tab=1
			result = tabify_content_space(content, num_tab=jumlah_tab, space_size=2)
		elif code.startswith('s4='):
			jumlah_tab = code.removeprefix('s4=')
			if not jumlah_tab:
				jumlah_tab=1
			result = tabify_content_space(content, num_tab=jumlah_tab, space_size=4)
		elif code == 'q21':  # " ke '
			result = replace_double_quote_with_single(content)
		elif code == 'q12':  # ' ke "
			result = replace_single_quote_with_double(content)
		elif code == 'eq2':  # escape double quote dg backslash, json favorite
			result = content.replace('"', '\\"')
		elif code == 's21':  # \\\\ ke \\
			result = replace_double_backslash_with_single(content)
		elif code == 's12':  # \\ ke \\\\, json favorite
			result = replace_single_backslash_with_double(content)
		elif code == 'eq2s12':  # json favorite: escape " dan \ menjadi \\
			result = replace_single_backslash_with_double(content).replace('"', '\\"')
		elif code == 'sbs':
			result = replace_slash_with_backslash(content)
		elif code == 'bss':
			result = replace_backslash_with_slash(content)
		elif code.startswith('^-'):  # hapus kiri/prefix
			query = code.removeprefix('^-')
			result = prefix_suffix_multiline(source_string=content, prefix=query, suffix=None, stripping=True)
		elif code.startswith('$-'):  # hapus kanan/suffix
			query = code.removeprefix('$-')
			result = prefix_suffix_multiline(source_string=content, prefix=None, suffix=query, stripping=True)
		elif code.startswith('^$-'):  # hapus kiri dan kanan
			query = code.removeprefix('^$-')
			result = prefix_suffix_multiline(source_string=content, prefix=query, suffix=query, stripping=True)
		elif code.startswith('^+'):  # add prefix
			query = code.removeprefix('^+')
			result = prefix_suffix_multiline(source_string=content, prefix=query, suffix=None, stripping=False)
		elif code.startswith('$+'):
			query = code.removeprefix('$+')
			result = prefix_suffix_multiline(source_string=content, prefix=None, suffix=query, stripping=False)
		elif code.startswith('^$+'):
			query = code.removeprefix('^$+')
			result = prefix_suffix_multiline(source_string=content, prefix=query, suffix=query, stripping=False)
		else:
			result = f"Not implemented: {content}."
	else:
		result = f"Not implemented: {content}."
	return result


def clipboard_manipulation(content: str):
	# content = indent_string(content, 2, 4)
	# content = indent_convert(content, 2, 't')
	# content = prefix_string(content, 10)
	# content = suffix_string(content, ',')
	content = replace_keyword(content)
	return content


def manipulate(content: str, dummy=True):
	res = 'ok'

	if dummy:
		alert('Masukkan data ke clipboard sblm tekan Enter...')
		content = trypaste()

	# meat
	content = clipboard_manipulation(content)

	alert(content, 'Content saya terima:')
	trycopy(content)
	return res


def manipulate_clip():
	res = manipulate(trypaste())
	return res


def convert_space_tab(bariskalimat, which=1):
	"""
	which
	! dan @
		1   tab to 2s
		2   tab to 4s
	# dan $
		3   2s to tab
		4   4s to tab
	% dan ^
		5   2 to 4
		6   4 to 2
	"""
	# bariskalimat = self.get_line_or_selected_text().strip()
	answer = bariskalimat
	if bariskalimat:
		source='t'
		target=2
		if which==2:
			source='t'
			target=4
		elif which==3:
			source=2
			target='t'
		elif which==4:
			source=4
			target='t'
		elif which==5:
			source=2
			target=4
		elif which==6:
			source=4
			target=2
		answer = indent_convert(bariskalimat, source, target)
	return answer
