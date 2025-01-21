import os, sys, pathlib, traceback
__curfile__ = pathlib.Path(__file__).resolve()
sidoarjodir = __curfile__.parent.parent.parent
sys.path.append(str(sidoarjodir))
import schnell.vendor.lark as lark
from schnell.vendor.lark import Lark
from schnell.vendor.lark.indenter import Indenter
from schnell.app.appconfig import programming_data
from schnell.app.fileutils import append_file, file_content

class PythonIndenter(Indenter):
	NL_type = '_NEWLINE'
	OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
	CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
	INDENT_type = '_INDENT'
	DEDENT_type = '_DEDENT'
	tab_len = 4

pohon = lark.tree.Tree
token = lark.lexer.Token
ispohon = lambda i: isinstance(i, pohon)
istoken = lambda i: isinstance(i, token)

kwargs = dict(postlex=PythonIndenter(), start='file_input')
grammar_file = 'py.grammar'
chosen_parser = Lark.open(grammar_file, rel_to=__file__, parser='lalr', **kwargs)

current_class = None

function_calls = []

dependency_graph = {}

def parameters(suite):
	"""
	parameters
		name        x
		name        w
		name        b
		None
		None
		None
	"""
	params = []
	for param in suite.children:
		if param is None:
			continue
		if isinstance(param, token):
			# print(f'\n\n*** ketemu token "{str(param)}"\n\n')
			params.append(param)
		elif param.data == 'name':
			arg = param.children[0]
			params.append(str(arg))
		elif param.data == 'paramvalue':
			# ada name dan value
			paramname = str(param.children[0].children[0])
			paramtype = param.children[1].data
			if param.children[0].data == 'typedparam':
				itemnametree = param.children[0].children[0]
				itemname = itemnametree.children[0]
				itemtype = 'getattr'
				if param.children[0].children[1].data == 'getitem':
					itemtype = 'getitem'
				params.append(f"{itemname}:{itemtype}")
			elif paramtype in ['string', 'number']:
				paramvalue = str(param.children[1].children[0])
				# params.append(f"paramvalue {paramname}|type {paramtype}|value {paramvalue}")
				params.append(f"{paramname}: {paramtype} = {paramvalue}")
			elif paramtype in ['list', 'tuple']:
				values = []
				for paramitem in param.children[1].children:
					values.append(str(paramitem.children[0]))
				# params.append(f"paramvalue {paramname}|type {paramtype}|value {', '.join(values)}")
				params.append(f"{paramname}: {paramtype} = [{', '.join(values)}]")
				# print(param)
			elif paramtype in ['dict']:
				values = []
				for paramitem in param.children[1].children:
					# values.append(str(paramitem.children[0]))
					itemname = str(paramitem.children[0].children[0])
					itemvalue = str(paramitem.children[1].children[0])
					values.append(f"{itemname}: {itemvalue}")
				params.append(f"{paramname}: {paramtype} = {{ {', '.join(values)} }}")
		elif param.data == 'starparams':
			for starparam_or_postparam in param.children:
				if starparam_or_postparam.children[0] is None:  # Tree(Token('RULE', 'poststarparams'), [None])])]),
					continue
				# print('starparam', starparam_or_postparam)
				paramname = str(starparam_or_postparam.children[0].children[0])
				params.append(f"args*: {paramname}")
			# ada_args = True
		elif param.data == 'kwparams':
			for kwname in param.children:
				paramname = str(kwname.children[0])
				params.append(f"kw**: {paramname}")
			# ada_kwargs = True
		elif param.data == 'typedparam':
			itemname = str(param.children[0].children[0])
			itemtype = 'getattr'
			if param.children[1].data == 'getitem':
				itemtype = 'getitem'
			params.append(f"{itemname}: {itemtype}")
	return params

def arguments_list(suite):
	retval = []
	for item in suite.children:
		if item.data == 'var':
			item = str(item.children[0].children[0])
			retval.append(item)
	return retval

def arguments_factor(suite):
	retval = ''
	for item in suite.children:
		if istoken(item):
			retval += str(item)
		elif item.data == 'number':
			retval += str(item.children[0])
	return int(retval)

def arguments(suite):
	retval = []
	for item in suite.children:
		if item.data == 'var':
			arg = str(item.children[0].children[0])
			retval.append(arg)
		elif item.data == 'list':
			arg_list = arguments_list(item)
			# retval += arg_list
			retval.append(arg_list)
		elif item.data == 'factor':
			arg_factor = arguments_factor(item)
			retval.append(arg_factor)
	return retval

def func_name(item):
	retval = ''
	# for item in suite.children:
	if item.data == 'var':
		retval = str(item.children[0].children[0])
	elif item.data == 'getattr':
		class_name = str(item.children[0].children[0].children[0])
		method_name = str(item.children[1].children[0])
		retval = f"{class_name}.{method_name}"
	return retval

def funccall(suite, add_to_dependency_graph=None, dependency_graph_parent=''):
	"""
	"""
	function_name, function_args = '', []
	for item in suite.children:
		if isinstance(item, pohon):
			if item.data in ['getattr', 'var']:
				function_name = func_name(item)
			# elif item.data == 'getattr':
			#     function_name = func_name(item)
			elif item.data == 'arguments':
				function_args = arguments(item)
	return function_name, function_args

def arith_expr(suite):
	retval = []
	value = ''
	for item in suite.children:
		if istoken(item):
			arg = str(item)
			# retval.append(arg)
			if arg == '+':
				value += (',' if value else '') + 'torch.add'
			elif arg == '-':
				value += (',' if value else '') + 'torch.sub'
			elif arg == '*':
				value += (',' if value else '') + 'torch.matmul'
			elif arg == '/':
				value += (',' if value else '') + 'torch.div'
		elif item.data == 'var':
			arg = str(item.children[0].children[0])
			retval.append(arg)
		elif item.data == 'term':
			args, val = assign_term(item)  # val = mul
			if value:
				value += ',' + val
			else:
				value = val
			retval += args
			# arg = str(item.children[0].children[0])
			# retval.append(arg)
			# elif item.data == 'term':
			#     args, val = assign_term(item)
			#     dependency_graph[function_name][left_hand_side_name]['value'] = val
			#     dependency_graph[function_name][left_hand_side_name]['depends'] = args
	return retval, value

def assign_term(suite):
	retval = []
	value = ''
	for item in suite.children:
		if istoken(item):
			arg = str(item)
			# retval.append(arg)
			if arg == '+':
				value = 'torch.add'
			elif arg == '-':
				value = 'torch.sub'
			elif arg == '*':
				value = 'torch.matmul'
			elif arg == '/':
				value = 'torch.div'
		elif item.data == 'var':
			arg = str(item.children[0].children[0])
			retval.append(arg)
	return retval, value

def assign(suite, function_name, function_parameters):
	left_hand_side_name = ''
	for item in suite.children:
		if isinstance(item, pohon):
			if item.data == 'var':
				left_hand_side_name = str(item.children[0].children[0])
				dg_item = {
					'type': 'assign',
					'name': left_hand_side_name,
					'value': '',
					'depends': [],
				}
				# dependency_graph.append(dg_item)
				# dependency_graph[left_hand_side_name] = dg_item
				dependency_graph[function_name][left_hand_side_name] = dg_item
			elif item.data == 'arith_expr':
				args, val = arith_expr(item)
				dependency_graph[function_name][left_hand_side_name]['value'] = val
				dependency_graph[function_name][left_hand_side_name]['depends'] = args
			elif item.data == 'term':
				args, val = assign_term(item)
				dependency_graph[function_name][left_hand_side_name]['value'] = val
				dependency_graph[function_name][left_hand_side_name]['depends'] = args
			elif item.data == 'funccall':
				name, args = funccall(item, add_to_dependency_graph=True, dependency_graph_parent=left_hand_side_name)
				dependency_graph[function_name][left_hand_side_name]['value'] = name
				dependency_graph[function_name][left_hand_side_name]['depends'] = args

def return_arith_expr(suite, function_name, function_parameters=[]):
	"""
	dependency_graph[function_name][dependency_name]['value'] = val
	dependency_graph[function_name][dependency_name]['depends'] = args
	"""

	items = []
	current_operator = ''
	current_term_operator = ''

	retval = []
	value = ''
	for item in suite.children:
		if istoken(item):
			arg = str(item)
			# retval.append(arg)
			if arg == '+':
				current_operator = 'torch.add'
			elif arg == '-':
				# value += (',' if value else '') + 'torch.sub'
				current_operator = 'torch.sub'
			elif arg == '*':
				# value += (',' if value else '') + 'torch.matmul'
				current_operator = 'torch.matmul'
			elif arg == '/':
				# value += (',' if value else '') + 'torch.div'
				current_operator = 'torch.div'


			if current_operator not in dependency_graph[function_name]:
				dependency_graph[function_name][current_operator] = {
					'value': current_operator,
					'depends': [],
				}
			else:
				i = 1
				current_operator = f"{current_operator}_{i}"
				while current_operator in dependency_graph[function_name]:
					i += 1
					current_operator = f"{current_operator}_{i}"
				dependency_graph[function_name][current_operator] = {
					'value': current_operator,
					'depends': [],
				}
			if current_term_operator:
				dependency_graph[function_name][current_operator]['depends'].append(current_term_operator)
			dependency_graph[function_name]['__output__']['depends'].append(current_operator)
		elif item.data == 'var':
			arg = str(item.children[0].children[0])
			# retval.append(arg)
			if current_operator:
				dependency_graph[function_name][current_operator]['depends'].append(arg)
			else:
				print(f"""var dalam arithmetic
				arg = {arg}
				function_name = {function_name}
				""")
		elif item.data == 'term':
			args, val = assign_term(item)  # val = mul
			# if value:
			#     value += ',' + val
			# else:
			#     value = val
			# retval += args

			term_operator = 'torch.matmul'
			if term_operator not in dependency_graph[function_name]:
				dependency_graph[function_name][term_operator] = {
					'value': term_operator,
					'depends': args,
				}
			else:
				i = 1
				term_operator = f"torch.matmul_{i}"
				while term_operator in dependency_graph[function_name]:
					i += 1
					term_operator = f"torch.matmul_{i}"
				dependency_graph[function_name][term_operator] = {
					'value': term_operator,
					'depends': args,
				}
			if current_operator:
				dependency_graph[function_name][current_operator]['depends'].append(term_operator)
			else:
				current_term_operator = term_operator

	return retval, value

def return_stmt(suite, function_name, function_parameters):
	dependency_name = '__output__'
	dependency_graph[function_name][dependency_name] = {}

	for item in suite.children:
		if isinstance(item, pohon):
			if item.data == 'var':
				depends = str(item.children[0].children[0])
				dg_item = {
					'type': 'return',
					'name': dependency_name,
					'depends': [depends],
				}
				# dependency_graph.append(dg_item)
				# dependency_graph[name] = dg_item
				dependency_graph[function_name][dependency_name] = dg_item
			elif item.data == 'funccall':
				# funccall(item, add_to_dependency_graph=True)
				# funccall(item)
				name, args = funccall(item)
				# if dependency_name not in dependency_graph[function_name]:
				#     dependency_graph[function_name][dependency_name] = {}
				dependency_graph[function_name][dependency_name]['value'] = name
				dependency_graph[function_name][dependency_name]['depends'] = args
			elif item.data == 'arith_expr':
				# args, val = arith_expr(item)
				# dependency_graph[function_name][dependency_name]['value'] = val
				# dependency_graph[function_name][dependency_name]['depends'] = args
				dependency_graph[function_name]['__output__']['depends'] = []
				return_arith_expr(item, function_name)

def expr_stmt(suite, function_name, function_parameters):
	for item in suite.children:
		if isinstance(item, pohon):
			if item.data == 'funccall':
				funccall(item)

def assign_stmt(suite, function_name, function_parameters):
	for item in suite.children:
		if isinstance(item, pohon):
			if item.data == 'assign':
				assign(item, function_name, function_parameters)

def process_suite(suite, level=0, function_name='', function_parameters=[]):
	for item in suite.children:
		if isinstance(item, pohon):
			if item.data == 'assign_stmt':
				assign_stmt(item, function_name, function_parameters)
			elif item.data == 'expr_stmt':
				expr_stmt(item, function_name, function_parameters)
			elif item.data == 'return_stmt':
				return_stmt(item, function_name, function_parameters)

		if hasattr(item, 'children'):
			process_suite(item, level+1)

def funcdef(item, current_class=None):
	function_name, function_parameters, function_type, function_suite = '', [], {}, None

	for _item in item.children:
		if _item is None:
			continue
		if _item.data == 'name':
			function_name = str(_item.children[0])
			if current_class is not None:
				function_name = f"{current_class}.{function_name}"
			dependency_graph[function_name] = {}
		elif _item.data == 'parameters':
			function_parameters = parameters(_item)
			dependency_graph[function_name]['__input__'] = function_parameters
		elif _item.data == 'test':
			pass
		elif _item.data == 'pass_stmt':
			pass
		elif _item.data == 'suite':
			process_suite(_item, 0, function_name, function_parameters)

def process_tree(tree, level=0, function_name=''):

	global current_class

	if level==0:
		function_name = '__global__'

	for item in tree.children:
		if isinstance(item, pohon):
			if item.data == 'funcdef':
				pass
			elif item.data == 'funccall':
				pass
			elif item.data == 'assign_stmt':
				pass
		if hasattr(item, 'children'):
			process_tree(item, level+1)

def graph_compile_code(code, return_prettified=False):
	result = chosen_parser.parse(code + '\n')
	process_tree(result)
	prettified = result.pretty()
	if return_prettified:
		return prettified
	else:
		print(prettified)
	return True

def test_python_file(filepath=r'C:\Users\usef\work\sidoarjo\schnell\vendor\upython\patch_linecache.py', return_status=False):
	status = graph_compile_code(file_content(filepath), return_prettified=return_status)
	if return_status:
		return status

def file_to_parsetree(filepath=r'C:\Users\usef\work\sidoarjo\schnell\vendor\upython\patch_linecache.py', return_status=True):
	status = graph_compile_code(file_content(filepath), return_prettified=return_status)
	return status

tab_space4 = ' '*4
tab_space2 = ' '*2
tab_tab = '\t'
FOOTER = '--#'
HEADER = '--% '
INDEX = 'index/fmus'

def folder_to_parsetree(base_folder,
	output_fmus=None,
	TAB='',
	# dont_skip_binary=True,
	create_index=True,
	skip_dirs=None,
	skip_files=None,
	skip_ext=None):
	from schnell.app.printutils import indah4
	base_folder = os.path.normpath(base_folder)
	content_result = {}

	project_name = os.path.basename(base_folder)
	if not output_fmus:
		output_fmus = project_name + '.fmus'
	parent_base_folder = os.path.dirname(base_folder)
	output_filepath = os.path.join(parent_base_folder, output_fmus)
	startpath = base_folder

	print(f"[ivyutils][folder_to_parsetree] {startpath} => {output_filepath}")

	if not TAB:
		tab_ = programming_data['j']['schnell']['app']['fmusutils']['indent_for_reverse_fmus']
		if tab_ == 'space4':
			TAB = tab_space4
		elif tab_ == 'space2':
			TAB = tab_space2
		else:
			TAB = tab_tab
	if skip_dirs is None:
		skip_dirs = programming_data['j']['schnell']['app']['fmusutils']['skip_folders']
	if skip_files is None:
		skip_files = programming_data['j']['schnell']['app']['fmusutils']['skip_files']
	if skip_ext is None:
		skip_ext = programming_data['j']['schnell']['app']['fmusutils']['skip_extensions']

	for root, subdirs, files in os.walk(startpath, topdown=True):
		subdirs[:] = [d for d in subdirs if d not in skip_dirs]
		# files = [f for f in files if (not (f in skip_files) and not ([ext for ext in skip_ext if f.endswith(ext)]))]
		files = [f for f in files if f.endswith('.py')]

		if create_index:
			level = root.replace(startpath, '').count(os.sep)
			subindent = TAB * (level+1)
			indent = TAB * (level)
			# if level == 0:
			namadir = os.path.basename(root)
			if '@' in namadir or '[' in namadir or ']' in namadir:
				namadir = namadir.replace('@','__AT__').replace('[','__LK__').replace(']','__RK__')
			value = '%s%s,d(/mk)'%(indent, namadir)
			# if INDEX not in content_result:
			# 	content_result[INDEX] = [value]
			# else:
			# 	content_result[INDEX].append(value)
			if INDEX not in content_result:
				content_result[INDEX] = value

		for filename in files:
			fullpath = os.path.join(root, filename)
			# file_entry(subindent, f, fullpath, startpath)
			relative = os.path.relpath(fullpath, startpath).replace('\\', '/')
			try:
				nilai_parsing_python_file = file_to_parsetree(fullpath, return_status=True)
				indah4(f"""nilai_parsing_python_file = file_to_parsetree(fullpath, return_status=True)\nfullpath = [{fullpath}]\nnilai_parsing_python_file = [{nilai_parsing_python_file[:50]}]""", warna='cyan')
			except Exception as err:
				indah4(f"""GAGAL nilai_parsing_python_file = file_to_parsetree(fullpath, return_status=True) => [{fullpath}]""", warna='cyan')
				print(err)
				trace = traceback.format_exc()
				print(trace)
				continue

			content_result[relative] = nilai_parsing_python_file
			if create_index:
				text_binary = 'e' # 'b64' if biner else 'e'
				filerepr = f'{filename},f({text_binary}=__FILE__={relative})'
				value = "%s%s" % (subindent, filerepr)  # subindent sudah diassign di if create_index sblmnya
				if INDEX not in content_result:
					content_result[INDEX] = [value]
				else:
					content_result[INDEX].append(value)

	for k in content_result.keys():
		# lines = content_result[k]
		stringified = content_result[k]
		# stringified = '\n'.join(lines).rstrip()
		header = HEADER + (project_name + '/' if k!=INDEX else '') + k
		entry = f"{header}\n{stringified}\n{FOOTER}\n\n"
		append_file(output_filepath, entry)

	print(f'[ivyutils][folder_to_parsetree] "{base_folder}" => "{output_filepath}" done.')

if __name__ == '__main__':
	file_to_parsetree()
