tambahan = """
HURUF_DIGIT: 			      ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 		  ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_SPACE: 			      ("_"|LETTER) 		    ("_"|LETTER|DIGIT|" ")*
HURUF_COMMA: 			      ("_"|LETTER) 		    ("_"|LETTER|DIGIT|",")*
HURUF_PASSWORD: 		    ("_"|LETTER)        ("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"@"|"#"|"*")*
HURUF_HOST: 			      ("_"|LETTER|DIGIT)  ("_"|LETTER|DIGIT|"."|"@")*
HURUF_FOLDER: 				  ("_"|LETTER|DIGIT|"/"|".") 	          ("_"|LETTER|DIGIT|"."|":"|"/"|"-"|"+"|" ")*
HURUF_SYSTEM: 			    ("_"|LETTER|DIGIT|"*"|"/"|"."|"\\"") 	(LETTER|DIGIT|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\"|"\"")*
HURUF_FOLDER_LAMA_BERBINTANG:   ("_"|LETTER|DIGIT|"/"|".") 	("_"|LETTER|DIGIT|"."|"-"|"/"|","|" "|"*")*
HURUF_FOLDER_LAMA_BERBINTANG_NOSPACE:   ("_"|LETTER|DIGIT|"/"|".") 	("_"|LETTER|DIGIT|"."|"-"|"/"|","|"*"|"~")*
"""

base_grammar = f"""
{tambahan}

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
