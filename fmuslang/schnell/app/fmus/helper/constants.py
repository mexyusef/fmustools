import enum

"""
kita gunakan istilah
"line_indicator" utk pattern dari line yg dicari pada source
"singkat" utk "baris_entry" dari new/target yg mau dijadikan output
"singkat" (level grammar.py) juga dinamai "line_content" (level processor.py)

mungkin nama yg lebih baik
singkat/line_content          baris_entry
line_indicator                baris_find
"""

class InsertReplace(enum.Enum):
  InsertBefore = 1
  InsertAfter = 2
  ReplaceAt = 3
  ReplaceFrom = 4
  RemoveLines = 5
  ReplaceEntry = 6
  ReplaceBetween = 7
  ReplaceString = 8
  ReplaceContent = 9 # replace whole file content
  CommentFile = 10 # replace whole file content

