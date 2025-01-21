# <satu<dua<tiga/config/(children)

declarative_program = """
declarative_program: declarative_element (declarative_element)*

declarative_element: "<" element_name element_config? cdata_text? element_children?

element_name: HURUF_DIGIT
element_config_separator: ","
element_config_separator2: "/"

element_config: "[" element_config_item (element_config_separator2 element_config_item)* "]"

element_config_item: HURUF_DIGIT  -> item_key_value_boolean
  | item_key "=" item_value       -> item_key_value

element_children: "(" declarative_program ")"

item_key: HURUF_DIGIT

// HURUF_NILAI -> x=1/2/3/4/5
// HURUF_NILAI_COMMA -> x=1,2,3,4,5
item_value: HURUF_NILAI_COMMA

cdata_text: "|" HURUF_CDATA

transformer: transform_value (transform_value)*
transform_value: "'" -> tx_single
| "\\"" -> tx_double
| "'d" -> tx_double
| "'c" -> tx_braces
| "'k" -> tx_brackets
| "'p" -> tx_parentheses
"""

huruf_berbeda = """
HURUF_CDATA: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|" "|";"|":"|"+"|"-"|","|"!")*
HURUF_DIGIT_COMMA: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|",")*
// bisa slash, gak bisa comma
HURUF_NILAI: ("_"|LETTER|DIGIT|"\\""|"{"|"."|"'") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|":"|"/"|"-"|"?")*
// pilih comma atau slash, kita pilih komma
HURUF_NILAI_COMMA: ("_"|LETTER|DIGIT|"\\""|"{"|"."|"'") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|":"|"-"|"?"|",")*
HURUF_NILAI_BERSLASH: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/")*
HURUF_NILAI_BERSPASI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|"`"|"{"|"}"|"("|")"|"="|">"|" ")*
HURUF_NON_OPEN: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|","|" "|"+"|"="|"-"|"_"|"@"|"#"|"$"|"%"|"^"|"&"|"*")*
HURUF_KODE_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{"|"<") 	("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/")*
"""

huruf = """
HURUF_DIGIT: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
"""

from langs import base_grammar

#<PersistGate /loading={<FullScreen Berspasi>},persistor={persistor}/
#<PersistGate $loading={<FullScreen />},persistor={persistor}$
#<PersistGate $loading={<FullScreen />},persistor={persistor}$bertulisan sblm children
#<a<b<c
#<a<b<c(<d<e)
#<a/disabled=true,onClick={()=>Mycomponent}/(<b)
# <a(<b<c(<e(<g(<i(<j<k/disabled/<l))<h)<f)<d)
#<a/disabled, nama=kuda, onClick={handleMe}/
#<a/disabled/ini adlh tulisanku untukmu
#<a/disabled/ini adlh tulisanku untukmu(<b(<c))
bahasa = f"""
{declarative_program}

{huruf_berbeda}

{huruf}

{base_grammar}
"""
