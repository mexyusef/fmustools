video_languages = """
video_program: "@v" video_operations
video_operations: video_operation (video_operation)*
video_operation: choose_dir
  | choose_fileopen
  | choose_filesave
  | start_time
  | start_frame
  | number_of_frame
  | get_frame
  | show_frame
  | cut_and_save
  | exclude_and_save

choose_dir                                : "cd"
choose_fileopen                           : "cfo"
choose_filesave                           : "cfs"
start_time                                : "st"
start_frame                               : "sf"
number_of_frame                           : "nof"
get_frame                                 : "gf"
show_frame                                : "sf"
cut_and_save                              : "c&s"
exclude_and_save                          : "x&s"
"""
