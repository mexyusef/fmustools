from .base import base_grammar
from .subclass_string import string_subclass_type
from .subclass_number import number_subclass_type
from .subclass_date import date_subclass_type

###################################################################

bahasa = f"""
keseluruhan: database
| table

database: dbconfig? table (table_separator table)*
table_separator: "|"
| NEWLINE

// [usef:rahasia@gisel.ddns.net:9022/tempdb]?@Article=#100?title,s|?Comment=#100?title,s
// [/tempdb]
dbconfig						: "[" dbtype? userpass? hostport? dbspec backendspec? frontendspec? "]"
dbtype							:  sql_nosql "://"
dbspec							: "/" dbname
userpass						: user ":" pass "@"
hostport						: host? ":" port
user							: HURUF
pass							: HURUF_PASSWORD
host							: HURUF_HOST
port							: BILBUL
dbname							: HURUF
// utk spec: host, port, dsb
backendspec					: "#" HURUF_DIGIT_COMMA
frontendspec				: "##" HURUF_DIGIT_COMMA

sql_nosql: 		"mg" -> mongodb
	|			"pg" -> postgresql
	|			"ms" -> mssql
	|			"my" -> mysql
	|			"sqlt" -> sqlite3

table: configuration? statement (insn_separator statement)*

configuration: "{{" config_spec ("," config_spec)* "}}"

// config_number_spec jumlah faker data utk digenerate utk table ybs
config_spec: config_name_spec "=" config_number_spec -> config_name_number
	| config_name_spec
	| "ts" -> config_timestamp_spec
	| "-id" -> config_remove_attribute_id
	| "->" has_one_syntax
	| "=>" belongs_to_syntax

has_one_syntax: assoc_table "/" foreign_column "/" domestic_column ("/" as_column)
belongs_to_syntax: assoc_table "/" foreign_column "/" domestic_column ("/" as_column)
assoc_table				: HURUF_SPACE
foreign_column			: HURUF_SPACE
domestic_column			: HURUF_SPACE
as_column				: HURUF_SPACE

//	| config_number_spec
//	| config_output_spec
//	| config_output_spec config_name_spec

config_output_spec: output_type
output_type: "sql" 				-> to_sql
	| "alchemy" 			    -> to_sqlalchemy
	| "sequelize" 			  	-> to_sequelize
	| "actix" 				    -> to_actix
	| "asp" 				    -> to_asp
	| "django" 				    -> to_django
	| "flask" 				    -> to_flask
	| "gorm" 				    -> to_gorm
	| "laravel" 			    -> to_laravel
	| "play" 				    -> to_play
	| "phoenix" 			    -> to_phoenix
	| "rails" 				    -> to_rails
	| "springboot" 			  	-> to_springboot
	
config_number_spec:	"#" number_of_data
number_of_data: BILBUL

config_name_spec: "@" schema_table
schema_table: (schemaname "/")? tablename

// contoh pake stringenum
// role,s(100),(admin,user,guest|guest)
statement: column_name "," column_type_spec ("," column_constraint_spec)?
	| primary_key_column
	| foreign_key_column
	| index_column
	| sistem (has_one | belongs_to | has_many | belongs_to_many) lingkungan // utk relation
	| master (one2one | one2many | many2one | many2many) slave

column_name: HURUF_DIGIT
tablename: HURUF_DIGIT
schemaname: HURUF_DIGIT

column_type_spec: column_type

// https://sequelize.org/v3/api/datatypes/
// tipe kolom start
column_type: "s" 	(":" string_subclass_type)? -> string
	| "t" 					-> text
	| "v" "(" BILBUL ")" (":" string_subclass_type)? -> varchar
	| "i" 					(":" number_subclass_type)? -> integer
	| "bi" 					-> bigint
	| "f" 					-> float
	| "D" 					-> double
	| "dec" 				-> decimal
	| "json" 				-> json
	| "jsonb"				-> jsonb
	| "u" 					-> url
	| "u0" 					-> uuid
	| "u1" 					-> uuidv1
	| "u4" 					-> uuidv4
	| "b" 					-> boolean
	| "dt" 					(":" date_subclass_type)? -> date			// models.DateField
	| "ts" 					-> timestamp													// models.DateTimeField
	| "n" 					-> number
	| "enum" 				-> enum
	| "ser" 				-> serial
	| "slug" 				-> slug
	| "img" 				-> image // mungkin juga blob? default ke string saja
	| "auto"				-> auto
	| "blob"				-> blob
	| "fk" "/" rel_to ("/" action_list)? ("/" related_name)? ("/" verbose_name)? 	-> django_foreign_key
	| "11" "/" rel_to ("/" action_list)? ("/" related_name)? ("/" verbose_name)?	-> django_one_to_one
	| "1m" "/" rel_to ("/" action_list)? ("/" related_name)? ("/" verbose_name)?	-> django_one_to_many
	| "mm" "/" rel_to	("/" related_name)?	-> django_many_to_many
	| "[" column_type "]" 	-> array_of
	| "[" "]"				-> empty_array
// tipe kolom end

{string_subclass_type}
{number_subclass_type}
{date_subclass_type}


min_max: "(" min ("," max)? ")"
min: BILBUL_BERTANDA
max: BILBUL_BERTANDA
numdigits: "(" BILBUL ")"
right_left: "(" digitright ("," digitleft)? ")"
digitright: BILBUL
digitleft: BILBUL

// kita ubah nama di constraint
// node_foreign_key 		-> node_foreign_key_constraint
// django_foreign_key		-> django_foreign_key_constraint
// krn django_foreign_key sudah dipake di (main)type
column_constraint_spec: column_constraint ("," column_constraint)*

// constraint start
column_constraint: "N" 							-> not_null				// null=False
	| "n"										-> yes_null
	| "r"										-> yes_required			// r = N
	| "R"										-> not_required			// R = n
	| "r" ":" HURUF 							-> required_with_validation
	| "u" 										-> unique
	| "U" 										-> no_unique			// unique=False
	| "b" 										-> yes_blank
	| "B" 										-> no_blank				// blank=False
	| "e" 										-> editable
	| "E" 										-> no_editable			// editable=False
	| "tr" 										-> yes_trim				// utk mongoose/sequelize trim=true
	| "uc" 										-> yes_uppercase
	| "lc" 										-> yes_lowercase
	| "ai"										-> auto_increment
	| "an"										-> auto_now
	| "ana"										-> auto_now_add	
	| "dbi"										-> db_index				// khusus django utk slug, char dll
	| "pk" pk_column_list?			-> primary_key
	| "len=" BILBUL					-> max_length
	| "min=" BILBUL					-> min_length
	| "digits=" BILBUL				-> max_digits
	| "places=" BILBUL				-> decimal_places
	| "BY"							-> find_by
	| "F" ":" schema_table_column_name constraint_name? action_list_node?	-> node_foreign_key_constraint
	| "fk" ":" schema_table_name action_list?								-> django_foreign_key_constraint

	| "df" "=" nilai_default 											// df=1 atau df=now
	| "ref" ":" HURUF 				-> references
	| "refk" ":" HURUF 				-> references_key
	| "(" enumname? stringenumvalues stringenumdefault? ")"	// (satu,dua,tiga>satu)
	| "[" enumname? enumvalues enumdefault "]"
// constraint end

related_name:			"rn=" HURUF
verbose_name:			"vn=" HURUF

rel_to: HURUF_SPACE		-> rel_to_object
	| "/" HURUF_SPACE (rel_to_fk)? (rel_to_backref)? (rel_to_lazy)?	-> rel_to_string

rel_to_fk: "|!" HURUF_DIGIT_MINUSPLUS

rel_to_backref: "|@" HURUF_DIGIT_MINUSPLUS -> backref_column
	| "|#" HURUF_DIGIT_MINUSPLUS -> backref_function // backref=db.backref('cart_item', uselist=False)

rel_to_lazy: "|$" "dyn" -> lazy_dynamic
	| "|$" "sel" -> lazy_true // lazy_select
	| "|$" "sq" -> lazy_subquery
	| "|$" "j" -> lazy_joined

nilai_default: HURUF_DIGIT_SPASI
	| "empty"	-> default_empty
	| "now" 	-> default_now					// defaultValue: sequelize.fn('NOW')
	| "null"	-> default_null					// DEFAULT NULL di mysql

pk_column_list: ":" column_list
stringenumvalues: enumvalue ("," enumvalue)*
enumvalues: enumvalue ("," enumvalue)*
enumvalue: HURUF_DIGIT_MINUSPLUS
enumdefault: ">" HURUF_DIGIT_MINUSPLUS
stringenumdefault: ">" HURUF_DIGIT_MINUSPLUS
enumname: HURUF_DIGIT_MINUSPLUS ">"

column_list: column_name ("," column_name)*

// https://mysql.tutorials24x7.com/blog/guide-to-design-a-database-for-blog-management-in-mysql

primary_key_column: "pk" ":" column_list
foreign_key_column: "fk" ":" column_name "->" schema_table_column_name constraint_name? action_list? // fk (internal_col) references schema.table(external_col)
// CONSTRAINT `fk_post_user` FOREIGN KEY (`authorId`) REFERENCES `blog`.`user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION);

index_column: "I" unique? ":" column_name direction_spec?	// INDEX `idx_post_user` (`authorId` ASC),
unique: "*"													// UNIQUE INDEX `generated_unique_index_name` (`mobile` ASC, email ASC)
direction_spec: ":" direction
direction: "a" 	-> index_ascending
	| "d"		-> index_descending

schema_table_name: tablename
	| schemaname "/" tablename

schema_table_column_name: column_name
	| tablename "/" column_name						// gunakan / alih2 . krn column_name bisa punya .
	| schemaname "/" tablename "/" column_name
// ((schemaname ".")? tablename ".")? column_name

constraint_name: HURUF // constraint `nama constraint` fk .. references ....

action_list_node: action_name2 ("," action_name2)*
action_name2: "c=" create_action 
	| "r=" read_action 
	| "u=" update_action 
	| "d=" delete_action 

action_list: action_name ("," action_name)*
action_name: "c" 		-> create_action
	| "r" 						-> read_action
	| "u" 						-> update_action
	| "d" deltype?		-> delete_action

// default cascade
deltype: "=cascade"	-> delete_cascade
	| "=setnull"			-> delete_setnull 									// on_delete=models.SET_NULL
	| "=cascade*"			-> delete_cascade_all_delete 				// cascade='all, delete'
	| "=cascade**"		-> delete_cascade_all_delete_orphan // cascade='all, delete-orphan'

create_action: HURUF 	// address = models.ForeignKey('app_label.Address', on_delete=models.CASCADE)
read_action: HURUF 		// author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
update_action: HURUF 
delete_action: HURUF 	// ON DELETE (no_action/cascade/...) 

sistem: tablename "[" column_name "]"
lingkungan: tablename "[" column_name "]"
has_one: "->"
belongs_to: "<-"
has_many: "=>"
belongs_to_many: "<="

master: tablename "[" col_nametypeconstraint_spec (";" col_nametypeconstraint_spec)* "]"
slave: tablename "[" col_nametypeconstraint_spec (";" col_nametypeconstraint_spec)* "]"
col_nametypeconstraint_spec: column_name "," column_type_spec ("," column_constraint_spec)?
one2one: "11"
one2many: "1m"
many2one: "m1" "(" master_column "," slave_column ")" // 
many2many: "mm"
master_column: HURUF_DIGIT
slave_column: HURUF_DIGIT

insn_separator: NEWLINE
	| ";"

// gak boleh kosong utk separator...
//	|

HURUF_DIGIT: 						("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@")*
HURUF_DIGIT_SPASI: 			("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"@"|" ")*
HURUF_DIGIT_MINUSPLUS: 	("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"-"|"+"|"@")*
HURUF_DIGIT_COMMA:			("_"|LETTER|DIGIT) 				("_"|LETTER|DIGIT|"."|"-"|"+"|"@"|",")*
HURUF_SPACE: 						("_"|LETTER) 							("_"|LETTER|DIGIT|" "|".")*
HURUF_COMMA: 						("_"|LETTER) 							("_"|LETTER|DIGIT|",")*
HURUF_SPACE_MINUS: 			("_"|LETTER) 							("_"|LETTER|DIGIT|" "|"-"|".")*


HURUF_PASSWORD: 	("_"|LETTER) 				("_"|LETTER|DIGIT|" "|"&"|"%%"|"."|","|"-"|"_"|"+"|"#"|"*")*
HURUF_HOST: 			("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
{base_grammar}
"""
