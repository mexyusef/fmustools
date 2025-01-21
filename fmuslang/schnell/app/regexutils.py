import re


def convert_to_valid_version(string):
    """
	Converts any string to a version string with only letters, digits, underscore, and dot.
	
	original_string = "This is a string with punctuations: !@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
	valid_version = convert_to_valid_version(original_string)
	print(valid_version)

	"""
    pattern = r'[^a-zA-Z0-9_.]+'
    return re.sub(pattern, '', string)


def detect_format(input_str, delimiter='/'):
	"""
	(code, result_tuple)
	code: 1 = tokens, 2 = tokens+temp, 3 = tokens+temp+model
	"""
	# digit1
	m = re.match(r'^(\d{1,4})\s*' + delimiter + '(.*)', input_str)
	if m:
		# return (1, (int(m.group(1)), None, None)), m.groups()
		return 1, m.groups()

	# digit1, digit2
	m = re.match(r'^(\d{1,4}),\s*([01]\.\d{1,3})\s*' + delimiter + '(.*)', input_str)
	if m:
		# return (2, (int(m.group(1)), float(m.group(2)), None)), m.groups()
		return 2, m.groups()

	# digit1, digit2, string
	m = re.match(r'^(\d{1,4}),\s*([01]\.\d{1,3}),\s*([\w\-]+)\s*' + delimiter + '(.*)', input_str)
	if m:
		# return (3, (int(m.group(1)), float(m.group(2)), m.group(3))), m.groups()
		return 3, m.groups()

	return (0, None)
# print('#1')
# print(detect_format('50/ini tokens saja'))
# print('#2')
# print(detect_format('512, 0.5/ini tokens dan temp'))
# print('#3')
# print(detect_format('1024, 0.8, gpt3-small/ini token, temp, model'))
# print('#4')
# print(detect_format('2048 (1024, 0.5)/ini harusnya gagal pake kurung'))
# print('#5')
# print(detect_format('512, 0.5, gpt3-big/ini juga lengkap token, temp model'))
# print(detect_format('100/ini harusnya temperature'))
# #1
# (1, ('50', 'ini tokens saja'))
# #2
# (2, ('512', '0.5', 'ini tokens dan temp'))
# #3
# (3, ('1024', '0.8', 'gpt3-small', 'ini token, temp, model'))
# #4
# (False, None)
# #5
# (3, ('512', '0.5', 'gpt3-big', 'ini juga lengkap token, temp model'))
# (1, ('100', 'ini harusnya temperature'))

def dimulai_digit(string, delimiter='/'):
	"""
	Check if a string starts with a digit followed by a delimiter.
	
	Args:
	- string (str): The string to check.
	- delimiter (str): The delimiter character that should follow the digit. Default is '/'.
	
	Returns:
	- A tuple containing (digit, therest) if the string starts with a digit followed by the delimiter, 
	  or (False, None) otherwise.
	"""
	if len(string) > 1:
		first_char = string[0]
		second_char = string[1]
		if first_char.isdigit() and second_char == delimiter:
			return (string.split(delimiter)[0], string.split(delimiter, 1)[1])
	return (False, None)


def ukuranhuruf_posy(text, pengali=0.8, ukuranhuruf=40, pattern = r"<(#?(\.?\d+)(?:,#?(\.?\d+))*)>?(.+)"):
	r"""
	pengali = posy, dimana letak text di dalam meme, default 20% dari bawah (0.8)
	ukuranhuruf = default 40

	pattern = r"<(#?(\.?\d+)(?:,#?(\.?\d+))*)>?(.+)"
	# <#66,.3>satu|<#30>dua|tiga|<.8>empat|<.1,#50>lima
	# mg ('#66,.3', '66', '.3', 'satu')
	# mg ('#30', '30', None, 'dua')
	# item: tiga
	# mg ('.8', '.8', None, 'empat')
	# mg ('.1,#50', '.1', '50', 'lima')
	"""
	if text.startswith('<') and '>' in text:
		m = re.match(pattern, text)
		if m:
			print('getxy matching chevrons:', m.groups())
			# ('#66,.3', '66', '.3', 'satu')
			_, dua, tiga, empat = m.groups()
			if '.' in dua:
				# jk float di dua, artinya pengali
				pengali = float(dua)
			else:
				# jk int di dua, artinya ukuranhuruf
				ukuranhuruf = int(dua)
			if tiga:
				if '.' in tiga:
					# jk float di dua, artinya pengali
					pengali = float(tiga)
				else:
					# jk int di dua, artinya ukuranhuruf
					ukuranhuruf = int(tiga)
			text = empat
	# else:
	# 	pass
	return text, pengali, ukuranhuruf
