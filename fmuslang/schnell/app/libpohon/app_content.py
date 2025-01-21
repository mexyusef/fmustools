# from schnell.app.usutils import tab_tab, tab_space
from schnell.app.stringutils import tab_space4, tab_tab, tab_space2
from schnell.app.utils import env_int
from .helper import detect_replace_assignment


def app_content(tables, app_content_argument, tab=tab_space4, provider='django'):
	"""	
	app.libpohon.app_content_model.app_content
		- memproses 1 table
		- from schnell.app.libpohon.app_content_model import app_content
	app.libpohon.app_content.app_content (this file)
		- memproses many tables
		- from schnell.app.libpohon.app_content import app_content
	"""
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		print(f'''libpohon/app_content.py/app_content
		args:
		tables = {tables}
		app_content_argument = {app_content_argument}
		''')

	contentlines = []

	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')				
		tablename = tbl.model

		content = app_content_argument

		# content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.capitalize())
		content = content.replace('__TABLENAME_UPPER__', tablename.upper())
		content = content.replace('__TABLENAME_LOWER__', tablename.lower())
		content = content.replace('__TABLENAME_PLURAL__', tablename + 's')
		content = content.replace('__TABLENAME_PLURAL_LOWER__', tablename.lower() + 's')
		content = content.replace('__TABLENAME_CASE__', tablename)
		content = content.replace('__TABLENAME_CAP_PLURAL__', tablename.capitalize() + 's')

		# legacy
		# content = content.replace('__TABLENAME_UPPER', tablename.upper())			
		# content = content.replace('__TABLENAME_PLURAL', tablename + 's')
		# content = content.replace('__TABLENAME_PLURAL_LOWER', tablename.lower() + 's')
		content = content.replace('__TEMPLATE_TABLENAME_LOWER__', tablename.lower())
		content = content.replace('__TEMPLATE_TABLENAME_CASE__', tablename)

		content = content.replace('$$GANTI_DENGAN_MODEL_UPPER$$', tablename.upper())
		content = content.replace('$$GANTI_DENGAN_MODEL_TITLE$$', tablename)
		content = content.replace('$$GANTI_DENGAN_MODEL_LOWER$$', tablename.lower())
		content = content.replace('$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$', tablename + 's')
		content = content.replace('$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$', tablename.lower() + 's')

		# tambah utk legacy
		appidx = str(index).zfill(2)
		content = content.replace('__TABLENAME__', tablename)
		content = content.replace('__APPIDX__', appidx)
		# replace TAB hrs terakhir utk hindari __TAB-LENAME__ etc dimakan
		content = content \
			.replace('__TAB(9)', tab*9) \
			.replace('__TAB(8)', tab*8) \
			.replace('__TAB(7)', tab*7) \
			.replace('__TAB(6)', tab*6) \
			.replace('__TAB(5)', tab*5) \
			.replace('__TAB(4)', tab*4) \
			.replace('__TAB(3)', tab*3) \
			.replace('__TAB(2)', tab*2) \
			.replace('__TAB(1)', tab*1)
		
		# UPDATE:
		# bisa modify kebutuhan column (parameter list, dsb) menggunakan konvensi di app.treeutils
		content = detect_replace_assignment(content, tbl, pemetaan=provider)
		if env_int('ULIBPY_FMUS_DEBUG')>1:
			print(f'	* app_content selesai satu table/model => {content}')
		contentlines.append(content)

	# template_app_content = '\n'.join([tab(2)+item for item in contentlines])
	template_app_content = '\n'.join([item for item in contentlines])
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		print('='*20, 'contentlines')
		print(template_app_content)
	return template_app_content


def app_content_tab(tables, app_content_argument, provider='django'):
	return app_content(tables, app_content_argument, tab=tab_tab, provider=provider)


def app_content_space(tables, app_content_argument, provider='django'):
	return app_content(tables, app_content_argument, tab=tab_space4, provider=provider)


def app_content_tab_by_file(tables, disini, filepath, provider='django'):
	"""
	disini = ayah(__file__,1)
	"""
	from schnell.app.dirutils import joiner
	from schnell.app.fileutils import file_content
	app_content_argument = file_content(joiner(disini, filepath))
	return app_content_tab(tables, app_content_argument, provider=provider)


def app_content_tab_by_file_simpler(tables, filepath, provider='django'):
	"""
	asumsikan:
	filepath = joinhere(__file__, 'path/to/filepath')
	"""
	# from schnell.app.dirutils import joiner
	from schnell.app.fileutils import file_content
	app_content_argument = file_content(filepath)
	return app_content_tab(tables, app_content_argument, provider=provider)
