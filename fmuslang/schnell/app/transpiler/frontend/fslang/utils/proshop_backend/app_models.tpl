__MODEL_IMPORTS__

class __TABLENAME_CASE__(__TABLE_BASEMODEL__):
__TABLE_FIELDS__

	class Meta:
		app_label = '__TABLENAME_LOWER__'
		db_table = '__TABLENAME_PLURAL_LOWER__'

	def __str__(self):
		return self.__FIRST_FIELD__
