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

# belum jelas utk escape double quote
# "\\""
# "\""

# pelajaran berharga
# di bahasa
#		\\ dan \\"
# di filedir_bahasa
#		\\\\ dan \\"
# krn di filedir_bahasa kita escape nya 2x

bahasa = r"""
?keseluruhan: _NL* abaikan

abaikan: HURUF_FOLDER_SYSTEM _NL [_INDENT abaikan+ _DEDENT]

// $ utk system command
// % utk user input
// # utk comment
// baru tau tab gak bisa
HURUF_FOLDER_SYSTEM: ("_"|LETTER|DIGIT|"/"|"."|"@"|"$"|"%"|"&"|"*"|"#"|"["|"]"|"~"|"?"|" "|"\\") (LETTER|DIGIT|"_"|"["|"]"|"*"|"."|":"|";"|"/"|","|"("|")"|"{"|"}"|"+"|"-"|"_"|"="|" "|"%"|"$"|"@"|"&"|"\\"|"\""|"!"|"<"|">"|"?"|"|"|"'"|"#"|"^"|"~"|/\t/|"`")*

%import common.CNAME 		-> NAME
%import common.WS_INLINE

%declare _INDENT _DEDENT

%ignore WS_INLINE

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

TAB: /\t/
_NL: /(\r?\n[\t ]*)+/
"""

# pengen tambah: special_command
# bisa exec python, bisa typing dg select window
# pesan_instruksi terpaksa kita modify @@
# krn @() selalu dimakan olehnya

# todo: fitur baru yg berguna...
# repeat
# 	contoh fungsinya?
filedir_bahasa = """
keseluruhan: insn+

// instruction start
insn: filename "," filetype fileoperation?
	| "$" system_operation_type
	| "/" quick_command
	| "/" -> empty_quick_command
	| "*" special_command
	| "@" "(" pesan_instruksi_dari_template ")"
	| "@" pesan_instruksi
	| "~" branch_instruksi
	| "?" pickone_instruksi
	| "%" save_variables
	| request_operation_from_user
	| "#" comment
	| "#" "(" komentar_dari_template ")"
	| "x=" pexpect_operation
// instruction end

// x=s(spawn_perintah)[e:"something", s:"something", sl:"something"]
pexpect_operation: pexpect_spawn pexpect_play?
pexpect_spawn: "s" "(" HURUF_FOLDER_LAMA_BERBINTANG ")"
pexpect_play: "[" pexpect_item ("," pexpect_item)* "]"
pexpect_item: "e:" "\\"" HURUF_FOLDER_LAMA_BERBINTANG "\\"" -> px_expect
	| "s:" "\\"" HURUF_FOLDER_LAMA_BERBINTANG "\\"" -> px_send
	| "sl:" "\\"" HURUF_FOLDER_LAMA_BERBINTANG "\\"" -> px_sendline

komentar_dari_template: komentar_kunci "=" komentar_baris
// pesan_instruksi_dari_template -> pesan_instruksi_selanjutnya
// kita pengen bisa diakhiri * agar tidak minta confirm
pesan_instruksi_dari_template: komentar_kunci "=" komentar_baris
komentar_baris: HURUF_FOLDER_LAMA
komentar_kunci: HURUF_FOLDER_LAMA_BERBINTANG

special_command: MENGANDUNG_AMPERSAND_DAN_TANDASERU
quick_command: MENGANDUNG_AMPERSAND_DAN_TANDASERU_QUICK_COMMAND

fileoperation: "(" file_dir_operation_type ("," file_dir_operation_type)* ")"

// coba.txt,f(@a,n=ini isi baris pertama) = ok
// coba.txt,f(n=ini isi baris pertama,@a) = error krn comma kemakan n=..
// ini mungkin krn file_operation_type memakan koma shg ,@a tidak diproses benar

file_dir_operation_type: file_operation_type	//
	| "/" dir_operation_type 					// agar fileop dan dirop bs share cmd, maka dirop prefix dg /
	| "@" operation_attributes

// file specifier start
// tanpa operasi ini maka filenya gak akan dibuat
// kecuali kita kenalkan mk utk touch file...
//(f=filename)
//(F=filename)
//(c=) akan minta user ngisi clipboard utk ditulis ke file
//(i=) akan minta input dari user sampai 1 baris berisi dot
// filename.txt,f(f=filename_sudahada.txt)
// filename.txt,f(F=/home/usef/filename_sudahada.txt)
// (f=...) kita ubah skrg bisa relative path dulu, jk gak isfile dari templates
file_operation_type: "f" "=" HURUF_FOLDER 		-> load_from_file // dari templates -> mending dari item.workdir
	//| "F" "=" HURUF_FOLDER 					-> load_from_file_absolute // dari abs dir
	| "F" "=" HURUF_FOLDER_LAMA					-> load_from_file_absolute
	| "D" "=" HURUF_FOLDER_LAMA_BERBINTANG		-> load_from_dir_with_filter
	| "i" "="									-> input_from_user_with_prompt
	| "c" "=" 									-> paste_from_clipboard_with_pause
    | "C" "=" 									-> paste_from_clipboard_without_pause
	| "t"	"="									-> touch_file
	| "n"	"="	ISI_CONTENT_FILE_BISA_URL		-> content_file

	// g "cerita.md,f(q=funny story about life of nongnong in 3 paragraphs)"
	| "q"	"="	ISI_CONTENT_FILE_BISA_URL					-> query_active_llm
	// g "cerita2.md,f(q:groq=create funny story about bubba)"
	| "q" ":" HURUF "="	ISI_CONTENT_FILE_BISA_URL			-> query_specific_llm

	// g "factorial.scala,f(qc=factorial scala)"
	| "qc"	"="	ISI_CONTENT_FILE_BISA_URL					-> query_active_llm_for_code
	//g "factorial.clj,f(qc:groq=factorial clojure)"
	| "qc" ":" HURUF "="	ISI_CONTENT_FILE_BISA_URL		-> query_specific_llm_for_code

	// g "tugas1-nextjs.md,f(Q=coba.fmus=tugas-1)"
	| "Q" "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 				-> query_active_llm_from_fmus
	// g "tugas2-react.md,f(Q:groq=coba.fmus=tugas-2)"
	| "Q" ":" HURUF "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 		-> query_specific_llm_from_fmus

	| "e" "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 				-> ambil_entry_dari_file_template
	| "cg" langchoice? "=" singkat_folder "=" HURUF_FOLDER_NEXTJS 	-> ambil_entry_codegen
	| "code" langchoice "=" ISI_FILE_TERMASUK_KOMA_TAMBAH_PERSEN 	-> ambil_replify_here
	| "b64" "=" singkat_folder "=" HURUF_FOLDER_LAMA 		-> ambil_terdekod_dari_file_template
	| "img" "=" HURUF_FOLDER_LAMA 							-> generate_image
	| "h" "=" ALAMAT 										-> url_file

	//| "e" "=" singkat "=" HURUF_FOLDER_LAMA 				-> ambil_entry_dari_file_template // e=template1=import from java
// file specifier end

langchoice: "[" HURUF_FOLDER "]"

// dir specifier start
// contoh load_program_from
// sensor,d(/mk,/load=__CURDIR/sensor/sensor.mk=program/sensor/fm.us)
// hasilnya: fmus.py line 518 dan 686
// operations.append(f"load_program_from={file_value}={line_value}")
dir_operation_type: "mk"					-> create_dir 					// mkdir -p
	| "cp" "=" HURUF_FOLDER					-> copy_dir_from				// cp somfolder . dari template
	| "content" "=" HURUF_FOLDER			-> copy_dircontent_from 		// cp somefolder/* .
	| "cpa" "=" HURUF_FOLDER				-> copy_absolute_dir_from		// cp somfolder . dari anywhere
    
    //17-7-23, pengen bisa windows path utk /load=, gagal
    //| "load" "=" HURUF_FOLDER	"=" HURUF_FOLDER_LAMA_BERBINTANG 				-> load_program_from
	| "load" "=" HURUF_FOLDER_BERBACKSLASH	"=" HURUF_FOLDER_LAMA_BERBINTANG 	-> load_program_from
    
	| "rm" 									-> remove_dir
	| "?" 									-> check_exists
	| "ls"									-> list_content
    // 27/11/23, kita buat HURUF_ANGKA_SPASI karena jangan sampai mengandung right-parenthesis
    | "find=" HURUF_FIND_CMD				-> find_within_directory	// mydir,d(/find=unique-files)
    | "grep=" HURUF_ANGKA_SPASI				-> grep_within_directory 	// mydir,d(/grep=interesting word)
    | "rm=" HURUF_ANGKA_SPASI				-> remove_within_directory 	// mydir,d(/rm=node_modules, .git, __pycache)
// dir specifier end

system_operation_type: MENGANDUNG_AMPERSAND_DAN_TANDASERU // yarn init, create-react-app
request_operation_from_user: "%%%"

// kita bikin @b, @x jangan @b,x krn masuk dlm operasi file/dir (oper,oper,oper)
// jadi rancu soalnya
operation_attributes: operation_attr // ("," operation_attr)*

// file operation start
operation_attr: "b"									-> binary_file_operation 		// @b
	| "x" "[" pattern ("," pattern)* "]"			-> excluding_in_copy
	| "a" 	-> appending_mode // (e=template=main.scala/baris1,@a) biar bisa */baris2 dst
	| "ts" 	-> tab_to_space
	| "ib" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" 		-> insert_before
	| "ia" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" 		-> insert_after
	| "iA" "=" singkat "=" BILBUL_BERTANDA 													-> insert_at // f=capcay.txt,iA=barisentry=-1
	| "ra" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" 		-> replace_at
	| "rf" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" 		-> replace_from
	| "rm" "=" jumlah_hapus "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" 	-> remove_lines
	| "re" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" 		-> replace_entry
	| "rb" "=" singkat "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_between
	| "rs" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> replace_string
	| "rc" "=" singkat 																		-> replace_content // whole file replace
	// yg pertama: komentar symbol spt # atau //, yg kedua baris yg mau dicomment
	| "cf" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" "=" "\\"" MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE "\\"" -> commenting_file

	// 27/11/23, konsep: line or string spec|operation|data
    | "line=" line_expression "|" line_operation "|" line_data 				-> fileops_line_expression
    | "line>" line_contains "|" line_operation "|" line_data 				-> fileops_line_contains
    // line_matches
    | "line~" line_regex "|" line_operation "|" line_data 					-> fileops_line_matches
    // line_between_contains
    | "btw>" line_contains line_contains "|" line_operation "|" line_data 	-> fileops_line_between_contains
    // line_between_matches
    | "btw~" line_regex line_regex "|" line_operation "|" line_data 		-> fileops_line_between_matches
    
    // utk string, kita mulai dg use case
    // ALLOWED_HOSTS = []
    // kita pengen oprek " = []" utk diganti dg yg baru
    // jd pengen replace 'after string' bukan string 'ALLOWED_HOSTS' nya sendiri
    | "str=" string_matches "|" string_operation "|" string_data -> fileops_string_at
    | "str+" string_matches "|" string_operation "|" string_data -> fileops_string_after
    | "str-" string_matches "|" string_operation "|" string_data -> fileops_string_before
// file operation end


line_expression: line_item ("," line_item)*
line_item: line_number
	| line_range
    | line_end
line_number: BILBUL
line_range: BILBUL "-" BILBUL
line_end: "~"

line_contains: "(" HURUF_LINE_CONTAINS ")"
line_regex: "(" HURUF_ANGKA_SPASI ")"
string_matches: "(" HURUF_ANGKA_SPASI ")"

string_operation: "r" -> string_replace
	| "d" -> string_delete

string_data: "(" HURUF_ANGKA_SPASI ")" -> string_data_literal

line_operation: "i+" -> line_insert_after
	| "i-" -> line_insert_before
    | "r" -> line_replace_at
    | "ri" -> line_replace_at_inclusive

line_data: "(" HURUF_ANGKA_SPASI ")" -> line_data_literal
	| "f:" HURUF_ANGKA -> line_data_filepath
    | HURUF_FOLDER_BERBACKSLASH "=" HURUF_FOLDER_LAMA_BERBINTANG -> line_data_fmus
    | "i:" -> line_data_input
    | "u:" HURUF_ANGKA -> line_data_url

jumlah_hapus: BILBUL
// di sini kita dukung operasi insert_before dll
// tapi file_operation butuh 1 more args: line indicator utk operasi, selain line baris/cari
// atau kita tambahkan saja di sini/operation_attr
// fmus baris 460
// digunakan di method write_file_with_variable_expansion

exclude_patterns: pattern ("," pattern)*
pattern: HURUF_SYSTEM

// branching start
// unless, while-not??? until -> until === do-unless === do-while-not
branch_instruksi: if_branch
| else_branch
| while_loop
| unless_loop
if_branch: 				"if" if_condition?
else_branch: 			"else" else_condition?
while_loop:				"while" while_condition?
unless_loop:			"unless" while_condition?

if_condition:			"[" binary_condition (binary_condition)* "]"
else_condition:			"[" binary_condition "]"
while_condition:		"[" value_condition ("," value_condition)* "]"

binary_condition: "1" -> binary_yes
| "0" -> binary_no
| "i" -> binary_input
| "?" HURUF_FOLDER_LAMA -> exist_filedir
| "?!" HURUF_FOLDER_LAMA -> dont_exist_filedir

value_condition: HURUF_ANGKA_SAMADENGAN

// ?choose[1,5,7]
// tiap anak kita kasih choose_key
pickone_instruksi: "pick" choose_condition?
choose_condition: "[" choose_number ("," choose_number)* "]"
choose_number: BILBUL -> pilihan_angka
| "i" -> pilihan_input
// branching end


filename: HURUF_FOLDER_PLUS_BRACKETS
filetype: file
	| dir
file: "f"
dir: "d"

pesan_instruksi: MENGANDUNG_AMPERSAND_DAN_TANDASERU
save_variables: singkat "=" panjang text_operations?
singkat_unused: HURUF_ANGKA
singkat: SINGKAT_IS_BARIS_ENTRY
singkat_folder: HURUF_FOLDER_LAMA
panjang: HURUF_SYSTEM_TERMASUK_KOMA_PIPA_KURAWAL
//comment: HURUF_SYSTEM_TERMASUK_KOMA 
comment: HURUF_SYSTEM_TERMASUK_KOMA_BERTAB
text_operations: "[" text_operation ("," text_operation)* "]"
text_operation: "@cap"  -> text_capitalize
| "@title" -> text_title
| "@lower" -> text_lower
| "@upper" -> text_upper
| "@plural" -> text_plural
| "@model" -> modelify // Product -> Product, Products, product, products, PRODUCT, PRODUCTS
| "@dot_to_under" -> dot_to_under
| "@under_to_dot" -> under_to_dot // a_b_c jadi a.b.c
| "@dot_to_path" -> dot_to_path
| "@path_to_dot" -> path_to_dot
| "@dot_to_slash" -> dot_to_slash
| "@slash_to_dot" -> slash_to_dot
| "@hyphen_to_underscore" -> hyphen_to_underscore

// _/.__something__/.__serta__ :-
// update: tambah + dan () utk nama file
HURUF_FOLDER_PLUS_BRACKETS:				("_"|LETTER|DIGIT|"/"|"."|"["|"]"|"\\\\") ("_"|LETTER|DIGIT|"."|":"|"/"|"-"|" "|"["|"]"|"+"|"("|")"|"$"|"\\\\"|"@"|"~"|"'"|"%")*
// update: tambah @
// update 17-7 tambah backslash, gagal
// HURUF_FOLDER: 							("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|":"|"/"|"-"|"+"|" "|"@"|"\\\\")*
HURUF_FOLDER: 							("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|":"|"/"|"-"|"+"|" "|"@")*
HURUF_FOLDER_BERBACKSLASH:					("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|":"|"/"|"-"|"+"|" "|"@"|"\\\\")*

// update: tambah @ dan + dan () -> err gak bisa terima ()
HURUF_FOLDER_LAMA:						("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|" "|"@"|"+"|":"|"\\\\"|"~")*

HURUF_FOLDER_NEXTJS:					("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|" "|"@"|"+"|"["|"]"|":"|"\\\\"|"'")*

//HURUF_FOLDER_LAMA_BERBINTANG: 		("_"|LETTER|DIGIT|"/"|"."|"*") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|" "|"*")*
// tambah backslash utk direktori
HURUF_FOLDER_LAMA_BERBINTANG: 			("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|" "|"*"|"+"|":"|"\\\\")*
ISI_FILE_TERMASUK_KOMA:					("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|"\\\\"|" "|";"|"&"|":"|"=")*
ISI_FILE_TERMASUK_KOMA_TAMBAH_PERSEN:	("_"|LETTER|DIGIT|"/"|"."|"\\"") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|"\\\\"|" "|";"|"&"|":"|"="|"%"|"*"|"$"|"\\""|"{"|"}")*
// tambah - di awal utk bisa n=--%, dan # utk --#
ISI_CONTENT_FILE_BISA_URL:	("_"|LETTER|DIGIT|"/"|"."|"\\""|"-") ("_"|LETTER|DIGIT|"."|"-"|"/"|","|"\\\\"|" "|";"|"&"|":"|"="|"%"|"*"|"$"|"\\""|"{"|"}"|"#"|"!")*
ALAMAT:									("_"|LETTER|DIGIT|"/") ("_"|LETTER|DIGIT|":"|"-"|"%"|"."|"/"|","|" "|"?")*
// tambah & di huruf system utk bisa command background
// tambah = dan () di huruf system utk bisa $(PWD) dst
HURUF_SYSTEM: 							("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\"") (LETTER|DIGIT|"$"|"@"|"&"|"="|"("|")"|"_"|"*"|"."|"/"|"-"|"+"|" "|":"|"\\\\"|"\\"")*
MENGANDUNG_AMPERSAND: 					("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\"") (LETTER|DIGIT|"$"|"_"|"*"|"."|","|"/"|"-"|"+"|"&"|"("|")"|"["|"]"|"{"|"}"|" "|":"|"\\\\"|"\\"")*

// tambah () di awal, krn $(cd ..) diawali dg parentheses
// tambah @ krn suka $yarn add @types/..
MENGANDUNG_AMPERSAND_DAN_TANDASERU: 	("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"("|")"|"*"|"%"|"="|"-"|"[") (LETTER|DIGIT|"$"|"_"|"*"|"."|","|"/"|"-"|"+"|"="|"&"|"@"|"%"|"("|")"|"["|"]"|"{"|"}"|" "|":"|";"|"\\\\"|"\\""|"!"|"<"|">"|"?"|"|"|"'"|"#"|"~"|"^"|"`")*
MENGANDUNG_AMPERSAND_DAN_TANDASERU_QUICK_COMMAND: ("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"("|")"|"*"|"%"|"="|"-") (LETTER|DIGIT|"$"|"_"|"*"|"."|","|"/"|"-"|"+"|"="|"&"|"@"|"%"|"("|")"|"["|"]"|"{"|"}"|" "|":"|";"|"\\\\"|"\\""|"\\|"|"!"|"<"|">"|"?"|"|"|"'"|"#"|"~"|"^"|"`")*
MENGANDUNG_AMPERSAND_DAN_TANDASERU_MINUS_QUOTE: ("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"("|")"|"*"|"#"|"@"|"'"|"-") (LETTER|DIGIT|"$"|"_"|"*"|"."|","|"/"|"-"|"+"|"="|"&"|"@"|"%"|"("|")"|"["|"]"|"{"|"}"|" "|":"|";"|"\\\\"|"!"|"<"|">"|"?"|"|"|"'"|"#"|"^"|"`"|"'")*
// bisa #&...maka & masukkan ke awalan
// tambah > krn kita pake 2>&1 dst
HURUF_SYSTEM_TERMASUK_KOMA:				("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"@"|"&"|" ") (LETTER|DIGIT|"$"|"@"|"&"|"="|"("|")"|"_"|"*"|"."|","|"/"|"-"|"+"|"'"|" "|";"|":"|"\\\\"|"\\""|">"|" ")*

// apa saja yg gak ada: ~!%^
//HURUF_SYSTEM_TERMASUK_KOMA_PIPA_KURAWAL: ("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"@"|"&"|" "|"[") (LETTER|DIGIT|"$"|"@"|"&"|"="|"("|")"|"_"|"*"|"."|","|"/"|"-"|"+"|"'"|" "|";"|":"|"\\\\"|"\\""|">"|" "|"|"|"{"|"}"|"]"|"#")*
HURUF_SYSTEM_TERMASUK_KOMA_PIPA_KURAWAL: ("_"|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"@"|"&"|" "|"[") (LETTER|DIGIT|"$"|"@"|"&"|"="|"("|")"|"_"|"*"|"."|","|"/"|"-"|"+"|"'"|" "|";"|":"|"\\\\"|"\\""|">"|"|"|"{"|"}"|"]"|"#")*
HURUF_SYSTEM_TERMASUK_KOMA_BERTAB:		("_"|/\t/|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"@"|"&"|" "|"%") (/\t/|LETTER|DIGIT|"$"|"@"|"&"|"="|"("|")"|"_"|"*"|"."|","|"/"|"-"|"+"|"'"|" "|";"|":"|"\\\\"|"\\""|">"|" "|"|"|"?")*

//HURUF_SYSTEM_TERMASUK_KOMA_BERTAB:		("_"|/\t/|LETTER|DIGIT|"*"|"/"|"."|"$"|"\\""|"@"|"&"|" "|"%") (/\t/|LETTER|DIGIT|"$"|"@"|"&"|"="|"("|")"|"_"|"*"|"."|","|"/"|"-"|"+"|"'"|" "|";"|":"|"\\\\"|"\\""|">"|" "|"|"|"?")*

// ini salah krn \\" bukan \\\"
// HURUF_SYSTEM: 						("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"/"|"-"|"+"|" "|":"|"\\\\"|"\\\"")*
// ini salah krn \: bukan :
// HURUF_SYSTEM: 						("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"/"|"-"|"+"|" "|"\:"|"\\"|"\\"")*
// HURUF_SYSTEM: 						("_"|LETTER|DIGIT|"/"|".") ("_"|LETTER|DIGIT|"."|"/"|"-"|"+"|" "|"\:"|"\\"|"\"")*

HURUF_LINE_CONTAINS: (HURUF|DIGIT|"_"|"\\"") ("_"|HURUF|DIGIT|"-"|" "|"."|","|"\\"")*
HURUF_FIND_CMD: (HURUF|DIGIT|"_"|"*"|".") ("_"|HURUF|DIGIT|"-"|" "|"*"|".")*
HURUF_ANGKA_SPASI:						(HURUF|DIGIT|"_") ("_"|HURUF|DIGIT|"-"|" ")*
HURUF_ANGKA: 							(HURUF|DIGIT|"_") ("_"|HURUF|DIGIT|"-")*
HURUF_ANGKA_SAMADENGAN:					(HURUF|DIGIT|"_") ("_"|HURUF|DIGIT|"-"|"="|"."|"*"|" "|"/")*
SINGKAT_IS_BARIS_ENTRY: 				(HURUF|DIGIT|"_") ("_"|HURUF|DIGIT|"-"|"."|"/")*

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
