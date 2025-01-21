frontend_languages = """
fe_operations: fe_oper ("," fe_oper)*
fe_oper: create_index
  | create_app
  | create_route
  | create_layout

create_index            : "cri"
create_app              : "cra"
create_route            : "crr"
create_layout: create_panel ("," create_panel)*
create_panel: create_main
  | create_header
  | create_sidebar
  | create_rightbar
  | create_footer
create_main     : "crlm"
create_header   : "crlh"  -> create_header_default
  | create_header_profile
  | create_header_hamburger
  | create_header_searchbar
  | create_header_notification
  | create_header_setting
  | create_header_general
  | create_header_logout
create_sidebar  : "crls"
create_rightbar : "crlr"
create_footer   : "crlf"

create_header_profile       : "crlhp"
create_header_hamburger     : "crlhh"
create_header_searchbar     : "crlhs"
create_header_notification  : "crlhn"
create_header_setting       : "crlht"
create_header_general       : "crlhg"
create_header_logout        : "crlhl"
"""
