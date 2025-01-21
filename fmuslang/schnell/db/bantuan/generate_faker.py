import bcrypt, pytz, random

from schnell.langs.data.fakesey import palsu as faker_instance

from .auto_increment import AutoIncrement
from .common import (
	Record,
	records_jsonify,
	django_relationship_fields,
	langsung_panggil_method,
	ubah_method_dan_panggil,
)

# ini satu sesi satu incremental jadinya...
auto_increment = AutoIncrement(0)
def generate_faker(table, generate_object_instance = {}, init_counter=None):
	"""
	kita bisa generate 
	{
		field1: value1,
		field2: value2,
	}
	atau:
	new Object(value1, value2, value3),
	new Object(value1, value2, value3),
	"""

	kwargs = {}
	if init_counter is not None:
		auto_increment.init(init_counter)

	for _, node in enumerate(table.children):
		maintype = node.type
		nama_kolom = node.label # ucsv/process.py:67
		# print('>>> faking instance utk jenis:', maintype, 'utk node:', node)

		if hasattr(node, 'typenum'):
			'''
			var(100) -> typenum = 100
			'''
			print('	>>>0/ bentuk [nama,type(100)] utk', node)
			# maintype
			jumlah = int(node.typenum)
			maintype = 'string' if maintype == 'varchar' else maintype
			kembali = getattr(faker_instance, f'_{maintype}') (jumlah)

		elif hasattr(node, 'subtype'):
			'''
			bentuk password,s,p
			p adlh subtype di lang.ucsv.grammar.subclass_string
			'''
			print('	>>>1/ bentuk [nama,type:subtype] utk', node)
			
			subclass = node.subtype
			# print('	>> masuk node.subtype')

			if maintype == 'string' and subclass == 'bcrypt':
				plaintext = node.bcrypt_plaintext.encode('utf8')
				kembali = bcrypt.hashpw(plaintext, bcrypt.gensalt())
				kembali = kembali.decode('utf8')

			elif maintype == 'array_of':
				'''
				AnyNode(hasConstraint=False, label='authors', subtype='string', type='array_of')
				'''
				from app.utils import acak
				kocak = acak(1,10)

				if 'author' in node.label or 'name' in node.label:
					kembali = [f"{getattr(faker_instance, f'generate') ('name')}" for _ in range(kocak)]
				elif node.subtype == 'string':
					kembali = [f"{getattr(faker_instance, f'generate') ('word')}" for _ in range(kocak)]
				elif node.subtype == 'integer':
					kembali = [f"{getattr(faker_instance, f'generate') ('pyint')}" for _ in range(kocak)]
				else:
					kembali = [f"{getattr(faker_instance, f'generate') ('word')}" for _ in range(kocak)]

			elif subclass == 'random_int':
				'''
				attr diberikan oleh
				langs.ucsv.processor
				'''
				if hasattr(node, 'max') and hasattr(node, 'min'):
					min = int(node.min)
					max = int(node.max)
					kembali = getattr(faker_instance, f'generate') (subclass, min, max)

				elif hasattr(node, 'min'):
					min = int(node.min)
					kembali = getattr(faker_instance, f'generate') (subclass, min)

				else:
					kembali = getattr(faker_instance, f'generate') (subclass)

			elif subclass == 'pyfloat':
				'''
				attr diberikan oleh
				langs.ucsv.processor
				'''
				if hasattr(node, 'right') and hasattr(node, 'left'):
					kembali = getattr(faker_instance, f'generate') (subclass, positive=True, right_digits=node.right, left_digits=node.left)

				elif hasattr(node, 'right'):
					kembali = getattr(faker_instance, f'generate') (subclass, positive=True, right_digits=node.right)

				else:
					kembali = getattr(faker_instance, f'generate') (subclass)

			elif subclass == 'random_number':

				if hasattr(node, 'digits'):
					kembali = getattr(faker_instance, f'generate') (subclass, digits=node.digits, fix_len=True)

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
			utk: username,s
			(hanya maintype, no subtype dan no typenum spt v(100))
			jk atas adlh bentuk v(100) atau s:p
			ini adlh bentuk s atau i maintype saja, tanpa subtype dan max size/len
			'''			
			# maintype = 'string' if maintype == 'varchar' else maintype
			# utk relationship kita gak generate faker...
			# django foreign key adlh main type, kita allow sbg integer
			skipme = maintype in django_relationship_fields
			# atau yg gak ada/perlu fakernya
			# skipme = skipme or (maintype in ['image', 'blob', 'auto'])
			# jk field = id,auto maka jadi KeyError bantu_sql wkt: item = kwargs[col.label]
			# skipme = skipme or (maintype in ['blob', 'auto'])
			skipme = skipme or (maintype in ['blob'])
			# ternyata image bisa gunakan url image = string...

			# mapping_ucsv_column_type_2_fakesey_number = maintype
			# if mapping_ucsv_column_type_2_fakesey_number == 'integer':
			# 	mapping_ucsv_column_type_2_fakesey_number = 'random_int'

			if skipme:
				kembali = None
				print(f'	SKIPPING >>>2/ bentuk [nama={node.label},type={maintype}]', node)
			else:
				'''
				satu per satu konversi dari ucsv column type di grammar.py
				ke field di fakesey
				'''
				print(f'	>>>2/ bentuk [nama={node.label},type={maintype}]', node)

				if (hasattr(node, 'auto_increment') and node.auto_increment==True) \
					or (maintype == 'auto' and (node.label == 'id' or node.label == '_id')):
					# print('...masuk autoincrement...')
					if not auto_increment.get_used(): 
						if hasattr(node, 'initial_value'):
							nilai = int(node.initial_value)
							kembali = auto_increment.init(nilai)
						else:
							auto_increment.set_used()
							kembali = auto_increment()
					else:						
						kembali = auto_increment()
						
				elif maintype == 'django_foreign_key':
					'''
					bisa juga generate uuid
					'''
					kembali = getattr(faker_instance, 'generate') ('random_int', 0)

				elif maintype == 'integer':
					kembali = getattr(faker_instance, 'generate') ('random_int', 0)
				
				elif maintype == 'boolean':
					kembali = getattr(faker_instance, 'generate') ('pybool')
					# True dan False => true, false
					kembali = 'true' if kembali else 'false'

				elif maintype == 'image':
					lebar = 600
					tinggi = 400
					if hasattr(node, 'lebar'):
						lebar = int(node.lebar)
					if hasattr(node, 'tinggi'):
						tinggi = int(node.tinggi)
					kembali = getattr(faker_instance, 'generate') ('image_url', width=lebar, height=tinggi)
					kembali = f"'{kembali}'"

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

				elif nama_kolom.lower() == 'username' or nama_kolom.lower() == 'user_name':
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

				elif nama_kolom.lower() == 'password':
					'''
					https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html#faker.providers.misc.Provider.password
					password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
					'''
					panjang=10
					kembali = getattr(faker_instance, 'generate') ('password', length=panjang)

				elif 'date' in nama_kolom.lower() and maintype == 'string':
					'''
					'unix_time',
					'date_time',
					'iso8601',
					'date',
					'time',
					'''
					kembali = getattr(faker_instance, 'generate') ('iso8601')

				elif 'time' in nama_kolom.lower() and maintype == 'string':
					kembali = getattr(faker_instance, 'generate') ('date_time')

				elif 'title' in nama_kolom.lower():
					kembali = getattr(faker_instance, 'generate') ('sentence')

				elif 'description' in nama_kolom.lower():
					kembali = getattr(faker_instance, 'generate') ('text')

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
						print(f"""
						faker everything else:
						node {node}
						maintype {maintype}
						""")
						kembali = getattr(faker_instance, f'_{maintype}') ()

		if kembali is not None: # jangan lupa krn kembali bisa False dari pybool
			# print('kembali berjenis:', type(kembali))
			if isinstance(kembali, list):
				print('list:')
				print(kembali)
				print('maintype:')
				print(maintype)
				# input(' ketemu list... ')

			kwargs.update({
				node.label: kembali
			})

	
	print('>>> record =>', kwargs)
	if generate_object_instance:
		'''
		utk springboot hasilkan new Object(...)

		bantu_sbgql.py:89
				generate_object_instance = {}
				for field_no, field in enumerate(tbl.children, 1):
					transformer = lambda x: str(x)
					if field.type == 'array_of':
						transformer = lambda a: str(a).replace('[', 'open', 1).replace(']', 'close', 1).replace('open', 'new String[] {').replace('close', '}')
					generate_object_instance.update({
						field.label: {
							'no': field_no,
							'transformer': transformer,
						}
					})
		'''
		label_positions = sorted(generate_object_instance.items(), key=lambda x:x[1]['no'])		
		object_params = []
		for lp in label_positions:
			label = lp[0]
			if label in kwargs:
				print(f"""
				label position list = {label_positions}
				label [{label}] tidak ada dalam [{django_relationship_fields}]
				""")
				'''
				SKIPPING >>>2/ bentuk [nama=order,type=django_one_to_one] 
				AnyNode(allowNull=True, blank=True, foreignKeyOnDelete='models.CASCADE', hasConstraint=True, 
					label='order', oneToOne=True, relTo='Order', 
					type='django_one_to_one')
				File "/home/usef/work/ulibs/schnell/db/bantuan/generate_faker.py", line 415, in generate_faker
						transformed = transformer(kwargs[label])
				KeyError: 'order'
				'''
				transformer = lp[1]['transformer']
				transformed = transformer(kwargs[label])
				object_params.append(transformed)
		return ','.join([str(i) for i in object_params])

	return kwargs

