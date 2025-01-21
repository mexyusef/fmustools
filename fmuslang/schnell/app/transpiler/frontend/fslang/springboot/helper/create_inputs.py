create_inputs_fieldlist_default = """
	id: ID
	name: String
"""

create_inputs_template = """
input __TEMPLATE_TABLENAME_CASE__CreateInput {
__TYPEDEFS_CREATEFIELDLIST__
}
input __TEMPLATE_TABLENAME_CASE__UpdateInput {
__TYPEDEFS_UPDATEFIELDLIST__
}
"""

def create_inputs(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()

		per_table = create_inputs_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		# harusnya oprek tiap field...
		per_table = per_table.replace('__TYPEDEFS_CREATEFIELDLIST__', create_inputs_fieldlist_default.strip())
		per_table = per_table.replace('__TYPEDEFS_UPDATEFIELDLIST__', create_inputs_fieldlist_default.strip())
		result.append(per_table)

	return '\n'.join(result)
