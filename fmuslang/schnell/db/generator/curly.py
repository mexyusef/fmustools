import json, os, pyperclip, subprocess, sys
# import lark
# from lark import (
# 	Lark,
# 	InlineTransformer,
# )
import schnell.vendor.lark
from schnell.vendor.lark import (
	Lark,
	InlineTransformer,
)
from anytree import RenderTree

base_grammar = """
%import common.CNAME                -> HURUF
%import common.ESCAPED_STRING       -> KALIMAT
%import common.WORD
%import common.DIGIT
%import common.HEXDIGIT
%import common.LETTER
%import common.INT                  -> BILBUL
%import common.SIGNED_INT           -> BILBUL_BERTANDA
%import common.SIGNED_NUMBER        -> BIL_BERTANDA
%import common.FLOAT                -> PECAHAN
%import common.NEWLINE
%import common.WS
%ignore WS
"""

bahasa = f"""
keseluruhan: insn+

insn: url options? methods? headers? data?

options: "[" optionlist "]"
optionlist: option ("," option)*
option: "o=" HURUF_DIGIT_SPASI -> simpan_file
	| "auth=" HURUF_DIGIT_SPASI -> user_pass // format: auth=user:password

methods: method
method: "g"     -> method_get
	| "p"       -> method_post
	| "u"       -> method_put
	| "c"       -> method_patch
	| "d"       -> method_delete
	| "h"       -> method_head

headers: header ("," header)*
header: "json"  -> header_json
	| "raw"				-> header_raw
	| "txt"				-> header_text
	| "form"			-> header_form

data: "{{" keyvals "}}"					-> data_json
	| "<" ANYTHING_GOES ">"				-> data_raw_text
keyvals: keyval ("," keyval)*
keyval: key "=" val
key: HURUF_DIGIT_SPASI
val: HURUF_DIGIT_SPASI

url: HURUF_HOST

HURUF_DIGIT: 			("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 		("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@"|" "|"-"|":")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 			("_"|LETTER) ("_"|LETTER|DIGIT|" ")*
HURUF_COMMA: 			("_"|LETTER) ("_"|LETTER|DIGIT|",")*

ANYTHING_GOES:			("_"|LETTER|DIGIT|"*"|"/"|"."|"\\""|"{{"|"[") (LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|";"|"\\"|"\""|"{{"|"["|"}}"|"]")*

HURUF_SYSTEM: 			("_"|LETTER|DIGIT|"*"|"/"|"."|"\\"") (LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\"|"\"")*
HURUF_PASSWORD: 		("_"|LETTER) ("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"@"|"#"|"*")*
HURUF_HOST: 			("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|"@"|"/"|":"|"?"|"&"|"="|"-")*
{base_grammar}
"""

method_map = {
	'method_delete': 'DELETE',
	'method_get': 'GET',
	'method_head': 'HEAD',
	'method_patch': 'PATCH',
	'method_post': 'POST',
	'method_put': 'PUT',
}

header_map = {
	'header_json'	: "Content-type: application/json",
	'header_text'	: "Content-Type: text/plain",
	'header_raw'	: "Content-Type: text/plain",
	'header_form'	: "Content-Type: application/x-www-form-urlencoded",
}

class TheProcessor(InlineTransformer):
	def keseluruhan(self, *instructions):
		return instructions

if sys.platform == 'win32':
	DATA_QUOTER = '"'
	DATA_FIELD_QUOTER = '\\"'
else:
	DATA_QUOTER = "'"
	DATA_FIELD_QUOTER = '"'


initialized = None

def initialize():
	parser = Lark(bahasa, start='keseluruhan').parse
	initialized = parser
	# print('...initialized.')
	return parser


def get_instructions(code):

	if not initialized:
		parser = initialize()
	else:
		parser = initialized

	print('='*10, code, '\n')
	parsed_tree = parser(code)
	instructions = TheProcessor().transform(parsed_tree)
	return instructions


def perintahsp_outerr(complete_command):
	cmdlist = complete_command.split()
	print(f'perintahsp_outerr: [{complete_command}] => {cmdlist}')
	output = subprocess.run(complete_command, capture_output=True, shell=True)
	_stdout = output.stdout.decode('utf8')
	_stderr = output.stderr.decode('utf8')
	# if _stdout is None:
	# 	_stdout = ''	
	# print(f'curl stdout [{_stdout}], stderr [{_stderr}]')
	return _stdout, _stderr


def process_language(code, force=False):
	instructions = get_instructions(code)

	# print('<<process_language')
	curls = ''
	for insn in instructions: # instructions adlh tuple
		for tree in insn.children: # insn adlh Tree
			
			# print('<<<', type(tree))
			print(tree.pretty())
			# print('>>>')

			if tree.data == 'url':
				url = str(tree.children[0])
				if not url .startswith('http'):
					url = 'http://' + url
				curls += url
			elif tree.data == 'options':
				'''
				options: "[" optionlist "]"
				optionlist: option ("," option)*
				option: "o=" HURUF_DIGIT_SPASI -> simpan_file
				'''
				tree_optionlist = tree.children[0]
				for tree_option in tree_optionlist.children:
					if tree_option.data == 'simpan_file':
						filename = str(tree_option.children[0])
						simpan_file = f" --output {filename} "
						# input(f'simpan file adlh: [{simpan_file}] ...press... ')
						curls += simpan_file
					elif tree_option.data == 'user_pass':
						'''
						/y. alamat [auth=user:pass,o=index.html]
						'''
						up = str(tree_option.children[0])
						username, password = up.split(':')
						user_pass = f" --user \"{username}:{password}\" "
						input(f'user_pass adlh: [{user_pass}] ...press... ')
						curls += user_pass
			elif tree.data == 'methods':
				method = tree.children[0].data
				curls += ' -X ' + method_map[method]
			elif tree.data == 'headers':
				header = tree.children[0].data
				curls += ' -H "' + header_map[header] + '"'
			elif tree.data  == 'data_json':
				'''
				bisa json atau raw/text yg diapit ""
				data: "{{" keyvals "}}"					-> data_json
				| "\"" ANYTHING_GOES "\""				-> data_raw_text
				'''
				print('<<<<')
				# print('cek anytree:', RenderTree(tree))
				print('cek data_json:')
				print(tree)
				print('>>>>')
				keyvals = tree.children[0]
				kvpair = []
				for kv in keyvals.children:
					kunci = kv.children[0]
					nilai = kv.children[1]
					k = str(kunci.children[0])
					v = str(nilai.children[0])
					bentukan = f'{DATA_FIELD_QUOTER}{k}{DATA_FIELD_QUOTER}: {DATA_FIELD_QUOTER}{v}{DATA_FIELD_QUOTER}'
					if v.isdigit():
						bentukan = f'{DATA_FIELD_QUOTER}{k}{DATA_FIELD_QUOTER}: {v}'

					kvpair .append(bentukan)
				
				curldata = f' -d {DATA_QUOTER}{{ {", ".join(kvpair)} }}{DATA_QUOTER}'
				curls += curldata
			
			elif tree.data == 'data_raw_text':
				'''
				ini blm ditest

				http://localhost:9001/rest/books -X POST -H "Content-Type: text/plain"

				curl --location --request POST 'http://localhost:9001/rest/books/' \
				--header 'Content-Type: text/plain' \
				--data-raw '{
						allBooks {
								isn
								title
						}
				}'
				'''
				textdata = tree.children[0]
				curldata = f' --data-raw {DATA_QUOTER}{textdata}{DATA_QUOTER}'
				curls += curldata

	print('curl args:', curls)
	print()
	# print('process_language>>')

	out = ''
	err = ''

	# upd: tambah -L utk follow redirect
	command = f"curl -L {curls}"
	if not force:
		yesno = input(f'Proceed to execute {command} y[n]?\n')
		if yesno == 'y':
			out, err = perintahsp_outerr(command)
	else:
		out, err = perintahsp_outerr(command)

	# print('output:', out)
	# print('err:', err)
	return out, err

if __name__ == '__main__':
	cmd = 'localhost:8080/urls p json {name=usef}'
	process_language(cmd, True)
