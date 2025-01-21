import bcrypt, json, random
from jinja2 import Template
from langs.data.fakesey import palsu as faker_instance
from app.printutils import indah3
from db.bantuan.common import (
  get_stringtemplate,
  append_fixture_entry,
	langsung_panggil_method,
	ubah_method_dan_panggil,
)
from db.bantuan.config import output_django_mkfile


def generate_faker(table):
	
	# records = []
	kwargs = {}
	# kembali = ''
	for index, node in enumerate(table.children):
		maintype = node.type
		nama_kolom = node.label # ucsv/process.py:67
		# print('>>> faking instance utk jenis:', maintype, 'utk node:', node)

		if hasattr(node, 'typenum'):
			'''
			var(100) -> typenum = 100
			'''
			print('	>>>0/ bentuk nama,type(100) utk', node)
			# maintype
			jumlah = int(node.typenum)
			maintype = 'string' if maintype == 'varchar' else maintype
			kembali = getattr(faker_instance, f'_{maintype}') (jumlah)

		elif hasattr(node, 'subtype'):

			print('	>>>1/ bentuk nama,type,subtype utk', node)
			
			subclass = node.subtype
			# print('	>> masuk node.subtype')

			if maintype == 'bcrypt':
				plaintext = node.bcrypt_plaintext.encode('utf8')
				kembali = bcrypt.hashpw(plaintext, bcrypt.gensalt())
				kembali = kembali.decode('utf8')

			elif subclass == 'random_int':

				if hasattr(node, 'max') and hasattr(node, 'min'):
					min = int(node.min)
					max = int(node.max)
					kembali = getattr(faker_instance, f'generate') (subclass, min, max)

				elif hasattr(node, 'min'):
					min = int(node.min)
					kembali = getattr(faker_instance, f'generate') (subclass, min)

			else:
				'''
				di sini kita perkenalkan di ucsv/processor:358,374
				StatementNode.subtype = 'enumvalues'
				StatementNode.subtype = 'stringenumvalues'
				dimana node punya "values"
				value dlm values diapit dg $$$ utk bisa amankan double quotes
				'''
				if subclass in ['enumvalues', 'stringenumvalues']:
					# proses enum vals tanpa faker
					kembali = random.choice(node.values)
				else:
					kembali = getattr(faker_instance, f'generate') (subclass)

				if subclass == 'simple_profile':
					if maintype == 'date':
						kembali = kembali['birthdate']
					else: # default kita ambil username = string dari simple_profile => s:u
						kembali = kembali['username'] # kembali.username gak bisa
		else:
			'''
			jk atas adlh bentuk v(100) atau s:p
			ini adlh bentuk s atau i dll
			'''
			# print('	>>>2/ bentuk nama,type utk', node)
			# maintype = 'string' if maintype == 'varchar' else maintype

			# utk relationship kita gak generate faker...
			skipme = maintype in ['django_foreign_key', 'django_one_to_one', 'django_one_to_many', 'django_many_to_many']
			# atau yg gak ada/perlu fakernya
			# skipme = skipme or (maintype in ['image', 'blob', 'auto'])
			skipme = skipme or (maintype in ['blob', 'auto'])
			# ternyata image bisa gunakan url image = string...

			# mapping_ucsv_column_type_2_fakesey_number = maintype
			# if mapping_ucsv_column_type_2_fakesey_number == 'integer':
			# 	mapping_ucsv_column_type_2_fakesey_number = 'random_int'

			if skipme:
				kembali = None
			else:
				'''
				satu per satu konversi dari ucsv column type di grammar.py
				ke field di fakesey
				'''
				if maintype == 'integer':
					kembali = getattr(faker_instance, 'generate') ('random_int', 0)
				
				elif maintype == 'boolean':
					kembali = getattr(faker_instance, 'generate') ('pybool')

				elif maintype == 'image':
					lebar = 600
					tinggi = 400
					if hasattr(node, 'lebar'):
						lebar = int(node.lebar)
					if hasattr(node, 'tinggi'):
						tinggi = int(node.tinggi)
					kembali = getattr(faker_instance, 'generate') ('image_url', width=lebar, height=tinggi)

				elif maintype == 'slug':
					'''
					https://faker.readthedocs.io/en/master/providers/faker.providers.internet.html#faker.providers.internet.Provider.slug
					'''
					kembali = getattr(faker_instance, 'generate') ('slug')

				elif maintype == 'email':
					'''
					https://faker.readthedocs.io/en/master/providers/faker.providers.internet.html#faker.providers.internet.Provider.email
					'''
					kembali = getattr(faker_instance, 'generate') ('email')

				elif maintype == 'timestamp':
					import pytz
					tzinfo = pytz.timezone('Asia/Jakarta')
					kembali = getattr(faker_instance, 'generate') ('date_time_this_year', before_now=True, after_now=False, tzinfo=tzinfo)
					# konversi ke string agar json serializable
					kembali = kembali.isoformat()

				elif maintype == 'decimal':
					'''
					left_digits = max_digits
					right_digits = decimal_places
					'''
					left_digits = int(node.max_digits) - int(node.decimal_places)
					right_digits = int(node.decimal_places)
					kembali = getattr(faker_instance, 'generate') ('pydecimal', left_digits=left_digits, right_digits=right_digits)
					# konversi ke string atau float agar json serializable
					# kembali = str(kembali)
					# str jadi gagal wkt python manage.py loaddata <app>
					kembali = float(kembali)

				elif nama_kolom in langsung_panggil_method:
					'''
					ada country, city dll
					perhatikan jk kita pengen nilai yg berbeda dari yg disediakan faker dll hrs ubah kode di sini
					'''
					kembali = getattr(faker_instance, 'generate') (nama_kolom)

				elif nama_kolom.lower() in ubah_method_dan_panggil.keys():
					'''
					ada postalcode, zipcode, zip
					perhatikan jk kita pengen nilai yg berbeda dari yg disediakan faker dll hrs ubah kode di sini
					'''
					panggil = ubah_method_dan_panggil[nama_kolom.lower()]
					kembali = getattr(faker_instance, 'generate') (panggil)

				elif nama_kolom == 'username':
					kembali = getattr(faker_instance, 'generate') ('simple_profile')['username']

				elif nama_kolom .startswith('crypto'):
					if nama_kolom == 'crypto':
						''' tuple (code, name) '''
						kembali = getattr(faker_instance, 'generate') ('cryptocurrency')
					elif nama_kolom == 'crypto1':
						kembali = getattr(faker_instance, 'generate') ('cryptocurrency_code')
					elif nama_kolom == 'crypto2':
						kembali = getattr(faker_instance, 'generate') ('cryptocurrency_name')

				elif nama_kolom .startswith('warna'):
					'''
					coba cari teknik utk hue dan luminosity
					color(hue='red')
						'monochrome', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', and 'pink'.
					color(luminosity='light')
						'bright', 'dark', 'light', or 'random'.
					color(hue='orange', luminosity='bright')
					'''
					if nama_kolom == 'warna':
						kembali = getattr(faker_instance, 'generate') ('hex_color')
					elif nama_kolom == 'warna1':
						kembali = getattr(faker_instance, 'generate') ('rgb_color')
					elif nama_kolom == 'warna2':
						kembali = getattr(faker_instance, 'generate') ('rgb_css_color')

				elif nama_kolom .startswith('cc_'):
					if nama_kolom == 'cc_1':						
						kembali = getattr(faker_instance, 'generate') ('credit_card_full')
					elif nama_kolom == 'cc_2':
						kembali = getattr(faker_instance, 'generate') ('credit_card_number')
					elif nama_kolom == 'cc_3':
						kembali = getattr(faker_instance, 'generate') ('credit_card_security_code')
					elif nama_kolom == 'cc_4':
						kembali = getattr(faker_instance, 'generate') ('credit_card_expire')

				elif nama_kolom .startswith('file_'):
					if nama_kolom == 'file_1':
						'''
						(category=None, extension=None)
						category: 'audio', 'image', 'office', 'text', and 'video'.
						'''
						kembali = getattr(faker_instance, 'generate') ('file_name')
					elif nama_kolom == 'file_2':
						'''
						category
						'''
						kembali = getattr(faker_instance, 'generate') ('file_extension')

				elif nama_kolom .startswith('addr_'):
					if nama_kolom == 'addr_city':
						kembali = getattr(faker_instance, 'generate') ('city')
					elif nama_kolom == 'addr_country':
						kembali = getattr(faker_instance, 'generate') ('country')
					elif nama_kolom == 'addr_countrycode':
						kembali = getattr(faker_instance, 'generate') ('country_code')
					elif nama_kolom == 'addr_zip':
						kembali = getattr(faker_instance, 'generate') ('postcode')
					elif nama_kolom == 'addr_jalan1': # no + nama
						kembali = getattr(faker_instance, 'generate') ('street_address')
					elif nama_kolom == 'addr_jalan2':
						kembali = getattr(faker_instance, 'generate') ('street_name')

				elif nama_kolom .startswith('geo_'):
					if nama_kolom == 'geo_1':
						kembali = getattr(faker_instance, 'generate') ('latlng')
						kembali = (float(kembali[0]), float(kembali[1]))
					elif nama_kolom == 'geo_2':
						kembali = getattr(faker_instance, 'generate') ('latitude')
						kembali = float(kembali)
					elif nama_kolom == 'geo_3':
						kembali = getattr(faker_instance, 'generate') ('longitude')
						kembali = float(kembali)
					elif nama_kolom == 'geo_4':
						'''
						local_latlng(country_code='US', coords_only=False)
						('40.72371', '-73.95097', 'Greenpoint', 'US', 'America/New_York')
						'''
						kembali = getattr(faker_instance, 'generate') ('local_latlng')
					elif nama_kolom == 'geo_5':
						kembali = getattr(faker_instance, 'generate') ('location_on_land')

				elif nama_kolom == 'password':
					'''
					https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html#faker.providers.misc.Provider.password
					password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
					'''
					panjang=10
					kembali = getattr(faker_instance, 'generate') ('password', length=panjang)

				else:
					'''
					jangan lupa () di akhir utk panggil fungsi
					jk
					AnyNode(allowNull=True, blank=True, hasConstraint=True, label='paymentMethod', max_length='200', type='string')
					ada maxlength maka gunakan...
					'''
					if hasattr(node, 'max_length'):
						maxlen = int(node.max_length)
						kembali = getattr(faker_instance, f'_{maintype}') (maxlen)
					else:
						kembali = getattr(faker_instance, f'_{maintype}') ()

		if kembali is not None: # jangan lupa krn kembali bisa False dari pybool
			# print('kembali berjenis:', type(kembali))
			if isinstance(kembali, list):
				print('list:')
				print(kembali)
				print('maintype:')
				print(maintype)
				input(' ketemu list... ')
			kwargs.update({
				node.label: kembali
			})
		
		# print('adding:', kwargs)
	
	print('>>> record =>', kwargs)
	return kwargs
	# records.append(Record(**kwargs))
	# return records


def gen_jsondata(tablename, records):
	"""
	bikin fixture entry %-- --# dan masukkan ke django.mk
	"""
	
	stringtemplate = get_stringtemplate(tablename, records)	
	template = Template(stringtemplate)
	input_records = str(records)
	try:		
		# indah3(f"records = {input_records}", warna='yellow')
		hasil = template.render(records=records)
		koma = hasil.rfind(',')
		hasil = hasil[:koma] + hasil[koma+1:]
		print('='*40, 'generate JSON')
		jsonify = json.loads(hasil)
		hasil = json.dumps(jsonify, indent=2)
		print(hasil)
		append_fixture_entry(output_django_mkfile, tablename, hasil)
	except Exception as err:
		import traceback
		display_record = input_records if len(records) < 10 else records[:5]
		indah3(f"stringtemplate bermasalah adlh [{stringtemplate}]", warna='white')
		indah3(f"Exception: {err} waktu process records: [{display_record}]", warna='red')		
		indah3(traceback.format_exc(), warna='magenta')
