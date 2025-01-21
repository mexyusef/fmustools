create_rootapp_autowired_template = """
  @Autowired
  private __TEMPLATE_TABLENAME_CASE__Service __TEMPLATE_TABLENAME_LOWER__Service;
"""


def create_rootapp_autowired(tables):
	result = []
	for table in tables:
		tablename_case = table.model
		tablename_lower = table.model.lower()
		per_table = create_rootapp_autowired_template.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		result.append(per_table)

	return '\n'.join(result)

