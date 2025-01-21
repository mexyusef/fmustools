declarative_languages = """
declaratives___: element (element)*
// <div [class=monyet] @@[react] (...)
// sementara kode dari @@[react] akan masuk ke <div class=monyet> ...kode di sini...
element: "<" element_name element_config? cdata_text? frontend_usage? element_children?
  | frontend_usage


element_name: HURUF_DIGIT transformer?
element_config: "[" element_config_item ("," element_config_item)* "]"
element_config_item: HURUF_DIGIT
  | item_key "=" item_value       -> item_key_value

element_children: "(" declaratives___ ")"
item_key: HURUF_DIGIT
// item value hrs bisa terima:
// ' " { } ( ) [ ] / @ : ;
// <Route path="/@:username/favorites" component={ProfileFavorites} />
item_value: HURUF_DIGIT_SPASI transformer?

cdata_text: "*" HURUF_DIGIT
frontend_usage : "@@" "[" HURUF_FOLDER "]"

// [k=v'd], [k=v'-] hasilkan - something
transformer: transform_value (transform_value)*
transform_value: "'" -> tx_single
| "''" -> tx_double
| "'d" -> tx_double
| "'c" -> tx_braces
| "'k" -> tx_brackets
| "'p" -> tx_parentheses
| "'-" -> tx_prepend_minus
| "'A" -> tx_capitalize
| "'l" -> tx_lower
| "'u" -> tx_upper
"""
