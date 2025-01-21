from app.fileutils import (
	file_content,
	append_file,
)
from ..config import output_django_mkfile


def append_entry(tablename, body, entry_id='models.py'):
	"""
	/apps/{tablename}/models.py
	"""
	start='--%'
	end='--#'
	header = f'/apps/{tablename}/{entry_id}'
	entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
	append_file(output_django_mkfile, entry_model)
	return entry_model

