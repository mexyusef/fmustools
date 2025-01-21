gui_languages = """
gui_program: "@g" widgets
widgets: widget (widget)*
container: form     container_children?
  | frame           container_children?
  | layout          container_children?
  | menu            container_children?
  | toolbar         container_children?
  | window          container_children?

container_children: "(" widgets ")"

widget: container
  | event
  | appbar
  | button
  | card
  | checkbox
  | drawer
  | fab
  | filedialog  
  | formitem
  | icon
  | imageview
  | input
  | label  
  | listview  
  | menuitem
  | message
  | modal
  | popup
  | progress
  | radio
  | select
  | spin
  | statusbar
  | tab
  | table
  | textarea
  | tooltip
  | treeview  

appbar                  : "AB"
button                  : "B"
card                    : "CA"
checkbox                : "C"
drawer                  : "D"
event                   : "E"
fab                     : "FAB"
filedialog              : "FD"
form                    : "F"
formitem                : "FI"
frame                   : "FR"
icon                    : "IC"
imageview               : "IV"
input                   : "I"
label                   : "L"
layout                  : "LY"
listview                : "LV"
menu                    : "M"
menuitem                : "MI"
message                 : "MSG"
modal                   : "MO"
popup                   : "POP"
progress                : "P"
radio                   : "R"
select                  : "S"
spin                    : "SP"
statusbar               : "SB"
tab                     : "TAB"
table                   : "TBL"
textarea                : "TA"
toolbar                 : "TB"
tooltip                 : "TT"
treeview                : "TV"
window                  : "W"
"""
