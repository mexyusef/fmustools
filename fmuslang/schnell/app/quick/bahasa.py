from schnell.langs import base_grammar

"""IDEA:
u -e/ -> ini kita kasih ~pick
u -e/conf,conf/
u -e/<quick statement>
"""

react_language = """
program: statement+
statement: 
	| statement_config? quick_statement?

statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
// statement config item start
statement_config_item: "*" -> run_fmus
	| "i" 			-> info // info atau help, mengentai kode yg dioprek
	| "ls" 			-> toc
	| "Atxt" 		-> fslang_z_quick_android_textinput				// u -e/Atxt/1
	| "Rch" 		-> fslang_z_quick_campur_react_tschakraui		// u -e/Rch/1
	| "Rgl" 		-> fslang_z_quick_campur_react_reactgridlayout	// u -e/Rgl/1
	| "R" 			-> fslang_z_quick_react		// u -e/R/1
	| "DJ" 			-> fslang_z_quick_django	// u -e/DJ/1
	| "N" 			-> fslang_z_quick_node		// u -e/N/1
	| "ST" 			-> fslang_z_quick_nest		// u -e/ST/1
	| "XT" 			-> fslang_z_quick_next		// u -e/XT/1
	| "A" 			-> fslang_z_quick_mobile	// u -e/A/1
	| "DO" 			-> fslang_z_quick_devops	// u -e/DO/1
	| "BE" 			-> fslang_z_quick_backend	// u -e/BE/1
	| "FE" 			-> fslang_z_quick_frontend	// u -e/FE/1
	| "K" 			-> fslang_z_quick_karya		// u -e/K/1
	| "algo" 		-> fslang_z_quick_algos		// u -e/algo/1
	| "tdd" 		-> fslang_z_quick_tdd		// u -e/tdd/1
	| "PR" 			-> fslang_z_quick_parser	// u -e/PR/1

	| "crajs" 		-> fslang_misc_crajs			// u -e/crajs/1
	| "crats" 		-> fslang_misc_crats			// u -e/crats/1
	| "aws" 		-> fslang_z_quick_campur_aws			// u -e/aws/1
	| "books" 		-> fslang_z_quick_campur_books			// u -e/books/1
	| "gomi" 		-> fslang_z_quick_campur_gomisc			// u -e/gomi/1
	| "hasura" 		-> fslang_z_quick_campur_hasura			// u -e/hasura/1
	| "html" 		-> fslang_z_quick_campur_htmltemplates	// u -e/html/1
	| "H" 			-> fslang_z_quick_campur_htmltemplates	// u -e/H/1
	| "jfx" 		-> fslang_z_quick_campur_javafx			// u -e/jfx/1
	| "netlify" 	-> fslang_z_quick_campur_netlify		// u -e/netlify/1
	| "prisma" 		-> fslang_z_quick_campur_prisma			// u -e/prisma/1
	| "rr" 			-> fslang_z_quick_campur_rubyrails		// u -e/rr/1
	| "tddjava"		-> fslang_z_quick_campur_tdd_tddjava	// u -e/tddjava/1
	| "tddjs" 		-> fslang_z_quick_campur_tdd_tddjs		// u -e/tddjs/1
	| "tddpy" 		-> fslang_z_quick_campur_tdd_tddpy		// u -e/tddpy/1
	| "twrds" 		-> fslang_z_quick_campur_onefilers_pytwitterredis		// u -e/twrds/1
	| "w3" 			-> fslang_z_quick_campur_web30			// u -e/w3/1
	| "webext" 		-> fslang_z_quick_campur_webext			// u -e/webext/1
	| "wp53" 		-> fslang_z_quick_campur_wp5_wd3		// u -e/wp53/1
	| "wp54" 		-> fslang_z_quick_campur_wp5_wd4		// u -e/wp54/1
	| "wp5ts" 		-> fslang_z_quick_campur_wp5_ts			// u -e/wp5ts/1

// statement config item end

quick_statement: program_backend
program_backend: HURUF_PROGRAM_BACKEND

program_frontend: declarative_element ("," declarative_element)*
declarative_element: element_name element_config? cdata_text? element_children?
element_name: HURUF_DIGIT
element_config_separator: ","
element_config: "/" element_config_item (element_config_separator element_config_item)* "/"
	| "$" element_config_item_berslash (element_config_separator element_config_item_berslash)* "$"
element_config_item: HURUF_DIGIT  -> item_key_value_boolean
	| item_key "=" item_value       -> item_key_value
element_config_item_berslash: HURUF_DIGIT  -> item_key_value_boolean
	| item_key "=" item_value       -> item_key_value
	| item_key "=" item_value_berslash       -> item_key_value_berslash
element_children: "(" program_frontend ")"
item_key: HURUF_DIGIT
// item value hrs bisa terima:
// ' " { } ( ) [ ] / @ : ;
// <Route path="/@:username/favorites" component={ProfileFavorites} />
item_value: HURUF_NILAI
	| "'" HURUF_NILAI_BERSPASI "'" -> diapit_sq
	| "\\"" HURUF_NILAI_BERSPASI "\\"" -> diapit_dq
item_value_berslash: HURUF_NILAI_BERSLASH
cdata_text: HURUF_CDATA

HURUF_CDATA: ("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|" "|";"|":"|"+"|"-")*
HURUF_NILAI: ("_"|LETTER|DIGIT|"\\""|"{") ("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" ")*
HURUF_NILAI_BERSLASH: ("_"|LETTER|DIGIT|"\\""|"{") ("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*
HURUF_NILAI_BERSPASI: ("_"|LETTER|DIGIT|"\\""|"{") ("_"|LETTER|DIGIT|"."|"`"|"{"|"}"|"("|")"|"="|" ")*
HURUF_NON_OPEN: ("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|"."|","|" "|"+"|"="|"-"|"_"|"@"|"#"|"$"|"%"|"^"|"&"|"*")*
HURUF_KODE_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{"|"<") ("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*

HURUF_PROGRAM_BACKEND: ("_"|LETTER|DIGIT|"\\""|"{"|"[") ("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/"|","|";"|":"|"@"|"["|"]"|"#"|"|"|"-")*
HURUF_PROGRAM_CSV: ("_"|LETTER|DIGIT|"\\""|"{"|"[") ("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|">"|"!"|"("|")"|" "|"/"|","|";"|":"|"@"|"["|"]"|"#"|"|")*
HURUF_PROGRAM_FRONTEND: ("_"|LETTER|DIGIT|"\\""|"{") ("_"|LETTER|DIGIT|"."|"\\""|"'"|"`"|"{"|"}"|"="|"<"|"!"|"("|")"|" "|"/")*
"""

huruf = """
HURUF_DIGIT: ("_"|LETTER|DIGIT) ("_"|LETTER|DIGIT|".")*
"""

bahasa = f"""
{react_language}

{huruf}

{base_grammar}
"""
