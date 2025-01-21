import datetime, time
from datetime import datetime as DT, timedelta, timedelta as TD


month2 = [
	'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
month3 = [
	'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
]


def iso():
	return datetime.datetime.now().isoformat()


def isofied():
	from .stringutils import replace_non_alpha
	return replace_non_alpha(datetime.datetime.now().isoformat())


def sekarang():
	return datetime.datetime.now()


def today():
	return datetime.datetime.today()


def today_ymd():
	"""
	1978-08-24
	"""
	return datetime.datetime.today().strftime('%Y-%m-%d')


def today_ydm():
	"""
	1978-24-08
	"""
	return datetime.datetime.today().strftime('%Y-%d-%m')


def today_mdy():
	"""
	08-24-1978
	"""
	return datetime.datetime.today().strftime('%m-%d-%Y')


def today_dmy():
	"""
	24-08-1978
	"""
	return datetime.datetime.today().strftime('%d-%m-%Y')


def waktu_hms():
	return datetime.datetime.today().strftime('%H:%M:%S')


def jam_hms():
	return datetime.datetime.today().strftime('%H:%M:%S')


def jam_hm():
	return datetime.datetime.today().strftime('%H:%M')


def sejam(mulai):
	"""
	sejam = sudah_sejam (sejak mulai)
	"""
	return sekarang() >= mulai + timedelta(hours=1)


def sehari(mulai):
	"""
	mencek jika sehari sudah berlalu terhadap rujukan "mulai"
	sehari = sudah_sehari (sejak mulai)
	"""
	return sekarang() >= mulai + timedelta(hours=24)


def beda_shm(s=1,m=0,h=0):
	"""
	kembalikan datetime dg jarak h:m:s dari sekarang
	beda_shm() = 1 detik dari now
	"""
	return sekarang() + timedelta(hours=h, minutes=m, seconds=s)


def epoch():
	"""
	returns: float
	"""
	epoch_time = int(time.time())
	return epoch_time


def epoch_diff(start, end):
	"""
	returns: float
	"""
	return end - start


def int_len(myint):
	return len(str(abs(myint)))
  

def is_epoch_ms(epoch):
	"""
	is ms?
	seconds atau ms
	"""
	if int_len(epoch)==13:
		return True
	return False


def fmt(dt, format=None):
	if not format:
		return dt.strftime('%Y-%m-%d %H:%M:%S')
	return dt.strftime(format)


def epoch2dt(epoch, utc=True):
	"""
	coba cek:
	https://stackoverflow.com/questions/12400256/converting-epoch-time-into-the-datetime
	"""
	if is_epoch_ms(epoch):
		epoch = epoch / 1000
	if utc:
		return datetime.datetime.utcfromtimestamp(epoch)
	return datetime.datetime.fromtimestamp(epoch)


def epoch2dtstr(epoch, utc=True, format=None):
	"""
	2021-08-18 12:12:52
	current = epoch()
	epoch2dtstr(current)
	"""
	dt = epoch2dt(epoch, utc=utc)
	return fmt(dt, format=format)


def format_epoch_longer(epoch, utc=False):
	"""
	%A Monday
	%a monday	
	"""
	# return fmt_epoch('%A, %-m %B %Y, %-H:%M:%S', utc)
	format = '%A, %d %B %Y, %H:%M:%S'
	return fmt(epoch2dt(epoch, utc), format)


def year():
	return DT.now().year


def waktu(mode='year'):
	"""
	https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
	"""
	if mode=='year':
		return DT.now().year
	elif mode=='month':
		return DT.now().month
	elif mode=='day':
		return DT.now().day
	elif mode=='hour':
		return DT.now().hour
	elif mode=='minute':
		return DT.now().minute
	elif mode=='second':
		return DT.now().second


def timestamp_for_file():
	tanggal = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S, %A')
	baris = f"[{tanggal}]"
	return baris


def doy():
	_doy = datetime.datetime.now().strftime('%j')
	return _doy


def jam():
	_doy = datetime.datetime.now().strftime('%H')
	return _doy


def menit():
	_doy = datetime.datetime.now().strftime('%M')
	return _doy


# https://stackoverflow.com/questions/33987060/python-context-manager-that-measures-time
from time import perf_counter
from contextlib import contextmanager


@contextmanager
def catchtime() -> float:
	start = perf_counter()
	yield lambda: perf_counter() - start


def lama_operasi(fungsi):
	with catchtime() as t:
		fungsi()
	return f"{t():.4f}"


def seconds_till_next_minutes(nextminute=1, millisecond=False, microsecond=False):
	"""
	misal 3.48 pengen capai 4.30
	nextminute = 30
	skrg+TD(minutes=nextminute) hasilkan 3:48:00+00:30:00 = 4:18:00
	replace min=30, sec=0, us=0 hasilkan: 4:30:00.000000
	"""
	skrg = DT.now()
	res = ( ( skrg+TD(minutes=nextminute) ).replace(minute=nextminute,second=0,microsecond=0) - skrg ).seconds
	if millisecond:
		return res * 1000
	elif microsecond:
		return res * 1000 * 1000
	return res


def seconds_till_next_hour(nexthour=1, millisecond=False, microsecond=False):
	"""
	https://stackoverflow.com/questions/52808344/get-number-of-seconds-until-the-start-of-the-next-hour
	https://stackoverflow.com/questions/45986035/seconds-until-end-of-day-in-python
	"""
	skrg = DT.now()
	# Datetime_object.replace(year,month,day,hour,minute,second,microsecond,tzinfo)
	res = ( ( skrg+TD(hours=nexthour) ).replace(minute=0,second=0,microsecond=0) - skrg ).seconds
	if millisecond:
		return res * 1000
	elif microsecond:
		return res * 1000 * 1000
	return res


def format_datetime(format_string, reference=None):
	"""
	create python function to manipulate date time, called format_datetime with my own convention
	like typical date format functions but with my own keyword (so that i can memorize it easily).
	keywords with their meanings are: 

	d=day, 
	m=month,
	y=year, 
	S=millisecond, 
	e=epoch-seconds, 
	E=epoch-milliseconds,
	(time are always zero padded)
	h=hour, 
	n=minute, 
	s=second 
	f=day names like Sun, Mon, Tue
	F=day names in full: Sunday, Monday, Tuesday
	j=month names like Jan, Feb, Mar
	J=month names in full: January, February, March

	format_datetime(format, reference=<default to now>)
	format_datetime('dd-mm-yyyy') => 18-03-2024
	format_datetime('dd-mm-yyyy', '25/12/1997=dd/mm/yyyy') => 25-12-1997
	here in reference string, i can pick arbitrary date then its format specifier with '=dd/mm/yyyy' (there's an equal sign in the middle between the datetime string and its format specifier).
	format_datetime('dd J yyyy') => 18 March 2024
	"""
	# Define the mapping of your custom keywords to strftime directives
	format_map = {
		'dd': '%d',
		'mm': '%m',
		'yyyy': '%Y',
		'S': '%f',  # Represents microseconds, not milliseconds
		'hh': '%H',
		'nn': '%M',
		'ss': '%S',
		'f': '%a',  # Fri
		'F': '%A',  # Friday
		'j': '%b',  # Jan
		'J': '%B',  # January
	}

	# Replace your custom keywords with the corresponding strftime directives
	for key, value in sorted(format_map.items(), key=lambda x: len(x[0]), reverse=True):
		format_string = format_string.replace(key, value)

	# If a reference is provided, parse it
	if reference:
		# Extract the date string and its format
		date_str, date_format = reference.split('=')
		# Replace your custom keywords in the reference format
		for key, value in sorted(format_map.items(), key=lambda x: len(x[0]), reverse=True):
			date_format = date_format.replace(key, value)
		# Print the values for debugging
		print(f"date_str: {date_str}, date_format: {date_format}")
		# Parse the reference date
		reference_date = datetime.datetime.strptime(date_str, date_format)
	else:
		# Use the current date and time if no reference is provided
		reference_date = datetime.datetime.now()

	# Return the formatted date
	return reference_date.strftime(format_string)


def test_format_datetime():
	print(format_datetime('dd-mm-yyyy'))  # => 18-03-2024
	print(format_datetime('dd-mm-yyyy', '25/12/1997=dd/mm/yyyy'))  # => 25-12-1997
	print(format_datetime('dd J yyyy'))  # => 18 March 2024


if __name__ == '__main__':
	with catchtime() as t:
		import time
		time.sleep(1)

	print(f"Execution time: {t():.4f} secs")
