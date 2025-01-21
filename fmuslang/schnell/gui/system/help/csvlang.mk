--% program dan examples
atau masuk repl via quick_command: /C. dan inline code dg: /c. 
(ini 3-char prefix)

atau dari special_command: **@
(ini 3-char prefix)

dari kbrepl:
../C.
../c.
..**@

app/transpiler/mycsv/main.py
app/transpiler/mycsv/main/csv_operation.py:

```
program: csv_operations
csv_operations: csv_operation (statement_separator csv_operation)*
statement_separator: "|"
csv_operation: csv_config? csv_code

csv_item: "mg"  -> mongoose
  | "sqlz"      -> sequelize
  | "pg"        -> sql_postgres
  | "ms"        -> sql_mssql
  | "my"        -> sql_mysql
  | "sqlt"      -> sql_sqlite
  | "torm"      -> nest_typeorm
  | "mg2"       -> nest_mongoose
  | "pris"      -> prisma
  | "hbr"       -> hibernate
  | "bts"       -> mybatis
  | "go"        -> struct_go
  | "rs"        -> struct_rs
  | "kt"        -> struct_kt
  | "ts"        -> struct_ts
  | "java"      -> struct_java
  | "dj"        -> django_orm
  | "fl"        -> be_flask
  | "fa"        -> be_fastapi
  | "nsm"       -> help_nest_mongo
  | "nsp"       -> help_nest_postgres
  | "json1"     -> json1
  | "json2"     -> json2
  | "csv"       -> csv
```

,.
from app.transpiler.mycsv.main import myrepl()

,.code
from app.transpiler.mycsv.main import process_language(code)

,.csv/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N

mg/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N

```
// mongoose
import mongoose from 'mongoose';
// const mongoose = require('mongoose');

const postreportSchema = new mongoose.Schema({
  category: { type: String, required: true }
}, { timestamps: true });

export default mongoose.model("PostReport", postreportSchema);
// module.exports = mongoose.model("PostReport", postreportSchema);
```

pris/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N

```
// prisma
generator client {
	provider = "prisma-client-js"
}

datasource db {
	provider = "postgresql"
	// provider = "mysql"
	// url      = env("DATABASE_URL")
	// DATABASE_URL="postgresql://usef:rahasia@localhost:5432/tempdb?schema=public"
	url      = "postgresql://usef:rahasia@localhost:5432/tempdb?schema=public"
}


// npx prisma migrate dev --name init

model PostReport {
	category        String
}
```

--#

--% langs.ucsv.grammar, langs.ucsv.processor

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
	|						"pg" -> postgresql
	|						"ms" -> mssql
	|						"my" -> mysql
	|						"sqlt" -> sqlite3

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
foreign_column		: HURUF_SPACE
domestic_column		: HURUF_SPACE
as_column					: HURUF_SPACE

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
	| "[" column_type "]" -> array_of
	| "[" "]" 						-> empty_array
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
column_constraint: "N" 			-> not_null					// null=False
	| "n"											-> yes_null
	| "r"											-> yes_required			// r = N
	| "R"											-> not_required			// R = n
	| "r" ":" HURUF 					-> required_with_validation
	| "u" 										-> unique
	| "U" 										-> no_unique				// unique=False
	| "b" 										-> yes_blank
	| "B" 										-> no_blank					// blank=False
	| "e" 										-> editable
	| "E" 										-> no_editable			// editable=False
	| "tr" 										-> yes_trim 				// utk mongoose/sequelize trim=true
	| "uc" 										-> yes_uppercase
	| "lc" 										-> yes_lowercase
	| "ai"										-> auto_increment
	| "an"										-> auto_now
	| "ana"										-> auto_now_add	
	| "dbi"										-> db_index					// khusus django utk slug, char dll
	| "pk" pk_column_list?		-> primary_key
	| "len=" BILBUL						-> max_length
	| "min=" BILBUL						-> min_length
	| "digits=" BILBUL				-> max_digits
	| "places=" BILBUL				-> decimal_places
	| "BY" 										-> find_by
	| "F" ":" schema_table_column_name constraint_name? action_list_node?	-> node_foreign_key_constraint
	| "fk" ":" schema_table_name action_list? 														-> django_foreign_key_constraint

	| "df" "=" nilai_default 											// df=1 atau df=now
	| "ref" ":" HURUF 				-> references
	| "refk" ":" HURUF 				-> references_key
	| "(" enumname? stringenumvalues stringenumdefault? ")"	// (satu,dua,tiga>satu)
	| "[" enumname? enumvalues enumdefault "]"
// constraint end

related_name: 	"rn=" HURUF
verbose_name:		"vn=" HURUF
rel_to: HURUF_SPACE				-> rel_to_object
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

--#

--% langs.ucsv.grammar, column type

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
	| "[" column_type "]" -> array_of
	| "[" "]" 						-> empty_array
// tipe kolom end

--#

--% langs.ucsv.grammar, column constraint
column_constraint: "N" 			-> not_null					// null=False
	| "n"											-> yes_null
	| "r"											-> yes_required			// r = N
	| "R"											-> not_required			// R = n
	| "r" ":" HURUF 					-> required_with_validation
	| "u" 										-> unique
	| "U" 										-> no_unique				// unique=False
	| "b" 										-> yes_blank
	| "B" 										-> no_blank					// blank=False
	| "e" 										-> editable
	| "E" 										-> no_editable			// editable=False
	| "tr" 										-> yes_trim 				// utk mongoose/sequelize trim=true
	| "uc" 										-> yes_uppercase
	| "lc" 										-> yes_lowercase
	| "ai"										-> auto_increment
	| "an"										-> auto_now
	| "ana"										-> auto_now_add	
	| "dbi"										-> db_index					// khusus django utk slug, char dll
	| "pk" pk_column_list?		-> primary_key
	| "len=" BILBUL						-> max_length
	| "min=" BILBUL						-> min_length
	| "digits=" BILBUL				-> max_digits
	| "places=" BILBUL				-> decimal_places
	| "BY" 										-> find_by
	| "F" ":" schema_table_column_name constraint_name? action_list_node?	-> node_foreign_key_constraint
	| "fk" ":" schema_table_name action_list? 														-> django_foreign_key_constraint

	| "df" "=" nilai_default 											// df=1 atau df=now
	| "ref" ":" HURUF 				-> references
	| "refk" ":" HURUF 				-> references_key
	| "(" enumname? stringenumvalues stringenumdefault? ")"	// (satu,dua,tiga>satu)
	| "[" enumname? enumvalues enumdefault "]"
// constraint end

--#

--% langs.ucsv.grammar.subclass_string, string subtype
string_subclass_type: "n"	  -> name
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
--#

--% langs.ucsv.grammar.subclass_number, number subtype
number_subclass_type: "ph"	-> phone_number
| "ccc"					            -> country_calling_code
| "cc"					            -> credit_card_number
| "ccf"					            -> credit_card_full
| "m"					              -> msisdn
| "ssn"					            -> ssn
| "rn" numdigits?           -> random_number
| "ri" min_max? 		        -> random_int				
// python data.py gen data 1 meja hitung:i:ri(-50,60)
| "rd"					            -> random_digit	
| "f"	right_left?           -> pyfloat
| "d"					              -> pydecimal
| "i"					              -> pyint
| "i128"					          -> i128
| "i64"					            -> i64
| "i32"					            -> i32
| "i16"					            -> i16
| "i8"					            -> i8
| "u128"					          -> u128
| "u64"					            -> u64
| "u32"					            -> u32
| "u16"					            -> u16
| "u8"					            -> u8
| "b"                       -> pybool
| "coo"					            -> coordinate
| "lat"					            -> latitude
| "long"				            -> longitude
| "ll"					            -> latlng
| "lll"					            -> local_latlng
| "lol"					            -> location_on_land
--#

--% langs.ucsv.grammar.subclass_date, date/time subtype
date_subclass_type: "b"		  -> simple_profile
| "dtb"					            -> date_time_between
| "iso"					            -> iso8601          // pilihan biasanya iso atau dt/timestamp
| "ut"					            -> unix_time
| "dt"					            -> date_time
| "d"					         	-> date
| "t"					            -> time

# penggunaan
# DateField()
# "d"					              -> date
# TimeField()
# "t"					              -> time
# Q: gimana dg timezone aware?
--#

--% mg, mongoose
mg/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N
--#

--% sqlz, sequelize
--#

--% pg, sql_postgres
--#

--% ms, sql_mssql
--#

--% my, sql_mysql
--#

--% sqlt, sql_sqlite
--#

--% torm, nest_typeorm
--#

--% mg2, nest_mongoose
--#

--% pris, prisma
--#

--% hbr, hibernate
--#

--% bts, mybatis
--#

--% go, struct_go
--#

--% rs, struct_rs
--#

--% kt, struct_kt
--#

--% ts, struct_ts
--#

--% java, struct_java
--#

--% dj, django_orm
--#

--% fl, be_flask
--#

--% fa, be_fastapi
--#

--% nsm, help_nest_mongo
--#

--% nsp, help_nest_postgres
--#

--% json1, json1
--#

--% json2, json2
--#

--% csv, csv
--#

