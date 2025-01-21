create_mutationtypes_template = """
create__TEMPLATE_TABLENAME_CASE__(__TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__CreateInput): __TEMPLATE_TABLENAME_CASE__
update__TEMPLATE_TABLENAME_CASE__(id: ID, __TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__UpdateInput): __TEMPLATE_TABLENAME_CASE__
delete__TEMPLATE_TABLENAME_CASE__(id: ID): String
"""


def create_mutationtypes(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()
		per_table = create_mutationtypes_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		result.append(per_table)

	return '\n'.join(result)
