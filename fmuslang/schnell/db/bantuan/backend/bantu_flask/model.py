from app.fileutils import file_content
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	append_entry,
	tab,
)
# from db.bantuan.common import tab
from .common import (
	filepath_input,
	filepath_output,
	# tpl_appgraphql,
	tpl_approutes,
	tpl_appindex,
	tpl_appmodel,
	tpl_appforms,
	# tpl_apputil,
	tpl_appresource,
	tpl_appcontent,
)
from .field_map import field_map

# /myflask2/project/apps/__TEMPLATE_modelname/index.py
# /myflask2/project/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.service.py
# /myflask2/project/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.model.py
# /myflask2/project/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.controller.py
# /myflask2/project/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.graphql.py

def generate_app_index(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appindex)
		# per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)    

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myflask2/project/apps/{tablename_lower}/__init__.py'
		entrify = append_entry(filepath_output,	header, per_table)


def generate_app_routes(tables):
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_approutes)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myflask2/project/apps/{tablename_lower}/routes.py'
		entrify = append_entry(filepath_output,	header, per_table)


def generate_app_model(tables):
	"""
	ada cek jk gak ada column id maka tambahkan manual
	__TEMPLATE_COLUMNS__
	__TEMPLATE_CHOOSE_COLUMN_REPR__
	__TEMPLATE_TODICT__
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		model = {}
		for colidx, column in enumerate(tbl.children):
			tipe_kolom = column.type
			nama_kolom = column.label
			terpetakan = field_map.get(tipe_kolom, tipe_kolom)
			model[nama_kolom] = f"db.Column(db.{terpetakan}__CONSTRAINTS_HOLDER__)"
			col_attrs = []
			if hasattr(column, 'relTo'):
				relation_model = column.relTo
				col_attrs.append(relation_model)
			if hasattr(column, 'allowNull'):
				col_attrs.append(f'nullable={column.allowNull}')
			if hasattr(column, 'defaultValue'):
				col_attrs.append(f'default="{column.defaultValue}"')
			if hasattr(column, 'db_index'):
				col_attrs.append(f'index={column.db_index}')
			if hasattr(column, 'max_length'):
				nilai = column.max_length
				pengganti = f'({nilai})__CONSTRAINTS_HOLDER__'
				model[nama_kolom] = model[nama_kolom].replace('__CONSTRAINTS_HOLDER__', pengganti)
			if hasattr(column, 'primaryKey'):
				col_attrs.append(f'primary_key={column.primaryKey}')
			if hasattr(column, 'unique'):
				col_attrs.append(f'unique={column.unique}')

			if col_attrs:
				comma_separated_attrs = ', '.join(col_attrs)
				model[nama_kolom] = model[nama_kolom].replace('__CONSTRAINTS_HOLDER__', ', ' + comma_separated_attrs)

		# kasih id jk gak ada
		id_exists = any([col for col in tbl.children if col.label=='id' or col.label=='_id'])
		if not id_exists:
			model['id'] = 'db.Column(db.Integer, primary_key=True)'

		formatted = []
		for k,v in model.items():
			field = f"{k.ljust(15)} = {v}"
			formatted.append(field)
		model_fields = '\n'.join([tab()+item for item in formatted])
		first_column = tbl.children[0].label

		column_list_non_id1 = [column.label for column in tbl.children]
		column_list_non_id2 = [f"'{item}': self.{item}" for item in column_list_non_id1]
		__TEMPLATE_TODICT__ = '\n'.join([tab()+item for item in column_list_non_id2])
		__TEMPLATE_TOJSON__ = '\n'.join([tab()+item for item in column_list_non_id2])
		__COLUMN_LIST__ = ', '.join([f'"{column.label}"' for column in tbl.children])

		per_table = file_content(tpl_appmodel)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)		
		per_table = per_table.replace('__TEMPLATE_COLUMNS__', model_fields)
		per_table = per_table.replace('__TEMPLATE_CHOOSE_COLUMN_REPR__', first_column)
		per_table = per_table.replace('__TEMPLATE_TODICT__', __TEMPLATE_TODICT__)
		per_table = per_table.replace('__TEMPLATE_TOJSON__', __TEMPLATE_TOJSON__)
		per_table = per_table.replace('__COLUMN_LIST__', __COLUMN_LIST__)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myflask2/project/apps/{tablename_lower}/models.py'
		entrify = append_entry(filepath_output,	header, per_table)


def generate_app_forms_resource(tables):
	"""
	sementara utk flask service berarti fur = forms, util, resource
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table_forms = file_content(tpl_appforms)
		per_table_forms = per_table_forms.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table_forms = per_table_forms.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		column_list_non_id1 = [column.label for column in tbl.children]
		# username = TextField('Username', id='username_login', validators=[DataRequired()])
		column_list_non_id2 = [f"{item.lower()} = TextField('{item.title()}', id='{item.lower()}_field', validators=[DataRequired()])" for item in column_list_non_id1]
		column_list_non_id3 = '\n'.join([tab(1)+item for item in column_list_non_id2])
		per_table_forms = per_table_forms.replace('__TEMPLATE_COLUMN_LIST', column_list_non_id3)

		# per_table_util = file_content(tpl_apputil)
		# per_table_util = per_table_util.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		# per_table_util = per_table_util.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		per_table_resource = file_content(tpl_appresource)
		per_table_resource = per_table_resource.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table_resource = per_table_resource.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table_forms)
		# print('-'*20)
		# print(per_table_util)
		print('-'*20)
		print(per_table_resource)
		print('~'*40)
		
		header_form = f'/myflask2/project/apps/{tablename_lower}/forms.py'
		entrify = append_entry(filepath_output,	header_form, per_table_forms)
		
		# header_util = f'/myflask2/project/apps/{tablename_lower}/util.py'
		# entrify = append_entry(filepath_output,	header_util, per_table_util)
		
		header_resource = f'/myflask2/project/apps/{tablename_lower}/resource.py'
		entrify = append_entry(filepath_output,	header_resource, per_table_resource)

# def generate_app_graphql(tables):
# 	for index, tbl in enumerate(tables,1):
# 		tablename_lower = tbl.model.lower()
# 		tablename_case = tbl.model

# 		per_table = file_content(tpl_appgraphql)
# 		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
# 		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

# 		print('*'*40)
# 		print(per_table)
# 		print('~'*40)
# 		header = f'/myflask2/project/apps/{tablename_lower}/{tablename_lower}.graphql.py'
# 		entrify = append_entry(filepath_output,	header, per_table)

def gen_models(tables):
	generate_app_index(tables)
	generate_app_routes(tables)
	generate_app_model(tables)
	generate_app_forms_resource(tables)
	# generate_app_graphql(tables)
