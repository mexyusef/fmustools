--% getting started
ada 2 versi yg kita buat...lokasi dimana saja nih?

chartlang:
from app.transpiler.frontend.main import process_language

dotlang:
own lang -> bisa publish

imagelang:
from app.transpiler.frontend.main import process_language

tuilang:
from app.transpiler.frontend.main import process_language

tviewlang:
from app.transpiler.frontend.main import process_language

1.   #...      replservice_helper/declarative
2.   "creator.grammar.grammar" => creator.grammar.decl ada transformer stlh <tag[key=val...]*cdata()
3.   cdata adlh *something, ini berbeda dg decl dari frontend di bawah berikut
4. app.specialcmd:     decl...
5. creator.repl: decl
6. creator.declarative.handler
7.              declarative_program
8.                      declaratives___

dari creator.repl (THE repl)
elif text == 'decl':
self.generate_declarative_program(self.pohon)

from creator.declarative import root_declarative
self.pohon = root_declarative(insn)
--#

--% app.transpiler.frontend.bahasa, cdata dg |
declarative_program: declarative_element (declarative_element)*

declarative_element: "<" element_name element_config? cdata_text? element_children?

element_name: HURUF_DIGIT
element_config_separator: ","

element_config: "[" element_config_item (element_config_separator element_config_item)* "]"

element_config_item: HURUF_DIGIT  -> item_key_value_boolean
  | item_key "=" item_value       -> item_key_value

element_children: "(" declarative_program ")"
item_key: HURUF_DIGIT
item_value: HURUF_NILAI
cdata_text: "|" HURUF_CDATA
transformer: transform_value (transform_value)*
transform_value: "'" -> tx_single
| "\\"" -> tx_double
| "'d" -> tx_double
| "'c" -> tx_braces
| "'k" -> tx_brackets
| "'p" -> tx_parentheses
--#

--% creator.grammar.decl, cdata dg *
declaratives___: element (element)*
element: "<" element_name element_config? cdata_text? frontend_usage? element_children?
  | frontend_usage
element_name: HURUF_DIGIT transformer?
element_config: "[" element_config_item ("," element_config_item)* "]"
element_config_item: HURUF_DIGIT
| item_key "=" item_value       -> item_key_value

element_children: "(" declaratives___ ")"
item_key: HURUF_DIGIT
item_value: HURUF_DIGIT_SPASI transformer?

cdata_text: "*" HURUF_DIGIT
frontend_usage : "@@" "[" HURUF_FOLDER "]"

// [k=v'd], [k=v'-] hasilkan - something
transformer: transform_value (transform_value)*
transform_value: "'" -> tx_single
| "''" -> tx_double
| "'d" -> tx_double
| "'c" -> tx_braces
| "'k" -> tx_brackets
| "'p" -> tx_parentheses
| "'-" -> tx_prepend_minus
| "'A" -> tx_capitalize
| "'l" -> tx_lower
| "'u" -> tx_upper
--#

--% creator.grammar.grammar
keseluruhan: insn+

insn: dirspec* filespec*
  | programs
  | browse_program
  | video_program  

//  | django_project

dirspec: "dir" dirconfig?
  | "dir" dirconfig? "(" dirspec* filespec* ")"
dirconfig: "[" HURUF_FOLDER "]"

dirname: HURUF_FOLDER

// sementara declarative dan imperative/functional terpisah
filespec: "F" fileconfig? programs?
  | "f" fileconfig? programs?
  | "DF" fileconfig? declaratives___?      -> declarative_program

di dalam creator.repl, fungsi generate_program
for insn in instructions: # instructions adlh tuple
    if insn.data == 'declarative_program':
        '''
        insn: insn
            declarative_program
                fileconfig  yaml
                declaratives___
                    element
                        element_name    apiVersion
                        cdata_text      v1
        '''
        from creator.declarative import root_declarative
        self.pohon = root_declarative(insn)
        self.program_mode = 'declarative'
        return 'declarative'
--#

--% creator.declarative.handler
def generate_program(insn, as_service=False):
	pohon = AnyNode(name='root', type='root', value='declarative')
	"""
	repl.py#1674
	if insn.data == 'declarative_program':
		from creator.declarative import root_declarative/generate_program
		self.pohon = root_declarative(insn)

	DF...code...
	DF[yaml]...code...
	insn: insn
		declarative_program
			fileconfig  yaml
			declaratives___
				element
					element_name    apiVersion
					cdata_text      v1
	"""
	check_yaml = insn.children[0]
	delimiter = DELIMITER_SAMADENGAN
	yaml_mode=False
	json_mode=False
	if check_yaml.data == 'fileconfig':
		check_yaml_value = str(check_yaml.children[0])
		if check_yaml_value == 'yaml':
			delimiter = DELIMITER_KOLON
			yaml_mode=True
		elif check_yaml_value == 'json':
			delimiter = DELIMITER_KOLON
			json_mode=True

    process_declarative_program(insn.children, pohon, delimiter=delimiter, first_time=True)

	# print(findall(self.pohon, lambda node: hasattr(node, 'original')))
	assign_level(pohon)
	create_closing_tags(pohon)
	reindex(pohon)

	# if self.config.run_configuration['print_after_process']:
	generated_code = generate_declarative_program(pohon, yaml_mode=yaml_mode, json_mode=json_mode)
	if as_service:
		return pohon, generated_code
	return pohon
--#

--% chartlang
from app.transpiler.frontend.main import process_language
--#

--% dotlang
own lang -> bisa publish
--#

--% imagelang
from app.transpiler.frontend.main import process_language
--#

--% tuilang
from app.transpiler.frontend.main import process_language
--#

--% tviewlang
from app.transpiler.frontend.main import process_language
--#

