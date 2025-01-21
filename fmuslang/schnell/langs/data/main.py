import sys
# python data.py gen data 1 User username:s(100) email:s:e password:s:p
# python data.py gen model User username:s(100) email:s password:s
# python data.py gen data 5 User born:d:b
# python data.py gen ru_RU:data 5 User angka:s:t
# python data.py gen ru_RU,ja_JP:data 5 User angka:s:t <- ini belum jalan krn Faker gak terima ru_RU,it_IT dst
# python data.py gen model User kunci:b:rahasia
from language import process_language
from generator import generate
from gensql import generate_sql
from genjson import generate_json
from genxml import generate_xml
from gensequelize import (
	generate_sequelize,
	generate_seeds,
	generate_bulkinsert,
)
from sequelize import (
	sequelize_init,
	exec_cmd_under_projectdir,
	sequelize_generate_seed,
	delete_seeders,
	SEQUELIZE,
)


def main(args):
	print("program:", args)
	generated_tree = process_language(args)
	conf, table, coltypes, colnames = generate(generated_tree)
	print('--------- generate sql')
	records = generate_sql(conf, table, coltypes, colnames)

	input('Generate json... ')
	stringtemplate = generate_json(table, records)
	print(stringtemplate)

	input('Generate xml... ')
	stringtemplate = generate_xml(table, records)
	print(stringtemplate)

	sequelize_model_generate, list_of_pairs = generate_sequelize(table, coltypes, colnames)
	seed_records = generate_seeds(conf, coltypes, colnames)
	print('<<--------- generate seeds')
	# print(seed_records)
	print('>>--------- generate seeds')

	sequelize_init()
	# tablename +s agar sama dg migrations dan seeders
	exec_cmd_under_projectdir([SEQUELIZE, 'model:generate', '--force', '--name', table+'s', '--attributes', list_of_pairs])
	sequelize_generate_seed(table)
	delete_seeders() # stlh generate, hapus file seeder krn mau gunakan versi kita

	generate_bulkinsert(table, seed_records)

# python main.py "data 1 User username:s(100) name:s email:s(100):e password:s:p"
# python main.py "data 10 User username:s(100):fn name:s:ln email:s(100):e password:s:p mypass:b:<rahasia> nilai:i:ri(1,100)"
# mypass:b:rahasia
# bilangan:ri(1,100)
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("program arg1")
		sys.exit(0)
	# stringi = ' '.join(sys.argv[1:])
	main(sys.argv[1])
