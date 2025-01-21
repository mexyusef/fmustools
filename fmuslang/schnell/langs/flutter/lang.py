lang_header = """
program: directory_spec
| file_spec
| program_spec
directory_spec: directory_name directory_operation
| directory_spec file_spec
file_spec: file_name file_operation
| file_spec program_spec
program_spec: import_spec var_spec class_spec func_spec
| import_spec 
| var_spec 
| class_spec
| func_spec
class_spec: class_stateless
| class_stateful
class_stateless: func_spec+
class_stateful: class_members
class_members: member_methods member_fields
| member_methods
| member_fields
func_spec: func_name func_params func_return
member_methods: constructor
member_fields:
func_name 
func_params 
func_return: widgets
widgets: widget ("," widget)*
widget: widget_type widget_attributes
widget_attributes: widget_attr ("," widget_attr)*
widget_attr: attr_name attr_values
attr_values: attr_value ("," attr_value)*
attr_value: 
"""

lang_body = """
"""
