--% program dan examples
,<
from app.transpiler.css.main import myrepl
,<code
from app.transpiler.css.main import process_language(code)

,<header/p0,x0,m0,bsbb

block_code
  block_header
    header_items
      header_item       header
  block_body
    key_values
      key_value_to_split        p0
      key_value_to_split        x0
      key_value_to_split        m0
      key_value_to_split        bsbb

header {
    padding: 0;
    x: 0;
    margin: 0;
    bsbb: ;
}

program: block+
block: block_code
  | block_import
--#

--% block_code
block_code: block_config? block_header block_body

block_config: blockconfiglist "/"
blockconfiglist: blockconfigitem+
blockconfigitem: "r" -> react_mode // camel case, not dash
  | "R" -> non_react

block_header: header_items
header_items: header_item ("," header_item)*
header_item: HURUF_DIGIT_COLON_SEMICOLON

//block_body: "/" key_values "/"
block_body: "/" key_values
key_values: key_value ("," key_value)*
key_value: HURUF_DIGIT -> key_value_to_split
  | key_item kv_separator value_item

key_item: HURUF_DIGIT
  | "~" HURUF_DIGIT_DASH_SPASI -> key_item_search

kv_separator: ":"
value_item: HURUF_DIGIT_DASH_SPASI

cssunit: "x" -> unspecified
  | "p" -> pixel
  | "r" -> rem
  | "e" -> em
  | "%" -> percent
  | "vw" -> vw
  | "vh" -> vh
--#

--% block_import
block_import: HURUF_DIGIT_KOMA_POUND
--#
