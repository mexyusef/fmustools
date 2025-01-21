# line expression
g "contoh.txt,f(@line=1,2,3|i+|(aku cuma), n=ini isi untuk coba line-expression)"

contoh.txt,f(@line=1,2,3|i+|(aku cuma), n=ini isi untuk coba line-expression)

insn
  filename      contoh.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      touch_file
    file_dir_operation_type
      operation_attributes          @...
        fileops_line_expression
          line_expression
            line_item
              line_number       1
            line_item
              line_number       2
            line_item
              line_number       3
          line_insert_after
          line_data_literal     aku cuma

# line contains
g "contoh.txt,f(@line>(find me goose)|i+|(aku cuma), n=ini isi untuk coba line-contains)"

@line>(find me goose)|i+|(aku cuma)

insn
  filename      contoh.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      touch_file
    file_dir_operation_type
      operation_attributes          @...
        fileops_line_contains
          line_contains find me goose
          line_insert_after
          line_data_literal     aku cuma

@line>(find me goose)|i+|(aku cuma)

# line matches/regex
insn
  filename      contoh3.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      operation_attributes
        fileops_line_matches
          line_regex    find me goose
          line_insert_after
          line_data_literal     aku cuma
    file_dir_operation_type
      content_file      contoh line matches dengan regex
g "contoh3.txt,f(@line~(find me goose)|i+|(aku cuma), n=contoh line matches dengan regex)
@line~(find me goose)|i+|(aku cuma)

# line between contains
insn
  filename      contoh4.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      operation_attributes
        fileops_line_between_contains
          line_contains start contains
          line_contains end contains
          line_insert_after
          line_data_literal     aku cuma
    file_dir_operation_type
      content_file      contoh line between contains dengan contains-contains

g "contoh4.txt,f(@btw>(start contains)(end contains)|i+|(aku cuma), n=contoh line between contains dengan contains-contains)
@btw>(string start)(string end)|i+|(aku cuma)

# line between matches
insn
  filename      contoh5.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      operation_attributes
        fileops_line_between_matches
          line_regex    start regex
          line_regex    end regex
          line_insert_after
          line_data_literal     aku cuma
    file_dir_operation_type
      content_file      contoh line between matches dengan regex-regex

g "contoh5.txt,f(@btw~(start regex)(end regex)|i+|(aku cuma), n=contoh line between matches dengan regex-regex)
@btw~(regex start)(regex end)|i+|(aku cuma)

# string ops

"str=" string_matches "|" string_operation "|" string_data -> fileops_string_at
"str+" string_matches "|" string_operation "|" string_data -> fileops_string_after
"str-" string_matches "|" string_operation "|" string_data -> fileops_string_before

string_matches: "(" HURUF_ANGKA_SPASI ")"

string_operation: "r" -> string_replace_at
	| "d" -> string_delete_at

string_data: "(" HURUF_ANGKA_SPASI ")" -> string_data_literal

konsep: kita bisa operasi pada string (str=), pada string sesudahnya (str+), pada string sebelumnya (str-)

## string at
@str=(GANTI AKU DONG)|r|(aku ganti dirimu yang jelek itu)
g "contoh-string-at.txt,f(@str=(GANTI AKU DONG)|r|(aku ganti dirimu yang jelek itu), n=ini isi file bohongan1)"
insn
  filename      contoh-string-at.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      operation_attributes
        fileops_string_at
          string_matches        GANTI AKU DONG
          string_replace_at
          string_data_literal   aku ganti dirimu yang jelek itu
    file_dir_operation_type
      content_file      ini isi file bohongan1

## string after
g "contoh-string-after.txt,f(@str+(ALLOWED_HOSTS)|r|(aku ganti semua string setelah mu dalam barismu), n=ini isi file bohongan2)"
insn
  filename      contoh-string-after.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      operation_attributes
        fileops_string_after
          string_matches        ALLOWED_HOSTS
          string_replace_at
          string_data_literal   aku ganti semua string setelah mu dalam barismu
    file_dir_operation_type
      content_file      ini isi file bohongan2

## string before
g "contoh-string-before.txt,f(@str-(LOOK TO THE LEFT)|r|(aku ganti semua string di belakangmu), n=ini isi file ...LOOK TO THE LEFT... bohongan3)"
insn
  filename      contoh-string-before.txt
  filetype
    file
  fileoperation
    file_dir_operation_type
      operation_attributes
        fileops_string_before
          string_matches        LOOK TO THE LEFT
          string_replace_at
          string_data_literal   aku ganti semua string di belakangmu
    file_dir_operation_type
      content_file      ini isi file bohongan3
