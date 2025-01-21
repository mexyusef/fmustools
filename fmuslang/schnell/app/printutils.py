import click, functools, json, math, os, pprint, re, textwrap, traceback
from itertools import islice
from itertools import zip_longest as zeal

from anytree.render import RenderTree

from .appconfig import programming_data
from .datetimeutils import format_epoch_longer
from .dirutils import latest_files, timeify_filelist
from .fileutils import file_content
from .utils import trycopy

# https://pygments.org/docs/quickstart/
# guess_lexer( code )
# get_lexer_by_name( language )
from pygments.lexers import guess_lexer, get_lexer_for_filename, get_lexer_by_name
from pygments import highlight
from pygments.token import Keyword, Name, Text
from pygments.lexer import RegexLexer, words
from pygments.formatters.terminal import TerminalFormatter

# https://github.com/pygments/pygments/tree/master/pygments/lexers
# https://github.com/pygments/pygments/blob/master/pygments/lexers/_mapping.py
from pygments.lexers import (
	ClojureLexer,
	CppLexer,
	CSharpLexer,
	CssLexer,
	GoLexer,
	HaskellLexer,
	HtmlLexer,
	JavaLexer,
	JsxLexer,
	JavascriptLexer,
	JsonLexer,
	KotlinLexer,
	MarkdownLexer,
	NginxConfLexer,
	PythonLexer,
	ScalaLexer,
	TypeScriptLexer,
	YamlLexer,
)
from pygments.formatters import (
	TerminalFormatter,
	TerminalTrueColorFormatter,
	NullFormatter,
)

# https://pygments.org/styles/
gaya = [
	# dark
	'monokai',
	'lightbulb',
	'github-dark',
	'rrt',

	'dracula',
	'gruvbox-dark',
	'solarized-dark',
	'paraiso-dark',
	'fruity',
	'vim',
	# sepia
	'gruvbox-light',
	'solarized-light',
	'perldoc',
	# light
	'default',
	'bw',
	'xcode',
	'sas',
	'staroffice',
]
# gaya_pilihan = 'rrt'
gaya_pilihan = 'fruity'
# gaya_pilihan = 'gruvbox-light',
background_pilihan = 'dark'
# https://pygments.org/docs/formatters/

# class TerminalFormatter
#     Short names:
#         terminal, console
#     Filenames:
#         None
#     Format tokens with ANSI color sequences, for output in a text console. Color sequences are terminated at newlines, so that paging the output works correctly.
#     The get_style_defs() method doesn’t do anything special since there is no support for common styles.
#     Options accepted:
#     bg
#         Set to "light" or "dark" depending on the terminal’s background (default: "light").
#     colorscheme
#         A dictionary mapping token types to (lightbg, darkbg) color names or None (default: None = use builtin colorscheme).
#     linenos
#         Set to True to have line numbers on the terminal output as well (default: False = no line numbers).
# class TerminalTrueColorFormatter
#     Short names:
#         terminal16m, console16m, 16m
#     Filenames:
#         None
#     Format tokens with ANSI color sequences, for output in a true-color terminal or console. Like in TerminalFormatter color sequences are terminated at newlines, so that paging the output works correctly.
#     New in version 2.1.
#     Options accepted:
#     style
#         The style to use, can be a string or a Style subclass (default: 'default').


# https://github.com/pygments/pygments/blob/master/pygments/lexers/_mapping.py
# pip install --user --upgrade pygments
lexer_map = {
	'clj'           : ClojureLexer,
	'cpp'           : CppLexer,
	'cs'            : CSharpLexer,
	'css'			: CssLexer,
	'go'            : GoLexer,
	'hs'            : HaskellLexer,
	'html'          : HtmlLexer,
	'json'          : JsonLexer,
	'java'          : JavaLexer,
	'js'          	: JavascriptLexer,
	'jsx'          	: JsxLexer,
	'kt'			: KotlinLexer,
	'md'			: MarkdownLexer,
	'ts'          	: TypeScriptLexer,
	'tsx'          	: JsxLexer,
	'nginx'         : NginxConfLexer,
	'py'            : PythonLexer,
	'scala'         : ScalaLexer,
	'yaml'          : YamlLexer,
}



show_lineno = False
# linenos=True
# linenos=show_lineno


class MyLexer(PythonLexer):
	
	fuck_object = None

	def my_callback(lexer, match):
		kata = match.group(1)
		if kata in MyLexer.fuck_object.keywords:
			yield match.start(), Name.Builtin, kata
		else:
			yield match.start(), Text, kata

	tokens = {
		'root': [
			# (words(('file', 'capcay')), Name.Builtin),
			# (words(('file', 'capcay')), Name.Builtin),
			(r'\s+', Text),
			(r'(\w+)', my_callback),
			(r'\W+', Text),
		],
	}

	def __init__(self, keywords):
		self.keywords = keywords

		MyLexer.fuck_object = self
		self.stripall = True
		self.tabsize = 2
		self.ensurenl = True
		self.filters = []
		# print('hasil tokens:', self.tokens)

	# def get_tokens_unprocessed(self, text):
	# 	for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
	# 		if token is Name and value in self.keys:
	# 			yield index, Keyword.Pseudo, value
	# 			# yield index, Name.Builtin, value
	# 		else:
	# 			yield index, token, value



def is_source_code(baris):
	# utk digunakan bersama print_source_code
	return [item for item in lexer_map.keys() if baris.endswith(item)]


def print_source_code(content, lexer='py'):
	# default_lexer = lexer_map[lexer] ()
	default_lexer = guess_lexer(content)
	print(highlight(content, default_lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan)))


def print_source_code_copy(content, lexer='py'):
	# default_lexer = lexer_map[lexer] ()
	default_lexer = guess_lexer(content)
	trycopy(content)
	print(highlight(content, default_lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan)))


def print_source_code_file(filepath):
	content = file_content(filepath)
	# default_lexer = lexer_map[lexer] ()
	try:
		default_lexer = get_lexer_for_filename(filepath)
	except:
		default_lexer = MarkdownLexer()
	print(highlight(content, default_lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan)))


def print_source_code_file_with_markdown(filepath, delegate_markdown=True):
	content = file_content(filepath)
	if filepath.endswith('.md') and delegate_markdown:
		from .formatutils.markdownutils import print_markdown_file
		print_markdown_file(filepath)
	else:
		try:
			default_lexer = get_lexer_for_filename(filepath)
		except:
			default_lexer = MarkdownLexer()
		print(highlight(content, default_lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan)))


def print_highlight_query(text_content, search_term, fg_color='\033[91m', bg_color='\033[43m'):
	# Use a regular expression to find lines containing the search term
	pattern = re.compile(re.escape(search_term), re.IGNORECASE)

	# Split the text content into lines
	lines = text_content.split('\n')

	highlighted_lines = []
	for i, line in enumerate(lines, start=1):
		if pattern.search(line):
			# Apply additional formatting or highlighting to the matched line
			highlighted_line = f"{fg_color}{bg_color}{i:3d}| {line}\033[0m"
		else:
			highlighted_line = f"{i:3d}| {line}"
		highlighted_lines.append(highlighted_line)

	# Join the lines back together
	highlighted_text = '\n'.join(highlighted_lines)
	print(highlighted_text)
	return highlighted_text


def print_highlight_query_file(filepath, search_term):
	filecontent = file_content(filepath)
	return print_highlight_query(filecontent, search_term)


def test_highlight_lines_with_line_numbers():
	with open(__file__, 'r', encoding='utf-8') as file:
		script_content = file.read()

	search_term = "highlight"

	# Create an instance of PythonLexer
	lexer = PythonLexer()

	# Highlight lines with line numbers using the custom function
	highlighted_text = print_highlight_query(script_content, search_term, fg_color='\033[91m', bg_color='\033[43m')

	# Highlight the entire content with line numbers using Pygments lexer
	colored_text = highlight(script_content, lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan))

	# Print the combined output
	print(highlighted_text)
	print("\n" + "="*20 + "\n")
	print(colored_text)


def highlight_lines_with_background(text_content, search_term, fg_color='\033[91m', bg_color='\033[43m'):
	# Use a regular expression to find lines containing the search term
	pattern = re.compile(re.escape(search_term), re.IGNORECASE)

	# Split the text content into lines
	lines = text_content.split('\n')

	highlighted_lines = []
	for line in lines:
		if pattern.search(line):
			# Apply additional formatting or highlighting to the matched line
			highlighted_line = f"{fg_color}{bg_color}{line}\033[0m"
		else:
			highlighted_line = line
		highlighted_lines.append(highlighted_line)

	# Join the lines back together
	highlighted_text = '\n'.join(highlighted_lines)
	return highlighted_text


def test_highlight_lines_with_background():
	with open(__file__, 'r', encoding='utf-8') as file:
		script_content = file.read()

	search_term = "highlight"

	# Create an instance of PythonLexer
	lexer = PythonLexer()

	# Highlight lines using the custom function with both foreground and background colors
	highlighted_text = highlight_lines_with_background(script_content, search_term, fg_color='\033[91m', bg_color='\033[43m')

	# Highlight the entire content using Pygments lexer with both foreground and background colors
	colored_text = highlight(script_content, lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan))

	# Print the combined output
	print(highlighted_text)  # versi highlighted
	print("\n" + "="*20 + "\n")
	print(colored_text)  # versi lexerised


def highlight_lines(text_content, search_term, highlight_color='\033[91m'):
	# Use a regular expression to find lines containing the search term
	pattern = re.compile(re.escape(search_term), re.IGNORECASE)

	# Split the text content into lines
	lines = text_content.split('\n')

	highlighted_lines = []
	for line in lines:
		if pattern.search(line):
			# Apply additional formatting or highlighting to the matched line
			highlighted_line = f"{highlight_color}{line}\033[0m"
		else:
			highlighted_line = line
		highlighted_lines.append(highlighted_line)

	# Join the lines back together
	highlighted_text = '\n'.join(highlighted_lines)
	return highlighted_text


def test_highlight_lines():
	with open(__file__, 'r', encoding='utf-8') as file:
		script_content = file.read()

	search_term = "highlight"

	# Create an instance of PythonLexer
	lexer = PythonLexer()

	# Highlight lines using the custom function
	highlighted_text = highlight_lines(script_content, search_term)

	# Highlight the entire content using Pygments lexer
	colored_text = highlight(script_content, lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg='dark'))

	# Print the combined output
	print(highlighted_text)
	print("\n" + "="*20 + "\n")
	print(colored_text)


def indah(message, warna='green', layar=None, width=80, newline=False,
	bold=True,
	blink=False,
	underline=True,
	reverse=True
):
	"""
warna apa aja? https://pypi.org/project/colorama/
	black red green yellow blue magenta cyan reset
"""
	try:
			# click.echo ( click.style(message.center(width), fg=warna, bg=layar, bold=True, blink=True, underline=True, reverse=True).decode('utf-8') )
		click.echo(
			click.style(
				message.center(width),
				fg=warna,
				bg=layar,
				bold=bold,
				blink=blink,
				underline=underline,
				reverse=reverse
			),
			nl=newline
		)

	except Exception as e:
		print(str(e))
		print(message)


def indah0(message, warna='green', newline=False, layar=None, bold=False,
	blink=False,
	underline=False,
	reverse=False
):
	"""
	left justified
	default: 80 column, centered
	"""
	indah(message, warna=warna, width=0, newline=newline, layar=layar, bold=bold, blink=blink, underline=underline, reverse=reverse)


def indah1(message, warna='green', layar=None, blink=False, underline=False, reverse=False):
	"""
	newline
	bold
	"""
	# indah0(message, warna, layar, bold=True, newline=True)
	indah(message, warna=warna, width=0, newline=True, layar=layar, bold=True, blink=blink, underline=underline, reverse=reverse)


def indah2(message, warna='green', layar=None, blink=False, underline=False, reverse=False):
	"""
	newline
	bold
	copy
	"""
	# indah0(message, warna, layar, bold=True, newline=True)
	indah(message, warna=warna, width=0, newline=True, layar=layar, bold=True, blink=blink, underline=underline, reverse=reverse)
	trycopy(message)


def indah3(message, warna='green', layar=None, blink=False, underline=False, reverse=False, newline=True):
	"""
	safe indah2 jk message kosong
	mengcopy pesan ke clipboard

	newline
	bold
	copy
	"""
	if not message:
		return

	indah(message, warna=warna, width=0, newline=newline, layar=layar, bold=True, blink=blink, underline=underline, reverse=reverse)
	trycopy(message)


def indah4(message, warna='green', layar='black', blink=False, underline=False, reverse=False, newline=True, bold=True):
	"""
	versi no copy clipboard dari indah3
	"""
	if not message:
		return

	indah(message, warna=warna, width=0, newline=newline, layar=layar, bold=bold, blink=blink, underline=underline, reverse=reverse)


def indahnl(message, warna='green', layar=None, bold=False, newline=False, blink=False, reverse=False, underline=False):
	"""
	newline
	"""
	# indah0(message, warna, layar, bold=True, newline=True)
	indah(message, warna=warna, width=0, newline=True, layar=layar, bold=bold, blink=blink, underline=underline, reverse=reverse)

def indahr(message, warna='green', layar=None, bold=False, newline=False, blink=False, underline=False):
	"""
	newline
	reverse
	"""
	# indah0(message, warna, layar, bold=True, newline=True)
	indah(message, warna=warna, width=0, newline=True, layar=layar, bold=bold, blink=blink, underline=underline, reverse=True)


def indahb(message, warna='green', layar=None, newline=False, blink=False, underline=False, reverse=False):
	"""
	newline
	bold
	"""
	# indah0(message, warna, layar, bold=True, newline=True)
	indah(message, warna=warna, width=0, newline=True, layar=layar, bold=True, blink=blink, underline=underline, reverse=reverse)


def indahu(message, warna='green', layar=None, newline=False, bold=False, blink=False, reverse=False):
	"""
	newline
	underline
	"""
	# indah0(message, warna, layar, bold=True, newline=True)
	indah(message, warna=warna, width=0, newline=True, layar=layar, bold=bold, blink=blink, underline=True, reverse=reverse)


def print_list(the_list, genap='yellow', ganjil='green'):
	for index, filename in enumerate(the_list):
		tulisan = f"{index}. {filename}"
		warna = genap if (index%2==0) else ganjil
		# indah0(tulisan, warna=warna, newline=True)
		indah4(tulisan, warna=warna)


def print_list_warna(the_list, genap='yellow', ganjil='green', bold=True, berwarna=True, special_ends=None, start=0, prefix='', extra_warna={}, extra_suffix='', no_index=False):
	"""
	contoh special_ends
	*.py
	maka highlight yg endswith tsb
	UPD:
	tambah extra_suffix utk bs kasih extra newline di antara baris
	tambah no_index jk gak mau ada index
	"""
	for index, filename in enumerate(the_list, start):
		# print(f"proses {index} dan {filename}.")
		tulisan = prefix + ('' if no_index else f'{index}. ') + f"{filename}" + (extra_suffix if extra_suffix else '')
		if berwarna:
			warna = genap if (index % 2 == 0) else ganjil
			if extra_warna:
				for k,v in extra_warna.items():
					if index % k == 0:
						warna = v
			if special_ends and filename.endswith(special_ends):
				indah0(tulisan, warna='white', layar='red', bold=bold, newline=True)
			else:
				indah0(tulisan, warna=warna, bold=bold, newline=True)
		else:
			print(tulisan)


def print_json(data, indent=4, warna='yellow', layar='black'):
	indah4(json.dumps(data, indent=indent), warna=warna, layar=layar)


def pp(data):
	pprint.pprint(data)


def ppr(data):
	from rich.pretty import pprint
	pprint(data)


def print_tree(node):
	print(RenderTree(node))


def get_tree(node):
	return RenderTree(node)


def filter_print_latest_files(code, basedir, cetak_waktu=False):
	"""
	kita nanti pengen bikin gini
	|50 word1 word2
	jadi dari hasil |50 kita filter yg mengandung word1 dan word2 saja.
	"""
	# print(f'cetak latest files [code={code}], [dir={basedir}]')
	if not code:
		code = '10' # minimal bertujuan utk lihat latest files

	m = re.match(r'^(\d+)\s*(.*)', code)
	if m:
		# print(f"ketemu m dg group: {m.groups()}")
		jumlah = m.group(1)
		jumlah = int(jumlah)
		result = latest_files(basedir, jumlah)

		# jk ada words utk ngefilter hasil ls by time
		allfilters = m.group(2)    
		if allfilters:
			'''
			di sini tentu pake any
			'''
			splittedfilters = allfilters.split()
			# print(f"splitted: {splittedfilters}")
			result = [item for item in result 
				if any([word for word in splittedfilters if word in item])]
			# print(f"result: {result}")

		if cetak_waktu:
			# print(f"sblm timeify")
			result_with_time = timeify_filelist(result) # latest_files_with_time(basedir, jumlah)
			# print(f"sblm print list warna")
			print_list_warna(result_with_time)
			return result_with_time
		else:
			print_list_warna(result)
			return result


def print_file(filepath):
	print(file_content(filepath))


def indah_file(filepath, warna='green', layar='black'):
	indah3(file_content(filepath), warna=warna, layar=layar)


def print_copy(content):
	print(content)
	trycopy(content)


def print_copy_file(filename, warna='white', pygments=False, lexer='py'):
	header = f"{'='*40} {filename}"
	content = file_content(filename)
	trycopy(content)
	# print(header)
	indah0(header, warna=warna, newline=True)

	if not pygments:
		print(content)
	else:
		default_lexer = lexer_map[lexer] ()
		filename, extension = os.path.splitext(filename)
		if extension:
			choose = [item for item in lexer_map.keys() if extension == '.' + item]
			if choose:
				choose = choose[0]
				default_lexer = lexer_map[choose]()

		print(highlight(content, default_lexer, TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan)))
		# print(highlight(content, get_lexer_for_filename(filename), NullFormatter()))
		# print(highlight(content, get_lexer_for_filename(filename), TerminalTrueColorFormatter()))


def dir_w_old(list_files, jumlah_kolom = None, screen_width = None):
	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_SCREENWIDTH"] or not screen_width:
		screen_width = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_SCREENWIDTH"]

	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_COLNUMBER"] or not jumlah_kolom:
		jumlah_kolom = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_COLNUMBER"]

	pecah = lambda asli, banyak: [asli[i: i+banyak] for i in range(0, len(asli), banyak) ]

	terbagi = pecah(list_files, jumlah_kolom)

	kolomku = f"{{: >{screen_width / jumlah_kolom}}}"
	# [ print(f"{kolomku*3}".format(*item)) for item in b(list(range(0,9)),3) ]
	for item in terbagi:
		print(f"{kolomku*len(item)}".format(*item))


def dir_w(sumber_array, jumlah_kolom = None, screen_width = None, warna='blue', layar=None, bold=True):
	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_SCREENWIDTH"] or not screen_width:
		screen_width = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_SCREENWIDTH"]

	if programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_COLNUMBER"] or not jumlah_kolom:
		jumlah_kolom = programming_data['j']['schnell']['app']["configuration"]["ULIBPY_DIR_W_COLNUMBER"]

	def print_transposed(terbagi):
		kolomku = f"{{: <{int(screen_width/jumlah_kolom)}}}"
		for item in terbagi:
			# bersihkan elem dari item yg None
			item = [el for el in item if el is not None]
			indah0(f"{kolomku*len(item)}".format(*item), warna=warna, layar=layar, bold=bold, newline=True)

	def transpose(array):
		return list(map(list, zeal(*array)))

	def ice(array, *args):
		return list(islice(array, *args))

	ambil = math.ceil(len(sumber_array) / jumlah_kolom)
	urut = [ice(sumber_array, ambil*oper, ambil*(oper+1)) for oper in range(jumlah_kolom)]
	transposed = transpose(urut)
	print_transposed(transposed)

# filedir/library.py
def print_enumerate(contentlist):
	for index, item in enumerate(contentlist):
		print('{:4d}| {:s}'.format(index, item))


def indah_enumerate(contentlist, warna='white'):
	for index, item in enumerate(contentlist):
		cetak = '{:4d}| {:s}'.format(index, item)
		indah0(cetak, newline=True, bold=True, warna=warna)


def print_copy_enumerate_filtercontent(string_content, filterpattern, warna='green'):
	index_lines = enumerate(string_content.splitlines())
	content = ['{:4d}| {:s}'.format(no, baris) for (no, baris) in index_lines if filterpattern in baris]
	trycopy(content)
	for line in content:
		indah3(line, warna=warna)


def print_copy_enumerate(content):
	trycopy(content)
	for index, item in enumerate(content.splitlines()):
		print('{:4d}| {:s}'.format(index, item))


def print_copy_enumerate_list(contentlist, delimiter=''):
	"""
	spt print_copy_enumerate
	tapi input adlh list, jd gak perlu splitlines() dulu
	"""
	trycopy(delimiter.join(contentlist))
	for index, item in enumerate(contentlist):
		print('{:4d}| {:s}'.format(index, item))


def print_debug(*args, **kwargs):
	if programming_data["debug"]:
		print(*args, **kwargs)


def indah_debug(*args, **kwargs):
	if programming_data["debug"]:
		indah4(*args, **kwargs)


class Debug:
	def __init__(self, isDebug=False, printToFile=''):
		# self.isDebug = isDebug
		self.isDebug = isDebug
		# input(f'nilai debug adlh [{self.isDebug}] dan args [{isDebug}] ')
		if printToFile:
			self.filename = printToFile
			self.fd = open(self.filename, 'a')

	def stop(self):
		if hasattr(self, 'filename'):
			if self.fd:
				os.close(self.fd)

	def __call__(self, *args, **kwargs):
		"""
		kita kasih kwargs: forced
		if forced == True maka print bagaimanapun
		"""
		# print('debug is called', 'debug?', self.isDebug, 'kwargs', kwargs)
		if self.isDebug:
			if hasattr(self, 'filename'):
				print(*args, **kwargs, file=self.fd)
			else:
				# indah0(*args, **kwargs)
				if len(args) == 1 and isinstance(args[0], str):
					pesan = args[0]
					indah0(pesan, **kwargs, reverse=True)
				else:
					print(*args, **kwargs)
		else:
			if kwargs and 'forced' in kwargs and kwargs['forced']:
				del kwargs['forced']
				input('forcing debug!')
				if len(args) == 1 and isinstance(args[0], str):
					pesan = args[0]
					indah0(pesan, **kwargs)
				else:
					print(*args, **kwargs)


def pigmen(content, keywords):
	print(highlight(content, MyLexer(keywords), TerminalFormatter()))
	# lexer = MyLexer()
	# state_item = (words(tuple(keywords)), Name.Builtin)
	# lexer.tokens = {
	# 	'root': [
	# 		state_item,
	# 		(r'\s+', Text),
	# 		(r'\w+', Text),
	# 		(r'\W+', Text),
	# 	],
	# }
	# print(highlight(content, lexer, TerminalFormatter()))


def print_file_pigmen(filepath, keywords):
	pigmen(file_content(filepath), keywords)


def printex(msg='', printer=print):	
	printer(msg)
	printer(traceback.format_exception())


def tryex(block_content, msg='', printer=print):
	try:
		block_content()
	except Exception as err:
		printer(f'{msg}: {err}')
		printer(traceback.format_exception())


from rich.tree import Tree
from rich import print
import os


def print_directory_tree_old(start_path='.', level=2, tree=None, skip_folders=None, skip_files=None):
    if skip_folders is None:
        skip_folders = ['node_modules', '.git', '__pycache__']
    if skip_files is None:
        skip_files = ['.DS_Store']

    if tree is None:
        tree = Tree(f"[bold]{os.path.basename(start_path) or '.'}[/bold]")

    for item in os.listdir(start_path):
        if item in skip_folders:
            continue
        path = os.path.join(start_path, item)
        if os.path.isdir(path):
            if level > 0:
                branch = tree.add(f"[bold]{item}[/bold]")
                print_directory_tree(path, level - 1, branch, skip_folders, skip_files)
            else:
                tree.add(f"[dim]{item}/[/dim]")
        elif item not in skip_files:
            tree.add(item)

    if level == 2:  # Only print for the top-level call
        print(tree)


def test_print_directory_tree_old():
	print_directory_tree()


def print_directory_tree(start_path='.', max_level=2, current_level=0, tree=None, skip_folders=None, skip_files=None):
    if skip_folders is None:
        skip_folders = ['node_modules', '.git', '__pycache__']
    if skip_files is None:
        skip_files = ['.DS_Store']

    if tree is None:
        tree = Tree(f"[bold]{os.path.basename(start_path) or '.'}[/bold]")

    if current_level < max_level:
        for item in os.listdir(start_path):
            if item in skip_folders:
                continue
            path = os.path.join(start_path, item)
            if os.path.isdir(path):
                branch = tree.add(f"[bold]{item}[/bold]")
                print_directory_tree(path, max_level, current_level + 1, branch, skip_folders, skip_files)
            elif item not in skip_files:
                tree.add(item)

    if current_level == 0:  # Only print for the top-level call
        print(tree)


def test_print_directory_tree():
	print_directory_tree(max_level=4)


if __name__ == '__main__':
	# from pygments import highlight
	# from pygments.lexers import PythonLexer
	# from pygments.formatters import (
	# 	TerminalFormatter,
	# 	TerminalTrueColorFormatter,
	# 	NullFormatter,
	# )

	with open(__file__, 'r', encoding='utf-8') as file:
		file_content = file.read()
		colored_text = highlight(file_content, PythonLexer(), TerminalTrueColorFormatter(linenos=show_lineno, style=gaya_pilihan, bg=background_pilihan))
		print(colored_text)
