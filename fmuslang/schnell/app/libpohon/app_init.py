from schnell.app.stringutils import tabify_contentlist_tab, tabify_contentlist_space
from schnell.app.usutils import tab
from schnell.app.utils import env_int


def app_init(tables, self_tab_mode='space2'):
	applines = []
	for index, tbl in enumerate(tables,1):
		# AnyNode(name='config', tables={'schemaname': 'public', 'tablename': 'MyTable', 'fakernum': 100}, type='config')
		appidx = str(index).zfill(2)
		# tablename = tbl.tables['tablename']
		tablename = tbl.model
		# perlu utk lower...ini akan jadi nama direktori utk masing2 app
		# %__TEMPLATE_APP01=task
		# %__TEMPLATE_APP02=user
		applines.append(f"%__TEMPLATE_APP{appidx}={tablename.lower()}")

	if self_tab_mode == 'tab':
		template_app_init = tabify_contentlist_tab(applines, num_tab=1)
	elif self_tab_mode == 'space2':
		template_app_init = tabify_contentlist_space(applines, num_tab=1, space_size=2)
	elif self_tab_mode == 'space4':
		template_app_init = tabify_contentlist_space(applines, num_tab=1, space_size=4)
	# template_app_init = '\n'.join([tab(1)+item for item in applines])
	# template_app_init = tabify_contentlist_tab(applines, num_tab=1)
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		print('='*20, 'applines')
		print(template_app_init)
	return template_app_init


def app_init_content(mkfile_input_content, RootNode, tables):
	"""
	2 baris ini sudah gak digunakan lagi
	template_app_init = app_init(tables)
	mkfile_input_content = mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)	
	"""
	template_app_init = app_init(tables)
	mkfile_input_content = mkfile_input_content.replace('__TEMPLATE_APP_INIT', template_app_init)
	mkfile_input_content = mkfile_input_content.replace('__NILAI_SERVER_PORT__', RootNode.serverport)
	mkfile_input_content = mkfile_input_content.replace('__NILAI_CLIENT_PORT__', RootNode.clientport)
	return mkfile_input_content

