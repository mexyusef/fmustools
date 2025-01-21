import bcrypt, datetime, decimal, json
from jsonify import MyJsonify

def Types_to_Faker_Mapper(faker_instance, record, configuration):
	"""
	proses ini menghasilkan pengapitan dg quote...pd kembali...mungkin tidak diinginkan utk xml, kecuali utk sql statement

	varchar,100 => string(100)
	string => tetap
	"""
	# print('\nTypes_to_Faker_Mapper =>', record, 'dan config:', configuration)

	if ',' in record: # 'varchar,100'
		jenis, jumlah = record.split(',')
		jenis = 'string' if jenis == 'varchar' else jenis # ubah varchar ke string sblm panggil method fakesey
		jumlah = int(jumlah)
		kembali = getattr(faker_instance, f'_{jenis}') (jumlah)

	elif '#' in record: # 'string#email'
		maintype, subclass = record.split('#')

		if maintype == 'bcrypt': # utk bcrypt kita peroleh value dg encode kata pd config plaintext, bukan dari faker
			# print("Bcrypting:", subclass)
			# print("config:", configuration)
			plaintext = configuration['bcrypt_plaintext'].encode('utf8')
			kembali = bcrypt.hashpw(plaintext, bcrypt.gensalt())
			kembali = kembali.decode('utf8')

		elif subclass == 'random_int':

			if 'random_int_max' in configuration:
				min = int ( configuration['random_int_min'] )
				max = int ( configuration['random_int_max'] )
				kembali = getattr(faker_instance, f'generate') (subclass, min, max)

			elif 'random_int_min' in configuration:
				min = int ( configuration['random_int_min'] )
				# max = int ( configuration['random_int_max'] )
				kembali = getattr(faker_instance, f'generate') (subclass, min)

		else:
			kembali = getattr(faker_instance, f'generate') (subclass)
			# print('subclass',subclass, 'dg main:',maintype, 'dan record', record)
			if subclass == 'simple_profile':
				# print('kembali adlh dict', kembali, 'dg keys:', kembali.keys())
				if maintype == 'date': # ini dari d:b
					kembali = kembali['birthdate']
				else: # default kita ambil username = string dari simple_profile => s:u
					kembali = kembali['username'] # kembali.username gak bisa

	else:
		kembali = getattr(faker_instance, f'_{record}') ()

	# print(f'Apakah kita punya kembali = [{kembali}]\n')

	if isinstance(kembali, dict):		
		kembali = json.dumps(kembali, cls=MyJsonify)

	elif isinstance(kembali, list):
		kembali = ', '.join(kembali)

	elif isinstance(kembali, int) or isinstance(kembali, float) or isinstance(kembali, decimal.Decimal):
		kembali = str(kembali)

	elif isinstance(kembali, datetime.datetime) or isinstance(kembali, datetime.date):
		kembali = kembali.isoformat()

	return '"' + kembali + '"'
