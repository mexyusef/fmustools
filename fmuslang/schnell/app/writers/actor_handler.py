from schnell.app.fileutils import file_content, file_lines
from .config import actor_file


CACHED_RESULT = []


def get_all_actors(reload=False):
	global CACHED_RESULT

	if reload:
		CACHED_RESULT = []

	if not CACHED_RESULT:
		CACHED_RESULT = file_lines(actor_file)
		# for filepath in zau_all_filepaths(0,999):
		# 	if isfile(filepath):
		# 		CACHED_RESULT += get_words_in_file(filepath)

	return CACHED_RESULT


def actor_name(number, base=0):
    number = int(number) # just in case
    return get_all_actors()[number+base]
