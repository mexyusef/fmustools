--% examples
daftar contoh yg sudah jalan di sini...

# package

,,go/Pmain
package main

# vars

,,go/$name='usef'
var name = "usef"

,,go/$name:s='usef'
var name string = "usef"

# constants

,,go/%name='usef'
const name  = "usef";

,,go/%name:s='usef'
const name string = "usef";

,,go/%name:Ai=[1,2,3]
const name []int = [1, 2, 3];
harusnya jadi:
name := []int{1,2,3}
name := [3]int{1,2,3}

di sini hrs bisa specify ukuran array.
juga hrs bs specify 2D dan 3D array.
var a [5]int 				# ukuran saja, tanpa init values
b := [5]int{1, 2, 3, 4, 5} 	# ukuran + init values
var twoD [2][3]int 			# ukuran saja

# for loop

## for traditional dg ;
,,go/for(i=1;i<=10;++i) {?+i}
for i := 1; i <= 10; ++i {
    fmt.Println(i)
}

## for each dg $a/b$ atau @a/b@ atau @a/b/i@
,,go/for$i/items${?+'hello'}
for (const i of items) {
    fmt.Println("hello")
}

,,go/for@barang/items@{?+'hello'}
for index, barang := range items {
    fmt.Println("hello")
}

,,go/for@barang/items/indexer@{?+'hello'}
for indexer, barang := range items {
    fmt.Println("hello")
}

,,go/for#i/items#{?+'hello'}
for for (const Tree('nama_jenis_identifier_optional', [Tree('nama_identifier', [Token('HURUF_DIGIT', 'i')])]) in Tree('nama_identifier', [Token('HURUF_DIGIT', 'items')])) {
{
    fmt.Println("hello")
}

## for in/index
for_in: key_name "/" array_name

## for of/value
for_of: item_name "/" array_name

## while
,,go/w//(i==True){} => err, ganti ke: go//w(i==True){?+hello} atau go/w(i==True){?+hello}
           ^ belum masuk, harusnya masuk operator?
           ini dihandle oleh expression item
.
err, harusnya:
go//w(1){?+hello}
go//w(i==True){?+hello}
hasilkan:
while i == True:
fmt.Println(hello)

bukan
go/w//(1){?+hello}
## if

## switch

# interface/trait/mixin

# enum

# class

## class contoh

# instantiation

# constructor/ctor

# field

# method

# function
### deklarasi fungsi

### pemanggilan fungsi

### deklarasi variable bertipe fungsi

### function type

# anonymous function

# funcparam bertipe fungsi

# assignment
ini belum bisa a[4]=100 utk assignment array item
,,go/a=100
a = 100

# import

# package/module/export

# type alias

# generic

# faker

# redis

# string operation

# array operation

# dict operation

# input output
?+i				print variables
?+'hello'		print string

,,go/?+i
fmt.Println(i)

,,go/?+'hello'
fmt.Println("hello")

# dataops

,,py/mydt?dn
const mydt = new Date()

,,py/mydt?dn24-08-78,04:00:00
const mydt = new Date("24-08-78 04:00:00")
--#

--% program
field_method_separator: "|"
statement_separator: ";"
param_separator: ","

program: program_configuration? item_line+

item_line: item_starter? item item_separator?
item_separator: ";"
  | item_separator_newline+
  |

item_starter: item_tab+
item_tab: "\\\\t"
item_separator_newline: "\\\\n"

item: package_item
  | import_item
  | export_item    
  | block_item
  | statement_item
  | expression_item
  | declarative_item
--#

--% package_item
package_item: keyword_package package_things
package_things: package_thing ("." package_thing)*
package_thing: HURUF_DIGIT_ONLY
--#

--% import_item
import_item: keyword_import import_config? import_container? import_things
  | keyword_import import_config? searchable

import_config: "/" importconfiglist "]=/"
importconfiglist: importconfig ("," importconfig)*
importconfig: "d" -> import_default // import { ... as default }
  | "m" -> import_module            // const ... = require(..)

// import sys
// from tree_sitter import Language, Parser

// Itempat|(item)
// Itempat|item,item,/item,/item
import_container: HURUF_DIGIT_DOT "|"

import_things: import_thing ("," import_thing)*
  | "(" import_things ")" -> import_things_enclose_all
import_thing: HURUF_EXPORT -> import_thing_default
  | "/" import_thing -> import_thing_enclose
--#

--% export_item
export_item: keyword_export export_config? export_content

// export src/calc.dart, src/music.dart
// export "src/calc.dart"; newline export "src/music.dart"

export_config: exportconfiglist "/"
exportconfiglist: export_config_item+
export_config_item: "d" -> export_default
  | "m" -> export_module    // module.exports = .., correspondingly utk import const .. = require(..)
  | "o" -> export_objectify // export {bla1, bla2, bla3};
export_content: "(" exportcontentlist ")"
exportcontentlist: exportcontent ("," exportcontent)*
exportcontent: HURUF_EXPORT
--#

--% block_item
block_item: scope_item
  | class_item
  | function_item
  | exception_item
  | interface_item
--#

--% scope_item
// ||//{}

scope_item: keyword_scope scope_config? condition_body
//scope_item: keyword_scope scope_config? scope_content
//scope_content: "{" condition_body "}"

scope_config: "/" scopeconfiglist "/"
scopeconfiglist: scopeconfig ("," scopeconfig)*
scopeconfig: "sc" -> dummy_scope_config

//scope_content: "{" scopecontentlist "}"
//scopecontentlist: scopecontent ("," scopecontent)*
//scopecontent: "s"
//  |
--#

--% class_item
class_item: "@" class_config? class_name class_content

// public
// implements interface x
// extends class x
// export
// decorated: @InputType()
class_config: "/" classconfiglist "/"
classconfiglist: classconfig ("," classconfig)*

// @/i:observable,:parent_class,@override/myclass
// bisa mult interface: @/i:satu,i:dua/myclass
// bisa juga bikin utk bantuan ini dan itu: graphql? grpc? mvc model? db table?
classconfig: "+" -> public
  | "-" -> private    // perlu utk class?
  | "#" -> protected  // perlu utk class?
  | "i" -> interface  // interface declare
  | "i+" -> interface_add // buat class decl+interface decl
  | "t" -> type_alias // kita buat juga type_alias versi single statement
  | "t+" -> type_alias  // class+type
  | "@" nama_identifier   -> decorator
  | ":" nama_identifier   -> extends
  | "i:" nama_identifier  -> implements // interface (beda i dan i: = beda func decl dan call)
  | "^" -> abstract // juga perlu final dan strictfp
  | "%" -> static
  | "F" -> final
  | "SF" -> strictfp
  | "D" -> default
  | "A" -> async
  | ">" -> explicit_default_constructor // percepat ngetik

// masukkan initializer list di sini...

// class name hrs bisa terima type parameters...
class_name: nama_identifier_with_typeparams

class_content: "{{" classcontentlist* "}}"
classcontentlist: classcontent ({field_method_separator} classcontent)*
// field content
// method content
// field dan method terbedakan dg adanya funcargs-funcbody utk method
classcontent: field_content
  | constructor_content
  | method_content
  |
--#

--% field_content
// sementara belum ada inisialisasi field
// mungkin perlu? tinggal tambah declaration_value? di ts bisa: https://www.typescriptlang.org/docs/handbook/2/classes.html
// tambah declaration_value? agar bisa inisialisasi field spt di ts

// dart: int? _private; yg nullable blm kehandle
// nama_jenis_identifier_nullable: nama_identifier "?" tipe_identifier
// baru dipake di funcparam utk funcdecl

field_content: field_config? field_name tipe_identifier? declaration_value?

field_config: "/" fieldconfiglist "/"
fieldconfiglist: fieldconfig ("," fieldconfig)*
// static
// final
// decorated: @Field()
fieldconfig: "+" -> public
  | "-" -> private
  | "#" -> protected
  | "ro" -> read_only       // readonly name: string = "world"; hanya assign dlm ctor
  | "%" -> static
  | "F" -> final
  | "L" -> late

field_name: HURUF_DIGIT

field_name_type: nama_identifier tipe_identifier? -> non_nullable_field
  | nama_jenis_identifier_nullable -> nullable_field
--#

--% method_content
method_content: method_config? function_name tipe_identifier? function_param function_content

method_config: "/" methodconfiglist "/"
methodconfiglist: methodconfig ("," methodconfig)*
// decorated: @Override
// static
// public
methodconfig: "g" -> getter   // this method is a getter
  | "s" -> setter             // this method is a setter
  | "+" -> public
  | "-" -> private
  | "#" -> protected
  | "%" -> static     // ingat python ada class vs static yg berbeda dikit konsepnya
  | "A" -> async
  | "o" -> override   // cepat @Override etc
--#

--% constructor_content

// > utk bedakan dg method
constructor_content: ">" constructor_config? function_param function_content

constructor_config: "[" constructorconfiglist "]"
constructorconfiglist: constructorconfig ("," constructorconfig)*
// termasuk ada destructor
constructorconfig: "c"
--#

--% function_item
function_item: keyword_function function_config? function_name tipe_identifier? function_param function_content

function_config: functionconfiglist "/"

//functionconfiglist: functionconfig ("," functionconfig)*
//:ai/foo(){}
functionconfiglist: functionconfig+

// language config -> /js, /py, /kt, /rs, /scala
// decorator
// async
// iife
// anonymous, lambda, closure, inner, arrow
// contoh di rust: const myconst = async (funcparams): Promise<sometype> => {}
// export + default
functionconfig: "+" -> public
  | "-" -> private
  | "#" -> protected
  | "%" -> static
  | "a" -> async
  | "x" -> export
  | "w" -> arrow
  | "i" -> iife
  | "no" -> anonymous

function_name: nama_identifier_with_typeparams

function_type: ":" HURUF_DIGIT

function_param: "(" paramlist* ")"
paramlist: param ("," param)*
// nama_jenis_identifier_optional = nama_identifier | nama_jenis_identifier
param: named_values
  | nama_identifier
  | nama_jenis_identifier
  | nama_jenis_identifier_nullable

// digunakan di expression-item:
// new_operator nama_identifier function_call_param -> instantiation_expression
function_call_param: "(" callparamlist* ")"
callparamlist: callparam ("," callparam)*
callparam: named_values
  | nama_identifier
  | literal  

// ini jadi setara dg function_call_param
argument_list: argument ("," argument)*
argument: expression_item
  | named_values
  | anonymous_function

function_content: "{" functioncontentlist* "}"
functioncontentlist: functioncontent (statement_separator functioncontent)*
functioncontent: statement_item
--#

--% anonymous_function
// anon func digunakan di argumentlist dari func decl/def
// tidak bisa (){}
// (satu,dua)24
// (satu,dua,42){} -> hasilkan 2 model: arrowfunc dan normalfunc
// statement_item dlm condition_body dipisah oleh separator
// utk arrow func, jk hanya ada satu statement maka gak perlu {} di output
anonymous_function: non_arrow_func? function_config? function_param anonymous_function_body

// utk bilang jangan gunakan arrow func -> :
non_arrow_func: keyword_function

anonymous_function_body: "{" statement_item (statement_separator statement_item)* "}" -> anon_statements
  | expression_item -> anon_expression
--#

--% exception_item
exception_item: exception_keyword exception_config? try_content except_content finally_content?

exception_config: "/" exceptionconfiglist "/"
exceptionconfiglist: exceptionconfig ("," exceptionconfig)*
// mungkin bisa kasih nama utk exception?
exceptionconfig: "x"

try_content: condition_body

//trycontentlist: trycontent ("," trycontent)*
//trycontent: "t"
//  | statement_item
//  |

except_content: exceptcontentlist
exceptcontentlist: exceptcontent (exceptcontent)*
exceptcontent: on_block_version? "(" exception_header ")" condition_body
exception_header: HURUF_DIGIT
on_block_version: "*" -> on_block
  | "$" -> on_catch_block // on IntegerDivisionByZeroException catch(e)

//except_content: "(" exceptcontentlist ")"
//exceptcontentlist: exceptcontent ("," exceptcontent)*
//exceptcontent: "x"
//  | statement_item
//  |

finally_content: "()" condition_body

//finally_content: "(" finallycontentlist ")"
//finallycontentlist: finallycontent ("," finallycontent)*
//finallycontent: "f"
//  | statement_item
//  |
--#

--% interface_item
# interface hanya berisi method, tapi utk antisipasi berbagai bhs yg berbeda2
# kita samakan dg class
# mari bikin interface, abstract class, dll di sini (sementara)

interface_item: interface_keyword class_config? class_name class_content
--#

--% dataops_statement
dataops_statement
--#

--% statement_item
statement_item: if_statement
  | for_statement
  | switch_statement
  | while_statement
  | single_statement
  | expression_item
  | enum_declaration
--#

--% if_statement
// if (if) {var myvar = 24}
if_statement: if_keyword condition_then_if (condition_then_elif)* condition_then_else?

condition_then_if: condition_if condition_body
condition_then_elif: condition_elif condition_body
condition_then_else: condition_else condition_body

condition_if: "(" expression_item ")"
condition_elif: "'(" expression_item ")"
condition_else: "()"
--#

--% for_statement
for_statement: for_keyword for_config? condition_for condition_body

for_keyword: "/4"
  | "for"

// harus bisa handle: for, for each, for in, for of
// for i=0; i<expession; i++
// for-each item,key of array
// for-in key of array
// for-of item of array

condition_for: for_variation
for_variation: "(" for_traditional ")"  // for(i=0;i<dict.length;i++)
  |  "(" for_while? ")" -> for_ever // for(i<10), for()
  | "@" for_each "@"  // for@item/items/index@ = for key,value
  | "#" for_in "#"    // for#key/items# = for key/index
  | "$" for_of "$"    // for$item/items$ = for value

// apa gak mendingan: for(name,start,end,step) => for(index,0,42,2)
for_traditional: for_start ";" for_end (";" for_step)?
for_while: expression_item
for_each: item_name "/" array_name ("/" key_name)?
for_in: key_name "/" array_name
for_of: item_name "/" array_name

//for_start: key_name "=" expression_item
for_start: nama_jenis_identifier_optional "=" expression_item
for_end: expression_item
for_step: expression_item

key_name: nama_jenis_identifier_optional
item_name: nama_jenis_identifier_optional
array_name: nama_identifier
  | expression_item

for_config: "[" for_config_items "]"
for_config_items: for_config_item ("," for_config_item)*
// gunakan for-traditional, create local var, use nonlocal var, for-in, for-of
for_config_item: "c"
--#

--% switch_statement
switch_statement: switch_keyword switch_config? condition_switch case_body+
switch_keyword: "/s"
  | "switch"
  | "sw"
  | "s"

condition_switch: "(" expression_item ")"

case_body: (condition_case|condition_defaultcase) condition_body

condition_case: "(" expression_item ")"
condition_defaultcase: "()"

switch_config: "/" switch_config_items "/"
switch_config_items: switch_config_item ("," switch_config_item)*
// gunakan switch(literal) dll
switch_config_item: "c"
--#

--% while_statement
while_statement: while_keyword while_config? condition_while condition_body
while_keyword: "/w"
  | "while"
  | "wh"
  | "w"

condition_while: "(" expression_item ")"

while_config: "/" while_config_items
while_config_items: while_config_item ("," while_config_item)*
// gunakan do-while, etc
while_config_item: "f" -> forever_loop

masalah:
go/w/(1){?+hello}
program_configuration_items
  program_configuration_item
    go

program_configuration_items => chosen languages = ['go']
item
  statement_item
    expression_item
      anonymous_function
kenapa masuk anon?
--#

--% single_statement
////////////////////////////////////////////////////////////////
// assignment
// initialization sama dg assignment?
// variable statement (dihandle $)
// typealias decl, enum decl
// throw (throw stmt), return (return stmt), yield (yield stmt), flow (continue+break stmt)
// with stmt, labelled stmt, debugger stmt
// empty stmt -> typescript hanya semicolon (terminator)
// abstract decl, namespace decl, interface decl, decorator list, generatorfunc decl
// expressionSequence adlh if(..), for(..; ..; ..), while(..), switch(..)
// tmsk di sini: function item (func+arrowfunc decl), exception item (try stmt), import item, export item, class item (class decl)
// tmsk: iteration stmt yg dihandle for+while
// tmsk: if stmt dan switch stmt yg sudah dihandle

single_statement: var_declaration
  | const_declaration
  | assignment_statement
  | flow_statement
  | return_statement
  | throw_statement
  | yield_statement
  | defer_statement
  | dataops_statement_with_identifier
  | stdout_operation
  | faker_ops
  | fmus_ops
  | redis_operation
  | typealias_declaration
  | destructuring_statement
  | "~" declarative_program

// dari go: defer statement

--#

--% dataops_statement_with_identifier
dataops_statement_with_identifier: nama_identifier dataops_statement
--#

--% assignment_statement
assignment_statement: nama_identifier assignment_config? "=" expression_item
assignment_config: ":" -> assignment_initialize // di v lang a = 42 vs a := 42
--#

--% typealias_declaration
typealias_declaration: typealias_keyword nama_identifier type_parameters? "=" tipe_data_semua
--#

--% flow_statement
flow_statement: flow_continue
  | flow_break
flow_continue: "continue"
  | "cont"
  | "co"
flow_break: "break"
  | "br"
--#

--% return_statement
return_statement: ">" expression_item
--#

--% throw_statement
throw_statement: ">>" throw_name? expression_item
throw_name: HURUF_DIGIT "/"
--#

--% yield_statement
yield_statement: ">>>" expression_item
--#

--% defer_statement
// dari go: defer statement
defer_statement: ">>>>" expression_item
--#

--% destructuring_statement
# /=satu,dua,tiga/empat/
# =/satu,dua,tiga/empat/
# =/o/satu,dua,tiga/empat/

destructuring_statement: destructuring_markstart destructuring_config? destructuring_content destructuring_markend
destructuring_markstart: "=/"
destructuring_markend: "/"
destructuring_config: destructuringconfiglist "/"
destructuringconfiglist: destructuringconfig+
destructuringconfig: "o" -> object // default
  | "l" -> list
  | "t" -> tuple

destructuring_content: destructuring_lhs "/" destructuring_rhs
destructuring_lhs: destructuring_lhs_item ("," destructuring_lhs_item)*

destructuring_lhs_item: HURUF_DIGIT_DESTRUCTURING
destructuring_rhs: HURUF_DIGIT_DESTRUCTURING
--#

--% var_declaration
// var myvar = 32, var myvar = E myfunc()
var_declaration: "$" declaration_config? declaration_name tipe_identifier? declaration_value?
--#

--% const_declaration, declaration_config
const_declaration: "%" declaration_config? declaration_name tipe_identifier? declaration_value?

// mutable dan immutable sudah dihandle oleh $ dan %
// $ pasti mutable let mut myvar = value;
declaration_config: "/" declarationconfiglist "/"

//declaration_config: declarationconfiglist
declarationconfiglist: declare_config ("," declare_config)*

// instance field, static field
// $stack=[]
declare_config: "+" -> public
  | "-" -> private
  | "#" -> protected
  | "%" -> static
  | "L" -> late
  | "F" -> final

declaration_name: HURUF_DIGIT

declaration_value: "=" expression_item
--#

--% declarative_program
single_statement: var_declaration
...
| "~" declarative_program
declarative_program: HURUF_KODE_FRONTEND
--#

--% expression_item
expression_item: function_call  // myfunc(34), myfunc(param1=42)
  | anonymous_function          // (req,res){}
  | literal
  | member_dot_expression
  | member_index_expression
  | casting_expression
  | expression_with_operator
  | nama_identifier
  | new_operator nama_identifier function_call_param -> instantiation_expression
  | range_expression
--#

--% casting_expression
casting_expression: expression_item (keyword_casting expression_item)+
--#

--% expression_with_operator
expression_with_operator: "!" expression_item -> not_expression
  | "++" expression_item -> pre_inc_expression
  | "--" expression_item -> pre_dec_expression
  | expression_item "++" -> post_inc_expression
  | expression_item "--" -> post_dec_expression
  | expression_item "+=" literal -> plus_equal_expression
  | expression_item "-=" literal -> minus_equal_expression
  | expression_item "?" expression_item ":" expression_item -> ternary_expression
  | expression_item "&&" expression_item -> and_expression
  | expression_item "||" expression_item -> or_expression
  | expression_item arithmetic_operator expression_item -> arithmetic_expression
  | expression_item relational_operator expression_item -> relational_expression <- ini padahal handle == dan !=

C:\Users\usef\work\sidoarjo\data\github\lalang>grep -r "expression_with_operator" .
./item_expression/__init__.py:  | expression_with_operator
./item_expression/__init__.py:expression_with_operator: "!" expression_item -> not_expression
--#

--% member_index_expression
// member index = obj[index]
// [ei]([ei])* atau ([ei])+
//member_index_expression: expression_item "[" expression_item "]" ("[" expression_item "]")*
member_index_expression: expression_item ("[" expression_item "]")+
--#

--% member_dot_expression
// member dot = obj.member
// nama.nama(.nama)* atau nama (.nama)+
// member_dot_expression: nama_tanpa_dot "." nama_tanpa_dot ("." nama_tanpa_dot)*
member_dot_expression: nama_tanpa_dot ("." nama_tanpa_dot)+
--#

--% function_call
function_call: function_name function_call_config? "(" argument_list* ")"

function_call_config: "/" funccallconfiglist

funccallconfiglist: funccall_config+
funccall_config: "a" -> await
--#

--% operator
// myobj = *MyClass{}
new_operator: "*"

arithmetic_operator: "+" -> operator_plus
  | "-" -> operator_minus
  | "*" -> operator_mult
  | "/" -> operator_float_division
  | "//" -> operator_int_floor_division
  | "%" -> operator_remainder

relational_operator: "<" -> operator_less
  | "<=" -> operator_less_equal
  | ">" -> operator_greater
  | ">=" -> operator_greater_equal
  | "==" -> operator_equal
  | "!=" -> operator_not_equal
--#

--% literal
literal: literal_number
  | literal_string
  | template_string // <my name is /name/ so take care yo>
  | literal_bool
  | literal_char
  | literal_list
  | literal_dict // termasuk literal obj di sini
  | literal_tuple // termasuk pair
  | literal_pair
  | literal_set

literal_template_string: literal_string
  | template_string

literal_number: BILBUL_BERTANDA
literal_string: "\\"" HURUF_TEMPLATESTRING "\\"" // "hello"
  | "'" HURUF_TEMPLATESTRING "'" // 'hello'
template_string: "<" HURUF_TEMPLATESTRING ">"
literal_bool: "T" -> boolean_true
  | "F" -> boolean_false
literal_char: "'" LETTER "'" // 'a'

literal_list: "[" list_items* "]"
list_items: list_item ("," list_item)*
list_item: expression_item

// krn () dan {} rebutan dg func param dan body
literal_dict: "{#" dict_items* "}"
dict_items: dict_item ("," dict_item)*
dict_item: dict_item_name ":" expression_item
dict_item_name: HURUF_DIGIT

literal_tuple: "(#" tuple_items* ")"
tuple_items: tuple_item ("," tuple_item)*
tuple_item: expression_item

literal_pair: "(@" tuple_item "," tuple_item ")"

// <> skrg dipake oleh template_string
literal_set: "<#" set_items* ">"
set_items: set_item ("," set_item)*
set_item: expression_item
--#

--% range_expression
## ..5,10 = 5,6,7,8,9
## ..//5,10 = 5,6,7,8,9,10
## ../to5 = 0,1,2,3,4
## ..//to5 = 0,1,2,3,4,5
## ../from10 = 10,11,12 (default = from)

range_expression: range_keyword range_expr_config? range_start "," range_stop ("," range_step)?

range_start: BILBUL
range_stop: BILBUL
range_step: BILBUL

range_expr_config: "/" range_expr_items
range_expr_items: range_expr_item ("," range_expr_item)*
// gunakan do-while, etc
range_expr_item: "/" -> range_config_close // inclusive range end, ..//start,stop,step
  | "to" -> range_config_to
  | "from" -> range_config_from
--#

--% enum_declaration
# &myenum{yo=42, yi=43, yu=44}

enum_declaration: enum_keyword enum_config? nama_identifier "{" enum_body "}"
enum_config: "#" -> enum_numeric // default
  | "$" -> enum_string

enum_body: enum_member_list ","?
enum_member_list: enum_member ("," enum_member)*
enum_member: nama_identifier ("=" expression_item)?
--#

--% declarative_item
declarative_item: "D"
--#

--% keywords
keyword_function    : ":"
keyword_import      : "I"
keyword_package     : "P"
keyword_export      : "X:"
keyword_casting     : ">>"
//keyword_scope: "(s)"
keyword_scope       : "||"
//
range_keyword       : ".."

typealias_keyword   : "&&"
interface_keyword   : "@@"
if_keyword          : "if"
//searchable_kw     : "~"
searchable_kw       : "`" // `kata utk dicari`
fmus_keyword        : "!!"
enum_keyword        : "&"
exception_keyword   : "x:"
csv_keyword         : "csv:"
--#

--% name, name

named_values: named_value ("," named_value)*
named_value: nama_identifier tipe_identifier? "=" nilai_identifier
nilai_identifier: expression_item

// ini bisa expression: pemanggilan fungsi (berarti bisa ada dot dong)
nama_tanpa_dot: HURUF_DIGIT_ONLY
nama_identifier: HURUF_DIGIT
nama_identifier_or_literal: literal
  | nama_identifier

// utk bedakan dg nama_identifier, tipe dibikin wajib di sini
// lihat juga: nama_identifier_with_typeparams
nama_jenis_identifier: nama_identifier tipe_identifier
nama_jenis_identifier_optional: nama_identifier tipe_identifier?

// kita hrs punya bentuk: (satu:i, dua?:f)
nama_jenis_identifier_nullable: nama_identifier "?" tipe_identifier

--#

--% jenis, tipe, type

// string, int, float, bool, char, any/object, void
// tipe_data_collection mendahului tipe_data_buatan spy gak kemakan
tipe_identifier: ":" tipe_data_config? tipe_data_builtin 
  | ":" tipe_data_config? tipe_data_collection
  | ":" tipe_data_config? tipe_data_buatan
  | ":" tipe_data_fungsi
  | ":" type_intersection
  | ":" type_union

// sementara hanya built in?
type_intersection: tipe_data_builtin ("&" tipe_data_builtin)+
type_union: tipe_data_builtin ("|" tipe_data_builtin)+

tipe_data_config: "[" tipe_data_config_items "]"
tipe_data_config_items: tipe_data_config_item ("," tipe_data_config_item)*
// dibungkus dg Promise, Option, Result, dll
// gunakan versi boxing: Integer, String, dll
// extend another type?
// juga utk gunakan subtype, i -> long, f -> double, s -> max length if applicable
tipe_data_config_item: "tdci"

tipe_data_builtin: "s" -> string
  | "i" -> integer    // i32
  | "f" -> float
  | "a" -> any        // kita bikin default: undefined
  | "b" -> boolean
  | "c" -> char
  | "dd" -> double
  | "dt" -> datetime
  | "h" -> short      // i16
  | "l" -> long       // i64
  | "y" -> byte       // ~ i8
  | "v" -> void       // any dan object masuk sini, kita bikin default: null
tipe_data_buatan: nama_identifier

tipe_data_semua: tipe_data_builtin
  | tipe_data_collection
  | tipe_data_fungsi
  | tipe_data_buatan
  | object_type

// name: ^&*[nama_identifier:type/type]
// [nama:s/s], ^[nama:s/s], &[nama:s/s], *[nama:s/s]
//tipe_data_fungsi: tipe_data_fungsi_config? "[" nama_identifier ":" tipe_data_semua "/" tipe_data_semua "]"
// apa perlu condition_body? utk statement list?
// const last = (arr:Array<number) => ...condition body... = return arr[arr.length-1]
// %last=[]...condition body...
tipe_data_fungsi: tipe_data_fungsi_config? type_parameters? "[" paramlist* "/" tipe_data_kembali? "]" condition_body?
tipe_data_kembali: tipe_data_semua
tipe_data_fungsi_config: "^" -> function_type_expression // default
  | "&" -> call_signature
  | "*" -> construct_signature

// (nama_identifier: real_type) => real_type
// function_type_expression: 

// hrs bs specify array of what...
// default = array of any/object
// A, D, DF, I, F, N, O, P, S, L
tipe_data_collection: "A" item_type?  -> array      // As
  | "D" (key_type "," value_type)?    -> dict       // Di,s
  | "DF" row_type "," column_type     -> dataframe  // DFs,s
  | "I"                               -> directory  // I
  | "F" file_type?                    -> file       // Fj
  | "N" network_type?                 -> network    // Ngrpc
  | "O" orm_type?                     -> orm        // Osqal
  | "P" (key_type "," value_type)?    -> pair       // Pi,s
  | "S" item_type?                    -> set        // Ss
  | "L" (item_type ("," item_type)*)? -> tuple      // Li,s,f
  | "O" some_type "," none_type          -> optional
  | "R" ok_type "," err_type             -> result
  | "P" value_type                    -> promise

// T, U, V suka digunakan utk generic, jadi tuple = L

// sementara baru tipe data primitif...
item_type: tipe_data_builtin
  | "/" tipe_data_buatan
key_type: tipe_data_builtin
value_type: tipe_data_builtin
  | "/" tipe_data_buatan
row_type: tipe_data_builtin
column_type: tipe_data_builtin
some_type: tipe_data_builtin
none_type: tipe_data_builtin
ok_type: tipe_data_builtin
err_type: tipe_data_builtin


file_type: "t"    -> file_text
  | "c"           -> file_csv
  | "doc"         -> file_doc
  | "h"           -> file_html
  | "j"           -> file_json
  | "rss"         -> file_rss
  | "xls"         -> file_xls
  | "xml"         -> file_xml
  | "y"           -> file_yaml

network_type: "R" -> network_rest
  | "d"           -> network_database
  | "gql"         -> network_graphql
  | "grpc"        -> network_grpc
  | "h"           -> network_http
  | "k"           -> network_kafka  
  | "m"           -> network_mqtt
  | "rmq"         -> network_rabbitmq
  | "s"           -> network_spark
  | "t"           -> network_tcp
  | "u"           -> network_udp
  | "w"           -> network_websocket

orm_type: "dj"    -> orm_django
  | "p"           -> orm_prisma
  | "sqal"        -> orm_sqlalchemy
  | "torm"        -> orm_typeorm

type_parameters: "<" type_parameter_list ">"
type_parameter_list: type_parameter ("," type_parameter)*
type_parameter: nama_identifier constraint?
  | type_parameters

// tipe data collection sementara diskip di sini
constraint: ":" tipe_data_buatan // <satu:dua> => <satu extends dua>
  | ":" tipe_data_builtin
  | ":" tipe_data_fungsi
  | ":" object_type

object_type: "{{" object_contents* "}}"
object_contents: object_content (statement_separator object_content)*
object_content: nama_identifier tipe_identifier

// aslinya "extends" union/intersection/primary-type | functype | ctortype | typegeneric | stringliteral
// class myclass<T:[name:s/s]>
// class myclass<T:{{length:number}}>
nama_identifier_with_typeparams: nama_identifier type_parameters?
--#

--% searchable
// I`satu dua tiga -empat -lima enam`
searchable: searchable_kw search_term searchable_kw
search_term: HURUF_SEARCHABLE
--#
