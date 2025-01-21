
from .base import base_grammar

data_grammar = f"""
keseluruhan             : insn+
insn                    : data_insn
data_insn               : "data" datanumber tablename column (column)*
datanumber              : BILBUL
| "rnd"                 -> random
| "rnd" "(" BILBUL ")"  -> varrandom
tablename               : HURUF
column                  : columnname ":" columntype
columnname              : HURUF
columntype              : string_type (":" string_subclass_type)*
| number_type (":" number_subclass_type)*
| date_type (":" date_subclass_type)*
| bcrypt_type ":" bcrypt_value


string_type: "s"            -> string
| "s" "(" BILBUL ")"        -> varchar
string_subclass_type: "n"	  -> name
| "fn"					            -> first_name
| "ln"					            -> last_name
| "e"					              -> email
| "F"					              -> name_female
| "M"					              -> name_male
| "p"					              -> password
| "u"					              -> simple_profile
| "city"				            -> city
| "country"				          -> country
| "color"				            -> color_name
| "j"					              -> job
| "c"					              -> company
| "a"					              -> address
| "ua"					            -> user_agent
| "T"                       -> text
| "w"                       -> word
| "W"                       -> words
| "t"                       -> sentence
| "lang"              	    -> language_name
| "loc"              	      -> locale
| "ph"					            -> phone_number
| "ccc"					            -> country_calling_code
| "cc"					            -> credit_card_number
| "ccf"					            -> credit_card_full
| "m"					              -> msisdn
| "ssn"					            -> ssn

number_type: "i"			      -> number
number_subclass_type: "ph"	-> phone_number
| "ccc"					            -> country_calling_code
| "cc"					            -> credit_card_number
| "ccf"					            -> credit_card_full
| "m"					              -> msisdn
| "ssn"					            -> ssn
| "rn" numdigits?	          -> random_number
| "ri" min_max? 		        -> random_int				
// python data.py gen data 1 meja hitung:i:ri(-50,60)
| "rd"					            -> random_digit	
| "f"					              -> pyfloat
| "d"					              -> pydecimal
| "i"					              -> pyint
| "b"                       -> pybool
| "coord"				            -> coordinate
| "lat"					            -> latitude
| "long"				            -> longitude
| "ll"					            -> latlng
| "lll"					            -> local_latlng
| "lol"					            -> location_on_land

date_type: "d"				      -> date
date_subclass_type: "b"		  -> simple_profile
| "dtb"					            -> date_time_between
| "iso"					            -> iso8601
| "ut"					            -> unix_time
| "dt"					            -> date_time
| "t"					              -> time

// password:b<rahasia>
bcrypt_type: "b"			      -> bcrypt
bcrypt_value: "<" HURUF_PASSWORD ">"

min_max: "(" min ("," max)? ")"
min: BILBUL_BERTANDA
max: BILBUL_BERTANDA
numdigits: "(" BILBUL ")"

HURUF_COMMA: ("_"|LETTER) ("_"|LETTER|DIGIT|",")*
HURUF_PASSWORD: ("_"|LETTER) ("_"|LETTER|DIGIT|" "|"&"|"."|","|"-"|"+"|"@")*

{base_grammar}
"""
