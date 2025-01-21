
class Record:
	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		# print('terima', kwargs, 'atau terima args?', args)

