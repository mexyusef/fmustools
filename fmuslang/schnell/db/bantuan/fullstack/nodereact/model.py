import json
from .common import (
	filepath_output,
	nodejs_sequelize_model_template,
	sequelize_type_mapper,
	QuoteChar,
	ReplaceQuoteChar,
	react_antd_app_route_template,
	react_antd_app_asset_json,
)
from db.bantuan.common import (
	TAB,
	tab,
)
from .antd_helper import (
	generate_react_component,
	generate_menu_json,
	generate_app_routes,
)
"""TODO
server:
client:
"""
from .common import append_entry

skipped_column_types = [
  'django_foreign_key',
  'django_one_to_one',
  'django_many_to_many',
]


def gen_models_nodejs(configuration):
	"""
	ini sekedar bikin <apps>/app/models/postgres.js
	"""
	
	tables = configuration['table_nodes']
	# ini hanya berisi label+type masing2 kolom, info2 lain gak dimasukkan
	# jadi lebih baik gunakan configuration['table_nodes'].children
	# configuration['table_nodes'] adlh AnyNode table yg berisi .model
	configuration['models'] = {}
	
	for index, tbl in enumerate(tables,1):

		model = {}
		configuration['models'][tbl.model] = []

		for colidx, column in enumerate(tbl.children):
			# tipe_model = sequelize_type_mapper[column.type]
			tipe_model = sequelize_type_mapper.get(column.type, column.type)

			# model[column.label] = tipe_model
			# form['name'] = column.label
			# form['type'] = column.type

			if hasattr(column, 'subtype'):
				tipe_model = tipe_model.replace('__SUBTYPE__', sequelize_type_mapper.get(column.subtype, column.subtype))

			if hasattr(column, 'relTo'):
				relation_model = column.relTo
				tipe_model = tipe_model.replace('ModelRujukan', relation_model)

			if column.type == 'varchar' and hasattr(column, 'typenum'):
				tipe_model += f'({column.typenum})'

			if hasattr(column, 'hasConstraint') and column.hasConstraint == True:
				model[column.label] = { 'type': tipe_model }
			else:
				model[column.label] = tipe_model

			if hasattr(column, 'unique'):
				model[column.label] .update({ 'unique': column.unique })

			if hasattr(column, 'allowNull'):
				model[column.label] .update({ 'allowNull': column.allowNull })

			if hasattr(column, 'references'):
				replacement = column.references.replace(QuoteChar, ReplaceQuoteChar)
				model[column.label] .update({ 'references': replacement })

			if hasattr(column, 'referencesKey'):
				replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
				model[column.label] .update({ 'referencesKey': replacement })

			if hasattr(column, 'primaryKey'):
				model[column.label] .update({ 'primaryKey': column.primaryKey })

			if hasattr(column, 'values'):
				'''
				values dan default menandakan enumvalues dan stringenumvalues
				item di dalamnya diapit QuoteChar $$$
				django perlu ganti $$$ ke empty
				node sequelize perlu ganti $$$ ke "
				'''
				replacement = [item.replace(QuoteChar, ReplaceQuoteChar) for item in column.values]
				model[column.label] .update({ 'values': replacement })

			if hasattr(column, 'default'):
				'''
				values dan default menandakan enumvalues dan stringenumvalues
				item di dalamnya diapit QuoteChar $$$
				django perlu ganti $$$ ke empty
				node sequelize perlu ganti $$$ ke "
				'''
				replacement = column.default.replace(QuoteChar, ReplaceQuoteChar)
				model[column.label] .update({ 'default': replacement })

			if hasattr(column, 'defaultValue'):
				replacement = column.defaultValue.replace(QuoteChar, ReplaceQuoteChar)
				if replacement in ['False', 'True']:
					'''
					konversi ke js
					'''
					replacement = 'false' if replacement == 'False' else 'true'
				model[column.label] .update({ 'defaultValue': replacement })
			
			if column.type not in skipped_column_types:
				configuration['models'][tbl.model].append({
					'name': column.label,
					'type': column.type,
				})

		# ini key dan val jadi ada " sedangkan sequelize fields gak pake quote
		# indent sesuai jumlah TAB
		hasil = json.dumps(model, indent=TAB)
		# kita masukkan ke config (columns) utk digunakan oleh react apps/components
		# sewaktu bikin form
		
		# gak perlu krn ada via tbl.children -> column

		# setiap "STRING", "NUMBER" dll menjadi STRING dan NUMBER
		# kita punya __DQTIMESTAMP__DQ dari pemetaan timestamp
		# stlh omit " kita jg kasih " utk field type yg diapit __DQ
		hasil = hasil.replace(ReplaceQuoteChar, '').replace('__DQ', '"')
		per_table = nodejs_sequelize_model_template
		per_table = per_table.replace('__TABLENAME__', tbl.model)
		per_table = per_table.replace('__TABLENAME_LOWER__', tbl.model.lower())
		per_table = per_table.replace('__TABLENAME_UPPER__', tbl.model.upper())
		per_table = per_table.replace('__TABLENAME_LOWER_PLURAL__', tbl.model.lower() + 's')
		per_table = per_table.replace('__TABLENAME_UPPER_PLURAL__', tbl.model.upper() + 's')
		per_table = per_table.replace('__TABLENAME_CAP_PLURAL__', tbl.model.capitalize() + 's')

		per_table = per_table.replace('__FIELDS__', hasil)
		per_table = per_table.replace('__TAB', tab(1))

		print('*'*40)
		print(per_table)
		print('~'*40)
		header = f'/np/node-postgres/src/apps/{tbl.model.lower()}/models/postgres.js'
		entrify = append_entry(filepath_output,	header, per_table)


def gen_models_reactantd_json(configuration):
	"""
	assets/<model>.json
	digunakan utk konfigurasi table di CRUD/get/list
	"""
	tables = configuration['table_nodes']
	
	for index, tbl in enumerate(tables,1):
		
		# per_table = react_antd_app_route_template
		# per_table = per_table.replace('__TABLENAME__', tbl.model)		
		# per_table = per_table.replace('__TABLENAME_LOWER__', tbl.model.lower())
		# per_table = per_table.replace('__TABLENAME_UPPER__', tbl.model.upper())
		# per_table = per_table.replace('__TABLENAME_LOWER_PLURAL__', tbl.model.lower() + 's')
		# per_table = per_table.replace('__TABLENAME_UPPER_PLURAL__', tbl.model.upper() + 's')
		# per_table = per_table.replace('__TABLENAME_CAP_PLURAL__', tbl.model.capitalize() + 's')
		# per_table = per_table.replace('__FIELDS__', hasil)
		# per_table = per_table.replace('__TAB', tab(1))

		model_low = tbl.model.lower()
		model_cap = tbl.model.capitalize()
		# columns = []
		# for colidx, column in enumerate(tbl.children):
		# 	columns.append(column.label)
		columns = [tab(2)+f'"{col.label}"' for col in tbl.children]
		pengganti = ',\n'.join(columns) + ',\n'
		content = react_antd_app_asset_json.replace('__TEMPLATE_APP_ASSET_JSON', pengganti)
		# review.json,f(e=utama=/np/react-antd/assets/review.json)
		header = f'/np/react-antd/assets/{tbl.model.lower()}.json'
		entrify = append_entry(filepath_output,	header, content)


def gen_models_reactantd_antd(configuration):
	"""
				Task,d(/mk)
					UpdateForm.js,f(e=utama=/np/react-antd/components/modules/Task/UpdateForm.js)
					FormProvider.js,f(e=utama=/np/react-antd/components/modules/Task/FormProvider.js)
					FormWrapper.js,f(e=utama=/np/react-antd/components/modules/Task/FormWrapper.js)
					Modal.js,f(e=utama=/np/react-antd/components/modules/Task/Modal.js)
					Task.js,f(e=utama=/np/react-antd/components/modules/Task/Task.js)
					CreateForm.js,f(e=utama=/np/react-antd/components/modules/Task/CreateForm.js)
					List.js,f(e=utama=/np/react-antd/components/modules/Task/List.js)
	jadi banyak yg dioprek...
	/np/react-antd/components/modules/Task/CreateForm.js
	/np/react-antd/components/modules/Task/FormProvider.js
	/np/react-antd/components/modules/Task/FormWrapper.js
	/np/react-antd/components/modules/Task/List.js
	/np/react-antd/components/modules/Task/Modal.js
	/np/react-antd/components/modules/Task/Task.js
	/np/react-antd/components/modules/Task/UpdateForm.js
	"""

	generate_react_component(configuration)
	# tables = configuration['table_nodes']
	
	# for index, tbl in enumerate(tables,1):
		
	# 	per_table = react_antd_app_mk_template
	# 	per_table = per_table.replace('__TABLENAME__', tbl.model)		
	# 	per_table = per_table.replace('__TABLENAME_LOWER__', tbl.model.lower())
	# 	per_table = per_table.replace('__TABLENAME_UPPER__', tbl.model.upper())
	# 	per_table = per_table.replace('__TABLENAME_LOWER_PLURAL__', tbl.model.lower() + 's')
	# 	per_table = per_table.replace('__TABLENAME_UPPER_PLURAL__', tbl.model.upper() + 's')
	# 	per_table = per_table.replace('__TABLENAME_CAP_PLURAL__', tbl.model.capitalize() + 's')
	# 	per_table = per_table.replace('__FIELDS__', hasil)
	# 	per_table = per_table.replace('__TAB', tab(1))
	# 	# review.json,f(e=utama=/np/react-antd/assets/review.json)
	# 	header = f'/np/react-antd/assets/{tbl.model.lower()}.json'
	# 	entrify = append_entry(filepath_output,	header, per_table)


def gen_models_reactantd(configuration):
	gen_models_reactantd_json(configuration)
	gen_models_reactantd_antd(configuration)


def gen_server_individual(configuration):
	from .nodepg_helper import gen_apps_index
	gen_apps_index(configuration)


# gen_models(configuration)
def gen_models(configuration):
	gen_models_nodejs(configuration)
	gen_models_reactantd(configuration)
	# spesifik di server
	gen_server_individual(configuration)
	# spesifik di antd
	generate_menu_json(configuration)
	generate_app_routes(configuration)
