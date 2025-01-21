# tab + tinggal kasih filepath
from .app_content_model import app_content_model_tab_by_file
from .app_content import app_content_tab_by_file
from .app_content_model import app_content_model_tab_by_file as acmfile
from .app_content import app_content_tab_by_file as acfile

libpohon_data_default_django_model_import = 'from django.db import models'

def get_import(tablename):
	from schnell.app.utils import salin_objek
	from schnell.app.appconfig import libpohon_data
	try:
		import_part = salin_objek(libpohon_data['import_part_by_table'][tablename])
		return import_part
	except Exception as err:
		return [libpohon_data_default_django_model_import]	

# contoh pake:

# header = f'/apps/{tablename}/models.py'
# per_table = app_content_model_tab(tablename, file_content(joiner(disini, 'app_models.tpl')))
# generated_fields = columnify_and_transform(self.tables, 'django', tablename)
# generated_fields = tabify_content(generated_fields, self_tab=tab_tab(), num_tab=1)
# basemodel = TIMESTAMPED_BASE_MODEL if hasattr(tbl, 'timestamp') else DEFAULT_BASE_MODEL
# import_part = get_import(tablename)
# if hasattr(tbl, 'timestamp'): # {@User=#5,ts}
# 	basemodel =  TIMESTAMPED_BASE_MODEL
# 	import_part.append(TIMESTAMP_IMPORT)
# else:
# 	basemodel =  DEFAULT_BASE_MODEL
# per_table = per_table.replace('__TABLE_FIELDS__', generated_fields)
# per_table = per_table.replace('__FIRST_FIELD__', first_column)
# per_table = per_table.replace('__TABLE_BASEMODEL__', basemodel)
# per_table = per_table.replace('__MODEL_IMPORTS__', '\n'.join(import_part))
