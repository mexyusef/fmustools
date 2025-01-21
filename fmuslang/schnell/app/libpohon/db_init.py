from schnell.app.stringutils import tabify_contentlist_tab, tabify_contentlist_space
from schnell.app.usutils import tab
from schnell.app.utils import env_int


def db_init(RootNode, self_tab_mode='space2'):
	# dbvalues = {}
	dblines = []
	dbinfo = RootNode

	if hasattr(dbinfo, 'username'):
		dblines.append(f"%__TEMPLATE_DBUSER={dbinfo.username}")

	if hasattr(dbinfo, 'password'):
		dblines.append(f"%__TEMPLATE_DBPASS={dbinfo.password}")

	if hasattr(dbinfo, 'host'):
		dblines.append(f"%__TEMPLATE_DBHOST={dbinfo.host}")
		
	if hasattr(dbinfo, 'port'):
		dblines.append(f"%__TEMPLATE_DBPORT={dbinfo.port}")

	if hasattr(dbinfo, 'dbname'):
		dblines.append(f"%__TEMPLATE_DBNAME={dbinfo.dbname}")

	if hasattr(dbinfo, 'dbtype'):
		dblines.append(f"%__TEMPLATE_DBTYPE={dbinfo.dbtype}")

	# %__TEMPLATE_DBUSER=usef
	# %__TEMPLATE_DBPASS=rahasia
	# %__TEMPLATE_DBHOST=gisel.ddns.net
	# %__TEMPLATE_DBPORT=9022
	# %__TEMPLATE_DBNAME=ecomm
	# template_db_init = '\n'.join([tab(1)+item for item in dblines])
	if self_tab_mode == 'tab':
		template_db_init = tabify_contentlist_tab(dblines, num_tab=1)
	elif self_tab_mode == 'space2':
		template_db_init = tabify_contentlist_space(dblines, num_tab=1, space_size=2)
	elif self_tab_mode == 'space4':
		template_db_init = tabify_contentlist_space(dblines, num_tab=1, space_size=4)
	# template_db_init = tabify_contentlist_tab(dblines, num_tab=1)
	if env_int('ULIBPY_FMUS_DEBUG')>1:
		print('='*20, 'dblines')
		print(template_db_init)
	return template_db_init

