from schnell.app.autoutils import confirm
# confirm('faker import #0 sblm palsu=faker_instance...')
from schnell.langs.data.fakesey import palsu as faker_instance

# from schnell.app.utils import (
# 	env_int,
# )
# confirm('faker import #1 sblm common')
# from .bantu_json import gen_djangojsondata
from .common import (
	Record,
	records_jsonify,
	records_jsonify_simple,
	records_csv,
	django_relationship_fields,
	langsung_panggil_method,
	ubah_method_dan_panggil,
)
# confirm('faker import #2 sblm utils')
from .utils import (
	get_tables_from_rootnode,
	# process_each_table_from_rootnode,
)
# confirm('faker import #3 sblm generatefaker')
from .generate_faker import generate_faker
# confirm('faker import #4, END import faker')


def bantu_faker(RootNode, output_type='json'):
	"""
	UPDATE:
	berbagai jenis faker
	faker json dg results
	faker json [{} {} {}]
	faker csv
	"""
	# process_each_table_from_rootnode(RootNode, callback_processor)

	# ini jadinya bbrp table bergabung dlm 1 file dipisah table_data_separator
	table_data_separator = '\n' + '='*40 + '\n'
	faker_per_table = []
	tables = get_tables_from_rootnode(RootNode)

	for index, tbl in enumerate(tables, 1):
		if hasattr(tbl, 'faker'):
			records = []
			for angka in range(tbl.faker):
				kwargs = generate_faker(table=tbl)
				records.append(Record(**kwargs))

			# django migration data
			# table_data = gen_djangojsondata(tbl.model, records)
			# normal json
			# table_data = str(records)
			# json dg header {results:{}}
			if output_type == 'json':
				table_data = records_jsonify(records, 'results')
				if table_data:
					faker_per_table . append(table_data)
			elif output_type == 'json_simple':
				table_data = records_jsonify_simple(records)
				if table_data:
					faker_per_table . append(table_data)
			elif output_type == 'csv':
				csv_data = records_csv(records)
				if csv_data:
					faker_per_table . append(csv_data)

	return table_data_separator.join(faker_per_table)
