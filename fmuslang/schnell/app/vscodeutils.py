import json, os
from .appconfig import programming_data
from .dirutils import joinhere, joiner, basename, isdir, isfile, does_exist, get_cwd, create_if_empty_dir
from .fileutils import file_content, file_write, get_definition_by_key_permissive_start, get_daftar
from .utils import perintah


# vscode_language_identifiers = programming_data['j']['schnell']['app']['vscodeutils']['vscode_language_identifiers']
# [
#     'bat',
#     'clojure',
#     # 'c',
#     'cpp',
#     'csharp',
#     'css',
#     'dockerfile',
#     'go',
#     'groovy',
#     'html',
#     'java',
#     'javascript',
#     'javascriptreact',
#     'json',
#     # 'makefile',
#     # 'markdown',
#     # 'perl',
#     # 'php',
#     # 'plaintext',
#     'python',
#     'r',
#     'ruby',
#     'rust',
#     'sass',
#     'scss',
#     'sql',
#     # 'swift',
#     'typescript',
#     'typescriptreact',
#     'vue',
#     'vue-html',
#     # 'xml',
#     # 'yaml',
# ]


def create_snippet(result, barisentry, content, diff_prefix=None):
	if diff_prefix is None:
		diff_prefix = programming_data['j']['schnell']['app']['vscodeutils']['vscode_snippet_prefix']
	title = diff_prefix + barisentry[:50] # jangan terlalu panjang
	description = barisentry # kasih prefix FM utk lihat perbedaan dg lainnya
	# kadang entry ada koma sblm space: nama, saya, adalah, wieke
	# prefix = [item.removesuffix(',').strip() for item in barisentry.split()]
	# upd, 31/8/2022, jangan displit lah
	prefix = barisentry[:50]
	body = content.splitlines()
	entry = {
		title: {
			'prefix': prefix,
			'body': body,
			'description': description
		}
	}
	result.update(entry)


def create_snippet_wrapper(input_filepath, base_folder=None, language=None):
	"""
	@params
	input_filepath
		mk file berisi bahasa misal /path/to/rs.mk
	base_folder
		/path/to/.vscode
	bahasa=None
		optional utk language snippet file (lang.json),
		default global snippet file (name.code-snippets)
	"""
	if not base_folder:
		base_folder = joiner(get_cwd(), '.vscode')

	create_if_empty_dir(base_folder) # buat /path/to/.vscode

	filename = os.path.basename(input_filepath)
	filename_without_extension, _ = os.path.splitext(filename)
	# if not language:
	#     language, _ = os.path.splitext(filename)
	# output_filepath = joiner(base_folder, language + '.code-snippets')
	if language and language in programming_data['j']['schnell']['app']['vscodeutils']['vscode_language_identifiers']:
		output_filepath = joiner(base_folder, language + '.json')
	else:
		output_filepath = joiner(base_folder, filename_without_extension + '.code-snippets')
	result = {}
	daftar = get_daftar(input_filepath)
	for barisentry in daftar:
		create_snippet(result, barisentry, get_definition_by_key_permissive_start(input_filepath, barisentry))

	# utk print
	jsonresult = json.dumps(result, indent=4)
	print(jsonresult)

	# tulis ke file
	original = {}
	if does_exist(output_filepath):
		original = json.loads(file_content(output_filepath))
	original.update(result)
	file_write(output_filepath, json.dumps(original, indent=4))
	return output_filepath


def vscode_edit_file(filepath):
	cmd = f'vscode {filepath}'
	# print('cmd dg --goto line:', cmd)
	# Arguments in `--goto` mode should be in the format of `FILE(:LINE(:CHARACTER))`
	# perintahsp_simple(cmd)
	perintah(cmd)


def vscode_edit_at_line(filepath, lineno):
	# from constants import vscode
	if not lineno or lineno < 0:
		lineno = 0

	cmd = f"vscode --goto \"{filepath}:{lineno}:1\""
	# print('cmd dg --goto line:', cmd)
	# Arguments in `--goto` mode should be in the format of `FILE(:LINE(:CHARACTER))`
	# perintahsp_simple(cmd)
	perintah(cmd)


def vscode_edit_fmus_at_entry(filepath, barisentry):
	pass
