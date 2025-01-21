import json, re, shlex, string, uuid


tab_tab = '\t'
tab_space2 = ' '*2
tab_space4 = ' '*4
tab_space6 = ' '*6
tab_space8 = ' '*8

default_tab = ' '*2 # '\t'
SQ = "'"
DQ = '"'
BT = '`'
_SQ = SQ
_DQ = DQ
_BT = BT
__SQ = SQ
__DQ = DQ
__BT = BT
__SQ__ = SQ
__DQ__ = DQ
__BT__ = BT
QuoteChar = '$$$'
EmptyReplaceQuoteChar = ''


"""
dipake utk repace/insert utk fileoperation...@ia, @ra, @rs, dst.
misal:
"target": "es5" menjadi "target": "es6"
"module": "commonjs"
@rs="__DQtarget__DQ: __DQes6__DQ"="__DQtarget__DQ: __DQes5__DQ"

  def sanitize_prohibited_chars(self, content):
    kita bisa tulis DQ sbg pengganti double quote
    @re,baris_cari_dalam_mk_file,"something DQemphasizedDQ and other"
    lihat di h feature
    pubspec.yaml,f(f=pubspec.yaml,@ra=flutter_sdk_no="sdk: DQ>=2.")
    sebetulnya lebih baik jk kita gunakan
    __DQ daripada DQ doang...
    for k,v in chars_to_sanitize_in_file_operation.items():
      content = content.replace(k, v)

    return content

TODO:
pake juga utk:
- get permissive di fileutils...agar kita bisa bikin --% dan --# sbg daleman dalam sebuah entry
- utk grammar.py agar bisa dipake di filename,f(...), dirname,d(...) dst

kita juga punya __AT utk @ utk nama direktori/file
mending operasi digabungkan di sini dg sanitize_chars.
"""
chars_to_sanitize_in_file_operation = {
  '__DQ__': '"',
    # '__DQ': '"',
  '__SQ__': "'",
    # '__SQ': "'",
  '__BT__': '`',
    # '__BT': '`',
  '__MINUS__': '-',
    # '__MINUS': '-',
  '__PLUS__': '+',
    # '__PLUS': '+',

  '__NL__': "\n",
    # '__NL': "\n",

  '__SL__': "/",
    # '__SL': "/",

  '__BS__': "\\",
    # '__BS': "\\",

  '__PP__': "|",
    # '__PP': "|",

  '__EXC__': "!",
    # '__EXC': "!",

  '__EQ__': '=',
    # '__EQ': '=',
  '__COMMA__': ",",
    # '__COMMA': ",",

  '__DOT__': ".",
    # '__DOT': ".",

  '__DOLLAR__': '$',
    # '__DOLLAR': '$',

  '__AMP__': '&',
    # '__AMP': '&',

  '__TLD__': '~',
    # '__TLD': '~',
  '__TILDE__': '~',
    # '__TILDE': '~',

  '__AT__': "@", # jangan lupa, yg panjang mendahului yg pendek
    # '__AT': "@",

  '__POUND__': "#",
    # '__POUND': "#",

  '__STAR__': "*",
    # '__STAR': "*",

  '__PRC__': "%", # jangan lupa, yg panjang mendahului yg pendek
    # '__PRC': "%", # ini krn %TEMP%,d dianggap sbg %TEMPLATE_SAVE_VAR etc


  '__CL__': ":",
  '__SC__': ";",

  '__LP__': "(",
    # '__LP': "(",
  '__RP__': ")",
    # '__RP': ")",
  '__LK__': "[", # jangan lupa, yg panjang mendahului yg pendek
    # '__LK': "[",
  '__RK__': "]", # jangan lupa, yg panjang mendahului yg pendek
    # '__RK': "]",
  '__LB__': "{",
    # '__LB': "{",
  '__RB__': "}",
    # '__RB': "}",

  '__LT__': "<",
  '__GT__': ">",

  '__TAB__': "\t",
  '__TAB1__': "\t",
  '__TAB2__': "\t\t",
  '__TAB3__': "\t\t\t",
  '__TAB4__': "\t\t\t\t",
  # '__TAB__': "\t",
  '__SPC1__': " ",
  '__SPC2__': " "*2,
  '__SPC3__': " "*3,
  '__SPC4__': " "*4,
  # '__SPC__': " ",
  # ini bisa bikin c:\tmp dan c:\newname jadi dikonversi, maka kita matikan 4-dec-2022
  # '\\n': "\n",
  # '\\t': "\t",
}


def uuid1():
  return uuid.uuid1().hex


def uuid4():
  return uuid.uuid4().hex


def split_safe_quote(text):
  # https://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python
  return shlex.split(text, posix=False)


def jsonify(data, indent=4):
  return json.dumps(data, indent=indent)


def max_item_len_in_list(the_list):
  return max([len(item) for item in the_list])


def email_valid(email):
  """
  https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
  """
  pat = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
  return re.search(pat, email)


def startswith_absolute_folder(text, pattern_suffix=''):
  """
  groups()
  group()
    AttributeError: 'NoneType' object has no attribute 'group'
  group(0)
  """
  if pattern_suffix:
    '''
    jk diberikan ",d"
    maka kita True = yes startswith abspath hanya jk text diakhiri dg ",d" maka proses text sbg path
    '''
    if not text.endswith(pattern_suffix):
      return False
  pat = '^(\/[^\/]+)+'
  return re.match(pat, text)


def strip0(text, prefix):
  return text.removeprefix(prefix).strip()


def strip1(text, suffix):
  return text.removesuffix(suffix).strip()


def remove_nondigits(text, replacer=''):
  pat = '[^0-9]'
  return re.sub(pat, replacer, text)


def hitung(text, char='|'):
  """
  hitung jumlah char dlm text
  """
  return text.count(char)


def ada(text, char):
  return hitung(text, char) > 0


def first_occurrence(text, char, start=0, end=-1):
  """
  https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python/2294502
  """
  return text.index(char, start, end)


def splitspace(text, count=1, delim=' '):
  """
  count=1
  'satu dua tiga empat' => ['satu', 'dua tiga empat']
  """
  return text.split(delim, count)


def list_startswith(the_list, the_start, lower=True):
  if lower:
    return [item for item in the_list if item.lower().startswith(the_start.lower())]
  else:
    return [item for item in the_list if item.startswith(the_start)]


def list_contains(the_list, the_start, lower=True):
  if lower:
    return [item for item in the_list if the_start.lower() in item.lower()]
  else:
    return [item for item in the_list if the_start in item]


def list_stringify(the_list, delimiter='\n', sort=True, prefixer=None, suffixer=None):
  if prefixer:
    the_list = [prefixer+item for item in the_list]
  if suffixer:
    the_list = [item+suffixer for item in the_list]
  if sort:
    return delimiter.join(sorted(the_list))
  return delimiter.join(the_list)


def gabung_kunci(the_dict, delimiter='\n', sort=True):
  if sort:
    return '\n'.join(sorted(the_dict.keys()))
  return '\n'.join(the_dict.keys())


def dari_kanan(sumber, karakter):
  return sumber.rfind(karakter)


def punctuation_in_string(text, with_space=False, allow_dash=False):
  allow_underscore = string.punctuation.replace('_', '')
  if with_space:
    allow_underscore += ' '  # space dianggap puncs, text stlh space akan diabaikan utk hitung zau
  if allow_dash:
    allow_underscore = allow_underscore.replace('-', '')  # - kita hapus dari daftar puncs, agar text stlh nya tdk dibypass
  # print("punctuation_in_string => allow_underscore:", allow_underscore)
  return [kar in allow_underscore for kar in text]


def get_first_punctuation_index(text, with_space=False, allow_dash=False):
  nonwords = r'[^\w]+'
  if with_space:
    nonwords = r'[^\w\s]+'
    if allow_dash:
      nonwords = r'[^\w\s\-]+'
  else:
    if allow_dash:
      nonwords = r'[^\w\s\-]+'
  all = re.findall(nonwords, text)
  # print('all puncs', all)
  if all:
    return text.index(all[0])
  return None


def is_camel_case(s):
  return s != s.lower() and s != s.upper() and "_" not in s


def pluralize(s):
  return s.lower() + 's'


def merge_lines(s, joiner='', strip=True):
  """
  joiner bisa juga space
  """
  linified = s.splitlines()
  if strip:
    linified = [item.strip() for item in linified]
  return joiner.join(linified)


def escape_quotes(s):
  return s.replace('"', '\\"')


def non_empty_lines(lines):
  return [item for item in lines if item.strip()]


def tabify_content(content, self_tab=default_tab, num_tab=1, delim='\n'):
  tabify = [num_tab*self_tab + item for item in content.splitlines()]
  # input(f"hasil tabify_content=[{tabify}] dg self_tab = [{self_tab}]")
  return delim.join(tabify)


def tabify_content_tab(content, num_tab=1, delim='\n'):
  from schnell.app.usutils import tab_tab
  return tabify_content(content, self_tab=tab_tab(), num_tab=num_tab, delim=delim)


def tabify_content_space(content, num_tab=1, delim='\n', space_size=2):
  from schnell.app.usutils import tab_space
  return tabify_content(content, self_tab=tab_space(space_size=space_size), num_tab=num_tab, delim=delim)


def tabify_contentlist(content, self_tab=default_tab, num_tab=1, aslist=False, delim='\n', string_ender=''):
  """
  string_ender
    jk pengen:
    a=1,
    b=2,
  """
  tabify = [num_tab*self_tab + item for item in content]
  if aslist:
    return tabify
  return delim.join(tabify) + string_ender


def tabify_contentlist_tab(content, num_tab=1, aslist=False, delim='\n', string_ender=''):
  from schnell.app.usutils import tab_tab
  return tabify_contentlist(content, self_tab=tab_tab(), num_tab=num_tab, aslist=aslist, delim=delim, string_ender=string_ender)


def tabify_contentlist_space(content, num_tab=1, aslist=False, delim='\n', string_ender='', space_size=2):
  from schnell.app.usutils import tab_space
  return tabify_contentlist(content, self_tab=tab_space(space_size=space_size), num_tab=num_tab, aslist=aslist, delim=delim, string_ender=string_ender)


def left_right_joinify_content(content, left='', middle='\n', right=''):
  """
  default: newline-joined
  """
  delimiter = left + middle + right
  return delimiter.join(content.splitlines())


def left_right_joinify_contentlist(content, left='', middle='\n', right=''):
  """
  default: newline-joined
  """
  delimiter = left + middle + right
  return delimiter.join(content)


def joinify_content(content, delimiter='\n'):
  """
  default: input dan output sama
  """
  return delimiter.join(content.splitlines())


def joinfy_contentlist(content, delimiter='\n'):
  return delimiter.join(content)


def tuplelify_string(content, header_lines=1):
   """
   split string jadi 2 strings: header sebanyak baris=header_lines dan body
   """
   contentlist = content.splitlines()
   # jk <=1 baris, no header, body=as is
   if len(contentlist)<2:
      return ('', contentlist)
   header, body = content[:header_lines], content[header_lines:]
   return '\n'.join(header), '\n'.join(body)


def clean_list_to_string(alist):
  """
  lst = [1,2,3,4,5] sbg list
  str(lst) = ['1','2','3','4','5'] sbg string
  clean_list_to_string = [1,2,3,4,5] sbg string
  """
  return str(alist).replace("'",'')


def dashToCamel(text):
  """
  dashToCamel('satu-dua-tiga-empat-lima')
  """
  hasil = text
  while '-' in hasil:
    b = hasil.index('-')
    hasil = hasil[:b] + hasil[b+1].upper() + hasil[b+2:]
  return hasil


d2C = dashToCamel


def dash_to_camel(text):
  return dashToCamel(text)


def sort_list(da_list, panjang_duluan=False):
  return sorted(da_list, key=len, reverse=panjang_duluan)


def list_take_shortest(da_list):
  if len(da_list) == 1:
    return da_list[0]
  a = sort_list(da_list)
  # print('LTS list:', da_list)
  if len(a):
    return a[0]
  return None


def list_take_longest(da_list):
  # print('LTL list:', da_list)
  if len(da_list) == 1:
    return da_list[0]
  a = sort_list(da_list, panjang_duluan=True)
  if len(a):
    return a[0]
  return None


def newlinify(baris):
  if not baris.endswith('\n'):
    baris += '\n'
  return baris


def replace_non_alpha(text, pengganti='_', exclude = '.'):
  """
  exclude adlh \W yg gak direplace dg _
  kita pengen . gak direplace oleh _
  """
  # return re.sub('\W+', pengganti, text)
  return re.sub(r'[^\w'+exclude+']', pengganti, text)


def splitstrip0(thelist):
  """
  split berbasis space dan selalu ALL fields
  """
  return [item.strip() for item in thelist.split()]


def splitstrip(thelist, delimiter=' ', maxsplit=-1):
  """
  bisa specify delimiter dan jumlah fields yg displit
  """
  return [item.strip() for item in thelist.split(delimiter, maxsplit)]


def joinsplitstrip(thelist, delimiter=' ', maxsplit=-1):
  return splitstrip(thelist, delimiter, maxsplit)


def joinsplitlines(thelist, pemisah='\n'):
  return pemisah.join(thelist.splitlines())


def joinsplitstriplines(thelist, pemisah='\n'):
  return pemisah.join([item.strip() for item in thelist.splitlines()])


def multiple_spaces_to_single_space(original_text, replacer=' '):
  """
  https://pythonexamples.org/python-replace-multiple-spaces-with-single-space-in-text-file/
  """
  # return ' '.join(original_text.split())
  return re.sub('\s+', replacer, original_text)


def sanitize(content):
  for k,v in chars_to_sanitize_in_file_operation.items():
    content = content.replace(k, v)
  return content


def sanitize_chars(content):
  return sanitize(content)


def split_by_pos(strng, sep, pos):
  """
  https://stackoverflow.com/questions/36300158/split-text-after-the-second-occurrence-of-character

  >>> strng = 'some-sample-filename-to-split'
  >>> split(strng, '-', 3)
  ('some-sample-filename', 'to-split')
  >>> split(strng, '-', -4)
  ('some', 'sample-filename-to-split')
  >>> split(strng, '-', 1000)
  ('some-sample-filename-to-split', '')
  >>> split(strng, '-', -1000)
  ('', 'some-sample-filename-to-split')
  """
  strng = strng.split(sep)
  return sep.join(strng[:pos]), sep.join(strng[pos:])


def bongkar_string(filelike_string):
  from .utils import env_ulibpy, env_get
  for envvar in env_ulibpy():
    expanded = env_get(envvar)
    filelike_string = filelike_string.replace(envvar, expanded)
  return filelike_string


def replace_indent_with_tabs(multiline_string):
  lines = multiline_string.splitlines()
  if len(lines) < 2:
    return multiline_string

  second_line_indent = len(lines[1]) - len(lines[1].lstrip())
  if second_line_indent == 0:
    return multiline_string

  result = []
  for line in lines:
    indent = len(line) - len(line.lstrip())
    if indent == 0:
      result.append(line)
    else:
      tabs = indent // second_line_indent
      result.append('\t' * tabs + line.lstrip())

  return '\n'.join(result)

# # Example usage:
# multiline_string = """
#     This is an example
#         Multiline string
#     With varying indentation
#             Among the lines
#         And we want to replace
#     the leading spaces with tabs
# """

def replace_four_spaces_with_tabs(multiline_string, spaces=4):
    return re.sub(r'(?<=\n) {'+str(spaces)+'}', '\t', multiline_string)

# # Example usage:
# multiline_string = """
#     This is an example
#         Multiline string
#     With varying indentation
#             Among the lines
#         And we want to replace
#     the leading spaces with tabs
# """

def replace_single_backslash_with_double(backslash_string):
  # original: skip \n, \r, \t
  # return re.sub(r'(?<!\\)\\(?!([nrt]))', r'\\\\', backslash_string)
  return re.sub(r'\\', r'\\\\', backslash_string)


def replace_double_backslash_with_single(backslash_string):
  return re.sub(r'\\\\', r'\\', backslash_string)

# # Example usage:
# original_string = r'c:\\tmp\\some\\folder\\n\\test\\t\\file.txt'
# result = replace_double_backslash_with_single(original_string)
# print(result)

# # Example usage:
# original_string = r'c:\tmp\some\folder\n\test\t\file.txt'
# result = replace_single_backslash_with_double(original_string)
# print(result)

# result = replace_four_spaces_with_tabs(multiline_string)
# print(result)

# result = replace_indent_with_tabs(multiline_string)
# print(result)
# multiline_string = """This is a multiline string.
# It spans multiple lines.
# \tIt also includes tabs."""
# escaped_string = escape_multiline_string(multiline_string)
# print(escaped_string)


def replace_single_quote_with_double(source_string):
  return re.sub(r'\'', r'"', source_string)


def replace_double_quote_with_single(source_string):
  return re.sub(r'"', r'\'', source_string)


def replace_backslash_with_slash(source_string):
  return re.sub(r'\\', r'/', source_string)


def prefix_suffix_multiline(source_string, prefix=None, suffix=None, stripping=True):
  if stripping:
    if prefix and suffix:
      result = [line.strip(prefix).strip(suffix) for line in source_string]
    elif prefix:
      result = [line.strip(prefix) for line in source_string]
    elif suffix:
      result = [line.strip(suffix) for line in source_string]
  else:
    if prefix and suffix:
      result = [(prefix + line + suffix) for line in source_string]
    elif prefix:
      result = [(prefix + line) for line in source_string]
    elif suffix:
      result = [(line + suffix) for line in source_string]
    return '\n'.join(result)


def replace_slash_with_backslash(source_string):
  return re.sub(r'/', r'\\', source_string)


def escape_multiline_string(input_string):
  """
  ada 3 proses
  """
  # escaped_string = replace_single_backslash_with_double(input_string)
  escaped_string = input_string
  escaped_string = escaped_string.replace('\n', '\\n').replace('\t', '\\t')
  escaped_string = replace_four_spaces_with_tabs(escaped_string) # jk ternyata gak diindent oleh \t tapi oleh 4 spaces
  return escaped_string


def multi_to_single_line(string):
  return escape_multiline_string(string)


def single_to_multi_line(string):
  return string.replace('\\n', '\n').replace('\\t', '\t')


from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
def inputify(text, outside_of_loop=False):  # outside_of_loop=True jk dipanggil dari luar session.prompt
  if '__INPUT__' in text:
    for _ in range(text.count('__INPUT__')):
      if outside_of_loop:  # jk gak bisa gunakan prompt toolkit
        masukan = input(f'Masukkan nilai untuk {text}')
      else:
        masukan = prompt(
          f'Give input value for {text}: ',
          placeholder=HTML('<style color="#888888">(Masukkan nilai pengganti __INPUT__)</style>'),
        )
      if masukan:
        text = text.replace('__INPUT__', masukan, 1)
  return text


def inputify_running(text, outside_of_loop=False):  # outside_of_loop=True jk dipanggil dari luar session.prompt
  if '__INPUT__' in text:
    current_prompt = text
    for _ in range(text.count('__INPUT__')):
      if outside_of_loop:
        masukan = input(f'Masukkan nilai untuk {current_prompt}')
      else:
        masukan = prompt(
          f'Give input value for {current_prompt}: ',
          placeholder=HTML('<style color="#888888">(Masukkan nilai pengganti __INPUT__)</style>'),
        )
      if masukan:
        _, current_prompt = [item.strip() for item in text.split('__INPUT__', 1)]
        text = text.replace('__INPUT__', masukan, 1)
  return text


def inputify_with_prompts(text, is_outside_loop=False):
    while '__INPUT__' in text:
        current_prompt = text.replace('__INPUT__', '{input_prompt}')
        if is_outside_loop:
            user_input = input(f'Enter a value for {current_prompt}: ')
        else:
            user_input = prompt(
                f'Enter a value for {current_prompt}: ',
                placeholder=HTML('<style color="#888888">(Enter a replacement for __INPUT__)</style>'),
            )
        if user_input:
            text = text.replace('__INPUT__', user_input, 1)
    return text


def varify_running(text, outside_of_loop=False):
    current_prompt = text
    # Find all occurrences of __VAR<digit>__ pattern using regular expression
    matches = re.findall(r'__VAR(\d+)__', text)
    matches = list(set(matches))
    # print('varify_running:', matches, 'outside_of_loop:', outside_of_loop, 'current_prompt:', current_prompt)
    # Iterate over each match
    for match in matches:
        var_name = f'__VAR{match}__'  # Construct the variable name
        if outside_of_loop:
            masukan = input(f'Masukkan nilai untuk {current_prompt}: ')
        else:
            masukan = prompt(
                f'Give input value for {current_prompt}: ',
                placeholder=HTML('<style color="#888888">(Masukkan nilai pengganti __VAR<digit>__)</style>'),
            )
        # Replace the variable with user input value
        if masukan:
            # current_prompt = current_prompt.replace(var_name, masukan, 1)
            # kita replace semua __VARn__ pada current_prompt
            current_prompt = current_prompt.replace(var_name, masukan)

    return current_prompt


def inputify_varify_running(text, outside_of_loop=True):
    return varify_running(
      inputify_with_prompts(text, outside_of_loop),
      outside_of_loop
    )


def clean_string(input_string, replacement='_'):
  # Define a translation table to replace punctuations with the specified character
  translation_table = str.maketrans(string.punctuation, replacement * len(string.punctuation))

  # Use translate method to perform the replacement
  cleaned_string = input_string.translate(translation_table)

  return cleaned_string


def test_clean_string():
  input_text = "Hello, this is a sample string! It has some punctuations."
  cleaned_text = clean_string(input_text)
  print(cleaned_text)


def sort_multiline_string(input_string):
  # Split the multiline string into a list of strings
  lines = input_string.split('\n')

  # Remove any empty strings from the list
  lines = [line.strip() for line in lines if line.strip()]

  # Sort the list of strings
  sorted_lines = sorted(lines)

  # Join the sorted strings back into a multiline string
  result_string = '\n'.join(sorted_lines)

  return result_string


def sort_and_remove_duplicates(input_string):
  # Split the multiline string into a list of strings
  lines = input_string.split('\n')

  # Remove leading and trailing spaces from each line
  lines = [line.strip() for line in lines]

  # Remove any empty strings from the list
  lines = [line for line in lines if line]

  # Remove duplicate lines while preserving the order
  unique_lines = list(dict.fromkeys(lines))

  # Sort the list of unique strings
  sorted_lines = sorted(unique_lines)

  # Join the sorted unique strings back into a multiline string
  result_string = '\n'.join(sorted_lines)

  return result_string


def test_sort_multiline_string():
  input_string = """apple
  banana
  grape
  orange
  """

  sorted_string = sort_multiline_string(input_string)
  print(sorted_string)


def detect_indentation(input_text):
  # Check if the input is a file path or a string
  if isinstance(input_text, str) and '\n' in input_text:
    lines = input_text.split('\n')
  else:
    # Assume it's a file path
    try:
      with open(input_text, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    except FileNotFoundError:
      return "File not found."

  # Patterns for detecting indentation
  tab_pattern = re.compile(r'^\t')
  two_space_pattern = re.compile(r'^ {2}')
  four_space_pattern = re.compile(r'^ {4}')

  # Counters for each type of indentation
  tab_count = 0
  two_space_count = 0
  four_space_count = 0

  for line in lines:
    if tab_pattern.match(line):
      tab_count += 1
    elif two_space_pattern.match(line):
      two_space_count += 1
    elif four_space_pattern.match(line):
      four_space_count += 1

  # Determine the dominant indentation
  max_count = max(tab_count, two_space_count, four_space_count)
  if max_count == tab_count:
    return "Detected indentation: Tab"
  elif max_count == two_space_count:
    return "Detected indentation: 2 spaces"
  else:
    return "Detected indentation: 4 spaces"


def test_detect_indentation():
  file_path = 'path/to/your/file.py'
  result = detect_indentation(file_path)
  print(result)


def insert_at_second_line_for_string(input_string, value, second_line=1):
  lines = input_string.split('\n')

  # Insert the value at the second line with the same indentation
  indentation = lines[second_line].split(lines[second_line].lstrip())[0]
  new_line = f"{indentation}{value}"
  lines.insert(second_line, new_line)

  result_string = '\n'.join(lines)
  print(f"Value {value} inserted at the second line of the string.")
  return result_string


def test_insert_at_second_line_for_string():
	input_string = """\
	def my_function():
			print("Hello, World!")

	# Rest of the code...
	"""
	result_string = insert_at_second_line_for_string(input_string, 1)
	print(result_string)


def insert_at_second_line_for_file(file_path, value, second_line=1):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      lines = file.readlines()

    # Insert the value at the second line with the same indentation
    indentation = lines[second_line].split(lines[second_line].lstrip())[0]
    new_line = f"{indentation}{value}\n"
    lines.insert(second_line, new_line)

    with open(file_path, 'w', encoding='utf-8') as file:
      file.writelines(lines)

    print(f"Value {value} inserted at the second line of the file.")
  except FileNotFoundError:
    print("File not found.")


def test_insert_at_second_line_for_file():
	file_path = 'path/to/your/file.py'
	insert_at_second_line_for_file(file_path, 1)


def remove_markdown_code(input_string):
  input_string = re.sub(r'^```.*$', '', input_string.strip(), flags=re.MULTILINE)
  return input_string


def extract_code(response: str) -> str:
  lines = response.strip().split('\n')

  # Check if the first line starts with ``` and the last line ends with ```
  if lines[0].startswith("```") and lines[-1].endswith("```"):
    # Count the total number of lines containing ```
    backtick_lines = sum(1 for line in lines if "```" in line)

    # Ensure there are only two lines with triple backticks
    if backtick_lines == 2:
      # Remove the first and last line
      return '\n'.join(lines[1:-1]).strip()

  # Return the original response if conditions are not met
  return response
