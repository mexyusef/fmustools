from .allownull import allownull
from .auto_now_add import auto_now_add
from .auto_increment import auto_increment
from .auto_now import auto_now
from .blank import blank
from .defaultvalue import defaultvalue
from .default import default
from .db_index import db_index
from .decimal_places import decimal_places
from .editable import editable
from .foreignkeyondelete import foreignkeyondelete
from .lower import lower
from .max_digits import max_digits
from .max_length import max_length
from .min_length import min_length
from .primarykey import primarykey
from .relto import relto
from .related_name import related_name
from .references import references
from .referenceskey import referenceskey
from .requiredvalidation import requiredvalidation
from .trim import trim
from .unique import unique
from .upper import upper
from .values import values
from .verbose_name import verbose_name
from ..ui import form_item_string, form_item_image, form_item_integer
from schnell.app.typemapper import type_mapper_by_provider
from schnell.app.appconfig import libpohon_data
import_part = libpohon_data['import_part']


def get_tipe_kolom(column, provider):
	if provider not in type_mapper_by_provider:
		raise Exception(f"""[app.libpohon.handlers.__init__]
		provider = {provider}
		tidak ada dalam type mapper:
		{', '.join(type_mapper_by_provider.keys())}
		""")
	mapper = type_mapper_by_provider.get(provider)
	# print(f'provider {provider} => mapper:', mapper)
	tipe_kolom = mapper.get(column.type, column.type)
	# UI process
	if provider in ['react_bootstrap_form1']:
		tipe_kolom = tipe_kolom \
			.replace('__COLUMN_TITLE__', column.label.title()) \
			.replace('__COLUMN_LOWER__', column.label.lower()) \
			.replace('__COLUMN_CAP__', column.label.capitalize()) \
			.replace('__COLUMN_UPFIRST__', column.label[0].upper()+column.label[1:]) \
			.replace('__COLUMN_ASIS__', column.label)
	# jk ada subtype
	# AnyNode(hasConstraint=False, label='images', subtype='string', type='array_of')
	# images: { type: Array(__SUBTYPE__),  },
	# images: __SUBTYPE__[];
	if column.type == 'array_of':
		if provider == 'django':
			'''
			django/JSONField gak perlu subtype
			'''
			jsonfield_import = 'from django.contrib.postgres.fields import JSONField'
			if jsonfield_import not in import_part:
				import_part.append(jsonfield_import)
			tipe_kolom = tipe_kolom.replace('ARRAY', 'JSONField').replace('(__SUBTYPE__)','')
		elif hasattr(column, 'subtype'):
			subjenis = column.subtype
			subjenis_terpetakan = mapper.get(subjenis, subjenis)
			tipe_kolom = tipe_kolom.replace('__SUBTYPE__', subjenis_terpetakan)
	elif column.type == 'empty_array':
		if provider == 'django':
			jsonfield_import = 'from django.contrib.postgres.fields import JSONField'
			if jsonfield_import not in import_part:
				import_part.append(jsonfield_import)
			tipe_kolom = tipe_kolom.replace('ARRAY', 'JSONField')
	elif column.type == 'django_foreign_key':
		# AnyNode(
		# foreignKey=True,
		# foreignKeyOnDelete='models.CASCADE',
		# hasConstraint=False,
		# label='category',
		# relTo='Category',
		# type='django_foreign_key')
		tipe_kolom = tipe_kolom.replace('ModelRujukan', column.relTo)
	return tipe_kolom


def tipe_nama_kolom(column, provider):
	return get_tipe_kolom(column, provider), column.label


def tipe_kolom_setara_atribut_kolom(column, provider):
	"""
	agar hasilkan
	namakolom: { type: Array, required: false, default: [] },
	klo django: namakolom = Array(attrs...)
	type: Array
	shg bisa digabungkan dg column_attrs
	"""
	kembali = ''
	jenis = get_tipe_kolom(column, provider)
	if provider == 'default':
		kembali += ''
	elif provider == 'nest_mongo':
		kembali += f'type: {jenis}'
	return kembali


def column_attrs(column, provider, tablename=None):
	colattrs = []
	# relTo dan relationship lain hrs mendahului col attrs lain
	if hasattr(column, 'relTo'):
		res = relto(column, provider, tablename)
		if res:
			colattrs.append(res)
	if hasattr(column, 'allowNull'):
		res = allownull(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'auto_increment'):
		res = auto_increment(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'auto_now'):
		res = auto_now(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'auto_now_add'):
		res = auto_now_add(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'blank'):
		res = blank(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'db_index'):
		res = db_index(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'decimal_places'):
		res = decimal_places(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'default'):
		res = default(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'defaultValue'):
		res = defaultvalue(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'editable'):
		res = editable(column, provider)
		if res:
			colattrs.append(res)

	if hasattr(column, 'lower'):
		res = lower(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'max_length'):
		res = max_length(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'max_digits'):
		res = max_digits(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'min_length'):
		res = min_length(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'primaryKey'):
		res = primarykey(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'references'):
		res = references(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'referencesKey'):
		res = referenceskey(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'related_name'):
		res = related_name(column, provider)
		if res:
			colattrs.append(res)
	# on_delete hrs setelah/dibelakang dari relation-to
	if hasattr(column, 'foreignKeyOnDelete'):
		res = foreignkeyondelete(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'requiredWithValidation'):
		res = requiredvalidation(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'trim'):
		res = trim(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'unique'):
		res = unique(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'upper'):
		res = upper(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'values'):
		res = values(column, provider)
		if res:
			colattrs.append(res)
	if hasattr(column, 'verbose_name'):
		res = verbose_name(column, provider)
		if res:
			colattrs.append(res)
	return colattrs
