
create_typedefs_fieldlist_default = """
	id: ID!
	name: String!
"""

create_typedefs_template = """
type __TEMPLATE_TABLENAME_CASE__ {
__TYPEDEFS_FIELDLIST__
}
"""

def create_typedefs(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()

		per_table = create_typedefs_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		# harusnya oprek tiap field...
		per_table = per_table.replace('__TYPEDEFS_FIELDLIST__', create_typedefs_fieldlist_default.strip())
		result.append(per_table)

	return '\n'.join(result)
