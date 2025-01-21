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
operation           : system_operation
	| database_operation
    | data_operation
    | channels_operation
system_operation	: "/sys"		-> query_system_information
database_operation	: read_information
	| write_operation
read_information: "/len"			-> database_size
	| "/length"					-> database_size
    | "/size"					-> database_size
    | "/i"						-> database_information
    | "/info"					-> database_information
write_operation: "/clr"			-> clear_database
	| "/clear"					-> clear_database
data_operation: range_operation
	| pattern_operation
range_operation: start_range? ":" end_range?
pattern_operation: HURUF_DIGIT 	// jangan dimulai /
channels_operation: "/l"		-> list_channels
	| channel_subscribe
    | channel_publish

// @kanal1,@kanal2/[avro]dict=username:usef,age:42
channel_publish: channels "/" wrapper_spec? type_spec? literal_data
channels: channel ("," channel)*
channel: "@" HURUF_DIGIT
wrapper_spec: "[" HURUF_DIGIT "]" 	// utk bs avro, protobuf
type_spec: HURUF_DIGIT "="			// dict=, list=, etc
literal_data: HURUF_DIGIT -> data_string // nanti bisa langsung eval() sesuai type_spec

// @kanal1/#
// @kanal1/c:/path/to/folder/file.py:function
// @kanal1/module.module.module.module.function
// how to handle?
channel_subscribe: channels "/" callback_spec
callback_spec: default_callback_spec		// print data to console
default_callback_spec: "#"

start_range: BILBUL
end_range: BILBUL
    
//operator opargs*
operator            : HURUF_DIGIT
opargs              : HURUF_DIGIT


HURUF_DIGIT: 			("_"|LETTER|DIGIT) 			("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 		("_"|LETTER|DIGIT) 			("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 			("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 			("_"|LETTER) 				("_"|LETTER|DIGIT|" "|".")*
HURUF_COMMA: 			("_"|LETTER) 				("_"|LETTER|DIGIT|",")*

HURUF_PASSWORD: 		("_"|LETTER) 				("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"#"|"*")*
HURUF_HOST: 			("_"|LETTER|DIGIT)			("_"|LETTER|DIGIT|".")*
{base_grammar}
"""
