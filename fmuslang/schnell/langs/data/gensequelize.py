from mapper import Types_to_Faker_Mapper
from record import Record
from helper import seeder_filename_template
from fakesey import palsu
from sequelize import (
	create_config_json,
	create_seederfile,
	run_migration,
	run_seed,
)

def sequelize_mapper(record):
	sequelize_types = ['string', 'integer', 'boolean', 'date', 'text']
	# print('sequelize mapper:', record)
	kembali = record
	if ',' in record: # varchar,100
		jenis, jumlah = record.split(',')
		if jenis == 'varchar':
			kembali = 'string' # dont care jumlah
	elif '#' in record: # string#name, kita ambil string discard name
		jenis, subjenis = record.split('#')
		if jenis in sequelize_types:
			kembali = jenis
		elif jenis == 'varchar':
			kembali = 'string'
		elif jenis == 'number':
			kembali = 'integer'
		elif jenis == 'bcrypt':
			kembali = 'string'

	return kembali

def tuple_to_pair_individual(original):
	return original[0] + ":" + original[1]

def tuple_to_pair_list(original_list):
	return list(map(tuple_to_pair_individual, original_list))

# generated_columns masih harus diproses
# sequelize-cli model:generate --name User --attributes username:varchar,100,email:string#email,password:string
# sequelize-cli model:generate --name User --attributes username:varchar,100,email:string#email,password:string#password

def generate_sequelize(tablename, columntypes, columnnames):
	values = list( map( sequelize_mapper, columntypes ) )
	gabung = list( zip( columnnames, values ) )
	list_of_pairs = ','.join(tuple_to_pair_list(gabung))
	# print('hasil mapped utk seq:', values, 'dan (column names,types):', gabung, "siap sequelize'd:", list_of_pairs)
	# sequelize = f'sequelize-cli model:generate --name {tablename} --attributes {",".join(generated_columns)}'

	print('\n\n')
	sequelize = f'model:generate --name {tablename}s --attributes {list_of_pairs}'
	print(sequelize)
	return sequelize, list_of_pairs

def generate_seeds(configuration, columntypes, columnnames):	

	seed_records = []
	print('Jumlah data seeder yang akan digenerate:', configuration['generate:number'])
	total = int(configuration['generate:number'])
	for counter in range(total):
		values = list( map( lambda record: Types_to_Faker_Mapper(palsu, record, configuration), columntypes) )
		print(values)
		strippedquotes_names = [item.replace('"', '') for item in columnnames]
		kwargs = dict(zip(strippedquotes_names, values))
		seed_records.append(Record(**kwargs))

	return seed_records
	# input('Press key to continue [yarn init, yarn add *, sequelize init, sequelize model:generate, sequelize db:seed:all]...')
	# yarn_init()
	# yarn_add_sequelize()
	# # delete_all() # models, migrations, seeders
	# sequelize_init()
	# # tablename +s agar sama dg migrations dan seeders
	# exec_cmd_under_projectdir([SEQUELIZE, 'model:generate', '--force', '--name', tablename+'s', '--attributes', list_of_pairs])
	# sequelize_generate_seed(tablename)
	# delete_seeders() # stlh generate, hapus file seeder krn mau gunakan versi kita

# input("Press key to continue [bulkInsert ke database]")
# generate_bulkinsert(tablename, seed_records)
def generate_bulkinsert(tablename, seed_records):	

	first_row = seed_records[0]
	print('masukkan ini dong sbg bulkinsert:',first_row.__dict__)
	# tambah createdAt dan updatedAt
	for row in seed_records:
		row.__dict__.update({'createdAt': 'new Date()', 'updatedAt': 'new Date()'})

	transformed_records = [item.__dict__ for item in seed_records]
	# db:migrate hasilkan tablename+s, seeder hrs ikutin
	seeder_content = seeder_filename_template \
		.replace('_TABLENAMES', tablename+'s') \
		.replace('__RECORDS', 
			str(transformed_records).replace('{','\n{').replace("'", '').replace(']','\n]')
		)

	print(seeder_content)
	create_config_json()
	create_seederfile(tablename, seeder_content)
	run_migration()
	run_seed()
	print('*** phew...')
