# from fakesey import Fakesey
from fakesey import palsu
from mapper import Types_to_Faker_Mapper
from record import Record

def generate_sql(configuration, tablename, columntypes, columnnames):

	# palsu = Fakesey()
	# if 'locale' in configuration:
	# 	print('gunakan locale:', configuration['locale'])
	# 	palsu = Fakesey(locale=configuration['locale'])

	prefix = f'INSERT INTO `{tablename}` ('
	middle = ') VALUES ('
	suffix = ');'		
	total = int(configuration['generate:number'])
	records = []

	for counter in range(total):
		values = list( map( lambda record: Types_to_Faker_Mapper(palsu, record, configuration), columntypes) )
		# first = f"""{prefix} {', '.join(columnnames)} {middle} "{getattr(palsu, f'_{columntypes[0]}') ()}" {suffix}"""
		sql_statement = f"""{prefix} {', '.join(columnnames)} {middle} {', '.join(values)} {suffix}"""
		print(sql_statement) # insert into ...
		# name_values.append( list(zip(columnnames, values)) )
		strippedquotes_names = [item.replace('"', '') for item in columnnames]
		strippedquotes_values = [item.replace('"', '') for item in values]
		kwargs = dict(zip(strippedquotes_names, strippedquotes_values))
		# print(kwargs)
		records.append(Record(**kwargs))

	return records
