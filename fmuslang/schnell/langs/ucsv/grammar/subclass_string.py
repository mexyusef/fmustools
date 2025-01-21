
string_subclass_type = """string_subclass_type: "n"	  -> name
| "fn"					            -> first_name
| "ln"					            -> last_name
| "e"					              -> email
| "F"					              -> name_female
| "M"					              -> name_male
| "p"					              -> password
| "b" "<" HURUF_PASSWORD ">" 	-> bcrypt_value
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
"""
