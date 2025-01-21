bahasa_header = """
program: statement+
statement: expression+ statement_terminator
expression: html_elements
statement_terminator: ";"
  |

html_elements: html_element+
html_element: "<" html_tag_start_name html_attribute* ">" html_content "<""/" html_tag_closing_name ">"
  | "<" html_tag_name html_attribute* html_content "/"">"
  | "<" html_tag_name html_attribute* "/"">"
  | "<" html_tag_name html_attribute* ">"

html_content: html_char_data? (html_element html_char_data?)*

html_tag_start_name: html_tag_name

html_tag_closing_name: html_tag_name

html_tag_name: HURUF_DIGIT

html_attribute: html_attribute_name "=" html_attribute_value
  | html_attribute_name
//| "'" html_attribute_name "=" html_attribute_value_berspasi

html_attribute_name: identifier

html_char_data: HURUF_NON_OPEN
html_attribute_value: HURUF_NILAI
  | "'" HURUF_NILAI_BERSPASI "'" -> diapit_sq
  | "\\"" HURUF_NILAI_BERSPASI "\\"" -> diapit_dq
html_attribute_value_berspasi: HURUF_NILAI_BERSPASI
identifier: HURUF_DIGIT
"""
#<View style={styles.container} onClick={()=>console.log(`hello`)}/>
#<View berspasi="aku adalah insan yang tak punya" style={styles.container} onClick={()=>console.log(`hello`)}/>
huruf = """
HURUF_DIGIT: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
HURUF_NILAI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|","|"\\""|"'"|"`"|"{"|"}"|"("|")"|"="|">")*
HURUF_NILAI_BERSPASI: ("_"|LETTER|DIGIT|"\\""|"{") 	("_"|LETTER|DIGIT|"."|","|"`"|"{"|"}"|"("|")"|"="|">"|" ")*
HURUF_NON_OPEN: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|"."|","|" "|"+"|"="|"-"|"_"|"@"|"#"|"$"|"%"|"^"|"&"|"*")*
"""
#<html><head><title>ini judul</title></head><body><main><section classname="whateve"></section></main></body></html>
#<html><head><title>ini judul</title></head><body><main><section classname="whateve"></section><br/><h1>ini h1</h1><hr/></main></body></html>
from langs import base_grammar

bahasa = f"""
{bahasa_header}

{huruf}

{base_grammar}
"""
