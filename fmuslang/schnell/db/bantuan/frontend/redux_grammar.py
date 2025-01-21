# from creator.grammar.base import base_grammar

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

redux_grammar = f"""
keseluruhan: statement (statement_separator statement)*
statement: store_statement
| reducer_statement
| action_statement

statement_separator: ";"

store_statement       : "dummy"
reducer_statement     : "dummy"
action_statement      : "@" action_types_statement

action_types_statement: action_type ("," action_type)*
action_type: action_type_compound_left
| action_type_compound_right
| action_type_simple

action_type_compound_left: "{{" part_items "}}" part_shared
action_type_compound_right: part_shared "{{" part_items "}}" 


action_type_simple: HURUF_DIGIT
part_shared: HURUF_DIGIT
part_items: part_item ("," part_item)*
part_item: HURUF_DIGIT

HURUF_DIGIT: 			      ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 		  ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
{base_grammar}
"""
