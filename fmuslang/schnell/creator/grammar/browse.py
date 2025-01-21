browse_languages = """
browse_program: "~browse" browse_spec?
browse_spec: "(" browse_subdir ")"          -> level_1
| "(" browse_subdir "," browse_mk_file ")"  -> level_2

browse_subdir:    HURUF_DIGIT_MINUSPLUS
browse_mk_file:   HURUF_DIGIT
"""
