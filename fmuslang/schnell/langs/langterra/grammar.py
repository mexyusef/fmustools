# from lang.ucsv.grammar.base import base_grammar

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
keseluruhan: database
| redis_statement

database: dbconfig? redis_statement
dbconfig						: "[" userpass? hostport? dbspec "]"
userpass						: user ":" pass "@"
hostport						: host? ":" port
user							: HURUF
pass							: HURUF_PASSWORD
host							: HURUF_HOST
port							: BILBUL
dbspec							: "/" dbnumber
dbnumber						: BILBUL

redis_statement     : statement (insn_separator statement)*
insn_separator      : NEWLINE
	| ";"
statement           : operation ("," operation)*
operation           : operator opargs*
operator            : HURUF_DIGIT
opargs              : HURUF_DIGIT


HURUF_DIGIT: 						("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 			("_"|LETTER) 				("_"|LETTER|DIGIT|" "|".")*
HURUF_COMMA: 			("_"|LETTER) 				("_"|LETTER|DIGIT|",")*

HURUF_PASSWORD: 	("_"|LETTER) 				("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"#"|"*")*
HURUF_HOST: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
{base_grammar}
"""
