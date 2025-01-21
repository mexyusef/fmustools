from schnell.app.usutils import tab


def app_model(tables, app_model, table_column_creator_index):
	"""
	table_column_creator_index
	index ke processor dari columnify
	"""
	contentlines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		
		# tablename = tbl.tables['tablename']
		tablename = tbl.model
		tablename_lower = tbl.model.lower()

		content = app_model
		
		# appidx = str(index).zfill(2)
		# content = content.replace('$$GANTI_DENGAN_INDEX$$', appidx)

		# content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
		content = content.replace('__TABLENAME_UPPER__', tablename.upper())
		content = content.replace('__TABLENAME_UPPER', tablename.upper())
		content = content.replace('__TABLENAME_LOWER__', tablename.lower())
		content = content.replace('__TABLENAME_LOWER', tablename.lower())
		content = content.replace('__TABLENAME_PLURAL__', tablename + 's')
		content = content.replace('__TABLENAME_PLURAL', tablename + 's')
		content = content.replace('__TABLENAME_PLURAL_LOWER__', tablename.lower() + 's')
		content = content.replace('__TABLENAME_PLURAL_LOWER', tablename.lower() + 's')
		content = content.replace('__TABLENAME_CASE__', tablename)
		content = content.replace('__TABLENAME_CASE', tablename)
		content = content.replace('__TABLENAME_CAP_PLURAL__', tablename.capitalize() + 's')
		content = content.replace('__TABLENAME_CAP_PLURAL', tablename.capitalize() + 's')
		# replacing __TAB hrs di akhir
		content = content \
			.replace('__TAB(9)', tab(9)) \
			.replace('__TAB(8)', tab(8)) \
			.replace('__TAB(7)', tab(7)) \
			.replace('__TAB(6)', tab(6)) \
			.replace('__TAB(5)', tab(5)) \
			.replace('__TAB(4)', tab(4)) \
			.replace('__TAB(3)', tab(3)) \
			.replace('__TAB(2)', tab(2)) \
			.replace('__TAB(1)', tab(1))
		contentlines.append(content)

	# template_app_model = '\n'.join([tab(2)+item for item in contentlines])
	template_app_model = '\n'.join([item for item in contentlines])
	print('='*20, 'contentlines')
	print(template_app_model)
	return template_app_model

