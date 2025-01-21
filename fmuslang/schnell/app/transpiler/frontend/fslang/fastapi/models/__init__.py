from app.fileutils import file_content, append_entry_tostring
from app.treeutils import get_tables
from app.usutils import (
	gen_template_db_init,
	gen_template_app_init,
	generate_app_content,
	write_mkfile,
	append_entry,
	tab,
)
from app.libpohon.columnify import (
	columnify_and_transform,
	transform_columns,
	columnify,
)
from app.dirutils import here, joiner
from .model_mapper import (
	graphene_mapper,
	sqlalchemy_column_mapper,
	pydantic_basemodel_mapper,
	pydantic_basemodel_mapper_optional,
)

disini = here(__file__)
tpl_appgraphql = joiner(disini, '../templates/fastapi_app_schema_v1.tpl')
tpl_appcontroller = joiner(disini, '../templates/fastapi_app_rest_crud_v1.tpl')
tpl_appindex = joiner(disini, '../templates/fastapi_app_rest_index_v1.tpl')
tpl_appmodel = joiner(disini, '../templates/fastapi_app_rest_models_v1.tpl')
tpl_appservice = joiner(disini, '../templates/fastapi_app_rest_routes_v1.tpl')
tpl_appcontent = joiner(disini, '../templates/fastapi_app_content_v1.tpl')


# /node-apollo-template/apps/__TEMPLATE_modelname/index.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.service.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.model.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.controller.js
# /node-apollo-template/apps/__TEMPLATE_modelname/__TEMPLATE_modelname.graphql.js

# /myfastapi/apps/$$GANTI_DENGAN_MODEL_LOWER$$/__init__.py
# /myfastapi/apps/$$GANTI_DENGAN_MODEL_LOWER$$/routes.py
# /myfastapi/apps/$$GANTI_DENGAN_MODEL_LOWER$$/crud.py
# /myfastapi/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models.py
# /myfastapi/apps/$$GANTI_DENGAN_MODEL_LOWER$$/schema.py

def generate_app_index(tables, mkfile_input_content):
	"""
	app/__init__.py
	ini kosong
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appindex)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)    

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myfastapi/apps/{tablename_lower}/__init__.py'
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content

def generate_app_route(tables, mkfile_input_content):
	"""
	app/routes.py
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appservice)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myfastapi/apps/{tablename_lower}/routes.py'
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content

def generate_app_crud(tables, mkfile_input_content):
	"""
	app/crud.py
	isinya gak banyak,
	cuma inheritance ke classes di app/models.py
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		per_table = file_content(tpl_appcontroller)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myfastapi/apps/{tablename_lower}/crud.py'
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content

def generate_app_model(tables, mkfile_input_content):
	"""
	app/models.py
	ini adlh workhorse
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model
		__TEMPLATE_MODEL_SQLAL_FIELDS__ = ''
		__TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__ = ''
		__TEMPLATE_BASEMODEL_FIELDS__ = ''

		__TEMPLATE_MODEL_SQLAL_FIELDS__cols = []
		__TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__cols = []
		__TEMPLATE_BASEMODEL_FIELDS__cols = []


		for colidx, column in enumerate(tbl.children):
			tipe_kolom = column.type
			tipe_kolom_sqlalchemy = sqlalchemy_column_mapper.get(tipe_kolom, tipe_kolom)
			nama_kolom = column.label
			column_name_spec = 'Column'
			column_spec = tipe_kolom_sqlalchemy
			constraint_spec = []
			skip_schema_creation = False

			if hasattr(column, 'primaryKey'):
				constraint_spec.append(f'primary_key={column.primaryKey}')
				skip_schema_creation = True
			if hasattr(column, 'unique'):
				constraint_spec.append(f'unique={column.unique}')
			if hasattr(column, 'db_index'):
				constraint_spec.append(f'index={column.db_index}')
			if hasattr(column, 'allowNull'):
				constraint_spec.append(f'nullable={column.allowNull}')
			if hasattr(column, 'defaultValue'):
				constraint_spec.append(f'default={column.defaultValue}')
			if tipe_kolom_sqlalchemy == 'django_foreign_key' and hasattr(column, 'relTo'):
				# ForeignKey("user.id")
				constraint_spec.append(f'ForeignKey("{column.relTo}")')
				column_spec = 'Integer' # foreign key jadi integer
				skip_schema_creation = True
			if tipe_kolom_sqlalchemy == 'django_one_to_many' and hasattr(column, 'relTo') and hasattr(column, 'related_name'):
				# owner = relationship("User", back_populates="items")
				# foreignKeyOnDelete='models.CASCADE', oneToMany=True, relTo='User', related_name='"items"'
				column_name_spec = 'relationship'
				column_spec = f'"{column.relTo}"' # bukan lagi String, Boolean dsb, tapi User dst
				constraint_spec.append(f'back_populates={column.related_name}') # sudah mengandung double quote
				skip_schema_creation = True
			
			constraint_spec_stringified = ''
			if constraint_spec:
				constraint_spec_stringified = ', ' + ', '.join(constraint_spec)
			kolom = f"{nama_kolom} = {column_name_spec}({column_spec}{constraint_spec_stringified})"

			__TEMPLATE_MODEL_SQLAL_FIELDS__cols.append(kolom)
			if not skip_schema_creation == True:
				__TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__cols.append(f"{nama_kolom}: {pydantic_basemodel_mapper_optional.get(tipe_kolom,tipe_kolom)}")
				__TEMPLATE_BASEMODEL_FIELDS__cols.append(f"{nama_kolom}: {pydantic_basemodel_mapper.get(tipe_kolom,tipe_kolom)}")

		__TEMPLATE_MODEL_SQLAL_FIELDS__ = '\n'.join([tab(1)+item for item in __TEMPLATE_MODEL_SQLAL_FIELDS__cols])
		__TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__ = '\n'.join([tab(1)+item for item in __TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__cols])
		__TEMPLATE_BASEMODEL_FIELDS__ = '\n'.join([tab(1)+item for item in __TEMPLATE_BASEMODEL_FIELDS__cols])

		per_table = file_content(tpl_appmodel)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE_MODEL_SQLAL_FIELDS__', __TEMPLATE_MODEL_SQLAL_FIELDS__)
		per_table = per_table.replace('__TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__', __TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__)
		per_table = per_table.replace('__TEMPLATE_BASEMODEL_FIELDS__', __TEMPLATE_BASEMODEL_FIELDS__)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myfastapi/apps/{tablename_lower}/models.py'
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content

def generate_app_graphql(tables, mkfile_input_content):
	"""
	__TAB(3)schema.py,f(e=utama=/myfastapi/apps/$$GANTI_DENGAN_MODEL_LOWER$$/schema.py)

	__TEMPLATE2_CREATE_ARGUMENTS__
		# name = graphene.String()
		# price = graphene.Float()
	"""
	for index, tbl in enumerate(tables,1):
		tablename_lower = tbl.model.lower()
		tablename_case = tbl.model

		__TEMPLATE2_CREATE_ARGUMENTS__ = ''
		__TEMPLATE_COMMA_MUTATE_FIELDS__ = '' # , name, price
		__TEMPLATE_MUTATE_ASSIGNS__ = '' # name=name, price=price
		__TEMPLATE_UPDATE_NONE__ = '' # , name=None, price=None
		__TEMPLATE_UPDATE_OR__ = '' # name or price
		__TEMPLATE_IF3_ASSIGN4__ = '' # 3if name: db_lower.name = name

		__TEMPLATE2_CREATE_ARGUMENTS__cols = []
		__TEMPLATE_COMMA_MUTATE_FIELDS__cols = []
		__TEMPLATE_MUTATE_ASSIGNS__cols = []
		__TEMPLATE_UPDATE_NONE__cols = []
		__TEMPLATE_UPDATE_OR__cols = []
		__TEMPLATE_IF3_ASSIGN4__cols = []

		for colidx, column in enumerate(tbl.children):
			skip_schema_creation = False
			tipe_kolom = graphene_mapper.get(column.type, column.type)

			if tipe_kolom == 'django_foreign_key' and hasattr(column, 'relTo'):
				skip_schema_creation = True
			if tipe_kolom == 'django_one_to_many' and hasattr(column, 'relTo') and hasattr(column, 'related_name'):
				skip_schema_creation = True

			kolom = tab(2) + f"{column.label} = {tipe_kolom}"
			if not skip_schema_creation:
				__TEMPLATE2_CREATE_ARGUMENTS__cols.append(kolom)
				__TEMPLATE_COMMA_MUTATE_FIELDS__cols.append(column.label)
				__TEMPLATE_MUTATE_ASSIGNS__cols.append(f"{column.label}={column.label}")
				__TEMPLATE_UPDATE_NONE__cols.append(f"{column.label}=None")
				__TEMPLATE_UPDATE_OR__cols.append(column.label)
				__TEMPLATE_IF3_ASSIGN4__cols.append(f"{tab(3)}if {column.label}:\n{tab(4)}db_{tablename_lower}.{column.label} = {column.label}")

		__TEMPLATE2_CREATE_ARGUMENTS__ = '\n'.join([item+tab(2) for item in __TEMPLATE2_CREATE_ARGUMENTS__cols])

		if __TEMPLATE_COMMA_MUTATE_FIELDS__cols:
			__TEMPLATE_COMMA_MUTATE_FIELDS__ = ', ' + ', '.join(__TEMPLATE_COMMA_MUTATE_FIELDS__cols)
		if __TEMPLATE_UPDATE_NONE__cols:
			# def mutate(parent, info, , title=None, description=None, done=None):
			# __TEMPLATE_UPDATE_NONE__ = ', ' + ', '.join(__TEMPLATE_UPDATE_NONE__cols)
			__TEMPLATE_UPDATE_NONE__ = ', '.join(__TEMPLATE_UPDATE_NONE__cols)

		__TEMPLATE_MUTATE_ASSIGNS__ = ', '.join(__TEMPLATE_MUTATE_ASSIGNS__cols)
		__TEMPLATE_UPDATE_OR__ = ' or '.join(__TEMPLATE_UPDATE_OR__cols)
		__TEMPLATE_IF3_ASSIGN4__ = '\n'.join(__TEMPLATE_IF3_ASSIGN4__cols)

		per_table = file_content(tpl_appgraphql)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_LOWER__', tablename_lower)
		per_table = per_table.replace('__TEMPLATE_TABLENAME_CASE__', tablename_case)
		per_table = per_table.replace('__TEMPLATE2_CREATE_ARGUMENTS__', __TEMPLATE2_CREATE_ARGUMENTS__)
		per_table = per_table.replace('__TEMPLATE_COMMA_MUTATE_FIELDS__', __TEMPLATE_COMMA_MUTATE_FIELDS__)
		per_table = per_table.replace('__TEMPLATE_MUTATE_ASSIGNS__', __TEMPLATE_MUTATE_ASSIGNS__)
		per_table = per_table.replace('__TEMPLATE_UPDATE_NONE__', __TEMPLATE_UPDATE_NONE__)
		per_table = per_table.replace('__TEMPLATE_UPDATE_OR__', __TEMPLATE_UPDATE_OR__)
		per_table = per_table.replace('__TEMPLATE_IF3_ASSIGN4__', __TEMPLATE_IF3_ASSIGN4__)

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/myfastapi/apps/{tablename_lower}/schema.py'
		mkfile_input_content = append_entry_tostring(mkfile_input_content, header, per_table)
	return mkfile_input_content

def gen_models(tables, mkfile_input_content):
	mkfile_input_content = generate_app_index(tables, mkfile_input_content)
	mkfile_input_content = generate_app_route(tables, mkfile_input_content)
	mkfile_input_content = generate_app_crud(tables, mkfile_input_content)
	mkfile_input_content = generate_app_model(tables, mkfile_input_content)
	mkfile_input_content = generate_app_graphql(tables, mkfile_input_content)

	return mkfile_input_content
