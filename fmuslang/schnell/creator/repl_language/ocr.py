from schnell.ai.autolib.ocr import capture_to_text
from schnell.app.printutils import indah3, indah4
from schnell.app.stringutils import multiple_spaces_to_single_space
from schnell.app.utils import GOOGLESEARCH, buka
from schnell.app.envvalues import datadir_
from schnell.app.dirutils import joiner
from schnell.app.fileutils import file_write, prepend_datetime_to_file, file_append
from schnell.app.datetimeutils import timestamp_for_file


def ocr(google_search=False):
	result, output_file = capture_to_text()
	indah4('='*40 + ' ' + output_file, warna='green')
	indah3(result, warna='white')
	indah4('='*40, warna='green')

	# simpan hasil output ke file
	filepath = joiner(datadir_(), 'ocr-data', 'ocr.txt')
	# prepend_datetime_to_file(filepath)
	# tanggal = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S, %A')
	# baris = f"[{tanggal}]"
	file_append(filepath, f"\n{timestamp_for_file()}\n{result}\n")

	if google_search and result:
		__TEXTPLACEHOLDER__ = multiple_spaces_to_single_space(result.strip(), replacer='+')					
		# code = text.removeprefix('g/').strip()
		# __TEXTPLACEHOLDER__ = code.replace(' ', '+')
		alamat = GOOGLESEARCH.replace('__TEXTPLACEHOLDER__', __TEXTPLACEHOLDER__)

		file_append(filepath, f'''\nGoogle searching "{__TEXTPLACEHOLDER__}"\n''')

		buka(alamat)
