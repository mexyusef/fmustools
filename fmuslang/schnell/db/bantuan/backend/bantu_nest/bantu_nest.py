from app.printutils import indah3
from .common import filepath_output
from .model import gen_models
from .mkfile import gen_mkfile


def bantu_nest(RootNode, project_dir='input', need_program_output=False):
	indah3('bantu_nest', warna='white')
	tables = gen_mkfile(RootNode, project_dir=project_dir)
	gen_models(tables)
	if need_program_output:
		return filepath_output
	return f'output: {filepath_output}'
