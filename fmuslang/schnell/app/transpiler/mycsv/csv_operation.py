csv_operation = """
program: csv_operations
csv_operations: csv_operation (statement_separator csv_operation)*
statement_separator: "|"
csv_operation: csv_config? csv_code

csv_config: csv_items "/"
csv_items: csv_item ("," csv_item)*
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
  | "all"       -> everything
  | "fmus"      -> fmusdir

csv_code: HURUF_KODE_CSV
// "[" utk konfig db/collection, "{" utk konfig table/document
// gara2 gak include space...jadi gak bisa {@User}<space>username,s
HURUF_KODE_CSV: 						("_"|LETTER|DIGIT|"["|"{") 	("_"|LETTER|DIGIT|"."|","|":"|";"|"@"|"#"|"="|"/"|"["|"]"|"{"|"}"|"("|")"|"<"|">"|"-"|" "|NEWLINE)*
"""
# HURUF_FOLDER_SYSTEM: ("_"|LETTER|DIGIT|"/"|"."|"@"|"$"|"%"|"&"|"#"|"["|"]"|"~"|"?"|" "|"\\") (LETTER|DIGIT|"["|"]"|"*"|"."|":"|";"|"/"|","|"("|")"|"{"|"}"|"+"|"-"|"_"|"="|" "|"%"|"$"|"@"|"&"|"\\"|"\""|"!"|"<"|">"|"?"|"|"|"'"|"#"|"^"|"~"|/\t/)*

from schnell.langs import base_grammar

bahasa = f"""
{csv_operation}

// csv_keyword: "$"

{base_grammar}
"""
