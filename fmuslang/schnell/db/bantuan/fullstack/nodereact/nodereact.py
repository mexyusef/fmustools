# from creator.bindings import process_fmus, run_fmus
from .common import filepath_output
from .model import gen_models
from .mkfile import gen_mkfile

def generate_pg_antd(RootNode, project_dir='input', need_program_output=False):
	configuration = gen_mkfile(RootNode, project_dir=project_dir)
	gen_models(configuration)
	if need_program_output:
		return filepath_output
	return f'output: {filepath_output}'
