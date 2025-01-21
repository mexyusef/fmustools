# from .flutter import flutter_languages
flutter_languages = """
flutter_program: "#flutter"
"""

mobile_languages = f"""

mobile_program: "#mob#" mobile_widgets
mobile_widgets: mobile_container* mobile_control*
| mobile_container
| mobile_control

// dipake gimana nih...
mobile_async : ""

mobile_container: mobile_form
| mobile_layout
| mobile_header
| mobile_rightbar
| mobile_sidebar

mobile_form : mobile_form_item ("," mobile_form_item)*
mobile_form_item: mobile_textfield
  | mobile_textarea
  | mobile_combobox
  | mobile_radio
  | mobile_switch

mobile_layout : ""
mobile_header : ""
mobile_rightbar : ""
mobile_sidebar : ""
mobile_menu: ""

mobile_bottombar : ""
mobile_drawer: ""

mobile_control: mobile_alert
| mobile_animation
| mobile_fab

mobile_alert : ""
mobile_animation : ""
mobile_fab : ""

mobile_icon : ""
mobile_image : ""
mobile_keyboard : ""
mobile_label : ""

mobile_gridview : ""
mobile_listview : ""
mobile_scrollview : ""

mobile_loading : ""
mobile_popup : ""
mobile_richtext : ""

mobile_tab : ""
mobile_theme : ""

mobile_datepicker : ""
mobile_timepicker : ""
mobile_picker : ""

mobile_textfield : ""
mobile_textarea : ""
mobile_combobox : ""
mobile_radio : ""
mobile_switch : ""

{flutter_languages}
""" 
