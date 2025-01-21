
create_querytypes_template = """
all__TEMPLATE_TABLENAME_CASE__s: [__TEMPLATE_TABLENAME_CASE__]
find__TEMPLATE_TABLENAME_CASE__ById(id: ID): __TEMPLATE_TABLENAME_CASE__
"""


def create_querytypes(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()
		per_table = create_querytypes_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		result.append(per_table)

	return '\n'.join(result)
